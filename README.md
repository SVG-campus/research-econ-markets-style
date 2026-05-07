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
```

Heavy runs: use Kaggle or Hugging Face Jobs (see meta repo `AGENTS.md`).

## Progress

See [docs/PROGRESS.md](docs/PROGRESS.md) for rubric-based **% proximity** to a defensible answer and links to shared methodology skills in the meta repo.

## Smoke caps

Notebook and local MC jobs should respect [runs/smoke.yaml](runs/smoke.yaml) (`n_boot_max`, `n_perm_max`); raise caps only on Kaggle/HF Jobs with a new `run_id`.

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
