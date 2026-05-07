"""Layer A smoke: bootstrap mean CI + run card."""

from __future__ import annotations

import numpy as np

from methodology_preamble import (
    PILLAR,
    assert_run_card,
    build_run_card,
    init_notebook,
)


def _boot_mean(
    arr: np.ndarray, n_boot: int, seed: int, alpha: float
) -> tuple[float, float, float]:
    rng = np.random.default_rng(seed)
    a = np.asarray(arr, dtype=float).ravel()
    boots = rng.choice(a, size=(n_boot, a.size), replace=True).mean(axis=1)
    lo_q = (alpha / 2) * 100
    hi_q = (1 - alpha / 2) * 100
    return float(a.mean()), float(np.percentile(boots, lo_q)), float(np.percentile(boots, hi_q))


def test_bootstrap_mean_respects_caps() -> None:
    info = init_notebook()
    caps = info["methodology_caps"]["bootstrap_mean_ci"]
    n_boot = min(300, int(caps["n_boot_max"]))
    alpha = float(caps["alpha"])
    rng = np.random.default_rng(info["seed"])
    x = rng.normal(loc=0.4, scale=1.0, size=45)
    m, lo, hi = _boot_mean(x, n_boot, info["seed"] + 5, alpha)
    assert lo <= m <= hi
    rc = build_run_card(
        run_id="layer_a_bootstrap_smoke",
        hypothesis="Synthetic mean with bootstrap CI smoke",
        metric=f"mean={m:.4f} ci=({lo:.4f},{hi:.4f}) n_boot={n_boot}",
        null="n/a",
        truth_scope="Synthetic RNG only",
        seed=info["seed"],
    )
    assert rc["pillar"] == PILLAR
    assert_run_card(rc)
