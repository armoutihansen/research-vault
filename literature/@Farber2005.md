---
citekey: Farber2005
title: Is Tomorrow Another Day? The Labor Supply of New York City Cabdrivers
authors: ["Farber, Henry S."]
year: 2005
type: journalArticle
doi: 10.1086/426040
zotero: "zotero://select/library/items/MQWB63RL"
pdf: /Users/jesper/Zotero/storage/HK32X9QH/Farber2005.pdf
tags: [literature]
keywords: [labor-supply, intertemporal-substitution, target-earnings, reference-dependence, optimal-stopping, taxi-drivers, behavioral-economics]
topics: ["[[expectations-based-reference-dependence]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The labor supply of taxi drivers is consistent with the existence of intertemporal substitution. My analysis of the stopping behavior of New York City cabdrivers shows that daily income effects are small and that the decision to stop work at a particular point on a given day is primarily related to cumulative daily hours to that point. This is in contrast to the analysis of Camerer et al., who find that the daily wage elasticity of labor supply of New York City cabdrivers is substantially negative, implying large daily income effects. This difference in findings is due to important differences in empirical methods and to problems with the conception and measurement of the daily wage rate used by Camerer et al.

## Summary
Farber reanalyzes the labor supply of New York City taxi drivers and overturns the influential "target earnings" interpretation of Camerer, Babcock, Loewenstein, and Thaler (1997). Rather than regressing log daily hours on a constructed daily wage, he models the discrete decision to stop work after each fare as a survival/hazard problem. He finds that the probability of stopping is driven primarily by cumulative hours worked, not by cumulative income earned. This is what a standard neoclassical intertemporal labor supply model with small daily income effects predicts, and it contradicts daily target earning, under which drivers should quit once a fixed daily income target is reached.

## Research question
Do New York City cabdrivers behave as daily target earners (quitting once a daily income target is met, implying a negative daily wage elasticity), or as neoclassical intertemporal optimizers who smooth labor and consumption across days (so that daily income effects are small and the stopping decision tracks accumulated hours)?

## Method / identification
Farber sketches an additively separable intertemporal utility model. Lifetime utility is
$$U=\sum_{t=0}^{T}(1+r)^{-t}\big[a(x_t)+b(l_t)\big],$$
with goods $x_t$, leisure $l_t$, daily earnings $y_t(1-l_t)$ as a function of work time, and a lifetime budget constraint. The intratemporal first-order condition equates the marginal wage to the marginal rate of substitution of leisure for goods:
$$y_t'(1-l_t)=\frac{b'(l_t)}{a'(x_t)}.$$
Whether daily income effects matter hinges on the relative discount factor $v=(1+\rho)/(1+r)$: if drivers smooth consumption over horizons longer than a day (small $v$ at the daily level), transitory daily wage variation should raise daily hours and daily income effects should be negligible. Target earning is the extreme opposite case (large $v$, marginal utility of goods very high until a target).

Empirically, rather than estimate hours directly, Farber treats the end of each fare as a discrete decision point and estimates a probit optimal-stopping (hazard) model. A driver stops at $t$ if a latent index $R_{idc}(t)=\gamma_1 h_t+\gamma_2 y_t+X_{idc}\beta+\mu_i+\varepsilon_{idct}\ge 0$, where $h_t$ is cumulative hours worked so far, $y_t$ is cumulative income so far, and $X$ holds weather plus fixed effects for hour-of-day, day-of-week, driver, and end-of-trip location. The neoclassical model predicts $\gamma_1>0$ (stopping rises with hours) and $\gamma_2\approx 0$ (stopping unrelated to accumulated income), with stopping falling when further earnings opportunities are high; target earning predicts the reverse. He also replicates Camerer et al.'s OLS regression $\ln H_{it}=\eta\ln W_{it}+X_{it}\beta+\varepsilon_{it}$, where the wage $W_{it}=Y_{it}/H_{it}$ is built using the reciprocal of hours, and argues it suffers from division bias.

## Data
593 handwritten trip sheets covering 584 shifts for 21 drivers, collected from a single Manhattan taxi leasing company over June 1999–May 2001 (drivers leased weekly for $575, kept all fare income plus tips). After cleaning (imputation rules in an appendix), the sample has 13,464 trips; each trip records start/end time, start/end location (coded into 11 areas; 92 percent intra-Manhattan), and fare. Augmented with NOAA temperature and rainfall data. Critically, there is no record of which days a driver chose not to work, so the participation (days-worked) margin cannot be studied. Farber also reanalyzes Camerer et al.'s original TRIP data.

## Key findings
- In the probit stopping model with driver fixed effects, the probability of stopping is significantly positively related to total hours worked (a one-hour increase raises the stopping probability by about 3.7 percentage points before time controls) and not significantly related to cumulative income. This is consistent with $\gamma_1>0,\ \gamma_2\approx 0$ — the neoclassical prediction, not target earning.
- An analysis of variance of the hourly wage shows over 70 percent of wage variation is unsystematic within-driver, within-day, interhour variation; within-shift autocorrelations of the hourly wage are small and statistically insignificant. There is thus little genuine transitory between-day wage variation to drive a target-earnings test, and no stable "daily wage" the driver could treat parametrically.
- Replicating Camerer et al.'s OLS log-hours regression on his own data reproduces their strongly negative elasticity (about $-0.69$), but Farber attributes this to division bias (the wage uses the inverse of the dependent variable) and to the absence of legitimate parametric wage variation.
- Drivers are substantially more likely to stop after a fare ending outside Manhattan (e.g. about 6 percentage points higher after a LaGuardia trip), plausibly because such fares take them toward home. Stopping is about 1.6 points less likely on hot days; rainfall has no significant effect on stopping (suggesting the difficulty of hailing cabs in rain reflects demand, not reduced supply).
- The contrasting results from his and Camerer et al.'s data are driven by analytic framework, not by data differences, since both methods reproduce across both datasets.

## Contribution
Farber reconciles the taxi-driver evidence with the broader emerging literature on labor supply in flexible-hours settings (stadium vendors, bicycle messengers) that finds positive intertemporal elasticities. By recasting the problem as optimal stopping rather than as an hours regression on a constructed wage, he removes division bias and the untenable assumption of a parametric daily wage, and shows the canonical behavioral-economics example of reference-dependent target earning is better explained by a conventional neoclassical model.

## Limitations & open questions
- Trip sheets cannot be verified against meter summaries, so completeness is assumed rather than checked.
- The data identify only the daily hours margin; the participation (days-worked) margin cannot be examined, yet a full labor-supply response operates on both margins.
- Farber estimates a stopping model but not a wage elasticity of labor supply: doing so would require exogenous permanent or transitory shifts in earnings opportunities, e.g. a natural or randomized field experiment delivering clean variation in daily earnings.
- He concedes drivers may have benchmark earnings levels, leaving open whether such reference points operate at horizons longer than a single day.

## Connections
This paper is the direct rebuttal to Camerer, Babcock, Loewenstein & Thaler (1997), whose target-earnings finding it disputes, and to Chou (2000), who extended that approach to Singapore. It builds on the flexible-hours labor supply literature, especially Oettinger (1999) on stadium vendors and Fehr & Goette (2002) on bicycle messengers, both of which find positive intertemporal elasticities; Farber argues their participation-margin designs supply the exogenous variation his own data lack. The intertemporal framework follows MaCurdy (1981) and the surveys of Pencavel (1986), Killingsworth & Heckman (1986), and Blundell & MaCurdy (1999). The hours-constraints literature he contrasts with includes Kahn & Lang (1991), Dickens & Lundberg (1993), Ham (1982), and Altonji & Paxson (1988). The broader debate over reference-dependence and loss aversion in labor supply continues in later work building on Koszegi & Rabin reference-dependent preferences and in Farber's own subsequent reanalyses of cabdriver behavior.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
