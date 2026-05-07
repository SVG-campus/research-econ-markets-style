"""Smoke: HF domain charter stream schema for research-econ-markets-style."""

from __future__ import annotations

from datasets import load_dataset


def test_yelp_stream_schema() -> None:
    rows = list(
        load_dataset(
            "Yelp/yelp_review_full",
            "yelp_review_full",
            split="train",
            streaming=True,
        ).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "label" in r and "text" in r
