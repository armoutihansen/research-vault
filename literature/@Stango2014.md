---
citekey: Stango2014
title: "Limited and Varying Consumer Attention: Evidence from Shocks to the Salience of Bank Overdraft Fees"
authors: ["Stango, Victor", "Zinman, Jonathan"]
year: 2014
type: journalArticle
doi: 10.1093/rfs/hhu008
zotero: "zotero://select/library/items/D2MGMFV5"
pdf: /Users/jesper/Zotero/storage/6H58PNZH/Stango2014.pdf
tags: [literature]
keywords: [limited-attention, salience, overdraft-fees, household-finance, consumer-protection, financial-literacy, reminders]
topics: ["[[behavioral-io-naivete-attention]]"]
related: [Barber2008, Eliaz2011a, Gabaix2006]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We explore dynamics of limited attention in the $35 billion market for checking overdrafts, using survey content as shocks to the salience of overdraft fees. Conditional on selection into surveys, individuals who face overdraft-related questions are less likely to incur a fee in the survey month. Taking multiple overdraft surveys builds a "stock" of attention that reduces overdrafts for up to two years. The effects are significant among consumers with lower education and financial literacy. Individuals avoid overdrafts by making fewer low-balance debit transactions and cancelling automatic recurring withdrawals. The results raise new questions about consumer financial protection policy.

## Summary
Stango and Zinman use online surveys whose *content* incidentally mentions overdraft fees as exogenous shocks to consumer attention, and trace their effect on actual overdraft incidence in linked checking-account transaction data. Merely being asked overdraft-related questions—conveying essentially no new information about one's own account terms—cuts the same-month probability of incurring an overdraft fee by ~3.7 percentage points off a 30% base. Repeated exposure builds a persistent but decaying "stock" of attention that lowers overdrafts for up to two years. Effects are largest for lower-education and lower-financial-literacy panelists, and operate by reducing low-balance debit/ACH transactions rather than by raising buffer balances.

## Research question
Does limited attention hinder individuals from acquiring and using readily available information when making financial decisions, and if so, how does consumer attention respond to shocks and evolve over time? Concretely: can salience shocks that carry no account-specific information nonetheless reduce overdraft fees, and are the effects immediate, persistent, or permanent?

## Method / identification
The unit of observation is a panelist-month. The authors define limited attention broadly as incomplete consideration of elements/prices in one's choice set (DellaVigna's 2009 taxonomy: salience affecting the effort to acquire/use information). They classify periodically administered online surveys as "generic," "overdraft-mentioning," or "overdraft-focused"; survey topics are not announced before a panelist chooses to take a survey, so within-panelist exposure to overdraft content is plausibly idiosyncratic conditional on selection into survey-taking.

The primary linear-probability estimating equation is:

$$\text{AnyOD}_{it} = \beta_1\,\text{TookOD}_{it} + \beta_2\,\text{ODSurveys\_Last2yrs}_{it} + \beta_3\,\text{TookAny}_{it} + \gamma\cdot\text{AnySurveys}_{it} + \beta_4\,\text{AnyOD}_{i,t-1} + \beta_5\,\text{Snowball}_{i,t-1} + \delta_i + \lambda_t + \varepsilon_{it}$$

where $\text{AnyOD}_{it}$ indicates at least one overdraft fee for panelist $i$ in month $t$; $\text{TookOD}_{it}$ is the immediate (click-through) effect; $\text{ODSurveys\_Last2yrs}_{it}$ is the cumulative attention "stock" (count of overdraft surveys in the past two years, incremented the month *after* taking to separate it cleanly from the immediate effect); $\text{TookAny}_{it}$ and the $\text{AnySurveys}_{it}$ indicators control for selection into and dynamics of survey-taking generally; $\delta_i$ are panelist fixed effects and $\lambda_t$ are month/year fixed effects. Estimated by OLS with standard errors clustered on panelist. Because some click-throughs do not answer questions, estimates are intent-to-treat and a lower bound on treatment-on-the-treated. Robustness includes conditional (fixed-effect) logit, Anderson–Hsiao / Arellano–Bond instruments for the lagged-dependent-variable bias, distributed-lag specifications (Figure 3) tracing onset and decay, and placebo content (auto-loan, gift-card, contactless-card questions).

## Data
Account-level panel from Lightspeed Research (formerly Forrester) "Ultimate Consumer Panel": thousands of panelists who grant access to online bank/credit accounts (incremental ~$20 enrollment payment). Up to three years (Feb-2006 to Dec-2008) of complete transaction-level statement data—every debit/credit, balance, and fee—with overdraft fees identified via text-string parsing of transaction descriptions. About 102,334 active panelist-months overall; 60,096 among ever-overdrafters (mean monthly overdraft incidence ~0.27). Survey responses provide the attention treatment plus registration-survey demographics (education for 3,675 panelists, self-assessed financial literacy for 1,852, household income for 3,634).

## Key findings
- **Immediate effect:** taking an overdraft-related survey lowers the probability of any overdraft that month by ~3.7 p.p. on a 30% base.
- **Attention stock:** cumulative overdraft surveys reduce overdrafts persistently; the distributed-lag profile (Figure 3) shows onset and slow decay, with 10 of 12 coefficients negative in each of the first and second post-survey years. Effects persist up to ~two years but are not permanent; the one- vs. two-year horizons are not statistically distinguishable.
- **Heterogeneity:** point estimates are uniformly larger for lower-education, lower/medium financial-literacy, and lower-income panelists (e.g., low-education: a two-survey panelist's overdraft probability falls 0.044 on a 0.290 base, ~15%). Equality across groups is only weakly rejected (significant only for the education stock effect).
- **Dose response by content:** the single overdraft-*focused* survey produces a stronger stock effect than surveys that merely *mention* overdrafts; balance/fee/spending-mentioning surveys also matter, while placebo content (auto loans, gift cards, contactless cards) does not—a content placebo test.
- **Mechanism:** consumers cut overdrafts by making fewer low-balance debit-card and recurring ACH transactions and cancelling autodebits—combining high- and low-frequency vigilance on transactions whose clearing balance is hard to forecast. No evidence they raise checking balances.

## Contribution
First field evidence that uninformative salience shocks—reminders carrying no consumer-specific information about account terms—causally and durably reduce a costly financial mistake, in a high-stakes $35bn market, using administrative transaction data rather than self-reports. It characterizes attention as **dynamic, associative, and malleable** (a buildable, decaying stock), distinct from classical disclosure. The policy reframing is sharp: where mandated disclosure focuses on one-shot upfront information that may only temporarily move behavior, ongoing reminders—even uninformative ones—may be a more effective or complementary instrument.

## Limitations & open questions
- **Welfare is indeterminate:** the authors explicitly decline welfare claims—they cannot say whether consumers under- or over-attend absent shocks, nor whether attention to overdrafts crowds out attention elsewhere; drawing policy welfare conclusions would be imprudent.
- **External validity:** the sample is relatively educated and online; would effects hold in more "downmarket" populations? The larger low-education/low-literacy effects may be partly mechanical (higher baseline overdraft rates), needing more work on robustness and mechanism.
- **Attention substitution:** does heightened attention on one margin (checking balances) come at a cost on another (credit-card balances)? An open empirical question flagged as future work, motivated by limited-attention findings in equity markets.
- **Attention vs. learning:** how do these salience effects compare to direct fee-paying learning effects (Agarwal et al. 2011; Haselhuhn et al. 2012)? Paying a fee last month strongly predicts paying one this month; disentangling attention from learning is left for later work.
- **Equilibrium/market design:** how would attention-reducing innovations (opt-out low-balance alerts, Mint/HelloWallet) and reminder provision by third parties reshape equilibrium contracts and pricing, and who should provide reminders?

## Connections
The paper sits at the intersection of limited-attention behavioral economics and household finance. It operationalizes DellaVigna's (2009) salience taxonomy and connects to the shrouded-attributes / consumer-myopia framework of [[@Gabaix2006|Gabaix and Laibson (2006)]] and to consideration-set models ([[@Eliaz2011a|Eliaz and Spiegler 2011]]). The reminder mechanism parallels Karlan, McConnell, Mullainathan, and Zinman's work on reminders and saving, and Bertrand et al. (2010) on advertising content. Limited-attention findings in financial markets—[[@Barber2008|Barber and Odean (2008)]], Hirshleifer–Lim–Teoh, DellaVigna and Pollet (2009)—motivate the attention-substitution conjecture, while Lacetera, Pope, and Sydnor (2012) and Kőszegi and Szeidl (2013, focusing) provide the broader inattention/salience modeling context. On policy, it engages Armstrong and Vickers (2012) on contingent charges, Grubb (2012) on bill-shock regulation, and Barr–Mullainathan–Shafir on behaviorally informed regulation and default-undoing. It builds directly on the authors' own Stango and Zinman (2009, 2011) work on avoidable overdrafts and disclosure enforcement.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
