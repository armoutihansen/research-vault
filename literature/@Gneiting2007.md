---
citekey: Gneiting2007
title: "Strictly Proper Scoring Rules, Prediction, and Estimation"
authors: ["Gneiting, Tilmann", "Raftery, Adrian E"]
year: 2007
type: journalArticle
doi: 10.1198/016214506000001437
zotero: "zotero://select/library/items/6IU7VX6T"
pdf: "/Users/jesper/Zotero/storage/QN3ZWAT5/Gneiting and Raftery - 2007 - Strictly Proper Scoring Rules, Prediction, and Estimation.pdf"
tags: [literature]
keywords: [proper-scoring-rules, belief-elicitation, probabilistic-forecasting, crps-energy-score, bregman-divergence, optimum-score-estimation, quantile-interval-forecasts]
topics: []
related: [Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Scoring rules assess the quality of probabilistic forecasts, by assigning a numerical score based on the predictive distribution and on the event or value that materializes. A scoring rule is proper if the forecaster maximizes the expected score for an observation drawn from the distribution $F$ if he or she issues the probabilistic forecast $F$, rather than $G \neq F$. It is strictly proper if the maximum is unique. In prediction problems, proper scoring rules encourage the forecaster to make careful assessments and to be honest. In estimation problems, strictly proper scoring rules provide attractive loss and utility functions that can be tailored to the problem at hand. This article reviews and develops the theory of proper scoring rules on general probability spaces, and proposes and discusses examples thereof. Proper scoring rules derive from convex functions and relate to information measures, entropy functions, and Bregman divergences. In the case of categorical variables, we prove a rigorous version of the Savage representation. Examples of scoring rules for probabilistic forecasts in the form of predictive densities include the logarithmic, spherical, pseudospherical, and quadratic scores. The continuous ranked probability score applies to probabilistic forecasts that take the form of predictive cumulative distribution functions. It generalizes the absolute error and forms a special case of a new and very general type of score, the energy score. Like many other scoring rules, the energy score admits a kernel representation in terms of negative definite functions, with links to inequalities of Hoeffding type, in both univariate and multivariate settings. Proper scoring rules for quantile and interval forecasts are also discussed. We relate proper scoring rules to Bayes factors and to cross-validation, and propose a novel form of cross-validation known as random-fold cross-validation. A case study on probabilistic weather forecasts in the North American Pacific Northwest illustrates the importance of propriety. We note optimum score approaches to point and quantile estimation, and propose the intuitively appealing interval score as a utility function in interval estimation that addresses width as well as coverage.

## Summary

This is the canonical reference and review article on **proper scoring rules** — positively oriented rewards $S(P,x)$ paid to a forecaster who quotes the predictive distribution $P$ when outcome $x$ materializes. The paper synthesizes a scattered literature into a unified theory on general probability spaces, develops the link between propriety and convex analysis, catalogues the standard scores (logarithmic, quadratic/Brier, spherical, CRPS), introduces the **energy score** and the broader **kernel score** family, treats quantile/interval forecasts, and closes with **optimum score estimation** — a general estimation paradigm of which maximum likelihood is the special case driven by the logarithmic score. Coverage is full (21-page journal article, all 10 sections plus appendix represented).

## Research question

How can the quality of *probabilistic* forecasts — predictive distributions rather than point forecasts — be evaluated by a single number in a way that (a) gives the honest forecaster no incentive to misreport, and (b) connects to a usable theory for estimation? The paper asks which functionals $S(P,x)$ are proper, characterizes them exhaustively, and asks how propriety bears on prediction, elicitation, and estimation.

## Method / identification

Theory paper. The central object is the expected score $S(P,Q)=\int S(P,\omega)\,dQ(\omega)$. $S$ is **proper** relative to a convex class $\mathcal{P}$ if $S(Q,Q)\succeq S(P,Q)$ for all $P,Q\in\mathcal{P}$ (i.e. $S(Q,Q)\geq S(P,Q)$), and **strictly proper** if equality holds only at $P=Q$.

The unifying result (Theorem 1) ties propriety to convexity: a regular scoring rule is proper iff its expected-score function $G(P)=S(P,P)=\sup_{Q}S(Q,P)$ is convex and $S(P,\cdot)$ is a subtangent of $G$ at $P$, giving the representation
$$S(P,\omega)=G(P)-\int G^{*}(P,\omega)\,dP(\omega)+G^{*}(P,\omega).$$
$G$ is the **generalized entropy / information measure**; the **divergence** $d(P,Q)=S(Q,Q)-S(P,Q)$ is the associated Bregman divergence. For categorical outcomes this specializes to the **Savage representation** (Theorem 2), $S(p,i)=G(p)-\langle G'(p),p\rangle+G_i(p)$, of which Brier, spherical, logarithmic, and zero-one scores are convex-function instances. For binary events, Schervish's representation (Theorem 3) writes any proper score as a Choquet mixture of cost-weighted asymmetric zero-one scores over a measure $\nu(dc)$ on cost-loss ratios.

For continuous outcomes, the **kernel-score** construction (Theorem 4) shows that any nonnegative continuous *negative definite* kernel $g$ yields a proper score $S(P,x)=\tfrac{1}{2}E_P g(X,X')-E_P g(X,x)$; Theorems 5 generalizes via completely monotone functions. Propriety is equivalent to a **Hoeffding-type inequality** $2E_{P,Q}g(X,Y)-E_P g(X,X')-E_Q g(Y,Y')\geq 0$.

For estimation (Sec. 9): the **optimum score estimator** is $\hat{\theta}_n=\arg\max_\theta \frac{1}{n}\sum_i S(P_\theta,X_i)$, consistent because strict propriety implies $\arg\max_\theta S_n(\theta)\to\theta_0$. This is minimum-contrast estimation (Pfanzagl; Birgé–Massart) and a special case of M-estimation; MLE is the logarithmic-score instance.

## Data

Primarily a theory paper. Two illustrative empirical exercises: (1) a 100,001-step simulated stationary bilinear (conditionally heteroscedastic) process comparing three 95% interval forecasts; (2) a **case study** on 16,015 records of 48-hour-ahead sea-level-pressure ensemble forecasts over the North American Pacific Northwest (Jan–Jun 2000, University of Washington 5-member MM5 ensemble), used to score Gaussian density forecasts as a function of an inflation factor $r$.

## Key findings

- **Theorem 1**: propriety $\Leftrightarrow$ convex expected-score function with the score as subtangent; the Savage representation (Theorem 2) is its rigorous categorical form, Schervish's Choquet mixture (Theorem 3) its binary form.
- Standard density scores are strictly proper: the **logarithmic** $\mathrm{LogS}(p,\omega)=\log p(\omega)$ (the *only* proper local score, by Bernardo), **quadratic**, and **pseudospherical/spherical**. The intuitive **linear score** $p(\omega)$ and Wilson's **probability score** are *improper*.
- The **CRPS**, $\mathrm{CRPS}(F,x)=-\int(F(y)-\mathbf{1}\{y\geq x\})^2\,dy=\tfrac{1}{2}E_F|X-X'|-E_F|X-x|$, is strictly proper, generalizes absolute error, and has closed forms for Gaussian and (in $O(n\log n)$) sample-based $F$. The **energy score** $\mathrm{ES}(P,x)=\tfrac{1}{2}E_P\|X-X'\|^\beta-E_P\|X-x\|^\beta$, $\beta\in(0,2)$, extends it to multivariate forecasts and is one member of the kernel-score family.
- **Skill scores** $(S^{fcst}-S^{ref})/(S^{opt}-S^{ref})$ are generally *improper* even from proper $S$ (Murphy's Brier skill score is only asymptotically proper).
- The quantile score $S(r;x)=(x-r)(\mathbf{1}\{x\leq r\}-\alpha)$ (econometric **tick/check loss**) is proper; the proper-quantile class is strictly larger than Cervera–Muñoz conjectured. The **interval score** $S^{int}_\alpha(l,u;x)=(u-l)+\tfrac{2}{\alpha}(l-x)\mathbf{1}\{x<l\}+\tfrac{2}{\alpha}(x-u)\mathbf{1}\{x>u\}$ jointly rewards sharpness and penalizes coverage misses.
- **Estimation**: optimum score estimation generalizes MLE; the no-parameter log Bayes factor equals the difference in logarithmic scores, motivating **random-fold cross-validation**.
- **Empirically**: the proper scores all maximized at inflation $r>1$, correctly diagnosing the underdispersive ensemble near $r_0=1.55$; the improper linear and probability scores maximized near $r\approx 0$, falsely implying deterministic forecasts — the headline cautionary result.

## Contribution

Provides the first unified, measure-theoretically rigorous treatment of proper scoring rules on general spaces; proves a rigorous Savage representation; introduces the energy score and the kernel-score class with their negative-definite-function / Hoeffding-inequality backbone; frames optimum score estimation as a generalization of MLE and M-estimation; and supplies a vivid demonstration that improper scores yield misleading scientific inferences. It became the standard citation for forecast evaluation and elicitation across statistics, meteorology, econometrics, and machine learning.

## Limitations & open questions

The authors explicitly flag (Sec. 10) that: the relationship between proper scoring rules and divergence functions is **not fully understood**; the characterization of proper scoring rules **for quantiles remains open** (they do not know whether their forms (40)/(42) are the general form); the propriety of **skill scores** needs follow-up despite Murphy's work; tailoring scores to asymmetric cost structures (false positives vs. negatives) beyond binary class-probability estimation is unresolved; and the connection between cross-validatory and likelihood-based model selection (BIC, AIC, DIC, Bayes factors) under general proper scores — including the conjectured asymptotic equivalences for random-fold cross-validation — is unproven. Selection guidelines for *which* proper rule to use are "in strong demand."

## Connections

The convex-analysis backbone draws on [[@Savage1971|Savage (1971)]], Schervish (1989), and Hendrickson & Buehler (1971), with the decision-theoretic and geometric framing from Dawid (1998, 2006) and Grünwald & Dawid (2004). The Brier score originates with Brier (1950), the logarithmic score with Good (1952); Buja, Stuetzle & Shen (2005) supply the beta family and the tailoring argument. The energy/kernel apparatus rests on Székely (2003), Székely & Rizzo (2005), Baringhaus & Franz (2004), and negative-definite-function theory (Berg, Christensen & Ressel 1984). The estimation thread connects to minimum-contrast estimation (Pfanzagl 1969; Birgé & Massart 1993), M-estimation and robust statistics (Huber 1964, 1967), and Bayes factors / BIC (Kass & Raftery 1995; Schwarz 1978). The tick/check loss links it directly to econometric quantile forecasting (Koenker & Bassett 1978; Giacomini & Komunjer 2005). This paper is the foundational reference for honest belief elicitation and for evaluating probabilistic predictions, dovetailing with Bayesian utility (Bernardo & Smith 1994) and downstream machine-learning use of Bregman divergences (Collins, Schapire & Singer 2002).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
