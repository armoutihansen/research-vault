---
citekey: Gneiting2011
title: Making and Evaluating Point Forecasts
authors: ["Gneiting, Tilmann"]
year: 2011
type: journalArticle
doi: 10.1198/jasa.2011.r10138
zotero: "zotero://select/library/items/8CDU6ZUF"
pdf: /Users/jesper/Zotero/storage/YITSHXXE/Gneiting - 2011 - Making and Evaluating Point Forecasts.pdf
tags: [literature]
keywords: [proper-scoring-rules, elicitability, point-forecasts, consistent-scoring-functions, belief-elicitation, statistical-functionals, forecast-evaluation, loss-functions]
topics: []
related: [Gneiting2007, Lambert2008, Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Typically, point forecasting methods are compared and assessed by means of an error measure or scoring function, with the absolute error and the squared error being key examples. The individual scores are averaged over forecast cases, to result in a summary measure of the predictive performance, such as the mean absolute error or the mean squared error. I demonstrate that this common practice can lead to grossly misguided inferences, unless the scoring function and the forecasting task are carefully matched. Effective point forecasting requires that the scoring function be specified ex ante, or that the forecaster receives a directive in the form of a statistical functional, such as the mean or a quantile of the predictive distribution. If the scoring function is specified ex ante, the forecaster can issue the optimal point forecast, namely, the Bayes rule. If the forecaster receives a directive in the form of a functional, it is critical that the scoring function be consistent for it, in the sense that the expected score is minimized when following the directive. A functional is elicitable if there exists a scoring function that is strictly consistent for it. Expectations, ratios of expectations and quantiles are elicitable. For example, a scoring function is consistent for the mean functional if and only if it is a Bregman function. It is consistent for a quantile if and only if it is generalized piecewise linear. Similar characterizations apply to ratios of expectations and to expectiles. Weighted scoring functions are consistent for functionals that adapt to the weighting in peculiar ways. Not all functionals are elicitable; for instance, conditional value-at-risk is not, despite its popularity in quantitative finance.

## Summary
This review article develops a decision-theoretic foundation for *making and evaluating point forecasts*. Competing forecasters are routinely ranked by an average score $\bar S=\frac1n\sum_i S(x_i,y_i)$, with $S$ a scoring function such as squared error (SE), absolute error (AE) or absolute percentage error (APE); surveys (Tables 2-3) show these dominate academia, business and meteorology. The central message: such ranking is *meaningless* unless the task is specified — either by disclosing $S$ ex ante (so the forecaster issues the optimal Bayes rule) or by issuing a *directive* naming a target functional (mean, quantile, etc.) and scoring with a function *consistent* for it. A simulation study makes the danger vivid: a forecaster reporting a non-optimal functional can beat the truth-teller purely because the wrong score is used, so naive comparisons "grossly misguide" inference.

## Research question
When and how is it legitimate to compare point forecasts by an average score? Equivalently: given a statistical functional $T$ (mean, median, quantile, expectile, ratio of expectations, CVaR), which scoring functions $S$ reward truthful reporting of $T$, and which functionals admit such a scoring function at all (are *elicitable*)?

## Method / identification
This is a decision-theory / mathematical-statistics paper; the apparatus is the relationship between scoring functions, optimal point forecasts and statistical functionals.

A functional $T$ maps a predictive distribution $F$ to a subset of the action domain $D$; the *Bayes rule* is $\hat x=\arg\min_x E_F S(x,Y)$. Key definition: $S$ is **consistent** for $T$ relative to a class $\mathcal F$ if $E_F S(t,Y)\le E_F S(x,Y)$ for all $F\in\mathcal F$, $t\in T(F)$, $x\in D$; **strictly consistent** if equality forces $x\in T(F)$. $T$ is **elicitable** if some $S$ is strictly consistent for it (term from [[@Lambert2008|Lambert, Pennock & Shoham 2008]]; concept from Osband 1985).

Structural results: **Theorem 1** (duality) — $S$ is consistent for $T$ iff every $x\in T(F)$ is a Bayes rule under $S$; making and evaluating are two sides of one coin. **Theorem 2** — consistent scoring functions form a convex cone. **Theorem 3** — every consistent $S$ induces a *proper scoring rule* $R(F,y)=S(t_F,y)$; the paper separates a proper scoring rule (on $\mathcal F\times D$, eliciting the whole distribution) from a consistent scoring function (on $D\times D$, eliciting one functional). **Theorem 4** (Osband's revelation principle) — elicitability is preserved under one-to-one reparametrization $T_g=g\circ T$. **Theorem 5** — *weighted* scores $S^{(w)}(x,y)=w(y)S(x,y)$ are consistent for $T^{(w)}(F)=T(F^{(w)})$, i.e. $T$ applied to the density-reweighted measure $\propto w(y)f(y)$. **Theorem 6** (Osband) — an elicitable functional has *convex level sets*; this necessary condition drives the negative results.

The constructive characterizations run through **Osband's principle**: if a smooth consistent $S$ exists, its first-argument gradient is an *identification function* $V$ with $E_F[V(x,Y)]=0\iff x\in T(F)$. Solving $\partial_x S(x,y)=h(x)V(x,y)$ and integrating recovers the general form of $S$ — with $V(x,y)=x-y$ for the mean, $V(x,y)=\mathbf 1(x\ge y)-\alpha$ for the $\alpha$-quantile, and $V(x,y)=2|\mathbf 1(x\ge y)-\tau|(x-y)$ for expectiles.

## Data
No empirical dataset. Evidence is (i) two literature surveys of 2008 journal volumes and business practitioner surveys documenting which scores are used (Tables 2-3), and (ii) a controlled *simulation study* on a volatile predictand contrasting "Mr. Bayes", an "optimist" and a "pessimist". The paper is otherwise pure theory.

## Key findings
The functional-by-functional characterizations are the core:

- **Mean / expectation (Theorem 7, [[@Savage1971|Savage 1971]]):** $S$ is (strictly) consistent for the mean iff it is a **Bregman function** $S(x,y)=\phi(y)-\phi(x)-\phi'(x)(y-x)$ with $\phi$ (strictly) convex. SE is the *unique* Bregman function that is both symmetric and of prediction-error form. The homogeneous Patton (2011) family — nesting SE ($b=2$) and QLIKE ($b=0$) — exhausts the homogeneous Bregman functions on $(0,\infty)^2$.
- **Ratios of expectations (Theorem 8):** $T(F)=E_F[r(Y)]/E_F[s(Y)]$ is elicitable, with an explicit $\phi$-based consistent form covering the squared-relative-error and observation-weighted scores (both consistent for $E_F[Y^2]/E_F[Y]$).
- **Quantiles (Theorem 9, classical Thomson 1979):** consistent iff *generalized piecewise linear* (GPL); AE is consistent for the median. APE is consistent not for the median but for the **median of order $-1$**, $\mathrm{med}^{(-1)}$, which systematically rewards severe *under*forecasts — a concrete warning to firms using APE.
- **Expectiles (Theorem 10):** elicitable; their consistent scores blend Bregman and GPL elements.
- **CVaR (Theorem 11) — negative result:** *conditional value-at-risk is not elicitable.* Two finite-support mixtures with equal CVaR but a strictly larger CVaR at their mean violate the convex-level-set necessary condition (Theorem 6). So no strictly consistent score exists, despite CVaR's popularity in finance.

The headline practical implication: SE elicits the mean, AE the median, and APE a non-standard underforecasting functional — so "use multiple error measures" is fine only if each is consistent for the named target.

## Contribution
Unifies a scattered literature (Savage, Thomson, Osband, Murphy & Daan) into a single elicitability/consistency framework, draws the sharp and previously-blurred line between proper scoring rules and consistent scoring functions, and supplies both classical and *new* characterizations (ratios of expectations, expectiles) plus the influential negative result that CVaR is not elicitable. It reframes forecast evaluation as a problem of matching score to directive, and turns Osband's principle into a working recipe for deriving consistent scores.

## Limitations & open questions
The paper itself flags several open problems: a **converse to Theorem 6** and, more broadly, a full **characterization of elicitability** (which functionals are elicitable?) remain open. The multivariate / vector-valued predictand case is only gestured at. The non-elicitability of CVaR leaves open how it should be backtested at all (later resolved via *joint* elicitability of the (VaR, CVaR) pair by Fissler & Ziggel and Acerbi & Szekely, outside this paper). For forecast *competitions* across heterogeneous series (M-competitions), comparability of scores across differing magnitude/volatility is left controversial, and skill scores / MASE-type ratios complicate expectation-optimizing behavior. Empirical and theoretical follow-up on the relative power of consistent scores (e.g. QLIKE vs SE in Diebold–Mariano tests) is invited.

## Connections
The decision-theoretic backdrop draws on [[@Savage1971|Savage (1971)]] and Osband (1985), with the term *elicitability* from [[@Lambert2008|Lambert, Pennock & Shoham (2008)]]. The proper-scoring-rule strand it disentangles is the subject of [[@Gneiting2007|Gneiting & Raftery (2007)]], with Dawid (2007), DeGroot & Fienberg (1983), Schervish (1989), Winkler (1996) and Buja, Stuetzle & Shen (2005) on binary-event scores. The motivating concern that forecasters report unspecified functionals is from Engelberg, Manski & Williams (2009) and Murphy & Daan (1985). Quantile elicitation links to Thomson (1979), Giacomini & Komunjer (2005) and Gneiting (2011, "Quantiles as Optimal Point Forecasts"); the volatility application connects to Patton (2011) and Patton & Sheppard (2009) via QLIKE, and asymmetric-loss prediction to Christoffersen & Diebold (1996) and Zellner (1986). The CVaR non-elicitability result speaks to the risk-measure literature of Artzner et al. (1999) and Acerbi (2002). Predictive-ability testing uses Diebold & Mariano (1995) and West (1996). For research-vault purposes this is the canonical reference linking proper scoring rules, belief elicitation and the design of loss functions for evaluating predictive models.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
