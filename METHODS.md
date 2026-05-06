# Methodology — Economics, markets, style signals

This pillar inherits the **three-layer** research standard from `alpaca-trading-algo/Exotic Research/METHODOLOGY_BACKBONE.md` (Layer A empirical, Layer B structural vocabulary, Layer C narrative hypotheses).

## Layer A — Empirical backbone

- Fix **random seeds** for any Monte Carlo / bootstrap in published runs; record seed in notebook frontmatter or run config.
- Prefer **small-sample CI smoke** in GitHub Actions; push heavy MC / replay to Kaggle or Hugging Face Jobs.
- Use **negative controls** when asserting statistical structure (shuffles, surrogates, label permutations) where applicable.
- Truth scope: Layer A validates **fit to data under explicit assumptions** — not automatic real-world deployment guarantees.

## Layer B — Structural ontology

- Document variables, constraints, and module boundaries in this repo's `README.md` as they crystallize from notebooks.
- Distinguish **notation / taxonomy** from formal proofs unless you derive a claim for a stated model class.

## Layer C — Narrative and intuition

- Prompts, analogies, and exploratory prose are **hypothesis generators** only.
- Promotion to "best answer" status requires Layer A evidence and documented **falsifiers** in the meta repo `BEST_ANSWERS_OVERVIEW.md`.



## Promotion rule (pillar)

No result is treated as **production** or **actionable edge** without:

1. Layer A metrics meeting pre-declared thresholds.
2. Independent replication notes (second seed / holdout / implementation cross-check).
3. Explicit statement of **remaining uncertainty** and **missing mechanisms**.

---

*Template aligned with Exotic Research METHODOLOGY_BACKBONE.md — customize with pillar-specific artifacts as code matures.*
