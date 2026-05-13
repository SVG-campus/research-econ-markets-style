"""Smoke: HF domain charter stream schema for research-econ-markets-style."""

from __future__ import annotations

import json
import numbers
from pathlib import Path

from datasets import load_dataset

from methodology_preamble import load_smoke_caps

_FIXTURE = Path(__file__).resolve().parent / "fixtures" / "yelp_review_stream_sample.json"
_PINNED_YELP = "Yelp/yelp_review_full"
_PINNED_YELP_CONFIG = "yelp_review_full"


def _assert_yelp_row_contract(row: object) -> None:
    assert isinstance(row, dict)
    assert "label" in row and "text" in row
    label, text = row["label"], row["text"]
    assert isinstance(label, numbers.Integral)
    li = int(label)
    assert 0 <= li <= 4
    assert isinstance(text, str) and text.strip() != ""


def test_yelp_pinned_stream_offline_fixture_matches_charter_schema() -> None:
    """Pinned `datasets.yaml` stream (`Yelp/yelp_review_full`): schema without Hub I/O."""
    payload = json.loads(_FIXTURE.read_text(encoding="utf-8"))
    assert isinstance(payload, list)
    assert len(payload) == 12
    for row in payload:
        _assert_yelp_row_contract(row)


def test_yelp_charter_perm_budget_respects_smoke_yaml_cap() -> None:
    """`CHARTER_YELP_STREAM_SMOKE` uses n_perm = max(39, min(149, n_perm_max))."""
    caps = load_smoke_caps()["methodology_caps"]["permutation_test"]
    n_perm_max = int(caps["n_perm_max"])
    n_perm = max(39, min(149, n_perm_max))
    assert n_perm_max >= 39, (
        "n_perm_max below 39 breaks the charter clamp vs smoke.yaml cap "
        "(notebook would run more permutations than methodology_caps allow)."
    )
    assert 39 <= n_perm <= 149
    assert n_perm <= n_perm_max


def test_yelp_stream_schema() -> None:
    rows = list(
        load_dataset(
            _PINNED_YELP,
            _PINNED_YELP_CONFIG,
            split="train",
            streaming=True,
        ).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        _assert_yelp_row_contract(r)
