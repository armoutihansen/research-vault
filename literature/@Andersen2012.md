---
citekey: Andersen2012
title: Non-linear mixed logit
authors: ["Andersen, Steffen", "Harrison, Glenn W.", "Hole, Arne Risa", "Lau, Morten", "Rutström, E. Elisabet"]
year: 2012
type: journalArticle
doi: 10.1007/s11238-011-9277-0
zotero: "zotero://select/library/items/XRF4F67F"
pdf: /Users/jesper/Zotero/storage/S5Q7L257/Andersen2012.pdf
tags: [literature]
keywords: [mixed-logit, structural-estimation, risk-attitudes, discounting, maximum-simulated-likelihood, behavioral-econometrics, random-coefficients]
topics: []
related: [Hole2007, McFadden2000, Revelt1998]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We develop an extension of the familiar linear mixed logit model to allow for the direct estimation of parametric non-linear functions defined over structural parameters. Classic applications include the estimation of coefficients of utility functions to characterize risk attitudes and discounting functions to characterize impatience. There are several unexpected benefits of this extension, apart from the ability to directly estimate structural parameters of theoretical interest.

## Summary
The paper extends the standard linear mixed logit (random-coefficients logit) by replacing the linear latent index with an arbitrary parametric non-linear function $G(\beta_n, x_{njt})$ defined over the "deep" structural parameters of a behavioral theory. This lets the analyst estimate quantities of direct theoretical interest, such as a CRRA risk-aversion coefficient or an exponential discount rate, together with their population heterogeneity, rather than recovering only a reduced-form linear proxy. Estimation is by maximum simulated likelihood (MSL) with Halton draws. Two extra payoffs follow: flexible bounded population distributions (the Logit-Normal and its "Beta4" generalization) come essentially "for free," and demographic covariates that are invariant across alternatives can affect choice without being mechanically interacted with task attributes.

## Research question
Why and how should one estimate the structural ("deep") parameters of a non-linear decision theory directly within a mixed logit framework, instead of relying on a linear mixed logit specification whose coefficients only encode those parameters indirectly under restrictive functional-form assumptions?

## Method / identification
The core object is a random utility / latent index for subject $n$ choosing alternative $j$ in task $t$. The standard linear mixed logit posits
$$U_{njt} = \beta_n x_{njt} + \varepsilon_{njt}$$
with $\varepsilon_{njt}$ i.i.d. type-I extreme value. The authors generalize the deterministic part to a non-linear function:
$$U_{njt} = G(\beta_n, x_{njt}) + \varepsilon_{njt}.$$
For risk attitudes under expected utility theory (EUT) with a CRRA utility $U(m_k) = m_k^{r}$, the index is set to expected utility $G(r_n, m_{njt}, p_{njt}) = EU_j = \sum_k [p_k \, U(m_k)]$. Individual coefficients follow a population density $f(\beta\mid\theta)$ with hyper-parameters $\theta$ (e.g. mean and standard deviation of a Normal). Conditional on $\beta_n$, choice probabilities take the conditional logit form
$$L_{nit}(\beta_n) = \frac{\exp\{G(\beta_n, x_{nit})\}}{\sum_j \exp\{G(\beta_n, x_{njt})\}},$$
the probability of a subject's full sequence of choices is $P_n(\beta_n) = \prod_t L_{ni(n,t)t}(\beta_n)$, and the unconditional likelihood integrates out heterogeneity, $P_n(\theta) = \int P_n(\beta_n) f(\beta\mid\theta)\, d\beta$. Because this integral has no closed form, the log-likelihood $LL(\theta) = \sum_n \ln P_n(\theta)$ is approximated by simulation, drawing $H$ replications $\beta^h$ and averaging: $SLL(\theta) = \sum_n \ln\!\big(\frac{1}{H}\sum_h P_n(\beta^h)\big)$. The authors use $H = 250$ Halton draws and build on [[@Hole2007|Hole's (2007)]] Stata linear mixed logit code. A Fechner behavioral-error term $\mu>0$ scales the EU difference before the logistic link, entering $G$ as $EU_j/\mu$ and itself treated as a (possibly random) coefficient. For flexible bounded heterogeneity they use the Logit-Normal distribution (Johnson 1949) and a four-parameter "Beta4" version that shifts and stretches it to respect theoretical bounds (e.g. $r>0$ for monotonicity). An appendix formally shows that under the non-linear index, alternative-invariant demographics $z_n$ do not cancel in the choice inequality (whereas they do in the linear case), so sex etc. can enter structurally without manual interactions.

## Data
Two laboratory/field experimental datasets. (1) Risk-attitude application: $N=63$ subjects, $T=60$ choices over $J=2$ lottery pairs, each lottery with up to $K=4$ outcomes over prizes $\{\$0,\$5,\$10,\$15\}$ with probabilities in 1/8 increments ("pie display"); three of 60 choices paid at random. (2) Joint risk-and-time application: $N=253$ Danish subjects (data from Andersen et al. 2008) making choices over immediate and delayed monetary amounts (initial delay 30 days), with a paired design that separately identifies risk attitudes and discount rates. Background daily consumption is fixed exogenously at $\omega = 118$ DKK.

## Key findings
- The MSL non-linear mixed logit recovers structural parameters directly. In the risk application, constraining $r_{sd}=0$ exactly reproduces ordinary ML ($r_{mean}=0.468$, the "representative agent"); allowing unobserved heterogeneity yields a statistically significant population standard deviation ($r_{mean}\approx 0.40$, $r_{sd}\approx 0.35$), and the heterogeneity term improves the log-likelihood more than adding the single sex covariate.
- Women are estimated to be more risk averse on average and to display greater variability in risk attitudes than men; crucially, sex enters the structural parameter without being interacted with task attributes.
- Under a Normal population distribution, part of the mass of $r$ falls below zero, violating local non-satiation in the tails; the bounded Beta4 distribution truncates this lower tail at 0 and is statistically rejected as Normal (D'Agostino et al. 1990 tests), illustrating that flexible bounded distributions "get the economics right."
- In the joint risk-time model, errors in estimating the utility curvature $r$ propagate to inference on the discount rate $\delta$ via full-information ML of the combined likelihood $\ln L = \ln L_{RA} + \ln L_{DR}$. The estimated $r$-$\delta$ covariance is significantly negative (correlation $\approx -0.13$), consistent with Jensen's inequality (more concave utility implies lower inferred $\delta$). The discount-rate population distribution is right-skewed (mean $\delta\approx 0.097$, median $0.080$), demonstrably non-Normal under the Logit-Normal transform.

## Contribution
A unified, computationally tractable framework (and accompanying Stata software generalizing [[@Hole2007|Hole 2007)]] for estimating the deep structural parameters of non-linear behavioral theories within mixed logit, jointly with their population heterogeneity. It clarifies that McFadden-Train approximation theorems (any random utility model can be approximated by a linear mixed logit) run only one way: they guarantee an equivalent linear model but do not let one recover the deep parameters, which require either restrictive linearizing assumptions or this explicit non-linear specification. The Logit-Normal/Beta4 device delivers bimodal, skewed, and theory-bounded population distributions at no extra parameter cost, and the appendix gives a clean rationale for including alternative-invariant demographics structurally.

## Limitations & open questions
- The Logit-Normal/Beta approximation is natively defined on the unit interval; extending bounded flexible distributions to general supports beyond simple transforms (log-Normal for non-negativity, Beta4 for finite intervals) is acknowledged as not fully general.
- The Normal population assumption produces theoretically nonsensical tails (non-satiation violations); the authors note one "could use our approach to generate nested hypothesis tests" of non-satiation, but do not carry this out.
- Parametric assumptions on $G(\cdot)$ "should remain untested" — the authors explicitly leave testing of the imposed functional forms (and reconciling with semi/non-parametric alternatives) as an open agenda, promising to "swim with the tide" of agnostic estimators once those can tractably deliver structural estimates.
- MSL practicalities (choice of draw scheme, the size of $H$ "practically needed") and the suspect identifying assumptions behind the linear-approximation theorems (random-effects-style orthogonality of unobservables to observables; reliance on polynomial approximations) are flagged as concerns but not resolved.

## Connections
The work sits squarely in the structural behavioral econometrics tradition of Harrison and Rutström (2008) and the companion Andersen, Harrison, Lau, and Rutström (2008, Econometrica) on jointly eliciting risk and time preferences, of which the discounting application is a simplified ("dual-self" removed) re-estimation. It builds technically on Train's (2003) and Cameron and Trivedi's (2005) treatments of mixed logit and MSL, the repeated-choice mixed logit of [[@Revelt1998|Revelt and Train (1998)]], and Hole's (2007) Stata implementation; the approximation theorems it qualifies are [[@McFadden2000|McFadden and Train (2000)]]. The Fechner stochastic-choice structure follows Hey and Orme (1994) and Wilcox (2008). Section 5 positions the approach against the distribution-free / non-parametric binary-choice literature — Gallant (1981) flexible functional forms (applied to binary choice by Chen and Randall 1997) and Matzkin's (1991, 1992) non-parametric monotone-concave utility estimation — arguing for explicit parametric structure when the deep parameters are themselves the inferential target. The Logit-Normal distribution derives from Johnson (1949), with antecedents in Mead (1965), Aitchison and Begg (1976), and Lesaffre et al. (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
