---
citekey: Arteaga2022
title: "xlogit: An open-source Python package for GPU-accelerated estimation of Mixed Logit models"
authors: ["Arteaga, Cristian", "Park, JeeWoong", "Beeramoole, Prithvi Bhat", "Paz, Alexander"]
year: 2022
type: journalArticle
doi: 10.1016/j.jocm.2021.100339
zotero: "zotero://select/library/items/FS89V9IR"
pdf: /Users/jesper/Zotero/storage/TE9JWXM8/Arteaga2022.pdf
tags: [literature]
keywords: [mixed-logit, discrete-choice, gpu-acceleration, maximum-simulated-likelihood, python, random-utility]
topics: []
related: [Croissant2020, McFadden2000, Revelt1998]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Mixed Logit is an advanced and flexible tool for the study of discrete choice problems. However, this flexibility involves computationally intensive calculations, as the estimation of Mixed Logit models requires the simulation of integrals. In addition, the specification of Mixed Logit models requires decisions such as potential explanatory variables to be included in the model as well as their mixing distributions. This specification process involves testing and estimation of different combinations of variables and mixing distributions, which is time consuming and computationally intensive. In response, this paper introduces xlogit, an open-source Python package that leverages the performance of graphic processing units (GPU) for an efficient estimation of Mixed Logit models. For benchmarking, the performance of xlogit was compared against the PyLogit and Biogeme Python packages as well as the mlogit, Apollo, gmnl, and mixl R packages. Artificially generated as well as actual data were used to evaluate the performance gains provided by xlogit. Results suggest that using a mid-range graphics card and a regular desktop computer, xlogit is in average 55x faster than Apollo, 43x faster than Biogeme, 74x faster than gmnl, 39x faster than mixl, 16x faster than mlogit, and 27x faster than PyLogit, with an additional advantage of efficient memory management. The performance gains provided by xlogit facilitate an efficient modeling process, as it enables the testing of a large number of model specifications more efficiently relative to existing software packages. xlogit's open source code, documentation, and usage examples are publicly available in the package's GitHub repository.

## Summary
This is a software paper introducing **xlogit**, an open-source Python package that estimates Mixed Logit (and Multinomial/Conditional Logit) discrete choice models by offloading the most expensive computations — log-likelihood and gradient evaluations across simulation draws — onto NVIDIA CUDA GPUs. By recasting the maximum-simulated-likelihood machinery as batched multidimensional array operations and supplying analytical gradients, xlogit achieves order-of-magnitude speedups (on average 16x–74x) over six established open-source estimators while using less memory, and it scales to hundreds of thousands of random draws on a commodity desktop.

## Research question
How can the estimation of Mixed Logit models — bottlenecked by the simulation of choice-probability integrals over a large number of random draws — be made fast and memory-efficient enough that analysts can iteratively test many specifications and use very large draw counts? The paper's practical question is whether consumer-grade GPU acceleration can deliver large, reproducible speed gains over existing CPU-based open-source tools without sacrificing estimate accuracy.

## Method / identification
The paper is a methods/software contribution, not an empirical identification exercise. Its formal content is the standard Mixed Logit estimation problem rendered in GPU-parallel form.

Utility for decision maker $n$ and alternative $j$ is linear, $V_{nj}=\sum_{k=1}^{K}\beta_k x_{jnk}=\beta x_{jn}$. The Mixed Logit choice probability integrates the logit kernel over the density of random coefficients,
$$P_n^c(\beta)=\int \frac{e^{\beta x_n^c}}{\sum_{j=1}^{J} e^{\beta x_n^j}}\, f(\beta)\, d\beta,$$
with the panel version taking the product $\prod_{t=1}^{T}$ over choice occasions. Because the integral has no closed form, it is approximated by maximum simulated likelihood: $R$ draws $\beta_r$ are taken from the assumed mixing distribution and the simulated probability is the average $\check{P}_n^c(\beta)=\frac{1}{R}\sum_{r=1}^{R}\frac{e^{\beta_r x_n^c}}{\sum_{j=1}^{J} e^{\beta_r x_n^j}}$. Estimation maximizes the simulated log-likelihood $\log[\check{L}(\beta)]=\sum_{n}\sum_{j} y_n^j \cdot \log(\check{P}_n^j)$ via the **BFGS** quasi-Newton routine.

Crucially, xlogit supplies **analytical gradients** rather than finite differences, reducing objective-function evaluations. The logit gradient $\frac{\partial \log[\check{L}]}{\partial\beta_k}=\sum_n\sum_j (y_n^j-\check{P}_n^j)\, x_{jnk}$ is decomposed for each random coefficient into a mean part $\beta_k^b$ and a spread part $\beta_k^w$, with distribution-specific forms: normal ($\beta_k=\beta_k^b+\beta_k^w\eta$), lognormal ($\beta_k=e^{\beta_k^b+\beta_k^w\eta}$), uniform ($\beta_k=\beta_k^b+\beta_k^w(2\mu-1)$), and triangular ($\beta_k=\beta_k^b+\beta_k^w\tau$). The computational innovation is implementation, not theory: rather than looping over individuals or draws, xlogit expresses the log-likelihood and gradient as single multidimensional-array computations distributed across GPU cores (via CuPy/CUDA), and uses **batch processing** of draws to keep GPU memory bounded while streaming data from RAM.

## Data
None original. xlogit's accuracy and speed are demonstrated on three illustrative datasets — the Swissmetro stated-preference transport dataset (6,768 records after filtering), a synthetically generated 4,000-choice inter-city mode dataset with planted coefficients (including deliberately non-significant variables), and the electricity-supplier dataset (4,308 choices, 361 individuals, unbalanced panel). These serve as validation and benchmark fixtures, not as objects of substantive inference.

## Key findings
1. **Accuracy parity.** Across all three datasets, xlogit's coefficients, standard errors, and log-likelihoods match Apollo, Biogeme, mlogit, and gmnl, with coefficient ratios deviating from one by at most 0.01 (Swissmetro), 0.042 (artificial), and 0.01 (electricity). It correctly recovers planted coefficients and flags the planted non-significant variables as statistically zero.
2. **Speed.** With a low-cost GTX1060 GPU (1280 CUDA cores), xlogit_gpu is on average **55x faster than Apollo, 43x faster than Biogeme, 74x faster than gmnl, 39x faster than mixl, 16x faster than mlogit, and 27x faster than PyLogit**, and it beats the multi-threaded Apollo/Biogeme/mixl even when those use 64 processor cores. Even xlogit without a GPU outperforms the CPU competitors.
3. **Scaling and memory.** xlogit estimates the electricity model with 500,000 draws in ~12 minutes and the artificial model with 50,000 draws in ~7 minutes. Batch processing keeps GPU memory under ~1.5 GB (and never above the 6 GB device limit), scaling linearly with draws; the binding constraint is RAM, not GPU memory.

## Contribution
The paper delivers the first open-source, GPU-accelerated Mixed Logit estimator with a comprehensive feature set: multiple mixing distributions (normal, lognormal, triangular, uniform, truncated normal), Halton draws, balanced and unbalanced panels, unbalanced alternative availability, sample weights, and post-estimation tools (predict, market-share forecasting, lrtest). By collapsing estimation times from minutes/hours to seconds, it makes large-draw estimation and assisted/automated specification search (testing many candidate models) computationally practical on consumer hardware.

## Limitations & open questions
The authors are explicit about scope and future work, which double as project-idea hooks:
- **Model coverage.** The current version supports only Logit-based models with a *linear* deterministic utility; Probit, Nested Logit, and Latent Class models are not supported and are flagged as future extensions.
- **Hardware lock-in.** GPU acceleration requires CUDA-enabled NVIDIA cards only; support for other GPU technologies (e.g., AMD/OpenCL) is future work.
- **Post-estimation breadth.** Additional post-estimation and specification-testing utilities are planned but not yet implemented.
- The RAM ceiling (not GPU memory) bounds the maximum number of draws — an open scaling constraint for very large datasets.

## Connections
The estimation theory follows Train (2003) and the maximum-simulated-likelihood treatment of Mixed Logit in [[@Revelt1998|Revelt & Train]] (1998, 2000); the model's universal-approximation property is from [[@McFadden2000|McFadden & Train (2000)]], with random-utility foundations in Manski (1977) and Ben-Akiva & Lerman (1985). The analytical-gradient derivations build on Hasan et al. (2016), and the BFGS/quasi-Newton optimization on Liu & Nocedal (1989) and Fletcher (1981). xlogit positions itself against the open-source estimators it benchmarks: PyLogit (Brathwaite & Walker 2018), Biogeme (Bierlaire 2020), mlogit ([[@Croissant2020|Croissant 2020]]), Apollo (Hess & Palma 2019), mixl (Molloy et al. 2021), and gmnl (Sarrias & Daziano 2017). Its motivating use case — accelerating iterative, large-scale specification search — connects to assisted/automated Mixed Logit specification methods by Paz et al. (2019), Ortelli et al. (2021), and Rodrigues et al. (2020). The Swissmetro fixture is from Bierlaire et al. (2001).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
