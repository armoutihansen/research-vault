---
citekey: Glaeser1996
title: Crime and Social Interactions
authors: ["Glaeser, Edward L.", "Sacerdote, Bruce", "Scheinkman, José A."]
year: 1996
type: journalArticle
doi: 10.2307/2946686
zotero: "zotero://select/library/items/V39M3NGH"
pdf: /Users/jesper/Zotero/storage/BKC4JJZ2/Glaeser1996.pdf
tags: [literature]
keywords: [social-interactions, crime, peer-effects, cross-city-variance, voter-model, identification, unobserved-heterogeneity]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The high variance of crime rates across time and space is one of the oldest puzzles in the social sciences; this variance appears too high to be explained by changes in the exogenous costs and benefits of crime. We present a model where social interactions create enough covariance across individuals to explain the high cross-city variance of crime rates. This model provides an index of social interactions which suggests that the amount of social interactions is highest in petty crimes, moderate in more serious crimes, and almost negligible in murder and rape.

## Summary
Cross-city and cross-precinct crime rates vary far more than differences in local economic and social conditions can explain (observables account for under 30% of the variance). The paper argues that the only way to generate this excess variance is positive covariance across individuals' crime decisions, i.e. social interactions. It builds a tractable local-interactions model in which a city's crime variance is the independent-decision variance inflated by a factor that declines in the share of "fixed" (uninfluenced) agents. Inverting this relationship turns the observed variance into an estimable index of social interaction. Empirically, interaction is highest for larceny and auto theft (implied social-group sizes over 200), moderate for assault, burglary and robbery (~100), and nearly negligible for murder, rape and arson (group sizes of one to five).

## Research question
What explains the extraordinarily high variance of crime rates across cities, precincts and time, when observable local conditions explain so little of it? Can the excess variance be used to measure the degree of social interaction (peer/neighbor influence) in different types of criminal behavior?

## Method / identification
The core is a one-dimensional local-interactions model adapted from physical-science voter models. There are $2n+1$ agents indexed $i=-n,\dots,n$, arranged on a circle; each chooses an action $a_i\in\{0,1\}$ where action 1 is "commit a crime," and agent $i$'s utility depends on $a_i$ and on the predecessor's action $a_{i-1}$. Agents come in three types: type 0 always chooses $a_i=0$ (diehard law-abiders), type 1 always chooses $a_i=1$ (diehard criminals), and type 2 imitates the predecessor (since $U_2(1,1)>U_2(1,0)$ and $U_2(0,0)>U_2(0,1)$). Types 0 and 1 are "fixed agents" with total probability $\pi=p_0+p_1$; the continuous-attribute interpretation lets city characteristics shift $p_0,p_1$ and the unconditional crime probability $p=p_1/(p_0+p_1)$.

The unique Nash equilibrium has each uninterrupted run of type-2 agents copying the fixed agent that begins it. Fixed agents create enough mixing for a central limit theorem. The key analytic result is the variance decomposition of the population-weighted crime rate: with $S_n$ the deviation of realized from expected crimes,
$$\lim_{n\to\infty}(2n+1)E(S_n^2)=\operatorname{var}(a_0)+2\lim_{n\to\infty}\sum_{i=1}^{n}\operatorname{cov}(a_0,a_i)=p(1-p)\,\frac{2-\pi}{\pi}\equiv\sigma^2.$$
Writing $f(\pi)=(2-\pi)/\pi$, the variance of $\sqrt{N}$-weighted crime rates equals $p(1-p)f(\pi)$: with no imitation $\pi=1$, $f(\pi)=1$; as the influenceable share rises ($\pi\to0$), $f(\pi)\to\infty$. The inverse $f^{-1}$ gives the index; the expected distance between fixed agents, $\approx 1/\pi$, is interpreted as average social-group (clique) size.

Identification's central difficulty is separating social interaction from unobserved spatial heterogeneity in the crime propensity $p$. The empirical framework writes the true probability with a logit form $p_j^*=e^{v_j}/(1+e^{v_j})$, $v_j=t_j+\varepsilon_j$, with $\varepsilon_j\sim N(0,\lambda^2)$ the unobserved-heterogeneity term. Defining $y_j=(p_j-\hat p_j)\sqrt{N_j}$, the law of total variance $\operatorname{var}(y)=\operatorname{var}[E(y_j\mid\varepsilon_j)]+E[\operatorname{var}(y_j\mid\varepsilon_j)]$ splits crime variance into a heterogeneity component (which grows linearly with city size $N_j$) and a social-interaction component $f(\pi)p_j^*(1-p_j^*)$ (which does not). This size dependence is what identifies the two. Estimation regresses crime rates on city characteristics via logit to form $\hat p_j$, then uses GMM on the moment equation in $(p_j-\hat p_j)^2 N_j$ to recover $\pi$ (hence $f(\pi)$) and $\lambda$ jointly. Robustness checks fix $\lambda$ so unobservables predict twice as much as a one-year lagged crime rate, and allow repeat offenders. Appendix 1 develops a symmetric (two-sided) imitation voter model that changes the functional form of $f(\pi)$ only marginally.

## Data
FBI Uniform Crime Reporting cross-city data for 1985 ($N=658$), 1970 ($N=617$, smaller due to availability), and 1986 ($N\approx631$), merged with County and City Data Book urban characteristics (population, growth, schooling, unemployment, poverty, female-headed households, owner occupancy, property taxes, police per capita, percent nonwhite, regional dummies). New York City Police Department reported-crime data by precinct for 1993 ($N=70$) matched to 1990 census-by-precinct data. Crimes are reported-and-verified (not arrests or surveys). Measurement error is discussed but its sign on the variance is shown to be theoretically ambiguous; drawing on Levitt's calculations, the authors argue the resulting bias is small.

## Key findings
- Excess variance is real: even allowing crime rates to come from up to seven distributions and controlling for observables, interurban crime variance stays very high, so multiple-equilibria (global-interaction) models cannot parsimoniously explain it; the data do not cluster into a few equilibria.
- Estimated $f(\pi)$ (Table IIA) implies high social interaction for larceny and auto theft (average social-group sizes over 200), moderate-to-large for assault, burglary and robbery (~100), and almost none for murder, rape and arson (group sizes of one to five).
- Interaction levels are roughly stable across the three samples for each crime even though mean crime levels differ, which the authors read as evidence the methodology is reliable.
- Cross-crime pattern: crimes committed by younger offenders show higher interaction. Cross-city pattern: for serious crime, larceny and auto theft, interaction is larger where families are less intact; conditional correlations point to family instability rather than unemployment, schooling or arrest rates as the operative channel.
- A placebo application to mortality from cancer, diabetes, pneumonia and suicide yields near-zero interaction; heart disease shows somewhat more but still less than most crimes.

## Contribution
Provides a micro-founded, estimable bridge from individual interaction to aggregate variance: rather than positing multiple equilibria, it uses local interactions plus a fraction of unresponsive agents to rationalize large but smooth cross-sectional variance, and crucially turns the second moment of crime rates into a measurable index of social interaction comparable across crimes, places and time. The variance-decomposition-by-city-size identification strategy generalizes beyond crime to any aggregate outcome suspected of cross-individual spillovers.

## Limitations & open questions
- The interaction estimate is only separable from unobserved heterogeneity under either a functional-form assumption on $\varepsilon_j$ (normality) or an assumed magnitude of heterogeneity; the authors concede a reader who rejects both must read the estimates as identifying only some combination of interaction and unobserved heterogeneity.
- Migration/locational sorting is taken as predetermined; sorting of criminals into the same areas is itself a form of positive interaction not separated out.
- Crimes are treated as independent social phenomena (no modeling of interactions across crime types); the authors flag this as unrealistic and a source of lost information.
- Measurement error's effect on the variance is theoretically signed only ambiguously.
- The model is one-dimensional with predecessor-only influence; richer spatial structure and joint local-plus-global interactions are noted as ideal but not implemented.
- Aggregate data cannot disentangle why local characteristics matter (own vs. environmental effects); individual-level data are needed.

## Connections
Builds directly on Becker (1968) and the deterrence/economics-of-crime tradition (Ehrlich 1975; Freeman 1991; Levitt 1994). The multiple-equilibria alternatives it argues against include Sah (1991) on arrest-probability spillovers and Murphy, Shleifer & Vishny (1993) on crowding out of legal activity; stigma channels relate to Rasmussen (1995). The local-interactions/voter-model machinery follows Kinderman & Snell (1980), Jovanovic (1985), and Scheinkman & Woodford (1994); sorting links to Ellison & Glaeser (1994). Empirical support for youth interactions echoes Case & Katz (1991). The differential-association sociology stems from Sutherland (1939) and Reiss (1980, 1988), with civilian-monitoring ideas from Jacobs (1961) and community enforcement from Akerlof & Yellen (1994). The paper is a foundational reference for the broader social-interactions literature later formalized by Brock & Durlauf and Glaeser & Scheinkman.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
