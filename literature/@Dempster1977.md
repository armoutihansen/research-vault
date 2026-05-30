---
citekey: Dempster1977
title: Maximum Likelihood from Incomplete Data Via the EM Algorithm
authors: ["Dempster, A. P.", "Laird, N. M.", "Rubin, D. B."]
year: 1977
type: journalArticle
doi: 10.1111/j.2517-6161.1977.tb01600.x
zotero: "zotero://select/library/items/8AYNAJJT"
pdf: /Users/jesper/Zotero/storage/APLTF7WY/Dempster1977.pdf
tags: [literature]
keywords: [em-algorithm, maximum-likelihood, incomplete-data, missing-data, latent-variables, convergence-theory, exponential-family]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A broadly applicable algorithm for computing maximum likelihood estimates from incomplete data is presented at various levels of generality. Theory showing the monotone behaviour of the likelihood and convergence of the algorithm is derived. Many examples are sketched, including missing value situations, applications to grouped, censored or truncated data, finite mixture models, variance component estimation, hyperparameter estimation, iteratively reweighted least squares and factor analysis.

## Summary

This is the foundational paper that names, unifies, and provides general convergence theory for the Expectation–Maximization (EM) algorithm: an iterative scheme for computing maximum-likelihood (ML) estimates when the observed data $y$ can be viewed as an incomplete (many-to-one) function of unobserved complete data $x$. Each iteration alternates an expectation step (E-step), which computes the conditional expectation of the complete-data log-likelihood given the observed data and the current parameter, and a maximization step (M-step), which maximizes that expectation. The authors prove that the observed-data likelihood is non-decreasing across iterations and characterize fixed points and convergence rates, then exhibit the breadth of the method across a wide catalogue of statistical models.

## Research question

How can one construct a single, general-purpose, theoretically grounded iterative algorithm for finding ML estimates (or posterior modes) in the pervasive class of problems where the data are "incomplete" — i.e. arising from missing values, grouping, censoring, truncation, latent variables, mixtures, or variance components — rather than deriving a separate ad hoc procedure for each special case?

## Method / identification

The formal setup posits two sample spaces, complete-data space $\mathcal{X}$ and observed space $\mathcal{Y}$, with a many-to-one map $x \mapsto y(x)$. A complete-data sampling density $f(x\mid\phi)$ induces the observed-data density by integrating over the fiber $\mathcal{X}(y)$:
$$g(y\mid\phi) = \int_{\mathcal{X}(y)} f(x\mid\phi)\, dx.$$
EM maximizes $L(\phi)=\log g(y\mid\phi)$ indirectly via $f$. The general iteration $\phi^{(p)}\to\phi^{(p+1)}$ is defined through the function
$$Q(\phi'\mid\phi) = E\!\left[\log f(x\mid\phi') \mid y, \phi\right],$$
with the **E-step** computing $Q(\phi\mid\phi^{(p)})$ and the **M-step** choosing $\phi^{(p+1)}=\arg\max_\phi Q(\phi\mid\phi^{(p)})$. For a regular exponential family $f(x\mid\phi)=b(x)\exp(\phi t(x)^T)/a(\phi)$, the E-step reduces to estimating the complete-data sufficient statistics $t^{(p)}=E(t(x)\mid y,\phi^{(p)})$ and the M-step to solving the ordinary likelihood equations $E(t(x)\mid\phi)=t^{(p)}$. A key analytic device decomposes the log-likelihood as $L(\phi)=Q(\phi\mid\phi)... $ via $Q(\phi'\mid\phi)=L(\phi')+H(\phi'\mid\phi)$, where $H(\phi'\mid\phi)=E[\log k(x\mid y,\phi')\mid y,\phi]$ and $k(x\mid y,\phi)=f(x\mid\phi)/g(y\mid\phi)$ is the conditional density of the missing information. The authors also define a **generalized EM (GEM)** algorithm, requiring only that the M-step *increase* (not maximize) $Q$, i.e. $Q(M(\phi)\mid\phi)\succeq Q(\phi\mid\phi)$. The same machinery yields posterior modes by maximizing $Q(\phi\mid\phi^{(p)})+G(\phi)$ where $G$ is the log-prior.

## Data

None — this is a methodological/theoretical paper. The only empirical illustration is a worked numerical example using Rao's (1965) genetic multinomial data on 197 animals split into four categories with cell probabilities $(\tfrac{1}{2}+\tfrac{1}{4}\pi, \tfrac{1}{4}(1-\pi), \tfrac{1}{4}(1-\pi), \tfrac{1}{4}\pi)$, where EM converges to $\pi^*\approx 0.6268$ with an observed linear convergence rate near $0.1328$.

## Key findings

- **Lemma 1:** $H(\phi'\mid\phi)\le H(\phi\mid\phi)$, with equality iff $k(x\mid y,\phi')=k(x\mid y,\phi)$ a.e. (a Jensen-inequality consequence).
- **Theorem 1 (monotonicity):** every GEM algorithm satisfies $L(M(\phi))\ge L(\phi)$ for all $\phi$; the likelihood never decreases, and increases strictly unless a fixed point is reached. Corollaries show ML estimates are fixed points of GEM.
- **Theorem 2:** under boundedness of $L(\phi^{(p)})$ and a curvature condition on the increments of $Q$, the sequence $\phi^{(p)}$ converges to some $\phi^*$ in the closure of the parameter space.
- **Theorems 3–4 (stationarity and rate):** under differentiability and negative-definite $D^{20}Q$, the limit satisfies $DL(\phi^*)=0$, and the local convergence is linear with rate governed by $DM(\phi^*)=D^{20}H(\phi^*\mid\phi^*)\,[D^{20}Q(\phi^*\mid\phi^*)]^{-1}$. The rate equals the largest eigenvalue of $DM(\phi^*)$; intuitively, EM is fast when the "fraction of missing information" is small, since $-D^2L$ measures information in $y$ and $-D^{20}H$ measures the (Fisher) information lost through incompleteness.

## Contribution

The paper coins the term "EM algorithm" and recognizes that dozens of previously isolated procedures — Hartley's (1958) multinomial methods, Healy–Westmacott (1956) missing-value ANOVA fill-in, the Baum et al. (1970) hidden-Markov reestimation, Orchard–Woodbury's (1972) "missing information principle", finite-mixture estimation, variance-component and factor-analysis algorithms, iteratively reweighted least squares — are all instances of one general scheme. It supplies the unifying convergence theory (monotone likelihood ascent, fixed-point characterization, and a clean information-theoretic convergence-rate formula) that earlier special-case treatments lacked, and extends seamlessly to Bayesian posterior-mode computation.

## Limitations & open questions

- The authors note EM provides ML *point* estimates but does **not** directly deliver standard errors or the observed information matrix; obtaining variance estimates requires extra computation (an explicit gap later filled by supplemented-EM and Louis-type methods).
- A referee's criticism (recorded in a footnote) is acknowledged: EM is really a *family* of algorithms whose per-step E and M implementations vary enormously in feasibility; the paper does not specify the inner computations.
- Convergence is only to a **stationary point**, which may be a local rather than global maximum, and may be a saddle point if $DM(\phi^*)$ has eigenvalues exceeding unity; behavior on **ridges** of the likelihood (e.g. non-identifiable factor-analysis directions) is delicate.
- The M-step can itself be non-closed-form (e.g. truncated families), requiring nested iteration; speed-ups (Aitken acceleration, Newton steps, incremental "increase-Q" GEM, factored-likelihood splitting) are suggested but not fully developed.
- Slow convergence when the missing-information fraction is large is flagged as a practical concern.

## Connections

The general representation $DL(\phi)=E(t\mid y,\phi)-E(t\mid\phi)$ is credited to Sundberg (1974, 1976), building on unpublished lecture notes of Martin-Löf; Lemma 1 / Theorem 1 appeared in a special case in Baum, Petrie, Soules & Weiss (1970) for what became the Baum–Welch / hidden-Markov algorithm. Predecessors include Hartley (1958) for multinomial incomplete counts, Healy & Westmacott (1956) for ANOVA missing values, Orchard & Woodbury (1972) and Beale & Little (1975) for the multivariate-normal "missing information principle", Hartley & Hocking (1971) on convergence, Woodbury (1971), and Carter & Myers (1973), Brown (1974) and Fienberg & Chen (1976) on discrete-data variants. The missing-at-random framing draws on Rubin (1974, 1976). The worked example uses Rao (1965). The paper is foundational for later work on EM convergence (Wu's later analysis), variance estimation, the ECM and generalized-EM families, and is a cornerstone reference in machine learning for latent-variable models, mixtures, and the link to variational lower bounds on the likelihood.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
