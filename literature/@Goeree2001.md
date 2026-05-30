---
citekey: Goeree2001
title: Ten Little Treasures of Game Theory and Ten Intuitive Contradictions
authors: ["Goeree, Jacob K.", "Holt, Charles A."]
year: 2001
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/IL3CKBUF"
pdf: /Users/jesper/Zotero/storage/92887QUQ/Goeree2001.pdf
tags: [literature]
keywords: [experimental-game-theory, quantal-response-equilibrium, one-shot-games, nash-equilibrium, bounded-rationality, noisy-introspection, coordination-games]
topics: []
related: [Bolton2000, Fehr1999, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper reports laboratory data for games that are played only once. These games span the standard categories: static and dynamic games with complete and incomplete information. For each game, the treasure is a treatment in which behavior conforms nicely to predictions of the Nash equilibrium or relevant refinement. In each case, however, a change in the payoff structure produces a large inconsistency between theoretical predictions and observed behavior. These contradictions are generally consistent with simple intuition based on the interaction of payoff asymmetries and noisy introspection about others' decisions.

## Summary
Goeree and Holt present ten paired one-shot games, each consisting of a "treasure" treatment where behavior matches the relevant Nash equilibrium (or refinement) strikingly well, and a "contradiction" treatment where a payoff change — often one that leaves the Nash prediction *unchanged* — drives behavior to the opposite end of the strategy space. The contradictions are not random noise: they track intuitive, payoff-magnitude-sensitive deviations that standard Nash analysis (which depends only on signs of payoff differences) ignores. The authors argue these patterns are organized by a model of noisy introspection that nests the logit quantal-response equilibrium as a limiting case.

## Research question
Does the Nash equilibrium (and its refinements) predict behavior in one-shot games, and if not, what systematic, economically-driven deviations arise when payoffs are changed in ways that leave the equilibrium prediction intact? Can a single class of boundedly-rational models explain both the successes ("treasures") and failures ("contradictions")?

## Method / identification
The design is a laboratory experiment using paired one-shot games. Cohorts of ten University of Virginia undergraduates first played a related game for ten periods under random matching ("part A"), then played roughly six genuinely one-shot games, each with fresh written instructions and assurance of a "quite different" subsequent task. Treasure and contradiction treatments were always paired, order-counterbalanced across sessions, and separated by unrelated one-shot games to suppress carryover. Subjects had prior strategic experience but no learning opportunity within a one-shot game, so beliefs must come from introspection.

The games span the textbook taxonomy: (i) static complete-information games — a traveler's dilemma (unique rationalizable equilibrium via iterated deletion), matching pennies (unique mixed equilibrium), and two coordination games (multiple equilibria); (ii) dynamic complete-information games — backward-induction "trust" and "credible-threat" games plus two-stage bargaining (subgame perfection); (iii) static incomplete-information games — private-value first-price auctions (Bayesian Nash); and (iv) dynamic incomplete-information signaling games (sequential equilibrium, Cho–Kreps intuitive criterion).

The explanatory model (Section V) is a noisy-introspection process. Choice probabilities follow a logit rule, $p_i = \exp(\pi_i^e/\mu)\,/\,\sum_{j=1}^{m}\exp(\pi_j^e/\mu)$, where $\mu$ is an error parameter ($\mu\to 0$ recovers best response, $\mu\to\infty$ gives uniform play). Letting $\phi_\mu$ denote the logit best-response map and iterating from a flat prior $p_0$ with *increasing* noise at higher levels gives
$$p = \lim \phi_{\mu_1}(\phi_{\mu_2}(\cdots\phi_{\mu_n}(p_0))),$$
with $\mu_1 \le \mu_2 \le \cdots$ and $\mu_n \to \infty$. The limit is independent of $p_0$, yields a unique prediction even with multiple equilibria, and allows "surprises" (choice probabilities need not match beliefs at any iteration). When the per-level error is constant, fixed points $\phi_\mu(p^*)=p^*$ are logit (quantal-response) equilibria.

## Data
Primary experimental data: choices from cohorts of ten subjects per game, typically 50 subjects (25 pairs) per treatment, with one auction game using 60 subjects (six cohorts). Subjects earned $6 show-up plus game earnings, averaging about $35 over two hours. Full individual-choice appendices were posted to the authors' web page.

## Key findings
- **Traveler's dilemma:** With a large penalty/reward $R=180$, about 80% chose the unique Nash/rationalizable claim of 180 (average 201); with $R=5$ the same fraction chose the *highest* claim (average 280) — the data mode sits at the opposite end of the strategy space from the unchanged Nash prediction. The effect persists and grows with repetition.
- **Matching pennies:** In the symmetric game, choices are essentially 50–50 as the mixed equilibrium predicts. Raising one row payoff from $0.80 to $3.20 (or lowering it to $0.44) leaves row's *own* equilibrium probability at one-half, yet 96% (resp. 92%) of row players moved toward the high-payoff cell — strong "own-payoff" effects unpredicted by Nash. Column players anticipated this. Nash works "only by coincidence," when payoffs are symmetric and deviation risks balanced.
- **Coordination with outside option:** Nash equilibria are independent of the row payoff $x$ in the $(L,S)$ cell, but raising $x$ from 0 to 400 cut high-payoff coordination from 80% to 32% of outcomes.
- **Minimum-effort coordination:** Any common effort is Nash, yet low effort cost ($c=0.1$) produced near-maximal effort (170) while high cost ($c=0.9$) produced near-minimal effort — coordination failure driven by a payoff parameter on which Nash is silent.
- **Kreps game:** Roughly two-thirds of column players chose the unique Non-Nash strategy; reframing to remove losses (ruling out loss aversion) left this nearly unchanged, while a heavy-handed payoff boost to the $(Bottom, Right)$ cell restored 84% Nash play.
- **Backward induction (trust / threats):** Subjects often failed to trust others' rationality when irrationality was nearly costless (only ~16–36% subgame-perfect outcomes in contradiction treatments), and non-credible "threats" altered behavior when carrying them out cost the threatener little (2 cents) but not when costly (40 cents).
- **Bargaining:** Two-stage alternating-offer demands deviated from subgame-perfect predictions, with larger deviations under inequity-accentuating endowments (Goeree and Holt 2000a).
- **Auctions:** In private-value first-price auctions, overbidding tracked the cost of deviating: the (0,3,6) treatment (where the unique Bayesian-Nash bids are unchanged from (0,2,5) but upward-deviation is relatively cheaper) yielded only 50% Nash bids vs. 80%.
- **Signaling:** A separating equilibrium was cleanly observed in the treasure game; a minor payoff change produced *separation that is not a Nash equilibrium* (all equilibria pool), contradicting both sequential equilibrium and the intuitive criterion.
- **Model:** The noisy-introspection / logit framework reproduces treasure-vs-contradiction patterns; fitting 37 matrix games gives a noise-growth rate $t=4.1$ (more noise at higher introspection levels).

## Contribution
The paper assembles a single, unified body of evidence that the sign-based logic of Nash equilibrium and its refinements systematically misses payoff-magnitude effects in one-shot play, while showing those same effects are intuitive and quantitatively organized by noisy introspection / quantal-response models. By using *paired* treatments that hold the Nash prediction fixed, it isolates behavioral forces from equilibrium selection, providing a memorable catalogue ("ten treasures, ten contradictions") that motivated the stochastic / behavioral game theory program.

## Limitations & open questions
- The authors explicitly note "relatively little theoretical analysis of one-shot games where learning is impossible," flagging introspection as understudied relative to refinements and learning — an open modeling agenda.
- Inequity aversion, loss aversion, maximin/security heuristics, and reciprocity are each shown to fail as general explanations, leaving an incomplete account; the noisy-introspection model itself shows "obvious discrepancies."
- Error parameters differ across games of differing complexity, so the model is not yet a portable cross-game predictor except among games of similar complexity.
- The authors propose directly *eliciting beliefs* during play as a promising next step.
- One-shot designs risk confusion effects in the absence of learning, which they argue are minimized by simple structure but not eliminated.

## Connections
The explanatory backbone draws on McKelvey & Palfrey (1995, 1998) quantal-response and logit equilibrium and Luce (1959) on the logit choice rule. The introspection hierarchy builds on Stahl & Wilson (1995) level-k rationality and Nagel (1995) guessing-game unraveling, with related limited-reasoning models by Kübler & Weizsäcker (2000) and the authors' own Goeree & Holt (1999, 2000b). The contradiction treatments engage social-preference theories of [[@Fehr1999|Fehr & Schmidt (1999)]] and [[@Bolton2000|Bolton & Ockenfels (2000)]], reciprocity in [[@Rabin1993|Rabin (1993)]], and loss aversion in Kahneman, Knetsch & Thaler (1991). Game-theoretic foundations referenced include Nash (1950), Selten (1975) subgame perfection, Rubinstein (1982) bargaining, Bernheim (1984) and Pearce (1984) rationalizability, Basu (1994) traveler's dilemma, Kreps (1995), Cho & Kreps (1987) intuitive criterion, Rosenthal (1981) centipede, and Beard & Beil (1994) on trusting others' rationality. The equilibrium-selection discussion invokes Harsanyi & Selten (1988) risk dominance and Van Huyck, Battalio & Beil (1990) coordination. Learning comparisons cite Erev & Roth (1998), Camerer & Ho (1999), and Crawford (1995).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
