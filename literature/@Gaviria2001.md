---
citekey: Gaviria2001
title: School-Based Peer Effects and Juvenile Behavior
authors: ["Gaviria, Alejandro", "Raphael, Steven"]
year: 2001
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/UADNZ24R"
pdf: /Users/jesper/Zotero/storage/EQ37RNNJ/Gaviria2001.pdf
tags: [literature]
keywords: [peer-effects, social-interactions, linear-in-means, instrumental-variables, endogenous-sorting, juvenile-behavior, social-capital]
topics: ["[[peer-effects-social-interactions]]"]
related: [Glaeser1996]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We use a sample of tenth-graders to test for peer-group influences on the propensity to engage in five activities: drug use, alcohol drinking, cigarette smoking, church going, and the likelihood of dropping out of high school. We find strong evidence of peer-group effects at the school level for all activities. Tests for bias due to endogenous school choice yield mixed results. We find evidence of endogeneity bias for two of the five activities analyzed (drug use and alcohol drinking). On the whole, these results confirm the findings of previous research concerning interaction effects at the neighborhood level.

## Summary
Gaviria and Raphael ask whether a tenth-grader's propensity to engage in five behaviors (drug use, alcohol drinking, cigarette smoking, church attendance, dropping out) responds to the prevalence of that same behavior among schoolmates. Using NELS data on ~12,300 students in 928 schools, they estimate a linear-in-means model by OLS and 2SLS, instrumenting peer behavior with peer family-background averages. They find large, significant school-level peer effects for all five outcomes. They then probe whether endogenous sorting of families across schools inflates these estimates by comparing recent movers to long-term residents, finding endogeneity bias only for drug use (and weakly alcohol). A nonparametric variance test in the spirit of [[@Glaeser1996|Glaeser, Sacerdote, and Scheinkman (1996)]] corroborates the presence of social interactions.

## Research question
Does a youth's individual propensity to engage in deviant or social behavior depend causally on the prevalence of that behavior among the youth's *school* peers (Manski's "endogenous" social effect), once one controls for personal/family background, school characteristics, and the threat of spurious correlation from endogenous school choice? The choice of schools (rather than neighborhoods) as the reference group is deliberate: it is meant to suppress contextual effects and isolate behavioral (endogenous) peer influence.

## Method / identification
The structural model of individual behavior is the linear-in-means specification (following Case & Katz 1991):
$$Y_{is} = c + X_{is}\beta + W_s\varphi + \alpha\,\bar{Y}_{-is} + \epsilon_{is}$$
where $Y_{is}$ is a binary outcome for student $i$ in school $s$, $X_{is}$ is personal/family characteristics, $W_s$ is school characteristics, and $\bar{Y}_{-is}$ is the leave-one-out school mean of the behavior. The coefficient $\alpha$ is the endogenous peer effect; contextual effects ($\bar{X}_{-is}$ entering directly) are assumed away by construction.

Three identification threats are addressed. (1) **Simultaneity/reflection**: because individual behavior feeds the group mean, $\bar{Y}_{-is}$ is correlated with $\epsilon_{is}$, biasing OLS. Under the maintained assumption of no contextual effects, the leave-one-out peer *background* averages $\bar{X}_{-is}$ are valid instruments for $\bar{Y}_{-is}$, yielding 2SLS estimates. Instruments are peer averages of parental-involvement and parental-control variables, the share of peers with parental drug problems, share with college-educated parents, and share in single-parent families. First-stage F-tests reject weak instruments and overidentification tests are not rejected. (2) **Omitted school variables**: addressed both via the same IV strategy and by expanding $W_s$ to a large battery of NELS school characteristics (drug-information programs, closed campus, dropout-prevention programs, public/private, science-teacher counts, school-year length, etc.). (3) **Endogenous school choice / sorting**: following [[@Glaeser1996|Glaeser (1996)]], the sample is split into families that moved in the last two years ("movers") versus "stayers." If unobserved parental conscientiousness correlates with peer quality, the upward bias should be larger for movers; a Chow-type test on the equality of $\alpha$ across subsamples gauges the bias. Standard errors throughout use Huber-White estimators clustered by school to handle the Moulton (1990) grouped-regressor problem. A separate **nonparametric test** defines $w_s = (y_s - \bar{y})\sqrt{N_s}$; under no interactions its cross-school variance equals $\bar{y}(1-\bar{y})$, so the ratio of actual variance to $\bar{y}(1-\bar{y})$ is an index of social interaction (a value above ~1.14 rejects the no-interaction null at 1% with 928 df).

## Data
National Education Longitudinal Study (NELS) first follow-up (1990), tenth-graders. Two-stage sampling (schools, then students within schools), with minority oversampling. Sample restricted to schools with at least five sampled students: 12,300 students across 928 schools, mean 13.3 students/school. Outcomes are self-reported binary behaviors; controls include race, sex, single-parent status, parental education and SES, parental drug use, several parental-involvement/monitoring measures, sibling dropout, and school disciplinary policies (suspension/expulsion rules), Catholic-school and non-MSA indicators.

## Key findings
- **Strong, robust peer effects for all five outcomes.** OLS estimates of $\alpha$ are large, positive, and highly significant; largest for drug use, smallest (still substantial) for cigarette smoking. Moving a teen from a school with zero drug prevalence to one with 50% prevalence raises individual drug-use probability by ~13 percentage points; analogous moves give +9 (alcohol), +8 (smoking), +11 (church), +8 (dropping out).
- **Social multipliers.** A worked example shows a multiplier of ~1.34 for drug use: a rise in the share of peers with drug-problem parents propagates through the endogenous peer channel.
- **2SLS raises or matches OLS.** IV estimates are similar for smoking, dropping out, and drug use, and higher for church attendance and especially alcohol, suggesting simultaneity bias is, if anything, downward.
- **Mixed endogeneity-of-choice evidence.** Peer effects are larger for movers than stayers for drug use and alcohol, but the mover-stayer difference is statistically significant only for drug use; no evidence of sorting bias for the other four outcomes.
- **Robust to school controls.** Adding the large NELS school-characteristics battery barely changes the estimates.
- **Nonparametric corroboration.** Cross-school variance of all five behaviors exceeds the no-interaction benchmark, both raw and after orthogonalizing on school attributes/SES. However, the variance indices are much smaller than Glaeser et al.'s (1996) crime indices, casting doubt on the structural interpretation of those indices.
- **Family-structure interaction.** Peer effects are significantly stronger for single-parent-family youths only for dropping out.

## Contribution
The paper argues that *schools* are the right "sphere of interaction" for studying social-capital accumulation among teenagers, because the peer set is well defined and contextual (background) channels are weaker than at the neighborhood level, so observed effects more plausibly reflect Manski's endogenous (behavioral) interactions. It combines a structural IV strategy with a mover-stayer design for endogenous sorting and a nonparametric variance test, providing convergent evidence of genuine peer effects across a range of juvenile behaviors and confirming neighborhood-level findings in a school setting.

## Limitations & open questions
- The IV strategy hinges on the **assumption of no contextual effects** ($\bar{X}_{-is}$ excludable); if contextual effects exist, the instruments are invalid.
- IV validity also requires omitted school variables be uncorrelated with peer SES averages, which the authors themselves call into doubt.
- The mover-stayer test is indirect; the authors note that even if school *choice* is endogenous, peer *quality* may not be, since parents cannot fine-tune their children's peers along every behavioral dimension simultaneously, possibly explaining the "mixed" result.
- The nonparametric test's interpretation as peer effects rests on the strong assumption that **unobservables play no crucial role**; the authors quote Durlauf (1997) that priors against group effects may be unmoved by such evidence.
- They flag that the puzzlingly low variance indices (versus [[@Glaeser1996|Glaeser et al. 1996]] crime indices) undermine the structural reading of the index method.
- Broadly, they call for "a larger body of empirical research" before social capital can be confidently "seen," leaving accumulation and depreciation of social capital as open ground.

## Connections
The linear-in-means specification and IV-via-peer-background strategy come directly from Case & Katz (1991); the conceptual taxonomy of endogenous, contextual, and correlated (spurious) effects, plus the reflection problem, is Manski (1995). The mover-stayer identification device is from [[@Glaeser1996|Glaeser (1996)]], and the nonparametric variance index is from [[@Glaeser1996|Glaeser, Sacerdote, and Scheinkman (1996)]]. The endogenous-sorting correction connects to Evans, Oates, and Schwab (1992) (who found peer effects vanish under IV), Rosenbaum (1993) (Gautreaux relocation), and Aaronson (1998) (sibling variation), with Rivkin (1997) cautioning against metropolitan-aggregate instruments. Theoretical motivations draw on Becker (1996) on social capital in preferences, Bernheim (1994) and Akerlof (1997) on conformity, Sah (1991) on detection externalities in crime, and Bikhchandani, Hirshleifer, and Welch (1992) on informational cascades/herding. The grouped-error standard-error correction follows Moulton (1990). Broader human-capital-externality framing references Borjas (1995), Kremer (1997), and Lucas (1988).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
