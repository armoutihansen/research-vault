---
citekey: Farber2008
title: "Reference-Dependent Preferences and Labor Supply: The Case of New York City Taxi Drivers"
authors: ["Farber, Henry S."]
year: 2008
type: journalArticle
doi: 10.1257/aer.98.3.1069
zotero: "zotero://select/library/items/DSMU7GMD"
pdf: /Users/jesper/Zotero/storage/MRBHBBJ4/Farber2008.pdf
tags: [literature]
keywords: [reference-dependent-preferences, labor-supply, taxi-drivers, target-earnings, loss-aversion, discrete-choice, optimal-stopping]
topics: ["[[expectations-based-reference-dependence]]"]
related: [Bateman1997, Farber2005]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> I develop a model of daily labor supply where preferences are dependent on a reference daily income level, and I apply this model to data on the labor supply of New York City taxi drivers. I find that there may be a reference level of income on a given day that affects labor supply. However, there is substantial day-to-day variation in a given driver's reference level, and most shifts end before reaching the reference income level. This pattern is inconsistent with an important role for reference-dependent preferences.

## Summary
Farber builds an empirical model of the daily stopping decision of NYC taxi drivers that allows for reference-dependent preferences without requiring the reference income level to be observed in advance, instead estimating each driver's mean reference income and its day-to-day variance as parameters. Fit to 12,187 trips across 538 shifts for 15 drivers, the model finds that reaching the reference income level sharply raises the probability of stopping (a large, positive kink parameter $\delta$), and that mean reference levels differ across drivers and correlate with hours and income. But the estimated daily variance of the reference level is so large that the reference point has little predictive power for any given day, and most shifts end before income reaches the reference level. The construct of a reference income level is thus a poor determinant of labor supply.

## Research question
Do New York City taxi drivers behave as if they have a daily reference (target) income level that governs their stopping decision, and if so, is the reference level stable enough day to day to be a useful, predictive determinant of labor supply? The paper directly challenges the target-earnings interpretation of Camerer, Babcock, Loewenstein & Thaler (1997).

## Method / identification
The theoretical core is a reference-dependent utility over income $Y=Wh$ and hours $h$ with a kink at reference income $T$:
$$U(Y,h)=\alpha(Y-T)-\frac{\theta}{1+\nu}h^{1+\nu}\ \ (Y<T), \qquad U(Y,h)=(Y-T)-\frac{\theta}{1+\nu}h^{1+\nu}\ \ (Y>T),$$
with $\alpha>1$ giving higher marginal utility of income below the kink, $\nu$ the disutility-of-work elasticity parameter (wage elasticity $=1/\nu$), and $\theta$ scaling disutility of work. A key analytic result: the implied labor supply curve is upward-sloping with elasticity $1/\nu$ for low and high wages but downward-sloping with elasticity $-1$ in an intermediate wage band $W^{*}<W<W^{**}$ where the driver acts as a target earner ($Y=T$). Hence reference dependence does NOT imply a globally negative labor supply elasticity — a direct rebuttal of CBLT.

The empirical model treats each end-of-trip moment as a stopping opportunity. A latent stopping index is
$$S_{ijt}=X_{ijt}\beta+\delta\,I[Y_{ijt}\ge T_{ij}]+\epsilon_{ijt},$$
with $\epsilon$ standard normal, so the per-trip stopping probability is $\Phi[X_{ijt}\beta+\delta I[Y_{ijt}\ge T_{ij}]]$. The driver stops after trip $t$ if $S_{ijt}>0$; observed stopping at trip $s$ requires not stopping in the prior $t-1$ trips. The reference level is unobserved and modeled as $T_{ij}=\theta_i+\mu_{ij}$ with $\mu_{ij}\sim N(0,\sigma^2)$. Because $T_{ij}$ is unobserved, the unconditional stopping probability after trip $t$ integrates over the $t+1$ intervals in which $T_{ij}$ can fall relative to accumulated income $Y_{ij1},\dots,Y_{ijt}$, weighting interval probabilities (differences of $\Phi[(Y_{ijk}-\theta_i)/\sigma]$) by conditional stopping probabilities. The stochastic $\mu_{ij}$ also ensures continuity/regularity of the likelihood in $\theta_i$. Parameters $\beta$, $\delta$, $\{\theta_i\}$, and $\sigma^2$ are estimated by maximum likelihood. A nested standard probit ($\delta=0$, no reference level) serves as the comparison model.

## Data
Trip sheets from NYC taxi drivers, obtained via a leasing company: 593 sheets for 21 drivers over June 1999–May 2001. After dropping drivers with $\le 10$ shifts, the analysis sample is 538 shifts and 12,187 trips for 15 drivers (avg 27.8 shifts/driver). Each sheet records start/end time, location, and fare per trip; supplemented with NOAA weather (temperature, rainfall, snowfall). Median fare $5.30; median trip 10 min; 92.5% of trips intra-Manhattan, so stopping opportunities are frequent and income exceeds the reference by only a small margin at the first opportunity. No data on number of shifts worked (sheets received unsystematically), precluding inter-day analysis.

## Key findings
- The kink parameter is large and positive, $\hat\delta=5.63$ (one-sided $p=0.06$), implying the stopping probability jumps to near one once reference income is reached — apparent strong evidence for reference dependence.
- Mean reference income $\theta_i$ varies significantly across drivers (low $105.51 for driver 2, high $324.46 for driver 11; mean $191.42, SD $61.40); equality of $\theta_i$ rejected ($p<10^{-15}$). $\theta_i$ correlates with a driver's average income (0.72) and hours (0.75).
- BUT day-to-day variance is huge: $\hat\sigma^2=2779.58$, i.e. a within-driver daily SD of $52.72. For a driver with mean $200, the 95% interval for the daily reference is $97–$303. So the reference level is nearly unpredictable on any given day.
- A shift-level regression of income on $\hat\theta_i$ gives slope 0.262 but $R^2$ only 0.08; most income variation is within-driver. Reference levels explain little labor supply variation.
- Model comparison: the reference-dependent model log-likelihood ($-1612.6$) modestly beats a fixed-effects probit with accumulated income ($-1619.6$ to $-1614.1$) despite fewer/comparable parameters, but the standard probit's income terms are jointly insignificant ($p=0.276$). The reference model fits "somewhat better" but only mildly and parsimoniously.

## Contribution
Provides a tractable, estimable model of labor supply with reference-dependent preferences that does not require the analyst to observe or fix the reference point in advance, and that simultaneously estimates the reference level's mean and day-to-day variance. Theoretically clarifies that reference dependence implies target-earning behavior only within an intermediate wage band, refuting the claim that a negative labor supply elasticity is the signature of reference dependence (Camerer et al. 1997). Empirically reframes the NYC-taxi debate: even granting a reference-level kink, day-to-day instability undermines its usefulness as a labor supply determinant.

## Limitations & open questions
- The non-increasing marginal wage assumption underlying the closed-form labor supply solution is violated in practice ([[@Farber2005|Farber 2005]] documents sharply increasing within-day wages); the empirical discrete-choice model is an approximation to the true dynamic optimal-stopping problem, not its full DP solution.
- No formal nested test cleanly separates reference dependence from driver heterogeneity plus other day-to-day labor supply variation; the author cannot estimate a model with two sets of driver fixed effects.
- The decisive open question: is the large day-to-day movement in reference income systematic and predictable (e.g., responding to anticipated demand/weather)? If so, reference dependence could still matter; the author flags this as unexamined and as the path to a definitive verdict.
- No information on number of shifts worked precludes analysis of inter-day labor supply substitution.

## Connections
The paper is a direct rejoinder to Camerer, Babcock, Loewenstein & Thaler (1997), whose negative-elasticity / target-earnings finding for NYC cabdrivers it both reinterprets and challenges, and it extends the author's own [[@Farber2005|Farber (2005)]] intertemporal-substitution analysis of the same data. The reference-dependence theory draws on Tversky & Kahneman (1991) loss aversion, the endowment effect of Thaler (1980) and Kahneman, Knetsch & Thaler (1991), the WTA–WTP test of Bateman, [[@Bateman1997|Munro, Rhodes, Starmer & Sugden (1997)]], housing-market reference points in Genesove & Mayer (2001), and the theoretical refinements of Munro & Sugden (2003) and Köszegi & Rabin (2004). Related flexible-hours labor supply work includes Oettinger (1999), Fehr & Goette (2002), and the hours-constraint literature (Altonji & Paxson 1988; Ham 1982; Dickens & Lundberg 1993). Neumark & Postlewaite (1998) supply a relative-income reference-point application. The broader elasticity literature is surveyed in Killingsworth & Heckman (1986), Pencavel (1986), and Blundell & MaCurdy (1999).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
