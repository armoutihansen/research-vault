---
citekey: DeJarnette2020
title: Time Lotteries and Stochastic Impatience
authors: ["DeJarnette, Patrick", "Dillenberger, David", "Gottlieb, Daniel", "Ortoleva, Pietro"]
year: 2020
type: journalArticle
doi: 10.3982/ECTA16427
zotero: "zotero://select/library/items/4RF4FGEL"
pdf: /Users/jesper/Zotero/storage/ZYIXYH8W/DeJarnette2020.pdf
tags: [literature]
keywords: [time-lotteries, stochastic-impatience, expected-discounted-utility, risk-and-time-preferences, non-expected-utility, intertemporal-choice]
topics: []
related: [Chen2013, Gul1991, Quiggin1982, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We study preferences over lotteries in which both the prize and the payment date are uncertain. In particular, a time lottery is one in which the prize is fixed but the date is random. With Expected Discounted Utility, individuals must be risk seeking over time lotteries (RSTL). In an incentivized experiment, however, we find that almost all subjects violate this property. Our main contributions are theoretical. We first show that within a very broad class of models, which includes many forms of nonexpected utility and time discounting, it is impossible to accommodate even a single violation of RSTL without also violating a property we termed Stochastic Impatience, a risky counterpart of standard Impatience. We then present two positive results. If one wishes to maintain Stochastic Impatience, violations of RSTL can be accommodated by keeping Independence within periods while relaxing it across periods. If, instead, one is willing to forego Stochastic Impatience, violations of RSTL can be accommodated with a simple generalization of Expected Discounted Utility, obtained by imposing only the behavioral postulates of Discounted Utility and Expected Utility.

## Summary
A *time lottery* fixes the prize but randomizes the payment date. Expected Discounted Utility (EDU) forces everyone to be Risk Seeking over Time Lotteries (RSTL) because the discount function $\beta^t$ is convex in $t$, so by Jensen a mean-preserving spread of the payment date is always preferred — independently of the curvature of utility over money. The paper shows experimentally that almost no one is consistently RSTL (most subjects are Risk Averse over Time Lotteries, RATL), then proves an impossibility result: within a very broad class of risk-and-time models, even a *single* RATL violation is incompatible with a new axiom, Stochastic Impatience. Finally it offers two escape routes — relax Independence across (but not within) periods, or drop Stochastic Impatience and obtain a one-parameter generalization of EDU (GEDU).

## Research question
What are individuals' intrinsic attitudes toward uncertainty in *when* (not just which) outcome is received? Does the standard model (EDU) capture them, and if not, how can risk-over-timing be modeled while preserving other desirable properties of risk and time preferences?

## Method / identification
The primitive is a complete, transitive preference $\succeq$ over the set $\Delta$ of simple lotteries over dated rewards $(x,t)\in[w,b]\times T$, with all uncertainty resolved immediately (static, no planning motive). EDU evaluates $V(p)=E_p[\beta^t u(x)]$; more generally $V(p)=E_p[D(t)u(x)]$ with $D$ strictly decreasing. **RATL/RSTL** (Definition 1) compare a sure date $\delta_{(x,\bar t)}$ against a time lottery $p_x$ with the same mean date. Convexity of $D$ is equivalent to RSTL, and all standard discount functions (exponential, hyperbolic, quasi-hyperbolic) are convex.

The new axiom is **Stochastic Impatience** (Definition 2): for $t_1<t_2$, $x_1>x_2$, $\tfrac12\delta_{(x_1,t_1)}+\tfrac12\delta_{(x_2,t_2)}\succeq\tfrac12\delta_{(x_1,t_2)}+\tfrac12\delta_{(x_2,t_1)}$ — pair the higher prize with the earlier date. Under Expected Utility this is exactly *decreasing differences* of $U$: $U(x_1,t_1)-U(x_1,t_2)\geq U(x_2,t_1)-U(x_2,t_2)$, i.e. prizes and waiting time are substitutes.

Basic axioms: Outcome Monotonicity, Impatience, and **No Future Bias** (the marginal rate of substitution between money and time is non-increasing in time — weaker than Stationarity, allows present but not future bias). Two model classes are used: (i) Expected Utility (adding Independence + Continuity), and (ii) **Generalized Local Bilinear Utility (GLBU)**, which restricts only 50/50 lotteries — $V=\pi(\tfrac12)U(x,t)+(1-\pi(\tfrac12))U(x',t')$ for the better outcome weighted $\pi(\tfrac12)$ — subsuming Rank-Dependent Utility, Cumulative Prospect Theory, and Disappointment Aversion.

The empirical method is an incentivized lab experiment (196 Wharton subjects), with Part I forced choices between time lotteries (mean-preserving spreads of payment dates) and Parts II–III using Multiple Price Lists to elicit time preferences, attitudes toward time lotteries, and atemporal risk preferences, including Allais common-ratio items. Two treatments vary the maximum delay (Long = 12 weeks, Short = 5 weeks).

## Data
Original incentivized experiment: 196 subjects at the Wharton Behavioral Lab, one randomly-selected question paid; plus a real-effort-task robustness experiment (Appendix D.4). Monetary stakes on the order of $15. This is novel data — prior literature used only unincentivized hypothetical surveys.

## Key findings
- **Pervasive RATL.** Only 2.86% (Long) / 9.89% (Short) of subjects are consistently RSTL; the majority choose RATL in the majority of questions, including the clean first question (RATL share significantly > 50%, exact binomial $p=0.002$). The pattern is incompatible not only with EDU but also with symmetric-error stochastic extensions of EDU (cross-treatment comparison gives the *opposite* of the EDU prediction, Fisher $p=0.003$).
- **RATL correlates with atemporal risk aversion** but is essentially uncorrelated with convexity of discounting or certainty bias — a connection EDU cannot deliver. 82% display convex discounting; ~40% are approximately EU over atemporal lotteries.
- **Theorem 1 (impossibility under EU).** Under Axioms 1–5, Stochastic Impatience implies RSTL — no single RATL violation is possible. Intuition: No Future Bias makes the MRS $\partial_t U/\partial_x U$ decreasing while Stochastic Impatience makes $\partial^2 U/\partial x\partial t\leq0$, forcing $\partial^2 U/\partial t^2\geq0$, which is RSTL.
- **Theorem 2 (impossibility beyond EU).** Any GLBU representation with an RATL instance ($\delta_{(x,t_2)}\succ\tfrac12\delta_{(x,t_1)}+\tfrac12\delta_{(x,t_3)}$, $t_2=\tfrac{t_1+t_3}2$) violates Stochastic Impatience. So probability distortions (RDU, CPT, DA) do not help.
- **Solution 1 — relax intertemporal Independence.** Imposing Independence only *within* each period (not across) breaks the link. The Dynamic Ordinal Certainty Equivalent (DOCE) model $V(p)=\sum_t \beta^t u\big(v^{-1}(\sum_x \hat p(x,t)v(x))\big)$ always satisfies Stochastic Impatience yet permits RATL when $v$ is sufficiently concave. This corresponds to aggregating risk first (per-period certainty equivalents) and time second.
- **Solution 2 — GEDU (Proposition 1).** Combining the axioms for exponential discounting (Stationarity) with those for Expected Utility yields not EDU but $V(p)=E_p[\varphi(\beta^t u(x))]$ with $\varphi$ strictly increasing — an extra curvature applied after discounting. EDU is the special case $\varphi$ affine. Here intertemporal substitution is governed by $u,\beta$ and atemporal risk by $\varphi\circ u$.
- **Proposition 2.** Under GEDU, $\succeq$ is RSTL / RNTL / RATL iff $\varphi$ is a convex / affine / concave transformation of $\ln$. More concave $\varphi$ implies *both* more atemporal risk aversion and more aversion to time lotteries — matching the experimental correlation.
- **Proposition 3.** Within GEDU on an interval $T$, adding Risk Stationarity, EDU is characterized exactly by strict RSTL.
- **Proposition 4.** Under GEDU, Stochastic Impatience and RSTL are equivalent.

## Contribution
Introduces two clean behavioral notions — risk attitude toward time lotteries (RATL/RSTL) and Stochastic Impatience — and provides the first incentivized evidence that the EDU-mandated RSTL is systematically violated. The central conceptual point, echoing Yaari (1987), is that EDU illegitimately ties a *deterministic* property (convex discounting) to a *stochastic* one (RSTL): it is not innocuous to reuse risk-free parameters under risk. The impossibility results are sharp and general (one violation suffices; they cover non-EU and non-exponential discounting), and the two constructive solutions (intertemporal-Independence relaxation; GEDU) give tractable modeling alternatives, with GEDU nesting Kihlstrom–Mirman-type multi-attribute utility applied to time.

## Limitations & open questions
- The framework analyzes *static* preferences with immediate resolution, deliberately excluding planning value and preferences over the timing of resolution of uncertainty — incorporating these instrumental/intrinsic distinctions is left open.
- GEDU extended to consumption *streams*, $\varphi(\sum_t \beta^t u(x_t))$, is **not dynamically consistent** unless it collapses to EDU; the dynamically-consistent Epstein–Zin (1989) alternative still sacrifices Stochastic Impatience whenever it permits RATL.
- A 'Negative-EDU' variant ($\beta>1$, negative $u$) reconciles RATL with Risk Stationarity but does not carry over to streams.
- The DOCE example is presented purely for illustration; assessing the normative/descriptive appeal of within-period-Independence models (which violate dynamic consistency and stochastic monotonicity) is left for future work.
- Which axiom one *should* give up (intertemporal Independence vs. Stochastic Impatience) is left to subjective judgment — no resolution is offered.

## Connections
Builds directly on Expected Discounted Utility and the Discounted Utility representation of Fishburn & Rubinstein (1982); the separability argument for Independence traces to Samuelson (1952). The decoupling logic — that a deterministic-curvature property need not govern a stochastic one — is explicitly framed as the temporal analogue of Yaari (1987). The GEDU form applies the multi-attribute utility of Kihlstrom & Mirman (1974) to time, and is related to Andersen et al. (2017), Abdellaoui et al. (2017), Edmans & Gabaix (2011), and Garrett & Pavan (2011). The within-period-Independence (DOCE) route draws on Selden (1978), Selden & Stux (1978), and Selden & Wei (2019); Epstein & Zin (1989), Chew & Epstein (1990), and Bommier et al. (2017) supply the dynamically-consistent recursive alternative, and the companion Dillenberger et al. (2018) links Stochastic Impatience to models separating risk and time. The GLBU umbrella nests [[@Quiggin1982|Quiggin (1982)]], [[@Tversky1992|Tversky & Kahneman (1992)]], [[@Gul1991|Gul (1991)]], Dean & Ortoleva (2017), and the biseparable model of Ghirardato & Marinacci (2001), while Cerreia-Vioglio et al. (2015) lies outside it. Prior time-lottery work includes Chesson & Viscusi (2003), Onay & Öncüler (2007), [[@Chen2013|Chen (2013)]], and Ebert (2017); Kacelnik & Bateson (1996) document RSTL in animal foraging and Eliaz & Ortoleva (2016) study ambiguous timing. On stochastic-choice concerns for risk/time elicitation the paper engages Luce (1958), McFadden (2005), Apesteguia & Ballester (2018), and Apesteguia et al. (2017); applications relying on RSTL include Ely & Szydlowski (2017) and Zhong (2019). The magnitude-effect flexibility connects to Noor (2011).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
