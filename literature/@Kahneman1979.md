---
citekey: Kahneman1979
title: "Prospect theory: An analysis of decision under risk"
authors: ["Kahneman, Daniel", "Tversky, Amos"]
year: 1979
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/Y9CCC9FQ"
pdf: /Users/jesper/Zotero/storage/7PTSFF77/Kahneman1979.pdf
tags: [literature]
keywords: [prospect-theory, decision-under-risk, loss-aversion, reference-dependence, probability-weighting, expected-utility-critique, behavioral-economics]
topics: ["[[prospect-theory-loss-aversion]]"]
related: [Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper presents a critique of expected utility theory as a descriptive model of decision making under risk, and develops an alternative model, called prospect theory. Choices among risky prospects exhibit several pervasive effects that are inconsistent with the basic tenets of utility theory. In particular, people underweight outcomes that are merely probable in comparison with outcomes that are obtained with certainty. This tendency, called the certainty effect, contributes to risk aversion in choices involving sure gains and to risk seeking in choices involving sure losses. In addition, people generally discard components that are shared by all prospects under consideration. This tendency, called the isolation effect, leads to inconsistent preferences when the same choice is presented in different forms. An alternative theory of choice is developed, in which value is assigned to gains and losses rather than to final assets and in which probabilities are replaced by decision weights. The value function is normally concave for gains, commonly convex for losses, and is generally steeper for losses than for gains. Decision weights are generally lower than the corresponding probabilities, except in the range of low probabilities. Overweighting of low probabilities may contribute to the attractiveness of both insurance and gambling. (Abstract transcribed from the printed Econometrica title page; Zotero record had no abstract.)

## Summary
Kahneman and Tversky document a battery of systematic violations of expected utility theory (EUT) in hypothetical choices between monetary and non-monetary lotteries, then build a descriptive alternative, prospect theory. The theory replaces the expectation principle with a two-phase process: an *editing* phase that reformulates prospects, and an *evaluation* phase in which an edited prospect is scored by combining a reference-dependent, S-shaped *value function* $v$ over gains and losses with a nonlinear *decision-weight function* $\pi$ over stated probabilities. The model accounts for the certainty effect, the reflection effect, probabilistic-insurance aversion, and framing-induced preference reversals (the isolation effect).

## Research question
Is expected utility theory an adequate *descriptive* model of how people choose among risky prospects, and if not, what alternative formal representation captures the observed regularities while remaining tractable?

## Method / identification
The empirical method is hypothetical choice problems administered as questionnaires to students and faculty (Israeli, plus replications at Stockholm and Michigan), with response splits reported as percentages and significance flagged at the .01 level. Each "effect" is demonstrated by paired problems engineered so that the modal preferences are jointly inconsistent with EUT's substitution/expectation axioms.

The theoretical core is a formal two-phase model. The *editing phase* applies operations -- coding (outcomes recoded as gains/losses about a reference point), combination, segregation, cancellation (discarding components shared by prospects), simplification (rounding), and detection of dominance. The *evaluation phase* defines the value $V$ of an edited prospect $(x,p;y,q)$ via two scales: decision weights $\pi(p)$ and subjective values $v(x)$, with $v(0)=0$, $\pi(0)=0$, $\pi(1)=1$. For a *regular* prospect (either $p+q<1$, or $x\ge 0\ge y$, or $x\le 0\le y$):
$$V(x,p;y,q)=\pi(p)\,v(x)+\pi(q)\,v(y).$$
For *strictly positive or strictly negative* prospects ($p+q=1$ with $x>y>0$ or $x<y<0$), the riskless component is segregated:
$$V(x,p;y,q)=v(y)+\pi(p)\,[v(x)-v(y)].$$
The two coincide for sure prospects: $V(x,1.0)=v(x)$. Equation (2) reduces to (1) only when $\pi(p)+\pi(1-p)=1$, which generally fails (subcertainty). An axiomatic sketch ensuring a unique $\pi$ and ratio-scale $v$ satisfying (1) is relegated to the appendix.

## Data
None in the modern sense -- no field or incentivized data. Evidence consists of response distributions to roughly 14 hypothetical choice problems (and their mirrored/reflected variants), with sample sizes $N$ of roughly 60-95 per problem. The authors explicitly defend hypothetical choices as the simplest broadly applicable method while acknowledging the validity concerns.

## Key findings
- **Certainty effect:** outcomes obtained with certainty are overweighted relative to merely probable ones (Allais-type Problems 1-4); produces violations of the substitution axiom.
- **Reflection effect:** reversing the sign of outcomes reverses the preference order, so risk aversion over gains is mirrored by risk seeking over losses (Table I). This shows aversion to uncertainty per se does *not* explain the certainty effect; rather, certainty amplifies both the aversiveness of losses and the desirability of gains.
- **Probabilistic insurance:** people reject insurance that merely lowers loss probability from $p$ to $p/2$, contradicting the concavity-of-$u$ rationale for ordinary insurance; the formal proof shows EUT with concave $u$ implies the opposite preference.
- **Isolation effect:** decomposing equivalent prospects in different ways yields different choices (two-stage game in Problem 10; bonus framing in Problems 11-12), establishing that carriers of value are *changes* in wealth, not final asset positions.
- **Value function:** $v$ is defined on deviations from a reference point, concave for gains ($v''<0$ for $x>0$), convex for losses ($v''>0$ for $x<0$), and steeper for losses (loss aversion: $v(x)+v(-y)>v(y)+v(-x)$ for $x>y\ge 0$, and at the limit $v'(x)<v'(-x)$), giving the S-shaped curve of Figure 3.
- **Weighting function:** $\pi$ is increasing but not a probability measure. It exhibits *overweighting* of small probabilities ($\pi(p)>p$ for small $p$), *subcertainty* ($\pi(p)+\pi(1-p)<1$), *subproportionality* ($\pi(pq)/\pi(p)\le \pi(pqr)/\pi(pr)$, equivalent to convexity in $\log p$), and *subadditivity* for small $p$; it is poorly behaved near the endpoints (Figure 4). Overweighting of rare events helps explain the coexistence of gambling and insurance.

## Contribution
Provides the foundational descriptive theory of decision under risk, displacing EUT as a positive model. It introduces reference dependence, loss aversion, diminishing sensitivity, and probability weighting -- concepts that became the bedrock of behavioral economics. It cleanly separates editing (which generates framing and intransitivity anomalies) from a bilinear evaluation rule that generalizes EUT.

## Limitations & open questions
- The theory is restricted to *simple* prospects with at most two non-zero outcomes and stated objective probabilities; extension to many-outcome and to subjective/ambiguous probabilities is left open (the latter motivated cumulative prospect theory in 1992).
- Decision weights expressed as a function of *stated* probability conflate this with the distinct phenomenon of probability *overestimation*; disentangling them is unresolved.
- $\pi$ is "not well-behaved near the endpoints"; the discontinuities and the boundary treatment of extreme probabilities are acknowledged as ad hoc.
- Editing can be performed in multiple sequences, so the final edited prospect -- hence the prediction -- can be context-dependent; a detailed theory of editing order is "beyond the scope."
- Equation (2) can generate violations of dominance unless dominance detection in editing intervenes; reconciling $\pi$'s nonlinearity with dominance is only partially handled.
- The value function's two-argument dependence on asset position is approximated away, leaving its scope conditions open.

## Connections
The paper is built as a direct critique of expected utility theory in the von Neumann-Morgenstern and Savage tradition, and of its normative defenses by Arrow and Pratt. The certainty-effect problems are variations on Allais (1953), with related evidence from MacCrimmon & Larsson. Markowitz (1952) anticipated value defined on gains/losses and risk seeking, but retained the expectation principle; Edwards introduced probability-transforming weights, and Fellner the notion of decision weights for ambiguity aversion, with related models by van Dam and scaling work by van Dam-type studies. The reflection/risk-seeking-over-losses pattern echoes Williams and the review by Fishburn & Kochenberger. The reference-point logic draws on Helson's adaptation-level theory. Tversky's earlier work on intransitivity and elimination-by-aspects informs the editing/simplification operations. The framework was later extended by [[@Tversky1992|Tversky & Kahneman (1992)]] into cumulative prospect theory with rank-dependent weighting, connecting to Quiggin's rank-dependent utility.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
