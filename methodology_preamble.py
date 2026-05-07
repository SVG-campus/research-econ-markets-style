"""Notebook / script preamble: load `runs/smoke.yaml`, set seeds, optional `research_methods`.

Usage at top of a Jupyter notebook:

    from methodology_preamble import init_notebook, build_run_card, assert_run_card
    info = init_notebook()
    rc = build_run_card(
        run_id="nb_001",
        hypothesis="…",
        metric="…",
        null="y_shuffle",
        truth_scope="…",
        seed=info["seed"],
    )
    assert_run_card(rc)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import yaml

PILLAR = "research-econ-markets-style"

_ROOT = Path(__file__).resolve().parent
_REQUIRED = ("run_id", "pillar", "seed", "hypothesis", "metric", "null", "truth_scope")


def _smoke_yaml_path() -> Path:
    """Resolve ``runs/smoke.yaml`` for repo checkouts and ``py-modules`` installs (CI imports from site-packages)."""
    candidates: list[Path] = []
    seen: set[Path] = set()

    def add(p: Path) -> None:
        q = p.resolve()
        if q not in seen:
            seen.add(q)
            candidates.append(q)

    add(Path.cwd() / "runs" / "smoke.yaml")
    add(_ROOT / "runs" / "smoke.yaml")
    here = Path.cwd().resolve()
    for _ in range(8):
        add(here / "runs" / "smoke.yaml")
        if here.parent == here:
            break
        here = here.parent
    for p in candidates:
        if p.is_file():
            return p
    raise FileNotFoundError(
        "runs/smoke.yaml not found (searched cwd, parents, package dir); "
        "run from pillar repo root or keep runs/smoke.yaml next to methodology_preamble.py."
    )


def load_smoke_caps() -> dict[str, Any]:
    path = _smoke_yaml_path()
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def init_notebook(*, extra_seed_offset: int = 0) -> dict[str, Any]:
    caps = load_smoke_caps()
    base = int(caps["seeds"]["global_default"])
    seed = base + int(extra_seed_offset)
    np.random.seed(seed)
    out: dict[str, Any] = {
        "pillar": PILLAR,
        "seed": seed,
        "methodology_caps": caps["methodology_caps"],
        "run_card_required": caps.get("run_card", {}).get("required_before_promotion", True),
    }
    try:
        from research_methods.seeds import set_global_seeds

        out["research_methods_seeds"] = set_global_seeds(seed)
    except ImportError:
        out["research_methods_seeds"] = None
        out["research_methods_hint"] = (
            "Install meta repo editable: pip install -e <path-to-Research-Apriori>"
        )
    return out


def _minimal_validate(card: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    for k in _REQUIRED:
        if k not in card or card[k] in (None, ""):
            errs.append(f"missing_or_empty:{k}")
    if "seed" in card and not isinstance(card["seed"], int):
        errs.append("seed_must_be_int")
    return errs


def build_run_card(
    *,
    run_id: str,
    hypothesis: str,
    metric: str,
    null: str,
    truth_scope: str,
    seed: int,
) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "pillar": PILLAR,
        "seed": seed,
        "hypothesis": hypothesis,
        "metric": metric,
        "null": null,
        "truth_scope": truth_scope,
    }


def assert_run_card(card: dict[str, Any]) -> None:
    errs = _minimal_validate(card)
    if errs:
        raise ValueError(errs)
    try:
        from research_methods.run_card import validate_run_card

        errs2 = validate_run_card(card)
    except ImportError:
        return
    if errs2:
        raise ValueError(errs2)
