---
citekey: Huber1982
title: "Adding Asymmetrically Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis"
authors: ["Huber, Joel", "Payne, John W.", "Puto, Christopher"]
year: 1982
type: journalArticle
doi: 10.1086/208899
zotero: "zotero://select/library/items/JCSZIWFN"
pdf: /Users/jesper/Zotero/storage/RPTQ6Y8J/Huber1982.pdf
tags: [literature]
keywords: [asymmetric-dominance, decoy-effect, regularity-violation, context-dependent-choice, discrete-choice-models, similarity-hypothesis]
topics: ["[[context-effects-attraction-compromise]]"]
related: [Manzini2007, Tversky1972]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> An asymmetrically dominated alternative is dominated by one item in the set but not by another. Adding such an alternative to a choice set can increase the probability of choosing the item that dominates it. This result points to the inadequacy of many current choice models and suggests product line strategies that might not otherwise be intuitively plausible.

## Summary
This is the founding paper of the *asymmetric dominance* (decoy / attraction) effect. Huber, Payne, and Puto show experimentally that adding a third alternative that is dominated by one option in a set (the "target") but not by another (the "competitor") *raises* the choice share of the dominating target. Because the added decoy itself is almost never chosen, this directly violates **regularity** — the axiom that enlarging a choice set cannot raise the probability of any incumbent option. It also *reverses* the **similarity hypothesis**: the decoy, which is most similar to the target, helps the target rather than cannibalizing it. The effect averages roughly a 9-percentage-point gain to the target across six product categories.

## Research question
Can the addition of a new alternative to a choice set increase the probability of choosing an item already in the set — and specifically, does an asymmetrically dominated alternative bias choice toward the option that dominates it, thereby violating regularity and reversing the similarity hypothesis?

## Method / identification
The core formal object is **regularity**: for $A \subseteq B$ and any $x \in A$,
$$\Pr(x;A) \ge \Pr(x;B).$$
Regularity is the weakest common restriction of both Luce's (1959) constant-utility (IIA) model and Tversky's (1972) elimination-by-aspects model; the authors note it is the one property of choice probabilities Luce called empirically undisconfirmed. They construct choice sets violating it *without* invoking choice-set-dependent "higher-order" rules (contrasting Corbin & Marley's hat and entrée counterexamples).

An alternative is **asymmetrically dominated** if it is dominated by at least one member of the set but not by at least one other. Each two-attribute product space contains a *target* and a *competitor* positioned so neither dominates the other (each superior on one attribute), plus a *decoy* placed in the region dominated by the target but not the competitor (Figure A).

The experimental design: 153 graduate/undergraduate business students chose from six product categories (cars, restaurants, beers, lotteries, film, TV sets), each alternative defined on two attributes, in two- or three-item sets. The decoy effect is measured as the change in the share of an item between when it plays the target role and when it plays the competitor role. Four **decoy-placement strategies** are crossed in a balanced design: range-increasing ($R$), extreme range-increasing ($R^*$), frequency-increasing ($F$), and combined range-frequency ($RF$). These are motivated by candidate mechanisms — range/frequency reweighting of attributes (à la Parducci 1974), popularity inference, attribute-by-attribute paired comparison, round-robin "win-counting," and Shugan's (1980) cost-of-thinking. **Between-subject** tests compare target share across decoy placements (Fisher exact tests); a **within-subject** test re-runs 93 subjects two weeks later with the decoy removed and tallies preference reversals (McNemar test).

The authors also give an impossibility argument: an asymmetrically dominated alternative cannot be represented by any one-dimensional constant- or random-utility scale, since the dominated item must lie an infinite distance below its dominator while nondominating pairs require finite distances.

## Data
Original experimental data: 153 subjects making forced single choices over six two-attribute product categories; 93 of them retested two weeks later (558 within-subject choices). The Appendix gives the full attribute levels and the group-to-strategy assignment.

## Key findings
- **Regularity is violated, directionally.** Adding the decoy raised target share in 18 of 24 between-subject cases ($p \le 0.05$), with an average gain of **9.2 percentage points**; the gain is in the hypothesized direction for all six product classes.
- **Strategy ranking.** Range-increasing strategies ($R$, $R^*$) were strongest (+13 points), then range-frequency $RF$ (+8), then frequency $F$ (+4, not significant). Notably, extreme range $R^*$ did not beat moderate range $R$, so a simple range-extension account is insufficient.
- **Within-subject reversals favor the target.** Among choices where the decoy was not picked (98%), 63% of 109 reversals went to the target vs. 37% to the competitor ($p \le 0.05$); target share rose from 53% to 56%. The within-subject effect (~3 points) is weaker than between-subject (~9 points), attributed to carryover/repeat-choice sensitization.
- **Substitution is negligible.** The decoy took only ~2% of choices, so the distortion effect is not masked by substitution — explaining why earlier studies (where added items grabbed substantial share) found regularity satisfied.
- **Similarity hypothesis reversed.** Decoys most similar to the target (range strategies, by the relative-similarity ratio of decoy–competitor to decoy–target distance) help the target most — the opposite of standard similarity predictions.

## Contribution
Introduces and empirically demonstrates the asymmetric-dominance effect, establishing that regularity — and with it Luce's model and its similarity-based extensions (elimination-by-aspects, Hausman–Wise probit, Batsell) — fails in a predictable, directional way that cannot be patched with choice-set-independent utilities. Managerially, it shows a product line's profitability can rise by adding a dominated item that almost no one buys, because the decoy redirects attention to a more profitable target. It thereby marks a boundary on the applicability of discrete-choice models and seeds the context-dependent-choice literature.

## Limitations & open questions
- The experiment uses only **three alternatives on two dimensions**; the authors expect the dominance effect *per se* to weaken with more options/dimensions (harder to recognize dominance), while range/frequency effects might strengthen.
- **No unique mechanism is identified** — perceptual reweighting (range, frequency), popularity inference, paired-comparison elimination, win-counting, and cost-of-thinking all predict the same direction. They call for research disentangling these, e.g. eliciting attribute weights (direct or statistical, à la Currim–Weinberg–Wittink) and process-tracing via verbal protocols or eye tracking (Payne–Braunstein–Carroll) to test whether decoys "alter the implicit choice agenda."
- The relative-similarity reversal is flagged as **speculative** pending a more precise similarity measure.
- Calls for **field validation** (e.g., the camel-hair-coat retail experiment, catalogue mailings) and near-dominance cases where the target–decoy choice is easy without strict dominance.

## Connections
Builds on and challenges Luce's (1959, 1977) choice axiom and the proportionality/IIA assumption used in applied share models (Silk & Urban 1978; Reibstein 1978; McFadden 1974 for transport mode choice). Directly confronts the similarity hypothesis of [[@Tversky1972|Tversky]] (1972, elimination by aspects) and its random-utility implementation by Hausman & Wise (1978), plus Batsell's (1980) substitutability model and Restle (1961). The regularity counterexamples of Corbin & Marley (1974) are contrasted as relying on higher-order rules. Mechanistic motivations draw on Parducci's (1974) range-frequency theory, Shugan's (1980) cost of thinking, and process work by Russo & Rosen (1975), Russo & Dosher (1980), and Payne, Braunstein & Carroll (1978). Coombs & Avrunin (1977) and Debreu's (1960) red-bus/blue-bus critique of Luce are also invoked. This paper anchors the later attraction-effect and context-dependent choice literature and connects to models of menu-dependent and reference-dependent choice such as [[@Manzini2007|Manzini & Mariotti (2007)]] and Bordalo, Gennaioli & Shleifer's salience theory.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
