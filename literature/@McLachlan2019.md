---
citekey: McLachlan2019
title: Finite Mixture Models
authors: ["McLachlan, Geoffrey J.", "Lee, Sharon X.", "Rathnayake, Suren I."]
year: 2019
type: journalArticle
doi: 10.1146/annurev-statistics-031017-100325
zotero: "zotero://select/library/items/YH2JGY4T"
pdf: /Users/jesper/Zotero/storage/P9HGIIPG/McLachlan2019.pdf
tags: [literature]
keywords: [finite-mixture-models, em-algorithm, model-based-clustering, latent-class-models, model-selection, robust-clustering]
topics: ["[[finite-mixture-models]]"]
related: [Dempster1977]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The important role of finite mixture models in the statistical analysis of data is underscored by the ever-increasing rate at which articles on mixture applications appear in the statistical and general scientific literature. The aim of this article is to provide an up-to-date account of the theory and methodological developments underlying the applications of finite mixture models. Because of their flexibility, mixture models are being increasingly exploited as a convenient, semiparametric way in which to model unknown distributional shapes. This is in addition to their obvious applications where there is group-structure in the data or where the aim is to explore the data for such structure, as in a cluster analysis. It has now been three decades since the publication of the monograph by McLachlan & Basford (1988) with an emphasis on the potential usefulness of mixture models for inference and clustering. Since then, mixture models have attracted the interest of many researchers and have found many new and interesting fields of application. Thus, the literature on mixture models has expanded enormously, and as a consequence, the bibliography here can only provide selected coverage.

## Summary

An *Annual Review of Statistics* survey of finite mixture models: their formulation, interpretation, estimation (chiefly maximum likelihood via the EM algorithm, plus Bayesian MCMC), the dominant normal/$t$/skew-$t$ component families, dimension-reduction via mixtures of factor analyzers, extensions to dependent data (hidden Markov models, mixtures of experts), and the perennially hard problem of choosing the number of components. It is a methodological map rather than a single new result, written by the authors of the canonical mixture-model monographs.

## Research question

How should heterogeneous data be modeled when a single parametric distribution is inadequate? More concretely: how does one specify, estimate, interpret, and select the order of a finite mixture distribution, and what component families and algorithms make this tractable across the many fields (genetics, cytometry, marketing, economics, imaging) where mixtures are now standard?

## Method / identification

The core object is the finite mixture density for a $p$-dimensional vector $Y$,
$$f(y;\Psi)=\sum_{i=1}^{g}\pi_i\,f_i(y;\theta_i),$$
with nonnegative mixing proportions $\pi_i$ summing to one and $\Psi=(\xi^{\top},\pi_1,\dots,\pi_{g-1})^{\top}$. Identifiability is defined up to permutation of the $g!$ component labels; the residual non-identifiability is harmless under a frequentist constraint but becomes the *label-switching problem* under Bayesian posterior simulation.

The review's central machinery is the EM algorithm of [[@Dempster1977|Dempster, Laird & Rubin (1977)]] applied to the incomplete-data formulation. Each observation is augmented with a latent multinomial label vector $Z_j\sim\mathrm{Mult}_g(1,\pi)$, giving complete-data log-likelihood $\log L_c(\Psi)=\sum_i\sum_j z_{ij}\{\log\pi_i+\log f_i(y_j;\theta_i)\}$. The **E-step** replaces each $z_{ij}$ by its posterior responsibility
$$\tau_i(y_j;\Psi^{(k)})=\frac{\pi_i^{(k)}f_i(y_j;\theta_i^{(k)})}{f(y_j;\Psi^{(k)})},$$
i.e. a *soft* allocation that avoids the bias of hard classification-ML. The **M-step** maximizes the resulting $Q$-function, yielding $\pi_i^{(k+1)}=\frac{1}{n}\sum_j\tau_i(y_j;\Psi^{(k)})$ and component updates that are closed-form for normal components. The monotonicity result $L(\Psi^{(k+1)})\ge L(\Psi^{(k)})$ guarantees convergence of the likelihood sequence (Wu 1983). Variants discussed: ECM, AECM, and the MM algorithm for intractable E-steps. Multiple random/k-means starts are recommended to escape spurious local maxima.

The Bayesian route writes the posterior $p(\Psi\mid y)=C^{-1}L(\Psi)p(\Psi)$ and approximates it by MCMC — Gibbs sampling with data augmentation of $z$, or Metropolis–Hastings; Richardson & Green's (1997) reversible-jump MCMC handles varying $g$.

For component specification the review treats: normal mixtures (affine-invariant clustering, but unbounded likelihood requiring covariance constraints / eigenvalue restrictions); **mixtures of factor analyzers**, where $\Sigma_i=B_iB_i^{\top}+D_i$ reduces the $\tfrac12 p(p+1)$ free parameters; robust $t$-mixtures (a gamma scale mixture with degrees-of-freedom $\nu_i$ as a robustness knob); and skew-normal/skew-$t$ and canonical fundamental skew-$t$ (CFUST) components for asymmetric clusters.

## Data

None original. Illustrative applications only: Fisher's Iris data (3-component normal vs skew-$t$ fits, misclassification dropping from 0.033 to 0.0067) and a hematopoietic stem-cell-transplant cytometry sample (~6,000 cells, four populations) where the skew-$t$ mixture beats the normal mixture.

## Key findings

This is a review, so "findings" are organizing results rather than new theorems. Key consolidated results: (1) normal mixtures are dense in the space of densities under the $L_1$ metric (Li & Barron 1999), so they serve as a semiparametric density estimator; BIC-based component selection is consistent (Roeder & Wasserman 1997, Keribin 2000). (2) EM gives monotone likelihood ascent but converges only to local maxima; the likelihood is unbounded for unrestricted normal covariances. (3) **Number-of-components selection is the most obdurate problem**: standard regularity conditions fail, so the likelihood-ratio statistic $-2\log\lambda$ lacks the usual $\chi^2$ null distribution. For a two-component test, $-2\log\lambda\sim\tfrac12\chi_0^2+\tfrac12\chi_1^2$ (chi-bar-squared; Titterington 1981, Hartigan 1985); with unrestricted means it is asymptotically unbounded at rate $\tfrac12\log\log n$. Practical alternatives are penalized criteria (AIC, BIC), the entropy-penalized ICL criterion of Biernacki, Celeux & Govaert (2000) which counters BIC's tendency to overfit clusters, and bootstrap resampling of the LRT. (4) Dependence is absorbed by making the latent labels $Z_j$ Markovian, giving hidden Markov models (EM = Baum–Welch) and Markov random fields.

## Contribution

A current, authoritative synthesis updating McLachlan & Basford (1988) and McLachlan & Peel (2000) for the 2010s: it threads together model-based clustering, robust and skewed component families, factor-analytic dimension reduction for high-dimensional data, and a catalogue of software (mclust, EMMIX suite, mixtools, flexmix, pgmm, Rmixmod). It positions mixtures as occupying the niche between parametric and nonparametric estimation.

## Limitations & open questions

The authors flag explicitly: (1) selecting $g$ remains unresolved — penalized criteria give no $p$-value and the LRT has no standard asymptotics; (2) likelihood unboundedness and spurious local maximizers under unrestricted covariances; (3) high-dimension-small-$n$ ($p\gg n$) settings where even mixtures of factor analyzers become computationally infeasible, motivating variable screening (EMMIX-GENE) and penalized/sparse approaches; (4) the label-switching problem in Bayesian inference; (5) the bibliography is "selected" — coverage of nonparametric mixing-distribution ML and recent deep mixture models is acknowledged as partial.

## Connections

The EM backbone is [[@Dempster1977|Dempster, Laird & Rubin (1977)]], with convergence theory from Wu (1983) and the ECM/AECM variants of Meng & Rubin (1993) and Meng & van Dyk (1997). Foundational monographs are Titterington, Smith & Makov (1985), McLachlan & Basford (1988), Lindsay (1995), and McLachlan & Peel (2000). Mixtures of factor analyzers trace to Ghahramani & Hinton (1997) and McLachlan & Peel (2000b); robust $t$-mixtures to McLachlan & Peel (1998); skew families to Azzalini & Dalla Valle (1996), Azzalini & Capitanio (2003), and Lee & McLachlan (2013, 2016). Component-number selection draws on Schwarz's (1978) BIC, Biernacki, Celeux & Govaert's (2000) ICL, and Richardson & Green's (1997) reversible-jump MCMC. Mixtures of experts originate with Jacobs et al. (1991). For an economist, this connects to latent-class and finite-mixture models of heterogeneous preferences and to mixture-of-logit demand estimation, where the same EM/soft-allocation logic underlies estimation of latent behavioral types.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
