---
citekey: Athey2019
title: Machine Learning Methods That Economists Should Know About
authors: ["Athey, Susan", "Imbens, Guido W."]
year: 2019
type: journalArticle
doi: 10.1146/annurev-economics-080217-053433
zotero: "zotero://select/library/items/VAGN8SLY"
pdf: /Users/jesper/Zotero/storage/H7Y8VLG6/Athey2019.pdf
tags: [literature]
keywords: [machine-learning, causal-inference, treatment-effect-heterogeneity, double-machine-learning, policy-learning, multi-armed-bandits, econometrics]
topics: []
related: [Hartford2016]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We discuss the relevance of the recent machine learning (ML) literature for economics and econometrics. First we discuss the differences in goals, methods, and settings between the ML literature and the traditional econometrics and statistics literatures. Then we discuss some specific methods from the ML literature that we view as important for empirical researchers in economics. These include supervised learning methods for regression and classification, unsupervised learning methods, and matrix completion methods. Finally, we highlight newly developed methods at the intersection of ML and econometrics that typically perform better than either off-the-shelf ML or more traditional econometric methods when applied to particular classes of problems, including causal inference for average treatment effects, optimal policy estimation, and estimation of the counterfactual effect of price changes in consumer choice models.

## Summary
Athey and Imbens survey the machine-learning toolkit they argue belongs in the core graduate econometrics curriculum. Framing the divide through Breiman's (2001) "two cultures," they contrast econometrics' focus on estimands, consistency, and inference with ML's focus on algorithms, out-of-sample predictive performance, and error-rate guarantees. After reviewing supervised methods (regularized regression, trees/forests, neural nets, boosting, SVMs), unsupervised methods (clustering, GANs), and matrix completion, the review's payoff is the intersection of ML and causal inference: doubly robust/orthogonalized estimation of average treatment effects, heterogeneous treatment effects via causal forests, optimal policy learning, and bandits for adaptive experimentation. The recurring lesson is that off-the-shelf ML optimized for prediction is the wrong tool for causal estimands, and purpose-built hybrids dominate.

## Research question
What parts of the modern ML literature are genuinely useful to empirical economists, and how must those methods be adapted when the target is a causal or structural parameter (with valid inference) rather than a prediction? Why has economics been slower than statistics to adopt ML, and which methods should enter the standard econometrics training?

## Method / identification
This is a methodological review, not an empirical paper. It formalizes the goals contrast: econometrics specifies an estimand as a functional of the data distribution and estimates parameters by minimizing an in-sample objective (e.g., least squares, MLE), prizing large-sample efficiency and confidence intervals; ML instead seeks an estimator $(\hat\alpha,\hat\beta)$ minimizing out-of-sample loss such as squared prediction error $(Y_{N+1}-\hat Y_{N+1})^2$, noting that beyond two regressors least squares is inadmissible. Core machinery surveyed: cross-validation and regularization for tuning; LASSO/ridge/elastic nets; regression trees, which greedily choose a covariate $k$ and threshold $c$ to minimize within-leaf squared error $Q(k,c)=\sum_{i:X_{ik}\le c}(Y_i-\bar Y_{k,c,l})^2+\sum_{i:X_{ik}>c}(Y_i-\bar Y_{k,c,r})^2$ then prune by cross-validation; random forests, boosting, deep nets, SVMs/kernels, $K$-means, GANs, and matrix completion. The causal core builds on potential outcomes under unconfoundedness $W_i\perp\!\!\!\perp(Y_i(0),Y_i(1))\mid X_i$. The ATE $\tau=E[Y_i(1)-Y_i(0)]$ is written via the efficient-score (doubly robust) representation using outcome model $\mu(w,x)=E[Y_i\mid W_i=w,X_i=x]$ and propensity $e(x)=E[W_i\mid X_i=x]$. The key device is **orthogonalization plus cross-fitting**: estimate nuisances $\hat\mu,\hat e$ by ML, plug into the influence function, and the resulting ATE estimate is efficient provided the product of nuisance error rates is $o(N^{-1/2})$, so each may converge as slowly as $N^{-1/4}$. Cross-fitting/sample-splitting/out-of-bag prediction ensures observation $i$'s nuisance values are estimated without $i$'s outcome.

## Data
None. The review uses stylized examples (a normal linear model, binary-outcome bandits with Beta posteriors) and cites empirical applications elsewhere rather than analyzing a dataset.

## Key findings
- **Prediction-optimal model selection is biased for causal targets.** Belloni et al. (2014): selecting covariates only to predict $Y$ can severely bias $\hat\tau$ because covariates strongly correlated with $W_i$ matter even if weakly correlated with $Y$; one must select on both the outcome and the treatment equations.
- **Orthogonalization/double robustness rate result.** Plug-in efficient ATE estimation is $\sqrt N$-efficient when $E\{[\hat\mu-\mu]^2\}^{1/2}\,E\{[\hat e-e]^2\}^{1/2}=o(N^{-1/2})$; errors in the nuisances are orthogonal to errors in the score, giving robustness to ML estimation error.
- **Covariate balancing** (Athey, Imbens & Wager 2016a; Zubizarreta 2015) can outperform plug-in propensity weighting when there are many weak confounders, by directly optimizing weights for covariate balance.
- **Heterogeneous effects need adapted criteria.** The CATE $\tau(x)=E[\tau_i\mid X_i=x]$ is identified under unconfoundedness, but its MSE criterion $\sum_i[\tau_i-\hat\tau(X_i)]^2/N$ is infeasible (the "fundamental problem of causal inference"), so standard cross-validation/regularization must be redesigned (Athey & Imbens 2016; generalized random forests, Athey, Tibshirani & Wager 2016b).
- **Optimal policy learning.** Athey & Wager (2017) bound the regret of policies of limited complexity, using semiparametric efficiency to sharpen ML regret bounds; the policy problem $\max_{\pi\in\Pi}\sum_i[2\pi(X_i)-1]\,\hat\Gamma_i$ can be recast as a classification problem.
- **Adaptive experimentation.** Multi-armed bandits (Thompson sampling, UCB) beat fixed A/B designs by balancing exploration and exploitation; with Beta-binomial conjugacy, Thompson sampling assigns arms in proportion to their posterior probability of being optimal, and its stochastic assignment aids randomization inference.

## Contribution
A widely cited, agenda-setting synthesis that translates ML for economists, clarifies why predictive guarantees differ from econometric inference, and curates the hybrid methods (double ML, causal forests, policy learning, contextual bandits, matrix completion for panel data) where ML-econometrics combinations dominate either field's standalone tools. It argues these belong in graduate training and helps economists communicate across disciplines.

## Limitations & open questions
- No general theory ranks supervised learners (deep nets vs. forests); the authors doubt uniform comparison results will ever be available.
- Many ML estimators (e.g., the neural-net IV estimator of [[@Hartford2016|Hartford et al. 2016]]) lack distributional theory, limiting valid inference.
- Designing feasible cross-validation/regularization criteria for causal/structural parameters remains hard because the relevant loss is unobservable.
- Estimated optimal policies $\hat\tau(x)>0$ may be complex and non-smooth, motivating restricted policy classes.
- Researchers should "articulate clearly the goals of their analysis" and which estimator properties matter — an implicit call to reconcile predictive and inferential standards.

## Connections
Anchored by Breiman (2001) on the two cultures of statistical modeling and Mullainathan & Spiess (2017) on prediction-as-substantive-problem. The causal-inference core builds on Rosenbaum & Rubin (1983) and Imbens & Rubin (2015) on unconfoundedness, Robins & Rotnitzky (1995) on doubly robust estimation, and Chernozhukov et al. (2017, 2018) on double/debiased machine learning. Heterogeneous effects and policy learning draw on Athey & Imbens (2016), Wager & Athey (2017) and Athey, Tibshirani & Wager (2016b) on (generalized/causal) random forests, Künzel et al. (2017) on meta-learners, Nie & Wager (2019) on the R-learner, Chipman et al. (2010) and Hill (2011) on BART, and Kitagawa & Tetenov (2015), Hirano & Porter (2009), and Athey & Wager (2017) on optimal policy/regret. The bandit material connects Thompson (1933), Lai & Robbins (1985), and Sutton & Barto (1998). Companion overviews include Athey & Imbens (2017b) on the state of applied econometrics and Belloni, Chernozhukov & Hansen (2014) on high-dimensional inference.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
