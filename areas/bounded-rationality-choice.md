---
slug: bounded-rationality-choice
title: "Bounded Rationality & Individual Choice"
type: area
scope: Procedural and limited-cognition models of individual choice and their revealed-preference content.
tags: [area]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This area covers procedural and limited-cognition models of individual choice and the revealed-preference content they carry: how to represent a decision maker who does *not* maximize one complete, menu-independent preference, and what observable choice (or non-choice, or process) data can recover about her underlying order. Its child topics span the classical axiomatic bedrock that the rest of the field breaks against, the three families of departure from it (two-stage procedures, attention/feasibility filters, satisficing thresholds), the context effects and incomplete-preference phenomena those procedures rationalize, and the welfare/policy question of what to do once $WARP$ fails. They cohere around one program: replacing global utility maximization with a *procedure* while keeping the model testable.

## Sub-areas / themes

The field rests on a foundational floor and rises through positive procedural models to a normative ceiling.

- **Foundations.** [[revealed-preference-foundations|Revealed-Preference & Rationalizability Foundations]] supplies the axioms ($WARP/SARP$, congruence, $\alpha/\beta/\gamma$) and the identification logic that every other topic is measured against — it sets the rules the rest of the area breaks.
- **Procedural choice (the positive core).** [[sequential-rationalizability-shortlists|Sequential Rationalizability & Shortlist Methods]] decomposes a choice act into ordered rationales; [[limited-attention-consideration-sets|Limited Attention & Consideration Sets]] keeps a stable preference but restricts the menu actually attended to; [[satisficing-search-revealed-preference|Satisficing, Search & Threshold Choice]] formalizes Simon's stop-when-good-enough via thresholds and stopping rules. These are three architectures — screen-then-pick, attend-then-maximize, search-then-stop — for the same departure from maximization.
- **Phenomena and primitives.** [[context-effects-attraction-compromise|Context Effects: Attraction, Compromise & Decoys]] catalogues the menu-geometry anomalies (regularity/IIA violations) the procedures must explain; [[incomplete-preferences-choice-deferral|Incomplete Preferences, Indecisiveness & Choice Deferral]] relaxes completeness/transitivity at the level of the order itself, rationalizing deferral and cycles.
- **Normative use.** [[behavioral-welfare-nudge|Behavioral Welfare Economics & Nudges]] asks how to make welfare statements and design defaults once choice is inconsistent — consuming the positive procedures as inputs.

## Cross-topic tensions

**1. The master tension: where does identification come from, and is the residual indeterminacy fixable or intrinsic?** Every positive topic hits a partial-identification ceiling, but blames a different culprit. [[limited-attention-consideration-sets|Limited attention]] frames it as data-type (deterministic filters recover only a partial order $P_R$; stochasticity buys unique recovery of $(\succ,\gamma)$). [[sequential-rationalizability-shortlists|Shortlist methods]] frame it as a lattice of representations where the middle relation $P^m$ loads onto either rationale. [[satisficing-search-revealed-preference|Satisficing]] frames it as time vs. menu variation. The field cannot agree whether the cure is richer data, stochasticity, or extra axioms.

**2. Vacuity of the bare architecture.** The same deflationary verdict recurs across topics: the two-stage threshold form is *empirically empty on single-valued data* ([[satisficing-search-revealed-preference|satisficing]], [[limited-attention-consideration-sets|limited attention]] both cite Manzini–Mariotti–Tyson), and sequential rationalizability with arbitrarily many rationales still cannot escape Always Chosen. All predictive force lives in the supplementary axioms (the filter, expansiveness, the shading relation) — so the "explanatory power" attributed to procedures may be an artifact of their side conditions, not their architecture.

**3. Irrationality vs. rational inference vs. broken primitive.** The *same observable anomaly* admits incompatible readings across topics: [[context-effects-attraction-compromise|context effects]] split between rational market inference (Kamenica), salience distortion (Bordalo et al.), and constructed preference; [[incomplete-preferences-choice-deferral|incomplete preferences]] read cycles as one agent's indecisiveness *or* as the footprint of aggregation (May, game trees); [[revealed-preference-foundations|foundations]] host Sen's claim that acts of choice cannot contradict each other at all. Choice data underdetermine which.

**4. Where welfare lives, and how discerning a criterion may be.** [[behavioral-welfare-nudge|Behavioral welfare]] is fractured between conservative-but-silent ($P^*$), refutable-but-recovering (distortion functions, which can even reverse Pareto), and irreducibly-stipulated (scoring rules). This directly consumes topic-3's "which observation is welfare-relevant": [[satisficing-search-revealed-preference|satisficing]] disputes small-menu vs. search-path as the arbiter, and [[sequential-rationalizability-shortlists|shortlists]] show a decoy can silently flip the rationale order and deceive Bernheim–Rangel — so a procedural model and its welfare verdict are not separable.

## Open questions

- **Mechanism discrimination from choice alone.** Categorization, rationalization, limited attention, and shortlisting are repeatedly shown observationally equivalent on standard data; separating them is the field's recurring unsolved demand and points squarely at process / non-choice data (eye-tracking, response times, choice-process trajectories).
- **The identification frontier of menu-dependence.** Between the identified (menu-independent) and vacuous (fully menu-dependent) extremes, which restricted forms of menu-/state-dependent attention, rationale-order, and thresholds stay tractable is open across at least three topics.
- **A complexity measure that penalizes structure, not just count.** The count-of-rationales program is either NP-hard or behaviorally uninformative; a "structured" graded-rationality index remains unbuilt.
- **Stochastic and hybrid representations.** Marrying deterministic procedures with utility noise — stochastic partial dominance, consideration-plus-RUM, probabilistic distortion functions for welfare — is flagged everywhere and delivered almost nowhere.
- **A non-vacuous welfare/policy discipline.** No paper supplies a principled rule for pruning ancillary conditions, selecting scoring weights, or deciding "where to stop" being libertarian — leaving choice architecture resting on benchmarks the foundational papers say are unavailable.

## Topics
```dataview
TABLE scope AS Scope
FROM "topics"
WHERE area = this.file.link
SORT file.name ASC
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
