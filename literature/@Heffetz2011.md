---
citekey: Heffetz2011
title: "A Test of Conspicuous Consumption: Visibility and Income Elasticities"
authors: ["Heffetz, Ori"]
year: 2011
type: journalArticle
doi: 10.1162/REST_a_00116
zotero: "zotero://select/library/items/DI9Q9Z5Y"
pdf: /Users/jesper/Zotero/storage/VE25AA87/Heffetz2011.pdf
tags: [literature]
keywords: [conspicuous-consumption, signaling, income-elasticity, expenditure-visibility, social-status, engel-curves]
topics: ["[[conspicuous-consumption-status]]"]
related: [Charles2009]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper shows that, consistent with a signaling-by-consuming model à la Veblen, income elasticities can be predicted from the visibility of consumer expenditures. We outline a stylized conspicuous consumption model where income elasticity is endogenously predicted to be higher if a good is visible and lower if it is not. We then develop a survey-based measure of expenditure visibility, ranking different expenditures by how noticeable they are to others. Finally, we show that our visibility measure predicts up to one-third of the observed variation in elasticities across consumption categories in U.S. data.

## Summary
Heffetz argues that cross-good differences in income (Engel-curve) elasticities are not just unexplained "tastes" but are partly predictable from how *socially visible* an expenditure is. He builds a stylized conspicuous-consumption model in which signaling-by-consuming endogenously turns visible goods into luxuries and invisible goods into necessities, develops a survey-based "Vindex" measuring how quickly others notice spending on a given category, and shows empirically that the Vindex explains up to roughly one-third of the variation in estimated elasticities across 29 U.S. consumption categories.

## Research question
Why do income elasticities differ across consumption categories—why is one good a necessity and another a luxury? Specifically, can the cross-expenditure variation in income elasticities be *predicted* from a measurable, non-ad-hoc feature of goods, namely their sociocultural visibility, rather than being attributed to unexplained heterogeneity in tastes?

## Method / identification
The paper combines a theoretical model, an original survey, and reduced-form regressions.

**Model.** Start from a textbook two-good Cobb-Douglas consumer with fundamental utility $f(v,w)=\beta_v\ln(v)+\beta_w\ln(w)$ under budget constraint $v+w=y$, giving constant unit elasticities (linear Engel curves, no taste differences). Following Ireland (1994), add a signaling motive: total utility is a convex combination of own fundamental utility and society's *belief* about it,
$$U=(1-a)f(v,w)+af(\hat v,\hat w),\qquad 0<a<1,$$
where $a$ indexes status sensitivity. Good $v$ is *visible* ($\hat v=v$) while $w$ is private and inferred via beliefs $\hat w(v)$; income $y$ is private but its lower support $b$ is common knowledge. Imposing a fully separating equilibrium (optimal choice given beliefs, plus correct inference $\hat w(v)=w$) yields the inverse Engel curve
$$y=\frac{1+\beta}{a+\beta}\,\beta\,v+C\,v^{-a},\qquad a>0,$$
with $C>0$ pinned down by a boundary condition at $y=b$ (the lowest type does not signal). The visible good's elasticity is
$$e_v\equiv\frac{dv}{dy}\frac{y}{v}=\left[a(1+\beta)\frac{v}{y}-\beta\right]^{-1}\!,$$
which satisfies $e_v>1$ (hence $e_w<1$ in a two-good model). So introducing signaling drives $e_v$ up and $e_w$ down—the visible good becomes a luxury, the invisible good a necessity. The result generalizes to Stone-Geary fundamental utility (Heffetz 2004).

**Visibility measure.** A national survey of 480 U.S. respondents asks how quickly they would notice another household's spending on each category, producing a visibility index (Vindex) over 29 consumption categories; relative rankings are highly stable across construction methods and demographic subsamples.

**Empirical test.** Weighted univariate OLS regressions (29 observations, weighted by consumption-category size) of estimated elasticities on the Vindex plus a constant, with robustness via leave-one-category-out "influential analysis" (522 regressions) and demographic subgroup re-estimation, plus a good/service control and a Vindex × Service interaction.

## Data
Two sources: (1) an original visibility survey of 480 U.S. respondents; (2) the U.S. Consumer Expenditure Survey (CEX), ~10,400 households (Harris and Sabelhaus 2005 extracts, 2003:3–2004:2 and 2005:1–2005:4), from which income (total-expenditure) elasticities are *nonparametrically* estimated for 29 categories covering essentially all consumer spending, for the whole population and for demographic subgroups (age, marital status, race, income quintiles).

## Key findings
- In the benchmark whole-population specification, the Vindex coefficient is positive, large, and statistically significant, with $R^2=0.18$—about one-sixth to one-fifth of cross-category elasticity variation explained by visibility alone.
- For the top three income quintiles, $R^2$ rises to 0.19–0.32 (up to roughly one-third); the visibility-elasticity link is strongest at higher incomes and weak/absent at the bottom.
- Adding a good-versus-service control and a Vindex × Service interaction raises $R^2$ to 0.40–0.48.
- Cars are the single most influential category fitting the narrative; dropping Car weakens the raw correlation but a significant relationship survives among the other 28 categories once a good/service control is included. Tobacco (Cig) is the most prominent outlier—dropping it substantially improves fit.
- Visibility rankings are remarkably stable across demographic groups (pairwise correlations among the nine indices/rankings of 0.94–1.00).

## Contribution
Provides the first direct empirical test linking a *measurable* feature of goods (sociocultural visibility) to their income elasticities, operationalizing Veblen's conspicuous consumption. Methodologically it follows the extended Stigler-Becker program—explaining behavior via measurable variables rather than "ad hoc assumptions concerning tastes." It supplies both a novel, transportable survey instrument (the Vindex) and a tractable signaling model deriving the visibility-to-elasticity mechanism, jointly explaining part of cross-good elasticity heterogeneity and offering evidence that consumption carries signaling value beyond intrinsic value.

## Limitations & open questions
The author explicitly flags several:
- **Correlation, not causation.** The design does not rule out reverse causality—high-elasticity goods might *become* more visible (e.g., because people are curious about what the rich buy, or because producers/government make luxuries salient). No test discriminates between the signaling mechanism and such alternatives.
- **Why only at the top?** The visibility-elasticity link appears mainly in upper quintiles; this could mean social effects bite only at higher (absolute or relative) income, or that smaller-than-demographic reference groups are needed to detect them lower down.
- **External validity.** Evidence is from one country, one time period, and only 29 categories; replication across settings and finer categories is needed.
- **Broader implications to test.** The result that visible budget shares grow at higher incomes suggests fads, fashions, and herd/social-learning behavior should be more important at higher incomes, and that top-driven income/wealth shocks should hit visible expenditures fastest—accelerating both downturns and recoveries. These macro/social-learning predictions are conjectural and untested here.

## Connections
The signaling architecture builds directly on Ireland (1994) on limiting markets for status signals and on Spence (1973) on job-market signaling; the conceptual roots are Veblen (1899/1965) on the leisure class and conspicuous consumption. The methodological stance follows Stigler and Becker (1977) ("De Gustibus Non Est Disputandum"). On Engel curves and elasticity estimation it draws on Working (1943), Blundell and Duncan (1998), and Lewbel (2006). The implicit taste-based alternative invokes Maslow (1943). Closely related empirical work on status consumption includes Chao and Schor (1998) on cosmetics and [[@Charles2009|Charles, Hurst, and Roussanov (2009)]] on conspicuous consumption and race (whose own survey was inspired by Heffetz's); Grinblatt, Keloharju, and Ikäheimo (2008) on neighbor automobile purchases, and Kuhn, Kooreman, Soetevent, and Kapteyn (2008) on the Dutch postcode lottery, study related social-influence-in-consumption channels. The discussed macro/social-learning extensions connect to Banerjee (1992) and Bikhchandani, Hirshleifer, and Welch (1992) on herd behavior and informational cascades, and to Frank's (1999) and Congleton's (1989) work on status competition.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
