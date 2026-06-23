# When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs

Public code and result-artifact repository for the paper **"When Top-1 Fails:
Calibrating LoRA Monitors for Masked Diffusion LMs"** by Lucky Verma and Pratik
Yadav.

The paper is on arXiv: (arXiv ID added on announcement). This repository holds
the reference logging/checking scripts and the sanitized aggregate result
artifacts that back every table and figure (under `results/`). See
[`results/README.md`](results/README.md) for the directory layout, run-id
encoding, and the table-to-file map.

## What This Paper Tests

The paper audits a transferred top-1-frequency collapse warning for LoRA
fine-tuning of masked diffusion language models. Across the reported DLM
cohorts, the top-1 warning fires on every configuration while observed collapse
is zero at the audited horizons. The paper therefore treats top-1 saturation as
a pre-equilibrium artifact in this setting and recommends family-local
inspection using max LoRA gradient norm instead.

## Repository Contents

- `scripts/reference_logger.py`: minimal JSONL logger for the monitor fields.
- `scripts/check_monitor_log.py`: small validator/summarizer for logged fields.
- `examples/example_monitor_log.jsonl`: tiny synthetic example for the scripts.
- `results/`: sanitized aggregate JSON/CSV artifacts backing every table and
  figure, grouped by purpose (`main/`, `controls/`, `falsification/`,
  `boundary/`, `method-comparison/`, `theory/`, `harness/`), with a
  `results/README.md` codebook.
- `CITATION.cff`: citation metadata.

## Scope

This is not a general DLM fine-tuning framework and not a universal detector. The
artifact is a reproducibility and inspection companion for the paper's scoped
claim: top-1 collapse warnings are not reliable PEFT early-warning signals in the
tested masked-DLM LoRA regimes, while max-gradient logs provide a more useful
family-local triage signal.

## Citation

If you use the scripts or released metrics, cite:

```bibtex
@article{verma2026top1fails,
  title={When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs},
  author={Verma, Lucky and Yadav, Pratik},
  year={2026},
  journal={arXiv preprint}
}
```

## License

Code in this repository is released under Apache-2.0. The released data
artifacts under `results/` are CC-BY-4.0.
