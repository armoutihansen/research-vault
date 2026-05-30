---
citekey: Grund2010
title: Evidence on performance pay and risk aversion
authors: ["Grund, Christian", "Sliwka, Dirk"]
year: 2010
type: journalArticle
doi: 10.1016/j.econlet.2009.09.005
zotero: "zotero://select/library/items/5EX54PH9"
pdf: /Users/jesper/Zotero/storage/U3BD8PES/Grund2010.pdf
tags: [literature]
keywords: [performance-pay, risk-aversion, principal-agent, moral-hazard, incentive-contracts, gsoep]
topics: []
related: [Ackerberg2002, Aggarwal1999]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Making use of a unique representative data set, we find clear evidence that risk aversion has a highly significant and substantial negative impact on the probability that an employee's pay is performance contingent, which confirms the well known risk-incentive trade-off.

## Summary
Grund and Sliwka use the 2004 (21st) wave of the German Socio-Economic Panel (GSOEP) to provide what they claim is the first representative-sample test of the role of individual risk aversion in performance-pay contracting. Exploiting a then-new, experimentally validated survey measure of willingness to take risks, they show via probit regressions that more risk-averse employees are significantly and substantially less likely to have their performance appraised and to receive performance-contingent wages. This directly confirms the risk-incentive trade-off predicted by agency theory, a relationship that prior empirical work using only proxies for risk (uncertainty measures, wealth) had struggled to detect.

## Research question
Does an employee's individual risk aversion reduce the probability that their pay is performance contingent, as the principal-agent (moral hazard) model predicts? Equivalently: is the agent's risk aversion -- as opposed to environmental uncertainty -- an empirically detectable constraining factor on the provision of incentives?

## Method / identification
The empirical strategy is a set of binary probit regressions estimated on cross-sectional GSOEP data. The key right-hand-side regressor is the respondent's self-reported willingness to take risks (career-domain question), measured on an 11-point scale from 0 ("unwilling to take risks") to 10 ("fully prepared to take risks"). This measure was experimentally validated by Dohmen et al. (2005) as a good predictor of lottery-choice behaviour. The authors estimate four specifications with different binary dependent variables:
- Model (1): performance is regularly appraised by a superior (1 = yes).
- Model (2): appraisal AND it has monetary consequences (monthly wage, bonus, future wage increases, or promotions).
- Model (3): appraisal AND impact specifically on bonus.
- Model (4): appraisal but with NO monetary consequences (individuals with monetary consequences omitted), comparing pure-monitoring cases against individuals with no appraisal at all.

All models control for individual characteristics (sex, age, years of schooling) and job-based characteristics: tenure, part-time status, East/West region, 15 job-status dummies (blue/white collar and civil servants), firm-size dummies, and 12 industry dummies. Robust standard errors are reported. Economic significance is assessed by computing predicted probabilities from the probit at different quantiles of the risk-attitude distribution (comparing the 75th vs 25th percentile, holding other regressors at their means).

## Data
GSOEP 2004 (21st wave), a large representative survey of people living in Germany. The 2004 wave was extended -- at the authors' own suggestion to the DIW GSOEP team -- with questions on whether performance is regularly assessed by a superior and whether that assessment affects monthly wage, yearly bonus, future salary increases, and/or promotions, plus the novel 11-point risk-attitude battery (general and domain-specific). Sample: about 7,500 full- and part-time employees not older than 65 (n = 7,598 in descriptive statistics; regression samples 5,680-7,598). Performance is regularly appraised for 31% of employees; of those, roughly two thirds report at least one monetary consequence.

## Key findings
- Univariate: mean career willingness-to-take-risks is significantly higher for employees with performance appraisals (4.25, SD 2.44) than without (3.75, SD 2.48), $p<0.001$; the difference holds across the whole distribution (Kolmogorov-Smirnov, $p<0.001$) and is larger still for those whose appraisal affects bonuses (mean 4.48).
- Probit models (1)-(3): a highly significant positive coefficient on risk attitude (about $0.031$ to $0.032$, all significant at 1%) -- i.e., greater willingness to take risks raises the probability of appraisal and of monetary consequences, equivalently risk aversion lowers it.
- Model (4): when the appraisal has NO monetary consequences, the risk-attitude coefficient is small and insignificant. So the link is specifically to economically consequential performance pay, not to monitoring per se -- ruling out a "risk-averse people dislike being monitored" alternative.
- Economic magnitude: a person at the 75th percentile of willingness to take risks has a 16% higher chance of being appraised than one at the 25th percentile; for the probability of bonus impact the inter-quartile gap is 27%.
- Self-selection: dropping job-characteristic controls (industry, job status, part-time, firm size) raises the inter-quartile difference to 33%, indicating that risk-averse individuals sort into jobs where performance-contingent pay is less likely; the controls partially absorb this channel.
- Controls: men more than women and full-timers more than part-timers have appraised jobs; appraisal is more common in larger firms; older employees are slightly less often appraised (an age effect that strengthens without risk-attitude controls, since age correlates positively with risk aversion).

## Contribution
This is the first study to examine the interrelation between individual risk aversion and performance pay using a representative individual-level sample with a direct, experimentally validated measure of risk preferences. Earlier empirical agency-theory tests (surveyed by Prendergast, 1999, 2002) focused on environmental uncertainty and found weak or contradictory support; risk aversion itself was treated as unobservable (Allen & Lueck, 1995; Chiappori & Salanié, 2003) or proxied indirectly by wealth or fixed effects. By measuring risk attitudes directly, the paper supplies clean, economically substantial confirmation of the risk-incentive trade-off central to moral-hazard theory.

## Limitations & open questions
- The paper's explicit open agenda: jointly model the triangular interrelation between individuals' risk aversion, uncertainty of the environment, and incentive contracts simultaneously -- which requires having measures of both individual risk preferences AND performance-signal uncertainty in the same data. The authors hope growing matched employer-employee data sets will make this feasible.
- Identification is cross-sectional and associational; the sorting/self-selection result is suggestive rather than causally pinned down (risk-averse workers selecting into fixed-pay jobs vs. firms designing contracts conditional on worker type are not separated).
- Risk attitude is self-reported survey response; though validated, it remains a proxy for the structural risk-aversion parameter of the agency model.
- The performance-pay variable is a binary appraisal/monetary-consequence indicator, not pay-for-performance sensitivity (the slope), so the test concerns the extensive margin rather than the intensity of incentives.

## Connections
The work sits squarely in the empirical principal-agent / moral-hazard tradition surveyed by Prendergast (1999, 2002), and tests the risk-incentive trade-off studied via environmental-uncertainty proxies by [[@Aggarwal1999|Aggarwal & Samwick (1999)]], Allen & Lueck (1992), Lafontaine (1992), [[@Ackerberg2002|Ackerberg & Botticini (2002)]], Hilt (2006), and Wulf (2007). It complements the small set of papers that engaged risk aversion more directly: Gaynor & Gertler (1995) on physician revenue-sharing, Ferrall & Shearer (1999) who estimate an agency model from copper-mine payroll, and Bellemare & Shearer (2006) on tree-planters' risk tolerance. The risk-attitude measure is taken from Dohmen et al. (2005), and the sorting interpretation connects to Dohmen & Falk (2006) on multidimensional sorting into tournaments. Theoretical statements about the unobservability of risk preferences come from Allen & Lueck (1995) and Chiappori & Salanié (2003); indirect wealth-based proxying appears in Laffont & Matoussi (1995).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
