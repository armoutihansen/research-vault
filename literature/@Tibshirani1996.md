---
citekey: Tibshirani1996
title: Regression Shrinkage and Selection via the Lasso
authors: ["Tibshirani, Robert"]
year: 1996
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/IREDFJAY"
pdf: /Users/jesper/Zotero/storage/DQHSGLG5/Tibshirani1996.pdf
tags: [literature]
keywords: [lasso, l1-regularization, variable-selection, shrinkage-estimation, sparse-regression, soft-thresholding, model-selection]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We propose a new method for estimation in linear models. The `lasso' minimizes the residual sum of squares subject to the sum of the absolute value of the coefficients being less than a constant. Because of the nature of this constraint it tends to produce some coefficients that are exactly 0 and hence gives interpretable models. Our simulation studies suggest that the lasso enjoys some of the favourable properties of both subset selection and ridge regression. It produces interpretable models like subset selection and exhibits the stability of ridge regression. There is also an interesting relationship with recent work in adaptive function estimation by Donoho and Johnstone. The lasso idea is quite general and can be applied in a variety of statistical models: extensions to generalized regression models and tree-based models are briefly described.

## Summary

Tibshirani introduces the **lasso** ("least absolute shrinkage and selection operator"), a penalized least-squares estimator that minimizes the residual sum of squares subject to an $\ell_1$ bound on the coefficient vector. The geometry of the $\ell_1$ constraint region (a diamond with corners on the axes) causes the solution to set some coefficients exactly to zero, so the lasso simultaneously *shrinks* (like ridge regression) and *selects* (like best-subset selection), yielding stable yet interpretable models in a single continuous procedure. The paper develops the estimator, its Bayesian interpretation, a quadratic-programming algorithm, methods for tuning the bound, simulation comparisons against ridge/subset/garotte, and extensions to generalized regression and tree models.

## Research question

Can one build a regression estimator that retains the **interpretability** of subset selection (producing sparse models with exact zeros) while avoiding its instability, and simultaneously enjoys the **stability** of ridge regression while avoiding ridge's failure to zero out coefficients? In short: is there a single continuous estimator that does both shrinkage and variable selection well across regimes?

## Method / identification

Given standardized predictors $x_{ij}$ (so $\sum_i x_{ij}/N=0$, $\sum_i x_{ij}^2/N=1$) and responses $y_i$, the lasso estimate $(\hat\alpha,\hat\beta)$ solves the constrained problem

$$(\hat\alpha,\hat\beta)=\arg\min\left\{\sum_{i=1}^{N}\Big(y_i-\alpha-\sum_j \beta_j x_{ij}\Big)^2\right\}\quad\text{subject to}\quad \sum_j |\beta_j|\le t.$$

Here $t\ge 0$ is the tuning parameter; with $\hat\alpha=\bar y$ the intercept drops out. Equivalently the constraint is a Lagrangian $\ell_1$ penalty added to the residual sum of squares. Letting $t_0=\sum_j|\hat\beta_j^{0}|$ for the full OLS fit, values $t<t_0$ induce shrinkage and, beyond a threshold, exact zeros; $t=t_0/2$ behaves roughly like a best subset of size $p/2$.

**Orthonormal case ($X^\top X=I$):** the solution is the *soft-threshold* estimator $\hat\beta_j=\operatorname{sign}(\hat\beta_j^{0})\,(|\hat\beta_j^{0}|-\gamma)^{+}$, where $\gamma$ is set so $\sum_j|\hat\beta_j|=t$. This contrasts with ridge (proportional scaling) and subset selection (hard thresholding), and coincides with the Donoho-Johnstone wavelet soft-thresholding proposal.

**Geometry:** the elliptical RSS contours first touch the $\ell_1$ diamond often at a corner (a zero coefficient); the ridge ball has no corners, so ridge rarely zeroes coefficients. With $p>2$ and correlated predictors, lasso signs can even differ from OLS signs.

**Bayes interpretation:** the lasso is the posterior mode under independent double-exponential (Laplace) priors $f(\beta_j)\propto \exp(-|\beta_j|/\tau)$ with $\tau=1/\lambda$ — heavier mass at zero and in the tails than the Gaussian prior implicit in ridge.

**Algorithm:** problem (1) is a quadratic program with $2^p$ sign constraints $\delta_i^\top\beta\le t$. Tibshirani introduces them sequentially, maintaining an equality (active) set $E$ and slack set $S$, adding the most violated constraint each step until the Kuhn-Tucker conditions hold; it converges in at most $2^p$ steps but empirically in $(0.5p,0.75p)$ iterations. An alternative (David Gay) splits $\beta_j=\beta_j^{+}-\beta_j^{-}$, giving $2p$ variables and $2p+1$ constraints solvable by standard QP.

**Tuning $t$:** three methods — fivefold cross-validation, generalized cross-validation (GCV) using an effective-parameter count $p(t)=\operatorname{tr}\{X(X^\top X+\lambda W^-)^{-1}X^\top\}$ with $W=\operatorname{diag}(|\hat\beta_j|)$, and a closed-form **Stein unbiased risk estimate** (SURE) that requires only one model fit (vs. 75 for CV).

**Standard errors:** via bootstrap, or an approximate ridge-form covariance $(X^\top X+\lambda W^-)^{-1}X^\top X(X^\top X+\lambda W^-)^{-1}\hat\sigma^2$ (which gives zero variance for zeroed predictors). Extension to generalized regression uses an IRLS loop wrapping the lasso QP.

## Data

A real example uses the **prostate cancer** data of Stamey et al. (1989): 8 standardized clinical predictors (lcavol, lweight, age, lbph, svi, lcp, gleason, pgg45) regressed on log prostate-specific antigen. The remaining evidence is from **simulation**: four designs varying signal-to-noise and effect structure (small number of large effects; small-to-moderate moderate effects; a single large effect; and a large $p=40$, $n=100$ model where subset regression is impractical), plus a logistic-regression illustration on the kyphosis data.

## Key findings

- **Sparsity from $\ell_1$:** the lasso produces exact zeros, giving interpretable submodels; on the prostate data with GCV-selected $s=t/t_0=0.44$ it retains lcavol, lweight, svi (the same three as best subset).
- **Soft thresholding equivalence:** in orthonormal designs the lasso *is* the soft-threshold estimator (eq. 13).
- **Donoho-Johnstone optimality (eq. 16):** for orthonormal designs with $y_i=\beta_i+\sigma z_i$, the soft-threshold (lasso) estimator with $\gamma=\sigma(2\log n)^{1/2}$ attains, up to a $(2\log p+1)$ factor, the risk of the ideal diagonal-projection oracle $R_{DP}$ — i.e. asymptotically it comes as close as subset selection to ideal selection.
- **Regime-dependent performance** (discussion): (a) few large effects — subset selection best, lasso close, ridge poor; (b) small-to-moderate moderate effects — lasso best, then ridge, then subset; (c) many small effects — ridge best by a margin, then lasso, then subset. The garotte slightly beats the lasso in (a) and slightly trails it in (b)-(c).
- **GCV** tuning was the most consistently effective across examples.

## Contribution

The paper defines a single estimator unifying shrinkage and selection, making sparse, stable, interpretable regression a tractable continuous-optimization problem. It supplies the geometric intuition for $\ell_1$-induced sparsity, the Laplace-prior Bayesian reading, practical QP algorithms, three tuning rules, and the bridge to Donoho-Johnstone wavelet theory and Frank-Friedman's "bridge" family ($\sum|\beta_j|^q\le t$, lasso $=q=1$, the smallest $q$ giving a convex region). It became foundational for high-dimensional statistics and sparse machine learning.

## Limitations & open questions

Tibshirani is explicit about several open problems:
- **Standard errors** are hard because the lasso is a non-linear, non-differentiable function of the responses even at fixed $t$; the ridge approximation gives variance 0 for zeroed predictors.
- **Theory for correlated predictors:** the important practical differences between methods arise under correlation, yet optimality results (like Donoho-Johnstone's) are obtained only for orthonormal designs and "seem to be more difficult to obtain" otherwise.
- **Convergence** of the IRLS-wrapped lasso for generalized regression "is not ensured in general"; likewise the more efficient constraint-dropping variant of the QP algorithm lacks a convergence proof.
- **The "bridge" family** — joint estimation of $\beta_j$ and the exponent $q$ — is suggested by Frank and Friedman as possibly effective but untested.
- The author flags ongoing extensions (tree shrinkage, a lasso-type MARS, ill-posed/wavelet problems) as open development, conjecturing that absolute-value constraints "might prove to be useful in a wide variety of statistical estimation problems," warranting further study.

## Connections

The lasso is positioned directly against **ridge regression** (Hoerl-Kennard $\ell_2$ shrinkage) and **best-subset selection**, and was motivated by Breiman's **non-negative garotte** (which shrinks OLS estimates by constrained non-negative factors but depends on OLS signs/magnitudes and so degrades when OLS is unstable). The orthonormal-case equivalence ties it to **Donoho and Johnstone's** wavelet soft-thresholding and their oracle-risk optimality theory, and to **Chen and Donoho's** basis pursuit. **Frank and Friedman's** bridge estimator generalizes it via the $\ell_q$ family. The Bayesian double-exponential reading connects to later Bayesian-lasso work and to **George and McCulloch's** Gibbs-sampling stochastic search variable selection. Tuning draws on **Stein (1981)** unbiased risk estimation and on cross-validation theory (Shao, Zhang, Breiman-Spector). Extensions cited include the Cox proportional-hazards lasso (Tibshirani 1994), monotone tree shrinkage (LeBlanc and Tibshirani 1994), and **Friedman's MARS**. The paper is the seed of the modern sparse-regression literature (later LARS, elastic net, group lasso, and high-dimensional consistency theory).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
