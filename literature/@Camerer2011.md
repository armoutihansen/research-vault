---
citekey: Camerer2011
title: Advances in Behavioral Economics
authors: ["Camerer, Colin F.", "Loewenstein, George", "Rabin, Matthew"]
year: 2011
type: book
doi: 10.2307/j.ctvcm4j8j
zotero: "zotero://select/library/items/RPLHT984"
pdf: /Users/jesper/Zotero/storage/UCIPBW8V/Camerer2011.pdf
tags: [literature]
keywords: [fairness, reciprocity, psychological-games, social-preferences, behavioral-game-theory, fairness-equilibrium, ultimatum-game]
topics: []
related: [Akerlof1982, Bolton2000, Dufwenberg2004, Falk2006, Fehr1999]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Although the Zotero record labels this item the Camerer-Loewenstein-Rabin edited volume *Advances in Behavioral Economics* (2011), the attached PDF is the reprinted source chapter: Matthew Rabin's "Incorporating Fairness into Game Theory and Economics" (*American Economic Review* 83(5), 1993, pp. 1281-1302). The paper builds a general game-theoretic model of fairness in which a player's utility depends not only on material payoffs but also on his beliefs about how kind or unkind the other player is being to him. People want to be kind to those who are kind and to hurt those who are unkind, and these motives matter more when material stakes are small. The resulting solution concept, *fairness equilibrium*, can both add equilibria to and eliminate equilibria from standard analysis, organizing experimental regularities (public-goods cooperation, ultimatum rejections) under common principles.

## Research question
Will adding fairness considerations to economic models substantially alter their conclusions, and if so, in which strategic situations and in what direction? More foundationally: how can the psychological facts that people reciprocate kindness and punish unkindness be incorporated into the *general* apparatus of noncooperative game theory, rather than via context-specific models?

## Method / identification
The formal device is a **psychological game** in the sense of Geanakoplos, Pearce, and Stacchetti (1989, "GPS"), where payoffs depend on beliefs as well as actions. Rabin's innovation is to *derive* the psychological game from an underlying two-player, finite-strategy "material game" with material payoff functions $\pi_i$, using fairness assumptions, so the model can be compared directly to standard analysis.

Each player tracks three objects: his action $a_i$, his belief $b_j$ about the other's strategy, and his belief $c_i$ about the other's belief about his own strategy. Given $b_j$, the feasible payoff set is $\Pi(b_j)=\{(\pi_i(a_i,b_j),\pi_j(b_j,a_i)) : a_i \in S_i\}$. Let $\pi_j^h(b_j)$ and $\pi_j^l(b_j)$ be player $j$'s highest and lowest Pareto-efficient payoffs in $\Pi(b_j)$, define the **equitable payoff** $\pi_j^e(b_j)=[\pi_j^h(b_j)+\pi_j^l(b_j)]/2$, and let $\pi_j^{\min}(b_j)$ be $j$'s worst feasible payoff. The **kindness function** is

$$f_i(a_i,b_j)=\frac{\pi_j(b_j,a_i)-\pi_j^e(b_j)}{\pi_j^h(b_j)-\pi_j^{\min}(b_j)}$$

(set to $0$ if the denominator is $0$). Symmetrically, $\tilde f_j(b_j,c_i)$ is player $i$'s belief about how kind $j$ is being to him. Utility is

$$U_i(a_i,b_j,c_i)=\pi_i(a_i,b_j)+\tilde f_j(b_j,c_i)\cdot\big[1+f_i(a_i,b_j)\big].$$

The multiplicative second term encodes reciprocity: if $\tilde f_j<0$ (I am treated unkindly) player $i$ gains utility from lowering $f_i$ (hurting $j$); if $\tilde f_j>0$ he gains from raising it. Kindness terms are normalized to $[-1,\tfrac12]$ and are invariant to positive affine transformations of material payoffs, while overall utility is not; because the fairness term is bounded, larger material stakes mechanically dominate it (stylized fact C). A **fairness equilibrium** is a psychological Nash equilibrium: a strategy pair $(a_1,a_2)$ with $a_i\in\arg\max_{a\in S_i}U_i(a,b_j,c_i)$ and the consistency condition $c_i=b_j=a_i$ (beliefs match behavior at all orders). Stakes are parameterized by a scale variable $X$ multiplying all material payoffs, so the family $G(X)$ isolates the effect of stake size on the strategic structure. Two auxiliary outcome classes drive the results: **mutual-max**, where each $a_i\in\arg\max_{a}\pi_j(a,a_j)$, and **mutual-min**, where each $a_i\in\arg\min_{a}\pi_j(a,a_j)$.

## Data
None - this is a pure theory paper. It cites laboratory evidence (public-goods experiments surveyed by Dawes and Thaler 1988; ultimatum-game experiments via Thaler 1988, Guth et al. 1982, Roth et al. 1991; Kahneman, Knetsch, and Thaler 1986 on price fairness) as motivation for its three stylized facts, but estimates no quantities and runs no experiment.

## Key findings
Worked through six 2x2-style examples (Battle of the Sexes, Prisoner's Dilemma, Prisoner's "Non-Dilemma," Chicken, the Grabbing Game, Leaving a Partnership), the paper proves six propositions:
- **Proposition 1.** Any Nash equilibrium that is also a mutual-max or mutual-min outcome is a fairness equilibrium.
- **Proposition 2.** Every fairness equilibrium is either *strictly positive* (both $f_i>0$) or *weakly negative* (both $f_i\le0$): kindness is symmetric in equilibrium; one player is never kind while the other is unkind.
- **Proposition 3.** Every strictly positive mutual-max outcome and every strictly negative mutual-min outcome is a fairness equilibrium for $X$ small enough.
- **Proposition 4.** An outcome that is neither mutual-max, nor mutual-min, nor (a qualifying) Nash equilibrium is *not* a fairness equilibrium for small $X$. Together 3-4: for small stakes, fairness equilibria are roughly the mutual-max and mutual-min outcomes.
- **Proposition 5.** For large $X$, strict Nash equilibria are fairness equilibria and non-Nash outcomes are not: fairness equilibria collapse to the Nash set as stakes grow.
- **Proposition 6 ("unhappy theorem").** Every game has at least one weakly negative fairness equilibrium - it is never guaranteed that players part on good terms. The asymmetry arises because being kind requires sacrificing material payoff, so self-interest can tempt meanness toward a kind partner but never tempts kindness toward a mean one.

Applications: a monopolist faces a fairness-constrained consumer (reservation price $r=v$) and can only sell below the classical monopoly price; the consumer views any $p>c$ as unfair ($f_M(z,z)=[c-z]/2[v-c]<0$), and willingness to pay rises with the firm's cost $c$ (rationalizing Thaler 1985). A gift-exchange labor model yields a "gift-giving" equilibrium with effort $e=H$ and bonus $b^*=R/(1+4R)$ only when $R<0.25\,[1/(0.5+\gamma)^{1/2}-1]$; if disutility $\gamma\ge2$ no cooperative equilibrium exists for any $R$.

## Contribution
Provides the first *general* formal model of reciprocal fairness applicable to all two-person complete-information games, embedding intentions (kindness inferred from foregone alternatives, as in the Prisoner's Non-Dilemma) directly into utility. It unifies seemingly disparate behaviors - ultimatum rejection, public-goods cooperation, below-monopoly pricing, efficiency wages - under one reciprocity principle, and shows fairness can both create and destroy equilibria. It is a foundational reference for the intentions-based stream of social-preference theory (later Dufwenberg-Kirchsteiger, Falk-Fischbacher) and for welfare analysis that counts agents' own fairness concerns, not just the planner's.

## Limitations & open questions
The author explicitly flags these as future work:
- **Reference dependence.** The kindness benchmark ignores the status quo and history; Kahneman et al. (1986) show price-fairness judgments depend heavily on what a firm charged before.
- **More than two players.** Behavior is unclear when an agent is hostile to some and friendly to others but cannot target (e.g., a single public-goods contribution: reward contributors or punish free-riders?).
- **Incomplete information.** Because motives are inferred from beliefs about payoffs and information, asymmetric information should dramatically reshape behavior; extending the model here is "essential for applied research."
- **Sequential games / forcing emotions.** Observing past play can change motivations, not merely convey information; can a first-mover *compel* positive regard, perhaps overturning Proposition 6?
- **Additional emotions (trust).** In the partnership game (Example 6) the model predicts only the inefficient (dissolve) outcome, missing plausible trust-rewarding cooperation - rewarding trust per se is not yet captured.
- **Existence and continuity.** The specific kindness function is not everywhere continuous, so the GPS existence theorem does not formally apply (no counterexample found); a single shared kindness function and pure-strategy emphasis are simplifications.
- **Magnitudes are only qualitative**: units of material payoff and the relative weight of fairness versus self-interest are not pinned down.

## Connections
Builds directly on Geanakoplos, Pearce, and Stacchetti (1989) and Gilboa-Schmeidler (1988) for psychological games, and on Akerlof's (1982) gift-exchange labor model and [[@Akerlof1982|Akerlof-Dickens (1982)]] belief-dependent utility. It is the intentions-based counterweight to the later *distributional* social-preference models of [[@Fehr1999|Fehr and Schmidt (1999)]] and [[@Bolton2000|Bolton and Ockenfels (2000)]], which condition on outcomes rather than motives; subsequent work ([[@Dufwenberg2004|Dufwenberg and Kirchsteiger 2004]]; [[@Falk2006|Falk and Fischbacher 2006]]) generalizes Rabin's reciprocity to sequential and richer games, addressing several open questions above. As a reprint in Camerer, Loewenstein, and Rabin's *Advances in Behavioral Economics*, it anchors the behavioral game-theory canon alongside ultimatum-game evidence (Guth et al. 1982; Roth et al. 1991) and price-fairness surveys (Kahneman, Knetsch, and Thaler 1986).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
