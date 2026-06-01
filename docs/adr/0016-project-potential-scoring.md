# ADR-0016: Project-potential scoring — compensatory value behind an admissibility filter

- Status: Accepted
- Date: 2026-06-01
- Relates to: ADR-0015 (idea-harvest / biblio); the Layer 2→3 bridge

## Context
`/idea-harvest`'s vetting emitted `novelty / feasibility / fit / grounding` as 1–5 *gut* numbers and a
hand-waved `composite` / `verdict` — the agent's overall feeling, not a defined function of the
dimensions, with no rubric for what a level *means*. So "project potential" was **unauditable** ("I don't
know how the scores are calculated"), it **averaged away fatal flaws** (a brilliant-but-infeasible or
unsound idea could still score mid), and it had no external anchor. The user wants to be **very selective
and critical** about potential, and wants the calculation **crystal-clear and reproducible**.

## Decision
**`Potential = 𝟙{admissible} · Σ wᵢ·dᵢ`** — a compensatory score behind an admissibility filter. The
shape is not arbitrary: the requirements contain **two different logical relationships**, and each forces
its operator.

### Two roles, two operators
- **Substitutable attributes → additive (compensation).** The user requires that reward and cost
  *compensate*: a low-effort *low-hanging fruit* (modest reward, tiny cost) and a high-reward *moonshot*
  (big reward, big cost) should **both** score high; only *expensive-and-unimportant* scores low. "High if
  reward **or** low-cost" is a *substitutes* relation, and addition is its operator — a big value in one
  term lifts the total regardless of the other. Multiplicative/ratio (ROI) operators are *conjunctive*:
  a low term drags the product down, which **craters the moonshot** (low feasibility ⇒ low product) — the
  opposite of compensation. So the value dimensions are **added**.
- **Necessary conditions → a gate (no compensation).** "Is the idea real / sound / not-already-done" is a
  *prerequisite*, not a tradeable attribute — no amount of *easy* compensates for *unsound* or *already
  published*. A necessary condition must **veto**, not contribute; as an addend it would be swamped by a
  high reward+ease. So validity is an **admissibility filter** (a 0/1 gate), kept out of the sum.

### The model
- **Admissibility filter** (pass/fail; failures are *dropped but listed*, never silently vanished):
  - *Sound & grounded* — coherent AND premise supported by **≥2 verified corpus papers** (not hallucinated).
  - *Not-already-done* — `biblio` finds nothing that *fully* does it.
- **Potential score** (admissible ideas only): `w_S·Significance + w_N·Novelty + w_F·Feasibility`, each
  dimension **1–5** on the *same* anchored scale (commensurable), **equal weights by default but an
  explicit, tunable parameter** (re-weight and re-rank *without re-vetting*), normalized to **0–100**.
  - *Significance* (how much it matters), *Novelty* (how new, above the floor), *Feasibility* (ease;
    inverse effort — low = hard but **never gated**, so moonshots survive).
- **Fit** (relevance to the user's research programme) — a **filter / sort key, not a score component**
  (great science slightly off-programme is still great science).
- **Rubrics + required evidence.** Each dimension has concrete 1–5 level descriptors; a dimension
  **cannot be scored above 3 without its cited evidence** present (`biblio` records, corpus citekeys, the
  target-venue band) — the main anti-inflation lever. Significance is *corroborated* by a **coarse target-
  venue band** (flagship / strong-field / specialist), the agent's estimate — venue **disciplines** the
  number but does not **define** it (merit stays primary over publishability). No canonical venue list is
  shipped at the idea stage; the AJG/FT50 CSV is deferred to `/promote-idea` / paper-targeting.
- **Judgment / calculation split.** The LLM (vetting agent) assigns only the **inputs** — the three
  dimension scores and the two admissibility verdicts, each with evidence. A **deterministic script**
  applies the filter, computes the score, and ranks. Same inputs → same number, by a documented formula;
  this is what makes potential auditable and reproducible (and re-weightable without re-vetting).
- **Calibration: lean.** The anchored rubrics (cross-agent consistency) + the evidence-cap + the
  admissibility filter are the calibrators. **No forced distribution and no per-idea multi-judge panel**
  in v1 — selectivity comes from *the filter + the score*, not a quota. (A final cross-idea consistency
  pass and an advisory "pursue above X" cut are clean future adds.)
- **Output.** Inadmissible ideas are listed separately with their failed gate + reason; admissible ideas
  are ranked by Potential (0–100), each showing the three dimension scores **+ their evidence**, the Fit
  tag, the admissibility evidence, and the refined pitch / first step / risks.

## Consequences
- "How is potential calculated?" is now literally a documented formula over evidence-backed inputs —
  auditable and reproducible; weights can be tuned and the list re-ranked without re-running vetting.
- Selective by construction: the filter kills the unsound/already-done, and the compensatory score (with
  Feasibility never gated) keeps both low-hanging fruit and moonshots while sinking the expensive-and-
  unimportant.
- LLM discretion is bounded to evidence-backed per-axis judgment; it no longer emits an opaque verdict.
- Requires a deterministic scoring script and a new vetting output schema (the agent stops emitting
  `composite`/`verdict`).

## Alternatives considered
- **Agent emits `composite` / `verdict`** (status quo) — fast, but an opaque gut number; the problem
  being solved. Rejected.
- **Multiplicative / ratio (ROI) aggregation** — conjunctive: low feasibility craters the product, so the
  *moonshot* scores low — contradicts the required reward↔cost compensation. Rejected.
- **Gated multiplicative *upside* (Significance × Novelty), feasibility-gated** (the original strawman) —
  kills the *low-hanging fruit* (low novelty) and the *moonshot* (low feasibility). Rejected.
- **Pure additive over all dimensions incl. grounding** — simplest, but a high reward+ease *swamps* an
  unsound or already-done idea, which then scores high. Rejected in favour of the validity gate.
- **Venue tier AS the Significance anchor + ship the AJG/FT50 CSV now** — most objective, but conflates
  merit with publishability and biases toward fashionable topics; the CSV is overkill at the idea stage.
  Reduced to a coarse corroborating band; CSV deferred to the promotion/paper stage.
- **Forced distribution / per-idea multi-judge panel** — more robust calibration, but arbitrary / costly;
  the rubric anchors + evidence-cap suffice for v1. Deferred.
