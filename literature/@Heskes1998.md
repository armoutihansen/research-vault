---
citekey: Heskes1998
title: Bias/Variance Decompositions for Likelihood-Based Estimators
authors: ["Heskes, Tom"]
year: 1998
type: journalArticle
doi: 10.1162/089976698300017232
zotero: "zotero://select/library/items/882FNSKH"
pdf: /Users/jesper/Zotero/storage/D2KB4755/Heskes1998.pdf
tags: [literature]
keywords: [bias-variance-decomposition, kullback-leibler-divergence, log-likelihood, logarithmic-opinion-pool, ensemble-learning, cross-entropy, zero-one-loss]
topics: []
related: [Tibshirani1996]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> The bias/variance decomposition of mean-squared error is well understood and relatively straightforward. In this note a similar simple decomposition is derived, valid for any kind of error measure that, when using the appropriate probability model, can be derived from a Kullback-Leibler divergence or loglikelihood.

## Summary
This short theoretical note derives a clean, general bias/variance decomposition for any likelihood-based error measure, generalizing the familiar mean-squared-error (MSE) result. The key move is to treat the loss not as a direct distance between a model output and a target, but as a Kullback-Leibler (KL) divergence between a probability statement induced by the model and a target probability. Heskes shows that if the "average model" is defined as the *geometric* mean of the ensemble densities (a logarithmic opinion pool) rather than the usual arithmetic mean, then error decomposes exactly as $\text{error} = \text{bias} + \text{variance}$, with the variance provably independent of the target. MSE falls out as the special case where outputs estimate the mean of a fixed-variance Gaussian. The framework yields a new decomposition for cross-entropy/log-loss and recovers zero-one loss only as a degenerate limit.

## Research question
Can the well-behaved bias/variance decomposition of mean-squared error be generalized to arbitrary likelihood-based loss functions (KL divergence, log-likelihood, cross-entropy) in a way that satisfies a set of natural desiderata — in particular, that the variance term is nonnegative and does *not* depend directly on the target distribution, while the bias depends only on the target and a well-defined average model?

## Method / identification
The setup is decision-theoretic over an ensemble of estimators. Let $Y$ be a (continuous or discrete) random variable, $q(y)$ the target density, and $\hat{p}(y)$ a density estimator (e.g., a probability statement read off a neural network output). There is an ensemble of such estimators — typically produced by running a learning algorithm on different training sets drawn from the same domain — and $E$ denotes expectation over that ensemble. Distance is measured by the KL divergence
$$K(q,\hat{p}) \equiv \int dy\, q(y)\log\frac{q(y)}{\hat{p}(y)}.$$
Following James and Hastie (1997), the **variance** is *defined* as the smallest average KL divergence between the estimators and some "average model" $\bar{p}$:
$$\text{variance} = \min_{a:\int a(y)\,dy=1} E\,K(a,\hat{p}) = E\,K(\bar{p},\hat{p}).$$
Solving this constrained minimization with a Lagrange multiplier (functional derivative w.r.t. $a(y)$) gives the average model as a *normalized geometric mean*:
$$\bar{p}(y) = \frac{1}{Z}\exp\!\big[E\log\hat{p}(y)\big],$$
i.e., a **logarithmic opinion pool**, not the arithmetic mean $E\,\hat{p}(y)$ used by Hall (1987) and Wolpert (1997). The **bias** is then defined as $K(q,\bar{p})$. Substituting the average model into the error and showing that $\log Z = -E\,K(\bar{p},\hat{p}) = -\text{variance}$ yields the exact additive decomposition
$$\text{error} = E\,K(q,\hat{p}) = K(q,\bar{p}) + E\,K(\bar{p},\hat{p}) = \text{bias} + \text{variance}.$$
There is no intrinsic-noise term here because a learner reproducing $q$ achieves zero KL. When only a single observation $Y=t$ is available rather than the full target density, the same derivation on the log-likelihood gives
$$-E\log\hat{p}(t) = -\log\bar{p}(t) + E\,K(\bar{p},\hat{p}),$$
and integrating over the target-generating density $q(t)$ recovers a three-way split $\text{error} = \text{intrinsic noise} + \text{bias} + \text{variance}$, where the intrinsic noise equals the Shannon entropy of $q$.

## Data
None — this is a purely theoretical note. No datasets or experiments; the only empirical content is worked analytical examples (Gaussian/MSE, mean-and-variance estimation, binary cross-entropy, zero-one loss).

## Key findings
- **General decomposition (Eq. 4/6).** For any likelihood-based estimator there exists an average model $\bar{p}$ — the logarithmic opinion pool — such that error splits exactly into bias plus variance, the variance is nonnegative and does *not* depend directly on the target density, and the bias depends only on $q$ and $\bar{p}$. This satisfies all three of the James–Hastie desiderata simultaneously, which the author stresses is nontrivial.
- **MSE as a special case.** Interpreting outputs $\hat{m}$ as the mean of a fixed-variance Gaussian makes the log-opinion-pool average $\bar{m}=E\,\hat{m}$ and recovers the classical $E[(\hat{m}-t)^2] = (\bar{m}-t)^2 + E[(\hat{m}-\bar{m})^2]$ up to a constant.
- **Mean-and-variance estimation.** With estimates of both mean and variance, the average model is Gaussian with *reciprocal-variance* averaging $1/\bar{\sigma}^2 = E(1/\hat{\sigma}^2)$ and precision-weighted mean $\bar{m}/\bar{\sigma}^2 = E(\hat{m}/\hat{\sigma}^2)$, with a corresponding closed-form decomposition.
- **Cross-entropy (new result).** For binary $Y$, the average model is obtained by *averaging the logits*: $\log\frac{\bar{p}}{1-\bar{p}} = E\log\frac{\hat{p}}{1-\hat{p}}$. The resulting decomposition (Eq. 7) has a variance term that, with the ensemble-generating operation held fixed, is independent of the target $t$ — contrasting favorably with Wolpert's (1997) decomposition (Eq. 8), whose variance still depends on $t$.
- **Zero-one loss as a limit.** Encoding a hard classification as a probability statement assigning $1$ to the predicted class and $\epsilon\ll1$ elsewhere, the log-opinion-pool average becomes the **majority vote** $\bar{y}=\arg\max_y f(y)$ as $\epsilon\to0$. Dividing by $-\log\epsilon$ yields $1-f(t) = [f(\bar{y})-f(t)] + [1-f(\bar{y})]$. This obeys the first two requirements but *breaks the third*: the limiting operation destroys the interpretation of the first term as the error of the average model, since it still depends on class frequencies $f(y)$.

## Contribution
A unifying, one-page-deep theoretical result showing that the elegant additivity of the MSE bias/variance decomposition is not special to squared error but holds for the entire family of KL/log-likelihood-based losses, *provided* the average model is taken as a geometric (logarithmic-pool) mean. It clarifies why prior KL decompositions (Hall 1987; Wolpert 1997) had a target-dependent variance — they used the arithmetic mean — and it argues, via the zero-one case, in favor of *first defining the variance* and deriving the bias, rather than the reverse.

## Limitations & open questions
- **Zero-one loss is only a degenerate limit.** The $\epsilon\to0$ construction loses the "error of the average model" interpretation, and the author concedes the exact split of the first term into bias and inherent noise "seems to be somewhat arbitrary." No fully satisfactory zero-one decomposition emerges; the author explicitly notes that *none* of the existing zero-one decompositions satisfies all three requirements.
- **Asymmetry of KL.** The decomposition depends on the direction of the KL divergence: reversing it gives the *linear* opinion pool $\bar{p}=E\,\hat{p}$ as the average model, but that error measure "cannot be transformed into a log-likelihood" for finite observations, limiting its use.
- **Zero-probability pathology.** The logarithmic opinion pool assigns probability zero to any outcome that any single estimator rules out — defensible from a Bayesian standpoint but a drawback "if the densities are not carefully estimated."
- **Absolute vs. relative values.** For zero-one loss the author notes practitioners care only about *changes* in bias and variance, not their absolute values — leaving the absolute decomposition partly conventional.
- The note is silent on estimation/finite-sample issues: how to estimate these terms from a finite number of training sets, and how the framework interacts with model averaging in practice, are left open.

## Connections
The paper sits squarely in the late-1990s line of work generalizing the classic MSE bias/variance dilemma of Geman, Bienenstock and Doursat (1992) to other losses. It adopts the desiderata and variance-first philosophy of James and Hastie (1997) and is most directly a corrective to Wolpert's (1997) "On bias plus variance" and Hall's (1987) KL-loss decomposition, both of which used arithmetic averaging and obtained target-dependent variance terms. The zero-one-loss discussion engages with Breiman (1996), Dietterich and Bakiri (1995), Friedman (1996), [[@Tibshirani1996|Tibshirani (1996)]], and Kohavi and Wolpert (1996). The central technical device — the logarithmic opinion pool / geometric mean of expert densities — connects to the literature on combining probability forecasts (Bordley 1982; Genest and Zidek 1986; Jacobs 1995) and to the author's own companion work on selecting weighting factors in logarithmic opinion pools (Heskes 1998, NIPS 10). The mean-and-variance example links to input-dependent-noise regression (Bishop and Qazaz 1997; Williams 1996).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
