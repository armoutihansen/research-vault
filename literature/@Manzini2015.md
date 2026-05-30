---
citekey: Manzini2015
title: State dependent choice
authors: ["Manzini, Paola", "Mariotti, Marco"]
year: 2015
type: journalArticle
doi: 10.1007/s00355-015-0894-3
zotero: "zotero://select/library/items/ADH6799Z"
pdf: /Users/jesper/Zotero/storage/WZNVIAH8/Manzini2015.pdf
tags: [literature]
keywords: [revealed-preference, bounded-rationality, choice-theory, psychological-state, state-dependent-choice, sequential-rationalizability, labour-supply]
topics: []
related: [Bernheim2009, Caplin2001, Cherepanov2013, Crawford2011, Eliaz2006, Farber2005, Kalai2002, Koszegi2006b, Mandler2012, Manzini2007, Manzini2012a, Salant2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We propose a theory of choices that are influenced by the psychological state of the agent. The central hypothesis is that the psychological state controls the urgency of the attributes sought by the decision maker in the available alternatives. While state dependent choice is less restricted than rational choice, our model does have empirical content, expressed by simple ‘revealed preference’ type of constraints on observable choice data. We demonstrate the applicability of simple versions of the framework to economic contexts. We show in particular that it can explain widely researched anomalies in the labour supply of taxi drivers.

## Summary
Manzini and Mariotti build a procedural choice model in which an agent screens alternatives through a sequential checklist of *properties* (attributes), and the agent's *psychological state* controls the order in which those properties are applied. The fixed set of properties — the *mindset* — encodes a stable personality, while a *state* is a strict linear order over that mindset. Two variants are studied: states triggered by the menu, and states driven by the exogenous environment (allowing multiple observations from the same menu). Each variant is characterized by exactly one revealed-preference axiom that sits strictly between WARP and a weaker textbook condition, so the framework is more permissive than rational choice yet still falsifiable. They apply a stripped-down version to the taxi-driver labour-supply anomaly.

## Research question
Can the influence of psychological state on choice be modeled in a way that (i) does not commit to any specific psychological mechanism, (ii) yields non-vacuous, directly testable revealed-preference restrictions, and (iii) is tractable enough to generate concrete economic predictions (e.g. negative wage elasticities)?

## Method / identification
The primitive is a choice correspondence $c$ on the collection $\Sigma$ of nonempty subsets of a finite set $X$. A *property* is identified with the set of alternatives possessing it, $P \subseteq X$. A *mindset* $\Pi \subseteq 2^{X}\setminus\emptyset$ is a set of distinct properties; it is *nested* if for all $P,Q\in\Pi$ either $P\subseteq Q$ or $Q\subseteq P$. A *state* is a strict linear order $<$ of $\Pi$. The agent applies a *checklist*: scanning properties in the state's order, at each property keeping only the survivors that possess it (if any), otherwise keeping all current survivors. This builds inductively a chain of *survivor sets* $S_A(P,<)$, and the choice $c(A)$ is the final survivor set.

The model extends [[@Mandler2012|Mandler, Manzini & Mariotti]] (2012, "MMM"), where a single fixed checklist is shown to be behaviorally equivalent to preference maximization (Proposition 1). The novelty is letting the order vary.

**Model 1 — menu-driven states.** A menu checklist is a pair $\big(\Pi,\{<_A\}_{A\in\Sigma}\big)$, one state per menu; multiple choices from a menu are read as made in the same (menu-induced) state.

**Model 2 — environment-driven states.** An environmental checklist is $\big(\Pi,\{<_m\}_{m\in M}\big)$; the analyst sees $c(A)=\bigcup_{<_m\in M}\gamma(A,<_m)$, the union over unobservable states $<_m$ of the state-conditional choices $\gamma(A,<_m)$.

The application (Sect. 5) specializes the mindset to two threshold properties — an income property $P^{I}$ (income above a target) and a leisure property $P^{L}$ (leisure above a target) — and derives labour-supply comparative statics graphically, exploiting the asymmetry that leisure targets face a physical bound while income targets need not.

## Data
None — this is a theory paper. The taxi-driver application is an illustrative model calibrated to the empirical debate (Camerer et al. 1997; [[@Farber2005|Farber 2005]], 2008; [[@Crawford2011|Crawford & Meng 2011]]), not an estimation; no dataset is analyzed.

## Key findings
- **Proposition 1 (MMM):** $c$ has a (fixed) checklist iff it maximizes a preference (weak order). Checklists $=$ rationality.
- **Proposition 2:** A menu-driven state dependent choice with a *nested* mindset maximizes a preference — state variation is then behaviorally invisible (illustrated by a satisficer revising numerical targets).
- **Proposition 3 (main, Model 1):** $c$ is a menu-driven state dependent choice iff it satisfies **Togetherness**: for all $A,B$, $[x\in A\setminus c(A),\ y\in c(A),\ y\in c(B)]\Rightarrow x\notin c(B)$. Equivalently, two alternatives both chosen from some menu are, in any other menu, either both chosen or both rejected. Togetherness is strictly weaker than WARP and strictly stronger than Sen's property $\beta$. It is single-valued-vacuous. A special "trigger checklist" version is characterized by t-WARP (WARP holding separately on the menus containing vs. not containing a trigger alternative). Corollary 1 gives an equivalent axiom, *All or Nothing*.
- **Proposition 4:** Each state-conditional $\gamma(\cdot,<_m)$ satisfies IIA.
- **Claim 1:** The aggregate $c$ in Model 2 can violate Expansion and property $\beta$ (hence Togetherness) — environment-driven states generate genuine inconsistency.
- **Proposition 5:** Environment-driven state dependent choice with a nested mindset maximizes a weak order.
- **Proposition 6 (main, Model 2):** $c$ is an environment-driven state dependent choice iff it satisfies **sd-WARP**: $[x\in A\setminus c(A),\ c(A)\subseteq B]\Rightarrow x\notin c(B)$. WARP strengthens sd-WARP by replacing the whole set $c(A)$ with any single chosen element. sd-WARP implies property $\alpha$ but $\alpha$ alone is insufficient. As a by-product this characterizes choice correspondences generated by Salant–Rubinstein "salient consideration" choice functions, and (via Litvakov 1981) sd-WARP $\Leftrightarrow$ property $\alpha$ + Chernoff's Postulate 5 (Claim 3).
- **Application:** Because income targets can be "unrealistic" while leisure targets cannot, the lexicographic model predicts (i) textbook responses to large wage drops but a wider range — including negative wage elasticities — for milder drops when income is targeted first, and (ii) "behaviorally extreme" supply: a gap of intermediate hours never chosen in any state. Two novel testable predictions: the size of the wage change matters for the conflicting evidence, and supply can be bimodal ("a lot" or "little").

## Contribution
The paper locates psychologically driven choice precisely in the logical space of revealed-preference axioms: both models lie strictly *between* the rational (WARP) model and weakened versions of it (property $\beta$ / property $\alpha$), each pinned down by a single transparent axiom. By keeping the mindset fixed and varying only the ordering, departures from rationality are attributed solely to state changes — imposing discipline absent in menu-dependent-utility (Kalai–Rubinstein–Spiegler), Green–Hojman, and Ambrus–Rozen multiself models, all of which can rationalize *any* behavior. It also supplies a hitherto-missing characterization of salient-consideration choice and offers a property-based (rather than utility-based) language with direct psychological interpretation.

## Limitations & open questions
- Testability hinges on observing **multiple choices from the same menu**; with single-valued data Model 1 is empirically vacuous and Model 2 collapses to standard utility maximization.
- The two models are logically independent (Togetherness and sd-WARP are independent), so choice data alone may not select between them — and rival explanations (rationalization à la [[@Cherepanov2013|Cherepanov et al. 2013]]) can fit the same data; context and non-choice data are needed.
- Frames and states need not be identifiable from each other even where the two frameworks are observationally equivalent.
- Multiself comparisons suggest restricting the *number of states/properties* to retain bite; principled restrictions are left open.
- Comparisons with inattention, categorization, and rationalization are incomplete because those theories are axiomatized only for single-valued choice; extending them to correspondences is flagged as open.
- The two-way feedback between choice and psychological state is explicitly unmodeled ("a first step"); the taxi application is "just a sketch," with full structural/empirical estimation and the bimodal-supply prediction left for future work.
- The 0–1 (all-or-nothing) satisfaction of properties is essential; a graded/semiorder version (state-dependent lexicographic semiorders) would break the frame-equivalence and is undeveloped.

## Connections
Directly extends [[@Mandler2012|Mandler, Manzini & Mariotti (2012)]] on choosing by checklist and [[@Manzini2007|Manzini & Mariotti (2007)]] on sequentially rationalizable choice; related to [[@Manzini2012a|Manzini & Mariotti (2012)]] on choice by lexicographic semiorders and on categorize-then-choose. The aggregate-over-states construction parallels [[@Salant2008|Salant & Rubinstein (2008)]] "choice with frames" and [[@Bernheim2009|Bernheim & Rangel (2009)]] choice with ancillary conditions, with welfare reasoning drawing on [[@Bernheim2009|Bernheim & Rangel (2009)]] and Mandler (2009) on distinguishing indifference from incompleteness. It contrasts with multiself / multiple-rationale models of [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]], Green & Hojman (2008), and Ambrus & Rozen (2013), and with indecisiveness models of [[@Eliaz2006|Eliaz & Ok (2006)]]. The attribute-based primitive follows Lancaster (1966) and connects to Dietrich & List (2013); menu/contemplation-cost triggers relate to Ergin & Sarver (2010) and the menu-choice literature (Kreps 1979; Dekel, Lipman & Rustichini 2001). The labour-supply application engages Camerer et al. (1997), [[@Farber2005|Farber]] (2005, 2008), Köszegi & [[@Koszegi2006b|Rabin (2006)]], and [[@Crawford2011|Crawford & Meng (2011)]]; related psychological-state models include [[@Caplin2001|Caplin & Leahy (2001)]] and Laibson (2001). The technical by-products link to Litvakov (1981) / Aizerman & Aleskerov (1995) and Caplin & Dean (2013) on eliciting state-dependent stochastic choice.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
