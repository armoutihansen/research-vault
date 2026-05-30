---
citekey: Peysakhovich2017
title: Using methods from machine learning to evaluate behavioral models of choice under risk and ambiguity
authors: ["Peysakhovich, Alexander", "Naecker, Jeffrey"]
year: 2017
type: journalArticle
doi: 10.1016/j.jebo.2016.08.017
zotero: "zotero://select/library/items/EDP3FYWM"
pdf: /Users/jesper/Zotero/storage/BA724Q3Y/Peysakhovich2017.pdf
tags: [literature]
keywords: [machine-learning, risk-preferences, ambiguity-aversion, probability-weighting, out-of-sample-prediction, behavioral-economics, explainable-variance]
topics: []
related: [Charness2002, Erev2010, Kahneman1979, Tibshirani1996, Tversky1992]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> How can behavioral science incorporate tools from machine learning (ML)? We propose that ML models can be used as upper bounds for the "explainable" variance in a given data set and thus serve as upper bounds for the potential power of a theory. We demonstrate this method in the domain of uncertainty. We ask over 600 individuals to make a total of 6000 choices with randomized parameters and compare standard economic models to ML models. In the domain of risk, a version of expected utility that allows for non-linear probability weighting (as in cumulative prospect theory) and individual-level parameters performs as well out-of-sample as ML techniques. By contrast, in the domain of ambiguity, two of the most widely studied models (a linear version of maximin preferences and second order expected utility) fail to compete with the ML methods. We open the "black boxes" of the ML methods and show that under risk we "rediscover" expected utility with probability weighting. However, in the case of ambiguity the form of ambiguity aversion implied by our ML models suggests that there is gain from theoretical work on a portable model of ambiguity aversion. Our results highlight ways in which behavioral scientists can incorporate ML techniques in their daily practice to gain genuinely new insights.

## Summary
Peysakhovich and Naecker propose using flexible machine-learning predictors as an estimate of the *explainable* variance in a choice data set, so that a structural economic model's out-of-sample fit can be benchmarked not against zero but against this empirical ceiling ("headroom"). Applied to willingness-to-pay (WTP) for lotteries, the method delivers a sharp verdict: under **risk**, expected utility with Prelec probability weighting and individual-level parameters matches a 55,000-parameter regularized regression, and the ML "black box" is shown to re-discover the same S-shaped weighting curve; under **ambiguity**, the two standard models (linear maximin and second-order expected utility) are decisively beaten by ML, and the implied ambiguity penalty is *convex* rather than linear, signalling that existing portable models miss structure that a parsimonious model could capture.

## Research question
How good are standard economic models of choice under uncertainty in absolute terms? Specifically: what fraction of the *explainable* (as opposed to total) variance in choice do they capture out-of-sample, and which domains of uncertainty are fruitful targets for new theory? The paper reframes model evaluation away from in-sample nested hypothesis tests toward out-of-sample prediction relative to an ML-estimated upper bound.

## Method / identification
The core methodological proposal: train a deliberately over-parameterized, regularized ML predictor on the same task and use its **test-set accuracy as an estimate of explainable variance**, giving an upper bound on any theory's achievable predictive power. Model quality is then explained variance as a *proportion of explainable variance*.

Economic models for **risk** (CRRA expected utility, EU):
$$\text{EU}(L) = p_{red}\,(\text{money}_{red})^{\alpha} + p_{blue}\,(\text{money}_{blue})^{\alpha}$$
with risk-aversion parameter $\alpha\in[0,1]$ ($\alpha=1$ risk-neutral). WTP is treated as the certainty equivalent, so parameters are fit via $\text{WTP}^{\alpha} = p_{red}\,(\text{money}_{red})^{\alpha} + p_{blue}\,(\text{money}_{blue})^{\alpha}$. Expected utility with probability weighting (EUP) adds a Prelec (1998) one-parameter weighting function:
$$f(p) = \frac{p^{\gamma}}{\left(p^{\gamma} + (1-p)^{\gamma}\right)^{1/\gamma}}$$
so $\text{EUP}(L) = f(p_{red})(\text{money}_{red})^{\alpha} + f(p_{blue})(\text{money}_{blue})^{\alpha}$, with $\gamma=1$ recovering linear weighting. Each model is fit both as a single representative agent and with individual-level parameters (adding ~300-fold parameters).

ML benchmark: **regularized regression** minimizing
$$\lVert y - X\beta\rVert^{2} + \lambda\,\lVert\beta\rVert_{P}$$
where $X$ is a polynomial basis expansion (quadratic terms plus all up-to-three-way interactions) of the decision features $\{p_{red},p_{blue},p_{green},\text{money}_{red},\text{money}_{blue}\}$, optionally interacted with subject dummies (yielding $>55{,}000$ coefficients, far exceeding the ~2100 training rows, making penalization essential). $P=1$ is lasso (sparsifying), $P=2$ is ridge; $\lambda$ is chosen by 7-fold cross-validation (one decision per individual per fold).

Economic models for **ambiguity** use states $w\in[0,1]$, increasing winning function $g(w)=w$, and a Bayesian posterior $p(X,Y)$ that is uniform on $[X,100-Y]$ given the partial information. The subjective win probability is $P(X,Y)=\int g(w)\,dp(X,Y)$. The **linear maximin** model is
$$U(X,Y,z) = \bigl(1 - \gamma(X+Y)\bigr)\,P(X,Y)\,z^{\alpha}$$
($\gamma=0$ reduces to EU; downweighting active when $X+Y<1$). **Second-order expected utility (SOEU)** is
$$U(X,Y,z) = \int \bigl(g(w)\,z^{\alpha}\bigr)^{\gamma}\,dp(X,Y)$$
($\gamma=1$ or degenerate $p$ recovers EU). "Opening the black box" traces implied curves by feeding controlled inputs through the fitted ridge model.

## Data
Original online experiments on Amazon Mechanical Turk (IRB-approved), all hypothetical WTP elicitations on 100-ball urn lotteries. **Risk:** $N_{recruited}=350$, $N_{sample}=315$ after a comprehension-quiz screen; each subject states WTP for 10 randomly generated lotteries (features drawn uniformly, prizes \$5–\$30), split 7 train / 3 test per person. **Ambiguity:** a separate sample ($N_{recruited}=350$, $N_{sample}=287$) using the Levy et al. (2010) / Peysakhovich and Karmarkar (2015) "at least X red, at least Y blue" design. Across both studies ~600+ participants and ~6000 choices.

## Key findings
1. **Risk:** Regularized regression beats plain EU by a large margin, but individual-level **EUP ties the ML models** out-of-sample. Probability weighting is the decisive feature; an interpretable ~600-parameter EUP matches a ~55,000-parameter predictor. Lasso underperforms ridge, indicating the basis expansion has *no* useful sparsity (many small but jointly important coefficients).
2. **Representative-agent assumption is highly restrictive:** ignoring individual heterogeneity cripples every model's predictive power.
3. **Black box (risk):** tracing the ridge model's implied weighting curve recovers the familiar S-shaped Prelec curve; predictions agree within ~\$1 except near $p\approx1$ (where the unconstrained ML curve need not return weight 1, and data are sparse).
4. **Ambiguity:** neither maximin nor SOEU competes with ridge. Here individual-level **lasso outperforms ridge**, implying genuine sparsity in the ambiguity parameter space.
5. **Black box (ambiguity):** the ML-implied ambiguity penalty is **convex** in the amount of residual ambiguity (not linear as maximin implies) and reproduces the predicted favorable/unfavorable information asymmetry of Peysakhovich and Karmarkar (2015) — suggesting maximin is "on the right track" but needs tuning analogous to what weighting adds to EU.

## Contribution
Introduces ML-as-explainable-variance-ceiling as a general, quantitative replacement for "ocular least squares" model checking and for pure prediction competitions (which lack a headroom estimate). It substantively vindicates probability weighting under risk while identifying ambiguity as an open theoretical frontier, and demonstrates "opening the black box" to extract interpretable structure (weighting and penalty curves) from a flexible predictor.

## Limitations & open questions
The authors explicitly flag: (i) developing a **simple, portable, parsimonious "plug-and-play" model of ambiguity aversion** whose penalty is convex — the paper's central project-idea hook; (ii) extending the analysis to other ambiguity models (rank-dependent utility, expected uncertain utility, variational preferences, smooth ambiguity) and checking whether each wins on different regions of the parameter space, hinting at a "final" model; (iii) **combining regularization, cross-validation and variable selection with richer structural economic models** rather than fitting the economic side by plain MLE; (iv) imposing economic axioms on ML via **parameter-sharing / invariance constraints** (e.g. color symmetry, weight $=1$ at $p=1$); (v) testing whether better structural models of preference also predict *field* behavior and perform better when nested in larger market models. They also note hypothetical online stakes and an experienced MTurk pool as caveats (argued to be features here), and SOEU's computational cost (numerical integration) as a tractability concern.

## Connections
Methodologically descends from Roth and Erev (1995) and the [[@Erev2010|Erev et al.]] (2010, 2015) choice-prediction competitions, and from Varian (2014), Athey and Imbens (2015), Wager and Athey (2015) on ML in econometrics/causal inference; the explainable-variance idea parallels Kleinberg, Liang and Mullainathan (2015) on randomness perception and is applied to social preferences by Epstein, Peysakhovich and Rand (2016) — extending the [[@Charness2002|Charness and Rabin (2002)]] tradition. On risk it builds on [[@Kahneman1979|Kahneman and Tversky (1979)]], [[@Tversky1992|Tversky and Kahneman (1992)]], Prelec (1998) and Gonzalez and Wu (1999) (weighting curvature). On ambiguity it engages Ellsberg (1961), Gilboa and Schmeidler (1989), Klibanoff et al. (2005), Maccheroni et al. (2006), Grant et al. (2009), Gul and Pesendorfer (2014), and the Machina-paradox experiments of L'Haridon and Placido (2009), Baillon et al. (2011) and Machina (2009). Estimation rests on [[@Tibshirani1996|Tibshirani (1996)]] (lasso) and Friedman, Hastie and Tibshirani's glmnet.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
