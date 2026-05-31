---
citekey: Tversky1974
title: "Judgment under Uncertainty: Heuristics and Biases"
authors: ["Tversky, Amos", "Kahneman, Daniel"]
year: 1974
type: journalArticle
doi: 10.1126/science.185.4157.1124
zotero: "zotero://select/library/items/YSEEBY59"
pdf: /Users/jesper/Zotero/storage/EHMXYGFQ/Tversky1974.pdf
tags: [literature]
keywords: [heuristics-and-biases, representativeness, availability, anchoring, base-rate-neglect, subjective-probability]
topics: ["[[prospect-theory-loss-aversion]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This article described three heuristics that are employed in making judgments under uncertainty: (i) representativeness, which is usually employed when people are asked to judge the probability that an object or event A belongs to class or process B; (ii) availability of instances or scenarios, which is often employed when people are asked to assess the frequency of a class or the plausibility of a particular development; and (iii) adjustment from an anchor, which is usually employed in numerical prediction when a relevant value is available. These heuristics are highly economical and usually effective, but they lead to systematic and predictable errors. A better understanding of these heuristics and of the biases to which they lead could improve judgments and decisions in situations of uncertainty.

## Summary
This is the foundational synthesis of the heuristics-and-biases program. Tversky and Kahneman argue that people assess probabilities and predict values not by applying the calculus of probability but by relying on a small set of cognitive shortcuts—representativeness, availability, and anchoring-and-adjustment. Each heuristic is usually serviceable but produces *systematic, predictable* errors (not random noise or motivated distortion). The paper catalogs roughly a dozen such biases, each tied to one of the three heuristics, and draws out implications for decision theory and applied judgment.

## Research question
How do people actually assess the probability of an uncertain event or the value of an uncertain quantity? Specifically: what psychological mechanisms underlie intuitive probabilistic judgment, and why do these mechanisms generate departures from normative (Bayesian / statistical) standards?

## Method / identification
None in the econometric sense—the paper is a programmatic *review* assembling results from a series of laboratory experiments (mostly the authors' own prior work, refs 1–2, 5–6). The "identification" strategy is the demonstration paradigm: construct stimuli in which the heuristic and the normative answer make *divergent* predictions, then show subjects systematically track the heuristic. Recurring designs include:
- **Base-rate manipulation (engineer/lawyer):** descriptions allegedly drawn from a population of 70/30 vs. 30/70 engineers/lawyers. By Bayes' rule the odds ratio across conditions should be $(.7/.3)^2 = 5.44$; subjects produced nearly identical judgments, ignoring the prior. A *worthless* description (Dick) drove judgments to $.5$ regardless of base rate, while *no* description recovered correct use of the prior.
- **Sample-size insensitivity (hospital problem):** subjects judge a large and small hospital equally likely to record days with $>60\%$ boys, ignoring that a small sample strays further from $50\%$—the "law of small numbers."
- **Anchoring (wheel of fortune):** an arbitrary number $0$–$100$ from a spun wheel shifts median estimates of, e.g., the percentage of African countries in the UN from $25$ (anchor $10$) to $45$ (anchor $65$); payoffs for accuracy did not remove the effect.
- **Insufficient adjustment (multiplication):** $5$-second estimates of $8\times7\times\cdots\times1$ (median $2{,}250$) vs. $1\times2\times\cdots\times8$ (median $512$), both far below the true $40{,}320$.
- **Calibration of subjective probability distributions:** elicited percentiles $X_{01},\dots,X_{99}$; true values fall outside $[X_{01},X_{99}]$ on $\sim 30\%$ of problems—overly tight intervals attributable to anchoring on one's best estimate.

## Data
None original beyond the cited experiments. Subjects are undergraduates, naive judges, and in some studies experienced research psychologists; stimuli are constructed vignettes, lists, urns, and numerical tasks.

## Key findings
**Representativeness** (judging $p(A\mid B)$ by similarity of $A$ to $B$) produces: insensitivity to prior probability / base rates; insensitivity to sample size; misconceptions of chance (gambler's fallacy, local representativeness, "law of small numbers"); insensitivity to predictability; the *illusion of validity* (confidence tracks fit of input to output, not reliability); and misconceptions of regression toward the mean (e.g., the flight-instructor inference that punishment "works" and reward "backfires," a pure regression artifact).

**Availability** (judging frequency/probability by ease of retrieval or construction) produces: biases from retrievability and salience (a burning house vs. a newspaper report); biases from the effectiveness of a search set (words beginning with $r$ judged more frequent than words with $r$ in third position); biases of imaginability (committee-size estimates as a decreasing function of $k$ rather than the correct binomial $\binom{10}{k}$, max $252$ at $k=5$); and *illusory correlation* (Chapman & Chapman), explained as availability of associative bonds.

**Anchoring-and-adjustment**: estimates are biased toward an initial value because adjustment is insufficient. This explains overestimation of conjunctive-event probability (chain-like structure → unwarranted planning optimism) and underestimation of disjunctive-event probability (funnel-like structure → underestimated system-failure risk), plus overly narrow subjective confidence intervals.

Overarching result: the biases are *cognitive*, not motivational—they survive accuracy incentives and afflict statistically sophisticated experts when they reason intuitively.

## Contribution
Established the heuristics-and-biases research program and a shared vocabulary (representativeness, availability, anchoring, base-rate neglect, the law of small numbers, illusion of validity, illusory correlation). It reframed deviations from rationality as lawful and predictable, seeding behavioral economics, behavioral decision theory, and—directly—Kahneman & Tversky's later prospect theory. Cited as a cornerstone of Kahneman's 2002 Nobel.

## Limitations & open questions
The authors raise several explicitly:
- **Why heuristics persist / fail to self-correct:** people do not induce statistical principles (regression, sample-size effects) from lifelong experience because "the relevant instances are not coded appropriately"—an open question about how experience could be restructured to teach these rules.
- **Coherence is insufficient for rationality:** an internally consistent subjective-probability measure (e.g., one embodying the gambler's fallacy) can still be incompatible with the judge's wider web of beliefs; the paper concedes "there can be no simple formal procedure" for assessing such global compatibility—an unresolved normative problem.
- **Calibration depends on elicitation procedure:** formally equivalent elicitation methods yield different distributions, leaving open how to elicit well-calibrated beliefs.
- The paper does not model *when* a given heuristic is triggered, nor offer a process theory predicting which bias dominates in a novel task—left for later work.

## Connections
Builds directly on Kahneman & Tversky's prior experimental papers (Psychol. Rev. 1973; Cognitive Psychol. 1972, 1973; "Belief in the law of small numbers," Psychol. Bull. 1971) and on Slovic & Lichtenstein on anchoring. It positions itself against the axiomatic subjective-probability tradition of Savage and de Finetti and modern (Bayesian) decision theory, and against the conservatism literature (Edwards). Chapman & Chapman supply the illusory-correlation phenomenon; Bar-Hillel the conjunctive/disjunctive betting study. Downstream it underwrites Kahneman & Tversky's prospect theory and the entire behavioral-economics literature on departures from expected-utility and Bayesian benchmarks—central to choice modeling where intuitive probability assessment substitutes for normative updating.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
