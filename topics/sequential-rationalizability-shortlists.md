---
slug: sequential-rationalizability-shortlists
title: "Sequential Rationalizability & Shortlist Methods"
type: topic
scope: "Two-stage / multi-rationale procedures (RSM, CTC, checklists, lexicographic semiorders) that rationalize cyclic and menu-dependent choice while staying testable."
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
area: "[[bounded-rationality-choice]]"
---

## Scope

This topic covers boundedly rational choice procedures that decompose a single choice act into *stages* — eliminate by one criterion, then choose by another — so that observed behavior need not be the maximization of one preference. It spans rational shortlist methods (two ordered rationales), categorize-then-choose, checklists, lexicographic semiorders, list/route procedures, and rationalization, unified by the Manzini–Mariotti question: given that such procedures rationalize cyclic and menu-dependent choice while remaining testable, *how much* of the unobserved internal machinery (the rationales, the shortlist, the categories) does choice data actually reveal? The boundary is deliberate: these are deterministic, finite-menu, single-rationale-set procedures whose content is fixed across menus — stochastic choice, attribute-search process models, and pure attention/consideration filters sit just outside and surface as bordering work.

## Sub-themes

- **Rational shortlist methods (RSM) and their identification.** The canonical two-rationale procedure $c(S)=\max(\max(S;P_1);P_2)$ and the program of recovering $(P_1,P_2)$ from data: [[@Manzini2007|Manzini & Mariotti (2007)]] (Expansion + Weak WARP), [[@Dutta2015|Dutta & Horan (2015)]] (revealed rationales = switches/reversals, the full lattice of representations), [[@Au2011|Au & Kawai (2011)]] (transitive rationales + NBCC, partial identification), [[@Horan2016|Horan (2016)]] (transitive shortlist methods via Strong Exclusivity, small-menu recovery).
- **Categorize-then-choose and shading.** Eliminate "shaded" categories of alternatives, then maximize: [[@Manzini2012a|Manzini & Mariotti (2012a)]] (CTC, characterized by Weak WARP, strictly larger than RSM because it captures menu effects), with the multivalued extension by [[@Garcia-Sanz2015|García-Sanz & Alcantud (2015)]] and the correspondence-domain "indecisive" extension of both RSM and CTC by [[@Armouti-Hansen2018|Armouti-Hansen & Kops (2018)]].
- **Checklists, lexicographic semiorders, and the "almost rational" boundary.** Sequential property/threshold elimination: [[@Mandler2012|Mandler, Manzini & Mariotti (2012)]] (checklists $\approx$ utility maximization, exponential discrimination), [[@Manzini2012|Manzini & Mariotti (2012b)]] (choice by lexicographic semiorders, Reducibility, basic 3-valued discrimination suffices on finite domains), [[@Kops2018|Kops (2018)]] (flexicographic SM, menu-dependent *order* of two rationales), [[@Manzini2015|Manzini & Mariotti (2015)]] (state-dependent checklists where psychological state sets the property order), [[@Payne1976|Payne (1976)]] (the empirical seed: process-tracing shows people switch to elimination heuristics as task complexity rises).
- **Multiple-rationale / multi-self rationalization (the count-of-rationales program).** How many orders, or which justifications, are needed: [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] (RMR and the minimal count $r(c)$), [[@Apesteguia2005|Apesteguia & Ballester (2005)]] (constructive minimal book of rationales via c-maximal sets), [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]] (rationalization — pick the $P$-best among self-justifiable options), [[@Heller2012|Heller (2012)]] (justifiable choice over lotteries, multiple-utility representation via CARNI).
- **Lists, routes, and game-tree-equivalent sequencing.** Procedures organized by an order over alternatives or over pairwise contests: [[@Rubinstein2006|Rubinstein & Salant (2006)]] (choice from lists, Partition Independence), [[@Yildiz2016|Yıldız (2016)]] (list-rationalizability, stochastic version, acyclicity of revealed-to-follow), [[@Apesteguia2013|Apesteguia & Ballester (2013)]] (sequential procedures guided by routes, a taxonomy $C^{RAT}\subset C^{SQB}\subset C^{RGT}\subset C^{SR}$), [[@Bajraj2015|Bajraj & Ülkü (2015)]] (top-2 shortlist with a winner-only-observable second criterion).
- **The "next-best"/similarity-mistake fringe.** Procedures that select something other than the top survivor: [[@Baigent1996|Baigent & Gaertner (1996)]] (never choose the uniquely largest — second-best as an internalized norm), [[@Houy2009|Houy & Tadenuma (2009)]] (lexicographic composition of $M$ criteria, the $\alpha$ vs $\beta$ aggregation gap), [[@Payro2015|Payró & Ülkü (2015)]] (similarity-based mistakes: keep everything similar to the best, the *opposite* movement to elimination).

## Cross-paper tensions

**1. What is "revealed," and is the first or the second rationale privileged?** The identification papers do not agree on what choice pins down. [[@Dutta2015|Dutta & Horan (2015)]] show that for the RSM the revealed 1-rationale (choice *switches*) and revealed 2-rationale (choice *reversals*) are exactly the pairs common to all representations, and that the indeterminate middle $P^m$ can be loaded onto *either* rationale — so the model is generically *not* point-identified, and the Bernheim–Rangel welfare relation silently overestimates $P_1$ and ignores $P_2$. [[@Au2011|Au & Kawai (2011)]] reach an almost paradoxical sharpening: a *less complete* criterion pins the preference *more* tightly (their lower bound $\underline{P_1^c}$ point-identifies $P_2$), and the representation is unique iff $\underline{P_1^c}=\overline{P_1^c}$. [[@Horan2016|Horan (2016)]] makes the same conservative/liberal trade-off explicit (Theorem 5) but argues it is forced only because no application fixes the interpretation of preferences in neither revealed rationale. So the field shares the conservative "intersection of all representations" notion ([[@Cherepanov2013|Cherepanov et al. (2013)]] and [[@Tyson2013|Tyson (2013)]] frame revelation as agreement across valid representations too) yet disagrees on whether the residual indeterminacy is a fixable artifact (Au–Kawai: add transitivity) or intrinsic (Dutta–Horan: it is a lattice).

**2. Is the anomaly in the *procedure* or in a *broken preference*?** [[@Au2011|Au & Kawai (2011)]] argue the anomaly is the shortlisting *stage*, not the preference: forcing both rationales standard (transitive criterion, complete-transitive preference) still yields cyclic *choice*, and the entire gap to general RSM is one axiom (NBCC) on the *indirectly* revealed preference. [[@Manzini2007|Manzini & Mariotti (2007)]] instead locate the content in arbitrary (possibly cyclic) rationales. [[@Horan2016|Horan (2016)]] reframes the whole question as which *context effects* (attraction vs. limited-attention reversals) are permitted, recasting RSM, $T_1$SM, and TSM as a single "exclusivity ladder" — a rival organizing axis to the transitivity-of-rationales axis.

**3. RSM vs CTC: more rationales vs richer first stage.** [[@Manzini2012a|Manzini & Mariotti (2012a)]] show that CTC, with only *two* relations (a shading relation on *sets* plus a preference), captures *menu effects* that the RSM — and indeed sequential rationalizability with *arbitrarily many* rationales — provably *cannot* (since any sequentially rationalizable function satisfies Always Chosen, per [[@Manzini2007|Manzini & Mariotti (2007)]]). So adding rationales (depth) and enriching the first stage to act on sets (the shading relation) are *non-comparable* routes to explanatory power. [[@Cherepanov2013|Cherepanov et al. (2013)]] then show CTC coincides empirically with basic rationalization and is strictly subsumed by *order* rationalization — so three differently-motivated procedures (categorization, self-justification, shortlisting) collapse onto the same axioms (Weak WARP / No Binary Chain Cycles), which [[@Manzini2012a|Manzini & Mariotti (2012a)]] treat as a welfare *opportunity* (convergent revelation licenses treating the relation as welfare-relevant) and [[@Cherepanov2013|Cherepanov et al. (2013)]] treat as a welfare *problem* (which rationale is "true" preference is unresolved).

**4. Fixed order vs. menu-/state-dependent order.** The classic procedures hardwire the order of stages; [[@Manzini2007|Manzini & Mariotti (2007)]] flag menu-dependent-order RSMs as an open class they "do not know" how to characterize. [[@Kops2018|Kops (2018)]] resolves the two-rationale case (flexicographic SM, characterized by Reversal Consistency) and shows the single relaxation buys cycles + attraction + compromise effects simultaneously — but at the cost that *what determines the order in a given menu is an unmodeled free parameter*, reviving Sen's re-individuation worry. [[@Manzini2015|Manzini & Mariotti (2015)]] discipline exactly this by holding the *mindset* (property set) fixed and letting only a psychological *state* permute it, but then testability *requires multiple observations from the same menu* — with single-valued data their Model 1 is empirically vacuous. So the gain in flexibility trades directly against falsifiability.

**5. Lexicographic composition need not commute, and "compose-then-maximize" $\neq$ "maximize-then-narrow."** [[@Houy2009|Houy & Tadenuma (2009)]] expose a tension internal to the *very idea* of sequential criteria: procedure $\alpha$ (build one composite relation, maximize) and procedure $\beta$ (maximize criterion by criterion) coincide only under quasi-transitivity; $\beta$ almost always returns a choice but routinely violates contraction consistency, $\alpha$ is consistent but often empty — a "fundamental dilemma." This sits uneasily with the RSM/CTC literature's habit of treating sequential elimination ($\beta$-style) as automatically well-behaved, and with [[@Apesteguia2013|Apesteguia & Ballester (2013)]]'s route procedures, which presuppose a clean order over contests.

**6. How many rationales, and does the count mean anything?** [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] propose $r(c)$, the minimal number of orderings, as a graded rationality measure — but show it diverges sharply from intuitive closeness to rationality (the second-best procedure needs only $\lceil\log_2 N\rceil$, the median nearly $N-1$), and concede the count ignores the *descriptive complexity* of the partition assigning rationales to menus. [[@Apesteguia2005|Apesteguia & Ballester (2005)]] make the count constructive but conjecture the general minimal-book problem is NP-complete and show natural pruning heuristics (inclusion-order, cardinality-order) fail. So the count-based program is in tension with itself: the measure is either computationally hard or behaviorally uninformative, and [[@Cherepanov2013|Cherepanov et al. (2013)]]'s rationalization sidesteps it entirely by allowing unboundedly many rationales but constraining *which* options each can justify.

**7. Elimination vs. inclusion.** Nearly every member eliminates down to survivors; [[@Payro2015|Payró & Ülkü (2015)]] move the opposite way — the best feasible option *survives* and passed-over alternatives *re-enter* if similar to it — yet land in the same revealed-preference family (a single weakening of Arrow, forcing cycles). [[@Baigent1996|Baigent & Gaertner (1996)]] go further still and *refuse* the maximum (second-best as a norm). These show the "two-stage screen-then-pick" template is not the only way to generate the same testable cyclic signatures, raising the question of whether choice data can ever distinguish elimination from inclusion.

## Open questions

- **Identification beyond two rationales and beyond complete data.** [[@Dutta2015|Dutta & Horan (2015)]] explicitly leave open whether their switch/reversal revealed-rationale theory extends to $K>2$ rationales (à la [[@Apesteguia2005|Apesteguia & Ballester (2005)]]) and to limited data (de Clippel–Rozen sense); the lattice structure their method needs fails for attention-filter models. [[@Garcia-Sanz2015|García-Sanz & Alcantud (2015)]] note their canonical *representation* is not a unique *identification* because the Dutta–Horan uniqueness argument "hinges on choices being univalued."
- **Characterizing menu-/state-dependent-order procedures with single-valued data.** [[@Manzini2007|Manzini & Mariotti (2007)]] and [[@Kops2018|Kops (2018)]] leave the $n>2$ flexible-order case open; [[@Manzini2015|Manzini & Mariotti (2015)]] need multi-valued observations from the same menu and leave the graded/semiorder state-dependent version (which would break frame-equivalence) undeveloped.
- **The full characterization of sequential rationalizability for choice *correspondences*.** Flagged by [[@Manzini2007|Manzini & Mariotti (2007)]], partially answered for two criteria under CWDE by [[@Garcia-Sanz2015|García-Sanz & Alcantud (2015)]] and for indecisive RSM/CTC by [[@Armouti-Hansen2018|Armouti-Hansen & Kops (2018)]], but the $K$-criterion correspondence case and the salience-CTC characterization ([[@Manzini2012a|Manzini & Mariotti (2012a)]]'s explicit open problem) remain.
- **Distinguishing indecisiveness from indifference, and "mistakes" from preference.** [[@Armouti-Hansen2018|Armouti-Hansen & Kops (2018)]] concede that with multiple criteria the indecisiveness/indifference boundary is "difficult, if not impossible" to draw from choice alone; [[@Payro2015|Payró & Ülkü (2015)]] cannot identify $R$ when two alternatives are adjacent-and-similar.
- **Welfare under sequential procedures.** [[@Kops2018|Kops (2018)]] shows a decoy can silently flip the order of rationales and deceive the Bernheim–Rangel criterion but offers no positive welfare rule; [[@Cherepanov2013|Cherepanov et al. (2013)]] and [[@Manzini2012a|Manzini & Mariotti (2012a)]] leave unresolved whether the shading relation / second rationale ever carries welfare content.
- **A complexity measure that penalizes structure, not just count.** [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] call for "structured" forms of rationalization that score the descriptive complexity of the menu-to-rationale assignment; [[@Apesteguia2005|Apesteguia & Ballester (2005)]] leave the NP-completeness conjecture and the search-space pruning open.
- **Finite vs. infinite domains.** [[@Manzini2012|Manzini & Mariotti (2012b)]] show acyclic-RSM = basic lexicographic semiorder only on *finite* domains (Prop. 3–4); [[@Au2011|Au & Kawai (2011)]] restrict to finite $X$. Where transitivity vs. acyclicity becomes a genuine behavioral threshold on larger domains is open.
- **Reconciling deterministic shortlisting with stochastic and process data.** [[@Yildiz2016|Yıldız (2016)]] randomizes comparisons but fixes a deterministic list (flagged as "particularly restrictive") and cannot capture the general duplicates effect; [[@Payne1976|Payne (1976)]] shows process-tracing reveals strategy-switching that outcome data underdetermine — the link between the axiomatic procedures and observable search is unformalized.

## Candidate ideas

- **Identify the rationales of a flexicographic / menu-dependent-order SM.** [[@Dutta2015|Dutta & Horan (2015)]]-style "switch/reversal" revealed-rationale theory exists only for fixed-order RSM; develop the analogous theory for [[@Kops2018|Kops (2018)]]'s FSM, asking exactly which order-flips are revealed by data and whether the unmodeled "order-setting frame" can be partially recovered — directly attacking Kops's free-parameter worry.
- **A descriptive-complexity rationality index.** Build the "structured RMR" measure [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] called for, combining $r(c)$ with the complexity of the menu-to-rationale map, and use [[@Apesteguia2005|Apesteguia & Ballester (2005)]]'s c-maximal-set machinery to make it computable; test it against the second-best vs. median divergence as a benchmark.
- **Experimentally separate elimination from inclusion procedures.** Design choice menus (and possibly process-tracing à la [[@Payne1976|Payne (1976)]]) that drive a wedge between [[@Manzini2007|Manzini & Mariotti (2007)]]-style elimination-RSM and [[@Payro2015|Payró & Ülkü (2015)]]-style similarity-inclusion, exploiting that the former rejects, the latter re-admits, alternatives similar to the best — both produce cycles, so the question is whether richer data can tell them apart.
- **Welfare protocol for two-stage choosers when a decoy controls the order.** Turn [[@Kops2018|Kops (2018)]]'s deception example and [[@Manzini2012a|Manzini & Mariotti (2012a)]]'s "binary choice reveals true preference" lesson into a positive, testable rule for recovering welfare-relevant preference under CTC/FSM, using [[@Cherepanov2013|Cherepanov et al. (2013)]]'s minimum-constraint refinement to identify when the second rationale is preference vs. salience.
- **Identification for sequential rationalization of correspondences with $K>2$ criteria.** Extend [[@Armouti-Hansen2018|Armouti-Hansen & Kops (2018)]] and [[@Garcia-Sanz2015|García-Sanz & Alcantud (2015)]] past two criteria, settling whether univalence is truly necessary for unique identification (the gap both papers flag) and characterizing salience-CTC for correspondences.
- **State-dependent semiorders with multi-observation data.** Operationalize [[@Manzini2015|Manzini & Mariotti (2015)]]'s graded/threshold extension (state-dependent lexicographic semiorders, building on [[@Manzini2012|Manzini & Mariotti (2012b)]]), exploiting their requirement of repeated same-menu choices to deliver the bimodal labour-supply prediction as a falsifiable empirical test.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Masatlioglu2012]] — cited by 8 members
- [[@Salant2008]] — cited by 7 members
- [[@Bernheim2009]] — cited by 6 members
- [[@Sen1993]] — cited by 5 members
- [[@Eliaz2006]] — cited by 3 members
- [[@Eliaz2011a]] — cited by 3 members
- [[@Rubinstein2012]] — cited by 3 members
- [[@Samuelson1938]] — cited by 3 members
- [[@Shafir1993]] — cited by 3 members
- [[@Simonson1992]] — cited by 3 members
- [[@Tversky1972]] — cited by 3 members
- [[@Tyson2008]] — cited by 3 members
- [[@Ehlers2008]] — cited by 2 members
- [[@Huber1982]] — cited by 2 members
- [[@Loomes1991]] — cited by 2 members
- [[@Manzini2014]] — cited by 2 members
- [[@Sen1971]] — cited by 2 members
- [[@Xu2007]] — cited by 2 members
- [[@Akerlof1982]] — cited by 1 member
- [[@Caplin2001]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
