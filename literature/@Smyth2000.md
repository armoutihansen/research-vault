---
citekey: Smyth2000
title: Model selection for probabilistic clustering using cross-validated likelihood
authors: ["Smyth, Padhraic"]
year: 2000
type: journalArticle
doi: "10.1023/A:1008940618127"
zotero: "zotero://select/library/items/4SGYP67I"
pdf: /Users/jesper/Zotero/storage/KCL6PBD6/Smyth2000.pdf
tags: [literature]
keywords: [cross-validation, model-selection, finite-mixture-models, probabilistic-clustering, number-of-components, kullback-leibler]
topics: []
related: [Dempster1977]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Cross-validated likelihood is investigated as a tool for automatically determining the appropriate number of components (given the data) in finite mixture modeling, particularly in the context of model-based probabilistic clustering. The conceptual framework for the cross-validation approach to model selection is straightforward in the sense that models are judged directly on their estimated out-of-sample predictive performance. The cross-validation approach, as well as penalized likelihood and McLachlan's bootstrap method, are applied to two data sets and the results from all three methods are in close agreement. The second data set involves a well-known clustering problem from the atmospheric science literature using historical records of upper atmosphere geopotential height in the Northern hemisphere. Cross-validated likelihood provides an interpretable and objective solution to the atmospheric clustering problem. The clusters found are in agreement with prior analyses of the same data based on non-probabilistic clustering techniques.

## Summary
Smyth proposes using **cross-validated likelihood** (specifically Monte-Carlo cross-validation, MCCV) as a model-selection criterion for choosing the number of components $k$ in finite mixture models used for probabilistic clustering. The idea is conceptually simple: rather than penalize the likelihood (AIC/BIC) or compute a full Bayesian posterior over $k$, one repeatedly partitions the data, fits each candidate model on a training portion, and scores it by its out-of-sample log-likelihood. The expected out-of-sample log-likelihood is shown to be an unbiased (up to an additive constant) estimator of the Kullback-Leibler distance from the truth, giving the criterion a clean justification. On a diabetes data set and a well-known atmospheric "regime" clustering problem, cross-validation, BIC, and McLachlan's bootstrap all agree, selecting $k=3$, and the recovered atmospheric clusters reproduce earlier non-probabilistic results.

## Research question
For finite-mixture-based probabilistic clustering, how can one objectively and automatically determine the number of components $k$ given the data, in a way that is conceptually transparent and trusted by domain scientists, rather than relying on penalized-likelihood approximations or fully Bayesian posteriors whose results depend opaquely on the quality of the underlying approximation?

## Method / identification
A finite mixture density with $k$ components is
$$f^{(k)}(x\mid\Phi^{(k)})=\sum_{j=1}^{k}\alpha_j\, g_j(x\mid\theta_j),\qquad \sum_j\alpha_j=1,\ \alpha_j>0,$$
with parameters $\Phi^{(k)}=\{\alpha_1,\dots,\alpha_k,\theta_1,\dots,\theta_k\}$ estimated by maximum likelihood via the EM algorithm (with multiple random and $k$-means initializations to avoid poor local maxima, and a floor on component variances to exclude singular edge solutions).

The training log-likelihood $l_k^{train}$ is non-decreasing in $k$, so it cannot select $k$. Smyth instead targets the test log-likelihood $l_k^{test}=l(\hat\Phi^{(k)}(D^{train})\mid D^{test})$. Defining the per-sample negative test log-likelihood $i_k=-l_k^{test}/N_{test}$, he shows
$$E[i_k]=\int f(x)\log\frac{f(x)}{f_k(x)}\,dx+\int f(x)\log\frac{1}{f(x)}\,dx,$$
i.e. the **KL distance** between the true density $f$ and the fitted $f_k$ plus a $k$-independent entropy constant. Thus the test log-likelihood is an unbiased estimator (within a constant) of KL distance, motivating it as a selection criterion.

Lacking a true hold-out set, he estimates $l_k^{test}$ by cross-validation over $M$ partitions:
$$l_k^{cv}=\frac{1}{M}\sum_{i=1}^{M} l\!\left(\hat\Phi^{(k)}(D\setminus S_i)\mid S_i\right),$$
where $S_i$ is the $i$-th evaluation subset and $D\setminus S_i$ the corresponding fitting set. He adopts **Monte-Carlo cross-validation** (Burman's repeated-learning-testing) with test fraction $\beta=0.5$ and $M=100$ partitions, having previously found ($\textit{Smyth 1996}$) that MCCV with $\beta=0.5$ is more reliable than 10-fold CV for choosing $k$. Approximate posterior probabilities on $k$ are obtained by exponentiating and normalizing the cross-validated log-likelihoods under equal priors. The method is benchmarked against BIC ($\text{penalty}=(p_k/2)\log n$) and McLachlan's parametric bootstrap likelihood-ratio test ($B=99$ replications, permitting testing at the 1% level).

## Data
Two real data sets. (1) **Reaven-Miller diabetes data**: 3-dimensional plasma measurements for 145 subjects clinically grouped as normal / chemically diabetic / overtly diabetic; analyzed unlabeled. (2) **Northern Hemisphere atmospheric geopotential height data**: daily NH 700-mb geopotential heights on a $10^\circ\times10^\circ$ grid (541 grid points), with 3960 "winter" days projected onto leading empirical orthogonal functions (EOFs / principal components), dimensions $d=2,\dots,12$; the 12-dimensional version was made publicly available by FTP.

## Key findings
- **KL-distance result**: the (scaled) expected out-of-sample log-likelihood is an unbiased estimator, up to a $k$-independent constant, of the Kullback-Leibler distance between truth and the candidate mixture (equation above), grounding cross-validated likelihood as a principled selection score.
- **Diabetes data**: BIC, cross-validated likelihood, and the bootstrap all select $k=3$, matching the original three-way clinical classification; normalized BIC and CV scores agree closely.
- **Atmospheric data**: all three methods point to $k=3$ Gaussian components; estimated posterior probability on $k=3$ is effectively 1 (and $\geq0.999$ across repeated runs with $M=20$). The three cluster centers, mapped back to physical grids, reproduce Cheng and Wallace's (1993) hierarchical-clustering regimes (Gulf-of-Alaska ridge, southern-Greenland blocking, "Rockies ridge"), providing an objective, independent validation of prior subjective analyses.
- **Robustness / dimensionality**: posterior mass stays on $k=3$ up to $d=6$ EOFs, then switches to $k=1$ as parameter count ($\propto kd^2$) outstrips the fixed data, illustrating the variance penalty of high dimensions. High pattern correlations across $d$ show the EOF projection does not distort the clusters.
- **Practical / sociological point**: atmospheric scientists reported greater willingness to trust a cross-validation criterion (direct out-of-sample interpretation) than a Bayesian analysis perceived as indirect.

## Contribution
Brings cross-validation — standard in supervised learning — into **unsupervised** mixture-model clustering as a transparent criterion for the number of components. It supplies an information-theoretic (KL) justification, demonstrates close agreement with penalized-likelihood and bootstrap methods on real data at comparable (linear-in-resampling, parallelizable) computational cost, and delivers an objective resolution to a long-standing atmospheric-science clustering problem.

## Limitations & open questions
- Cross-validation is less data-efficient than a fully Bayesian approach, since each model is fit on only a fraction of the data; no comparison to Bayesian **MCMC** methods is attempted here.
- No systematic method exists for choosing the test fraction $\beta$ for a problem with unknown structure; $\beta=0.5$ is only an empirically robust default. The author calls for a **bias-variance characterization** of the $\beta$ trade-off (as in regression/classification CV theory).
- Only the number-of-components problem for **Gaussian** mixtures is treated; extending to other independence structures, non-Gaussian components, and Markov / hidden-Markov models is flagged as future work.
- Comparative studies across penalized-likelihood, Bayesian, and cross-validation methodologies are explicitly left open.

## Connections
The mixture-model clustering framework draws on McLachlan and Basford (1988), Titterington, Smith and Makov (1985), and Everitt and Hand (1981), with EM estimation from [[@Dempster1977|Dempster, Laird and Rubin (1977)]] and McLachlan and Krishnan (1997). The closest methodological competitor is McLachlan's (1987) parametric bootstrap likelihood-ratio test (see also McLachlan and Peel 1997, 1998, and Feng and McCulloch 1996 on why standard LRT asymptotics break down for mixtures). Penalized-likelihood selection connects to Schwarz's (1978) BIC, Kass and Raftery (1995) on Bayes factors, and Fraley and Raftery (1998); Chickering and Heckerman (1997) is cited for viewing penalized likelihood as approximations to the Bayesian solution. The cross-validation methodology builds on Burman (1989), Shao (1993), and Zhang (1993) in regression, Silverman (1986) for density estimation, Breiman et al. (1984) for CART, and Smyth (1996) for MCCV; Dawid (1984) frames CV as a Bayesian approximation, and Good (1952) supplies the log predictive score. The KL-distance argument uses Cover and Thomas (1991). The atmospheric application connects to Cheng and Wallace (1993), Kimoto and Ghil (1993), Mo and Ghil (1988), Michelangeli, Vautard and Legras (1995), and the author's own Smyth, Ide and Ghil (1999). Related extensions appear in Smyth (1997) for hidden Markov models and Smyth and Wolpert (1999) for stacking density estimators.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
