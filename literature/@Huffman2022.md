---
citekey: Huffman2022
title: "Persistent overconfidence and biased memory: Evidence from managers"
authors: ["Huffman, David", "Raymond, Collin", "Shvets, Julia"]
year: 2022
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/L87Q5F5K"
pdf: /Users/jesper/Zotero/storage/76YQD7R7/Huffman2022.pdf
tags: [literature]
keywords: [overconfidence, motivated-beliefs, biased-memory, belief-updating, field-experiment, tournament-incentives]
topics: []
related: [Brunnermeier2005, Koszegi2006a, Sarver2018, Sliwka2020]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

A long-standing puzzle is how overconfidence survives repeated, salient feedback. Studying roughly 230 store managers in a chain who compete in a high-powered quarterly tournament and receive detailed rank feedback, the authors document three linked facts: managers (i) make overconfident predictions about their own future rank, (ii) hold overly positive memories of past rank, and (iii) the two are positively correlated at the individual level. Both reduced-form and structural analyses point to a "motivated beliefs" explanation, in which agents distort memories of feedback to sustain unrealistic expectations. To the authors' knowledge this is the first field evidence directly linking persistent overconfidence about the future to biased memory of the past.

## Research question

Does persistent overconfidence about relative performance exist in a real workplace with rich repeated feedback; do agents hold overly positive memories of past performance; and is overly positive memory associated with overconfident prediction at the individual level, as motivated-beliefs models predict?

## Method / identification

Two data sources are combined: (a) firm historical records of quarterly tournament outcomes (2008:I-2016:I), and (b) a lab-in-the-field study (239 managers, 32 sessions in late 2015) that incentive-elicited each manager's predicted modal performance quintile for 2015:IV (about \$22 for a correct guess) and their recalled rank in 2015:II, learned roughly two months earlier (\$1.50 for recall within $\pm 10$ ranks).

The identification challenge, following Benoit & Dubra (2011), is that ex post prediction errors need not imply bias once ex ante private signals are accounted for. The authors exploit that the key signal — past tournament rank — is public. They benchmark predictions against multinomial-logit panel models using lagged outcomes (best fit at eight lags), labeling discrepancies "ex ante prediction errors." They also apply the Burks et al. (2013) test on ex post errors (which they cannot reject).

The structural model formalizes Bayesian learning: each manager $k$ has a fixed type $a_{k}\in\{1,\dots,5\}$; each period a public signal $s_{k,t}$ (the quintile) is drawn via a type-to-signal matrix $P_{t}$, with $p_{t}(s\mid a)$. Beliefs $f_{k,t}(a)$ over types generate signal beliefs $g_{k,t}(s)=\sum_{a} f_{k,t}(a)\,p_{t}(s\mid a)$, and managers bet on the modal signal. $\hat{P}$ is estimated from observed signal-to-signal transition matrices $Z_{t}$ (whose average is the empirical transition matrix $\hat{Z}$); starting from uniform priors, Bayes' rule yields posteriors per manager. Two extensions: (1) a private-signal matrix $Q$ estimated by simulated method of moments to give private information maximal latitude to rationalize the data (at most five signals suffice per Benoit-Dubra Theorem 4); (2) a biased-memory matrix $M$ calibrated from observed recall frequencies, with managers updating on remembered rather than actual signals, allowing heterogeneity in being motivated/unmotivated, in sophistication vs naivete (a la Benabou & Tirole 2002 metacognition), and in randomness of the memory technology. Models are compared to the data via Euclidean distance with bootstrap/simulation-based tests.

## Data

Firm administrative tournament records for about 230-300 stores per quarter, 2008:I-2016:I; plus an incentivized lab-in-the-field study of 239 managers (about 56% female, median age 36, median tenure 2.5 years) eliciting predictions, memories, and traits (risk aversion, competitiveness, knowledge of the scheme, a delegation/brain-teaser task).

## Key findings

Reduced form: 48% of managers are overconfident vs 21% underconfident relative to the panel predictor, averaging about 0.5 quintiles too optimistic; overconfidence is just as prevalent among experienced managers, so it is persistent. Memory: top performers recall accurately, but managers below the top have large recall errors skewed toward overly positive memories; average recall error is significantly better-than-actual. Link: a one-SD increase in recalled second-quarter performance is associated with predicting about 0.5 quintiles higher, with actual past performance roughly half as large and insignificant — managers predict off remembered, not actual, performance; flattering memory significantly raises the probability of overconfidence, and the link does not weaken with experience.

Structural: 45% overconfident vs 26% underconfident relative to the Bayesian benchmark (average about 0.4 quintiles optimistic), and the model is rejected (distance 210, far in the bootstrap tail); two years is enough time for Bayesians to correct overconfident priors, validating the experience cutoff. The best-fitting private-signal model barely improves fit (43%/25%) and is rejected at the 1% level, with implausible features. The biased-memory model assigns about 40% naifs, 31% sophisticates, 29% unmotivated, generates 33% overconfident vs 17% underconfident, cuts distance to 135 (about 90th percentile), and cannot be statistically rejected — the only specification that fits. Exploratory: overconfident managers perform no worse overall, but earn higher profits and worse customer-service scores, hire fewer assistant managers, and delegate less.

## Contribution

First field evidence directly linking persistent overconfidence about the future to biased memory of the past, establishing the empirical relevance of motivated-beliefs theory in a high-stakes, high-feedback workplace. Methodologically, it shows how public-signal histories can discipline private-information explanations of overconfidence, and how a structural model can quantify whether biased memory explains the prevalence and magnitude of overconfidence.

## Limitations & open questions

The authors flag: the prediction measure elicits only the modal quintile, not full belief distributions (dictated by comprehension constraints), so the sharpest Benoit-Dubra-style tests are unavailable; the biased-memory model still under-predicts the absolute prevalence of both biases; turnover may bias the estimated mix of naifs/sophisticates/unmotivated if low-ability types selectively leave; the sample is too small, with limited decision outcomes, to credibly open the "black box" of how overconfidence affects managerial performance — and because motivated beliefs are endogenous, present-bias-driven overconfidence could mask a positive effect of confidence on performance, a general caution for the overconfidence literature. The management-style results are correlational and exploratory. Underconfidence among a minority of managers, and its causes, is an open area for future research.

## Connections

The paper operationalizes the motivated-beliefs framework of Benabou & Tirole (2002, 2011, 2016 survey), with memory-distortion technologies as in Compte & Postlewaite (2004) and Gottlieb (2010), and ego/anticipatory-utility variants in [[@Koszegi2006a|Koszegi (2006)]], [[@Brunnermeier2005|Brunnermeier & Parker (2005)]], Bracha & Brown (2012), and [[@Sarver2018|Sarver (2018)]]. Identification rests on Benoit & Dubra (2011) and the ex post test of Burks et al. (2013). It extends field overconfidence work on investors and CEOs (Barber & Odean 2001; Malmendier & Tate 2005, 2015; DellaVigna & Malmendier 2006) and on truckers and poker players (Hoffman & Burks 2020; Park & Santos-Pinto 2010). On biased memory it complements lab evidence from Chew, Huang & Zhao (2020) and [[@Sliwka2020|Zimmermann (2020)]], and motivated-belief lab studies by Eil & Rao (2011) and Schwardmann & van der Weele (2019). Alternative non-motivated accounts it contrasts with include Heidhues, Koszegi & Strack (2018), the Dunning-Kruger effect (Kruger & Dunning 1999), and overconfident-priors models (Santos-Pinto & Sobel 2005; Van den Steen 2004); gender differences in confidence echo Niederle & Vesterlund (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
