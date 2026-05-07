"""Smoke-check notebooks + CI notebook list."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


def test_ci_notebooks_config_lists_smoke_paths() -> None:
    p = Path(__file__).resolve().parents[1] / "runs" / "ci_notebooks.yaml"
    assert p.is_file(), f"missing {p}"
    txt = p.read_text(encoding="utf-8")
    assert "SMOKE_LAYER_A.ipynb" in txt
    assert "SMOKE_BOOTSTRAP.ipynb" in txt
    assert "SMOKE_IMPORTS.ipynb" in txt
    assert "enabled: false" in txt


def test_smoke_notebook_contains_preamble() -> None:
    p = Path(__file__).resolve().parents[1] / "notebooks" / "SMOKE_LAYER_A.ipynb"
    assert p.is_file(), f"missing {p}"
    nb = json.loads(p.read_text(encoding="utf-8"))
    blob_parts: list[str] = []
    for c in nb.get("cells", []):
        if c.get("cell_type") != "code":
            continue
        src = c.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        blob_parts.append(src)
    blob = "\n".join(blob_parts)
    assert "init_notebook" in blob and "assert_run_card" in blob


def test_smoke_bootstrap_notebook_wired() -> None:
    p = Path(__file__).resolve().parents[1] / "notebooks" / "SMOKE_BOOTSTRAP.ipynb"
    assert p.is_file(), f"missing {p}"
    nb = json.loads(p.read_text(encoding="utf-8"))
    blob_parts: list[str] = []
    for c in nb.get("cells", []):
        if c.get("cell_type") != "code":
            continue
        src = c.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        blob_parts.append(src)
    blob = "\n".join(blob_parts)
    assert "boot_mean" in blob and "assert_run_card" in blob


def test_smoke_imports_notebook_wired() -> None:
    p = Path(__file__).resolve().parents[1] / "notebooks" / "SMOKE_IMPORTS.ipynb"
    assert p.is_file(), f"missing {p}"
    nb = json.loads(p.read_text(encoding="utf-8"))
    blob_parts: list[str] = []
    for c in nb.get("cells", []):
        if c.get("cell_type") != "code":
            continue
        src = c.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        blob_parts.append(src)
    blob = "\n".join(blob_parts)
    assert "init_notebook" in blob and "METHODS.md" in blob


def test_ci_notebooks_yaml_schema() -> None:
    p = Path(__file__).resolve().parents[1] / "runs" / "ci_notebooks.yaml"
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    assert data.get("version") == 1
    rows = data.get("notebooks")
    assert isinstance(rows, list) and len(rows) >= 1
    enabled_any = False
    for row in rows:
        if row.get("enabled", True) is False:
            continue
        enabled_any = True
        path = row.get("path")
        assert isinstance(path, str) and path.endswith(".ipynb")
        t = int(row.get("timeout_seconds", 120))
        assert 30 <= t <= 900
    assert enabled_any, "at least one notebook row must be enabled for CI"
