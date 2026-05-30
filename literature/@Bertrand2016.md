---
citekey: Bertrand2016
title: Trickle-Down Consumption
authors: ["Bertrand, Marianne", "Morse, Adair"]
year: 2016
type: journalArticle
doi: 10.1162/REST_a_00613
zotero: "zotero://select/library/items/UZQYYRRV"
pdf: /Users/jesper/Zotero/storage/4HZFBX7D/Bertrand2016.pdf
tags: [literature]
keywords: [income-inequality, conspicuous-consumption, expenditure-cascades, household-saving, status-seeking, relative-income]
topics: []
related: [Charles2009, Frank2014, Heffetz2011, Kuziemko2014]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We document that nonrich households consume a larger share of their current income when exposed to higher top income and consumption levels. Permanent income, wealth effects, and upward local price pressures cannot provide the sole explanation for this finding. Instead, we show that the budget shares that nonrich households allocate to more visible goods and services rise with top income levels, consistent with status-maintaining explanations for our primary finding. Nonrich households might have saved up to 3% more annually by the mid-2000s had incomes at the top grown at the same rate as median income since the early 1980s.

## Summary
Using U.S. micro consumption data 1980-2008, Bertrand and Morse show that "nonrich" households (below the 80th income percentile in their state-year) spend a larger share of current income when the rich in their state get richer. They rule out a battery of noncausal explanations (permanent income, precautionary saving, wealth effects, local price pressure) and find that the extra spending concentrates in *more visible* consumption categories, consistent with status-driven "trickle-down consumption" / expenditure cascades. A counterfactual implies the savings rate of the nonrich would have been roughly 2-3 percentage points higher by the mid-2000s had top incomes grown at the median rate.

## Research question
Are the secular rise in U.S. income inequality and the secular decline in the personal savings rate causally linked? Specifically: does exposure to higher local top incomes lead nonrich households to consume more out of current income, and if so, through what mechanism (rational permanent-income updating, wealth effects, price effects, or social comparison)?

## Method / identification
The core specification is an OLS regression on the cross-sectional CEX sample of nonrich households,
$$\text{Log(Consumption)}_{ist} = \beta\,\text{Log(80thPercentileIncome)}_{st} + X_{ist} + \text{IncomeFE}_{ist} + \alpha_s + \delta_t + \varepsilon_{ist},$$
where $i$ indexes households, $s$ states, $t$ years. The key regressor is the log 80th- (or 90th-) percentile state income, three-year averaged over $t,t-1,t-2$ (motivated by a lagged behavioral response). Controls include state and year fixed effects, state-specific time trends, a flexible income control ($2{,}000 income-bucket dummies), and sociodemographics; standard errors clustered at the state level, observations CEX-weighted.

Because there is no clean instrument for top-income variation, identification of a *causal* channel is indirect: the authors test and reject candidate noncausal stories one by one, then show the *composition* of the spending response matches a social-comparison mechanism. Specific tests:
- Permanent income / precautionary saving: in the PSID panel they regress future log family income (at $t{+}1,t{+}2,t{+}4$) on current income plus log top-percentile income (eq. 2); they also regress self-reported income expectations from the Michigan Surveys of Consumers on top income (eq. 3), and regress the standard deviation of future log income on top income.
- Wealth/home-equity effects: re-estimate eq. (1) separately for homeowners vs. renters, and interact with the post-1995 housing-boom subperiod.
- Local price pressure: regress local CPI on top income, then re-estimate eq. (1) controlling for log local CPI (overall and disaggregated into food, shelter, apparel, transportation, medical), both OLS and IV; supplement with Handbury-Weinstein "exact" price indices.
- Rich-vs-nonrich consumption link: an IV specification instruments $\text{Log(ConsumptionofRich)}$ and $\text{Log(ConsumptionofVeryRich)}$ with the 80th/95th-percentile income thresholds, addressing both unobserved state shocks and CEX measurement error in rich consumption.
- Mechanism (visibility vs. income elasticity): a demand-system regression of each category's budget share $x_{kist}$ ($k=1\dots15$) on instrumented rich consumption (with national CPI $P_t$, local CPI $p_{st}$, household controls, state/year FE, state trend; eq. 4). The estimated category coefficients $\beta_k$, scaled by mean budget share, are then plotted against Heffetz's (2011) visibility score and against estimated income elasticity to see which dimension organizes the response.

## Data
- **Consumer Expenditure Survey (CEX) Interview Survey, 1980-2008** (primary): annual household consumption built by summing four quarterly surveys; service-flow measures for vehicles (accelerated depreciation, ~15% of prior-year value) and shelter (payment-flow default, rental-equivalence alternative); excludes home/vehicle purchases. ~77,500 nonrich household-year observations; covers 44 states plus DC (six sparsely sampled states missing). Categories follow [[@Charles2009|Charles et al. (2009)]], expanded to 15.
- **March CPS** for state-year income-distribution percentiles (20th/50th/80th/90th/95th), used to classify CEX households as nonrich/rich/very rich.
- **PSID 1980-2007** for the future-income (permanent-income / precautionary) tests.
- **University of Michigan Surveys of Consumers** for income-growth expectations and the Index of Consumer Expectations.
- **BLS local CPIs**, **[[@Heffetz2011|Heffetz (2011)]]** visibility scores, **Chetty et al. (2014)** income-segregation measures, and **NIPA / Census** for the aggregate counterfactual.

## Key findings
- **Primary result (Table 1):** a 1% rise in the 80th-percentile state income is associated with a ~0.27% rise in nonrich consumption (0.345 with state trends and unemployment controls), holding own income and characteristics fixed; equivalently a 10% rise in the 80th percentile maps to ~3% higher nonrich consumption. The effect is robust across decades (weaker in the 2000s), state subsets, and to dropping households above the 60th percentile (ruling out misclassification). Median (50th) and bottom (20th) income show no such association, and rich consumption is not symmetrically driven by nonrich income.
- **Rich-consumption IV (Table 2):** a 10% increase in *rich consumption* is associated with ~4.4% higher nonrich consumption; positive and significant across consumption-level and consumption-to-income-ratio outcomes.
- **Permanent income / precautionary saving rejected (Tables 3-4):** top income today does not predict higher (or more stable) future income for the nonrich—most point estimates are negative—and self-reported income expectations and consumer-expectation indices are, if anything, *negatively* related to local top income.
- **Wealth effects rejected (Table 5):** sensitivities are if anything larger for renters than homeowners, and not concentrated in the post-1995 housing boom.
- **Price pressure partial (Table 6):** top income does raise local CPI (coefficient ~0.54), but controlling for local prices leaves the consumption-top-income relationship essentially intact; prices are not the sole explanation, though shelter stickiness may contribute.
- **Mechanism = visibility (demand system, Fig. 1):** the budget-share response sorts strongly on *visibility*, not income elasticity. Fitted line: visibility $= 0.534 + 0.194\times(\text{scaled response})$, versus a flat, insignificant relation for income elasticity. Food away from home, shelter, personal care, and clothing/jewelry rise most; utilities and some other nondurables fall. Vehicles are a notable null/outlier despite high visibility. The response is stronger where "segregation of affluence" is lower (coefficient 0.472 vs. 0.213), consistent with an exposure-based status channel.
- **Counterfactual (Table 7):** had top incomes grown at the median rate since 1982, nonrich consumption would have been ~2.7-3.2% lower by 2005 (~$1,763-$2,116 per household), raising the counterfactual personal savings rate from an actual 1.5% to ~3.5-3.9%.

## Contribution
Provides large-sample, within-market empirical evidence for "trickle-down consumption"—that local top-income growth depresses nonrich saving via status-driven spending—operationalizing Veblen/Duesenberry conspicuous-consumption and Frank-Levine-Dijk expenditure-cascade theory through the visibility gradient of budget shares. It links rising inequality directly to the falling personal savings rate, and (in the online appendix) to personal bankruptcies, self-reported financial duress, and the political economy of credit expansion.

## Limitations & open questions
- **No instrument / indirect causal inference:** the authors explicitly cannot rule out an omitted time-varying state factor that jointly raises top incomes and nonrich consumption; causality rests on rejecting alternatives plus the composition evidence.
- **Geographic coarseness:** the state is the finest CEX geographic unit, preventing analysis of the finer neighborhood dynamics that expenditure cascades likely operate through; they call for finding "naturally occurring experiments" at finer geography.
- **CEX measurement error:** systematic and growing underreporting of consumption by the rich biases rich/very-rich consumption levels downward.
- **The vehicle anomaly:** high-visibility vehicles show no response, inconsistent with prior "keeping up with the Joneses" car evidence and only partly explained by slow adjustment.
- **Suggested future work:** lab/experimental settings on relative-position effects (citing [[@Kuziemko2014|Kuziemko et al., 2014]]); systematic study of the political economy of credit expansion and its relation to top-income growth; and how lenders responded to local inequality. The credit, bankruptcy, and HR 5334 voting evidence is flagged as "admittedly preliminary."

## Connections
The paper sits at the intersection of consumption theory and inequality. It tests and rejects Friedman's (1957) permanent income hypothesis and Carroll's (1992) precautionary-saving motive as explanations, and pushes against the Mian-Sufi (2011) home-equity wealth-effect channel. Its positive interpretation revives Veblen (1899) and Duesenberry (1949) relative-income/conspicuous-consumption ideas, and most directly operationalizes [[@Frank2014|Frank, Levine, and Dijk (2014)]] "expenditure cascades," distinguishing it from the Luttmer (2005) "keeping up with the Joneses" formulation by emphasizing comparisons *up* the distribution rather than to peers. The visibility measurement builds on [[@Heffetz2011|Heffetz (2011)]] and [[@Charles2009|Charles, Hurst, and Roussanov (2009)]]; measurement issues draw on Aguiar and Bils (2015). The aggregate-saving and credit-supply narrative connects to Rajan (2010) on inequality-driven credit expansion and to the broader literature on the determinants of the U.S. saving-rate decline.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
