---
citekey: Rendle2019
title: "On the Difficulty of Evaluating Baselines: A Study on Recommender Systems"
authors: ["Rendle, Steffen", "Zhang, Li", "Koren, Yehuda"]
year: 2019
type: preprint
doi: ""
zotero: "zotero://select/library/items/4XHNJ6ZL"
pdf: /Users/jesper/Zotero/storage/RIVJBFSJ/Rendle2019.pdf
tags: [literature]
keywords: [recommender-systems, matrix-factorization, evaluation-methodology, baselines, reproducibility, benchmarking]
topics: []
related: [Rendle2012]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Numerical evaluations with comparisons to baselines play a central role when judging research in recommender systems. In this paper, we show that running baselines properly is difficult. We demonstrate this issue on two extensively studied datasets. First, we show that results for baselines that have been used in numerous publications over the past five years for the Movielens 10M benchmark are suboptimal. With a careful setup of a vanilla matrix factorization baseline, we are not only able to improve upon the reported results for this baseline but even outperform the reported results of any newly proposed method. Secondly, we recap the tremendous effort that was required by the community to obtain high quality results for simple methods on the Netflix Prize. Our results indicate that empirical findings in research papers are questionable unless they were obtained on standardized benchmarks where baselines have been tuned extensively by the research community.

## Summary
Rendle, Zhang, and Koren show that the apparent five-year progress on the Movielens 10M (ML10M) rating-prediction benchmark is largely an artifact of poorly-tuned baselines. With a careful setup, a vanilla matrix-factorization baseline — and especially a Bayesian variant plus decade-old implicit/temporal tricks — outperforms *every* newly proposed method reported on the benchmark. They contrast this with the Netflix Prize, where competitive incentives drove the community to well-calibrated baseline numbers. The takeaway: statistical significance, reproducibility, and hyperparameter search are necessary but not sufficient for reliable empirical claims; only standardized benchmarks with community-tuned baselines deliver trustworthy comparisons.

## Research question
Are the empirical findings produced by the standard best-practice evaluation protocol in recommender systems (reproducible experiments, multiple datasets, hyperparameter search, statistical significance testing) actually reliable? More pointedly: is the difficulty of *running baselines properly* a large enough source of error to invalidate the conclusions drawn from years of published comparisons?

## Method / identification
This is an empirical/meta-scientific study, not a new model. The authors take the ML10M benchmark (RMSE on a random 90:10 split / 10-fold CV) and re-run "baseline" methods that prior papers had reported as weak. All models are expressed inside a single factorization-machine framework using the `libFM` library, parameterized by which features are included:

- Matrix Factorization: features $(u, i)$ — equivalent to biased MF / RSVD.
- SVD++: $(u, i, iu)$ — adds implicit user feedback (bag-of-words over watched items).
- timeSVD: $(u, i, t)$ — adds day-level temporal categorical.
- timeSVD++: $(u, i, t, iu)$.
- timeSVD++ flipped: $(u, i, t, iu, ii)$ — also adds implicit *item* information (set of users who watched a movie).

Two learning algorithms are compared: Gibbs sampling (MCMC, the "Bayesian" variants) and SGD. The Bayesian models are emphasized because they have fewer critical hyperparameters — only sampling steps, embedding dimension, and initialization (Gaussian, std $0.1$). For SGD, a grid over regularization $\{0.02,0.03,0.04,0.05\}$ and learning rate $\{0.001,0.003\}$ is tuned on a held-out 5% of training data. The argument is identification-by-demonstration: a single counterexample (a "weak" baseline beating all SOTA) suffices to falsify the benchmark's accumulated conclusions. A second strand is a historical case study of the Netflix Prize, recapping how reported vanilla-MF RMSEs fell from ~0.94 to ~0.8985 only through sustained community effort.

## Data
Movielens 10M (10 million ratings; standard random 90:10 split with 10-fold CV). Netflix Prize dataset is used as a documented historical case study (its training/probe/qualifying/quiz/test split is described but the authors re-analyze published numbers rather than re-running it).

## Key findings
- **A vanilla MF baseline beats all SOTA on ML10M.** SGD-MF reaches RMSE $0.7720$ (512-dim), versus reported $0.8256$ (RSVD) and $0.803$ (Biased MF) — and beats newer methods like LLORMA ($0.7815$), AutoRec ($0.782$), WEMAREC ($0.7769$).
- **Bayesian MF (a method prior work called one of the *worst*) is the new best.** Gibbs-sampled MF hits RMSE $0.7633$, edging past the best previously reported result, MRMA ($0.7634$) — improving on it by $0.0144$, comparable to several years of claimed progress.
- **Decade-old tricks add large gains:** Bayesian timeSVD $0.7587$, SVD++ $0.7563$, timeSVD++ $0.7523$, and timeSVD++ flipped $0.7485$.
- **Insufficient reliability indicators (Section 3):** statistical significance only measures within-setup variance, not whether the method is set up well; reproducibility (rerunning shared code) reproduces numbers but not *proper* setups; hyperparameter search misses "knobs" (centering, shuffling, early stopping, initialization) that experts apply tacitly.
- **Netflix vs. ML10M contrast:** the Prize's leaderboard incentive produced well-calibrated baselines that have shown little overfitting after a decade and whose best methods also win on ML10M; ML10M's publication-novelty incentive did not.

## Contribution
Provides a concrete, high-profile demonstration that the field's standard evaluation practice can yield systematically misleading conclusions, with the striking result that "weak" baselines outperform every published improvement on a heavily-studied benchmark. It reframes the reproducibility crisis around *baseline tuning* specifically, and argues for standardized, community-maintained benchmarks plus explicit incentives for improving baselines. The paper became an influential reference point for the broader debate on whether deep-learning recommenders genuinely beat well-tuned classical methods.

## Limitations & open questions
- The authors explicitly note that the newly-proposed methods might *themselves* improve with more careful tuning — so the comparison is not necessarily a verdict on the methods, only on the reported numbers (this is framed as further evidence that running experiments is hard).
- They acknowledge SGD results could likely improve with more sophisticated hyperparameter selection (per-bias/per-embedding rates, learning-rate decay schedules), leaving "how good can a properly-tuned baseline get?" open.
- The overfitting-to-benchmarks concern is acknowledged but only argued away empirically for large datasets; the long-run risk is left open.
- Most recommender tasks (item recommendation, cold-start, forecasting, explanation) lack standardized benchmarks — building them is posed as open community work.
- How to design *incentives* for tuning and reporting well-known methods (so the Netflix dynamic recurs) is raised but unresolved.

## Connections
The MF and learning machinery draws on Koren, Bell & Volinsky's matrix-factorization line (Koren 2008 on neighborhood/SVD++; Koren 2009 on temporal dynamics / timeSVD++), Funk's (2006) FunkSVD, Paterek (2007), and Salakhutdinov & Mnih (2008) on Bayesian probabilistic matrix factorization via MCMC. The factorization-machine framing and libFM solver come from [[@Rendle2012|Rendle]] (2012, 2013) and Freudenthaler, Schmidt-Thieme & Rendle (2011) on Bayesian factorization machines. The "newly proposed methods" it overturns include Lee et al. (2013, LLORMA), Sedhain et al. (2015, AutoRec), Chen et al. (2015, WEMAREC), Li et al. (2017, MRMA), and Zheng et al. (2016, CF-NADE). The Netflix Prize case study cites Bennett & Lanning (2007) and the BellKor/BigChaos/Pragmatic Theory winning ensembles (Koren 2009; Töscher & Jahrer 2009). Thematically it sits alongside later reproducibility critiques such as Dacrema, Cremonesi & Jannach's "Are we really making much progress?" (2019) and broader work by Armstrong, Moffat et al. on stagnant baselines in information retrieval.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
