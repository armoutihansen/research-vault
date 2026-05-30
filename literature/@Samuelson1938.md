---
citekey: Samuelson1938
title: The Empirical Implications of Utility Analysis
authors: ["Samuelson, Paul A."]
year: 1938
type: journalArticle
doi: 10.2307/1905411
zotero: "zotero://select/library/items/DG6NXCAD"
pdf: /Users/jesper/Zotero/storage/B2I3QPEX/Samuelson1938.pdf
tags: [literature]
keywords: [revealed-preference, utility-theory, demand-theory, slutsky-symmetry, consumer-choice, integrability]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

Samuelson asks whether ordinal utility analysis, once stripped of hedonistic and welfare connotations, retains any operational content — implications about observable price–quantity behavior that could in principle be refuted. He answers yes, deriving a compact set of restrictions on individual and market demand functions from a single "stability" inequality on prices and quantities. This is the bridge paper between his 1938 "New Foundations" revealed-preference postulate and the classical Slutsky–Hicks integrability conditions: it squeezes out the empirically meaningful content of utility theory using only observables.

## Research question

Does utility analysis, in its modern ordinal form, have any empirical (refutable) implications for individual and group price–quantity behavior, or is it an empty, circular tautology ("people act according to a plan; a plan is how people act")? If it does, what is the most economical way to express those implications using only observable prices and quantities?

## Method / identification

Pure deductive mathematical economics; no data. Samuelson assumes only an ordinal preference field $U=F[\varphi(x_1,\dots,x_n)]$ over $n$ commodities, with curvature (second-order) conditions sufficient for a proper constrained maximum under the budget $\sum_i p_i x_i = I$. The substantive content is loaded into one observational postulate: a "stability" condition on price and quantity changes,
$$\sum_{i=1}^{n} \Delta p_i\,\Delta x_i < 0 \quad\text{for}\quad \sum_{i=1}^{n} p_i \,\Delta x_i = 0,\ \text{not all } \Delta x_i = 0,$$
which in the limit becomes $\sum_i dp_i\,dx_i < 0$ subject to $\sum_i p_i\,dx_i = 0$. Crucially, only prices and quantities appear — no unobservable utility.

From the demand functions $x_i = h^i(p_1,\dots,p_n,I)$ with $I=\sum_i x_i p_i$, he differentiates ($dx_i = \sum_j h^i_j\,dp_j + h^i_I\,dI$, $dI = \sum_i x_i\,dp_i + \sum_i p_i\,dx_i$) and substitutes the postulate $\sum_i p_i\,dx_i = 0$ to obtain the quadratic form
$$\sum_{i=1}^{n}\sum_{j=1}^{n}\bigl(h^i_j + x_j h^i_I\bigr)\,dp_i\,dp_j < 0,$$
whose matrix is the Slutsky substitution matrix. He requires it to be negative semi-definite on the relevant subspace, expressed via signed principal minors $(-1)^m \Delta_{i_1,\dots,i_m} > 0$. The argument is then run three ways: (Section IV) holding income fixed and varying only prices, yielding a symmetric coefficient matrix $\sigma_{ij}=\tfrac12(h^i_j+h^j_i)$ and bordered-determinant conditions; the inverse "compensated" form in terms of $\gamma_{ij}$; and (Section V) aggregation from $s$ individuals to market demand $X_i = \sum_r {}^r x_i$, summing the individual inequalities to obtain analogous conditions on $H_{ij}$ and on $a_{ij}=H_{ji}+\sum_r {}^r x_j\,{}^r h^i_I$.

## Data

None — this is a purely theoretical, deductive paper. No empirical estimation or experiment; the entire contribution is the derivation of refutable restrictions that observable demand data could later be tested against.

## Key findings

- **Utility analysis is not empty.** It yields refutable restrictions on price–quantity behavior, contradicting the claim that ordinal utility is operationally meaningless.
- **The substitution-matrix inequality (8):** $\sum_{i,j}(h^i_j + x_j h^i_I)\,dp_i\,dp_j < 0$ — negative semi-definiteness of the Slutsky matrix — which Samuelson notes had not previously appeared in this form. Symmetry of the coefficients is the integrability condition.
- **Own-price effect need not be negative (10):** $\dfrac{\partial x_i}{\partial p_i} + x_i\dfrac{\partial x_i}{\partial I} < 0$. The compensated own-price effect is negative, but the uncompensated demand curve can slope upward if the income effect is sufficiently negative (Giffen goods are admitted).
- **Demand curves need not slope down.** Marshall's dictum that any price fall raises quantity demanded is shown to be a non-implication of utility theory.
- **Market-level conditions (Section V):** the same negative-semidefinite/symmetry structure survives aggregation across individuals (conditions 56, 61), so market demand inherits refutable restrictions — but only when each individual's income is specified, not from aggregate income alone.
- **Homogeneity (12):** $\sum_j h^i_j p_j = -h^i_I I$ (Euler's theorem), letting income elasticities be re-expressed via price elasticities.
- The five derived condition sets (9), (25), (34), (56), (61) reproduce and extend earlier fragmentary results of Johnson (1913, two goods), Slutsky (1915, the single condition 10), and Hotelling (1935, condition 34).

## Contribution

Establishes that ordinal utility theory has genuine empirical content and packages it in a uniform, observable-only formalism. By starting from a price–quantity stability postulate rather than from a utility function, Samuelson derives the Slutsky symmetry and negativity conditions quickly, exposes the income-effect caveat to the law of demand, and — importantly — extends the conditions from individual to market demand, where the substitution-effect logic still constrains aggregate behavior. This consolidates the revealed-preference program he launched in "New Foundations" (1938) and lays groundwork for the later weak/strong axioms of revealed preference and the integrability literature.

## Limitations & open questions

- **Aggregate-income aggregation (explicit open problem):** Samuelson shows it is impossible in general to derive market-demand restrictions depending only on price changes and *total* income, because there is generally no functional link between aggregate quantities demanded and aggregate income (as distinct from each individual's income). He explicitly defers this: "The problems which this entails must be reserved for consideration at a future time." This is the kernel of the later Sonnenschein–Mantel–Debreu non-aggregation results.
- The non-invertibility case $I=0$ (Jacobian $|h^i_j|=0$) is flagged as special; conditions (25) remain valid but the inverse demand representation fails.
- Whether the implied price–quantity hypothesis is *fruitful* (empirically successful) is declared out of scope — only that it is refutable.
- Hotelling's conjecture that stronger conditions "with considerable probability" hold for total demand is left unresolved; Samuelson notes counterexamples (e.g. negatively inclined supply schedules) but offers no general resolution.

## Connections

Directly continues Samuelson's "New Foundations for the Pure Theory of Consumer's Behaviour" (*Economica*, 1938), where the revealed-preference postulate originates. It reconstructs and generalizes the Slutsky (1915) decomposition and the symmetry/negativity of the substitution matrix, the Hicks–Allen ordinal indifference-curve apparatus, and Hotelling's (1935) demand-with-budget conditions, while crediting Johnson (1913) and Georgescu-Roegen (1936). The unresolved market-aggregation problem anticipates the Sonnenschein–Mantel–Debreu theorems on the arbitrariness of aggregate excess demand. Downstream, the paper feeds the Weak and Strong Axioms of Revealed Preference (Samuelson 1948, Houthakker 1950) and Afriat-style nonparametric tests of utility maximization — the modern empirical machinery for checking choice consistency against the very conditions derived here.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
