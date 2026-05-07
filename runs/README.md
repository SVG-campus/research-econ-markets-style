# Run configuration

`smoke.yaml` caps stochastic budgets for **local smoke** and CI-friendly notebooks. Full archival runs override via env or a `runs/full.yaml` (add when ready) and must log seeds.

`ci_notebooks.yaml` lists notebooks executed headlessly in GitHub Actions after `pytest` (see `scripts/ci_execute_smoke_nb.py`).

On **CI failure**, GitHub Actions uploads `notebooks/`, `runs/`, and `scripts/ci_execute_smoke_nb.py` as a downloadable artifact for debugging.

Optional rows may set `enabled: false` so future charter notebooks stay listed without running in CI until they are stable headless.

The committed **`notebooks/CHARTER_SHELL.ipynb`** is a minimal charter-shaped template (preamble + run card only). It is listed with `enabled: false` by default—extend it with real Layer A cells, verify headless execution locally, then set `enabled: true`.
