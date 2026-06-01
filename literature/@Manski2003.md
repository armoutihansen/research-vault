---
citekey: Manski2003
title: Analysis of Treatment Response
authors: []
year: 2003
type: bookSection
doi: 10.1007/0-387-21786-X_8
zotero: "zotero://select/library/items/DAPS8WRZ"
pdf: /Users/jesper/Zotero/storage/CU8UTWTL/2003 - Analysis of Treatment Response.pdf
tags: [literature]
keywords: [partial-identification, treatment-effects, identification-region, worst-case-bounds, nonparametric-bounds, instrumental-variables, selection-problem]
topics: []
related: []
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> _No abstract in source metadata; see Summary below._

## Summary

This is a chapter from Charles Manski's monograph *Partial Identification of Probability Distributions* (Springer, 2003), the book-length statement of his "partial identification" / "credible inference" research program. The PDF supplied is a condensed reference version: it reproduces the introduction and a walkthrough of the early chapters — Ch. 1 Missing Outcomes, Ch. 2 Instrumental Variables, Ch. 3 Conditional Prediction with Missing Data — and lists the ten-chapter table of contents in which "Analysis of Treatment Response" is Chapter 7. Coverage here is **targeted**: I read the front matter, the introduction, and the propositions of Chapters 1-3 (which supply the identification machinery Chapter 7 applies) rather than the entire monograph. This is a general methodological reference text in econometric identification, only loosely tied to the user's substantive program (social/other-regarding preferences, choice modelling, belief elicitation), though its set-identification logic bears on choice-model and ML-for-theory work where point identification is fragile.

The unifying thesis is the **Law of Decreasing Credibility**: "the credibility of inference decreases with the strength of the assumptions maintained." Rather than combining data with assumptions strong enough to force point identification, Manski first asks what the data reveal *assumption-free*, yielding a set-valued **identification region**, and then asks how that region shrinks as assumptions are layered in. This reframes identification from a binary event (identified / not) into a continuum.

## Research question

Given a sampling process that only partially identifies a population parameter, what is the *sharp* set of parameter values consistent with the empirical evidence alone, and how does that set contract as one adds distributional or instrumental assumptions? For treatment response specifically (Ch. 7), the question is: what can be learned about the distribution of outcomes under a treatment when only the outcome under the *realized* treatment is observed (the selection problem / fundamental problem of counterfactuals)?

## Method / identification

The framework is nonparametric set identification. A population is a probability space and $y$ is an outcome with distribution $P(y)$; a binary indicator $z$ marks whether a realization is observed. By the law of total probability,
$$P(y) = P(y\mid z=1)P(z=1) + P(y\mid z=0)P(z=0).$$
The sampling process reveals $P(y\mid z=1)$ and $P(z)$ but is silent on $P(y\mid z=0)$, so the identification region is
$$H[P(y)] = \{\,P(y\mid z=1)P(z=1) + \gamma P(z=0):\ \gamma \in \Gamma_Y\,\},$$
where $\Gamma_Y$ is the space of all probability measures on $Y$. For a parameter $\tau[P(y)]$ the region is the image $\{\tau(\eta):\ \eta \in H[P(y)]\}$.

Key sharp results:
- **Proposition 1.1 (mean):** for bounded $g$ with $g_0=\inf g$, $g_1=\sup g$, the identification region for $E[g(y)]$ is the worst-case-bounds interval $[E[g(y)\mid z=1]P(z=1)+g_0 P(z=0),\ E[g(y)\mid z=1]P(z=1)+g_1 P(z=0)]$ — the *width* equals $(g_1-g_0)P(z=0)$, the missing mass times the outcome range.
- **Corollary 1.1.1 (event probability):** $H[P(y\in B)] = [P(y\in B\mid z=1)P(z=1),\ P(y\in B\mid z=1)P(z=1)+P(z=0)]$.
- **Proposition 1.2 (D-parameters):** for any functional $D$ that respects stochastic dominance, the extreme points of its identification region are obtained by placing all missing mass at $g_0$ (lower) or $g_1$ (upper); this yields quantile bounds and, via differencing, *outer* (non-sharp) bounds on contrasts like the interquartile range.

Assumptions then shrink the region. An **instrumental variable** $v$ (Ch. 2) is, on its own, uninformative, but combined with assumptions has identifying power: mean-independence / statistical-independence (SI) intersects the $v$-specific regions, $H_{SI}[P(y)] = \bigcap_{v\in V}\{\dots\}$, and emptiness of that intersection *refutes* the assumption. Missing-at-random (MAR) restores point identification but is non-refutable. Chapter 3 extends all of this to conditional prediction $P(y\mid x=x)$ with jointly missing outcomes and covariates, and to parametric best-predictor estimation, where the identification region is the set of $\theta^*=\arg\min_\theta E\{L[y-f(x,\theta)]\}$ over all feasible distributions of the missing data.

## Data

This is a methodological / theoretical text; it develops identification theory and estimators rather than analyzing a dataset. Estimation is by the **sample analog**: replace population distributions with empirical ones, e.g. $H_N[P(y)]$, which converges to the population region. Manski notes computation can be hard — even best linear prediction under square loss requires conjecturing all missing values, yielding a *set* of least-squares estimates.

## Key findings

The headline contribution is conceptual and theorem-backed: sharp, assumption-free bounds exist and are typically informative (non-trivial intervals), even though they do not point-identify. The propositions give closed-form worst-case bounds for means, event probabilities, quantiles, and stochastic-dominance parameters under missing data; the IV results characterize exactly when instruments help and when assumptions become refutable; the conditional-prediction results extend the program to regression and parametric prediction. Applied to treatment response (Ch. 7), this delivers the **Manski worst-case bounds** on average treatment effects under the selection problem with no assumptions, which monotone-treatment-response and monotone-IV assumptions (Chs. 8-9) then tighten.

## Contribution

Manski reframes empirical inference around a *menu* of conclusions indexed by assumption strength, rather than a single point estimate resting on untestable assumptions. By separating identification from statistical inference and reporting the whole identification region, the approach establishes a "domain of consensus" robust to disagreement about assumptions and makes the data's limits explicit. The book is the foundational synthesis of the partial-identification literature (bounds analysis) in econometrics.

## Limitations & open questions

- The assumption-free bounds, while sharp, can be wide (width scales with missing mass), so the practical payoff hinges on which *credible* assumptions are available — the choice of assumptions is left to the analyst.
- Difference parameters and joint conditional distributions generally yield only *outer* (non-sharp) bounds; sharp characterizations for general missing-data patterns remain hard.
- Statistical inference *on a set* (confidence regions for partially identified parameters) is flagged but not fully resolved here — a problem the subsequent literature (Imbens-Manski, CHT) took up.
- Computation of sample-analog regions is a standing challenge even in benign linear cases.
- Open hook for the user's program: porting sharp partial-identification logic to structural choice and social-preference models, and to ML predictors where point identification of the target functional fails.

## Connections

The book consolidates Manski's earlier work, including *Identification Problems in the Social Sciences* (1995) and the nonparametric treatment-bounds papers Manski (1990, 1997). The set-inference questions it raises were developed by Imbens & Manski (2004) on confidence intervals for partially identified parameters and by Chernozhukov, Hong & Tamer (2007) on inference for set-identified models; Tamer (2010) surveys the field. The treatment-effect bounds connect to the LATE / monotonicity framework of Imbens & Angrist (1994) and to Heckman & Vytlacil's marginal-treatment-effect program, which take the complementary point-identifying route. The stochastic-dominance machinery links to the dominance orderings used throughout decision theory and choice modelling.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
