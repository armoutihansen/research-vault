---
citekey: Crawford2011
title: "New York City Cab Drivers' Labor Supply Revisited: Reference-Dependent Preferences with Rational-Expectations Targets for Hours and Income"
authors: ["Crawford, Vincent P.", "Meng, Juanjuan"]
year: 2011
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/RP48KTDN"
pdf: /Users/jesper/Zotero/storage/HWBNCJRP/Crawford2011.pdf
tags: [literature]
keywords: [reference-dependent-preferences, labor-supply, loss-aversion, rational-expectations, koszegi-rabin, income-targeting]
topics: []
related: [Abeler2011, Farber2005, Kahneman1979, Koszegi2006b]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper proposes a model of cab drivers' labor supply, building on Henry S. Farber's (2005, 2008) empirical analyses and Botond Köszegi and Matthew Rabin's (2006; henceforth "KR") theory of reference-dependent preferences. Following KR, our model has targets for hours as well as income, determined by proxied rational expectations. Our model, estimated with Farber's data, reconciles his finding that stopping probabilities are significantly related to hours but not income with Colin Camerer et al.'s (1997) negative "wage" elasticity of hours; and avoids Farber's criticism that estimates of drivers' income targets are too unstable to yield a useful model of labor supply.

## Summary

Crawford and Meng revisit the celebrated puzzle of New York City cab drivers, who appear to work fewer hours on high-wage days—a negative labor-supply elasticity that contradicts the neoclassical model. They build a reference-dependent labor-supply model in the spirit of Köszegi and Rabin (KR, 2006), with daily targets for *both* hours *and* income, where the targets are proxied rational expectations rather than estimated latent variables. Re-estimating on Farber's (2005, 2008) data, the model reconciles Farber's stopping-probability findings with Camerer et al.'s (1997) negative wage elasticity, and—because the rational-expectations targets are operationalized via low-endogeneity sample proxies—escapes Farber's complaint that estimated income targets are too unstable to be useful.

## Research question

Is cab drivers' labor supply reference-dependent, and if so does a model with KR-style rational-expectations targets for both hours and income reconcile the conflicting prior evidence (Camerer et al.'s negative wage elasticity vs. Farber's null on income targeting) better than either a neoclassical model or Farber's income-only targeting model?

## Method / identification

The driver's daily total utility over income $I$ and hours $H$, given targets $I^r$ and $H^r$, is a weighted average of consumption utility and gain–loss utility:
$$V(I,H\mid I^r,H^r) = (1-\eta)\big(U_1(I)+U_2(H)\big) + \eta\, R(I,H\mid I^r,H^r),$$
with weight $\eta\in(0,1)$ on gain–loss utility. The separable gain–loss term applies a loss-aversion coefficient $\lambda$ to the realized-minus-target *consumption-utility* differences, in each of income and hours, e.g. a loss in income contributes $\lambda\big(U_1(I)-U_1(I^r)\big)$ when $I<I^r$ and a gain contributes $U_1(I)-U_1(I^r)$ when $I>I^r$ (symmetrically for hours, with $U_1$ increasing/concave, $U_2$ decreasing/concave). Following KR's Assumption A3', gain–loss utility is linear in those utility differences (ruling out diminishing sensitivity), and $\lambda$ is common to income and hours.

Targets are KR rational expectations, but treated as *point* expectations (the authors argue this exaggerates loss aversion and so biases against the reference-dependent model). With risk-neutrality in income and serially uncorrelated within-day earnings, expected hourly earnings act like a predetermined random daily wage $w^e$, and optimal stopping is characterized by a generalized first-order condition with kinks at the reference points: the driver continues while $w^e$ exceeds the relevant marginal rate of substitution. Across the four gain–loss regions, the hours-disutility cost of income is the neoclassical $-U_2'(H)/U_1'(I)$ in the gain–gain and loss–loss interiors, but is scaled by $(1-\eta+\eta\lambda)$ or $1/(1-\eta+\eta\lambda)$ in the mixed (income-loss/hours-gain and income-gain/hours-loss) domains. This makes the reference-dependent labor-supply curve nonmonotonic, with a downward-sloping segment where the income target binds second.

Estimation proceeds in three layers, closely following Farber's econometric strategies: (A) probit models of the stopping probability linear in cumulative hours and income, but *split-sample* by whether the first hour's earnings exceed proxied expectations—a criterion approximately uncorrelated with stopping errors, limiting selection bias; (B) reduced-form probits adding dummies for hitting the income and hours targets; (C) a structural reference-dependent model. The crucial identification device throughout is operationalizing each driver's targets as sample averages, driver/day-of-week by driver/day-of-week, computed only from days *prior* to the day in question (avoiding the confounding of including the current shift). In the structural model $\eta$ and $\lambda$ are not separately identified, but the combination $\eta(\lambda-1)$ is.

## Data

Farber's (2005, 2008) trip-sheet data on New York City cab drivers: 21 drivers, 584 trip sheets (shifts), June 2000–May 2001, all weekly lessees free to choose daily hours, plus weather controls. The prior-day-averaging proxy censors first-of-week shifts (3,124 of 13,461 observations); estimation samples are roughly 8,958 observations (split into ~4,664 high-early-earnings and ~4,294 low-early-earnings shift-trips).

## Key findings

- **Split-sample reversal (Section IIA, Table 2).** When the first hour's earnings exceed expectations, hours (not income) significantly raises the stopping probability; when they fall short, income (not hours) does. This *reversal* is impossible under a neoclassical model (targets irrelevant) but is one of the two signatures of a reference-dependent model with homogeneous preferences—here the *second* target a driver reaches dominates the stopping decision.
- It is also inconsistent with Farber's *income-only* targeting model, which cannot generate the significant hours effect on good days combined with its insignificance on bad days.
- **Reduced form (Section IIB).** Dummies for crossing the income and hours targets carry large, significant increments with the reference-dependent sign pattern; effects come from being above/below target rather than from levels.
- **Structural (Section IIC, Tables 4–5).** The identified function $\eta(\lambda-1)$ is precisely and plausibly estimated, deviates strongly and significantly from the neoclassical value, and is robust to the expectations proxy. The specification allowing sophisticated within-shift wage forecasting fits best; ruling out hours-targeting or day-of-week variation carries nontrivial likelihood cost.
- The model reproduces a *negative aggregate* wage elasticity while preserving the neoclassical positive incentive of *anticipated* wage increases (gain–loss utility drops out for perfectly anticipated changes), and reconciles Farber's smooth aggregate stopping–income relationship with the significant hours/insignificant income pattern.

## Contribution

First structural test of KR's reference-dependent preferences—with rational-expectations targets in *both* income and hours—applied to field labor supply. Methodologically it shows that proxying targets as predetermined sample expectations (rather than estimating unstable latent targets) overcomes Farber's main critique, and that a sample-splitting design on early earnings yields a robust, near-assumption-free test for reference dependence.

## Limitations & open questions

- Targets are modeled as *point* (not distributional) expectations and drivers ignore option value in stopping; the authors flag that distributional preferred personal equilibrium might behave differently and that their myopic stopping departs from KR's preferred personal equilibrium.
- $\eta$ and $\lambda$ are not separately identified—only $\eta(\lambda-1)$.
- Preferences are assumed homogeneous; the authors note (citing Doran 2009) that real heterogeneity—some drivers reference-dependent, some neoclassical—permits other significance patterns and calls for individual-level data.
- The sample is small (21 drivers); they explicitly call for larger datasets and more careful modeling of targets, and ask how far reference dependence extends beyond inexperienced workers or unanticipated changes (the question with the largest policy stakes).
- Within-day serial correlation of earnings is assumed away for tractability, despite Camerer et al.'s contrary evidence.

## Connections

Directly extends [[@Farber2005|Farber]] (2005, 2008) and operationalizes Köszegi & [[@Koszegi2006b|Rabin]] (2006; 2007) reference-dependent preferences with expectations-based reference points; the empirical puzzle originates with Camerer, Babcock, Loewenstein & Thaler (1997). The reference-dependence/loss-aversion machinery descends from [[@Kahneman1979|Kahneman & Tversky (1979)]] and Tversky & Kahneman (1991). Related field labor-supply evidence includes Oettinger (1999) on stadium vendors, Fehr & Goette (2007) on bicycle messengers, Doran (2009) on driver heterogeneity, and Post, Van den Assem, Baltussen & Thaler (2008) on stopping without option value. The rational-expectations-target view of reference points was tested in the lab by [[@Abeler2011|Abeler, Falk, Goette & Huffman (2011)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
