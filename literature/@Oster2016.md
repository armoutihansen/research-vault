---
citekey: Oster2016
title: "Optimal expectations and limited medical testing: Evidence from huntington disease: Corrigendum"
authors: ["Oster, Emily", "Shoulson, Ira", "Dorsey, E. Ray"]
year: 2016
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/ZE5JJS6V"
pdf: /Users/jesper/Zotero/storage/93N95DIA/Oster2016.pdf
tags: [literature]
keywords: [optimal-expectations, motivated-beliefs, information-avoidance, bayesian-updating, huntington-disease, overoptimism, corrigendum]
topics: []
related: [Brunnermeier2005, Caplin2001, Oster2013a]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is a short (4-page) corrigendum to [[@Oster2013a|Oster, Shoulson, and Dorsey (2013)]], "Optimal Expectations and Limited Medical Testing: Evidence from Huntington Disease" (AER). It updates and corrects Figure 4 of the original paper, which compared individuals' perceived risk of Huntington disease (HD) with the "actual risk" implied by Bayesian updating on motor symptoms. Two problems are fixed: (i) newly available genetic-testing data from the PHAROS sample replace a workaround that used an external comparison group, and (ii) a construction error in which the baseline HD probability was wrongly held at 50 percent regardless of age. The corrected figure shows substantially less overoptimism than originally reported — people with low symptom levels are roughly correct (if anything slightly pessimistic), while overoptimism remains strong among those with advanced symptoms. The authors argue the core optimal-expectations theory still fits the data.

## Research question
The original paper asked whether people hold systematically optimistic beliefs about their disease state and whether such "optimal expectations" rationalize observed patterns of medical (genetic) testing avoidance. This corrigendum narrows that question to a measurement issue: how does perceived HD risk actually compare to the true posterior probability of carrying the HD mutation, conditional on observed motor score, once correct data and correct baseline priors are used?

## Method / identification
The substantive object is a Bayesian-updating calculation of "true risk." For an at-risk individual observed with motor score $X$ at a given age, the corrected posterior is the probability they carry the HD mutation given the symptom signal. The corrected procedure combines (a) a baseline prior on carrying the HD mutation that *declines with age* — among 100 at-risk individuals reaching age 50 without diagnosis, fewer than 50 carry the mutation — with (b) the likelihood of each motor score among PHAROS participants known (from the now-accessible gene-testing data) to carry vs. not carry the mutation. Schematically, the posterior is

$$p(\text{HD}\mid X, \text{age}) = \frac{p(X\mid \text{HD})\, \pi(\text{age})}{p(X\mid \text{HD})\, \pi(\text{age}) + p(X\mid \neg\text{HD})\,\bigl(1-\pi(\text{age})\bigr)}$$

where $\pi(\text{age})$ is the age-adjusted baseline. The original figure had erroneously fixed $\pi=0.5$ and, lacking PHAROS gene status, had estimated the not-at-risk likelihood $p(X\mid \neg\text{HD})$ from an external comparison group (spouses in the COHORT study) rather than from PHAROS itself. The detailed estimation of age-conditioned posteriors is carried out in the companion clinical paper Oster et al. (2015).

## Data
PHAROS (Prospective Huntington At-Risk Observational Study): 1,001 individuals entering at 50 percent HD risk, followed up to ten years with visits roughly every nine months, undergoing HD motor-symptom evaluation and being asked at some visits about perceived HD risk. The key change is that limited access to PHAROS gene-testing data became available after original publication, allowing the motor-score likelihoods to be computed within-sample rather than via the COHORT spouse comparison group. (Privacy concerns still prevent constructing the "ideal" figure plotting realized mutation share directly against perceived risk.)

## Key findings
The corrected Figure 4 (reproduced as "Figure 1") shows much less overoptimism than the published version, which had shown overoptimism at *all* motor-score levels. Now: at low symptom levels, perceived and true risk roughly coincide (individuals are if anything slightly pessimistic, though differences are small); overoptimism remains strong at advanced symptom levels. A decomposition ("Figure 2," which retains the incorrect 50 percent baseline but uses the new data) shows that most of the change is driven by the *new data*, not by the baseline-probability fix — the baseline error mattered relatively little. Intuitively, a motor score of "1" appears about as often among non-carriers as carriers, so a low score is nearly uninformative and the true risk at that level is just the (sub-50 percent, age-adjusted) baseline. The original data had overstated how often carriers show low scores and understated how often non-carriers do.

## Contribution
Documents and corrects an empirical error in a widely cited applied-theory paper, and clarifies where its evidence for biased ("optimal") beliefs actually resides. The authors argue the theory's primitive — that some people choose to hold incorrect, overoptimistic beliefs that constrain their actions — continues to fit, because the "interesting action" (testing increasing with risk, consistent action choices, biased beliefs) is concentrated among symptomatic individuals, where overoptimism survives correction. It is a notable example of transparent self-correction in economics.

## Limitations & open questions
The authors explicitly note that even with newly available data it remains impossible — due to concerns about revealing gene status to participants — to construct the "ideal" figure plotting realized HD-mutation share directly against perceived risk by motor score; the analysis still relies on a Bayesian-updating construction rather than raw realized outcomes. The reconciliation of the corrected pattern (correct beliefs at low symptoms, overoptimism only at high symptoms) with the optimal-expectations model is asserted rather than re-estimated here, leaving open how much of the original structural fit is robust. Whether overoptimism concentrated among the highly symptomatic reflects motivated belief or, e.g., denial/coping or imperfect symptom self-assessment is not separately identified.

## Connections
The corrigendum belongs to the optimal-expectations and motivated-beliefs literature: the underlying model derives from [[@Brunnermeier2005|Brunnermeier and Parker (2005)]] on optimal expectations, with related anticipatory-utility and belief-utility treatments in [[@Caplin2001|Caplin and Leahy (2001)]] and Köszegi (2006). The substantive application — avoidance of free, informative medical (genetic) tests as a way to protect optimistic beliefs — connects to the broader literature on information avoidance, e.g., Golman, Hagmann, and Loewenstein (2017) and [[@Oster2013a|Oster, Shoulson, and Dorsey (2013)]] itself. The Bayesian-updating benchmark and the documentation of systematic departures from it relate to work on belief updating and overconfidence, including Eil and Rao (2011) and Möbius, Niederle, Niehaus, and Rosenberg (2011) on asymmetric (self-serving) updating of good vs. bad news. The companion clinical paper Oster et al. (2015), "Informativeness of Early Huntington Disease Signs about Gene Status," supplies the corrected posterior estimates.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
