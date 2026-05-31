---
citekey: Bayer2016
title: "fastFM: A Library for Factorization Machines"
authors: ["Bayer, Immanuel"]
year: 2016
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/YHBIISLL"
pdf: /Users/jesper/Zotero/storage/AY8288A5/Bayer2016.pdf
tags: [literature]
keywords: [factorization-machines, recommender-systems, matrix-factorization, mcmc-gibbs-sampling, sparse-features, python-library]
topics: ["[[recommender-systems-matrix-factorization]]"]
related: [Rendle2012]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Factorization Machines (FM) are currently only used in a narrow range of applications and are not yet part of the standard machine learning toolbox, despite their great success in collaborative filtering and click-through rate prediction. However, Factorization Machines are a general model to deal with sparse and high dimensional features. Our Factorization Machine implementation (fastFM) provides easy access to many solvers and supports regression, classification and ranking tasks. Such an implementation simplifies the use of FM for a wide range of applications. Therefore, our implementation has the potential to improve understanding of the FM model and drive new development.

## Summary
This is a short JMLR "Machine Learning Open Source Software" paper introducing **fastFM**, a Python/C library for Factorization Machines (FM). Its goal is to make FM — a general supervised model for sparse, high-dimensional feature interactions that has dominated recommendation and click-through-rate competitions — accessible outside its niche by bundling regression, classification, and ranking tasks with multiple solvers (ALS, MCMC/Gibbs, SGD) behind a scikit-learn-compatible API. The contribution is engineering and dissemination rather than a new model: a layered, BSD-licensed, tested implementation whose ALS and MCMC solvers match the reference libFM in accuracy while being competitive or faster in runtime.

## Research question
Not a hypothesis-testing paper. The implicit question is practical: how can Factorization Machines — empirically successful but confined to specialist recommender-system use — be packaged so that the broader ML research community can apply, inspect, and extend them across regression, classification, and ranking tasks without sacrificing the performance of the reference C implementation?

## Method / identification
The core object is the FM **model equation** of degree 2. For an input $x\in\mathbb{R}^p$ with global bias $w_0\in\mathbb{R}$, linear weights $w\in\mathbb{R}^p$, and per-feature latent factor vectors $v_i\in\mathbb{R}^k$, the prediction is
$$\hat{y}^{FM}(x) := w_0 + \sum_{i=1}^{p} w_i x_i + \sum_{i=1}^{p}\sum_{j>i} \langle v_i, v_j\rangle\, x_i x_j$$
where each pairwise interaction coefficient is *factorized* as the inner product $\langle v_i,v_j\rangle$ rather than learned freely. This factorization is what lets FM estimate interactions even under extreme sparsity: with one-hot user/item encoding $x=\{\dots,0,1,0,\dots,0,1,0,\dots\}$ the equation collapses to $\hat{y}^{FM}(x)=w_0+w_i+w_j+v_i^{T}v_j$, recovering biased matrix factorization $R_{i,j}\approx b_0+b_i+b_j+u_i^{T}v_j$ (Srebro et al., 2004).

Architecturally, fastFM separates a performance-critical C core (**fastFM-core**) from interface code, exposing it through a CLI and a Cython-built Python extension. Sparse design matrices (often >95% sparse) use compressed row storage (CRS) and the CXSparse library for sparse matrix/vector operations, enabling zero-copy memory sharing between Python and C. Solvers (Table 1): regression and classification each support ALS, MCMC, and SGD; ranking uses SGD. Loss functions are square loss (regression); probit MAP, probit, and sigmoid (classification); and pairwise Bayesian Personalized Ranking, BPR (Rendle et al., 2009), for ranking. The MCMC solver implements the Bayesian FM (Freudenthaler et al., 2011) via Gibbs sampling with Gaussian priors on parameters. Correctness is enforced by a continuous-integration test suite using Posterior Quantiles (Cook et al., 2006) for the MCMC sampler and Finite Differences for SGD solvers.

## Data
None collected. Benchmarking uses the public **MovieLens 10M** dataset with its original train/test split, run for a fixed 200 iterations to compare fastFM against libFM.

## Key findings
Not theorems but engineering results. (1) fastFM's ALS and MCMC solvers are **indistinguishable in accuracy** from the reference libFM and compare favorably in runtime on MovieLens 10M; runtime scales linearly in the latent rank $k$ for both implementations. (2) The scikit-learn-compatible API makes common workflows trivial — e.g. an MCMC FM classifier via `fm.fit_predict(X_train, y_train, X_test)` and warm-started ALS regression. (3) Per-iteration model inspection is cheap: running the MCMC solver one iteration at a time (`n_more_iter=1`) lets the user read out `fm.w_`, `fm.V_`, and `fm.hyper_param_` for Bayesian model checking and MCMC convergence diagnostics (e.g. trace/density of the first-order hyperparameter $\sigma_w$), with negligible Python call overhead.

## Contribution
A unified, tested, BSD-licensed FM library that (i) is the first to combine ALS, MCMC, and SGD solvers across regression, classification, and ranking — notably providing a ranking (BPR) loss that competing toolkits lack; (ii) interoperates with scikit-learn and exposes interactive Python access to internal parameters for diagnostics; and (iii) matches the de facto reference libFM on accuracy and runtime. By lowering the barrier to entry, it aims to broaden FM adoption beyond collaborative filtering and CTR prediction into general sparse-feature supervised learning.

## Limitations & open questions
The paper is explicit that fastFM is **not** intended to replace distributed large-scale frameworks such as GraphLab and Bidmach; it targets single-machine ease of use and extensibility instead, leaving distributed/out-of-core FM training out of scope. Empirical validation is confined to a single benchmark (MovieLens 10M) and to second-order interactions in the standard FM equation — higher-order FM, alternative priors, and broader task/dataset coverage are implicitly left for future work and community contributions, which the test suite and open license are designed to enable.

## Connections
The model is Rendle's Factorization Machine, detailed in [[@Rendle2012|Rendle]] (2012b, "Factorization machines with libFM") and shown to subsume biased matrix factorization (Srebro et al., 2004, maximum-margin matrix factorization). The Bayesian/MCMC variant follows Freudenthaler, Schmidt-Thieme & Rendle (2011), and the ranking loss is Bayesian Personalized Ranking from Rendle, Freudenthaler, Gantner & Schmidt-Thieme (2009). Competition pedigree is documented in Rendle & Schmidt-Thieme (2009), [[@Rendle2012|Rendle (2012a)]], and Bayer & Rendle (2013). The Python interface mirrors scikit-learn (Pedregosa et al., 2011) and is built with Cython (Behnel et al., 2011); sparse linear algebra relies on CXSparse (Davis, 2006). Related FM/MF implementations include GraphLab (Low et al., 2014), Bidmach (Canny & Zhao, 2013), and SVDFeature (Chen et al., 2012). Solver-correctness testing draws on Posterior Quantiles (Cook, Gelman & Rubin, 2006).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
