---
citekey: Ghahramani1993
title: Supervised learning from incomplete data via an EM approach
authors: ["Ghahramani, Zoubin", "Jordan, Michael"]
year: 1993
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/GN2L5U2J"
pdf: /Users/jesper/Zotero/storage/RNEX3TIF/Ghahramani1993.pdf
tags: [literature]
keywords: [em-algorithm, mixture-models, missing-data, density-estimation, supervised-learning, gaussian-mixture]
topics: []
related: [Dempster1977]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Real-world learning tasks may involve high-dimensional data sets with arbitrary patterns of missing data. In this paper we present a framework based on maximum likelihood density estimation for learning from such data sets. We use mixture models for the density estimates and make two distinct appeals to the Expectation-Maximization (EM) principle (Dempster et al., 1977) in deriving a learning algorithm—EM is used both for the estimation of mixture components and for coping with missing data. The resulting algorithm is applicable to a wide range of supervised as well as unsupervised learning problems. Results from a classification benchmark—the iris data set—are presented. (Abstract empty in Zotero; reproduced verbatim from the PDF.)

## Summary
Ghahramani and Jordan recast supervised learning as joint-density estimation with mixture models, and show that the Expectation-Maximization (EM) algorithm can be invoked twice within a single coherent framework: once to fit the latent mixture-component labels, and once to fill in arbitrary patterns of missing feature values. Because the method estimates the full joint density $P(\mathbf{x},\mathbf{y})$ rather than a direct input/output map, it handles supervised learning, unsupervised learning, inverse problems, and incomplete data uniformly. A demonstration on the iris classification benchmark shows graceful degradation as the fraction of missing features grows, dominating the common mean-imputation heuristic.

## Research question
How can one build a single, principled learning framework that (i) treats supervised and unsupervised learning identically, (ii) represents arbitrary relations between variables rather than just a function, and (iii) copes gracefully with data sets that have arbitrary, possibly per-example patterns of missing values?

## Method / identification
The core move is to model the data $\mathcal{X}=\{\mathbf{x}_1,\dots,\mathbf{x}_N\}$, with no input/output distinction, as i.i.d. draws from a mixture density
$$P(\mathbf{x}_i)=\sum_{j=1}^{M}P(\mathbf{x}_i\mid\omega_j;\theta_j)\,P(\omega_j),$$
and to maximize the log-likelihood $l(\theta\mid\mathcal{X})=\sum_{i=1}^{N}\log\sum_{j=1}^{M}P(\mathbf{x}_i\mid\omega_j;\theta_j)P(\omega_j)$. Direct maximization is hard (log of a sum), so EM introduces a hidden indicator $z_{ij}$ for which component generated point $i$, yielding the complete-data log-likelihood $l_c(\theta\mid\mathcal{X},Z)=\sum_i\sum_j z_{ij}\log P(\mathbf{x}_i\mid z_i;\theta)P(z_i;\theta)$. The algorithm iterates
$$\text{E-step: } Q(\theta\mid\theta_k)=E[l_c(\theta\mid\mathcal{X},Z)\mid\mathcal{X},\theta_k],\qquad \text{M-step: } \theta_{k+1}=\arg\max_\theta Q(\theta\mid\theta_k).$$
For a **mixture of Gaussians** the E-step reduces to the responsibilities $h_{ij}=E[z_{ij}\mid\mathbf{x}_i,\theta_k]$, and the M-step re-estimates means and covariances as $h_{ij}$-weighted data statistics. A parallel derivation gives a **mixture of Bernoullis** for binary data (and multinomials for categorical data; mixed real/binary/categorical dimensions follow by assuming a joint density with mixed component types).

The second, novel contribution adds missing values as a *second* form of incomplete data. Each vector splits into observed and missing parts $(\mathbf{x}_i^o,\mathbf{x}_i^m)$, with the pattern allowed to differ per example. The E-step now estimates both the component labels $z_i$ and the missing components $\mathbf{x}_i^m$, using the current density to "complete" the data. Crucially, the authors show that naively plugging in the expected missing value fails — even for a single 2-D Gaussian the imputed values lie on a line, biasing the covariance. EM instead requires taking expectations of *whatever incomplete terms appear in the likelihood*: the sufficient statistics need $E[z_{ij}\mid\mathbf{x}_i^o,\theta_k]$, $E[z_{ij}\mathbf{x}_i^m\mid\mathbf{x}_i^o,\theta_k]$, and $E[z_{ij}\mathbf{x}_i^m\mathbf{x}_i^{m\top}\mid\mathbf{x}_i^o,\theta_k]$. These are computed via the Gaussian regression of the missing on the observed dimensions, so the second-moment term carries the conditional covariance $\Sigma_j^{mm}-\Sigma_j^{mo}\Sigma_j^{oo-1}\Sigma_j^{mo\top}$ rather than just an outer product of imputed means.

For prediction (function approximation), an input $\mathbf{x}_i^{\,\mathrm{I}}$ is conditionalized to $P(\mathbf{x}^o\mid\mathbf{x}_i^{\,\mathrm{I}})$, again a mixture of Gaussians. Three point estimators are offered: the least-squares estimate (LSE) $\hat{\mathbf{x}}^o=E(\mathbf{x}^o\mid\mathbf{x}_i^{\,\mathrm{I}})$, a stochastic sample (STOCH), and a single-component LSE (SLSE) using the highest-posterior Gaussian. The LSE estimator is a convex sum of linear regressions whose weights $h_{ij}$ vary nonlinearly over the input space. Classification is handled by adding multinomial components for the class label and reading off $P(C=d\mid\mathbf{x},\theta)$.

## Data
The iris benchmark: 100 training and 50 test points, each with 4 real-valued attributes and one of three class labels. The authors also mention (without tables) applying the method to clustering 35-dimensional greyscale images and approximating the kinematics of a three-joint planar arm from incomplete data.

## Key findings
The central result is the unified two-EM learning algorithm and the explicit E-step formulas for Gaussian and Bernoulli mixtures under missing data. A key technical point is that correct EM requires the conditional second moments of the missing data (not mean imputation), otherwise covariance estimates are biased. Empirically (Figure 1), on iris the EM density-estimation classifier degrades gracefully as the proportion of missing features rises and substantially outperforms mean imputation (MI), with the gap widening as more features go missing.

## Contribution
The paper unifies two previously separate uses of EM — fitting mixture densities and handling missing data in statistics (Little & Rubin, 1987) — into one algorithm, and reframes supervised learning as density estimation in which input/output, supervised/unsupervised, and complete/incomplete data are all special cases. The density-based view also enables representing arbitrary relations (forward map, inverse map, or any relation between subsets of variables), going beyond function approximation. It connects to and generalizes mixtures-of-experts, CART, and MARS, which it notes the LSE-on-Gaussian-mixture estimator resembles (competitively partitioning the input space and fitting local linear regressions).

## Limitations & open questions
The authors flag that parametric methods can lack flexibility versus nonparametric ones (argued to be largely circumvented by mixtures, but not eliminated). They note density estimation in high dimensions is generally harder and needs more parameters than function approximation — an implicit scaling concern. The motivation for the density-based generality points to a stated open agenda: solving inverse problems / inverting causal systems where data come from a *relation* rather than a noisy function, pursued in a companion paper (Ghahramani, 1994). The number of mixture components $M$ is taken as given; model selection is not addressed. The missing-data treatment assumes the EM/likelihood machinery is appropriate (effectively missing-at-random style assumptions inherited from Little & Rubin) without separate discussion.

## Connections
The work sits squarely on [[@Dempster1977|Dempster, Laird & Rubin (1977)]], whose EM algorithm it applies twice, and on Little & Rubin (1987) for the missing-data branch. It is a sibling to the mixtures-of-experts line (Jacobs et al., 1991; Jordan & Jacobs, 1994), differing by estimating the joint density rather than a conditional regression. It relates to decision-tree and spline regressors CART (Breiman et al., 1984) and MARS (Friedman, 1991), and to general regression neural networks (Specht, 1991) and the rule-based network structuring of Tresp et al. (1993). The companion Ghahramani (1994) extends the framework to inverse problems. As an early, clean statement of mixture-model EM with missing data, it is a foundational reference for later latent-variable and probabilistic-modeling work relevant to choice modeling and structural estimation with incomplete observations.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
