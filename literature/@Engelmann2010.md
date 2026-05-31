---
citekey: Engelmann2010
title: Inequality Aversion and Reciprocity in Moonlighting Games
authors: ["Engelmann, Dirk", "Strobel, Martin"]
year: 2010
type: journalArticle
doi: 10.3390/g1040459
zotero: "zotero://select/library/items/XYFHWPGC"
pdf: /Users/jesper/Zotero/storage/ZNLLJNJA/Engelmann2010.pdf
tags: [literature]
keywords: [inequality-aversion, reciprocity, moonlighting-game, social-preferences, experimental-economics, reference-points]
topics: ["[[inequity-aversion-distributional-preferences]]"]
related: [Bolton2000, Charness2002, Cox2004, Dufwenberg2004, Falk2006, Falk2008, Fehr1999]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We study behavior in a moonlighting game with unequal initial endowments. In this game, predictions for second-mover behavior based on inequality aversion are in contrast to reciprocity. We find that inequality aversion explains only few observations. The comparison to a treatment with equal endowments supports the conclusion that behavior is better captured by intuitive notions of reciprocity than by inequality aversion. Extending the model by allowing for alternative reference points promises better performance, but leads to other problems. We conclude that the fact that inequality aversion often works as a good short-hand for reciprocity is driven by biased design choices.

## Summary
Engelmann and Strobel run a one-shot moonlighting game designed so that distributional (inequality-aversion) motives and reciprocity motives make *opposite* predictions for the second mover. By raising the second mover's endowment so much that a "poor pickpocket" first mover who *takes* money is still far poorer than his victim, they break the usual lab coincidence whereby unkind actions leave the actor richer. The headline result: when the two motives conflict, reciprocity wins decisively and inequality aversion has almost no explanatory power. Inequality aversion only "works" in standard experiments because designers conventionally pick settings in which equal payoffs are the natural neutral benchmark, so the kind are poor and the unkind are rich. The paper is thus a methodological critique: inequality aversion is at best an as-if short-hand for reciprocity, not a literal preference.

## Research question
Do models of literal inequality aversion (Fehr-Schmidt, Bolton-Ockenfels) retain any predictive power for responder behavior once the implicit design assumption is broken, namely the assumption that a *kind* first-mover action leaves the second mover richer than the first mover and an *unkind* action leaves the second mover poorer? Put differently: when reciprocity and inequality aversion point in different directions, which one organizes the data, and how much of inequality aversion's apparent success is an artifact of biased experimental design?

## Method / identification
The core instrument is a modified **moonlighting game** (Abbink, Irlenbusch and Renner). Player 1 first either *takes* $\{3,6,9\}$ EMU from Player 2 (each EMU taken costs P2 one EMU) or *sends* $\{3,6,9\}$ EMU (tripled on arrival), or does nothing. Player 2 then either returns money one-for-one or assigns *reduction points* at cost 1 EMU to herself and $-3$ EMU to Player 1. Two design innovations drive identification:

1. **Strategy method.** Player 2 commits to a complete response schedule for every Player 1 action before learning the realized choice, yielding a full reaction function per subject rather than a single point.

2. **Endowment manipulation across two treatments** to dissociate the motives. In **Treatment 1** endowments are *almost equal* (P1 = 17, P2 = 18 EMU); slight inequality removes perfect equality as a focal point while keeping reciprocity and inequality aversion *aligned*. In **Treatment 2** the second mover is endowed with 48 EMU, so that even after P1 takes the maximum 9, P2 (39) still vastly out-earns P1 (26) — the "poor pickpocket." Here punishing a *taker* is reciprocal but *anti*-inequality-averse (it increases the gap from the disadvantaged party's perspective), while *rewarding* a taker is inequality-averse but anti-reciprocal.

The identification strategy is two paired cross-treatment comparisons, tested with Mann-Whitney rank-sum tests on the 23 (T1) and 24 (T2) independent Player-2 observations:
- **Same action, different inequality:** compare P2's reaction to a *given* P1 action across treatments. Reciprocity predicts no difference (P2 only cares how P1's act affected her own payoff); inequality aversion predicts a difference (resulting distributions differ).
- **Same inequality, different action:** compare P2 after "send 3" in T1 (gap $27-14$) against P2 after "take 9/6/3" in T2 (gaps $39-26$, $42-23$, $45-20$), constructed so the resulting payoff gap is equal but the *act* differs. Inequality aversion predicts identical behavior; reciprocity predicts rewards in T1 but punishment in T2. Under the linear Fehr-Schmidt model the choices after "send 3" (T1) and "take 9" (T2) should be *exactly* equal since both yield an inequality of 13.

The paper also derives qualitative predictions for explicit reciprocity models. The **Dufwenberg-Kirchsteiger** sequential-reciprocity model (with belief-dependent equitable payoff = average of max and min feasible-efficient payoffs) predicts, in a kind equilibrium, larger but less likely returns in T2, and in an unkind equilibrium more punishment in T2; its linearity forces extreme actions (send everything / punish maximally) and even makes kind equilibria self-undermining. The **Falk-Fischbacher** model, which assesses kindness by direct payoff comparison, implies *no punishment at all* in T2 (a taker is "kind" since P2 stays ahead) and weakly kinder reactions in T2. The **Cox-Friedman-Sadiraj** revealed-altruism model (Axioms R and S — reciprocity and status-quo) matches the authors' intuition: changing the status quo to favor P2 raises P2's altruism, harming it lowers altruism, with initial endowments serving as the status quo.

## Data
Original lab data: six z-Tree sessions (three per treatment, ~16 subjects each, one T1 session with 14), Royal Holloway, March 2005 and 2006, mostly undergraduates, one-shot. Yields 23 (T1) and 24 (T2) independent observations per role. Average earnings £9.13 (T1) and £15.91 (T2) at 2 EMU = £1. Player-2 full response schedules are reported subject-by-subject in Tables 2 and 3.

## Key findings
- **Result 1.** When the motives agree (T1 after taking), behavior is largely consistent (8 subjects clearly inequality-averse, 14 not rejecting it). When they conflict (T2 after taking), of the 12 non-selfish responders, 8 act against inequality aversion but in line with reciprocity (they punish the poorer taker), and only 2 are unambiguously inequality-averse.
- **Result 2.** Even when P2 returns money, it almost never equalizes payoffs — altruism rarely extends to self-sacrifice benefiting the richer player.
- **Result 3.** *Same action, different inequality*: P2's reactions do not differ significantly across treatments ($p>0.1$ for every P1 action) — refuting inequality aversion and the Falk-Fischbacher "kinder in T2" prediction.
- **Result 4.** *Same inequality, different action*: reactions differ sharply ($p<0.01$, Mann-Whitney) — "send 3" in T1 draws returns and never punishment, while "take 9/6/3" in T2 draws punishment in 8-9 of cases. This is the central evidence for reciprocity.
- **Result 5.** Dufwenberg-Kirchsteiger and Falk-Fischbacher qualitative predictions fail: punishment is rarely maximal, transfers are never maximal, punishment *does* occur in T2 (against Falk-Fischbacher), and punishment is *not* stronger in T2 (against Dufwenberg-Kirchsteiger). The Cox-Friedman-Sadiraj status-quo logic fits best — for 13 of 16 subjects who both punish and reward, "P1 takes nothing" is the turning point.
- **Result 6.** Player 1 behavior is nearly identical across treatments (mean transfer $-3$ vs $-3.63$, $p>0.5$), contradicting inequality aversion's prediction of more taking in T2.

## Contribution
The paper isolates negative reciprocity from advantageous inequality aversion within a single canonical game and shows reciprocity dominates. It reframes a large literature: the empirical success of Fehr-Schmidt / Bolton-Ockenfels models is substantially an artifact of design choices where equal payoffs are the focal neutral point (the kind are poor, the unkind rich). It complements [[@Falk2008|Falk-Fehr-Fischbacher (2008)]] by showing that when reciprocity is *not merely removed* but set *in opposition*, inequality aversion fails outright; and it mirrors the authors' own distribution-game finding (Engelmann-Strobel 2004) that subjects rarely punish blameless rich players, here adding that they readily punish blameworthy poor ones.

## Limitations & open questions
The authors are unusually explicit about boundaries and open hooks:
- **No elicited beliefs**, so only qualitative predictions for the belief-dependent Dufwenberg-Kirchsteiger and Falk-Fischbacher models could be tested — a clean replication eliciting first- and second-order beliefs is an open task.
- **The design tests negative reciprocity against advantageous inequality aversion**, which may bias toward reciprocity since negative reciprocity is more robust than positive, while Fehr-Schmidt assumes disadvantageous-inequality aversion exceeds advantageous.
- **Reference-point extension is not a fix.** Re-centering Fehr-Schmidt on the "do-nothing" allocation (a) predicts *no* T1-T2 difference, contradicting the small observed differences; (b) requires identifying a neutral action that is often ambiguous (e.g., the neutral wage in a gift-exchange game when the selfish-equilibrium wage is small but positive); (c) makes the model labelling-dependent — relabelling "take" as "send less" should, and probably would, change behavior, yet a general inequality-aversion model must be label-invariant. Allowing *heterogeneous* reference points renders the model untestable (it can fit anything).
- **Entitlement-based reference points also fail**: in the ultimatum game unequal endowments are *not* accepted as a neutral status quo, so the entitlement story does not generalize.
- The experiment was **not purpose-built to test Cox-Friedman-Sadiraj** (it predates it); the authors flag an ideal three-treatment design in which P2 faces the *identical budget set* after a take in the asymmetric treatment, a send in the symmetric treatment, and a neutral action — letting all behavioral differences be attributed cleanly to the status-quo shift.

## Connections
Directly extends [[@Falk2008|Falk, Fehr and Fischbacher]] (2008, *GEB*), whose random-move moonlighting treatment removed reciprocity; this paper instead opposes it. It builds on the moonlighting game of Abbink, Irlenbusch and Renner (2000). The targets of critique are the inequality-aversion models of [[@Fehr1999|Fehr and Schmidt (1999)]] and [[@Bolton2000|Bolton and Ockenfels]] (2000, ERC). It situates against the explicit reciprocity theories of [[@Dufwenberg2004|Dufwenberg and Kirchsteiger (2004)]], [[@Falk2006|Falk and Fischbacher (2006)]], and especially Cox, Friedman and Sadiraj (2008, "Revealed Altruism"), whose status-quo Axiom S best rationalizes the data. The distributional backdrop — that efficiency and maximin often beat inequality aversion — comes from [[@Charness2002|Charness and Rabin (2002)]] and the authors' own Engelmann and Strobel (2004, *AER*) and (2007). Related identification strategies appear in [[@Cox2004|Cox (2004)]], Kagel and Wolfe (2001), and Bolton, Brandts and Ockenfels (1998). The trust/investment paradigm referenced is Berg, Dickhaut and McCabe (1995).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
