---
citekey: Loomes1986
title: Disappointment and Dynamic Consistency in Choice under Uncertainty
authors: ["Loomes, Graham", "Sugden, Robert"]
year: 1986
type: journalArticle
doi: 10.2307/2297651
zotero: "zotero://select/library/items/GE8RIZ44"
pdf: /Users/jesper/Zotero/storage/REK2W5YD/Loomes1986.pdf
tags: [literature]
keywords: [disappointment-theory, expected-utility, decision-under-uncertainty, independence-axiom, dynamic-consistency, allais-paradox, regret-theory]
topics: []
related: [Bell1985, Kahneman1979, Tversky1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The central proposition of disappointment theory is that an individual forms expectations about uncertain prospects, and that if the actual consequence turns out to be worse than (or better than) that expectation, the individual experiences a sensation of disappointment (or elation) generating a decrement (or increment) of utility which modifies the basic utility derived from the consequence. By incorporating a simple disappointment-elation function into a model of individual choice, many observed violations of conventional expected utility axioms—including violations of Savage's sure-thing principle and the "isolation effect"—can be predicted and defended as rational and dynamically consistent behaviour.

## Summary

Loomes and Sugden develop *disappointment theory*: a parsimonious, transitive alternative to expected utility (EU) in which the satisfaction from an outcome is augmented by a disappointment/elation term comparing the realised consequence to the chooser's prior expectation for that prospect. A single convex/concave disappointment-elation function $D(\cdot)$ added to basic utility predicts a battery of replicated EU anomalies—the common consequence and common ratio effects, violations of Savage's sure-thing principle, and (in a multi-stage extension) the isolation effect—while keeping choice rational and dynamically consistent. It is the companion to the authors' earlier regret theory: regret compares outcomes *across actions within a state*, disappointment compares outcomes *across states within an action*.

## Research question

Can the observed violations of EU that regret theory leaves unexplained—in particular violations of Savage's sure-thing principle and the isolation effect (a violation of the compound probability axiom)—be generated and *defended as rational* by a simple, transitive psychological model of choice under uncertainty?

## Method / identification

The model is a decision-theoretic construction, not an estimation. An action $A_i$ is an $n$-tuple of state-contingent consequences $x_{ij}$ occurring with probabilities $p_j$ ($0 < p_j \le 1$, $\sum_j p_j = 1$). A *basic utility* function $C(\cdot)$, unique up to a positive affine transformation, assigns $c_{ij} = C(x_{ij})$—the ex post utility absent any regret/disappointment. The prior expectation of $A_i$ is taken as expected basic utility $\bar{c}_i = \sum_{j=1}^{n} p_j c_{ij}$. A differentiable disappointment-elation function $D(\cdot)$ maps the gap $c_{ij}-\bar{c}_i$ to a utility increment/decrement, so modified utility under state $j$ is $c_{ij}+D(c_{ij}-\bar{c}_i)$. The decision maker maximises expected modified utility

$$E_i = \sum_{j=1}^{n} p_j\big[c_{ij} + D(c_{ij}-\bar{c}_i)\big],$$

with $A_i \succeq A_k \iff E_i \ge E_k$. Because $E_i$ is a real-valued index, $\succeq$ is complete, reflexive and transitive—so, unlike regret theory, the model *cannot* generate intransitive choice.

Structural assumptions on $D(\cdot)$: $D(0)=0$ (under certainty, behave as a basic-utility maximiser); $D$ has the sign of its argument and $D'(\cdot)\ge 0$ (disappointment is painful, elation pleasurable, both increasing in the gap); $D$ is *convex for positive gaps and concave for negative gaps* (intensity of both sensations increases at the margin); and $D'(\cdot) < 1$ everywhere to preserve first-order stochastic dominance. A linear $D$ reproduces EU exactly. Two simplifying (non-essential) assumptions: symmetry $D(\xi)=-D(-\xi)$, and an initially linear basic-utility $C(\cdot)$ to isolate the work done by disappointment.

For the multi-stage extension, dynamic consistency is built in by setting $C(x_{ij}) = E^*_j$—the basic utility of a consequence that is itself an action equals that sub-action's expected modified utility. This yields a recursive treatment generalising to any number of stages and lets the model violate the compound probability axiom while *respecting* dynamic consistency.

## Data

None—this is a theoretical paper. It is illustrated against published experimental evidence rather than new data: the Allais (1953) problem, Kahneman and Tversky's (1979) common-ratio and common-consequence problems, and Tversky and Kahneman's (1981) three-problem isolation-effect design (85 of 205 subjects showed the common ratio effect; of these, 20 violated dynamic consistency and 65 the compound probability axiom).

## Key findings

- **Sure-thing-principle violations (common consequence effect).** Holding a common consequence $c^*$ as the only varying element, there exists a threshold $\theta$ with $A_1 \succeq A_2 \iff c^* \ge \theta$, so lowering $c^*$ flips the preference—exactly the observed reversal. Under symmetry, $0 < p < 0.5 < \lambda < 1$ guarantees the reversal as $c^*$ falls from $\lambda c$ to $0$. The result is robust to unequal expected basic utilities (via dominance-based constructions $A_3, A_4$) and to concave $C(\cdot)$.
- **Common ratio effect** follows from the same expression (2) by instead varying $p$ with $c^*=0$.
- **Relation to other models.** The implied Machina local utility function is derived; the model's assumptions ($C$ increasing, $0 \le D' < 1$) guarantee stochastic-dominance preference, and a $D$ that is convex-high/concave-low rationalises simultaneous gambling and insurance. The model is *not* a special case of Machina's (1982) Hypothesis II ("fanning out"): it permits preference "re-reversals" when expected basic utilities differ (none observed empirically). It is also distinguished from Bell's (1985) kinked-linear formulation, which cannot explain anomalies among equal-expected-value prospects, whereas the non-linear $D$ can.
- **Isolation effect.** With dynamic consistency imposed via $C(x_{ij})=E^*_j$, the model predicts $C \sim D \iff A \sim B$ but implies *no* equivalence between $\{C,D\}$ and $\{E,F\}$—so the isolation effect is a logical corollary of the common ratio effect, explaining why the compound probability axiom is violated far more often than dynamic consistency.

## Contribution

Provides a transitive, psychologically grounded model that (i) explains sure-thing-principle and compound-probability-axiom violations that regret theory alone cannot, and (ii) frames these violations as *rational* maximisation of expected satisfaction inclusive of anticipated disappointment/elation—not as irrational error or mere framing. By pairing within-action (disappointment) and across-action (regret) comparisons, it points toward a unified theory of rational choice encompassing both, and links seemingly unrelated anomalies (independence-axiom, compound-probability, and ultimately transitivity violations) under one rationale.

## Limitations & open questions

- The model is by construction transitive and so *cannot* explain observed intransitive choice—the very phenomenon regret theory targets; the authors flag that a more general theory should encompass both regret and disappointment.
- The shape, symmetry, and linear-$C$ assumptions are admitted simplifications adopted "mainly to ease exposition," not derived—their empirical form is left open.
- The model permits "re-reversals" that no experiment has tested (most use only pairwise choices; detecting re-reversals needs at least a triple)—an explicit empirical hook.
- No claim that reversals occur *only* under $\lambda > 0.5, p < 0.5$; behaviour in the complementary region ($\lambda < 0.5, p > 0.5$) is left unresolved.
- Reconciling the normative status of violations (rational vs. irrational) remains contested, invoked rather than settled.

## Connections

This paper is the explicit companion to the authors' own regret theory in Loomes & Sugden (1982) and Loomes & Sugden (1983), and builds directly on the disappointment intuition of [[@Bell1985|Bell (1985)]], whose kinked-linear "linear expectations" model it generalises (Bell (1982) covers the regret analogue). It is positioned within the non-EU "preference orderings over distributions" class anticipated by Samuelson (1950) and Allais (1953) and developed by Hagen (1979), Chew & MacCrimmon (1979), and Fishburn (1982, 1983); it is carefully contrasted with Machina's (1982) Generalized Expected Utility and Hypothesis II "fanning out." The anomalies it targets come from [[@Kahneman1979|Kahneman & Tversky (1979)]] (prospect theory), [[@Tversky1981|Tversky & Kahneman (1981)]] (framing and the isolation effect), Moskowitz (1974), and Slovic & Tversky (1974); the normative debate engages Savage (1954), MacCrimmon (1968), MacCrimmon & Larsson (1979), and Morgenstern (1979).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
