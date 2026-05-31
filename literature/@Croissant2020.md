---
citekey: Croissant2020
title: "Estimation of Random Utility Models in R: The mlogit Package"
authors: ["Croissant, Yves"]
year: 2020
type: journalArticle
doi: 10.18637/jss.v095.i11
zotero: "zotero://select/library/items/9ZL8EPSK"
pdf: /Users/jesper/Zotero/storage/THSJIQFD/Croissant2020.pdf
tags: [literature]
keywords: [discrete-choice, random-utility-models, mixed-logit, nested-logit, maximum-simulated-likelihood, r-package]
topics: ["[[discrete-choice-econometrics]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> mlogit is a package for R which enables the estimation of random utility models with choice situation and/or alternative specific variables. The main extensions of the basic multinomial model (heteroscedastic, nested and random parameter models) are implemented.

## Summary
This is the *Journal of Statistical Software* article documenting the R package **mlogit**, a unified maximum-likelihood toolkit for estimating random utility (discrete choice) models. It walks through the data-management and formula interface, the landmark multinomial logit (MNL) model, two extensions that relax the i.i.d. Gumbel error assumption (the heteroscedastic logit and the nested logit), and the random-parameters (mixed) logit estimated by simulation. The paper is part software manual, part econometric primer, drawing heavily on Train (2009) for the theory. Because this is a 41-page software article with extensive code listings, I read it in a targeted way: front matter, introduction, the model-description/formula section, and each model's formal derivation and worked example, sampling but not transcribing the R output blocks.

## Research question
Not a hypothesis-testing paper. The motivating problem is practical and infrastructural: how to provide a single, consistent R interface and estimator for the full family of random utility models, given that the standard formula-data interface cannot naturally express choice problems where covariates may be alternative-specific, choice-situation-specific, or both, and where coefficients may be generic or alternative-specific.

## Method / identification
The unifying framework is the random utility model: decision maker $i$ chooses alternative $j$ that maximizes utility $U_{ij}=V_{ij}+\epsilon_{ij}$, where the observable part for the package's general specification is
$$V_{ij}=\alpha_j+\beta x_{ij}+\nu t_j+\gamma_j z_i+\delta_j w_{ij}.$$
Because only utility differences matter, identification requires normalizing choice-situation-specific coefficients (e.g., the intercept and $\gamma_j$) by setting one alternative's value to zero; with $J$ alternatives only $J-1$ such coefficients are identified. Pure alternative-specific variables $t_j$ force dropping intercepts to avoid perfect multicollinearity.

The package expresses these covariate classes through a three-part `Formula` object (`choice ~ generic | choice-situation-specific | alternative-specific`) over data indexed by three keys: alternative (`alt`), choice situation (`chid`), and individual (`id`), handled in both "wide" and "long" shapes via the companion `dfidx` package.

Models implemented:
- **MNL**: i.i.d. Gumbel errors give the closed-form $P_{il}=e^{\beta^\top x_{il}}/\sum_j e^{\beta^\top x_{ij}}$, estimated by Newton-Raphson (globally concave log-likelihood).
- **Heteroscedastic logit** (Bhat 1995): alternative-specific error scales $\theta_j$ break the i.i.d. assumption; the choice probability becomes a one-dimensional integral $P_l=\int \prod_{j\neq l} \exp(-e^{-(V_l-V_j-\theta_l\ln t)/\theta_j})\,e^{-t}\,dt$.
- **Nested logit**: alternatives grouped into nests; estimated either jointly or sequentially via inclusive values $\mathrm{iv}_{ig}=\ln\sum_{j\in B_g}e^{\beta^\top x_{ij}}$, with nest elasticities (the $\mathrm{iv}$ coefficients) governing within-nest correlation.
- **Mixed / random-parameters logit (MXL)**: coefficients $\beta_i$ are random draws from $f(\beta,\theta)$; the unconditional probability is the $K$-dimensional integral $P_{il}(x_i,\theta)=\int \big(e^{\beta^\top x_{il}}/\sum_j e^{\beta^\top x_{ij}}\big) f(\beta,\theta)\,d\beta$, estimated by **maximum simulated likelihood** averaging over $R$ draws. Individual-level posteriors are recovered as choice-probability-weighted averages $\hat\beta_i=\sum_r P_{ir}\beta_r/\sum_r P_{ir}$. Available mixing distributions: normal, log-normal, censored-normal, uniform, triangular, plus zero-bounded variants; panel structure is accommodated by holding $\beta_i$ fixed across an individual's repeated choices.

Testing is unified across all models via the Wald, likelihood-ratio, and Lagrange-multiplier (score) tests; the score test is highlighted as especially convenient because it only requires the (easier) constrained model.

## Data
None original. The package ships illustrative datasets used as running examples: `Train` (a Dutch stated-preference rail survey, wide format), `ModeCanada` (intercity travel mode choice), an environmental-compliance choice dataset (electricity firms under different regulatory regimes), and `JapaneseFDI` (Head and Mayer 2004; choice among 57 European regions in 9 countries by Japanese firms, used to illustrate nested logit with regions nested in countries).

## Key findings
As a software paper the "findings" are demonstrations of capability rather than theorems: the MNL on `ModeCanada` yields a globally concave likelihood estimated in a handful of Newton-Raphson iterations (McFadden $R^2\approx0.31$); the environmental-compliance example shows scale heterogeneity across regulatory regimes, with a likelihood-ratio test strongly rejecting coefficient equality up to a scalar; the `JapaneseFDI` nested-logit example shows the four testing principles agreeing in rejecting both "no nests" (all elasticities equal one) and "unique nest elasticity" hypotheses. The substantive contribution is that all of these heterogeneous models live under one estimation interface with shared post-estimation methods (fitted probabilities, inclusive values, marginal effects, consumer surplus, individual parameters).

## Contribution
Provides the first and most comprehensive R package for the random utility model family under a single interface, documented to JSS standards. Beyond software, the article is a compact, self-contained exposition of the econometrics of discrete choice — covariate taxonomy, identification/normalization, the i.i.d.-relaxing logit extensions, and simulation-based mixed logit — making it a standard methodological reference and reproducible-research artifact for applied choice modeling.

## Limitations & open questions
The author explicitly notes several models that exist in the package but are *not* covered in the article (deferred to vignettes), which double as scope boundaries: the **rank-ordered logit** (for ranked rather than single-choice data), the **overlapping nested logit** (alternatives in more than one nest), the **paired combinatorial logit** (every pair of alternatives forms a nest), and the **multinomial probit** (multivariate-normal errors). The paper also flags practical estimation pitfalls rather than open theory: unbounded mixing distributions (especially log-normal, with its heavy left tail) can produce implausible moments such as infinite willingness-to-pay, motivating bounded or zero-bounded distributions; and the $K$-dimensional MXL integral has no quadrature solution, forcing reliance on simulation whose draw count $R$ trades off accuracy against cost.

## Connections
The theoretical backbone follows McFadden (1974, 1978) on conditional/multinomial logit and Train (2009) for the modern synthesis. The heteroscedastic logit is due to Bhat (1995); nested logit normalization issues connect to Daly (1987), Heiss (2002), and Hensher and Greene (2002); finite-moment concerns for willingness-to-pay in random-coefficient models follow Daly, Hess, and Train (2012). On the software side it situates mlogit against neighboring R packages: gmnl (Sarrias and Daziano 2017) for generalized and latent-class mixed logit, mnlogit (Hasan, Wang, and Mahani 2016) for fast MNL, and Bayesian alternatives bayesm (Rossi 2019), MNP (Imai and van Dyk 2017), and RSGHB. The companion infrastructure packages are dfidx and the Formula package (Zeileis and Croissant 2010); the JapaneseFDI application is from Head and Mayer (2004).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
