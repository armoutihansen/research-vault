---
citekey: Bloom2015
title: Does Working from Home Work? Evidence from a Chinese Experiment
authors: ["Bloom, Nicholas", "Liang, James", "Roberts, John", "Ying, Zhichun Jenny"]
year: 2015
type: journalArticle
doi: 10.1093/qje/qju032
zotero: "zotero://select/library/items/XHHLR54Y"
pdf: /Users/jesper/Zotero/storage/3UQRRU2E/Bloom2015.pdf
tags: [literature]
keywords: [working-from-home, field-experiment, randomized-controlled-trial, productivity, management-practices, self-selection]
topics: []
related: [Lazear2000]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A rising share of employees now regularly engage in working from home (WFH), but there are concerns this can lead to "shirking from home." We report the results of a WFH experiment at Ctrip, a 16,000-employee, NASDAQ-listed Chinese travel agency. Call center employees who volunteered to WFH were randomly assigned either to work from home or in the office for nine months. Home working led to a 13% performance increase, of which 9% was from working more minutes per shift (fewer breaks and sick days) and 4% from more calls per minute (attributed to a quieter and more convenient working environment). Home workers also reported improved work satisfaction, and their attrition rate halved, but their promotion rate conditional on performance fell. Due to the success of the experiment, Ctrip rolled out the option to WFH to the whole firm and allowed the experimental employees to reselect between the home and office. Interestingly, over half of them switched, which led to the gains from WFH almost doubling to 22%. This highlights the benefits of learning and selection effects when adopting modern management practices like WFH.

## Summary
A nine-month randomized controlled trial of working from home (WFH) inside Ctrip, China's largest travel agency. Call center volunteers were randomized (by birthday parity) to four days/week at home versus all-office, holding everything else (equipment, pay, schedule, tasks) constant. WFH raised performance by 13%, halved attrition, and improved satisfaction, but lowered promotion conditional on performance. A subsequent firm-wide rollout with free reselection revealed strong learning and selection effects: over half of employees switched, and the long-run treatment effect nearly doubled to 22%.

## Research question
Is allowing employees to work from home a productivity-enhancing management practice, or does it induce shirking? More precisely: what is the causal effect of WFH on (i) individual employee performance and its components (minutes worked vs. calls per minute), (ii) quit and promotion rates and reported satisfaction, and (iii) firm profitability — and how much of the realized return comes from direct treatment versus self-selection once employees and the firm learn their type?

## Method / identification
A field randomized controlled trial. Of 996 employees in the airfare and hotel departments of Ctrip's Shanghai call center, 503 volunteered; 249 met eligibility criteria (>=6 months tenure, broadband, a private room). Random assignment used birthday parity: even-numbered birthdays worked from home four of five shifts (the fifth in-office), odd-numbered birthdays stayed in the office as controls. Only the location of work differed — IT equipment, central call-routing, tasks, schedule (set by team leader), and the flat-wage-plus-linear-performance-bonus pay scheme were identical across arms, isolating the WFH effect from bundled practices like flexible hours.

The core estimator is an intention-to-treat panel difference-in-differences with the saturated specification (equation 1):

$$\text{Employee Performance}_{i,t} = \beta\,(\text{Treat}_i \times \text{Experiment}_t) + \tau_t + \gamma_i + e_{i,t}$$

where $\text{Treat}_i$ is the treatment-group dummy (even birthday), $\text{Experiment}_t$ is a dummy for the experimental window (December 6 to August 14), $\tau_t$ is a full set of weekly time dummies (absorbing seasonal demand shocks like Chinese New Year and the 2010 World Expo), and $\gamma_i$ is a full set of individual fixed effects. The outcome is a performance $z$-score normalized within worker type using the pre-experiment mean and standard deviation, alongside logged weekly calls answered, logged calls per minute on the phone, and logged weekly minutes on the phone. The 13% performance figure decomposes into a $\sim 9\%$ minutes-worked margin and a $\sim 4\%$ calls-per-minute margin.

Several theoretical models anchor the design (Section II): the impact on firm profits, on hours/effort (via a break-choice problem whose sign is signed by an envelope-theorem argument), and on selection is shown to be theoretically ambiguous, motivating the experiment. Three robustness threats are addressed: (1) spillovers/quality — the Shanghai control group is benchmarked against similar workers at the Nan Tong call center (no performance drop), and two quality metrics show no degradation; (2) demoralization of "lottery losers" — ruled out via the Nan Tong comparison; (3) attrition bias — present but biased *downward*, so the true effect is if anything larger. The rollout phase exploits voluntary reselection to separate direct from selection effects.

## Data
Ctrip's centralized Oracle-grade database supplies daily performance and minutes-on-phone records for all airfare/hotel employees from January 1, 2010 onward, plus attrition, promotion (tracked to September 2012), and internal satisfaction/exhaustion surveys. The authors added two demographic/attitude survey waves (November 2010, August 2011), focus groups, and a mandatory post-experiment survey of 957 employees in May 2013. Estimation samples run to roughly 17,806 weekly observations on 249 eligible employees (with smaller in-experiment subsets).

## Key findings
- **Performance (equation 1):** Treatment performance rose 0.232 SD (column 1; s.e. 0.063), about a 13% increase. Decomposition: $\sim 9\%$ from more minutes worked per shift (fewer breaks, sick days, time off — attributed to convenience at home) and $\sim 4\%$ from more calls per minute (attributed to a quieter environment).
- **No quality loss and no spillovers:** two quality metrics unchanged; the Nan Tong control benchmark shows no demoralization effect.
- **Attrition and satisfaction:** home workers' quit rate fell by $\sim 50\%$; reported work satisfaction and attitudinal measures improved.
- **Promotion penalty:** conditional on performance, home workers' promotion rate fell by about 50% — an "out of sight, out of mind" cost.
- **Firm profitability:** total factor productivity rose 20–30% and the firm saved roughly \$2,000/year per home worker (about two-thirds from reduced office space).
- **Learning and selection (rollout):** when WFH was offered firm-wide with free reselection, over half of employees switched (two-thirds of controls stayed office-based citing loneliness; half of treated returned to the office — disproportionately poor home performers). Selection plus direct effects raised the long-run performance gain to 22%, nearly double the 13% direct effect — a $\sim 2{:}1$ ratio mirroring [[@Lazear2000|Lazear (2000)]]'s Safelite piece-rate study.

## Contribution
Argued to be the first randomized controlled experiment on working from home, and an unusually clean within-firm RCT (privileged access via coauthor and Ctrip cofounder James Liang). It supplies causal evidence where prior WFH research was largely case studies and cross-sectional surveys, decomposes the productivity gain into interpretable margins, and — by following workers through the post-experiment rollout — quantifies the role of learning and selection in the adoption of modern management practices, connecting WFH to the broader literature on why productivity-enhancing practices diffuse slowly.

## Limitations & open questions
- **External validity:** the sample is call center workers (lower-paid, $\sim$half performance pay, measurable output); direct performance implications may not transfer to professional or team-based jobs.
- **Promotion mechanism:** why promotion falls conditional on performance (reduced face time / manager visibility) is documented but not structurally identified.
- **Short-run modeling assumptions:** wages, prices, skill levels, and access to new labor markets (e.g., suburban workers, parents) are held fixed; longer-run general-equilibrium effects are explicitly left open.
- **Loneliness/social value of the office:** the large share returning to the office despite commute savings suggests a high value on workplace social interaction that the study measures only indirectly.
- **Team/overtime constraints:** individuals could not work overtime independently, so the design cannot speak to flexible-hours WFH variants.

## Connections
The selection-versus-treatment decomposition directly parallels [[@Lazear2000|Lazear (2000)]] on piece-rate pay at Safelite, with a similar 2:1 selection-plus-incentive to direct-effect ratio. The slow-diffusion-of-practices framing draws on Griliches (1957) on hybrid seed corn and the management-and-productivity literature (Bloom & Van Reenen 2007; Bloom et al. 2013; Syverson 2011; Gibbons & Henderson 2013; Leibenstein 1966). The work-life-balance RCT by Kelly et al. (2014) is the closest experimental antecedent. Call center performance and monitoring connect to Nagin et al. (2002) on rational cheating and Batt et al. (2004). Urban/IT-fragmentation links go to Bento et al. (2005), Rossi-Hansberg, Sarte & Owens (2009), and Glaeser (2013); the value of workplace social interaction echoes Hamermesh (1990).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
