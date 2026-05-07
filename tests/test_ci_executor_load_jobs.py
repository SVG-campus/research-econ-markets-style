"""CI executor _load_jobs: skip disabled rows."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_ci_execute(root: Path):
    mod_path = root / "scripts" / "ci_execute_smoke_nb.py"
    spec = importlib.util.spec_from_file_location("ci_execute_smoke_nb", mod_path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_load_jobs_includes_three_smoke_notebooks() -> None:
    root = Path(__file__).resolve().parents[1]
    mod = _load_ci_execute(root)
    jobs = mod._load_jobs(root)
    paths = {p.resolve() for p, _ in jobs}
    assert root.joinpath("notebooks", "SMOKE_LAYER_A.ipynb").resolve() in paths
    assert root.joinpath("notebooks", "SMOKE_BOOTSTRAP.ipynb").resolve() in paths
    assert root.joinpath("notebooks", "SMOKE_IMPORTS.ipynb").resolve() in paths


def test_load_jobs_excludes_disabled_placeholder() -> None:
    root = Path(__file__).resolve().parents[1]
    mod = _load_ci_execute(root)
    jobs = mod._load_jobs(root)
    rels = {p.relative_to(root).as_posix() for p, _ in jobs}
    assert "notebooks/CHARTER_PLACEHOLDER.ipynb" not in rels
