# Run configuration

`smoke.yaml` caps stochastic budgets for **local smoke** and CI-friendly notebooks. Full archival runs override via env or a `runs/full.yaml` (add when ready) and must log seeds.

`ci_notebooks.yaml` lists notebooks executed headlessly in GitHub Actions after `pytest` (see `scripts/ci_execute_smoke_nb.py`).

On **CI failure**, GitHub Actions uploads `notebooks/`, `runs/`, and `scripts/ci_execute_smoke_nb.py` as a downloadable artifact for debugging.

Optional rows may set `enabled: false` so future charter notebooks stay listed without running in CI until they are stable headless.

**`notebooks/CHARTER_SHELL.ipynb`** (minimal preamble + run card) runs in CI **after** the three `SMOKE_*.ipynb` notebooks (see [`ci_notebooks.yaml`](ci_notebooks.yaml) for order) and **before** `CHARTER_EXTENDED_LIGHT`, **`CHARTER_LAYER_A_MULTIDRAW_SMOKE`**, and the domain stream charter—extend it as the charter grows.

**`notebooks/CHARTER_EXTENDED_LIGHT.ipynb`** (synthetic mean + run card) runs next as a light Layer A–shaped check.

**`notebooks/CHARTER_LAYER_A_MULTIDRAW_SMOKE.ipynb`** — synthetic two-sample pooled-label **permutation** null (Hub-free), capped by `runs/smoke.yaml`; runs **before** the domain stream charter row in [`ci_notebooks.yaml`](ci_notebooks.yaml).

**`notebooks/CHARTER_YELP_STREAM_SMOKE.ipynb`** runs next: small streaming slice of `Yelp/yelp_review_full` + y-shuffle null + run card (sentiment proxy only).

**`FUTURE_CHARTER_SLOT.ipynb`** is listed disabled with **no** committed file: replace that row with a real path when you add a heavier charter notebook, verify headless execution locally, then set `enabled: true`.

## Promotion audit (canonical numbers)

Template: [`runs/promotion_audit.example.yaml`](promotion_audit.example.yaml) — copy the `example_entry` shape when recording a promotion; keep **`trace_run_ids`** aligned with CI notebook `run_id` fields (multidraw smoke + domain stream charter); fill **`commit_sha`** (`github.sha` in Actions, `git rev-parse HEAD` locally), optional **`ci_run_url`**, and run-card **seed / null** fields before treating metrics as canonical. Full gate: [meta `PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research/blob/main/docs/PROMOTION_CHECKLIST.md) (meta hub; historical remote name **Research-Apriori**).
