---
citekey: Dekel2010
title: How (Not) to Do Decision Theory
authors: ["Dekel, Eddie", "Lipman, Barton L."]
year: 2010
type: journalArticle
doi: 10.1146/annurev.economics.102308.124328
zotero: "zotero://select/library/items/RKNDHTJ4"
pdf: /Users/jesper/Zotero/storage/YRE7LSM2/Dekel2010.pdf
tags: [literature]
keywords: [decision-theory, representation-theorems, identification, methodology, revealed-preference, nonchoice-data, axiomatization]
topics: ["[[behavioral-welfare-nudge]]"]
related: [Bernheim2009, Harless1994, Manzini2007]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We discuss the goals and means of positive decision theory and the implications for how to do decision theory. We argue that the goal of positive economic theory generally is to provide predictions and understanding and that representation theorems and other results of decision theory should be seen as ways to achieve these goals. We also argue that the interpretation of a model is relevant to whether and how we use the model, that psychological considerations are not necessary for useful decision theory but can be helpful, and that nonchoice data, interpreted properly, can be valuable in predicting choice and therefore should not be ignored.

## Summary
This is a methodological review (Annual Review of Economics) on how to do *positive* decision theory. Dekel and Lipman argue that the point of positive economic theory is to deliver predictions about choice and to deliver understanding, and that the canonical tools of decision theory - representation, identification, and comparative theorems - are best read as means to those two ends rather than ends in themselves. Along the way they defend a richer model-selection criterion than naive falsificationism: the *story* of a model (its informal interpretation), its tractability, and its range of out-of-sample predictions all matter, not just in-sample fit. They then draw out implications for the role of psychology, the use of nonchoice data, and what makes a good axiomatization.

## Research question
What are the goals of positive decision theory, what kinds of formal results serve those goals, and what does that imply about how decision theory should be practiced - specifically how to select among models, how to treat psychological and nonchoice data, and what constitutes a good axiomatization?

## Method / identification
This is a conceptual/methodological essay, not an empirical or formal paper, but it is organized around the formal apparatus of decision theory. The authors model an agent via a class of utility functions and relate it to observable choice, formalized either as a choice correspondence (a map from feasible sets to chosen elements) or as a preference relation $\succeq$ interpreted as revealed preference. They taxonomize three result types: (i) *representation theorems*, which show a functional form represents behavior iff that behavior satisfies certain axioms (necessary-and-sufficient characterizations); (ii) *identification/uniqueness theorems*, which state how far behavior pins down the objects (utilities, beliefs) in the representation; and (iii) *comparatives/comparative statics*, which connect changes in representation objects to changes in behavior. The non-identification of state-dependent expected utility is worked through formally: with two states an agent maximizing $(1/4)u(f(s_1),s_1)+(3/4)u(f(s_2),s_2)$ is behaviorally indistinguishable from one with $v(x,s_1)=(1/2)u(x,s_1)$, $v(x,s_2)=(3/2)u(x,s_2)$ and beliefs $(1/2,1/2)$, since the products are identical - so probabilities and state-dependent utilities cannot be separated without a normalization (e.g. the Anscombe-Aumann state-independence axiom).

## Data
None - this is a methodological review of the decision-theory literature, not an empirical study. Its "data" are illustrative examples drawn from existing models (subjective expected utility, Gilboa-Schmeidler multiple priors, Gul-Pesendorfer temptation, Kreps's demand for flexibility, Arrow-Pratt risk aversion, Allais/Ellsberg paradoxes). The 28-page article was read in full via extracted text.

## Key findings
- Models are useful in three ways even absent new predictions: they can reveal that an intuition "A leads to X" is flawed or requires an unpalatable extra assumption; they can flesh out the intuition into new conditional predictions ("A leads to X only if B"); and they can yield understanding that later generates predictions (e.g. Spence's signaling).
- Refutation should not be the sole model-selection criterion. Because every model is "refuted in the strictest sense" (a map at scale 1:1 is useless), what matters is whether the *simplifications driving an odd prediction Y are essential* to the explanation of why A leads to X. The story, tractability, and breadth of predictions justified by a small number of principles all count; a model that fits everything only by per-datapoint tweaks "adds no understanding."
- Representation theorems matter chiefly for their *sufficiency* (the hard direction): only sufficiency guarantees you know *all* the model's implications, lets you compare models (e.g. how multiple priors differs from SEU via a restricted independence axiom and an ambiguity-aversion/randomization-preference property), confirms a story's apparent feature (e.g. multiple-priors "pessimism," minimax-regret ex-post knowledge) is not an unrecognized requirement, and underwrites robustness claims.
- *Identification* is undervalued outside decision theory: if representation objects lack behavioral meaning the model is loosely connected to reality. Identification is the precondition for comparative statics (e.g. Arrow-Pratt). Achieving it has costs - richer domains and stronger assumptions - but normalizations (state independence) can be preferable even if some equivalent representation is "truer," because they deliver useful theorems (e.g. mean-preserving-spread results from concavity of $u$).
- Psychology is *not necessary but can help*: psychological realism is not costless (it can destroy useful tools, as in the state-independent vs. state-dependent example), but psychology can boost the plausibility of competing out-of-sample predictions and suggest genuinely new predictions (Laibson's cue-based consumption).
- Nonchoice data (response times, eye movements, brain imaging) should not be ignored: against Gul-Pesendorfer, the authors argue greater confidence in auxiliary parts raises confidence in the whole model, and with limited choice data nonchoice data aids model selection.
- A good axiomatization identifies the key behavior/domain (the creative, "art" step - e.g. Ramsey's bets, Kreps's menus, Kreps-Porteus timing of resolution), states axioms about observables, in preference terms, conditional rather than universal, simple and familiar, few in number, separating focal axioms from simplifications - while warning that innocuous-looking simplifications (independence in Gul-Pesendorfer temptation) can have substantive bite.

## Contribution
A widely cited articulation of the methodology of positive (predictive) decision theory that reframes representation, identification, and comparative theorems as instruments for prediction and understanding, defends a non-falsificationist account of model selection in which the model's "story" legitimately matters, and stakes out a moderate position in the economics-vs-psychology and choice-vs-nonchoice-data debates between Gul-Pesendorfer-style choice purism and behavioral/neuroeconomic approaches.

## Limitations & open questions
- Welfare/prescriptive analysis is the paper's explicit open frontier: prediction of choice is insufficient for normative claims, and once agents can make mistakes the revealed-preference assumption "choice reveals welfare" becomes inappropriate. The authors say they "have nothing to add" beyond pointing to a hypothesis we trust more than revealed preference, and to Bernheim-Rangel, Chambers-Hayashi, Koszegi-Rabin, Noor, and Rubinstein-Salant.
- Identifying the key behavior and the right domain is "the most essential step, but also the step that is closest to an art" - the authors cannot give a recipe for distinguishing good from bad modeling choices here.
- There is no general metric for the "size" of a change in a model (changes are typically non-nested in functional form), which limits how robustness can be quantified.
- How to weigh subjective judgments of plausibility across economists (and between economists and psychologists) is left to the "marketplace of ideas," which the authors concede may be subject to market failure.
- Whether and when combining multiple new ingredients (e.g. temptation *and* ambiguity) is fruitful is left open; their default is to study one new ingredient at a time.

## Connections
Squarely in the axiomatic decision-theory tradition: Savage (1954) on subjective expected utility, Anscombe & Aumann (1963) on state independence, Arrow (1971) and Pratt (1964) on risk-aversion measures. The behavioral anomalies motivating the field are Allais (1953) and Ellsberg (1961, 2001), with the generalized-EU response of Machina (1982) and betweenness models of Chew (1983) and Dekel (1986). The ambiguity literature is represented by Schmeidler (1989) and Gilboa & Schmeidler (1989) on multiple priors, with Bewley (2002) on incomplete-preference (Knightian) ambiguity and Maccheroni et al. (2006) and Siniscalchi (2009). The menus/temptation strand runs through Kreps (1979) on demand for flexibility, Gul & Pesendorfer (2001, 2005) and Dekel, Lipman & Rustichini (2001, 2009) on temptation and self-control, with Epstein (2006) on non-Bayesian updating and Kreps & Porteus (1978), Segal (1990), Epstein & Zin (1989) on the timing of resolution of uncertainty. The methodological foils are Gul & Pesendorfer (2008) on "the case for mindless economics" and Camerer (2008) and Caplin (2008) on neuroeconomics, with Kreps (1990) on intuition as data. Related "eliminate-then-maximize" choice models are [[@Manzini2007|Manzini & Mariotti (2007)]] and Eliaz & Spiegler (2008). Empirical use of complete axiomatizations is exemplified by [[@Harless1994|Harless & Camerer (1994)]]; nonchoice-data work by Caplin & Dean (2009) and Arieli et al. (2009). On welfare under mistakes: [[@Bernheim2009|Bernheim & Rangel (2009)]], Koszegi & Rabin (2008), Rubinstein & Salant (2009), Chambers & Hayashi (2008). Broader procedural-rationality roots in Simon (1982) and Rubinstein (1998), with O'Donoghue & Rabin (1999) as a representative behavioral-economics complement.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
