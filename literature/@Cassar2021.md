---
citekey: Cassar2021
title: "Intentions for Doing Good Matter for Doing Well: The Negative Effects of Prosocial Incentives"
authors: ["Cassar, Lea", "Meier, Stephan"]
year: 2021
type: journalArticle
doi: 10.1093/ej/ueaa136
zotero: "zotero://select/library/items/XYYATTZE"
pdf: /Users/jesper/Zotero/storage/DM8NRHLX/Cassar and Meier - 2021 - Intentions for Doing Good Matter for Doing Well The Negative Effects of Prosocial Incentives.pdf
tags: [literature]
keywords: [prosocial-incentives, reciprocity, corporate-social-responsibility, field-experiment, worker-motivation, intentions-and-motives]
topics: ["[[prosocial-behavior-image-signaling]]"]
related: [Akerlof1982, Benabou2010, Bolton2000, Cassar2018, Dufwenberg2004, Ellingsen2008, Falk2006, Fehr1993, Fehr1999, Gneezy2000, Rabin1993, vonSiemens2013]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Many firms consider prosocial initiatives to be an effective tool to motivate workers. However, despite some initial supportive evidence, little is known about when and how prosocial incentives work. Our field experiment shows that the instrumental use of prosocial incentives to increase effort can backfire. The negative effect is particularly strong for performance-based prosocial incentives, which are, by construction, more instrumental than unconditional incentives, and for the workers who do not care about the charitable cause. These findings highlight some serious limitations of prosocial incentives: firms' perceived intentions and the pool of employees will be crucial for their effectiveness.

## Summary
A field experiment with ~3,000 Amazon Mechanical Turk workers, run for a real Italian pharmaceutical firm, shows that prosocial (charitable-donation) incentives used instrumentally to extract effort can backfire. Whereas making a private monetary bonus performance-based raises effort, making an equally sized charitable donation performance-based does not help and if anything reduces effort. The mechanism is reciprocity: conditioning the donation on performance signals that the employer's motive is to profit, which is perceived as less kind, depressing reciprocal effort, especially among workers who do not care about the charity. Even unconditional charitable incentives can backfire relative to no incentive.

## Research question
When and why do prosocial incentives (charitable donations tied to work) motivate or demotivate workers? Specifically, does the instrumental nature of how a prosocial incentive is structured, performance-based versus unconditional, alter workers' perception of the employer's intentions/motives and thereby their reciprocal effort, and does this depend on whether workers care about the cause?

## Method / identification
A pre-registered (AEARCTR-0001962) between-subjects field experiment with a $2\times2$ core design crossing the nature of the incentive (private monetary bonus vs. charitable donation, both 75 cents) with whether it is performance-based (conditional on creating $\ge 3$ extra slogans) or unconditional. A baseline with no extra incentive and explanation/no-explanation variants (cheap-talk justifications) give nine treatments total. Workers create marketing slogans; the firm pays a $1.50 base wage.

The behavioural prediction comes from a reciprocity model. The agent's utility is
$$U_a = w + b + \theta d + k^p(b,d)\,\Phi(e) - C(e),$$
where $w$ is the wage, $b$ a monetary bonus, $d$ a charitable donation, $\theta \in [0,1)$ the agent's heterogeneous charity motivation, $C(e)$ the convex cost of effort, $\Phi(e)$ an increasing reciprocity term, and $k^p \in [-1,1]$ the perceived kindness of the employer's action. The key assumption is that performance-based incentives are perceived as more instrumental and hence less kind: $k^p_{\mid d=d(e)} < k^p_{\mid d=\bar d}$ and $k^p_{\mid b=b(e)} < k^p_{\mid b=\bar b}$. Comparing the first-order conditions under unconditional vs. conditional donations, $k^p_{\mid d=\bar d}\Phi'(e^*) = C'(e^*)$ versus $\theta d'(e^*)\Phi'(e^*) + k^p_{\mid d=d(e)}\Phi'(e^*) = C'(e^*)$, yields three predictions: (P1) performance-based charitable incentives reduce effort of self-oriented agents ($\theta \approx 0$) vs. unconditional; (P2) this difference is less negative or positive for charity-oriented ($\theta > 0$) agents; (P3) the effort gain from making incentives performance-based is larger for monetary than charitable incentives (since $\theta < 1$). Outcomes are the proportion creating more than three slogans (extensive margin) and slogan count (intensive margin). Comparisons use Mann-Whitney tests and OLS regressions with a charitable $\times$ conditional interaction. A separate 2020 third-party survey (401 M-Turkers) elicits perceived motive and kindness to validate the mechanism.

## Data
Original field-experimental data: 3,004 treated M-Turk workers (2,719 completers, 50.7% female), collected over under two days in January 2017. Charity motivation elicited via self-reported donating/volunteering frequency, used to split workers into roughly equal "self-oriented" (1,329) and "charity-oriented" (1,390) groups. Plus a 401-respondent follow-up perception survey.

## Key findings
Making a monetary incentive performance-based raises the share creating more than three slogans by about 11-13 pp ($p<0.01$) and slogan count by ~11%. Making the charitable donation performance-based instead lowers the share from 54% to 49% ($p=0.10$), marginally backfiring; the charitable $\times$ conditional interaction is highly significant ($p<0.01$), confirming P3. For self-oriented workers the performance-based donation clearly backfires (share down ~11 pp, $p<0.01$); for charity-oriented workers the effect is only marginally positive, confirming P1 and P2. Against the no-incentive baseline, monetary incentives raise effort (+23 pp conditional, +9 pp unconditional, both $p<0.01$), but charitable incentives reduce it (−12 pp conditional $p<0.01$; −8 pp unconditional $p<0.05$), so even unconditional prosocial incentives can backfire. Differential attrition reinforces the story: attrition is lowest for unconditional monetary bonuses (7.0%) and highest for conditional charitable incentives (12.8%). The third-party survey confirms the two-step mechanism: conditional donations are perceived as more instrumental and less kind, with a Spearman correlation of 0.75 ($p=0.00$) between perceived instrumentality and perceived unkindness. Cheap-talk explanations have no effect.

## Contribution
Documents previously unknown limits and negative effects of prosocial incentives, showing they operate not only via prosocial motivation but via workers' perceptions of the employer's intentions/motives and hence reciprocity. Provides field evidence that intentions and motives, not just kindness of outcomes, matter for reciprocal behaviour, complementing lab-based intention-based reciprocity models. Extends the literature on detrimental effects of monetary incentives by showing non-monetary incentives can be even more fragile, while using monetary incentives as a within-experiment benchmark to control for control-aversion. Informs the CSR-as-HR-tool literature: instrumental CSR can be worse than ineffective and the employee pool matters.

## Limitations & open questions
The authors flag: (i) results depend on specific parameters, base pay was generous relative to M-Turk norms (which itself triggered baseline reciprocity, making no incentive non-profitable for the firm); (ii) it is a one-shot setting abstracting from employer behaviour and repeated interaction, so it is not an equilibrium analysis and worker beliefs may be off-path, though they note signalling (Ellingsen and Johannesson, 2008) or intention-based (von Siemens, 2013) models could rationalise it; (iii) reverse causality in the self/charity-oriented split, since working hard to generate a donation could raise self-reported giving; (iv) alternative explanations and slogan-quality concerns. Open hooks: building the equilibrium/signalling model; testing in repeated employment relationships; mapping how the employee pool's composition should govern whether firms adopt performance-based prosocial incentives.

## Connections
Builds on intention-based and motive-based reciprocity theory: [[@Rabin1993|Rabin (1993)]], [[@Dufwenberg2004|Dufwenberg and Kirchsteiger (2004)]], [[@Falk2006|Falk and Fischbacher (2006)]], and especially Sobel (2005), Cabral et al. (2014), Johnsen and Kvaloy (2016), and Orhun (2018). Uses [[@Fehr1999|Fehr and Schmidt (1999)]] and [[@Bolton2000|Bolton and Ockenfels (2000)]] as the distributional benchmark of reciprocity. Theoretically related to von [[@vonSiemens2013|Siemens (2013)]] and [[@Ellingsen2008|Ellingsen and Johannesson (2008)]] on signalling and control. On prosocial incentives it contrasts with the largely positive findings of Tonin and Vlassopoulos (2015), Imas (2014), Charness et al. (2014), Gerhards (2015), DellaVigna and Pope (2016), and Cassar (2017a), aligning instead with the negative results of Fehrler and Kosfeld (2014) and List and Momeni (2020). On detrimental incentive effects it draws on [[@Gneezy2000|Gneezy and Rustichini (2000)]], Gneezy and Rey-Biel (2014), Falk and Kosfeld (2006), and the review by Gneezy, Meier and Rey-Biel (2011). On gift exchange it connects to [[@Akerlof1982|Akerlof (1982)]], [[@Fehr1993|Fehr et al. (1993)]], Gneezy and List (2006), and Esteves-Sorenson (2017). On CSR motives and disclosure see Bénabou and [[@Benabou2010|Tirole (2010)]], Cassar (2017b), Carlos and Lewis (2017), Newman and Cain (2014), and the review by [[@Cassar2018|Cassar and Meier (2018)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
