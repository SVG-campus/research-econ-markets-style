# Pillar progress — `research-econ-markets-style`

**Overall solution proximity (rubric v2): ~53%** toward a defensible, preregistered answer for this pillar’s charter.

Formula (same as meta `docs/PILLAR_PROGRESS.md`): `round(0.30×charter + 0.30×LayerA + 0.25×repro + 0.15×data)` on 0–100 subscores.

See the full rubric and sibling pillars: [meta `docs/PILLAR_PROGRESS.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PILLAR_PROGRESS.md).

## This pillar

| Axis | % | Note |
|------|---:|------|
| Charter + prereg | 56 | `docs/PREREG.md` + `METHODS.md` |
| Layer A / nulls | 38 | Permutation + bootstrap tests; `SMOKE_LAYER_A` + `SMOKE_BOOTSTRAP` notebooks (CI) |
| Reproducibility | 77 | `runs/smoke.yaml`, `runs/ci_notebooks.yaml`, `methodology_preamble`, pytest + headless CI (3 smoke + `CHARTER_SHELL` + `CHARTER_EXTENDED_LIGHT`) |
| Domain data | 36 | `datasets.yaml` Hub pins + `reference_streams` |

## Links

- Preregistration template: [docs/PREREG.md](PREREG.md)
- Methodology skills (exact code): [Research-Apriori `skills/`](https://github.com/SVG-campus/Research-Apriori/tree/main/skills)
- Install: [CURSOR_SKILLS_INSTALL.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/CURSOR_SKILLS_INSTALL.md)
