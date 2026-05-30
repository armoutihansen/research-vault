---
citekey: Lleras2017
title: "When more is less: Limited consideration"
authors: ["Lleras, Juan Sebastián", "Masatlioglu, Yusufcan", "Nakajima, Daisuke", "Ozbay, Erkut Y."]
year: 2017
type: journalArticle
doi: 10.1016/j.jet.2017.04.004
zotero: "zotero://select/library/items/SYJ2DJPW"
pdf: /Users/jesper/Zotero/storage/PWR4UG4P/Lleras2017.pdf
tags: [literature]
keywords: [limited-consideration, consideration-sets, revealed-preference, choice-overload, bounded-rationality, attention, welfare-analysis]
topics: []
related: [Apesteguia2013, Caplin2011, Cherepanov2013, Dutta2015, Eliaz2011, Hauser1990, Jeuland1983, Mandler2012, Manzini2007, Masatlioglu2012, Masatlioglu2013, Rubinstein2006, Salant2008]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> There is well-established evidence that decision makers consistently fail to consider all available options. Instead, they restrict attention to only a subset of alternatives and then undertake a more detailed analysis of this reduced set. This systematic lack of consideration of available options can lead to a “more is less” effect, where excess of options can be welfare-reducing for a decision-maker (DM). Building on this idea, we model individuals who might pay attention to only a subset of the choice problem presented to them. Within this smaller set, a DM is rational in the standard sense, and she chooses the maximal element with respect to her preference. We provide a choice theoretical foundation for our model. In addition, we show which alternatives are revealed preferred to which and discuss welfare implications.

## Summary
The paper builds an axiomatic choice-theoretic model of "choice overload": a decision maker (DM) considers only a subset of the feasible menu, then maximizes a standard preference within that consideration set. The key structural assumption is the **Competition Filter** — if an option attracts attention in a large menu, it still attracts attention in any subset. The resulting **Overwhelming Choice (OC)** model is characterized by a single behavioral axiom, a weakening of WARP. Although the model rationalizes apparent preference reversals, it still permits sharp welfare inference: precisely those choice reversals between nested menus reveal preference, and they pin down exactly when "more is less."

## Research question
Can the empirical phenomenon of choice overload — DMs neglecting available options because there are too many — be given a falsifiable revealed-preference foundation? Specifically: (1) what observable restriction on choice data is necessary and sufficient for a DM to be maximizing a stable preference over an (unobserved) attention-limited consideration set whose formation obeys "more is less"; and (2) since being chosen no longer reveals being preferred, what choice data permit welfare/preference inference?

## Method / identification
The framework is abstract single-valued choice theory. Let $X$ be a nonempty set of alternatives and $\mathcal{X}$ the nonempty subsets. A **consideration map** $\Gamma:\mathcal{X}\to\mathcal{X}$ assigns to each feasible menu $S$ a considered subset $\Gamma(S)\subseteq S$. The central restriction is:

**Competition Filter.** For all $x\in S\subseteq T$, if $x\in\Gamma(T)$ then $x\in\Gamma(S)$.

(That is, attention grabbed in a larger, more competitive menu survives in any smaller menu — formally Sen's $\alpha$ applied to consideration rather than to choice.) The DM then maximizes a strict linear order $\succ$ over the considered set. A choice function $c$ is an **Overwhelming Choice (OC)** if there exist $\succ$ and a competition filter $\Gamma$ with $c(S)=\max(\succ,\Gamma(S))$.

The behavioral test weakens WARP by separating "feasible" from "considered." Standard WARP asks for a best element $b^{*}\in S$ chosen from any $T\ni b^{*}$ with $c(T)\in S$. The relaxation only invokes this when $b^{*}$ is known to be considered, which (via the competition filter) holds when $b^{*}$ was chosen from some superset:

**(A1) WARP-CO.** For any nonempty $S$ there is $b^{*}\in S$ such that for any $T\ni b^{*}$: if (i) $c(T)\in S$ and (ii) $b^{*}=c(T')$ for some $T'\supset T$, then $c(T)=b^{*}$.

Revealed preference is defined directly from choice reversals: $x\,P\,y$ if $x=c(S)$, $y=c(T)$ with $\{x,y\}\subseteq S\subset T$ (choosing $y$ from the larger menu certifies $y$ is considered in $S$, so picking $x$ in $S$ reveals $x\succ y$). $P_{T}$ is its transitive closure. The Appendix extends everything to **choice correspondences** with a weak order (allowing indifference), via two axioms: **Weak Revealed Indifference (WRI)** and **No Cyclic Choice Reversals (NCCR)**.

## Data
None — this is a pure axiomatic decision-theory paper. It cites supporting empirical/eye-tracking evidence (Reutskaja et al. 2011; Miller 1956; marketing work of [[@Jeuland1983|Shugan 1983]], [[@Hauser1990|Hauser–Wernerfelt 1990)]] to motivate the competition-filter axiom, but proves no estimates and runs no experiment.

## Key findings
- **Lemma 1.** $c$ satisfies WARP-CO if and only if the revealed-preference relation $P_{T}$ is acyclical.
- **Theorem 1 (characterization).** $c$ is an Overwhelming Choice if and only if it satisfies WARP-CO. The model is thus fully testable nonparametrically from choice data even though consideration sets are never observed; only three observations can falsify it (e.g. $c(\{x,y,z,t\})=y$, $c(\{x,y,z\})=x$, $c(\{x,y\})=y$).
- **Proposition 1 (revealed preference).** For an OC, $x$ is revealed preferred to $y$ (i.e. ranked above $y$ in *every* representation $(\Gamma,\succ)$) if and only if $x\,P_{T}\,y$. Choice reversals are both necessary and sufficient for preference revelation; being chosen alone reveals nothing.
- **Corollary 1 (welfare / "more is less").** A smaller menu $S\subset T$ is strictly welfare-enhancing whenever $c(S)\,P_{T}\,c(T)$ (in particular when $c(T)\in S$ and $c(S)\neq c(T)$). Conversely, if $c(T)\notin S$ the larger menu can be welfare-enhancing, so even WARP-compliant data cannot guarantee "more is better."
- **Indistinguishability result.** Any competition filter can be rewritten as both a categorization shading relation $\Gamma_{\sqsupset}$ ([[@Mandler2012|Manzini–Mariotti 2012)]] and a set of rationales $\Gamma_{\{R_i\}}$ (Cherepanov et al. 2013); the three first stages generate identical choice behavior and are inseparable on choice data alone.
- **Theorem 2 / Propositions 2–4, Corollary 2.** For choice correspondences, OC is characterized by NCCR + WRI; $R=P\cup I$ has well-defined transitive closure $R_{T}$, and its asymmetric/symmetric parts $P_{T}$, $I_{T}$ exactly characterize revealed strict preference and revealed indifference.

## Contribution
The paper supplies a clean revealed-preference foundation for choice overload and the "more is less" effect, reducing a rich class of consideration heuristics (Top-N, shortlisting, top-on-each, categorization, rationalization, narrowing down) to a single intuitive property (the competition filter) and a single testable axiom (WARP-CO). Relative to [[@Masatlioglu2012|Masatlioglu, Nakajima and Ozbay (2012)]], whose **Attention Filter** is built on unawareness (removing an unconsidered item leaves the consideration set unchanged), the competition filter is orthogonal and complementary: it captures the size/competition channel that the attention filter explicitly does not, and it covers categorization, rationalization and narrowing-down examples that violate the attention filter. The welfare results give applied analysts an operational criterion — observed choice reversals — for diagnosing when adding options hurts consumers.

## Limitations & open questions
- The authors note that combining their competition filter with the Masatlioglu et al. (2012) attention filter (consideration sets satisfying *both*) does **not** yield a clean characterization; they state the result exists "upon request" but is omitted for space — an explicit open modeling problem.
- Preferences are **not point-identified**: multiple $\succ$ can rationalize the same data, so only the partial order $P_{T}$ is recovered. Welfare statements are therefore necessarily partial.
- The model is silent on *how* the consideration set forms — by design it does not commit to a heuristic, which is exactly why categorization, rationalization and the OC model are shown to be observationally equivalent. Distinguishing the underlying psychological mechanism would require data beyond standard choice (e.g. process/attention data).
- The competition filter is imposed as an axiom motivated by marketing/eye-tracking evidence rather than derived; direct experimental testing of WARP-CO and of the competition-filter property itself is left open.

## Connections
The paper sits squarely in the bounded-rationality / limited-attention revealed-preference literature. Its closest sibling is **[[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]]** "Revealed Attention" (attention filter, unawareness), from which it borrows the every-representation definition of revealed preference and which it positions as complementary. The two-stage "consider then maximize" structure connects it to sequential-elimination models: **[[@Manzini2007|Manzini & Mariotti (2007)]]** shortlisting / sequentially rationalizable choice, **[[@Apesteguia2013|Apesteguia & Ballester (2013)]]** and **[[@Dutta2015|Dutta & Horan (2015)]]** on identifying rationales, **[[@Mandler2012|Manzini & Mariotti (2012)]]** categorization (Weak-WARP), and **[[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]]** rationalization (also Weak-WARP) — the latter two shown here to be choice-equivalent to OC. Related consideration-set work includes **[[@Salant2008|Salant & Rubinstein (2008)]]** "(a,f): choice with frames," **[[@Rubinstein2006|Rubinstein & Salant (2006)]]** choice from lists, **[[@Masatlioglu2013|Masatlioglu & Nakajima (2013)]]** iterative search, **[[@Caplin2011|Caplin & Dean (2011)]]** search and choice-process data, **[[@Eliaz2011|Eliaz, Richter & Rubinstein (2011)]]** choosing finalists, and **Masatlioglu & Ok (2014)** reference-dependent choice with psychological constraints. The motivating "choice overload"/"paradox of choice" evidence draws on **Reutskaja et al. (2011)**, **Miller (1956)**, **Gourville & Soman (2005)** and **Schwartz (2005)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
