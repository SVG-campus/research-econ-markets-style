# Pillar progress — `research-econ-markets-style`

**Overall solution proximity (rubric v2): ~55%** toward a defensible, preregistered answer for this pillar’s charter.

Formula (same as meta `docs/PILLAR_PROGRESS.md`): `round(0.30×charter + 0.30×LayerA + 0.25×repro + 0.15×data)` on 0–100 subscores.

See the full rubric and sibling pillars: [meta `docs/PILLAR_PROGRESS.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PILLAR_PROGRESS.md).

## This pillar

| Axis | % | Note |
|------|---:|------|
| Charter + prereg | 56 | `docs/PREREG.md` + `METHODS.md` |
| Layer A / nulls | 42 | Permutation + bootstrap + **`CHARTER_LAYER_A_MULTIDRAW_SMOKE`** + **domain charter stream** notebook (CI) |
| Reproducibility | 79 | `runs/smoke.yaml`, `runs/ci_notebooks.yaml`, `methodology_preamble`, pytest + headless CI (seven CI notebooks: adds `CHARTER_LAYER_A_MULTIDRAW_SMOKE` before domain stream charter); `runs/promotion_audit.example.yaml` **`trace_run_ids`** + schema test in CI |
| Domain data | 40 | `datasets.yaml` Hub pins + `reference_streams` + charter stream smoke |

## Links

- Preregistration template: [docs/PREREG.md](PREREG.md)
- Methodology skills (exact code): [Research-Apriori `skills/`](https://github.com/SVG-campus/Research-Apriori/tree/main/skills)
- Install: [CURSOR_SKILLS_INSTALL.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/CURSOR_SKILLS_INSTALL.md)
- Meta promotion + PR defaults: [`docs/PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) · [`.github/pull_request_template.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/.github/pull_request_template.md)
