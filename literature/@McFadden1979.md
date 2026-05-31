---
citekey: McFadden1979
title: "Quantitative Methods for Analysing Travel Behaviour of Individuals: Some Recent Developments"
authors: ["McFadden, Daniel"]
year: 1979
type: bookSection
doi: ""
zotero: "zotero://select/library/items/ZAWX7LBX"
pdf: /Users/jesper/Zotero/storage/QIYFN9WJ/McFadden1979.pdf
tags: [literature]
keywords: [discrete-choice, random-utility, multinomial-logit, generalized-extreme-value, choice-based-sampling, travel-demand, nested-logit, aggregation]
topics: ["[[discrete-choice-econometrics]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This chapter is concerned with quantitative methods for the analysis of travel behaviour of individuals. It reviews some of the recent developments in model specification, estimation, model evaluation and testing, and aggregation and forecasting. Topics in model specification include the multinomial-probit model and its computation, and generalised-extreme value models and their relation to sequential models. Topics in estimation methods include the use of choice-based samples, sample designs and incomplete choice sets. Model evaluation topics include prediction-success tables and diagnostic tests of specification. Aggregation and forecasting topics include aggregation by the Clark method, synthesis of the distribution of explanatory variables, and the calculus of demand elasticities.

## Summary
A wide-ranging methodological survey (Cowles Discussion Paper 474, 1977) that pulls together the late-1970s state of the art in disaggregate discrete-choice modeling, organized around five pillars: model specification (MNL, nested/sequential MNL, MNP, GEV), statistical estimation (maximum likelihood, choice-based and stratified sampling, estimation from sampled choice sets), computation of the MNP via the Clark approximation, model evaluation (likelihood-ratio index, prediction-success tables), and aggregation/forecasting (Clark-method aggregation, synthesis of explanatory-variable distributions, an elasticity calculus). Though framed as travel-demand analysis, the toolkit is the general machinery of random-utility discrete choice and the paper is foundational for structural choice modeling far beyond transportation.

## Research question
What quantitative tools are available — and what are their statistical and computational properties — for specifying, estimating, evaluating, and forecasting with disaggregate (individual-level) models of discrete choice? Concretely: which random-utility specifications relax the MNL independence-from-irrelevant-alternatives (IIA) restriction while remaining tractable, how can such models be estimated consistently from non-random (choice-based, stratified, subset) samples, and how are disaggregate estimates aggregated into population forecasts and policy-relevant elasticities?

## Method / identification
This is a survey of formal results rather than an empirical study; the "method" is a synthesis of random-utility theory and its estimators.

- **MNL and nested/sequential MNL.** The joint MNL for mode–destination–auto choice is $P_{mda}=e^{V_{mda}}/\sum_{n,c,b}e^{V_{ncb}}$, decomposable via inclusive values $I_{da}=\log\sum_n e^{\alpha x_{nda}}$ into conditional/marginal logits. The sequential (nested) model relaxes the constraint that inclusive-value coefficients equal one: it is identical to joint MNL only when $\theta=\lambda=1$.
- **GEV.** A central theorem (McFadden 1977): if $G(y_1,\dots,y_J)$ is nonnegative, homogeneous of degree one, with $\lim_{y_i\to+\infty}G=+\infty$ and mixed partials $\partial^k G/\partial y_{i_1}\cdots\partial y_{i_k}$ nonnegative for odd $k$ and nonpositive for even $k$, then $P_i=e^{V_i}G_i(e^{V_1},\dots,e^{V_J})/G(e^{V_1},\dots,e^{V_J})$ is a utility-consistent choice model. MNL is the special case $G=\sum_j y_j$; nesting $G$ (e.g. eq. 18 with similarity parameters $0\le\sigma_m<1$) yields the nested-logit family.
- **Daly–Zachary / consistency result.** Using $\bar U(V_1,\dots,V_J)=\mathbb{E}\,\mathrm{Max}_j U_j$, choice probabilities are the gradient $P_i=\partial \bar U/\partial V_i$, and the necessary-and-sufficient condition for a three-level nested logit to be consistent with random utility maximization is that every inclusive-value coefficient lie in $(0,1]$.
- **MNP.** Utilities are jointly normal; choice probabilities are $(J-1)$-dimensional normal integrals — exact only by numerical integration, impractical for $J\ge5$.
- **Estimation theory.** Maximum likelihood for random samples; the Manski–McFadden (1977) general theory of estimation under arbitrary stratified sampling, distinguishing exogenous from endogenous ("choice-based") sampling, and giving consistent estimators (full-information ML eq. 38, 42; the Lerman–Manski WESML weighted estimator eq. 39, $w(i)=Q(i)/H(i)$; Manski–McFadden estimators eq. 40, 41) keyed to which marginals $p(z)$, $Q(i)$ are known.
- **Estimation from sampled choice sets.** Theorem 2: for MNL, if the choice-set assignment rule $\pi(D\mid i,z)$ satisfies the *positive conditioning property* ($j\in D,\pi(D\mid i)>0\Rightarrow\pi(D\mid j)>0$), a modified likelihood adding $\log\pi(D\mid\cdot)$ correction terms is consistent; under the stronger *uniform conditioning property* it reduces to the standard subset likelihood. This exploits IIA to calibrate MNL from a strict subset of the choice set.

## Data
None — this is a methodological review with no original dataset. Illustrative numerical results (Tables 2–3) on asymptotic efficiency of choice-based sample designs are adapted from Cosslett (1977) for stylized probit/logit/arctan models.

## Key findings
- **GEV characterization theorem** giving closed-form, utility-consistent choice probabilities for an entire family generalizing MNL and nested logit.
- **Nesting consistency condition**: nested/sequential MNL is consistent with random-utility maximization iff each inclusive-value coefficient lies in $(0,1]$; $1-\theta$ and $1-\lambda$ index the similarity of alternative modes and destinations.
- **Choice-based sampling**: naively treating choice-based samples as random yields inconsistent MNL estimates, but the inconsistency is confined to the alternative-specific dummy coefficients. Consistent estimators exist for every information case; efficiency results (Tables 2–3) show knowledge of aggregate shares $Q(1)$ is very valuable, the equal-shares design is robustly near-optimal, and choice-based designs can dominate exogenous sampling, especially for rare alternatives.
- **MNP computation**: the Daganzo–Bouthelier–Sheffi method recursively applies the Clark (1961) approximation (a normal approximating the max of two normals) to reduce a $J$-alternative MNP probability to a univariate integral requiring $J-2$ Clark applications; analytic derivatives are likewise approximable. Accuracy degrades for many alternatives or negatively correlated, similar-mean variates.
- **Model evaluation**: the likelihood-ratio index $\rho^2=1-L/L_0$ defined "about aggregate shares" (so $L_0$ uses sample shares), with the caution that $\rho^2$ of 0.2–0.4 already represents an excellent fit; plus the prediction-success table and success index $\sigma_i=N_{ii}/N_{\cdot i}-N_{\cdot i}/N_{\cdot\cdot}$.
- **Aggregation/forecasting**: the Clark-method aggregation computes population shares $Q(i)=\int H_i(u,\dots,u)\,du$ without intermediate per-individual choice probabilities; SYNSAM-style synthesis (Cosslett et al. 1977, via iterative proportional fitting) builds explanatory-variable distributions from Census data; and a four-rule elasticity calculus (aggregation over segments, over alternatives, component effects, multiple effects) yields policy-relevant elasticities.

## Contribution
Consolidates and extends the random-utility discrete-choice program: it states the GEV theorem and the nested-logit consistency condition, packages the Manski–McFadden stratified-sampling estimation theory and choice-based-sampling results, makes MNP computationally practical via the Clark approximation, and supplies the evaluation and aggregation apparatus ($\rho^2$, prediction-success tables, Clark aggregation, the elasticity calculus) that became standard in applied choice modeling. It is a key bridge between McFadden's 1973 MNL theory and the broader GEV/MNP/sampling literature, much of which underlies his later Nobel-recognized work.

## Limitations & open questions
The paper itself flags several open problems (each a project hook):
- **Finite-sample properties of ML are largely unknown**; limited Monte Carlo suggests ML is unduly sensitive to observations with low fitted probabilities (non-robust to specification/measurement error). Berkson–Theil estimators may be preferable when grouping is possible (rare with travel data); robust alternatives like NLLS (eq. 56) are consistent but less efficient and underused empirically.
- **Improving the Clark approximation**: it tends to underestimate small probabilities (skew of the max of normals) and worsens with many alternatives; the author suggests empirically adjusting the Clark formulae or adapting the methodology to GEV-distributed variates (whose maxima are again GEV, bounding error as $J$ grows).
- **Sample-design selection** generally requires a Bayesian approach with priors on parameters; optimal $H(1)$ is sensitive to the model and parameter value, leaving the choice of design genuinely open.
- **IIA validity must be tested per application**; the McFadden–Tye–Train diagnostic tests (universal-logit, subset-consistency, and residual-based tests) are sketched but not fully developed here.
- **Specification tests where the universe of alternatives cannot be enumerated** (e.g. MNL vs. MNP, or which travel-time measure is correct) are noted as requiring statistical-decision-theory methods "beyond the scope of this paper."
- The concluding remark that "the task of establishing a firm analytic and statistical foundation for the subject has just begun" is an explicit invitation.

## Connections
Builds directly on McFadden (1973, "Conditional Logit Analysis") for MNL and on the GEV result of McFadden (1977, residential location). The nested-logit consistency result connects to Ben-Akiva (1973), Daly–Zachary (1976), Williams (1977), and Ben-Akiva–Lerman (1977), who independently derived the disjoint-nest form; the social-welfare/consumer-surplus identity via $\bar U=\mathbb{E}\,\mathrm{Max}\,U$ links to Domen/cich–McFadden (1975) and Harris–Tanner. Choice-based and stratified-sampling estimation rests on Lerman–Manski (1976), Manski–McFadden (1977), and Cosslett (1977); MNP computation on Thurstone (1927), Bock–Jones (1968), Hausman–Wise (1976), Manski (1976), Daganzo–Bouthelier–Sheffi (1976), and Clark (1961). Aggregation draws on McFadden–Reid (1975), Koppelman (1975), and the SYNSAM synthesis (Cosslett, Duguay, Jung, McFadden 1977) via Deming–Stephan (1940) iterative proportional fitting. The whole forms the methodological backbone for structural discrete-choice estimation in industrial organization, labor, and environmental economics, and prefigures modern mixed-logit and simulation-based estimation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
