---
citekey: Fischbacher2001
title: Are people conditionally cooperative? Evidence from a public goods experiment
authors: ["Fischbacher, Urs", "Gächter, Simon", "Fehr, Ernst"]
year: 2001
type: journalArticle
doi: 10.1016/S0165-1765(01)00394-9
zotero: "zotero://select/library/items/BMKLA4TT"
pdf: /Users/jesper/Zotero/storage/NJDMUVXH/Fischbacher2001.pdf
tags: [literature]
keywords: [conditional-cooperation, public-goods-game, strategy-method, free-riding, social-preferences, experimental-economics]
topics: []
related: [Bolton2000, Dufwenberg2004, Fehr1999, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We study the importance of conditional cooperation in a one-shot public goods game by using a variant of the strategy-method. We find that a third of the subjects can be classified as free riders, whereas 50% are conditional cooperators.

## Summary
Fischbacher, Gächter, and Fehr directly elicit individuals' willingness to cooperate conditionally in a one-shot linear public goods game using a variant of Selten's strategy method. Rather than inferring conditional cooperation indirectly from contribution dynamics, they ask each subject for a full "contribution table" specifying how much they would contribute for every possible average contribution of the other group members. About 50% of subjects are conditional cooperators (own contribution rises with others'), roughly 30% are pure free riders, and 14% display hump-shaped schedules. Crucially, conditional cooperators contribute with a "self-serving bias," sitting at or below the 45-degree diagonal, which the authors argue mechanically explains the ubiquitous decay of contributions in repeated public goods experiments.

## Research question
Are people conditionally cooperative — i.e., willing to contribute more to a public good the more others contribute — and is this heterogeneous motivation, combined with free riding, sufficient to explain the well-documented decline of cooperation over repetitions in public goods games?

## Method / identification
The setting is a standard linear public goods game (Ledyard, 1995) with four players. Each subject is endowed with 20 tokens and chooses $g_i$, with the payoff function
$$\pi_i = 20 - g_i + 0.4 \sum_{j=1}^{4} g_j.$$
The marginal per-capita return of 0.4 implies that complete free riding ($g_i = 0$) is the dominant strategy for a rational, selfish player, while the social optimum is full contribution.

The identification innovation is a variant of the strategy method (Selten, 1967). Each subject makes two decisions without knowing the others': (i) an unconditional contribution (a single number), and (ii) a contribution table — a vector specifying, for each of the 21 possible rounded average contributions of the other three members ($0,1,\dots,20$), how much the subject would contribute. To make all entries incentive-compatible, a random mechanism (a 4-sided die) selects, in each group, exactly one player for whom the contribution table becomes payoff-relevant; for the other three, their unconditional contribution counts. Each subject thus faces probability $1/4$ that the schedule is binding, ensuring every table entry is potentially payoff-relevant.

Formally the design is an extensive-form game: nature picks three players who contribute simultaneously; the fourth observes their rounded average and best-responds via the table. For the fourth player, contributing zero is optimal regardless of others, so under rationality and selfishness the entire schedule should be all zeros — making any increasing schedule an unambiguous measure of conditional cooperation. The game is played only once (no repetition), deliberately ruling out reputation or repeated-game motives so that increasing schedules reflect preferences rather than strategic intertemporal calculation.

## Data
44 subjects (first- and second-semester undergraduates from various fields, excluding economics) at the University of Zurich computerized lab, run in two sessions using the z-Tree software (Fischbacher, 1999). Subjects formed 11 independent groups of four; because each played only once, all 44 contribution schedules are independent observations. Subjects first passed 10 control questions (all solved correctly). Average earnings were 27.6 Swiss Francs (about \$21), a deliberately high stake.

## Key findings
- **Average conditional cooperation:** The mean contribution schedule is clearly increasing in others' average contribution (Fig. 1); on average subjects are conditional cooperators rather than free riders, despite the one-shot nature.
- **Three types at the individual level (Fig. 2):**
  - *Conditional cooperators* — 22 subjects (50%). Sixteen are increasing and weakly monotonic; four are "perfect" conditional cooperators lying exactly on the diagonal (matching others). All have positive, 1%-significant Spearman rank correlations between own and others' contributions.
  - *Free riders* — 13 subjects (~30%), submitting all-zero schedules.
  - *Hump-shaped* — 6 subjects (14%): near-perfect conditional cooperation up to others contributing ~10 tokens, then declining.
  - *Other/unclassifiable* — 3 subjects.
- **Self-serving bias:** Only 11.9% of conditional cooperators' entries lie strictly above the diagonal; the bulk sit at or below it. Behavior is best described as "conditional cooperation with a self-serving bias."
- **Unconditional contributions** averaged 6.7 tokens (33.5% of endowment), consistent across types (free riders 2.0; conditional cooperators 8.4; hump-shaped 9.0).
- **Explaining decay:** Because some subjects free ride unconditionally and conditional cooperators systematically undershoot the diagonal, contributions in repeated play are predicted to "spiral downwards," producing the positive-but-deteriorating contribution paths seen across experiments.
- **Stability check:** A post-experimental hypothetical re-elicitation produced near-identical schedules, supporting the assumption that the elicited preferences are stable.

## Contribution
The paper provides the first clean, direct, incentive-compatible measurement of conditional cooperation at the individual level using the strategy method, distinguishing it from prior indirect inferences (Croson, 1998; Keser & van Winden, 2000; Brandts & Schram, 2001; Sonnemans et al., 1999). It establishes a now-canonical type taxonomy (conditional cooperators, free riders, hump-shaped) and offers a parsimonious preference-based explanation for the universal decline of cooperation, anchoring later work on heterogeneous social preferences and mechanism design that exploits conditional cooperation.

## Limitations & open questions
- **Stability across experience:** The downward-spiral interpretation hinges on schedules not changing with experience; the authors test this only via a hypothetical questionnaire, explicitly flagging stability as an assumption rather than a demonstrated fact.
- **Group composition:** They note the speed of convergence "depends on the actual composition of the group," leaving the dynamics of heterogeneous-type groups unmodeled.
- **Motivational source:** Conditional cooperation could reflect altruism, warm glow, inequity aversion, or reciprocity; the design does not discriminate among these underlying motives.
- **Out-of-equilibrium unconditional play:** They set aside whether non-zero unconditional contributions are best responses to beliefs about conditional cooperators (relaxing common knowledge of rationality), focusing only on the schedule.
- **External validity:** Small sample (44 subjects), one-shot, anonymous, student subjects.

## Connections
The conditional-cooperation motive is closely tied to reciprocity models such as [[@Rabin1993|Rabin (1993)]] and [[@Dufwenberg2004|Dufwenberg & Kirchsteiger (2004)]], and to distributional social-preference models including [[@Fehr1999|Fehr & Schmidt (1999)]] inequity aversion and [[@Bolton2000|Bolton & Ockenfels (2000)]] ERC, all candidate microfoundations the paper deliberately leaves open. The experimental antecedents on public goods decay include Andreoni (1995) on kindness versus confusion, Palfrey & Prisbrey (1997) on anomalous behavior, and the survey by Ledyard (1995); contemporaneous indirect evidence on conditional cooperation appears in Keser & van Winden (2000), Sonnemans, Schram & Offerman (1999), and Brandts & Schram (2001), with comparable results in Ockenfels (1999). The strategy method itself originates with Selten (1967), and the z-Tree platform is Fischbacher (1999). The paper's type taxonomy directly motivates later structural estimation of social-preference type mixtures, e.g. Bardsley & Moffatt (2007) and Fischbacher & Gächter (2010), which builds on this same elicitation to model belief-driven contribution dynamics.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
