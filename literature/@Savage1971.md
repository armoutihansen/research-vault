---
citekey: Savage1971
title: Elicitation of Personal Probabilities and Expectations
authors: ["Savage, Leonard J."]
year: 1971
type: journalArticle
doi: 10.1080/01621459.1971.10482346
zotero: "zotero://select/library/items/QQ5MHBA2"
pdf: /Users/jesper/Zotero/storage/2QIB253U/Savage - 1971 - Elicitation of Personal Probabilities and Expectations.pdf
tags: [literature]
keywords: [proper-scoring-rules, belief-elicitation, subjective-probability, decision-theory, convex-analysis, incentive-compatibility]
topics: ["[[experimental-belief-elicitation]]", "[[scoring-rules-elicitability]]"]
related: [Gneiting2007]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Proper scoring rules, i.e., devices of a certain class for eliciting a person's probabilities and other expectations, are studied, mainly theoretically but with some speculations about application. The relation of proper scoring rules to other economic devices and to the foundations of the personalistic theory of probability is brought out. The implications of various restrictions, especially symmetry restrictions, on scoring rules is explored, usually with a minimum of regularity hypothesis.

## Summary
A foundational theoretical paper on **proper scoring rules** for eliciting a person's subjective ("personal") probabilities and, more generally, expectations of random quantities. Savage's organizing idea is that a probability $P(A)$ is *a price* — a marginal rate of substitution of cash for money contingent on the event $A$ — elicitable by a behavioral interrogation analogous to the one used for ordinary prices. The paper unifies scattered antecedents (Brier, McCarthy, de Finetti, Good) under one convex-analytic theory, characterizes the entire class of incentive-compatible eliciting devices, derives the symmetric and special-form rules (quadratic/Brier, logarithmic, ratio), generalizes to simultaneous elicitation of vectors of rates and to full distributions, links the construction to statistical decision theory and to de Finetti's operational definition of probability, and closes with an extended discussion of practical obstacles. Coverage is full: extraction was clean and all ten sections were read.

## Research question
Under what conditions on a payment scheme will a coherent, expected-utility-maximizing person ("homo economicus" with locally linear utility for money) find it strictly in his self-interest to report his *true* personal probability of an event, or his true expectation of a random quantity? Equivalently: characterize the full class of "proper" (truth-inducing) scoring rules, and identify which restrictions (symmetry, dependence-on-discrepancy-only, separability) single out the familiar special cases.

## Method / identification
This is a theory paper built on convex analysis. The experimenter offers, for a chosen response $x$, an income that is linear in the subject's true rate $r$: $I(x;r)=b(x)r+c(x)$. Properness requires
$$I(x;r)=b(x)r+c(x)\le b(r)r+c(r)=J(r)$$
with equality iff $x=r$. The central result: this holds iff $J(r)\equiv I(r;r)$ is **strictly convex** and $I(x;\cdot)$ is a *line of support* of $J$ at $x$; since a strictly convex function has a distinct support at each point, the report $x=r$ is uniquely optimal. The misreport loss is the Bregman-type divergence $L(x;r)=J(r)-J(x)-J'(x)(r-x)\ge 0$. Savage proves a **monotonicity** property — keeping any unavoidable discrepancy small still pays — and shows $b,c$ are pinned down by $J$ up to an irrelevant lump-sum gift. For probabilities the scheme pays $Y(x)$ if event $D$ occurs and $Z(x)$ otherwise, with $J(p)=pY(p)+(1-p)Z(p)$ convex. The decision-theoretic route (Section 7) recovers the same class: $J(p)=\max_a[Y(a)p+Z(a)(1-p)]$ is the convex upper envelope of the available acts. He also treats utility nonlinearity, proposing utility-free lottery-ticket currency (after Smith) and constant-risk-aversion exponential utility $(1-e^{-\lambda x})/\lambda$ (after Pratt).

## Data
None. This is a purely theoretical paper; Savage explicitly states he has done no empirical work in the area. Section 10 surveys others' experimental and applied work (meteorology, oil-drilling, academic testing, expert elicitation) but presents no original data.

## Key findings
1. **Characterization theorem.** A scoring rule is strictly proper iff its expected-score function $J$ is strictly convex and the rule pays a line of support of $J$; this exhausts the admissible class up to lump-sum transfers.
2. **Symmetry / discrepancy restrictions force the quadratic rule.** Requiring loss to depend only on the discrepancy, $L(x;r)=H(x-r)$, or to be symmetric, $L(x;r)=L(r;x)$, both force $J$ quadratic and hence $L(x;r)=k(x-r)^2$ — the **Brier / quadratic** rule (the two conditions are equivalent).
3. **Ratio-discrepancy gives the logarithmic rule.** $L(x;r)=H(r/x)$ forces $J(r)=m+lr-k\log r$ and $H(u)=k(u-1-\log u)$ — the **logarithmic** rule.
4. **Uniqueness of the expectation eliciter.** For a rich class of distributions the only $S(x;v)$ with $E[S(x;V)]\le E[S(r;V)]$ at $r=E(V)$ is $b(x)v+c(x)+f(v)$; for indicators the additive $f$ is nugatory. Least squares $S=-(x-v)^2$ is the canonical instance.
5. **Vector / distribution elicitation.** The theory extends to vectors of rates and to distributions over a partition, with $J$ strictly convex on the simplex and $I(x;V)=J(x)+J'(x)(V-x)$.
6. **Separability ⇒ logarithmic.** Requiring the income when $D_s$ obtains to depend on $x_s$ alone forces (for $n>2$) $f_s(z)=k\log z+l_s$, recovering Good's rule and the information loss $L(x;p)=k\sum_s p_s\log(p_s/x_s)$.
7. **Operational foundation of probability.** Following de Finetti, the unique support point $p_0$ of a strictly convex $J$ can *define* personal probability; the construction yields a coherent (finitely additive) probability measure, and different $J$ elicit the same $p$.

## Contribution
The canonical synthesis that put proper scoring rules on a rigorous convex-analytic footing, tying them to (i) the economics of marginal rates of substitution, (ii) statistical decision theory, and (iii) de Finetti's operational foundations of probability. It supplies the characterization theorem and the derivations isolating the Brier and logarithmic rules, and frames belief elicitation as an incentive-compatible mechanism — a direct ancestor of modern incentivized belief elicitation and of property-elicitation / forecast-evaluation theory.

## Limitations & open questions
- **Nonlinear utility of money** is the central practical threat: properness rests on locally linear utility, but large stakes (which improve the subject's attention) distort reports toward risk attitudes rather than beliefs. Savage's proposed remedies (lottery-ticket currency, paying in utiles, exponential-utility correction) are admittedly partial — quantifying and correcting these distortions is left open (and is the seed of a large later literature).
- **Endogenous, decision-relevant events** cannot be scored at all when the action taken (e.g. whether to drill) precludes ever observing the outcome — "we can never know what would have happened." Savage flags "business sharing" as only a partial workaround.
- **Choice among the plethora of proper rules** rests on informal criteria (distance sensitivity, comprehensibility); no decision-theoretic selection principle is given.
- **Vagueness and unstable, intransitive preferences** of real subjects, and the special training elicitation seems to require, are noted as obstacles needing education rather than theory.
- The clean **separated-income** ideal is "not quite attainable": the logarithmic rule assigns $-\infty$ to a report of probability zero.

## Connections
The paper consolidates Brier (1950) on the quadratic forecast-verification score, McCarthy (1956) on convex measures of the value of information, Good (1952) on the logarithmic rule, and de Finetti (1937) on subjective probability and coherence, with whom Savage originally co-authored the project. The exponential constant-risk-aversion utility draws on Pratt (1964) and the utility-free currency on Smith (1961); the sealed-bid price-elicitation analogue is Marschak's (1964) mechanism, related to the later Becker–DeGroot–Marschak procedure. It builds on Savage's own *Foundations of Statistics* (1954). Downstream it is the precursor to the modern unified treatment of strictly proper scoring rules and property elicitation by [[@Gneiting2007|Gneiting & Raftery (2007)]], to distance-sensitive rules (Staël von Holstein 1970; Epstein 1969), and to incentivized belief elicitation in experimental economics.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
