---
citekey: Gerasimou2016
title: Partially dominant choice
authors: ["Gerasimou, Georgios"]
year: 2016
type: journalArticle
doi: 10.1007/s00199-015-0869-8
zotero: "zotero://select/library/items/S87LPHKR"
pdf: /Users/jesper/Zotero/storage/HUQVZ9DI/Gerasimou2016a.pdf
tags: [literature]
keywords: [incomplete-preferences, partial-dominance, attraction-effect, revealed-preference, context-dependent-choice, bounded-rationality, warp-axioms]
topics: []
related: [Bernheim2009, Bordalo2013, Cherepanov2013, Eliaz2006, Eliaz2011, Huber1982, Lombardi2009, Manzini2007, Manzini2012a, Masatlioglu2012, Ok2015, Rubinstein2012, Sen1971, Simonson1989, Tversky1972, deClippel2012]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This paper proposes and analyzes a model of context-dependent choice with stable but incomplete preferences that is based on the idea of partial dominance: an alternative is chosen from a menu if it is not worse than anything in the menu and is also better than something else. This choice procedure provides a simple explanation of the attraction/decoy effect. It reduces to rational choice when preferences are complete in two ways that are made precise. Some preference identification and choice consistency properties associated with this model are analyzed, and certain ways in which its predictions differ from those of other recently proposed models of the attraction effect are also discussed.

## Summary
Gerasimou builds a deterministic choice-theoretic model in which a decision maker with stable but *incomplete* preferences chooses from a menu any alternative that is (i) undominated and (ii) itself dominates some other feasible alternative. This "partial dominance" requirement is a minimal tie-breaker added to the classical maximal-element rule, and it suffices to rationalize the attraction/decoy effect while still nesting standard utility maximization as the complete-preferences special case. The model is characterized by three weakenings of WARP, and the paper supplies two new decompositions of WARP itself, a preference-recovery (welfare-elicitation) result, a catalogue of which consistency axioms survive, and out-of-sample comparisons against three competing models of the attraction effect.

## Research question
When preferences are incomplete and no most-preferred option exists in a menu, what choice rule does (or should) the agent follow, and can a minimal, behaviorally disciplined modification of the standard "choose an undominated option" rule explain the robust attraction/decoy effect while remaining a special case of rational choice? Secondary questions: which WARP-implied consistency axioms does such a rule satisfy or violate, and under what conditions can an outside observer recover the agent's true (incomplete) preferences from choice data?

## Method / identification
The setting is abstract revealed-preference theory. $X$ is a finite grand set with $|X|\geq 3$; $\mathcal{M}$ is the collection of nonempty menus; choice is a nonempty-valued correspondence $C:\mathcal{M}\rightrightarrows X$ with $C(A)\subseteq A$. Preferences are a binary relation $\succ$ that is assumed *asymmetric* and *acyclic* but not necessarily complete; $x$ and $y$ are incomparable when $x\not\succ y$ and $y\not\succ x$ (interpreted as indecisiveness, not indifference).

The **partially dominant (PD)** correspondence is defined by: if every pair in $A$ is incomparable then $C(A)=A$; otherwise
$$C(A)=\Big\{x\in A : z\not\succ x \text{ for all } z\in A,\ \text{ and } x\succ y \text{ for some } y\in A\Big\}.$$
That is, the agent first takes the undominated (maximal) set, then keeps only those maximal options that *also* dominate something — a two-step procedure using one stable preference relation in both steps.

The axiomatic machinery rests on weakenings of WARP via a narrowed revealed-preference notion that only "trusts" binary menus:
- **a-WARP**: if $C(\{x,y\})=x$ and $x\in B$ then $y\notin C(B)$.
- **b-WARP**: if $x\in C(A)$ and $y\in A\setminus C(A)$ then $y\notin C(\{x,y\})$.
- **Partial b-WARP**: if $x\in C(A)$ then $y\notin C(\{x,y\})$ for *some* $y\in A\setminus C(A)$ (relaxes b-WARP from "every" rejected option to "some").
- **Weak Property $\gamma$**: if $x\in C(A_i)$ for $i=1,\dots,k$ and $x=C(A_j)$ uniquely for some $A_j$ with $|A_j|>1$, then $x\in C(\bigcup_l A_l)$.
- **CIR (choice implies rejection)**: $|A|>1\Rightarrow C(A)\subset A$, a weakening of single-valuedness used only to pin down strict rational choice.

Identification of the model is by representation theorem (Proposition 4): the three axioms a-WARP + Partial b-WARP + Weak Property $\gamma$ are *equivalent* to existence of a unique acyclic $\succ$ generating the PD rule. Logical independence of the three is shown by counterexamples in Appendix 2.

## Data
None — this is a pure axiomatic/decision-theory paper with no empirical dataset. Illustration is via stylized two-attribute geometric examples (Figs. 1-2) and small finite enumerations (menus over $\{w,x,y,z\}$).

## Key findings
- **Proposition 1**: For nonempty-valued $C$, WARP $\Leftrightarrow$ (Properties $\alpha$ and $\beta$) $\Leftrightarrow$ (a-WARP and b-WARP) $\Leftrightarrow$ rationalization by a weak order. This gives a *novel* decomposition of WARP into a-WARP/b-WARP, paralleling Sen's $\alpha/\beta$, that splits consistency into "binary-to-large" and "large-to-binary" components.
- **Proposition 2**: Adding CIR, WARP $\Leftrightarrow$ Property $\alpha$ $\Leftrightarrow$ a-WARP, each $\Leftrightarrow$ rationalization by a strict linear order (utility maximization with no indifference).
- **Proposition 3**: a-WARP + Property $\gamma$ $\Leftrightarrow$ the benchmark maximal-element rule under a unique acyclic $\succ$.
- **Proposition 4 (main result)**: a-WARP + Partial b-WARP + Weak Property $\gamma$ characterize the PD correspondence (unique acyclic $\succ$). PD strictly refines the benchmark maximal rule (its choice set is a subset) yet is logically distinct from it.
- **Observation 2**: When $\succ$ is the Pareto partial order on attribute space, PD predicts the attraction effect: $C(\{x,y\})=\{x,y\}$ but $C(\{x,y,z\})=y$ once decoy $z$ (dominated by $y$, attribute-incomparable to $x$) is added. PD also captures "idiosyncratic" attraction effects under subjective dominance.
- **Proposition 5 (preference recovery)**: With $|X|=m>n>2$, if the domain includes all $n$-element menus and there exist $n-2$ alternatives universally incomparable to everything, then the Bernheim–Rangel criterion ("$y$ never chosen in the presence of $x$") correctly reveals $x\succ y$. The simplest case $n=3$ needs all triples plus one universally-incomparable alternative.
- **Observation 3**: PD may violate Properties $\alpha,\beta,\gamma$, Aizerman, Weak WARP, Weakened WARP, and Reference Consistency, but always satisfies Rationality of Indifference and the Eliaz–Richter–Rubinstein (ERR) axiom — putting an upper bound on its irrationality and showing it is *not* a rational-shortlist model (Manzini–Mariotti) nor a revealed-(p)reference model (Ok–Ortoleva–Riella).

## Contribution
The paper's central contribution is a minimal, intuitive bounded-rationality model — menu-independent incomplete preferences producing menu-dependent choices — that explains the attraction/decoy effect while nesting rational choice and being characterized by transparent weakenings of WARP. A secondary, independently useful contribution is the a-WARP/b-WARP decomposition of WARP, which furnishes a new normative yardstick (distinct from Sen's $\alpha/\beta$) for grading the rationality deviations of behavioral choice models: a model can flout both $\alpha$ and $\beta$ yet still satisfy the appealing a-WARP and thereby retain a rationality core. The Proposition 5 recovery result links the procedure to behavioral welfare economics (Bernheim–Rangel) by stating when choices identify welfare preferences.

## Limitations & open questions
- The author flags that the preference restrictions in Proposition 5 (requiring $n-2$ *known* universally incomparable alternatives, and the observer being non-agnostic about which they are) are "particularly demanding and limiting the generality of this result" — recovering incomplete preferences from sparse menu data more generally is left open.
- Footnote 6 explicitly calls for "careful experimental work" to settle whether the attraction effect should be modeled as $C(\{x,y\})=\{x,y\}\to C(\{x,y,z\})=y$ (PD-compatible) or as the a-WARP-violating pattern $C(\{x,y\})=x\to C(\{x,y,z\})=y$; existing between-subject one-shot data cannot discriminate.
- The four hypothetical two-attribute problems (Fig. 2) are offered precisely as designs for *future experiments* to compare PD against the Lombardi (Lo), de Clippel–Eliaz (dCE), and Ok–Ortoleva–Riella models on out-of-sample predictions (compromise effect, similarity effect, dominated-option choice).
- PD does *not* capture the compromise effect or the similarity effect (it merely does not rule them out), whereas dCE precisely captures the compromise effect — leaving open a unified model.
- The model is deterministic; a stochastic-choice extension is implicit but unaddressed.

## Connections
The benchmark maximal-element rule descends from [[@Sen1971|Sen (1971)]], Schwartz (1976), Moulin (1985), Bossert–Sprumont–Suzumura (2005); the WARP/Arrow (1959) foundation and Sen's $\alpha,\beta,\gamma$ are the reference axioms relaxed here. The attraction effect originates with [[@Huber1982|Huber, Payne & Puto (1982)]]; the compromise effect with [[@Simonson1989|Simonson (1989)]]; the similarity effect with Debreu (1960) and [[@Tversky1972|Tversky (1972)]]. Mariotti (2008)'s "justification by an asymmetric relation" framing motivates PD's weakening (every chosen option need only $J$-dominate *some* rejected one), and is contrasted with von Neumann–Morgenstern stable sets. The three rival models of the attraction effect are [[@Lombardi2009|Lombardi (2009)]], de [[@deClippel2012|Clippel & Eliaz (2012)]], and [[@Ok2015|Ok, Ortoleva & Riella (2015)]]; related bounded-rationality machinery includes [[@Manzini2007|Manzini & Mariotti (2007)]] sequential/rational-shortlist choice, [[@Eliaz2011|Eliaz, Richter & Rubinstein (2011)]], [[@Masatlioglu2012|Masatlioglu–Nakajima–Ozbay (2012)]] revealed attention, and [[@Bordalo2013|Bordalo–Gennaioli–Shleifer (2013)]] salience. The welfare-recovery link runs through [[@Bernheim2009|Bernheim & Rangel (2009)]], with related elicitation work by [[@Rubinstein2012|Rubinstein & Salant (2012)]], [[@Manzini2012a|Manzini & Mariotti (2012)]], [[@Cherepanov2013|Cherepanov–Feddersen–Sandroni (2013)]], and Fleurbaey & Schokkaert (2013). Incomparability-versus-indifference foundations draw on [[@Eliaz2006|Eliaz & Ok (2006)]], Mandler (2009), and the author's own Gerasimou (2012).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
