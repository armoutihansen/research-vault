---
citekey: Murphy2023
title: "Probabilistic machine learning: Advanced topics"
authors: ["Murphy, Kevin P."]
year: 2023
type: book
doi: ""
zotero: "zotero://select/library/items/CRIPGI6T"
pdf: /Users/jesper/Zotero/storage/T3INRP7M/Murphy2023.pdf
tags: [literature]
keywords: [probabilistic-machine-learning, bayesian-inference, variational-inference, generative-models, graphical-models, gaussian-processes, reinforcement-learning, causality]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

Murphy's *Probabilistic Machine Learning: Advanced Topics* (MIT Press, 2023) is the second of a two-volume graduate sequence and serves as a reference monograph rather than a research paper. It develops machine learning from a unifying probabilistic (largely Bayesian) standpoint, covering the modelling, inference, prediction, generation, discovery, and decision-making pillars of modern ML. Across roughly 1350 pages and 36 chapters it treats probabilistic graphical models, approximate inference (variational, MCMC, SMC), deep and Bayesian neural networks, Gaussian processes, deep generative models (VAEs, autoregressive models, normalizing flows, energy-based models, diffusion models, GANs), latent-variable and state-space models, representation learning, interpretability, decision theory, reinforcement learning, and causality. The book is freely available under a CC-BY-NC-ND license. This note is a *targeted* reading of a 1354-page source: front matter, brief and detailed contents, and representative chapter introductions; it summarizes the book's scope and organizing logic rather than every technical result.

## Research question

Not a hypothesis-driven study. The organizing question is methodological: how can the diverse methods of modern machine learning be presented coherently under a single probabilistic framework, so that supervised, unsupervised, generative, and decision-making tasks are seen as instances of specifying a probabilistic model, performing (approximate) inference, and acting under uncertainty?

## Method / identification

The unifying formalism is the probabilistic model $p(\mathbf{x}, \mathbf{z}, \mathbf{y} \mid \boldsymbol{\theta})$ over observed data, latent variables, targets, and parameters, with learning cast as inference over $\boldsymbol{\theta}$ (and prediction as inference over $\mathbf{y}$ or $\mathbf{z}$). Recurring tools include Bayes' rule $p(\boldsymbol{\theta}\mid \mathcal{D}) \propto p(\mathcal{D}\mid \boldsymbol{\theta})\,p(\boldsymbol{\theta})$, the exponential family with its natural/mean-parameter duality, and divergence measures ($f$-divergences, integral probability metrics, MMD, total variation) used both as objectives and as analysis tools.

The book is organized into six parts. (I) *Fundamentals*: probability, statistics (Bayesian, frequentist, conjugate/noninformative/hierarchical priors, empirical Bayes), graphical models (directed Bayes nets, undirected MRFs, CRFs), information theory, and optimization. (II) *Inference*: an algorithmic overview, Gaussian filtering/smoothing, message passing, variational inference (the ELBO $\mathcal{L}(\boldsymbol{\phi}) = \mathbb{E}_{q_{\boldsymbol{\phi}}}[\log p(\mathbf{x},\mathbf{z}) - \log q_{\boldsymbol{\phi}}(\mathbf{z})]$, reparameterized/amortized/black-box VI, CAVI, VBEM, tighter bounds such as the IWAE multi-sample ELBO), and Monte Carlo, MCMC, and sequential Monte Carlo. (III) *Prediction*: GLMs, deep neural networks, Bayesian neural networks, Gaussian processes (Mercer kernels, sparse/inducing-point approximations), and learning beyond the i.i.d. assumption (distribution shift, robustness). (IV) *Generation*: VAEs, autoregressive models, normalizing flows, energy-based models, diffusion models, and GANs. (V) *Discovery*: latent factor models, state-space models (HMMs, LDS), graph learning, nonparametric Bayes, representation learning, and interpretability. (VI) *Action*: decision making under uncertainty, reinforcement learning (including model-based RL and MPC), and causality (identification, estimation). Methods are derived with explicit objective functions and estimators rather than only described.

## Data

None — this is a textbook/monograph. It uses many illustrative datasets and worked examples (e.g., coin-tossing for Bayesian inference, GMM fitting via VBEM, Ising-model CAVI, object tracking with linear dynamical systems, protein-sequence alignment with HMMs) but introduces no new empirical dataset.

## Key findings

As a reference work it has no single result; its "findings" are the canonical algorithms and identities it consolidates: Bayes' rule and conjugate-prior updates; the exponential-family / maximum-entropy correspondence; conditional-independence semantics of directed vs. undirected graphical models and the label-bias problem motivating CRFs; the EM and variational-EM algorithms; the ELBO and its reparameterized, amortized, black-box, and multi-sample (IWAE) variants; MCMC and SMC samplers; the Gaussian-process predictive equations and sparse approximations; the change-of-variables identity underlying normalizing flows; the score-based / denoising view of diffusion models; the Baum-Welch algorithm and Kalman filter for state-space models; and the identification-and-estimation pipeline of causal inference. The contribution is the *coherent probabilistic framing* that makes these appear as variations on shared principles.

## Contribution

Provides an up-to-date, unified graduate reference that integrates classical probabilistic ML (graphical models, GPs, MCMC) with the deep-learning era (deep generative models, BNNs, diffusion, large-scale amortized inference), all under one notation and Bayesian-leaning philosophy. Its breadth and freely available, regularly updated form make it a standard map of the field and a common methodological vocabulary for researchers building probabilistic and generative models.

## Limitations & open questions

Being a synthesis, the book repeatedly flags frontier problems rather than solving them: scalable and well-calibrated inference for Bayesian neural networks; tighter and lower-variance variational bounds; reliable inference under distribution shift and robustness to model misspecification; evaluation and likelihood estimation for implicit/adversarial generative models; combining VI with MCMC for more accurate posteriors; representation-learning theory (what makes a representation good and identifiable); interpretability methods that are faithful rather than merely plausible; and causal identification and estimation from observational data under realistic assumptions. Each of these is an explicit open-research hook rather than a settled topic.

## Connections

The book is the sequel to Murphy's earlier *Machine Learning: A Probabilistic Perspective* (2012) and companion *Probabilistic Machine Learning: An Introduction* (2022), and overlaps in spirit with Bishop (2006), *Pattern Recognition and Machine Learning*, and Koller & Friedman (2009) on graphical models. The variational-inference chapters build on Jordan et al. (1999) and Blei, Kucukelbir & McAuliffe (2017); amortized/reparameterized VI follows Kingma & Welling (2014) and Rezende & Mohamed (2015) on VAEs and normalizing flows; diffusion models trace to Ho, Jain & Abbeel (2020) and Song & Ermon (2019); GANs to Goodfellow et al. (2014); Gaussian processes to Rasmussen & Williams (2006); and the causality chapter draws on Pearl (2009) and the potential-outcomes tradition of Imbens & Rubin (2015). For an economist working on choice modeling and social preferences, the parts on probabilistic graphical models, latent-variable/state-space estimation, and the causality chapter connect most directly to structural and behavioral econometrics.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
