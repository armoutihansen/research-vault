---
citekey: Hogarth1975
title: Cognitive Processes and the Assessment of Subjective Probability Distributions
authors: ["Hogarth, Robin M."]
year: 1975
type: journalArticle
doi: 10.1080/01621459.1975.10479858
zotero: "zotero://select/library/items/QG4GRZM9"
pdf: /Users/jesper/Zotero/storage/924RJGFK/Hogarth - 1975 - Cognitive Processes and the Assessment of Subjective Probability Distributions.pdf
tags: [literature]
keywords: [belief-elicitation, proper-scoring-rules, subjective-probability, heuristics-and-biases, calibration, overconfidence, bayesian-updating]
topics: []
related: [Gneiting2007]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> This article considers the implications of recent research on judgmental processes for the assessment of subjective probability distributions. It is argued that since man is a selective, sequential information processing system with limited capacity, he is ill-suited for assessing probability distributions. Various studies attesting to man's difficulties in acting as an "intuitive statistician" are summarized in support of this contention. The importance of task characteristics on judgmental performance is also emphasized. A critical survey of the probability assessment literature is provided and organized around five topics: (1) the "meaningfulness" of probability assessments; (2) methods of eliciting distributions; (3) feedback and evaluation of assessors; (4) differential ability of groups of assessors and (5) the problems of eliciting a single distribution from a group of assessors. Conclusions from the analysis with respect to future work include the need to capitalize on cognitive simplification mechanisms; making assessors aware of both human limitations and the effects of task characteristics; and emphasizing feedback concerning the nature of the task at hand.

## Summary

This is an invited review/position article in *JASA* (Applications Section) that confronts the personalistic (subjective) theory of probability with the then-emerging cognitive psychology of judgment. Hogarth's thesis is that because humans are selective, step-wise information processors of limited capacity, they are poorly equipped to act as "intuitive statisticians" and thus to assess coherent subjective probability distributions. The paper marshals two decades of psychological evidence on failures of intuitive statistical reasoning, critically surveys the elicitation literature around five recurring themes, and derives prescriptions for designing assessment procedures that work *with* rather than against human cognition. It is a survey/methodological piece: there is no new dataset or formal theorem of the author's own, and its contribution is synthetic and programmatic.

## Research question

How well can human beings assess subjective probability distributions, given what cognitive psychology reveals about the capabilities and limitations of human judgment, and how should elicitation procedures be designed in light of those limitations? The paper responds explicitly to de Finetti's call that the "true subjective probability problem" is an empirical question about how probabilities are actually assessed by people and how that ability can be improved.

## Method / identification

This is a critical literature review and conceptual synthesis, not an empirical or formal-theory paper. The author's analytical scaffolding rests on two distinctions imported from the judgment literature. First, following Winkler and Murphy, the "goodness" of an assessor is decomposed into *substantive* goodness (subject-matter knowledge) and *normative* goodness (the ability to express opinions coherently in probabilistic form). Second, three evaluation methods for assessments are distinguished: comparison to experimenter-set "objective" probabilities; penalty/scoring functions; and long-run calibration (matching empirical relative frequencies, e.g., events assigned $0.60$ should occur about 60% of the time).

The one formal apparatus developed is the theory of proper scoring rules. For an $n$-fold partition of mutually exclusive, exhaustive events $E_1,\dots,E_n$, the assessor reports a probability vector $r=(r_1,\dots,r_n)$ while holding true beliefs $p=(p_1,\dots,p_n)$; truthful reporting is $r=p$. If $S_k(r)$ is the score received when event $k$ obtains, the assessor's subjectively expected score is

$$S(r,p)=\sum_{k} p_k S_k(r).$$

A scoring rule is *strictly proper* if

$$S(p,p)>S(r,p)\quad\text{for all } r\neq p,$$

so that expected score is uniquely maximized by honest reporting. The rule presupposes an idealized assessor (coherent, fully comprehending the elicitation mechanism, with utility linear in money over the relevant range, maximizing expected utility). Hogarth catalogs the standard families (quadratic/Brier, logarithmic, spherical) and reviews relaxations of these assumptions.

## Data

No primary data. As a review, it reanalyzes and synthesizes a large secondary literature spanning laboratory experiments (bookbag-and-poker-chip Bayesian revision tasks, almanac credible-interval questions, weather forecasting, stock-market prediction, urn/Bernoulli tasks) and theoretical contributions on subjective probability and scoring rules.

## Key findings

The central diagnostic claim is that humans are ill-suited to distributional assessment, supported by a catalogue of documented biases: (1) the concept of a *sampling distribution* is essentially absent — Kahneman and Tversky found subjects generated near-identical distributions for sample sizes of 10, 100, and 1,000, ignoring how standard errors shrink with $n$ (the "law of small numbers"). (2) Intuitions about *independence* and *randomness* are weak (gambler's fallacy; Wagenaar's finding that sequences are judged "most random" when the repetition probability is biased away from 0.5). (3) Estimates of *central tendency* are fairly accurate but estimates of *dispersion* are not — people effectively estimate a coefficient of variation rather than variance, and Beach and Scopp found subjects' "variance" estimates corresponded to mean absolute deviation raised to an exponent near $0.39$. (4) Assessed credible intervals are badly *overconfident* — Alpert and Raiffa's "98% credible intervals" excluded the true value 40–50% of the time, and informing subjects did not fix it. (5) People overestimate conjunctive and underestimate disjunctive probabilities, exhibit *illusory correlation*, and lean on *representativeness* and *availability* heuristics.

On task characteristics: assessed probabilities are highly sensitive to *response mode* (linear scale vs. odds vs. log-odds), payoffs, presentation order (primacy/recency), and the amount of information — there is "no true prior distribution" waiting to be read off. On feedback: *task-structure* feedback generally outperforms pure *outcome* feedback, and adding outcome feedback to task-structure feedback can even depress performance. On scoring rules: although conceptually ingenious, many well-known proper rules are *insensitive* (expected-score differences across reported probabilities are small, so they fail to motivate sharp assessments), presume a single "true" internal distribution that often does not exist, ignore the subjective cost of assessment, and are poorly understood by the mathematically untrained — so their practical value may accrue more to evaluators than to assessors. A counterpoint is that trained *substantive experts* (e.g., meteorologists in Murphy–Winkler and Peterson et al.) produce well-calibrated interval forecasts, indicating limitations are heavily task- and training-dependent.

## Contribution

The paper is an early, influential bridge between the subjectivist/Bayesian elicitation tradition (de Finetti, Savage, Winkler) and the heuristics-and-biases program (Tversky and Kahneman), framed for a statistics audience. It reframes elicitation as a *cognitive* problem: rather than assuming a latent coherent distribution to be extracted, it argues procedures should exploit the simplification strategies people already use (anchoring-and-adjusting, pairwise comparison, decomposition into manageable units with mechanical aggregation via Bayes' theorem), warn assessors of their own biases, and tailor methods to task structure. It also gives a compact, critical exposition of proper scoring rules and their practical shortcomings.

## Limitations & open questions

The paper itself flags that the empirical base is thin and unsystematic: experiments rarely vary substantive vs. normative expertise jointly, mostly use naive subjects who may not understand the response required, and ignore personality and cultural background. Hogarth names several explicit open problems that read as a research agenda: (1) build a *taxonomy of assessment task characteristics* so that, by logical analysis, one could match judgmental strategies to task types — there is "no reason why one kind of assessment procedure should be the most effective in all situations." (2) Shift research from "how well" people assess uncertainty to "how" they do it (process-level explanation linking task variables to elicited heuristics). (3) Determine which elicitation procedures best exploit cognitive simplification mechanisms and how people learn the characteristics of real-world data-generating processes. (4) Develop scoring rules that are *sensitive* enough to reward sharp, careful assessment without presuming a unique true distribution and while accounting for the cost of assessment. (5) Study feedback design (outcome vs. task-structure vs. process) and group elicitation more systematically.

## Connections

Directly extends the subjectivist foundations of de Finetti (1937, 1962) and Savage on coherent personal probability, and the elicitation program of Winkler (1967) and Winkler & Murphy (1968) on assessing "good" probability assessors. The diagnostic core draws on Tversky & Kahneman's heuristics-and-biases work (representativeness, availability, the law of small numbers) and Slovic & Lichtenstein's review of judgment paradigms, plus Peterson & Beach's "man as intuitive statistician." The formal scoring-rule material is a precursor to the modern synthesis in [[@Gneiting2007|Gneiting & Raftery (2007)]] on strictly proper scoring rules and the calibration literature (e.g., Dawid). The overconfidence-in-credible-intervals theme connects to Alpert & Raiffa's calibration training and later overconfidence research by Lichtenstein, Fischhoff, and Phillips. It is a natural touchstone for belief elicitation, proper scoring rules, and the behavioral critique of the expected-utility assumptions underlying incentive-compatible elicitation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
