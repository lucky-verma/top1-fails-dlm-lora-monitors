# When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs

<p align="center">
  <a href="https://arxiv.org/abs/2606.24119"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2606.24119-b31b1b.svg"></a>
  <a href="https://doi.org/10.48550/arXiv.2606.24119"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.48550%2FarXiv.2606.24119-blue.svg"></a>
  <a href="results/README.md"><img alt="Artifacts" src="https://img.shields.io/badge/Artifacts-results-green.svg"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/Code-Apache--2.0-3776ab.svg"></a>
  <a href="CITATION.cff"><img alt="Citation" src="https://img.shields.io/badge/Citation-CFF%201.2.0-green.svg"></a>
</p>

Public code and result-artifact repository for the paper **"When Top-1 Fails:
Calibrating LoRA Monitors for Masked Diffusion LMs"** by Lucky Verma
(Independent Researcher) and Pratik Yadav (University of Maryland, Baltimore
County).

Paper: [arXiv:2606.24119](https://arxiv.org/abs/2606.24119) |
[DOI](https://doi.org/10.48550/arXiv.2606.24119) |
[PDF](https://arxiv.org/pdf/2606.24119) |
[Artifacts](results/README.md).

This repository holds the reference logging/checking scripts and the sanitized
aggregate result artifacts that back every table and figure (under `results/`). See
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

## Quick Start

The two scripts are standard-library only (Python 3.10+); there is nothing to
install.

```bash
git clone https://github.com/lucky-verma/top1-fails-dlm-lora-monitors.git
cd top1-fails-dlm-lora-monitors

# Summarize the bundled example monitor log:
python3 scripts/check_monitor_log.py examples/example_monitor_log.jsonl
```

Output (the example illustrates the paper's effect — the legacy top-1 warning
fires while the max-gradient inspection trigger does not):

```json
{
  "first_step": 0,
  "last_step": 11,
  "max_grad_inspection_trigger_50": false,
  "max_grad_norm": 28.2,
  "max_top1_token_freq": 0.91,
  "n_steps_logged": 2,
  "top1_warning_legacy_threshold_0p5": true
}
```

Append a monitor record from your own DLM-LoRA training step:

```bash
python3 scripts/reference_logger.py my_run.jsonl \
  --step 200 --loss 1.83 --max-grad-norm 41.2 \
  --top1-token-freq 0.62 --mask-ratio 0.40 \
  --rank 64 --model-family llada
```

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
  journal={arXiv preprint arXiv:2606.24119},
  doi={10.48550/arXiv.2606.24119},
  url={https://arxiv.org/abs/2606.24119},
  eprint={2606.24119},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```

## License

Code in this repository is released under Apache-2.0. The released data
artifacts under `results/` are CC-BY-4.0.
