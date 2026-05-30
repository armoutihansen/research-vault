---
citekey: Lundborg2006
title: Having the wrong friends? Peer effects in adolescent substance use
authors: ["Lundborg, Petter"]
year: 2006
type: journalArticle
doi: 10.1016/j.jhealeco.2005.02.001
zotero: "zotero://select/library/items/QMXB23GS"
pdf: /Users/jesper/Zotero/storage/3ALSMGI8/Lundborg2006.pdf
tags: [literature]
keywords: [peer-effects, adolescent-substance-use, reflection-problem, fixed-effects, instrumental-variables, health-economics, social-interactions]
topics: []
related: [Gaviria2001]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Swedish cross-sectional survey data on young individuals aged 12–18-year-old was used to analyse school–class based peer effects in binge drinking, smoking and illicit-drug use. Significant and positive peer effects were found for all three activities. By introducing school/grade fixed effects, the estimated peer effects were identified by variation in peer behaviour across school–classes within schools and grades, implying that estimates were not biased due to endogenous sorting of students across schools. Further, endogeneity bias due to bi-directionality of peer effects was found for binge drinking and smoking. Controlling for this source of endogeneity resulted in even stronger peer effects.

## Summary
Lundborg estimates endogenous peer effects in three adolescent risky behaviours (binge drinking, smoking, illicit-drug use) using survey data from one Swedish town, defining the peer group narrowly as classmates. The paper's contribution is methodological discipline within a single dataset: it confronts Manski's two main confounds in sequence. School/grade fixed effects strip out cross-school sorting, and a two-stage probit instruments away the reflection/simultaneity bias from peers influencing each other. Peer effects survive both: fixed effects shave 10–19% off the raw correlation, but instrumenting for endogenous peer behaviour more than doubles the marginal effects, implying the naive estimate is downward (not upward) biased once measurement error and reflection are addressed.

## Research question
Do peers causally influence an adolescent's probability of binge drinking, smoking, and using illicit drugs, and how large are these effects once spurious sorting and the bi-directionality (reflection) of peer behaviour are accounted for? Substantively, the policy motivation is the "social multiplier": if peer effects are real, interventions (e.g. a minimum legal drinking age) are amplified at the group level because reducing one adolescent's consumption also lowers consumption among the peers who feed back on them.

## Method / identification
The estimating equation is a latent-variable probit. For individual $i$ in class $c$, grade $g$, school $s$,
$$Y^{*}_{icgs} = \beta_0 + \beta_1\,\mathrm{PEER}_{cs} + \beta_2 X_{icgs} + \beta_3 D_{gs} + \varepsilon_{icgs},$$
with the observed binary outcome $Y_{icgs}=1$ if $Y^{*}_{icgs}>0$. The peer regressor is the leave-one-out class mean,
$$\mathrm{PEER}_{ic} = \frac{1}{N-1}\sum_{\substack{j=1 \\ j\neq i}}^{N} y_j,$$
where $y_j$ is classmate $j$'s binary substance-use indicator. $X$ holds personal controls (age dummies, gender, born-in-Sweden, truancy, single-parent household, smokeless-tobacco use, solvent sniffing, desire to try narcotics, parental drinking attitudes, perceived alcoholism/lung-cancer risk), and $D_{gs}$ is a vector of school/grade dummies. Standard errors use Stata's robust sandwich estimator clustering on class.

Identification proceeds in three nested specifications. (1) Baseline probit, no fixed effects, peer use treated as exogenous. (2) Add school/grade fixed effects: because Swedish parents choose residence/school but cannot choose their child's class, and schools do not track students across classes by ability, the remaining within-school/grade variation in $\mathrm{PEER}_{cs}$ is argued to be free of sorting (Manski's "correlated effects"). (3) Two-stage probit (Maddala, 1983, pp. 244–245) to purge the endogenous, bi-directional component: first-stage OLS regresses peer use on instruments plus the exogenous $X$; the fitted value replaces $\mathrm{PEER}_{cs}$ in the second-stage probit. Instruments are class-average background characteristics (share in single-parent households, share living in an apartment, share with foreign-born parents, share who have drunk with parents; plus, for drugs, share knowing a supplier; for drinking, share encouraged to drink by parents and share whose parents would supply beer). The exclusion logic rests on the prior argument that contextual effects are negligible at the class level, so peers' family background acts only through peers' behaviour. Instrument validity is checked with a first-stage F-test, first-stage $R^2$, two Bollen et al. (1995) overidentification tests (an LR comparison and a Wald test of excluded instruments re-entered into the structural equation), and a Rivers–Vuong (1988) endogeneity test (first-stage residual added to the main equation; significance implies endogeneity). The author notes Rivers–Vuong control-function estimates were nearly identical to the Maddala two-step.

## Data
Two anonymous classroom surveys (May 2000 and May 2001) in Trelleborg, a mid-sized town on Sweden's south coast; 3253 questionnaires, ~53% from 2001. Respondents are aged 12–18 (compulsory grades 6–9 and upper-secondary years 1–2). Usable samples after missing-data deletion: 2606 (binge drinking), 2640 (smoking), 3027 (drugs), clustered in 149 classes. Outcomes are dichotomous: binge drinking (heavy consumption in the past month, with explicit volume thresholds), daily/near-daily smoking, any illicit-drug use in the past 6 months. Base rates are 0.37, 0.14, and 0.05 respectively. Five school districts; some districts contain small one-class-per-grade schools that share a district code and so cannot be separately identified — a key data limitation. At upper-secondary level the author uses programme/grade (vocational vs. preparatory) rather than school fixed effects.

## Key findings
- Baseline (no FE, exogenous peers): significant positive marginal effects of peer use on own use — 0.284 (binge drinking), 0.180 (smoking), 0.057 (drugs); a 10-point rise in peer prevalence raises own probability by 2.84, 1.8, and 0.57 points respectively. Magnitude tracks base rate: largest for the most common behaviour, smallest for the rarest.
- Adding school/grade fixed effects keeps all three significant at 1% but shrinks them — by ~19% (binge drinking, 0.284→0.230), ~16% (smoking, to 0.166), and ~10% (drugs, to 0.065). Thus cross-school sorting accounts for only that fraction of the raw correlation, not the whole effect.
- A sensitivity check dropping districts with unidentifiable small schools and then all upper-secondary observations leaves binge-drinking and drug effects significant at 1%; the smoking effect becomes insignificant in the most restrictive cut, but with much-reduced sample (916 obs) the author cannot distinguish a true null from low power.
- Two-stage (endogenous peers): all three remain positive and significant, but marginal effects more than double — binge drinking 0.230→0.557, smoking 0.166→0.470, drugs 0.065→0.159. Rivers–Vuong rejects exogeneity for binge drinking and smoking but not for drugs. Overidentification tests do not reject instrument validity; first-stage adjusted $R^2$ ranges 0.37–0.82. The interpretation is that the naive estimate is biased *downward*, plausibly because measured peer behaviour is error-ridden and instrumenting also attenuates that measurement-error bias.
- Heterogeneity (interaction terms): females are *less* influenced by peer binge drinking but *more* influenced by peer smoking than males; students born outside Sweden are more influenced by peer drug use; single-parent-household status yields no significant interaction (consistent with Gaviria and Raphael, 2001). Perceived alcoholism and lung-cancer risk significantly reduce drinking and smoking respectively.

## Contribution
The paper improves credibility over earlier neighbourhood- or school-level peer-effect studies on three fronts: (i) a narrow, behaviourally meaningful peer group (the actual classmates), reducing peer-group measurement error; (ii) institutionally grounded fixed-effects identification that exploits the fact that Swedish parents cannot select their child's class, neutralising cross-school sorting; and (iii) explicit treatment of the reflection problem via instruments built from class-average backgrounds, justified by the claim that contextual effects vanish at the class level. The headline empirical message — that correcting for endogeneity raises rather than lowers peer effects — pushes against the common presumption that uncorrected peer-effect estimates are inflated.

## Limitations & open questions
- **Within-school (within-grade) sorting is not controlled.** If parents persuade a principal to place a child in a particular class (e.g. for a preferred teacher), residual sorting can still contaminate the estimates; the author concedes this cannot be fully ruled out.
- **Unidentifiable small schools.** Some one-class-per-grade schools share a district code, so a sliver of between-school variation survives the fixed effects; handled only by sensitivity analysis, at the cost of power (notably for smoking).
- **Endogenous individual controls.** Risk perceptions and the truancy / smokeless-tobacco / solvent-sniffing / desire-to-try-narcotics regressors may be jointly determined with substance use (reverse causality, common unobservables); the author flags their coefficients as potentially biased and leaves instrumenting them to future work.
- **Joint determination of the three behaviours.** Smoking, drinking, and drug decisions may be simultaneous; a multivariate probit is named as the natural extension but is "beyond the scope of this paper."
- **Cross-study comparability.** Magnitudes are not directly comparable to prior work because peer groups and methods differ; the author also cautions against perceived-peer-behaviour designs, which suffer "projection effects" that overstate peer influence.
- **External validity.** Estimates come from a single Swedish municipality, leaving generalisability to other institutional settings open.

## Connections
The framing is squarely Manski (1993, 1995): endogenous vs. contextual vs. correlated effects, and the reflection problem the two-stage strategy attacks. The fixed-effects-plus-class-average-instruments design is borrowed explicitly from Case and Katz (1991) and [[@Gaviria2001|Gaviria and Raphael (2001)]], with the latter also supplying the comparison estimates (peer marginal effects of ~0.32/0.35/0.16) and the single-parent null. Norton, Lindrooth and Ennett (1998) supply much larger neighbourhood-level estimates. Methodological scaffolding comes from Maddala (1983) for the two-stage probit, Rivers and Vuong (1988) for the endogeneity test and control-function alternative, Bollen et al. (1995) for overidentification testing, and Guilkey et al. (1992) for the finding that Maddala's standard-error correction offers no finite-sample gain. Related contemporaneous peer-effect work includes Clark and Lohéac (2004), Krauth (2004), and the room-mate randomisation of Kremer and Levy (2003). Theoretically the paper sits beside the addiction/price literature (Becker and Murphy, 1988; Becker, 1992) and social-interaction welfare results (Laux, 2000), with the risk-perception findings echoing Viscusi (1990, 1991) and the author's own work with Lindgren (2002, 2004).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
