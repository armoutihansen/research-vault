---
citekey: Zrill2021
title: (Non-)Parametric Recoverability of Preferences and Choice Prediction
authors: ["Zrill, Lanny"]
year: 2021
type: journalArticle
doi: 10.1162/rest_a_01143
zotero: "zotero://select/library/items/5223R5C8"
pdf: /Users/jesper/Zotero/storage/IVBU85L8/Zrill2021a.pdf
tags: [literature]
keywords: [revealed-preference, decision-under-risk, disappointment-aversion, out-of-sample-prediction, non-parametric-bounds, adaptive-experiment, garp]
topics: []
related: [Andreoni2002, DellaVigna2018, Fisman2007, Gul1991, Peysakhovich2017]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Simple functional forms for utility require restrictive structural assumptions that are often contrary to observed behavior. Even so, they are widely used in applied economic research. I address this issue using a two-part adaptive experimental design to compare the predictions of a popular parametric model of decision making under risk to those of non-parametric bounds on indifference curves. Interpreting the latter as an approximate upper bound, I find the parametric model sacrifices very little in terms of predictive success. This suggests that, despite their restrictiveness, simple functional forms may nevertheless be useful representations of preferences over risky alternatives.

## Summary
Zrill confronts the classic generality-vs-parsimony trade-off in revealed-preference theory by asking how much out-of-sample predictive accuracy is lost when one imposes a simple parametric functional form instead of staying agnostic with non-parametric bounds. Using a two-part adaptive lab experiment (portfolio choice over Arrow securities, then individually tailored pairwise lottery comparisons), he recovers each subject's preferences both parametrically (Disappointment Aversion with CRRA utility) and non-parametrically (Varian bounds on indifference curves, modified for GARP violators). Treating the non-parametric bounds as an approximate upper bound on any deterministic model's predictive success, he finds the parametric model predicts 72.0% of pairwise choices correctly versus 74.8% for the bounds—a relative loss of only ~6%. The headline message: restrictive simple functional forms sacrifice very little predictive power and remain useful representations of risk preferences.

## Research question
How large is the cost, measured as lost out-of-sample predictive success, of imposing a simple parametric functional form on preferences relative to staying within the most conservative non-parametric structure consistent with observed choice? Equivalently: are popular simple utility specifications (e.g. Disappointment Aversion / Expected Utility with CRRA) "good enough" predictors of behavior under risk despite known structural violations, and can the gap to a non-parametric benchmark be quantified as the price of those extra assumptions?

## Method / identification
A two-part **adaptive experimental design** (building on Halevy, Persitz, and Zrill 2018). In **Part 1**, 171 subjects choose portfolios $x_i=(x_{i1},x_{i2})$ of state-contingent tokens from linear budget sets with normalized prices $p_i$ and two equally likely states (22 budget-set observations per subject). From these data, preferences are recovered two ways, automatically and within three minutes:

(1) **Parametric**: a two-parameter Disappointment Aversion (DA) model ([[@Gul1991|Gul 1991)]], which nests Expected Utility and equals Rank-Dependent Utility under two equally likely states:
$$u(x_{i1},x_{i2})=\gamma\,w\!\left(\max\{x_{i1},x_{i2}\}\right)+(1-\gamma)\,w\!\left(\min\{x_{i1},x_{i2}\}\right)$$
with $\gamma=\frac{1}{2+\beta}$, $\beta>-1$, and CRRA utility-for-gains $w(z)=\frac{z^{1-\rho}}{1-\rho}$ for $\rho\ge 0,\ \rho\ne 1$ (and $w(z)=\ln z$ at $\rho=1$). Here $\gamma$ is the weight on the better outcome: $\beta>0$ is disappointment aversion (better outcome under-weighted), $\beta<0$ is elation seeking, and $\beta=0$ collapses to EU. Parameters are recovered by minimizing the **Money Metric Index (MMI)**, the income-metric incompatibility between revealed preferences and the parametric ranking.

(2) **Non-parametric**: Varian (1982) bounds on indifference curves—the revealed-preferred set $RP(x)$ and revealed-worse set $RW(x)$. Zrill's main methodological innovation handles subjects who violate GARP, for whom $RP(x_1)$ and $RW(x_1)$ overlap so no separating indifference curve exists. He takes the vector of optimal budget adjustments $v$ from the **Varian Inconsistency Index** (Varian 1990)—the minimal proportional budget perturbations that remove preference cycles—and builds a modified relation $R_v$ with $v$-revealed sets $RW_v(x)$ and $RP_v(x)$ whose interiors are necessarily disjoint (Theorem 1 of Halevy-Persitz-Zrill 2018). These "generalized" bounds encode only the $v$-rationalizable preference content and represent the subject's "approximate" preferences. Convexity is imposed when the recovered $\beta\ge 0$ (quasi-concave $u$); symmetry is added for subjects with no first-order-stochastic-dominance violations.

In **Part 2**, an algorithm constructs 18 individually tailored pairwise comparisons between a Part-1 portfolio $x_A$ and an algorithm-generated $x_B$, searched along the 45-degree line and the budget boundary, and classifies each by whether the two recovery methods agree: **Type A (Agree)** $u(x_B)>u(x_A)$ with $x_B\in RP_v(x_A)$ (or the reverse); **Type D (Disagree)** $u(x_B)>u(x_A)$ but $x_B\in RW_v(x_A)$ (or the reverse); **Type U (Unidentified)** $x_B\notin RP_v(x_A)\cup RW_v(x_A)$, where the bounds are silent and only the parametric model speaks. Target mixture: 9 Type U, 5 Type A, 4 Type D. Crucially, choice sets for Part 2 are drawn from *binary* comparisons while estimation used *linear budget* sets—a genuine out-of-sample, cross-frame test exploiting the portability of structural models. The author concedes the comparison-construction algorithm is "admittedly ad hoc."

## Data
Original lab data: **171 subjects** (ORSEE/UBC Vancouver School of Economics, Oct 2018 & Mar 2019; mostly undergraduates), 40 choices each (22 budget-set + 18 pairwise), ~45-minute sessions, mean earnings CAD \$27.25. Data quality is high: 98.8% of subjects have <5% efficiency loss, 40.7% pass GARP outright; median DA misspecification is 3.8% of income, with 69.5% under 5%. Substantial preference heterogeneity, including 23.4% elation-seeking subjects.

## Key findings
- **Aggregate**: DA model predicts **72.0%** of all pairwise choices correctly (2085/2894); non-parametric bounds predict **74.8%** (696/931) of the comparisons they identify. Interpreting the latter as an approximate upper bound for any deterministic model that $v$-rationalizes the data, the **relative loss from the parametric restriction is only 6.1% (4.6 percentage points, 74.8% vs 70.2% on Type U)**.
- **By type**: DA predicts Type A 77.8%, Type U 70.2%, Type D 56.0% (Table 2).
- **Individual level**: median subject predictive success 72.2% (~13/18); the model beats 50% for all but 14/171 subjects (8.2%). Non-parametric median is 80.0% vs 71.4% parametric on identified pairs; but the individual-level cost is noisy—negative for 37.8% of subjects (small per-subject samples of identified pairs).
- **Simulation/null**: predicting a subject's choices with *other* subjects' recovered parameters yields much worse fit; a one-sided Wilcoxon paired-sign test strongly rejects ($z=8.24$, $p\approx 0$), confirming the comparisons were non-trivial and the algorithm was not rigged toward success.
- **Robustness**: alternative specifications (DA with CARA, EU with CRRA) perform similarly to DA-CRRA, while the Expected Value model (no curvature) does markedly worse (54.4% overall)—evidence that utility curvature matters and the design poses a genuine test.

## Contribution
First lab test of the *predictive* (not within-sample) success of non-parametric revealed-preference bounds, and first use of those bounds as an out-of-sample benchmark / approximate upper bound against which to price the assumptions of a parametric model. Methodologically, it introduces a way to construct non-parametric bounds for GARP-violating subjects by reusing the Varian-Inconsistency-Index budget adjustments to define a $v$-revealed preference relation—characterizing the preferences "closest" to simple utility maximization. Substantively, it provides a proof of concept that the Halevy-Persitz-Zrill adaptive design generalizes from comparing estimators to comparing whole models, and offers reassurance to applied/structural behavioral economists that simple CRRA-type forms lose little predictive power while gaining tractability, portability, and interpretability.

## Limitations & open questions
The author is explicit about several open problems:
- **Ad hoc comparison-selection algorithm**: relies on the author's "accumulated wisdom" to trade off non-trivial vs robust comparisons; an *explicit optimality criterion* for selecting pairwise comparisons is "left for future work" and acknowledged as "very challenging."
- **Single environment**: tested only for decision-making under risk with two equally likely states; generalization to richer/more complex environments is unverified, and "more work is required in order to understand its limitations."
- **Individual-level cost is poorly identified**: small per-subject numbers of non-parametrically identified pairs (median subject has only 6 identified, 15 have none); future designs should collect *more identified comparisons per subject*.
- **Choice of inconsistency index**: only the Varian Inconsistency Index is used; whether CCEI, Houtman-Maks, money-pump, or other indices yield better adjustments is left open.
- **Non-nesting**: the non-parametric bounds do not nest the parametric model, so the "upper bound" is only approximate and can be beaten by the misspecified parametric model for some subjects; tighter constructions (e.g. via Polisson-Quah-Renou 2020 or MMI-based adjustments) are noted as possible extensions.
- **Extending the recoverability method** beyond simple utility maximization to demanding models (expected-utility, homothetic, correlation-neutral preferences) is flagged as a natural extension.

## Connections
The design directly extends **Halevy, Persitz, and Zrill (2018)** (same Part-1 elicitation, MMI vs NLLS recovery, Theorems 1-2 underpinning the bounds and misspecification measure) and the linear-budget elicitation of **Choi et al. (2007, 2014)**, with antecedents in **[[@Andreoni2002|Andreoni and Miller (2002)]]** and **[[@Fisman2007|Fisman, Kariv, and Markovits (2007)]]** for other-regarding preferences and **Andreoni and Sprenger (2012)** for intertemporal choice. The parametric model is **[[@Gul1991|Gul's (1991)]]** Disappointment Aversion; the non-parametric machinery rests on **Afriat (1967)**, **Varian (1982, 1990)**. Goodness-of-fit and approximate-rationalization links connect to **Polisson, Quah, and Renou (2020)**, **Echenique, Imai, and Saito (2021)**, **de Clippel and Rozen (2020)**, **Heufer and Hjertstrand (2019)**, **Nishimura, Ok, and Quah (2017)**, **Aguiar, Hjertstrand, and Serrano (2020)**, and the income-expansion-path approach of **Blundell, Browning, and Crawford (2003, 2008)**. The out-of-sample-prediction framing parallels machine-learning train/test logic (**Mullainathan and Spiess 2017**), the completeness/predictability discussion of **Fudenberg et al. (2021)**, and cross-validation work by **[[@Peysakhovich2017|Peysakhovich and Naecker (2017)]]** and **Breig (2020)**. Related adaptive-design work includes **DOSE** (**Chapman et al. 2018**; **Camerer and Imai 2018**), and the structural-behavioral-estimation concerns of **[[@DellaVigna2018|DellaVigna (2018)]]**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
