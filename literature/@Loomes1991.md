---
citekey: Loomes1991
title: Observing Violations of Transitivity by Experimental Methods
authors: ["Loomes, Graham", "Starmer, Chris", "Sugden, Robert"]
year: 1991
type: journalArticle
doi: 10.2307/2938263
zotero: "zotero://select/library/items/827YBJWI"
pdf: /Users/jesper/Zotero/storage/2CRF8C6H/Loomes1991.pdf
tags: [literature]
keywords: [preference-reversal, transitivity, regret-theory, choice-under-uncertainty, experimental-economics, non-expected-utility]
topics: []
related: [Grether1979, Kahneman1979, Loomes1986, Loomes1987, Quiggin1982, Tversky1981, Tversky1990]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The preference reversal phenomenon is usually interpreted as evidence of nontransitivity of preference, but has also been explained as the result of: the difference between individuals' responses to choice and valuation problems; the devices used by experimenters to elicit valuations; and the "random lottery selection" incentive system. This paper reports an experiment designed so that none of these factors could generate systematic nontransitivities; yet systematic violations of transitivity were still found. The pattern of violation was analogous with that found in previous preference reversal experiments and is consistent with regret theory.

## Summary
Loomes, Starmer, and Sugden design a preference-reversal experiment built entirely from binary choices over carefully constructed triples of gambles, stripping away the certainty-equivalent valuation tasks, the BDM elicitation device, and any reliance on the random-lottery-selection (RLS) incentive scheme being treated naively. These were precisely the three loopholes that Holt (1986), Karni & Safra (1987), and Segal (1988) had used to argue that classic preference reversals might be reconciled with transitive preferences (under failures of independence or reduction). Across 200 subjects facing pairwise choices over ten triples, the authors still find systematic intransitive cycles, asymmetrically biased toward the direction predicted by regret theory. The null of equal-frequency cycles is rejected at $p<10^{-13}$, casting serious doubt on the descriptive validity of the transitivity axiom itself.

## Research question
Can systematic violations of transitivity be observed in an experiment that is immune to the three "rational-choice" rescue arguments for preference reversal, namely (a) choice-vs-valuation response disparities, (b) the BDM certainty-equivalent elicitation device interacting with independence-axiom failures, and (c) the random-lottery-selection incentive system combined with non-independent preferences over compound lotteries? If so, are the cycles asymmetric in the direction regret theory predicts?

## Method / identification
The design is a pure pairwise-choice test of transitivity. Each subject confronts triples of actions $A,B,C$ of the structure in the paper's Table I. The authors use the regret-theory formulation of [[@Loomes1987|Loomes & Sugden (1987)]]: for actions $A_i=(x_{i1},\dots,x_{in})$ and $A_k=(x_{k1},\dots,x_{kn})$ over states $j$ with probability $p_j$, preference is governed by a skew-symmetric advantage function $\Psi(\cdot,\cdot)$:
$$A_i \succeq A_k \iff \sum_j p_j\,\Psi(x_{ij},x_{kj}) \geq 0.$$
Three restrictions are imposed: (i) skew-symmetry, $\Psi(x,y)=-\Psi(y,x)$ (hence $\Psi(x,x)=0$); (ii) increasingness in the first argument for money; and (iii) regret-aversion (convexity): for $x>y>z$, $\Psi(x,z)>\Psi(x,y)+\Psi(y,z)$. Summing the three pairwise inequalities for a cycle and using skew-symmetry and regret-aversion, the authors prove that one cyclic direction (the "predicted cycle" $B\succ A,\ C\succ B,\ A\succ C$) is consistent with regret theory while the opposite ("unpredicted cycle") is not.

The triples are built (Table II is a special case of Table I) so that $A$ plays the role of a \$-bet (large prize, low probability) and $B$ a P-bet (modest prize, high probability), with $C$ a near-certain payoff. Crucially every transitive ordering of $A,B,C$ remains consistent with both EUT and regret theory, so the only discriminating signal is the *direction* of cycles. For each triple the three pairwise choices yield $2^3=8$ response patterns: six are transitive orderings, one is the predicted cycle, one the unpredicted cycle. Under transitivity (with no error), cycles can arise only under complete indifference, in which case predicted and unpredicted cycles should appear with equal frequency — this equal-frequency claim is the **null hypothesis**. The authors show this null also follows from Holt's hypothesis: if a subject treats the whole 20-question experiment as a single reducible compound lottery with transitive preferences over reduced lotteries, then by the reduction principle the $Z$+(vii) and $Z$+(viii) compound lotteries are identical, so (vii) and (viii) are again equiprobable. Thus the equal-frequency null holds whether or not RLS is valid. The composite alternative is: RLS is valid and subjects choose per regret theory, implying predicted cycles dominate. Test: one-tailed binomial.

## Data
Original experiment: 200 subjects, randomly split into Subsample I (100 subjects, Triples 1–5) and Subsample II (100, Triples 6–10), each facing 20 pairwise choice problems (15 from five triples plus 5 dominance checks reported elsewhere). Payoffs in UK pounds, choices displayed as grids over numbered sealed-envelope tickets; one of 20 questions selected by a 20-sided die and played for real (RLS). Subjects could review and revise all answers, deliberately permitting Holt-style whole-experiment optimization.

## Key findings
- For every one of the ten triples, predicted cycles outnumber unpredicted ones; in seven triples (1–6 and 8) the null of equal cycle frequency is rejected ($p<0.01$, one-tailed binomial). Cyclical responses (vii)+(viii) account for 14–29% of observations per triple.
- Taking the subject as unit (Table V): of 200 subjects, 98 cycled only in the predicted direction, 19 only in the unpredicted direction, 72 had no cycles, 11 both. The equal-frequency null is rejected at $p<10^{-13}$.
- The theoretical result: under regret-aversion, the predicted cycle direction is generic (occurs for some parameters and some $\Psi$) while the unpredicted direction is impossible. This links the experimentally observed asymmetry directly to the regret-aversion property of $\Psi$.
- Because the design uses only binary choices, the observed asymmetry cannot be attributed to choice/valuation disparities (Slovic–Lichtenstein), to the BDM device (Karni–Safra, Segal), nor — given transitive preferences over reduced lotteries — to RLS (Holt).

## Contribution
Provides the cleanest demonstration to its date that preference reversals reflect genuine, systematic intransitivity of preference rather than artifacts of valuation elicitation or incentive mechanisms. It converts regret theory from a post-hoc rationalization into a falsifiable, directional prediction about pairwise-choice cycles, and supplies strong evidence against transitivity as a descriptive axiom — a foundational empirical anchor for non-transitive (regret/disappointment) theories of choice under uncertainty.

## Limitations & open questions
- The alternative hypothesis is composite: rejecting the null jointly affirms RLS validity *and* regret-theoretic choice. The authors lean on independent "isolation effect" evidence ([[@Kahneman1979|Kahneman & Tversky 1979]]; [[@Tversky1981|Tversky & Kahneman 1981]]; Holler 1983) that RLS is valid, but cannot internally separate these components.
- The discriminating power rests on the special construction of Table II (the $\$$-bet's winning event being a subset of the P-bet's, and $d>e$). If either special assumption is relaxed, regret theory permits cycles in *both* directions (Loomes, Starmer & Sugden 1989), so the directional test does not generalize to arbitrary gamble pairs.
- Regret theory is offered as the only known hypothesis consistent with the data; the authors do not rule out as-yet-unproposed transitive explanations, only the three then-extant ones.
- The dominance-violation questions embedded in the design are deferred to a separate paper, leaving the interaction of intransitivity and dominance unexplored here.

## Connections
Directly answers the independence/reduction-based rescue arguments of Holt (1986), Karni & Safra (1987), and Segal (1988), and is a methodological sibling of Cox & Epstein (1989), who likewise test preference reversal without the independence axiom but via framing of single-choice vs valuation pairs. It builds on the regret-theory program of Loomes & Sugden (1982, 1983, 1987) and Loomes, Starmer & Sugden (1989), and on the disappointment/dynamic-consistency model of [[@Loomes1986|Loomes & Sugden (1986)]]. The phenomenon traces to Lichtenstein & Slovic (1971) and Lindman (1971), brought to economists by [[@Grether1979|Grether & Plott (1979)]], with the information-processing interpretation of Slovic & Lichtenstein (1983) and the large-sample evidence of [[@Tversky1990|Tversky, Slovic & Kahneman (1990)]]. The generalized non-expected-utility theories invoked include Machina (1982), weighted utility (Chew & MacCrimmon 1979; Fishburn 1983), and rank-dependent utility ([[@Quiggin1982|Quiggin 1982]]; Yaari 1987), all of which retain transitivity and are therefore distinguished from regret theory by this design. The BDM mechanism is from Becker, DeGroot & Marschak (1964); the acts framework from Savage (1954).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
