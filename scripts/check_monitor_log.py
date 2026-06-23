#!/usr/bin/env python3
"""Validate and summarize a JSONL monitor log."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = {"step", "loss", "max_grad_norm", "top1_token_freq", "mask_ratio"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("log", type=Path)
    args = ap.parse_args()
    rows = [json.loads(line) for line in args.log.read_text().splitlines() if line.strip()]
    if not rows:
        raise SystemExit("empty log")
    for i, row in enumerate(rows):
        missing = REQUIRED - set(row)
        if missing:
            raise SystemExit(f"row {i} missing {sorted(missing)}")
    max_grad = max(float(r["max_grad_norm"]) for r in rows)
    max_top1 = max(float(r["top1_token_freq"]) for r in rows)
    print(json.dumps({
        "n_steps_logged": len(rows),
        "first_step": rows[0]["step"],
        "last_step": rows[-1]["step"],
        "max_grad_norm": max_grad,
        "max_top1_token_freq": max_top1,
        "top1_warning_legacy_threshold_0p5": max_top1 >= 0.5,
        "max_grad_inspection_trigger_50": max_grad >= 50.0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
