---
citekey: Johnson2014
title: Logistic matrix factorization for implicit feedback data
authors: ["Johnson, Christopher C."]
year: 2014
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/Z4TKBZU5"
pdf: /Users/jesper/Zotero/storage/5CITV72A/Johnson2014.pdf
tags: [literature]
keywords: [matrix-factorization, implicit-feedback, collaborative-filtering, recommender-systems, latent-factor-models, logistic-regression]
topics: ["[[recommender-systems-matrix-factorization]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Collaborative filtering with implicit feedback data involves recommender system techniques for analyzing relationships betweens users and items using implicit signals such as click through data or music streaming play counts to provide users with personalized recommendations. This is in contrast to collaborative filtering with explicit feedback data which aims to model these relationships using explicit signals such as user-item ratings. Since most data on the web comes in the form of implicit feedback data there is an increasing demand for collaborative filtering methods that are designed for the implicit case. In this paper we present Logistic Matrix Factorization (Logistic MF), a new probabilistic model for matrix factorization with implicit feedback. The model is simple to implement, highly parallelizable, and has the added benefit that it can model the probability that a user will prefer a specific item. Additionally, we show it to experimentally outperform the widely adopted Implicit Matrix Factorization method using a dataset composed of music listening behavior from streaming music company Spotify.

## Summary
Johnson (Spotify, 2014) introduces **Logistic Matrix Factorization (Logistic MF)**, a probabilistic latent-factor model for collaborative filtering on *implicit* feedback (clicks, streams) rather than explicit ratings. Instead of minimizing weighted RMSE on a binarized preference matrix as in Hu, Koren & Volinsky's Implicit MF (IMF), Logistic MF models the *probability* that a user prefers an item via a logistic function of user/item latent vectors plus biases, and maximizes a confidence-weighted log-posterior. Trained by alternating AdaGrad gradient ascent and parallelized via a MapReduce sharding scheme, it matches IMF at high latent dimensionality but markedly outperforms it at low dimensionality on a 50k-user / 10k-artist Spotify dataset.

## Research question
How can implicit feedback (e.g. play counts) be turned into accurate, scalable, *personalized* recommendations using a matrix-factorization model that (a) directly yields a probability of user preference and (b) parallelizes to web scale, while improving on the dominant Implicit MF approach?

## Method / identification
The data is a sparse non-negative user-item interaction matrix $R = (r_{ui})_{n \times m}$, where $r_{ui} \in \mathbb{R}_{\geq 0}$ is how many times user $u$ interacted with item $i$. Users and items are embedded in $f$-dimensional latent factor matrices $X_{n \times f}$ (taste) and $Y_{m \times f}$ (style). Let $l_{ui}$ denote the event that user $u$ prefers item $i$. Its probability is logistic in the inner product of the latent vectors plus user/item biases $\beta_u, \beta_i$:

$$p(l_{ui}\mid x_u, y_i, \beta_u, \beta_i) = \frac{\exp(x_u y_i^{T} + \beta_u + \beta_i)}{1 + \exp(x_u y_i^{T} + \beta_u + \beta_i)}$$

Non-zero entries are treated as positive observations and zero entries as negative ones, with a **confidence** weight $c = \alpha r_{ui}$ (so each non-zero entry counts as $c$ positives and each zero as one negative; an alternative log-scaling $c = 1 + \alpha\log(1 + r_{ui}/\epsilon)$ tempers power-user bias). Assuming independence, the likelihood is

$$L(R\mid X, Y, \beta) = \prod_{u,i} p(l_{ui})^{\alpha r_{ui}}\,(1 - p(l_{ui}))$$

Zero-mean spherical Gaussian priors on $x_u, y_i$ regularize the model, which (after dropping constants into $\lambda$) reduces to $\ell_2$-regularization, giving the log-posterior

$$\log p(X, Y, \beta\mid R) = \sum_{u,i}\alpha r_{ui}(x_u y_i^{T} + \beta_u + \beta_i) - (1 + \alpha r_{ui})\log(1 + \exp(x_u y_i^{T} + \beta_u + \beta_i)) - \frac{\lambda}{2}\lVert x_u\rVert^2 - \frac{\lambda}{2}\lVert y_i\rVert^2$$

This is maximized by **alternating gradient ascent**: fix $X, \beta$ and step on $Y, \beta$, then fix $Y, \beta$ and step on $X, \beta$. Each iteration is linear in $\lvert U\rvert$ and $\lvert I\rvert$; AdaGrad adaptive step sizes sharply cut the iteration count. To scale, $R$ is sharded into $K \times L$ blocks; per-pair gradient contributions are computed in the map phase and summed per user (or item) in the reduce phase, fitting the MapReduce paradigm. Negative sampling (fewer $r_{ui} = 0$ draws, with $\alpha$ reduced in compensation) further approximates the full loss when full linear computation is infeasible.

## Data
Spotify listening logs: $\lvert X\rvert = 50{,}000$ uniformly random active users restricted to the $\lvert I\rvert = 10{,}000$ most popular artists, over two years (May 2011 – June 2013). A "listen" is any continuous stream of a song for more than 30 seconds (to drop sampling noise). The matrix $R$ has 86 million non-zero and 414 million zero entries; no contextual/temporal weighting was added. The production system is reported to scale to 40 million users and 20 million songs.

## Key findings
Evaluation uses **Mean Percentage Ranking (MPR)** on a held-out 10% of *entries* (not listens, to avoid favoring already-listened artists), where lower is better and random ranking gives 50%. (1) The popularity baseline already reaches MPR 14.9%. (2) Both Logistic MF and IMF converge to similar MPR at ~100 latent factors (5.99 for Logistic MF vs 6.27 for IMF). (3) The decisive advantage of Logistic MF is at *low* dimensionality: with only 10 latent factors it achieves MPR 8.065% versus IMF's 16.9% (barely above the popularity baseline). Performing well with fewer factors matters because of the curse of dimensionality (less training data needed) and because smaller item-vector dimensionality shrinks ANN/k-d-tree/LSH structures used for real-time recommendation. (4) Qualitative cosine-similarity nearest-neighbor "Related Artists" lists (using 60 factors) are argued to be subjectively better under Logistic MF.

## Contribution
A new probabilistic framework for implicit-feedback collaborative filtering that models preference probability with a **logistic** link (rather than the Gaussian/RMSE objective of Hu et al. or the Poisson factorization of Gopalan et al.), is simple to implement, AdaGrad-accelerated, and MapReduce-parallelizable. It demonstrably beats the widely adopted Implicit MF at low rank on real Spotify data and powers production features (Discover, Radio, Related Artists). The model has become a standard baseline in the implicit-feedback recommender literature.

## Limitations & open questions
The paper is largely an applied systems contribution and leaves several threads open: (i) no contextual or temporal weighting was used despite the model explicitly allowing real-valued, reweighted $r_{ui}$ — integrating context/time (à la Karatzoglou et al. or Koren) is left unexplored; (ii) the alternative log-scaling confidence function is mentioned but not empirically evaluated; (iii) negative sampling is used as an approximation without a rigorous analysis of the accuracy/speed tradeoff; (iv) evaluation is on a single proprietary dataset (Spotify, top artists only) and one recall-style metric (MPR), so external validity to other domains and tasks is untested; (v) the qualitative Related-Artists comparison is explicitly subjective ("we leave it to the reader to have their own opinion"); (vi) no formal treatment of cold-start or side-information (content/audio) fusion, which the related-work survey flags as important.

## Connections
The model is positioned directly against Hu, Koren & Volinsky (2008) Implicit MF, sharing the confidence-weighting idea $c = \alpha r_{ui}$ but swapping weighted RMSE for a logistic likelihood. It builds on classic matrix-factorization recommenders from the Netflix Prize era (Funk, 2006; Bell, Koren & Volinsky, 2007; Koren's temporal-dynamics work, 2009) and the broader family of latent-factor models — Probabilistic Latent Semantic Indexing (Hofmann), Latent Dirichlet Allocation (Blei, Ng & Jordan, 2003), and Restricted Boltzmann Machines (Salakhutdinov, Mnih & Hinton, 2007). On the probabilistic side it relates to Salakhutdinov & Mnih's Probabilistic Matrix Factorization (2007), Mnih & Teh's tree-structured implicit model (2011), and Gopalan, Hofman & Blei's Poisson factorization (2013), differing by its logistic link. One-Class Collaborative Filtering with negative sampling (Pan et al., 2008) motivates the positive/unlabeled treatment of zeros; neighborhood methods (Herlocker et al., 1999; Sarwar et al., 2001; Linden, Smith & York's Amazon item-to-item, 2003) are the baselines MF supersedes. Optimization and scaling draw on AdaGrad (Duchi, Hazan & Singer, 2011) and distributed-SGD / parallel MF work (Gemulla et al., 2011; Recht & Ré, 2013; Yu et al., 2012; Zhou et al., 2008; Das et al., 2007 on Google News).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
