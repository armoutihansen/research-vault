---
citekey: Loewenstein1987
title: Anticipation and the Valuation of Delayed Consumption
authors: ["Loewenstein, George"]
year: 1987
type: journalArticle
doi: 10.2307/2232929
zotero: "zotero://select/library/items/BRBT4HDG"
pdf: /Users/jesper/Zotero/storage/TLI3EQG9/Loewenstein1987.pdf
tags: [literature]
keywords: [intertemporal-choice, anticipation, savouring-and-dread, discounted-utility, time-inconsistency, negative-discounting, behavioral-economics]
topics: ["[[anticipatory-utility-motivated-beliefs]]"]
related: [Caplin2001]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Loewenstein extends the Discounted Utility (DU) model by recognising that anticipation of future consumption is itself an immediate source of utility ("savouring" for pleasant outcomes, "dread" for unpleasant ones). Because waiting yields a flow of anticipal pleasure or pain, the value of a delayed outcome need not decline monotonically with delay: people may prefer to *defer* fleeting, vividly imaginable pleasures and to *accelerate* fleeting, vivid pains, contradicting positive-discounting DU. The model reproduces hump-shaped time profiles of value, explains downward bias in estimated discount rates, and rationalises violations of the intertemporal independence axiom and a novel "reverse time inconsistency."

## Research question
Why do people sometimes exhibit negative or non-monotonic time discounting -- deferring pleasant outcomes (a kiss, a vacation, fine wine) and hastening unpleasant ones (a shock, a dental visit) -- in violation of the standard assumption of positive time preference embedded in DU? Can a single modification of DU accommodate both myopic and far-sighted intertemporal behaviour?

## Method / identification
A continuous-time deterministic model of valuing a *single* future act of consumption under certainty. A consumer at time $t_0$ anticipates consuming $x$ at time $T \ge t_0$; consumption yields a constant utility flow $U(x)$ over an interval of duration $L$, i.e. $U_t(x,T,L)=U(x)$ for $T \le t \le T+L$ and zero otherwise. Before consumption begins, the agent derives anticipation utility proportional to the discounted integral of future consumption utility:
$$U_t^A(x,T,L)=\alpha\,U(x)\,e^{-\delta(T-t)}\,(1-e^{-\delta L}),$$
where $\delta$ measures preoccupation with the future (low $\delta$ = savouring distant outcomes) and $\alpha$ measures the "vividness"/imaginability of the outcome. The present dollar value $Y$ of delayed consumption solves $U(Y)$ equal to the discounted integral of anticipation utility plus consumption utility, both discounted at the *conventional* rate $r>0$. Setting $t_0=0$ and integrating:
$$U(Y)=U(x)\!\left[\frac{\alpha}{\delta-r}\,(e^{-rT}-e^{-\delta T})(1-e^{-\delta L})+\tfrac{1}{r}e^{-rT}(1-e^{-rL})\right].$$
It is assumed $\delta > r$. Comparative statics are obtained by differentiating $U(Y)$ with respect to $T$ (locating the optimal consumption time $T_m$ for desired outcomes and the indifference threshold $T_i$ for undesired ones) and totally differentiating to sign $\partial T_m/\partial L$, $\partial T_m/\partial \alpha$, etc. (Appendices 2-5). The theory is illustrated with three small survey studies of undergraduates, not used for structural estimation.

## Data
Illustrative survey evidence only (no econometric estimation). (1) 30 undergraduates stated maximum willingness-to-pay to obtain/avoid five outcomes (gain/lose \$4, avoid losing \$1000, avoid a 110-volt shock, a kiss from a movie star) at delays from immediate to 10 years; the kiss showed hump-shaped valuation and the shock showed increasing avoidance value with delay, while money was discounted conventionally. (2) A "hamster-cage cleaning" reservation-wage question (37 respondents): mean required immediate payment rose from \$30 (next week) to \$37 (one year out). (3) 37 undergraduates faced paired restaurant-dinner sequences demonstrating an independence violation (84% chose to delay a fancy dinner; 57% reversed when a common later lobster dinner was appended).

## Key findings
- **Optimal deferral of desired consumption.** Consumption is deferred ($T_m>t_0$) iff $\alpha(1-e^{-\delta L}) > 1-e^{-rL}$ (condition 8). Deferral is more likely for large $\alpha$ (vivid/savourable) and small $\delta$.
- **Fleetingness promotes deferral/acceleration.** $\partial T_m/\partial L \le 0$: shorter-duration ("fleeting") pleasures are deferred; longer ones are consumed sooner. Symmetrically, fleeting, vivid pains are gotten over with quickly ($T_i>t_0$); prolonged/permanent harms are deferred.
- **Devaluing vs. discounting.** The paper distinguishes "discounting" (preference for early utility, governed by $r$) from "devaluing" (the net change in an outcome's present value with delay). Devaluing can be initially negative even though $r>0$, producing a reversed-S value profile rather than DU's convex decay.
- **Downward bias in estimated discount rates.** Because savouring/dread attenuate devaluing -- most strongly at short/moderate horizons and for fleeting or vivid goods -- conventional DU estimates of discount rates are biased downward and are category-specific, invalidating Landsberger's assumption of a consumption-independent discount rate and undermining Hausman's air-conditioner imputations.
- **Reverse time inconsistency.** An agent who defers to savour faces the same incentive again at $T_m$, suggesting infinite deferral; self-credibility, enforcement/reinforcement mechanisms, and side-bets typically halt it, but the phenomenon is observed (hoarded Hallowe'en candy, perpetually deferred vacations, misers).
- **Independence violations.** Appending a common later outcome changes preference over earlier sub-streams, because anticipal pleasure of the later good raises the marginal utility of earlier consumption -- a rationale absent from axiomatic DU (Koopmans 1960; Meyer 1976).

## Contribution
Provides the first formal economic model in which anticipation enters utility, reviving the Benthamite/Jevonsian notion of "anticipal pleasure and pain" and Marshallian "vividness." It yields a unified account of both negative discounting and standard impatience, predicts hump-shaped/reversed-S valuation profiles, explains anomalous post-retirement saving (wealth as a "licence to savour"; goal-based saving; misers), and supplies behavioural micro-foundations for later work on anticipation, savouring/dread, and reference-dependent intertemporal choice.

## Limitations & open questions
- The core model treats only a *single* act of consumption under *certainty*; generalisation to complex consumption streams is sketched only informally (footnote: $\max\int V(U_t^C+U_t^A)\,e^{-rt}\,dt$ with $V'>0,\,V''<0$).
- $\alpha$ (vividness) is acknowledged as *not directly observable*, complicating identification and estimation.
- The effect of $\delta$ on $T_m$ is *ambiguous* in sign.
- The empirical evidence is hypothetical-survey-based with small undergraduate samples; the shock results are hard to generalise to naturalistic economic settings.
- Reverse time inconsistency lacks a complete equilibrium treatment of when self-credibility actually binds versus permits indefinite deferral.

## Connections
Directly modifies the Discounted Utility model of Koopmans (1960) and Samuelson, and engages Strotz (1956) on myopia and time inconsistency, proposing the mirror-image "reverse time inconsistency." It builds on classical sources -- Bentham (1789), Jevons (1905), Bohm-Bawerk (1889), Marshall (1891) -- on anticipation and vividness, and is kin to Pope (1983) on the utility of the pre-outcome period and Wolf (1970) on utility from memory. It critiques the discount-rate estimation of Hausman (1979) and Landsberger (1971), and connects to the self-control literature of Ainslie (1975), Elster (1979), Schelling (1978), and Thaler (1981). The work anticipates Loewenstein & Prelec (1991, 1993) on anomalies and sequence preferences in intertemporal choice, [[@Caplin2001|Caplin & Leahy (2001)]] on anticipatory feelings and anxiety, and broader behavioural-economics treatments of reference dependence and emotion in decision-making.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
