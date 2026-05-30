---
citekey: Isler2023
title: Scarcity improves economic valuations when cognitively salient
authors: ["Isler, Ozan", "Yilmaz, Onurcan", "Dulleck, Uwe"]
year: 2023
type: journalArticle
doi: 10.1016/j.jebo.2023.02.019
zotero: "zotero://select/library/items/PBZ8FEWK"
pdf: /Users/jesper/Zotero/storage/PQSY27TD/Isler2023.pdf
tags: [literature]
keywords: [scarcity, context-effects, replication, willingness-to-pay, behavioral-economics, rational-choice, cognitive-salience]
topics: []
related: [Kahneman1979, Tversky1974, Tversky1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In an influential article, Shah et al. (2015) hypothesized that resource scarcity weakens the effect of irrelevant contextual factors on economic valuations. The hypothesis that "scarcity frames value" qualifies the applicability of standard theories of rational choice and suggests a revised psychological foundation. In support, Shah et al. showed that differences in the willingness to pay for a commodity depending on where it was purchased (a fancy hotel vs. a run-down store) and in the willingness to travel to receive a fixed discount depending on the size of the purchase (a cheap vs. an expensive computer) were smaller among those with low personal incomes. In a large-scale preregistered experiment (N = 3,442), we tested whether scarcity framed value during the COVID-19 pandemic as well. The sample exhibited the canonical context effects overall. Consistent with the hypothesis, these effects tended to be smaller among those facing higher scarcity of personal income. Extending the original findings, economic valuations of low-income earners improved, particularly when scarcity was on the minds of the participants, as those with high financial and other resource scarcity concerns were less susceptible to the context effects. Our findings indicate that scarcity frames value, especially when it is cognitively salient, and emphasize the importance of considering contextual factors when attempting replications.

## Summary
A large preregistered ($N=3{,}442$) independent replication-and-extension of Shah, Shafir & Mullainathan's (2015) "scarcity frames value" hypothesis, conducted on Prolific during the late COVID-19 pandemic (March 2022). The canonical context effects (transaction-utility in the beer-on-the-beach task; proportional thinking in the willingness-to-travel task) replicated strongly overall, but the preregistered test that *income* scarcity moderates them was directionally right yet statistically null. The novel finding comes from preregistered exploratory analysis: context effects shrank when scarcity was *cognitively salient* — participants high in financial concerns and COVID-19 resource-scarcity threat perceptions (especially within the low-income group) made more context-stable valuations. The authors reframe "scarcity frames value" as conditional on the subjective salience of scarcity at the moment of choice.

## Research question
Does resource scarcity improve economic valuations by reducing the influence of normatively irrelevant contextual features — and is it objective income scarcity or the *cognitive salience* of scarcity that does the framing? Concretely, do the canonical context effects (WTP gap between a fancy resort vs. run-down store; WTT gap across discounted-item prices) shrink for lower-income / higher-scarcity-concern individuals?

## Method / identification
Online survey experiment closely re-implementing two key studies from Shah et al. (2015) — Study 1d (beer-on-the-beach, WTP) and Study 2c (proportional thinking, WTT) — identified in consultation with the original corresponding author (A. K. Shah) as the critical hypothesis-testing studies. Each subject completed both scenarios in counterbalanced order, then a demographic survey, a financial-concerns scale (5 items, Kim & Garman 2003), a two-item COVID-19 resource-scarcity and health-threat-perception measure (0–100), and a 5-item financial-literacy test.

Design and elicitation:
- **Beer-on-the-beach (Thaler 1985):** between-subjects, two conditions ("fancy resort hotel" vs. "small, run-down grocery store"); WTP elicited open-ended. The transaction-utility effect predicts higher WTP in the hotel condition.
- **Proportional thinking ([[@Tversky1981|Tversky & Kahneman 1981]]):** three price conditions for a tablet ($300, $500, $1000) with a fixed $50 discount thirty minutes away; binary WTT outcome. Effect predicts WTT falls as base price rises (proportionally smaller discount).

Identification is **correlational/observational on income** (scarcity is not manipulated; only the context condition is randomized). Personal income computed as the OECD equivalence transformation: income-bin midpoint divided by $\sqrt{\text{household size}}$.

Estimators (preregistered): for H1, two-way ANOVA on WTP testing the income $\times$ context interaction; for H2, Wald tests on the income $\times$ context interaction in binary logistic regressions on WTT. Each hypothesis tested twice — median-split income groups and continuous log-income. Significant interactions in the direction "WTP/WTT gaps increase with income" would support the hypotheses. Power analysis (G*Power, $\alpha=0.05$, $1-\beta=0.90$) targeted the smaller original interaction effect ($\eta_p^2=0.003$), requiring $\geq 3{,}494$ participants. Quota sampling across 8 subgroups (income $\times$ household size $\times$ gender) matched the original sample's demographics. Outliers (personal income $<\$2{,}440$ or WTP $>\$24$, inflation-adjusted from the original thresholds) were excluded.

## Data
Primary: 3,442 complete, unique submissions from US residents recruited on Prolific (Mage = 36.91, 53.8% female), quota-matched to Shah et al. (2015) on household income, household size, and gender. Median household income ($55,000) and mean household size (2.73) closely matched the original. Materials, data, and analysis code preregistered and posted on OSF (osf.io/xuc9m; osf.io/kdfjn).

## Key findings
- **Canonical context effects replicated strongly.** Beer-on-the-beach: WTP $\$1.03$ higher from the resort ($7.72$) than the store ($6.69$); $t(3440)=7.90$, $p<.001$, $d=0.27$ — almost identical to Shah et al. after 19% inflation adjustment. Proportional thinking: WTT fell 22.3 pp across prices (76.8% / 69.7% / 54.5% for \$300/\$500/\$1000); $\chi^2(2)=135.47$, $p<.001$.
- **Preregistered income-moderation (H1, H2) NOT supported.** Effects were directionally smaller for lower-income participants but interactions were null: beer $F(1,3438)=0.69$, $p=.408$ (median split) and $p=.313$ (continuous); travel $\chi^2(1)=0.28$, $p=.596$ (median split) and $p=.114$ (continuous).
- **Cognitive-salience extension (exploratory) supported.** Context effects were significantly weaker for participants with above-median financial concerns (beer interaction $F(1,3438)=4.27$, $p=.039$) and above-median COVID-19 threat perceptions (beer $F=7.63$, $p=.006$; travel $\chi^2(1)=8.95$, $p=.003$). The moderation was concentrated in the low-income group; within it, resource-scarcity threat perceptions improved valuations in both tasks.
- **Financial literacy moderated in the *opposite* direction:** higher literacy *increased* context effects (beer $d=0.44$ vs. $0.09$, $F=19.03$, $p<.001$), most pronounced among the low-income. Literacy was positively correlated with income ($r=.23$) and negatively with financial concerns and threat perceptions ($r=-.15$ each), confounding the surface relationship; the authors speculate low-literacy reliance on heuristics may yield more context-stable choices.

## Contribution
First high-powered, preregistered *independent* test of the two studies the original authors deem critical to "scarcity frames value," addressing the scarce and conflicting prior replication record (O'Donnell et al. 2021; Camerer et al. 2018). It refines the hypothesis: objective income scarcity alone did not reliably frame value during the pandemic, but the *cognitive salience* of scarcity (subjective financial concern, scarcity-threat perception) did — a new contextual moderator. Methodologically, it demonstrates the value of consulting original authors before data collection and of measuring contextual shifts (here, the COVID-19 decision environment) that can invalidate naive direct replication.

## Limitations & open questions
- **Correlational design** (scarcity not manipulated) prevents causal inference; the authors call for experiments that manipulate resource scarcity *or* its cognitive saliency directly. (They note Study 6 of Shah et al. 2015 on time scarcity as a rare causal exception, itself failed to replicate by O'Donnell et al. 2021.)
- **WEIRD samples only** — both original and replication restricted to Western, educated, industrialized, rich, democratic populations; cross-cultural replication is needed before generalizing.
- **COVID-19 context** makes this not a clean direct replication but a test embedded in pandemic-altered threat perceptions; how scarcity frames value outside such a shock is open.
- **Unexplained financial-literacy reversal:** whether low-literacy heuristic reliance genuinely improves context-stability, or is an artifact of correlated moderators, is unresolved.

## Connections
The paper is built directly on Shah, Shafir & Mullainathan (2015) "Scarcity frames value" and the broader scarcity-mindset program of Mullainathan & Shafir (2013), Shah, Mullainathan & Shafir (2012), and Mani et al. (2013) on poverty and cognitive function. The canonical anomalies it tests come from Thaler (1980, 1985) on transaction utility and mental accounting and [[@Tversky1981|Tversky & Kahneman (1981)]] on framing; it positions these against the classical rational-choice benchmark of Robbins (1932), Savage (1954), and Von Neumann & Morgenstern (1944), and the bounded-rationality critique of Simon (1955, 1990), [[@Tversky1974|Tversky & Kahneman (1974)]], and [[@Kahneman1979|Kahneman & Tversky (1979)]]. On replication and evidentiary value it engages O'Donnell et al. (2021) and Camerer et al. (2018), with the original authors' replies (Shah et al. 2018, 2019). Neural evidence for a scarcity-valuation link comes from Huijsmans et al. (2019); the objective-vs-subjective threat distinction parallels Isler et al. (2020) on influenza vaccination, and the heuristics-can-help argument draws on Gigerenzer (2008) and Isler & Yilmaz (2019). Financial literacy measures follow Isler, Rojas & Dulleck (2022).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
