---
citekey: Manski2004
title: Measuring Expectations
authors: ["Manski, Charles F."]
year: 2004
type: journalArticle
doi: 10.1111/j.1468-0262.2004.00537.x
zotero: "zotero://select/library/items/BTI7JANP"
pdf: /Users/jesper/Zotero/storage/YHZWF6Y3/Manski - 2004 - Measuring Expectations.pdf
tags: [literature]
keywords: [belief-elicitation, subjective-probabilities, expectations, identification, discrete-choice, proper-scoring-rules, ambiguity, rational-expectations]
topics: ["[[subjective-expectations-probability-judgment]]"]
related: [Gneiting2007, McFadden2000, Tversky1974]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> To predict choice behavior, the standard practice of economists has been to infer decision processes from data on observed choices. When decision makers act with partial information, economists typically assume that persons form probabilistic expectations for unknown quantities and maximize expected utility. Observed choices may be consistent with many alternative specifications of preferences and expectations, so researchers commonly assume particular sorts of expectations. It would be better to measure expectations in the form called for by modern economic theory; that is, subjective probabilities. Data on expectations can be used to relax or validate assumptions about expectations. Since the early 1990's, economists have increasingly undertaken to elicit from survey respondents probabilistic expectations of significant personal events. This article discusses the history underlying the new literature, describes some of what has been learned thus far, and looks ahead towards making further progress.

## Summary

Manski's Fisher–Schultz Lecture is a programmatic manifesto for the direct measurement of subjective probabilistic expectations as a complement to choice data in the econometric analysis of decision making under uncertainty. The core argument is an identification one: when a decision maker acts with partial information and is modeled as a subjective-expected-utility maximizer, observed choices are jointly determined by *preferences* and *expectations*, and the same choice data are consistent with many distinct (preference, belief) pairs. Inferring a decision process from choices alone therefore requires strong, typically untestable, maintained assumptions — most commonly rational expectations. Manski argues this convention is responsible for a "crisis of credibility" and proposes instead to elicit beliefs in the form theory calls for: subjective probability distributions over unknown quantities. The paper surveys the intellectual history (from Samuelson's and McFadden's revealed preference, to Juster's 1966 purchase-probability questions, to the 1990s surge in probabilistic survey research), reports substantive findings from the author's own elicitation work, reviews how elicited expectations can be validated against realizations, shows how they can resolve identification problems in econometric choice models, and closes by proposing the elicitation of probability *ranges* to capture ambiguity. Coverage here is full (all sections 1–9 read; only the closing paragraphs of the brief forward-looking Section 9 were truncated in extraction, but its agenda is conveyed throughout).

## Research question

Can econometric analysis of decision making under partial information be put on a credible empirical footing? Manski's answer is that choice data *alone* cannot do this, because preferences and expectations are not jointly identified from choices, and that the standard rational-expectations fix is generally implausible. The constructive question is then: how can researchers directly measure expectations (as subjective probabilities), how accurate are such measurements, and how can they be used to relax or validate belief assumptions in choice models?

## Method / identification

The paper is primarily a conceptual and identification-theoretic essay illustrated with formal examples. The abstract decision problem is: with choice set $C$, state space $\Gamma$, true state $\gamma^* \in \Gamma$, and objective $f(c,\gamma): C \times \Gamma \to \mathbb{R}$, the agent wishes to solve $\max_{c \in C} f(c,\gamma^*)$ but does not know $\gamma^*$. Economists assume the agent instead places a subjective distribution $Q$ on $\Gamma$ and solves $\max_{c \in C} \int u[f(c,\gamma)]\, dQ$, and routinely further assume *rational expectations* — that $Q$ equals the objective law $P$ generating $\gamma^*$.

The central identification point is made by two worked illustrations. (i) **Schooling**: across studies (Freeman 1971; Willis & Rosen 1979; Manski & Wise 1983), the assumed information set and updating rule differ; Manski (1993a) shows that if youth do *not* condition expectations on ability while a researcher assumes they do, one may wrongly conclude youth ignore the returns to schooling. (ii) **Ultimatum game**: with $K$ dollars, offer $c \in [0,K]$ and responder acceptance $d(c) \in \{0,1\}$, proposer payoff $y(1,c,d)=(K-c)d(c)$. Two utility types — selfish $U_1 = (K-c)d(c)$ and fairness $U_2 = [(K-c)d(c)]\cdot cd(c)$ — combined with three belief specifications $Q_1, Q_2, Q_3$ over acceptance probabilities yield six agent types. Expected-utility maximization gives chosen offers $c(1,1)=K/4$, $c(1,2)=c(1,3)=K/2$, $c(2,1)=c(2,2)=K/2$, $c(2,3)=2K/3$. Four of six types offer the even split $K/2$, so the modal even-split offer does *not* reveal a fairness preference — preferences and expectations are observationally entangled.

The methodological remedy is elicitation of probabilistic expectations directly from survey respondents (the Juster purchase-probability format and its descendants), and their use to *relax* the belief assumption: given measured expectations, one needs only assume elicited beliefs faithfully describe perceptions, not that they are rational. Manski also reviews the partial-identification stance: combining data with credible assumptions may bound but not point-identify $P$, motivating beliefs as *sets* of distributions rather than a single $Q$.

## Data

This is a survey/conceptual paper rather than a primary empirical study, but it marshals extensive secondary evidence from probabilistic elicitation programs: the Survey of Economic Expectations (SEE), Health and Retirement Study (HRS), Bank of Italy SHIW, Dutch VSB Panel, NLSY97, and the Michigan Survey of Consumers. Reported substantive domains include job-insecurity perceptions, year-ahead income expectations, Social Security benefit expectations, mutual-fund return expectations, voting (probabilistic polling), survival probabilities, and student perceptions of returns to schooling.

## Key findings

(1) **Non-identification**: choice data alone cannot separate preferences from expectations (the ultimatum and schooling illustrations). (2) **Rational expectations is generally implausible**: a decision maker learning $P$ faces the same identification and finite-sample induction problems as the empirical economist, who routinely cannot learn $P$; Savage's axioms justify subjective EU but impose *no* restriction making expectations rational. (3) **Respondents can and will report probabilities**: large surveys show meaningful, internally coherent probabilistic responses, vindicating Juster (1966) over verbal/attitudinal formats. (4) **Elicited beliefs have predictive accuracy**: e.g., Dominitz (1998) finds earnings expectations match realizations reasonably well but are too optimistic and overconfident ex post; Hurd & McGarry (2002) find subjective survival probabilities to 75/85 predict actual mortality (e.g., mean elicited survival-to-75 was .45 among HRS respondents who died by 1994 versus .65 among survivors). (5) **Beliefs resolve choice-model identification**: Nyarko & Schotter (2002) use a proper scoring rule to elicit beliefs about opponents and break the experimental identification problem; Delavande (2003), Lochner (2003), van der Klaauw & Wolpin (2002) estimate random-utility models using elicited expectations. (6) **Ambiguity**: a single elicited distribution may be a "probabilistic summary of ambiguity"; eliciting probability *ranges* lets respondents express ignorance ("0 to 100"), bounded ambiguity ("30 to 70"), or precision, and disambiguates the troublesome "fifty–fifty" response.

## Contribution

The paper crystallizes the case for treating subjective probabilistic expectations as measurable economic data and launched the modern subjective-expectations research program. Its enduring contribution is methodological framing: it converts a diffuse discomfort with belief assumptions into a clean identification argument, legitimizes survey elicitation against decades of economists' "hostility to subjective data," and lays out an agenda spanning elicitation design, accuracy validation, integration into structural choice models, and the measurement of ambiguity. It is now a foundational citation for belief-elicitation and expectations economics.

## Limitations & open questions

Manski names several explicit open problems. (1) **Psychological realism**: willingness to report probabilities does not establish that people *think* probabilistically or use a single $Q$ to decide — the ambiguity hypothesis (sets of priors, à la Gilboa & Schmeidler 1989) remains untested at the elicitation level, and range-elicitation is proposed but unvalidated. (2) **Expectations formation**: predicting behavior after policy interventions that shift beliefs in non-obvious ways requires a theory of belief formation, "about which little is known"; lab Bayesian-updating studies map poorly to real-world information environments. He suggests lengthy semi-structured "conversations" with small samples, which large surveys cannot support. (3) **Residual preference assumptions**: even with elicited beliefs, estimating choice models still needs untestable assumptions on the population distribution of preferences. (4) **Eliciting full distributions** (e.g., entire life-cycle earnings paths) is often impractical, forcing reliance on partial expectations data.

## Connections

The non-identification thesis builds on Manski's own revealed-preference critiques (Manski 1993a, 2002a) and his partial-identification program ([[@McFadden2000|Manski 2000a]], 2003). The elicitation lineage runs from Juster (1966) and Tobin (1959) through Dominitz & Manski (1997a,b) and the SEE/HRS surveys. The belief-elicitation-via-incentives strand connects to proper scoring rules (Nyarko & Schotter 2002), which links to the broader scoring-rule literature later synthesized by [[@Gneiting2007|Gneiting & Raftery (2007)]]. The discrete-choice and random-utility machinery descends from McFadden (1974); the axiomatic foundation is Savage (1954). The ambiguity discussion connects to Ellsberg (1961), Gilboa & Schmeidler (1989) maxmin expected utility, robust Bayes (Berger 1985), and Camerer & Weber (1992). The bias findings (overconfidence, "fifty–fifty" heaping) link to [[@Tversky1974|Tversky & Kahneman (1974)]] and the cognitive-psychology heuristics literature.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
