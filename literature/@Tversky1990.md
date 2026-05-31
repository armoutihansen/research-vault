---
citekey: Tversky1990
title: The Causes of Preference Reversal
authors: ["Tversky, Amos", "Slovic, Paul", "Kahneman, Daniel"]
year: 1990
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/HI4J2HS3"
pdf: /Users/jesper/Zotero/storage/INJ22AEA/Tversky1990.pdf
tags: [literature]
keywords: [preference-reversal, procedure-invariance, scale-compatibility, contingent-weighting, intransitivity, time-preference]
topics: ["[[prospect-theory-loss-aversion]]"]
related: [Grether1979, Kahneman1979]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Observed preference reversal (PR) cannot be adequately explained by violations of independence, the reduction axiom, or transitivity. The primary cause of PR is the failure of procedure invariance, especially the overpricing of low-probability high-payoff bets. This result violates regret theory and generalized (nonindependent) utility models. PR and a new reversal involving time preferences are explained by scale compatibility, which implies that payoffs are weighted more heavily in pricing than in choice.

## Summary

Tversky, Slovic, and Kahneman dissect the classic preference-reversal (PR) phenomenon — where people *choose* a high-probability "H bet" over a low-probability high-payoff "L bet" yet assign a *higher selling price* to L — and ask which axiom of rational choice it really violates. Through an extended three-option experimental design and a novel "ordinal payoff scheme," they show that PR is driven overwhelmingly (~90% of test patterns) by a failure of **procedure invariance**, not by intransitivity, nonindependence, or violations of the reduction axiom. The specific culprit is the **overpricing of L bets**, which they explain via **scale compatibility**: because both prices and payoffs are denominated in dollars, payoffs receive greater weight in pricing than in choice. They confirm the same mechanism produces a new reversal in intertemporal choice.

## Research question

PR is robust and survives incentive-compatible elicitation, but its *cause* is unsettled. Three rival explanatory families had been proposed: (a) nontransitive-choice models (Loomes-Sugden regret theory; Fishburn's SSB), (b) response-bias / procedure-invariance models (Tversky-Sattath-Slovic contingent weighting), and (c) generalized (nonindependent) utility models (Holt; Karni-Safra; Segal). The paper asks: which axiom does PR actually violate — transitivity, procedure invariance, independence, or the reduction axiom — and can the dominant cause be pinned down empirically?

## Method / identification

The core methodological contribution is a **diagnostic decomposition**. Let $C_H$ and $C_L$ be the cash equivalents (minimum selling prices) of bets $H$ and $L$; let $\succ$ denote strict preference over options and $>$ ordering of cash amounts, with monetary consistency $X>Y \Rightarrow X\succ Y$. A standard PR is $H\succ L$ together with $C_L>C_H$. Procedure invariance is the requirement $B\succ X \iff C_B>X$. The authors prove that any PR pattern satisfying the test condition $H\succ L$ and $C_L>X>C_H$ must violate **either** transitivity **or** invariance, and that the two cannot fail simultaneously within this three-option design. Inserting a sure amount $X$ between the two prices and eliciting the three choices $H$-$L$, $H$-$X$, $L$-$X$ partitions every PR pattern into exactly four mutually exclusive cells:

- (1) Intransitivity: $L\succ X\succ H$, yielding the cycle $L\succ X\succ H\succ L$.
- (2) Overpricing of L (OL): $X\succ H$ and $X\succ L$, i.e. $C_L\succ X\succ L$.
- (3) Underpricing of H (UH): $H\succ X$ and $L\succ X$, i.e. $H\succ X\succ C_H$.
- (4) Both OL and UH: $H\succ X$ and $X\succ L$.

To neutralize the rival nonindependence explanation, they introduce the **ordinal payoff scheme**: subjects separately price each bet and separately choose within pairs; one pair is drawn at random and a coin flip decides whether the subject plays the bet they *chose* or the bet they *priced higher*. Because prices are used only to *order* bets within a pair, choice and pricing are strategically equivalent, and rationalizing systematic reversals would require preferring an even-chance mixture of $H$ and $L$ to either alone — which can produce random but not systematic reversals. This severs PR from the independence and reduction axioms (which are only invoked to justify the BDM scheme). Study 2 transports the same design to **intertemporal choice**, with delayed payments $(X,T)$ (receive \$X, T years hence), short-term $S$, long-term $L$, and immediate $X$. They also formalize the contingent-weighting representation: $B=(P,X)$ is chosen over $B'=(P',X')$ iff $\log P+\alpha\log X>\log P'+\alpha\log X'$ and priced above $B'$ iff $\log P+\beta\log X>\log P'+\beta\log X'$. Invariance entails $\beta=\alpha$; **compatibility predicts $\beta>\alpha$**.

## Data

Original experiments. Study 1: 198 subjects (main group; 179 with complete data) recruited via newspaper ads at the University of Oregon, median age 22, run in class settings for pay; plus 179 subjects with real monetary incentives (15% played for real). Eighteen triples of (H, L, X) of roughly equal expected value, in three sets spanning small bets, payoffs scaled ×25, and long shots; probabilities expressed as multiples of 1/36. Study 2 (time preferences): 169 subjects on four triples; a follow-up of 184 subjects substituted attractiveness ratings (0-20) for pricing. A 42-subject Stanford sub-study tested the mixed-strategy hypothesis directly.

## Key findings

- **PR is pervasive and incentive-insensitive.** H chosen over L 74% of the time, yet $C_H>C_L$ in only 34%; standard reversals (45%) dwarf nonstandard ones (4%). Real monetary incentives left the rate essentially unchanged (46% vs 44%).
- **The diagnostic decomposition (Table 3, 620 patterns):** only **10% intransitive**; **90% non-invariant**, of which overpricing of L (65.5%) dominates underpricing of H (6.1%); both = 18.4%. This refutes regret theory, which predicts 100% intransitivity, and rules out generalized-utility/nonindependence accounts, since PR is no more frequent under BDM than under the ordinal scheme. No subject favored the mixed strategy.
- **Scale compatibility confirmed.** Fitting the contingent-weighting model subject-by-subject, $\beta>\alpha$ for 87% of subjects (greater risk aversion in choice than pricing). Nonmonetary payoffs cut PR from 41% to 24%; in a matching task the matched attribute is weighted more heavily, so probability matches imply 73% preference for H vs only 49% from payoff matches.
- **Study 2 generalizes to time:** S chosen over L 74% of the time but priced higher only 25%, giving >50% PR; the decomposition again shows overpricing of the long-term prospect L as the dominant cause (54.8%). With *ratings* instead of pricing, PR collapses to 11% and rating tracks choice — consistent with compatibility rather than singular-vs-comparative evaluation.

## Contribution

The paper reframes PR from a transitivity violation into a violation of **procedure invariance**, isolating overpricing of low-probability high-payoff bets as the mechanism and grounding it in scale compatibility. It refutes the then-fashionable rescue of PR via generalized (nonindependent) utility theory and regret theory. Methodologically, the three-option diagnostic and ordinal payoff scheme provide a clean axiom-attribution tool. Conceptually, the authors elevate **invariance** (both description invariance / framing and procedure invariance / elicitation) above independence or transitivity as the deepest threat to rational-choice theory, concluding that no theory can be simultaneously normatively acceptable and descriptively adequate because invariance is "normatively unassailable and descriptively incorrect."

## Limitations & open questions

- The ordinal payoff scheme "requires, in effect, the ranking of all bets," which **might induce intransitive subjects to behave transitively**, possibly underestimating the contribution of intransitivity — the authors argue against this but cannot rule it out.
- Compatibility **does not explain several secondary effects**: the occurrence of systematic intransitivities and the occasional underpricing of H bets remain unaccounted for; a separate **prominence** effect is invoked as an additional, distinct factor.
- The reconciliation of normative and descriptive decision theory is declared infeasible — an open challenge they leave to "descriptive models of much greater complexity" requiring explicit framing and context-dependent weighting.
- Whether a more elaborate (>3 option) design would reveal joint transitivity-and-invariance violations is left open.

## Connections

This is a capstone of the Lichtenstein-Slovic (1971, 1973) PR program and a direct rebuttal to the economists' challenge of [[@Grether1979|Grether and Plott (1979)]]. It defeats the nonindependence rescue of Holt (1986), Karni and Safra (1987), and Segal (1988), and the intransitivity-based regret theory of Loomes and Sugden (1982, 1983) and Fishburn's SSB (1984, 1985). The scale-compatibility / contingent-weighting machinery comes from Tversky, Sattath, and Slovic (1988) and Slovic, Griffin, and Tversky (1990); the BDM elicitation it scrutinizes is Becker, DeGroot, and Marschak (1964). It sits alongside Tversky and Kahneman (1986) on framing (description invariance) and prospect theory ([[@Kahneman1979|Kahneman and Tversky 1979]]), and connects to Bostic, Herrnstein, and Luce (1990) and Schkade and Johnson (1989, process evidence). Within choice modeling broadly, it is a foundational demonstration that elicitation method is not a neutral window onto a fixed preference — a caution central to any structural estimation of preferences from choice or valuation data.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
