# Economics, markets, style signals

**Org:** `SVG-campus`  
**Slug:** `research-econ-markets-style`

## Contents

Notebooks live in `notebooks/` (imported from the legacy flat `Research` layout).

## Methods

See [METHODS.md](METHODS.md) and the preregistration template [docs/PREREG.md](docs/PREREG.md).

## Data registry

See [datasets.yaml](datasets.yaml) — prefer **streaming** Hub / Kaggle API over local mirrors.

## Validation

```bash
pip install -U pip
pip install -e ".[dev]"
pytest -q
python scripts/ci_execute_smoke_nb.py
```

Heavy runs: use Kaggle or Hugging Face Jobs (see meta repo `AGENTS.md`).

## Progress

See [docs/PROGRESS.md](docs/PROGRESS.md) for rubric-based **% proximity** to a defensible answer and links to shared methodology skills in the meta repo.

## Smoke caps

Notebook and local MC jobs should respect [runs/smoke.yaml](runs/smoke.yaml) (`n_boot_max`, `n_perm_max`); raise caps only on Kaggle/HF Jobs with a new `run_id`.

## CI notebooks (GitHub Actions)

The ordered list for headless execution lives in [runs/ci_notebooks.yaml](runs/ci_notebooks.yaml) and is run locally via `python scripts/ci_execute_smoke_nb.py` (same command as CI after `pytest`). By default CI runs **seven** enabled notebooks: **three** smokes (`SMOKE_*`), **`CHARTER_SHELL.ipynb`**, **`CHARTER_EXTENDED_LIGHT.ipynb`**, **`CHARTER_LAYER_A_MULTIDRAW_SMOKE.ipynb`** (Hub-free capped permutation), and **one pillar-specific domain Hugging Face stream charter** notebook (see `runs/ci_notebooks.yaml` and [runs/README.md](runs/README.md)). The disabled **`FUTURE_CHARTER_SLOT.ipynb`** row (no committed file) reserves the next heavy charter path—swap in a real `.ipynb` when ready, verify headless locally, then set `enabled: true`. On CI failure, GitHub Actions attaches `notebooks/`, `runs/`, and the executor script as a downloadable artifact.

## Notebook preamble (seeds + run card)

At the top of exploratory notebooks:

```python
from methodology_preamble import init_notebook, build_run_card, assert_run_card

info = init_notebook()
rc = build_run_card(
    run_id="nb_YYYYMMDD_01",
    hypothesis="…",
    metric="…",
    null="describe null (e.g. y_shuffle)",
    truth_scope="observational / scenario scope",
    seed=info["seed"],
)
assert_run_card(rc)
```

Install this repo editable (`pip install -e ".[dev]"`) so `research_methods` strict validation runs; otherwise minimal key checks still apply.
