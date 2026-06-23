# Results artifacts — codebook

Sanitized aggregate JSON/CSV that back the tables and figures in *"When Top-1
Fails: Calibrating LoRA Monitors for Masked Diffusion LMs."* These are
group-level result artifacts (per-cohort summaries, bootstrap CIs, sweeps); raw
per-run cells are not part of this release. Files keep numeric diagnostics only;
local paths, host names, checkpoint/adapter paths, W&B metadata, and internal
process notes are removed.

## Directory layout

| Dir | Holds |
|---|---|
| `main/` | Headline results: top-1 fire vs collapse, max-gradient separation, held-out precision + bootstrap CI, step-k timing, pre-equilibrium saturation, gradient concentration, task probe |
| `controls/` | Autoregressive masked-CE controls (Pythia 160M–6.9B, Qwen3.5-9B) + AR scaling-law fits |
| `falsification/` | Single-axis intervention probes (PiSSA, GraLoRA, Stiefel, entropy bonus + lambda sweep, LR warmup, init perturbation, gating, clip, etc.) |
| `boundary/` | DLM scale/architecture boundary (Dream-7B, MDLM-OWT-130M, LLaDA-MoE-A1B, LLaDA2.1-mini transfer, long-horizon 2k) |
| `method-comparison/` | Method-comparison holdout masked-CE + multi-benchmark tables |
| `theory/` | Theory-diagnostic suites, SNR_eff, stable-rank, instability-equation fits, noise-floor, stat-rigor, budget-triage |
| `harness/` | lm-eval-harness smoke outputs (GSM8K / HumanEval / MMLU) for the in-domain masked-CE convergence sanity check |

## Run-id encoding

Run identifiers referenced inside the aggregates encode the configuration:

| Token | Meaning | Example |
|---|---|---|
| `r<N>` | LoRA rank | `r64` = rank 64 |
| `m<0pXX>` | mask ratio | `m0p40` = 0.40 |
| `s<N>` | seed | `s1337` |
| `lr<X>en<Y>` | learning rate | `lr3en5` = 3e-5 |
| `lambda<X>p<Y>` | entropy-bonus lambda | `lambda5p0` = 5.0 |

## Table / figure to file map

| Paper element | File |
|---|---|
| Fig. 1 / hero (top-1 vs max-grad) | `main/llada2_surface.json`, `main/cross_arch_top1_fire.json` |
| Fig. 2 / step-k precision sweep | `main/stepk_precision_sweep.json` |
| Pre-equilibrium top-1 figure | `main/preequilibrium_top1.json` |
| Rank-amp Gini / parameter routing | `main/gradient_concentration.json` |
| Held-out max-gradient decision rule | `main/heldout_precision.json` |
| Held-out bootstrap CI (reproducibility) | `main/heldout_bootstrap_ci.json` |
| Bootstrap rank-amp CI | `main/rank_amplification_ci.json` |
| Cross-family max-gradient stats | `main/cross_family_maxgrad_stats.json` |
| Task-performance probe (2x2 factorial) | `main/task_perf_3seed.json` |
| AR control surfaces | `controls/pythia_ar_surface.json`, `controls/qwen_ar_surface.json` |
| AR scaling law | `controls/ar_scaling_law_fit.json`, `controls/ar_scaling_law_supplement.json` |
| Scale-architecture boundary | `boundary/scale_boundary_summary.json` |
| LLaDA2.1-mini transfer / critical n=10 | `boundary/llada21_transfer.json` |
| MDLM / Dream cross-family top-1 | `main/cross_arch_top1_fire.json` |
| Method-comparison holdout | `method-comparison/method_holdout_n10.json`, `method-comparison/method_table.json` |
| Multi-benchmark masked-CE | `method-comparison/multibench_table.json`, `method-comparison/multibench_results.json` |
| Single-axis falsification probes | `falsification/*.json` |
| Theory-diagnostic suite | `theory/theory_suite.json` |
| SNR_eff(rho, rank) | `theory/snr_eff.json` |
| Cell noise floor | `theory/cell_noise_floor.json` / `.csv` |

Filenames are descriptive; the original internal run-tracking codes (k-IDs,
wave/batch tags, dates) have been dropped from the public release.
