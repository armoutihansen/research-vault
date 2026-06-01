---
slug: scoring-rules-elicitability
title: "Proper Scoring Rules & Elicitability"
type: topic
scope: "The statistical decision theory of proper scoring rules and which functionals of a distribution admit a consistent scoring function (elicitability), via convex/Bregman duality."
area: "[[beliefs-forecasting-elicitation]]"
tags: [topic]
created: 2026-06-01
generated: 2026-06-01
---

## Scope

This topic is the statistical decision theory of *honest reporting*: which payment rule $S$ makes truthfully reporting an object — a whole predictive distribution, or a single functional of it — the uniquely expected-payoff-maximizing response, and which objects admit any such rule at all. The unifying machinery is convex/Bregman duality: a rule is proper exactly when its expected-score function is (strictly) convex and the rule is a subtangent of it, so the realized score is a Bregman divergence from truth. The two faces of the question — *propriety* (eliciting the full distribution $P$) and *elicitability* (eliciting one functional $T(F)$ via a consistent scoring function) — are the same duality read at two granularities, and the topic's tension lives in the gap between what is elicitable and what practitioners want to score.

## Sub-themes

- **The convex/Bregman foundation.** Savage (1971) is the source: a scoring rule is strictly proper iff its expected-score function $J$ is strictly convex and the rule pays a line of support of $J$, with misreport loss the Bregman-type divergence $L(x;r)=J(r)-J(x)-J'(x)(r-x)$. Gneiting & Raftery (2007) lift this to general probability spaces (Theorem 1: propriety $\Leftrightarrow$ convex generalized-entropy function $G(P)=S(P,P)$ with $S(P,\cdot)$ a subtangent), recovering Savage's categorical case as the Savage representation and tying the associated divergence to Bregman divergences and information measures.

- **Pinning down specific rules: symmetry, axioms, locality.** Savage (1971) shows symmetry/discrepancy restrictions force the quadratic (Brier) rule and a ratio-discrepancy restriction forces the logarithmic rule. Selten (1998) gives a four-axiom characterization (symmetry, elongation invariance, incentive compatibility, neutrality) singling out the quadratic rule uniquely up to positive affine rescaling — but as a measure of *predictive success* for ranking competing probabilistic theories, not merely as an elicitation device. Gneiting & Raftery (2007) add the locality result (the logarithmic score is the only proper *local* density score) and the energy/kernel-score family for continuous and multivariate outcomes.

- **From distributions to functionals — elicitability.** Lambert, Pennock & Shoham (2008) generalize propriety from whole distributions to a single *property* $\Gamma$ of a distribution over a finite outcome space, with the clean geometric characterization: $\Gamma$ is elicitable iff its level sets are convex (equivalently $\Gamma$ is a linear constraint on $P$), plus a signature-plus-weight representation of *all* truthful contracts and the notion of elicitation complexity. Gneiting (2011) develops the parallel for real-valued point forecasts: a functional is elicitable if a strictly *consistent* scoring function exists, with functional-by-functional characterizations (means $\Leftrightarrow$ Bregman; quantiles $\Leftrightarrow$ generalized piecewise linear; expectiles; ratios of expectations) via Osband's principle, and the line between a proper scoring rule and a consistent scoring function.

- **The boundary of elicitability — negative results.** Gneiting (2011) shows conditional value-at-risk is *not* elicitable (it violates Osband's convex-level-set necessary condition). Heinrich (2014) answers Gneiting's open question by showing the *mode* is not elicitable either — and crucially via a mechanism that does *not* violate convex level sets, proving that convexity of level sets is necessary but **not sufficient** for elicitability.

## Cross-paper tensions

The first fault line is **what convex level sets actually buy you.** Lambert, Pennock & Shoham (2008) make convex level sets the *characterization* of elicitability (necessary and sufficient) on finite outcome spaces; Gneiting (2011) carries the convex-level-set condition over to real-valued functionals but only as a *necessary* condition (Theorem 6), leaving its converse open. Heinrich (2014) then breaks the symmetry decisively: the mode has convex level sets yet is not elicitable on rich classes with Lebesgue densities. So the same geometric criterion that is *exact* in the Lambert–Pennock–Shoham finite world is provably *insufficient* in Gneiting's continuous world — the two papers pull the convexity condition in opposite directions, and the difference is precisely the move from finite $\Omega$ (where Lambert et al. themselves flag continuous spaces as where their proofs may fail) to densities admitting tall thin peaks.

Second, **which canonical rule, and on what grounds.** Savage (1971) derives both the quadratic and the logarithmic rule, each from a different *a priori* restriction (symmetry vs. ratio-discrepancy), and explicitly declines to give a decision-theoretic selection principle among the plethora of proper rules. Selten (1998) supplies exactly such a principle and concludes the *quadratic* rule is uniquely justified — but his decisive axiom, *neutrality* ($L(p\mid q)=L(q\mid p)$), is the symmetry condition Savage already showed forces the quadratic, and Selten himself flags neutrality as a contestable normative choice for asymmetric-loss settings. Against this, Gneiting & Raftery (2007) treat *no* single rule as canonical, emphasizing that the choice of proper rule is "in strong demand" and task-dependent, and that the logarithmic — not the quadratic — is privileged by locality and by being the MLE-inducing optimum score. The corpus thus holds two incompatible answers to "which rule": Selten's axiomatic uniqueness of the quadratic vs. the Gneiting–Raftery view that propriety leaves a whole convex cone open and locality points elsewhere.

Third, **propriety vs. consistency — full distribution vs. single functional.** Gneiting (2011) sharpens a distinction the older literature blurred: a *proper scoring rule* elicits the whole $P$, a *consistent scoring function* elicits one functional $T(F)$, and every consistent $S$ induces a proper rule but not conversely. Savage (1971), Selten (1998), and Lambert et al. (2008) (in its full-distribution mode) sit on the propriety side; Gneiting (2011) and Heinrich (2014) live on the functional side. The tension is that the practitioner's actual object — a point forecast, a risk measure — is usually a functional, yet the foundational rules and the experimental-belief tradition (the shared Savage/Gneiting–Raftery anchors) are built to elicit the *whole* distribution, so the elicitability gap (CVaR, mode, variance, centered moments) is exactly the set of objects people want but cannot honestly score with a single rule.

Fourth, **the role of strictness and richness of the class.** Heinrich (2014) (Proposition 1) shows the mode *is* elicitable on unimodal *discrete* classes, and non-elicitability appears only once the class is rich enough to carry tall thin density peaks — so elicitability is not a property of the functional alone but of the functional-plus-class pair. This sits uneasily with the cleaner, class-light statements in Lambert et al. (2008) and Gneiting (2011), and with Selten's (1998) finite-action setting where the quadratic rule is unconditionally available; the corpus never reconciles how much of "non-elicitability" is intrinsic vs. an artifact of admitting pathological distributions.

## Open questions

- A **full characterization of elicitability** for real-valued functionals — the converse to the convex-level-set condition — is explicitly open in Gneiting (2011) and is exactly what Heinrich (2014) shows the obvious candidate (convex level sets) *cannot* be. What stronger condition is both necessary and sufficient on continuous outcome spaces?
- Gneiting & Raftery (2007) flag that the relationship between proper scoring rules and divergence functions is **not fully understood**, and that the general form of proper *quantile* scores is unknown — they cannot tell whether their explicit forms exhaust the class.
- **Elicitation complexity and higher-order elicitability.** Lambert et al. (2008) leave the complexity of common properties unpinned (kurtosis $C^3$ vs $C^4$) and the *necessity* of convex level sets for set/vector elicitability open; Heinrich (2014) leaves open whether the mode is *jointly* elicitable with an auxiliary functional (higher-order elicitability), the route by which CVaR was later rescued.
- **The boundary between elicitable and non-elicitable classes.** Heinrich (2014) conjectures the mode non-elicitability extends to Cauchy and Student-$t$ mixtures but proves it only for Gaussian mixtures, and the discrete case is elicitable — so where exactly does the boundary fall?
- **Which proper/consistent rule to use** is unresolved: Savage (1971) gives only informal criteria, Selten (1998) restricts to fully-specified finite-action theories (no model-complexity penalty, "area theories" and subset-predicting theories left open), and Gneiting & Raftery (2007) call selection guidelines for proper rules "in strong demand."
- Selten (1998) leaves open how to measure predictive success when a theory predicts a *subset* of the distribution simplex (qualitative properties like unimodality) or has unknown parameters — i.e. comparing theories of differing complexity.

## Candidate ideas

- **A sufficient condition for real-line elicitability that survives Heinrich's counterexample.** Heinrich (2014) shows convex level sets are necessary but not sufficient; the open converse in Gneiting (2011) is the target. Pursue a *theory* project characterizing elicitability on density classes via a local identifiability / order-sensitivity condition on the candidate identification function $V$ (the object Osband's principle produces), and test it against the known elicitable (mean, quantile, expectile) and non-elicitable (mode, CVaR) cases. Feasible as pure theory; no experiments needed.

- **Class-relative elicitability map for the mode.** Heinrich's (2014) Proposition 1 (discrete: elicitable) vs. Theorems 1–3 (rich density classes: not) leave the boundary unmapped, with explicit conjectures for Cauchy/Student-$t$ mixtures. A theory + simulation project would prove or disprove non-elicitability for those named families and chart which *parametric* density classes restore mode-elicitability — directly closing one of Heinrich's stated hooks. Theory with light Monte-Carlo (the bimodal-mixture design Heinrich already runs is reusable).

- **Higher-order joint elicitability of the mode.** Heinrich (2014) flags but does not address whether the mode becomes elicitable jointly with an auxiliary functional, mirroring the (VaR, CVaR) rescue of Gneiting's (2011) CVaR non-elicitability result. A theory project: find an auxiliary functional $g(F)$ (e.g. a modal-interval width or a local density level) such that $(\text{mode}, g)$ is jointly elicitable, constructing the consistent score via Osband's principle. Pure theory.

- **Reconciling Selten's quadratic uniqueness with Gneiting–Raftery locality.** Selten (1998) axiomatizes the quadratic rule as *the* measure of predictive success via neutrality; Gneiting & Raftery (2007) privilege the logarithmic rule via locality and MLE-optimality. A theory + simulation project: state the minimal axiom (neutrality vs. locality vs. a complexity penalty) that decides between quadratic and logarithmic when ranking competing *behavioral* choice theories, then show on existing model-comparison data which axiom the standard log-likelihood horse-race implicitly assumes. Theory + existing-data; connects directly to Selten's open problem of comparing theories of unequal complexity.

- **A consistent success measure for subset-predicting theories.** Selten (1998) leaves open how to score a theory that predicts a *region* of the distribution simplex (a qualitative restriction like unimodality, à la error-laden EU models) rather than a point distribution. Combine Lambert, Pennock & Shoham's (2008) elicitation-complexity apparatus with Gneiting's (2011) set-valued consistency to derive a strictly consistent score for *set-valued* predictions, quantifying the precision/accuracy trade-off Selten describes. Theory, extending the Lambert et al. set-elicitability results whose necessity is itself open.

- **Elicitation-complexity audit of the functionals economists actually report.** Lambert et al. (2008) define $k$-elicitability but pin down few common properties; Gneiting (2011) shows variance, centered moments, and CVaR are not directly elicitable. A theory + existing-data project: compute the elicitation complexity of the functionals routinely reported in empirical economics (variance, Gini, CVaR, ratios of expectations) and flag which published forecast-comparison exercises are scoring non-elicitable targets — a direct, low-cost extension of Gneiting's (2011) APE-elicits-the-wrong-functional warning. Existing-data / theory only.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
_None — no member cites an in-corpus paper outside this topic._

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
