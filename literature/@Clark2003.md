---
citekey: Clark2003
title: "Unemployment as a Social Norm: Psychological Evidence from Panel Data"
authors: ["Clark, Andrew E."]
year: 2003
type: journalArticle
doi: 10.1086/345560
zotero: "zotero://select/library/items/UC47PQBR"
pdf: /Users/jesper/Zotero/storage/KFVKJUZ2/Clark2003.pdf
tags: [literature]
keywords: [social-norms, unemployment, subjective-well-being, reference-groups, hysteresis, panel-data]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This article uses seven waves of panel data to test for social norms in labor market status. The unemployed's well‐being is shown to be strongly positively correlated with reference group unemployment (at the regional, partner, or household level). This result, far stronger for men, is robust to controls for unobserved individual heterogeneity. Panel data also show that those whose well‐being fell the most on entering unemployment are less likely to remain unemployed. These findings suggest a psychological explanation of both unemployment polarization and hysteresis, based on the utility effects of a changing employment norm in the reference group.

## Summary
Clark tests one of the cornerstones of social-norm theory directly: that individual utility depends on a norm. Using seven waves of the British Household Panel Survey (BHPS) and the GHQ-12 as a proxy for utility, he shows that while higher unemployment among "relevant others" lowers the well-being of the employed, it *raises* the well-being of the unemployed. Unemployment always hurts, but it hurts less when more people around you are also unemployed. The effect is strong for men, weak for women, and survives individual fixed effects. He then links the result to behavior: those most psychologically hurt by unemployment search harder and exit unemployment faster, offering a psychological micro-foundation for unemployment hysteresis and polarization.

## Research question
Does the psychological (utility) cost of an individual's own unemployment depend on the unemployment of relevant others, as social-norm and social-comparison models predict? And does the resulting heterogeneity in the well-being cost of unemployment feed back into labor-market behavior (search, exit), generating hysteresis?

## Method / identification
The paper operationalizes Akerlof's (1980) social-norm model. Utility is $W=W(R,A,d^c,X)$ where $R$ is reputation, $A$ a dummy for obeying the code, $d^c$ belief in the code, and $X$ tastes. Dropping the unmeasurable $d^c$ and identifying adherence with the employment rate, reputation takes the linear form $R=-ue_i(1-ue_i^*)$, so there is no reputation effect if the individual is employed ($ue_i=0$) and a penalty $1-ue_i^*$ that shrinks as others' unemployment $ue_i^*$ rises. Substituting gives the estimating equation

$$W_i = a + b_1\, ue_i + b_2\, ue_i^* + b_3\,(ue_i\, ue_i^*) + \gamma' X + e_i.$$

The theory predicts $b_1<0$, $b_2<0$, and crucially the interaction $b_3>0$: own unemployment hurts less when reference-group unemployment is high. Three reference groups define $ue_i^*$: the regional unemployment rate (by sex/region/year), partner's labor-force status, and the unemployment rate among other adults in the household.

Estimation proceeds in three layers. (1) Pooled ordered probits of the GHQ caseness score on labor-force status plus controls (income, sex, age, age$^2$, education, health, marital status, children, region, wave). (2) Fixed-effects: since no fixed-effects ordered-probit exists, the GHQ score is dichotomized at the top value (=12) and conditional fixed-effects logits remove unobserved individual heterogeneity. (3) Behavior: among prime-age males who moved employment$\to$unemployment, the within-person GHQ change is grouped into bins and entered into probits for current job search and for remaining unemployed two waves later.

## Data
British Household Panel Survey (BHPS), waves 1–7 (collected late 1991 through ~1998), restricted to labor-force-active individuals aged 16–65. This yields 39,477 observations on 9,461 individuals (2,901 present in all seven waves), including 3,148 observations on 1,870 unemployed individuals (mean unemployment rate 8.0%). The utility proxy is the GHQ-12 "caseness" score (0–12, higher = better mental well-being; Cronbach's alpha 0.89). Regional ILO unemployment rates (11 regions, from the Labour Force Survey) supply the regional norm.

## Key findings
- Own unemployment strongly lowers GHQ (ordered-probit coefficient ~$-0.43$, t≈19), even controlling for income, which is itself a weak/insignificant predictor of well-being.
- The interaction $b_3$ is positive and significant for nine of twelve own$\times$others'-unemployment estimates in the pooled probits (Table 3). Employed and unemployed well-being would equalize at a regional unemployment rate of ~24% (out of sample); the well-being cost of unemployment is ~2.5x larger in the lowest-unemployment region (4%) than the highest (16%).
- Partner and household: an unemployed/inactive partner lowers the employed's well-being but the interaction for the unemployed is positive and significant; the test $-0.512+0.287=0$ (household rate) is rejected — an unemployed person's well-being rises when another household adult becomes unemployed. Own unemployment still hurts even when all others are unemployed.
- Results are robust to individual fixed effects (panel logits), though identification relies on movers and the partner-interaction cells are small.
- Effects are sizable for men, weak/insignificant for women (the gender asymmetry is a recurrent theme). For prime-age men, an unemployed partner roughly halves the employed–unemployed gap in P(GHQ=12).
- Behavior (Table 6, prime-age males): those whose GHQ fell by more than two points on entering unemployment are more likely to be searching and are ~22% *less* likely to remain unemployed two waves later — those hurt most leave fastest. This is robust to controlling for the income change.
- Alternative explanations (shift-share/compositional sorting, benefit incentives for unemployed couples, division of household chores) are tested and rejected, strengthening the norm interpretation. A footnote distinguishes social comparison from social norm: since unemployed status lies below the norm, the two coincide, but the *negative* correlation of the employed's well-being with others' unemployment favors the norm model.

## Contribution
One of the first large-scale, direct tests of the utility (not outcome) implication of social-norm theory, providing micro-evidence for Akerlof's (1980) reputation mechanism. It supplies a psychological foundation for unemployment hysteresis and polarization distinct from correlated shocks, insider–outsider, or human-capital-depreciation accounts: a weakening employment norm reduces the well-being gain from work, dampening search. It also demonstrates the usefulness of psychological well-being measures (GHQ) as proxy-utility tools for labor economics.

## Limitations & open questions
- The behavioral analysis rests on very small samples (287 search, 238 exit observations; prime-age males only) and the search effect is only significant at 10%.
- Fixed-effects identification of the unemployment interactions relies on movers and several partner-interaction cells are tiny (e.g., 44–77 observations), leaving those terms imprecise.
- The norm/comparison effect is consistently weak or absent for women — the paper leaves the source of this gender asymmetry unexplained.
- Norms ($d^c$, beliefs in the code) are not directly measured; adherence is proxied by the realized employment rate, so the "norm" is inferred rather than observed.
- The reverse-causation reading of the exit result (those expecting to find work soon are less unhappy) is argued against but not fully ruled out.
- Identifying the *correct* reference group remains open; only region, partner, and household are tried.

## Connections
The theoretical backbone is Akerlof (1980) on social custom and Lindbeck, Nyberg & Weibull (1999) on social norms and labor supply. The proxy-utility approach builds on the happiness-economics tradition: Easterlin (1974), Clark & Oswald (1994, 1996), Blanchflower & Oswald (1998), Winkelmann & Winkelmann (1998), Frey & Stutzer (1999), Di Tella, MacCulloch & Oswald (2001), and Frank (1985) on relative income. The closest precursor on work norms is Lalive & Stutzer (2000), who proxy the work norm by referendum votes and relate it to unemployment exit. Habituation/comparison-to-past work includes Clark (1999) and Clark, Georgellis & Sanfey (2001) using GSOEP. Related household-externality and reference-group work includes Neumark & Postlewaite (1998), Clark (1996), Whelan (1994), and Woittiez & Theeuwes (1995). The hysteresis/multiple-equilibria framing connects to Pissarides (1992) (thick-market externalities) and to Darity & Goldsmith (1996) on psychological effects of unemployment.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
