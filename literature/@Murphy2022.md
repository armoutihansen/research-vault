---
citekey: Murphy2022
title: "Probabilistic machine learning: an introduction"
authors: ["Murphy, Kevin P."]
year: 2022
type: book
doi: ""
zotero: "zotero://select/library/items/G3429LR9"
pdf: /Users/jesper/Zotero/storage/UZYMWM4M/Murphy2022.pdf
tags: [literature]
keywords: [probabilistic-machine-learning, supervised-learning, bayesian-inference, maximum-likelihood, bias-variance-tradeoff, regularization, deep-learning, textbook]
topics: []
related: [Bruhin2019, Murphy2023]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero) This is Kevin P. Murphy's graduate textbook *Probabilistic Machine Learning: An Introduction* (MIT Press, 2022), an 858-page successor to his 2012 *Machine Learning: A Probabilistic Perspective*. It develops the full range of modern ML — supervised, unsupervised, and (briefly) reinforcement learning — from a single unifying probabilistic lens, treating all unknown quantities as random variables endowed with probability distributions. Part I covers statistical foundations (probability, statistics, information theory, linear algebra, optimization); Parts II–IV cover supervised learning (linear/logistic regression, GLMs, deep neural networks: MLPs, CNNs, RNNs/Transformers); Part V covers unsupervised learning (dimensionality reduction, clustering, graph embeddings). A companion volume, *Probabilistic Machine Learning: Advanced Topics* ([[@Murphy2023|Murphy 2023)]], extends the treatment.

## Summary
A comprehensive, probabilistically-unified introductory graduate textbook on machine learning. Murphy's organizing thesis is that "almost all of machine learning can be viewed in probabilistic terms": supervised learning fits conditional models $p(y\mid x;\theta)$, unsupervised learning fits unconditional generative models $p(x)$, and decision-making under uncertainty is governed by Bayesian/frequentist decision theory. Coverage of this note is **targeted** (the source is an 858-page book): I read the front matter, the Chapter 1 Introduction, and the Chapter 1.6 Discussion in full, plus the table-of-contents-level chapter introductions across the book, and I weighted heavily toward the chapters the user has personally annotated — Chapter 1 (the ML taxonomy) and Chapter 4 (Statistics) — which carry ~190 highlights and several research notes.

## Research question
Not a research paper but a pedagogical synthesis. The framing question is: *how can the heterogeneous methods of machine learning — classification, regression, deep learning, clustering, dimensionality reduction — be presented within one coherent mathematical framework?* Murphy's answer is probability theory used as a "unifying lens," because (i) it is the optimal approach to decision-making under uncertainty (Ch. 5), and (ii) it is the shared language of statistics, control theory, econometrics, information theory, and the rest of computational science.

## Method / identification
The "method" is the probabilistic formalism applied uniformly. Supervised learning is cast as learning a mapping $f:\mathcal{X}\to\mathcal{Y}$ from a training set $\mathcal{D}=\{(x_n,y_n)\}_{n=1}^N$. For classification with $C$ classes, the model outputs a conditional distribution $p(y=c\mid x;\theta)=f_c(x;\theta)$ with $f:\mathcal{X}\to[0,1]^C$, typically via the softmax,
$$\mathrm{softmax}(a):=\left[\frac{e^{a_1}}{\sum_{c'=1}^C e^{a_{c'}}},\dots,\frac{e^{a_C}}{\sum_{c'=1}^C e^{a_{c'}}}\right].$$
Fitting uses the negative log-likelihood as loss, $\ell(y,f(x;\theta))=-\log p(y\mid f(x;\theta))$, with the average NLL
$$\mathrm{NLL}(\theta)=-\frac{1}{N}\sum_{n=1}^N \log p(y_n\mid f(x_n;\theta)),$$
minimized to obtain the MLE $\hat\theta_{\mathrm{mle}}=\arg\min_\theta \mathrm{NLL}(\theta)$. For regression under Gaussian noise $p(y\mid x;\theta)=\mathcal{N}(y\mid f(x;\theta),\sigma^2)$, the NLL is proportional to mean squared error, so MLE $\equiv$ least squares. Chapter 4 generalizes this to empirical risk minimization, $\mathcal{L}(\theta;\mathcal{D})=\frac{1}{N}\sum_n \ell(y_n,\theta;x_n)$, and develops Bayesian inference via Bayes' rule $p(\theta\mid\mathcal{D})\propto p(\mathcal{D}\mid\theta)\,p(\theta)$, the posterior predictive $p(y\mid x,\mathcal{D})=\int p(y\mid x,\theta)\,p(\theta\mid\mathcal{D})\,d\theta$ (a Bayes model average), MAP estimation, conjugate priors, empirical Bayes (type-II maximum likelihood), and the frequentist sampling-distribution view. Regularization is introduced as $\mathcal{L}(\theta)+\lambda\, C(\theta)$ with $C(\theta)=-\log p(\theta)$, recovering MAP estimation and (for $C(\theta)=\lVert w\rVert_2^2$) ridge regression. Model selection uses validation risk and $K$-fold cross-validation.

## Data
None — this is a textbook, not an empirical study. Illustrative datasets (Iris, MNIST/image classification) are used pedagogically, and a companion set of Python notebooks (`probml.github.io/book1`) accompanies the text.

## Key findings
As a textbook, the "findings" are canonical results assembled and unified, including: (i) **MLE $\equiv$ least squares** under Gaussian noise; (ii) **MLE $\equiv$ minimizing KL divergence** $D_{\mathrm{KL}}(p\Vert q)$ between the empirical and model distributions, and equivalently minimizing cross-entropy; (iii) **log-loss as a tight convex upper bound on 0-1 loss**; (iv) **MAP $\equiv$ regularized ERM**, with a uniform prior recovering the MLE; (v) the **bias-variance tradeoff**, where MSE decomposes into squared bias plus variance (and ridge/MAP trades bias for variance); (vi) the asymptotic **Gaussian sampling distribution of the MLE**; (vii) the distinction between **epistemic (model) and aleatoric (data) uncertainty**; and (viii) the taxonomy of missingness — MCAR, MAR, NMAR — governing when the missing-data mechanism can be ignored.

## Contribution
A single-volume, modern, probabilistically-coherent entry point to ML at the graduate level, deliberately tracing "one particular path through this interconnected landscape, using probability theory as our unifying lens." It bridges ML with statistics, econometrics, and information theory, and explicitly situates ML relative to predictive analytics, data mining, data science, and AI. The Discussion also flags the alignment problem, reward hacking, inverse reinforcement learning, and the AGI-vs.-augmented-intelligence (IA) framing — connecting technical content to AI-safety concerns.

## Limitations & open questions
Being a textbook, its "open problems" are conceptual caveats Murphy raises explicitly: the **alignment problem** — the gap between what we ask algorithms to optimize and what we actually want — and **reward hacking** from misspecified loss functions; the difficulty of specifying loss functions that capture all preferences and multi-objective tradeoffs; the limits of imitating human behavior (inverse RL can inherit data bias). It defers advanced inference (variational inference, MCMC, deep generative models, causality) to the sequel (Murphy 2023). For a reader in choice modeling, an implicit open hook is how the Bayesian model-averaging / posterior-predictive machinery relates to and potentially improves estimation in discrete-choice and social-preference models (a connection the user flagged in their own annotations).

## Connections
The direct predecessor is Murphy's *Machine Learning: A Probabilistic Perspective* (2012); the sequel is *Probabilistic Machine Learning: Advanced Topics* (2023). It sits in the MIT *Adaptive Computation and Machine Learning* series alongside Bishop's *Pattern Recognition and Machine Learning*, Rasmussen & Williams' *Gaussian Processes*, Koller & Friedman's *Probabilistic Graphical Models*, and Sutton & Barto's *Reinforcement Learning*. It cites Mitchell's classic definition of learning and Russell's *Human Compatible* on alignment. Most relevant to this vault: the user's own annotations link the **Bayesian model averaging / posterior predictive** treatment (Ch. 4) to **mixed logit** estimation and to **[[@Bruhin2019|Bruhin, Fehr & Schmidt (2019)]]**'s individual-level estimation of social preferences — suggesting that integrating over a parameter posterior (rather than relying on point individual-level estimates) may be a methodologically superior route for the user's social-preference and choice-prediction work. The MLE/MAP/ERM/regularization scaffolding here is the statistical backbone for the user's [[predicting-comparative-social-preferences]] line of research.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
