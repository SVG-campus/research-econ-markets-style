# Preregistration template — `research-econ-markets-style`

**Pillar:** `research-econ-markets-style`  
**Title:** Economics, markets, style signals

## Charter (one paragraph)

Blend macro/micro text and tabular signals with honest nulls and no silent look-ahead.

## Primary question (Layer A)

- **Question:** _What measurable difference do we expect under the stated hypothesis?_
- **Primary metric:** _e.g. mean delta, AUC, correlation, regret …_
- **Direction / threshold:** _pre-specify sign or minimal effect size before peeking._

## Null / negative controls

- **Null model:** _e.g. y-shuffle, permutation, time-shift, placebo instrument …_
- **Caps:** read `runs/smoke.yaml` (`n_perm_max`, `n_boot_max`) for local smoke; raise only on Kaggle/HF Jobs with a new `run_id`.

## Truth scope & ethics

- **Scope:** observational / simulated / scenario — _not_ universal causal claims unless design supports it.
- **Data rights:** cite Hub/Kaggle dataset cards; no redistribution beyond their licenses.

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact.
