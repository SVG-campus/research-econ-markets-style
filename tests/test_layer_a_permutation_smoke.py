"""Layer A smoke: capped permutation p-value + run card."""

from __future__ import annotations

import numpy as np

from methodology_preamble import (
    PILLAR,
    assert_run_card,
    build_run_card,
    init_notebook,
)


def _y_shuffle(y: np.ndarray, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    y = np.asarray(y).ravel()
    idx = rng.permutation(y.size)
    return y[idx].copy()


def _corr(y: np.ndarray, x: np.ndarray) -> float:
    return float(
        np.corrcoef(np.asarray(y).ravel(), np.asarray(x).ravel())[0, 1]
    )


def _perm_p(y: np.ndarray, x: np.ndarray, n_perm: int, seed: int) -> tuple[float, float]:
    obs = _corr(y, x)
    rng = np.random.default_rng(seed)
    ge = 1
    for _ in range(n_perm):
        yp = _y_shuffle(y, int(rng.integers(0, 2**31 - 2)))
        c = _corr(yp, x)
        if abs(c) >= abs(obs):
            ge += 1
    return obs, ge / (n_perm + 1)


def test_layer_a_permutation_and_run_card() -> None:
    info = init_notebook()
    n_max = int(info["methodology_caps"]["permutation_test"]["n_perm_max"])
    n_perm = max(49, min(199, n_max))

    rng = np.random.default_rng(info["seed"])
    x = rng.normal(size=60)
    y = 0.05 * x + rng.normal(scale=1.0, size=60)

    obs, p = _perm_p(y, x, n_perm=n_perm, seed=info["seed"] + 1)

    rc = build_run_card(
        run_id="layer_a_ci_smoke",
        hypothesis="Synthetic independence smoke: correlation near 0 under y-shuffle null",
        metric=f"corr_obs={obs:.4f} p_perm={p:.4f} n_perm={n_perm}",
        null="y_shuffle",
        truth_scope="Synthetic RNG only; not a domain claim",
        seed=info["seed"],
    )
    assert rc["pillar"] == PILLAR
    assert_run_card(rc)
    assert 0.0 <= p <= 1.0
