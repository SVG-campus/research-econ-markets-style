# Pillar progress — `research-econ-markets-style`

**Overall solution proximity (rubric v2): ~54%** toward a defensible, preregistered answer for this pillar’s charter.

Formula (same as meta `docs/PILLAR_PROGRESS.md`): `round(0.30×charter + 0.30×LayerA + 0.25×repro + 0.15×data)` on 0–100 subscores.

See the full rubric and sibling pillars: [meta `docs/PILLAR_PROGRESS.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PILLAR_PROGRESS.md).

## This pillar

| Axis | % | Note |
|------|---:|------|
| Charter + prereg | 56 | `docs/PREREG.md` + `METHODS.md` |
| Layer A / nulls | 40 | Permutation + bootstrap + **domain charter stream** notebook (CI) |
| Reproducibility | 78 | `runs/smoke.yaml`, `runs/ci_notebooks.yaml`, `methodology_preamble`, pytest + headless CI (six CI notebooks (adds `CHARTER_YELP_STREAM_SMOKE` on Yelp stream)) |
| Domain data | 40 | `datasets.yaml` Hub pins + `reference_streams` + charter stream smoke |

## Links

- Preregistration template: [docs/PREREG.md](PREREG.md)
- Methodology skills (exact code): [Research-Apriori `skills/`](https://github.com/SVG-campus/Research-Apriori/tree/main/skills)
- Install: [CURSOR_SKILLS_INSTALL.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/CURSOR_SKILLS_INSTALL.md)
- Meta promotion + PR defaults: [`docs/PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) · [`.github/pull_request_template.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/.github/pull_request_template.md)
