---
citekey: Trueblood2013
title: "Not Just for Consumers: Context Effects Are Fundamental to Decision Making"
authors: ["Trueblood, Jennifer S.", "Brown, Scott D.", "Heathcote, Andrew", "Busemeyer, Jerome R."]
year: 2013
type: journalArticle
doi: 10.1177/0956797612464241
zotero: "zotero://select/library/items/Y3YHFQIN"
pdf: /Users/jesper/Zotero/storage/9FSHPQ2Q/Trueblood2013.pdf
tags: [literature]
keywords: [context-effects, attraction-effect, similarity-effect, compromise-effect, perceptual-choice, stochastic-choice, simple-scalability]
topics: ["[[context-effects-attraction-compromise]]"]
related: [Huber1982, Simonson1989, Tversky1972, Tversky1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Context effects—preference changes that depend on the availability of other options—have attracted a great deal of attention among consumer researchers studying high-level decision tasks. In the experiments reported here, we showed that these effects also arise in simple perceptual-decision-making tasks. This finding casts doubt on explanations limited to consumer choice and high-level decisions, and it indicates that context effects may be amenable to a general explanation at the level of the basic decision process. We demonstrated for the first time that three important context effects from the preferential-choice literature—similarity, attraction, and compromise effects—all occurred within a single perceptual-decision task. Not only do our results challenge previous explanations for context effects proposed by consumer researchers, but they also challenge the choice rules assumed in theories of perceptual decision making.

## Summary

Three classic context effects from the consumer-choice literature—the attraction, similarity, and compromise effects—are usually attributed to high-level, semantically rich deliberation about products. Across three within-subjects experiments, Trueblood, Brown, Heathcote, and Busemeyer show that all three effects also arise in a stripped-down perceptual task: choosing the largest of three rectangles. Because the stimuli carry no hedonic content (no gains, losses, or "quality"), the results imply that context effects are a general property of the basic choice process rather than artefacts of consumer reasoning, and they challenge any perceptual-choice model that obeys simple scalability.

## Research question

Are the attraction, similarity, and compromise effects—long studied as features of high-level preferential choice—also present in low-level perceptual decision making? If so, can a single mechanism operating at the level of the basic decision process explain context dependence across both domains, undermining explanations that invoke domain-specific high-level constructs (e.g., loss aversion over attributes)?

## Method / identification

The unifying paradigm is a ternary perceptual choice: on each trial three rectangles appear left-to-right and the participant presses one of three keys to select the rectangle with the largest area. Height and width serve as the two attribute dimensions (analogous to price and quality), perceived separately and integrated into area (Anderson & Weiss, 1971). Rectangle dimensions were drawn from bivariate normal distributions (e.g., mean height 50 px, mean width 80 px, variance 2 px, no correlation) to inject trial-to-trial noise. The two target options $X$ and $Y$ always had equal area, so neither was objectively correct; only the decoy's position determines the predicted shift. No feedback was given, removing any incentive consequence.

Each experiment manipulated the third (decoy) option to instantiate one effect, with the decoy's identity counterbalanced near $X$ vs. near $Y$ to avoid confounding context effects with biased guessing. Effects are defined as choice-probability inequalities:

- **Attraction** (Exp. 1): a decoy similar but inferior to a focal option raises that option's share. Formally $p(X\mid\{X,Y,A_X\}) > p(X\mid\{X,Y,A_Y\})$ and $p(Y\mid\{X,Y,A_X\}) < p(Y\mid\{X,Y,A_Y\})$. Three decoy types were crossed—range ($R$, weaker on the focal option's weaker attribute), frequency ($F$, weaker on its stronger attribute), and range-frequency ($RF$, weaker on both)—720 trials/subject (180 each type + 180 fillers).
- **Similarity** (Exp. 2): a decoy $S_X$ similar to but equally attractive as $X$ raises the share of the dissimilar option $Y$; "focal" denotes the dissimilar alternative. Tested separately for height-greater-than-width and width-greater-than-height sets.
- **Compromise** (Exp. 3): with $\text{height}(C_X) < \text{height}(X) < \text{height}(Y) < \text{height}(C_Y)$ and all areas equal, $X$ and $Y$ act as compromise vs. extreme depending on the decoy; the intermediate option should gain share.

Filler trials contained one objectively largest rectangle and were used to screen subjects (exclusion if filler accuracy fell >2 SD below the mean). Estimands are mean choice probabilities for focal vs. nonfocal options, tested with paired $t$-tests across subjects.

## Data

Behavioral data from three samples of undergraduates run for course credit: Exp. 1, $n=53$ (Newcastle, online); Exp. 2, $n=62$ (Newcastle); Exp. 3, $n=63$ (Indiana, lab). Each completed 720 randomized trials. No external dataset; all data are generated by the authors' rectangle-choice task.

## Key findings

- **Attraction effect (Exp. 1):** the focal option was chosen significantly more often than the nonfocal option, $t(48)=2.601$, $p=.012$. Effect-size ordering matched the consumer literature ([[@Huber1982|Huber et al., 1982]]): range strongest, $t(48)=3.616$, $p<.001$; range-frequency next, $t(48)=2.085$, $p=.042$; frequency negligible, $t(48)=1.135$, $p=.262$. 69% / 61% / 59% of subjects showed range / range-frequency / frequency effects.
- **Similarity effect (Exp. 2):** the dissimilar (focal) option gained share, $t(61)=2.882$, $p=.006$, consistently across both orientations; 69% of subjects showed it—far more than the 3-of-8 in Tversky's (1972) perceptual task.
- **Compromise effect (Exp. 3):** the compromise option was preferred over the extreme option, $t(58)=1.967$, $p=.054$ (two-tailed; significant one-tailed, which the directional hypothesis justifies); 66% of subjects showed it. First evidence of a perceptual compromise effect.
- All three effects co-occur in one paradigm with nonhedonic stimuli, so explanations resting on attribute-level gains/losses cannot be the common cause.

## Contribution

The first demonstration that the attraction, similarity, and compromise effects all arise within a single, semantically empty perceptual task. This (i) unifies the historically separate consumer-choice and perceptual-choice literatures, suggesting a common process-level mechanism; (ii) challenges any perceptual-choice rule satisfying *simple scalability*—the ratio-of-strengths rule, signal-detection models, Luce-style choice (Luce, 1959; Medin & Schaffer, 1978; Nosofsky, 1986); and (iii) rules out loss aversion as the general explanation, since the rectangle attributes carry no gains or losses. The results support dynamic, sequential-sampling accounts—multialternative decision field theory (MDFT; Roe et al., 2001) and the leaky competing accumulator (LCA; Usher & McClelland, 2004)—and the authors argue MDFT's distance-based account is more plausible than LCA's asymmetric (loss-aversion-flavored) value function for perceptual stimuli.

## Limitations & open questions

The authors flag several explicit open problems:

- **Why does effect size vary across domains?** Table 1 shows the effects generalize but shrink in some tasks; one conjecture is that faster response times produce smaller effects (consistent with Pettibone, 2012, where attraction and compromise effects grow with deliberation time). Untested here.
- **The compromise effect is marginal** ($p=.054$, two-tailed), leaning on a one-tailed justification—the weakest of the three results.
- **Phantom-decoy effect not studied:** little is known about MDFT/LCA predictions for it; the authors call for perceptual phantom-decoy experiments and model predictions.
- **Distinguishing MDFT vs. LCA:** both fit the effects, but their added dynamic flexibility "needs to be justified." Response-time data—easy to collect in perception—could discriminate the models (cf. Tsetsos et al., 2010); proposed as future work.
- **Comparison-induced-distortion theory** (Choplin & Hummel) is an untested alternative that has been fit to attraction but not similarity or compromise data.

## Connections

Directly operationalizes the three canonical context effects from [[@Huber1982|Huber, Payne, and Puto (1982)]] (attraction), [[@Tversky1972|Tversky (1972)]] (similarity, via elimination-by-aspects), and [[@Simonson1989|Simonson (1989)]] (compromise). The reductionist move builds on Choplin & Hummel (2005) (perceptual attraction with ovals) and Tsetsos, Usher, & McClelland (2011) (perceptual similarity). The constructive theoretical targets are the dynamic accumulator models MDFT (Roe, Busemeyer, & Townsend, 2001; Hotaling, Busemeyer, & Li, 2010) and LCA (Usher & McClelland, 2004), and the paper positions itself against Tversky & Kahneman (1991) and [[@Tversky1993|Tversky & Simonson (1993)]] reference-dependent, loss-aversion theories. For economists working on stochastic choice and menu-dependent (context-dependent) preferences, this is a clean existence proof that violations of simple scalability / IIA-type regularity arise even absent semantic content, motivating process models over static random-utility specifications.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
