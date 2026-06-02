---
citekey: Fudenberg2020
title: Quantifying the Restrictiveness of Theories
authors: ["Fudenberg, Drew", "Gao, Wayne", "Liang, Annie"]
year: 2020
type: journalArticle
doi: 10.2139/ssrn.3580408
zotero: "zotero://select/library/items/J9PEL8IR"
pdf: /Users/jesper/Zotero/storage/QXNFQYTS/Fudenberg2020.pdf
tags: [literature]
keywords: [model-restrictiveness, model-completeness, prospect-theory, cognitive-hierarchy, model-selection, behavioral-economics]
topics: ["[[ml-evaluating-economic-theories]]"]
related: [Bruhin2010, Fudenberg2019a, Fudenberg2019b, Gul1991, Peysakhovich2017, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We propose a new way to quantify the restrictiveness of an economic model, based on how well the model fits simulated, hypothetical data sets. The data sets are drawn at random from a distribution that satisfies some application-dependent content restrictions (such as that people prefer more money to less). Models that can fit almost all hypothetical data well are not restrictive. To illustrate our approach, we evaluate the restrictiveness of popular behavioral models in two experimental settings—certainty equivalents and initial play—and explain how restrictiveness reveals new insights about each of the models.

## Summary
The paper introduces *restrictiveness*: a model-fit diagnostic that asks not how well a parametric model fits the real data, but how well it can fit *hypothetical* data drawn at random from an analyst-specified set of "conceivable" behaviors. A model that approximates almost any conceivable data is unrestrictive (it imposes little structure beyond background assumptions); one that fits most synthetic data poorly is restrictive. Paired with the authors' earlier *completeness* measure (fit on real data), restrictiveness lets one judge whether a model's empirical success reflects captured structure or mere flexibility. Applied to Cumulative Prospect Theory (CPT), Disappointment Aversion (DA), and cognitive-hierarchy models of initial play, the measure overturns naive parameter-counting intuitions: a 3-parameter CPT is quite flexible, whereas 1-2 parameter game-theoretic models are extremely restrictive.

## Research question
When a parametric model fits observed data well, is that because it captures regularities specific to the data, or because it is flexible enough to fit nearly any conceivable data? The paper seeks a quantitative, easy-to-compute measure of model restrictiveness that does not require analytical results (representation theorems, VC dimension) about the model's empirical content, and is independent of how much real data is available.

## Method / identification
Let $X$ be an observable feature vector on a finite set $\mathcal{X}$ with known marginal $P_X^*$, and $Y$ an outcome. The analyst learns a statistic $s(P^*_{Y\mid X=x})$ via a *predictive mapping* $f:\mathcal{X}\to\mathcal{S}$; the true mapping is $f^*(x):=s(P^*_{Y\mid X=x})$, and $\mathcal{F}$ is the set of all mappings. Two leading cases: predicting a conditional expectation with squared loss $l(f,(x,y))=(y-f(x))^2$ (discrepancy $d_{MSE}$), and predicting a conditional distribution with negative log-likelihood loss (discrepancy $d_{KL}$, the expected Kullback-Leibler divergence).

To measure restrictiveness of a parametric model $F_\Theta=\{f_\theta\}_{\theta\in\Theta}$, the analyst fixes a *conceivable set* $F_M\subseteq\mathcal{F}$ (encoding background knowledge, e.g. first-order stochastic dominance) and a prior $\mu\in\Delta(F_M)$, typically uniform. For a drawn mapping $f$, the model's approximation error is $d(F_\Theta,f):=\inf_{\theta\in\Theta} d(f_\theta,f)$, normalized by a naive benchmark $f_{naive}\in F_\Theta$ to give the *f-discrepancy*

$$\delta_f := \frac{d(F_\Theta,f)}{d(f_{naive},f)} \in [0,1].$$

Restrictiveness is $r := \mathbb{E}_\mu[\delta_f]$. Completeness ([[@Fudenberg2019a|Fudenberg et al. 2019]]) is the dual on real data: $\kappa^* := 1-\delta_{f^*}$, the fraction of the naive-to-best error reduction the model achieves. Restrictiveness is estimated by Monte Carlo: draw $M$ mappings, average $\delta_m$; the estimator $\bar\delta_M$ is asymptotically normal ($\sqrt{M}(\bar\delta_M - r)/\hat\sigma_\delta \to N(0,1)$, Proposition 1). Completeness is estimated via $K$-fold cross-validation ($K=10$) and is also asymptotically normal (Theorem 1), so confidence intervals are available for both. The CI on $r$ reflects only simulation error, not sampling error in the data.

## Data
Two experimental datasets. Application 1: 25 binary lotteries $(z,\underline z,p)$ from [[@Bruhin2010|Bruhin et al. (2010)]], 8906 observations, outcome = reported certainty equivalents (also a loss-domain set and 18 three-outcome lotteries from Bernheim & Sprenger 2020). Application 2: 466 unique $3\times 3$ matrix games from [[@Fudenberg2019b|Fudenberg & Liang (2019)]], each a vector in $\mathbb{R}^{18}$, outcome = distribution of row-player initial play over three actions. Synthetic data for restrictiveness are generated from uniform $\mu$ over FOSD-respecting mappings (lotteries) or weak dominance-respecting mappings (games).

## Key findings
- **CPT vs DA (Definitions 1-3, Table 1):** CPT is 95% complete but only moderately restrictive ($r=0.32$); DA is just 27% complete yet more restrictive ($r=0.46$). So CPT's empirical success partly reflects flexibility, but the composite $r-(1-\kappa^*)$ is $+0.27$ for CPT vs $-0.27$ for DA—CPT's completeness more than compensates.
- **Parameter count is misleading:** Nested specifications show that nonlinear probability-weighting parameters buy more completeness per unit of lost restrictiveness than utility-curvature parameters; three CPT parameter combinations are dominated (both less complete and less restrictive than alternatives). CPT is about twice as restrictive on three-outcome lotteries ($r=0.63$) as on binary ones, quantifying the extra bite of rank dependence.
- **Initial play (Section 6):** PCHM, Logit Level-1, and Logit PCHM are 43.6%, 72.7%, 72.9% complete but *all extremely restrictive* ($r=0.993, 0.969, 0.972$; every f-discrepancy $\ge 0.943$). Logit Level-1 and Logit PCHM are nearly identical in both measures despite dissimilar functional forms, suggesting initial play is largely unstrategic.
- **Robustness:** restrictiveness is insensitive to perturbing $\mu$ to nearby beta distributions (bounded by total variation, eq. 4) and to dropping FOSD.

## Contribution
A practical, model-agnostic complexity measure for economic theories that, unlike AIC/BIC or cross-validation, embodies an *intrinsic* preference for parsimony independent of sample size, and unlike VC dimension or Selten's (1991) area measure requires no representation theorem—only the ability to numerically fit synthetic data. It supplies estimators and asymptotic inference for both restrictiveness and completeness, and demonstrates that the two together give a richer model-evaluation criterion than either alone.

## Limitations & open questions
The authors leave several explicit hooks: how to combine $\kappa^*$ and $r$ into a single criterion (lexicographic, $r-(1-\kappa^*)$, or the quantile of $\delta_{f^*}$) is left to the analyst's discretion. The choice of $F_M$ and $\mu$ is guided by intuition, not formal principle—analogous to choosing alternatives for a power calculation. If a model with an economically interpretable parameter proves unrestrictive, how should its estimated parameter value be interpreted? They note the narrative may not map onto the parameter's economic meaning and leave this to future work. Extension to continua of features / infinite-dimensional $F_M$ (Section 8, Appendix F) and to subject-level heterogeneity is sketched but not fully developed. A broad open direction: quantifying how restrictive economic models are relative to nearly nonparametric machine-learning approaches.

## Connections
Builds directly on the *completeness* measure of [[@Fudenberg2019a|Fudenberg, Kleinberg, Liang & Mullainathan (2019)]] and the initial-play data and analysis of [[@Fudenberg2019b|Fudenberg & Liang (2019)]]. The restrictiveness idea revises Koopmans & Reiersol (1950) on observational restrictiveness and Selten (1991), whose pass-rate/area measure it generalizes by using approximate rather than exact fit and by normalizing against a naive benchmark. It is close in spirit to Bronars (1987)'s power evaluation of Varian's (1982) GARP test, and to Afriat-index work by Choi et al. (2007) and Polisson, Quah & Renou (2020). The models studied are Cumulative Prospect Theory ([[@Tversky1992|Tversky & Kahneman 1992]]; weighting form from Goldstein & Einhorn 1987 and Lattimore et al. 1992), Disappointment Aversion ([[@Gul1991|Gul 1991]]; parametrization from Routledge & Zin 2010), and the Poisson Cognitive Hierarchy Model (Camerer, Ho & Chong 2004), with logit variants from Wright & Leyton-Brown (2014) and level-k roots in Stahl & Wilson (1994, 1995) and Nagel (1995). Related complexity notions include VC dimension (applied to choice under uncertainty by Basu & Echenique 2020), and the completeness result connects to [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] on CPT versus lasso.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
