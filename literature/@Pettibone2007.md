---
citekey: Pettibone2007
title: Testing alternative explanations of phantom decoy effects
authors: ["Pettibone, Jonathan C.", "Wedell, Douglas H."]
year: 2007
type: journalArticle
doi: 10.1002/bdm.557
zotero: "zotero://select/library/items/28FYWR5B"
pdf: /Users/jesper/Zotero/storage/2942DJU4/Pettibone2007.pdf
tags: [literature]
keywords: [phantom-decoy, context-effects, loss-aversion, relative-advantage-model, attraction-effect, choice-theory, consumer-choice]
topics: []
related: [Huber1982, Kahneman1979, Sen1997, Shafir1993, Simonson1989]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Phantom decoys are alternatives that asymmetrically dominate a targeted alternative and yet lead to increased selection of the target when the decoy is declared to be unavailable. This effect is difficult to explain within most standard theoretical accounts of decoy effects. The current experiments tested between three explanations of this effect: (1) the relative advantage model based on loss aversion, (2) similarity substitution, and (3) range weighting. In Experiment 1, participants were presented trinary choice sets, with half of the sets containing a phantom decoy in one of five possible locations within the attribute space. Phantom decoy effects were robust across all decoy locations but one, and the pattern of effects most closely corresponded to predictions of the relative advantage model. Experiment 2 used a within-subjects manipulation of the five phantom decoy locations. The overall pattern of effects most closely corresponded to predictions from the relative advantage model, as did the pattern for the group of participants who exhibited the strongest phantom decoy effects. Copyright © 2007 John Wiley & Sons, Ltd.

## Summary
A *phantom decoy* is a highly attractive alternative that is included in a choice set but announced as unavailable; it asymmetrically dominates a target $T$ and yet, paradoxically, raises choice of $T$ over its competitor $C$. Pettibone and Wedell pit three accounts of this effect against each other — loss aversion (the relative advantage model), similarity-substitution, and range-weighting — by systematically varying the phantom's location in a two-dimensional attribute space across five decoy types. Because the three mechanisms imply *different* patterns of effect-magnitude across locations, the design discriminates among them. Across a between-subjects (Exp. 1) and a within-subjects (Exp. 2) study, the loss-aversion relative advantage model gives the best overall account, especially for the subgroup showing the clearest phantom effects, though no model explains every datum (notably the failure of the frequency phantom PF).

## Research question
What mechanism produces phantom decoy effects, and under what configurations of the unavailable alternative is the effect strongest? Concretely: do effects (a) decline with dissimilarity to the target (similarity-substitution), (b) grow with range extension and vanish without it (range-weighting), or (c) track the asymmetry of losses versus gains relative to the phantom (relative advantage / loss aversion)? Subsidiary applied question: which phantom locations make the retail "bait-and-switch" tactic work, and which can backfire?

## Method / identification
The two attributes are placed in a 2-D space where $T=\{3,5\}$ and $C=\{5,3\}$ lie on a common equi-preference contour (equal weighting $\Rightarrow$ 50/50 in pairwise choice). Five phantom locations are constructed: range ($PR=\{3,6\}$), extreme range ($PER=\{3,7\}$), frequency ($PF=\{4,5\}$), range-frequency ($PRF=\{4,6\}$), and extreme range-frequency ($PERF=\{4,7\}$); each phantom asymmetrically dominates $T$. The identification logic is that the three theories generate distinct quantitative predictions (Table 1) for the choice-share shift across these five locations.

All models feed a logistic choice rule
$$\Pr(T)=\frac{1}{1+\exp(-c\,(V_T-V_C))}$$
with a single scaling parameter $c$ fitted to equate the $PR$ effect at a 0.10 share difference across models.

**Similarity-substitution.** City-block distance $d_{ij}=0.5\lvert X_{i1}-X_{j1}\rvert+0.5\lvert X_{i2}-X_{j2}\rvert$ feeds an exponential-decay similarity $S_{ij}=\exp(-d_{ij})$ (Shepard 1987); the value of each option is its similarity to the (favored) phantom, so $V_T=S_{T,\text{phantom}}$, $V_C=S_{C,\text{phantom}}$. Prediction: effects shrink monotonically with distance, weakest for $PERF$.

**Range-weighting.** A dimension's weight rises with its range: $w_1=\mathrm{Range}_1/(\mathrm{Range}_1+\mathrm{Range}_2)$ with $w_2=1-w_1$ (RW1), or a step version $w_1=0.50+a$ whenever dimension 1's range exceeds dimension 2's (RW2, after Mellers & Biagini 1994). Prediction: no effect for $PF$ (no range extension), possibly larger effects for the extreme-range $PER$/$PERF$.

**Relative advantage (loss aversion, [[@Shafir1993|Tversky & Simonson 1993)]].** Each option is valued by summing advantages (gains) and disadvantages (losses) relative to the phantom, weighting losses more: $V_i=\mathrm{Gains}_i-2(\mathrm{Losses}_i)$ (RA1), or with diminishing sensitivity $V_i=\mathrm{Gains}_i^{0.50}-2(\mathrm{Losses}_i^{0.50})$ (RA2, à la prospect theory). Because shifting along dimension 1 (the frequency manipulation) adds to $T$'s loss relative to the phantom but not to $C$'s, the model predicts strong, roughly equal effects for $PR$/$PER$ and weak effects for $PF$/$PRF$/$PERF$.

**Experiment 1** — between-subjects decoy location (5 conditions, $N$ = 90/102/81/89/77), within-subject which alternative is favored. 20 consumer choice sets (computers, video cameras, etc.); half contained phantoms, half three equal options. The phantom blinked as "unavailable." Effect index = $\Pr(T\mid T\text{ favored})-\Pr(T\mid C\text{ favored})$.

**Experiment 2** — fully within-subjects (all five locations crossed with context, six replications each), $N=262$, using homogeneous grocery products described by price ($0.39–$4.19) and a 0–100 quality rating; the phantom was crossed out with a red "X." Participants were segregated post hoc into Positive ($n=79$), Low ($n=156$), and Negative ($n=27$) groups by their summed phantom-effect score; need-for-cognition and choice latency were collected as candidate moderators.

## Data
No external dataset — original lab experiments. Experiment 1: 439 undergraduates (Univ. of Alabama Huntsville and SIU Edwardsville). Experiment 2: 262 undergraduates (Univ. of South Carolina and SIUE). Stimuli are hypothetical multi-attribute consumer products; the dependent measure is choice frequency for the target across context conditions.

## Key findings
- **Robustness (Exp. 1).** Four of five phantoms produced significant positive target shifts; only $PF$ did not (effects: $PR$ .20, $PER$ .14, $PF$ .04 n.s., $PRF$ .09, $PERF$ .10). The overall $\sim$11-point between-subjects effect confirms phantom decoys generally work.
- **Discriminating contrasts (Exp. 1).** The relative advantage contrast ($PR$+$PER$ vs. $PF$+$PRF$+$PERF$) was significant, $F(1,434)=8.24$, and captured 80% of the systematic between-location variance. The range-weighting contrast ($PF$ vs. rest) was also significant ($F=4.39$) but explained only 43%. The similarity-substitution contrast (close vs. far) was nonsignificant ($F=0.05$) — no support.
- **Within-subjects (Exp. 2).** Only $PR$ (.10) and $PER$ (.05) reached significance overall, matching the relative advantage ranking; effects were about one-third the between-subjects size ($\sim$4 points; mean phantom score $M=1.17$, $t(261)=4.89$).
- **Individual differences (Exp. 2).** A Decoy $\times$ Group interaction was significant ($F(8,1036)=2.47$). The **Positive** group followed the relative advantage prediction almost exactly: the $PR$+$PER$ vs. rest contrast captured 80% of variance with *no* significant residual ($F(3,76)=0.53$ n.s.); range-weighting left significant residuals and similarity-substitution found no support. The **Low** group (the majority) showed a significant *positive* $PR$ effect but a significant *negative* $PF$ effect — explained by no single model. The **Negative** group (10%) showed uniformly negative effects, consistent with dominance-valuing / dimensional contrast.
- **Mechanism verdict.** Combined evidence supports a loss-aversion mechanism shared with the relative advantage model and the Usher–McClelland leaky-accumulator; similarity is *not* the key determinant, decisively ruled out by the null $PF$ effect.

## Contribution
First direct, parametric test pitting the three leading phantom-decoy accounts against one another by exploiting their divergent predictions across attribute-space locations, including the first empirical test of the authors' own similarity-substitution hypothesis (Pettibone & Wedell 2000) — which it falsifies. It establishes that a single loss-aversion mechanism (relative advantage; cf. leaky accumulator) parsimoniously covers phantom alongside asymmetric-dominance, inferior, and compromise decoys, and yields an applied rule: an unavailable superior alternative bolsters a target when the target's loss relative to the phantom is markedly smaller than the competitor's. It also documents systematic heterogeneity — a minority for whom phantoms *backfire*.

## Limitations & open questions
- **No model fits all subgroups.** The Low (majority) group's mixed pattern — positive $PR$ but negative $PF$ — fits none of the three models and seems to require a *two-process* account combining a target-favoring process (loss/weighting/similarity) with a target-hurting dimensional-contrast or dominance-valuing process. The authors pose specifying such a formulation as open.
- **The "boomerang"/negative effect.** Why some individuals show consistently negative phantom effects, and what conditions trigger a phantom to *adversely* affect the target, is flagged explicitly for future research.
- **No moderator found.** Neither need for cognition nor choice latency predicted the phantom-effect score; the grouping is post hoc by effect size, which the authors concede limits inference. Finding an independent predictor is left open.
- **Single-process alternatives untested.** They suggest comparison-induced-distortion (Choplin & Hummel 2005), where effect sign depends on whether the obtained attribute difference exceeds the expected one, or an MDFT (Roe et al. 2001) variant with a mediating process that reweights the phantom's favorability, as candidate single-mechanism accounts.
- **Common-vs-multiple mechanism.** A proposed design: within-subject manipulation of many decoy locations to see whether different decoy effects correlate, signaling one mechanism versus several.
- **Effect-size instability.** The large gap between between- ($\sim$11 pts) and within-subjects ($\sim$4 pts) magnitudes (number of sets, repeated $T$-$C$ pairs, task familiarity) is noted but not resolved.

## Connections
The phantom decoy traces to Pratkanis and Farquhar (1992); related demonstrations include Highhouse (1996) and the authors' Pettibone and Wedell (2000), whose similarity-substitution conjecture this paper tests and rejects. The standard asymmetric-dominance decoy literature ([[@Huber1982|Huber, Payne & Puto 1982]]; Huber & Puto 1983; [[@Simonson1989|Simonson 1989]]; Wedell 1991; Wedell & Pettibone 1996) supplies the three families of explanation — range-weighting (challenged by Mellers & Biagini 1994; Wedell 1998), value-shift / dimensional contrast (Choplin & Hummel 2005; Dhar & Glazer 1996), and relational valuation. The winning account is the relative advantage model of [[@Shafir1993|Tversky and Simonson (1993)]], grounded in the loss aversion of [[@Kahneman1979|Kahneman and Tversky's (1979)]] prospect theory; its dynamic cousins are Roe, Busemeyer and Townsend's (2001) multi-alternative decision field theory and the Usher and McClelland (2004) leaky-accumulator. Cross-species decoy effects (Shafir, Waite & Smith 2002; Hurly & Oseen 1999) are cited to argue justification is not necessary. Methodological scaffolding: Shepard (1987) on similarity-distance, range-frequency theory (Parducci 1995), the choice-is-more-lexicographic-than-judgment result (Tversky, Sattath & Slovic 1988; [[@Sen1997|Wedell & Senter 1997)]], and the need-for-cognition scale (Cacioppo, Petty & Kao 1984).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
