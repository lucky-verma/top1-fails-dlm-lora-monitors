#!/usr/bin/env python3
"""Minimal JSONL monitor logger for DLM-LoRA training runs.

The paper's diagnostic needs only a small set of fields: step, loss, LoRA
gradient norm, top-1 token frequency, mask ratio, and collapse/warning flags.
This logger deliberately avoids framework-specific state, checkpoints, W&B URLs,
local paths, prompts, completions, and credentials.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "step",
    "loss",
    "max_grad_norm",
    "top1_token_freq",
    "mask_ratio",
}


def append_record(path: Path, record: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_FIELDS - set(record))
    if missing:
        raise ValueError(f"missing required monitor fields: {missing}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("output", type=Path)
    ap.add_argument("--step", type=int, required=True)
    ap.add_argument("--loss", type=float, required=True)
    ap.add_argument("--max-grad-norm", type=float, required=True)
    ap.add_argument("--top1-token-freq", type=float, required=True)
    ap.add_argument("--mask-ratio", type=float, required=True)
    ap.add_argument("--rank", type=int)
    ap.add_argument("--model-family", default="unknown")
    ap.add_argument("--collapsed", action="store_true")
    args = ap.parse_args()
    append_record(args.output, vars(args) | {"output": None})


if __name__ == "__main__":
    main()
