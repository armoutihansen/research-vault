---
citekey: Charles2009
title: Conspicuous Consumption and Race
authors: ["Charles, Kerwin Kofi", "Hurst, Erik", "Roussanov, Nikolai"]
year: 2009
type: journalArticle
doi: 10.1162/qjec.2009.124.2.425
zotero: "zotero://select/library/items/ETCBBYHC"
pdf: /Users/jesper/Zotero/storage/RUZ33S7L/Charles2009.pdf
tags: [literature]
keywords: [conspicuous-consumption, status-signaling, reference-group, racial-consumption-gaps, permanent-income, veblen-goods]
topics: ["[[conspicuous-consumption-status]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Using nationally representative data on consumption, we show that Blacks and Hispanics devote larger shares of their expenditure bundles to visible goods (clothing, jewelry, and cars) than do comparable Whites. These differences exist among virtually all subpopulations, are relatively constant over time, and are economically large. Although racial differences in utility preference parameters might account for a portion of these consumption differences, we emphasize instead a model of status seeking in which conspicuous consumption is used as a costly indicator of a household's economic position. Using merged data on race- and state-level income, we demonstrate that a key prediction of the status-signaling model—that visible consumption should be declining in reference group income—is strongly borne out in the data for each racial group. Moreover, we show that accounting for differences in reference group income characteristics explains most of the racial difference in visible consumption.

## Summary

Charles, Hurst, and Roussanov document that Black and Hispanic U.S. households spend roughly 25-30% more on "visible" goods (apparel, jewelry, personal care, cars) than otherwise-similar White households at the same permanent income, while consuming less of nearly everything else. Rather than attributing this to racial taste differences (which they argue is tautological and unfalsifiable), they explain it with a Spence-style signaling model in which conspicuous consumption is a costly signal of unobserved income, and the equilibrium signal depends on the income distribution of one's reference group. The model's sharp prediction — visible spending falls as reference-group mean income rises — holds both across and within races, and controlling for race/state reference-group income characteristics explains away most of the racial gap.

## Research question

Do racial differences in conspicuous (visible) consumption exist in nationally representative data after conditioning on permanent income; what accounts for them; and can a status-signaling model with identical preferences across races (rather than racial taste differences) explain both the cross-race gaps and the within-race correlation between visible spending and reference-group income?

## Method / identification

The empirical core is a regression of log visible expenditures on race indicators and a permanent-income proxy:
$$\ln(\text{visible}_i) = \beta_0 + \beta_1 \text{Black}_i + \beta_2 \text{Hispanic}_i + \varphi \ln(\text{Total Expenditure})_i + \theta X_i + \eta_i.$$
Because CEX income data are poor (missing for 27% of the sample; racial income gaps inconsistent with the CPS), the authors invoke the Permanent Income Hypothesis to use log total expenditure as a permanent-income proxy. Since total expenditure is endogenous to and shares measurement error with any expenditure component, they instrument $\ln(\text{Total Expenditure})_i$ with a vector of current/permanent income controls (log current income, a cubic in income, education, one-digit industry and occupation), reporting very large first-stage F-statistics. Standard errors are clustered at the state level.

The theory is a separating signaling model. Agents in group $k$ have income $y_i^k$ drawn from a known distribution; income finances observed consumption $c$ and unobserved residual $(y-c)$. Utility is
$$v(y_i^k - c_i^k) + u(c_i^k) + w(s_i^k),$$
with $u,v,w$ concave and twice differentiable, and status $s_i^k = E[y_i^k \mid c_i^{k*}, k]$. In the fully revealing separating equilibrium beliefs are correct, $s_i(c_i^{k*}(y_i^k)) = y_i^k$. The framework follows Glazer and Konrad (1996).

To test reference-group predictions, the authors merge CPS-based mean and dispersion (coefficient of variation) of income for each race/state cell into the CEX and estimate
$$\ln(\text{visible}_{ik}) = \beta_0 + \delta_1 \mu_k^y + \delta_2 D_k^y + \varphi \text{Expenditure}_i + \theta X_i + \eta_i,$$
run separately by race, with reference-group income measured from CPS (male labor income of the race/state cell). Falsification tests relate visible spending to other groups' incomes and relate nonvisible spending to own-reference income; state fixed effects absorb generic regional propensities.

## Data

Primary: Consumer Expenditure Survey (CEX), 1986-2002, NBER family extracts (Harris-Sabelhaus categories); 49,363 households (37,289 White, 6,766 Black, 5,308 Hispanic), heads aged 18-49, unit of analysis = average quarterly expenditure. Reference-group incomes from the Current Population Survey (CPS). Corroboration from the 2005 Panel Study of Income Dynamics (PSID), which has high-quality multi-year income (permanent income = average family income 1999-2005) but limited consumption detail (mainly clothing and recent car price). A 320-respondent online survey of University of Chicago students validates which goods are "visible."

## Key findings

- After proxying for permanent income, Blacks and Hispanics spend about 26% and 23% more on visible goods than comparable Whites (preferred IV specification, Table II row 6). Unconditionally they appear to spend less, because visible goods are luxuries (Engel-curve slope $\approx 1.5$) and minorities have lower incomes. The absolute gap is roughly \$1,900/year, a lower bound given CEX underreporting.
- Gaps hold across nearly all subgroups (single men, single women, married; all education levels) and are stable over 17 years, but decline sharply with age (30% at 18-34, 23% at 35-49, 15% at 50-69).
- The higher visible spending is financed by lower spending on essentially every other category — education (-16%), entertainment (-29%), health (-50%), and on saving — except housing/utilities.
- PSID replicates the CEX: Blacks spend 24% more on clothing and buy cars 12% more expensive, with similar negative gaps in food, entertainment, transportation.
- Signaling model results: equilibrium $c_i^{k*}$ is strictly increasing in own income $y_i$; the poorest person signals nothing beyond the no-signaling level; the effect of greater income dispersion is theoretically ambiguous; but adding poorer people to a group (lowering mean income) unambiguously raises visible spending at every income level.
- The central prediction holds: visible spending falls strongly in reference-group mean income within each race. For Whites, $\delta_1 \approx -0.60$ (doubling state mean White income cuts White visible spending ~60%). Falsification tests pass — other groups' incomes have null/tiny effects, and nonvisible spending is unrelated to reference income.
- Controlling for race/state reference-group mean (and dispersion) income causes the Black and Hispanic visible-spending gaps to vanish; state fixed effects show it is the racial reference group's income, not a generic state trait, that drives the result.

## Contribution

The paper provides the first systematic, nationally representative documentation of racial differences in conspicuous consumption conditional on permanent income, and shows these can be rationalized without invoking racial preference differences. It operationalizes the abstract "reference group" of status-signaling theory using observable race/state income distributions, turning a long-discussed but rarely tested idea (Veblen 1899; Smith 1759) into testable, confirmed predictions, and links consumption behavior directly to social/relative-position concerns rather than relying on subjective-well-being evidence.

## Limitations & open questions

- Reference-group income is not exogenously assigned; lacking instruments for location, the authors cannot fully rule out sorting (e.g., high-discount-rate individuals selecting into high-mean-income states), though tobacco/alcohol and nonvisible-spending patterns argue against it.
- Results do not rule out that racial differences in utility parameters operate alongside the identified signaling channel.
- The race/state cell is a coarse reference group dictated by CEX spatial resolution; finer interactions (friends, family) may use different reference groups and different visible goods (home furnishings, children's education).
- Open avenues the authors flag: which specific conspicuous goods matter in which social contexts; whether people choose neighbors with status considerations in mind; and policy implications for wealth/savings gaps and for status-driven spending (e.g., weddings, recent immigrants).

## Connections

The signaling framework adapts Spence (1973) and is, the authors note, nearly identical to Glazer and Konrad (1996) on observable charitable donations, with formal antecedents in Mailath (1987) and Ireland (1994); related conspicuous-consumption signaling appears in Bagwell and Bernheim (1996). The relative-consumption alternative traces to Duesenberry (1949). The permanent-income proxying rests on Modigliani and Brumberg (1954) and Friedman (1957). Empirical relative-position and well-being work includes Clark and Oswald (1996), McBride (2001), Luttmer (2005), and the survey by Kahneman and Krueger (2006); Ravina (2007) and Kuhn et al. (2008) are recent exceptions studying visible/relative consumption directly. The conceptual roots are Veblen (1899) and Smith (1759), with an early racial-consumption precedent in Alexis (1970). Policy-relevant status-spending applications include Bloch, Rao, and Desai (2004) on Indian weddings.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
