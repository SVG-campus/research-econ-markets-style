"""`runs/promotion_audit.example.yaml` stays parseable and aligned with promotion checklist."""

from __future__ import annotations

from pathlib import Path

import yaml


def test_promotion_audit_example_schema() -> None:
    root = Path(__file__).resolve().parents[1]
    p = root / "runs" / "promotion_audit.example.yaml"
    assert p.is_file(), f"missing {p}"
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    assert data.get("version") == 1
    assert data.get("pillar") == "research-econ-markets-style"
    ex = data.get("example_entry")
    assert isinstance(ex, dict)
    for k in ("promoted_at", "run_id", "source_path", "commit_sha", "metric_excerpt", "null_method"):
        assert k in ex, f"example_entry missing {k}"
    ids = data.get("trace_run_ids")
    assert isinstance(ids, list) and len(ids) >= 2
    assert "charter_layer_a_multidraw_smoke" in ids
    assert "charter_econ_yelp_stream_smoke" in ids
