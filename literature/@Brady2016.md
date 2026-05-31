---
citekey: Brady2016
title: Menu-Dependent Stochastic Feasibility
authors: ["Brady, Richard L.", "Rehbeck, John"]
year: 2016
type: journalArticle
doi: 10.3982/ECTA12694
zotero: "zotero://select/library/items/4Q5GW4DV"
pdf: /Users/jesper/Zotero/storage/48WUS3AN/Brady2016.pdf
tags: [literature]
keywords: [stochastic-choice, random-feasibility, consideration-sets, revealed-preference, random-utility, substitutes-complements, mobius-inversion]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Manzini2014]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We examine the role of stochastic feasibility in consumer choice using a random conditional choice set rule (RCCSR) and uniquely characterize the model from conditions on stochastic choice data. Feasibility is modeled to permit correlation in availability of alternatives. This provides a natural way to examine substitutability/complementarity. We show that an RCCSR generalizes the random consideration set rule of [Manzini and Mariotti, 2014]. We then relate this model to existing literature. In particular, an RCCSR is not a random utility model.

## Summary
A short "Notes and Comments" piece in *Econometrica* that explains stochastic choice not through random utility but through *random feasibility*: the agent has a fixed strict preference and maximizes it over a randomly drawn feasible subset of the offered menu, defaulting to an outside option $x^*$ when the feasible set is empty. The key device is a **Random Conditional Choice Set Rule (RCCSR)**, in which a single full-support distribution $\pi$ over subsets is conditioned on the offered menu. Because $\pi$ lives on *subsets*, it can encode correlation in availability, giving a clean revealed-preference handle on substitutes vs. complements. The paper axiomatizes the RCCSR uniquely from choice data, shows it strictly generalizes [[@Manzini2014|Manzini–Mariotti's (2014)]] random consideration set rule (recovered by swapping one axiom), and proves it is *not* a random utility model.

## Research question
When a researcher observes stochastic choice (e.g., scanner data on repeat grocery purchases) but cannot observe which alternatives were actually available at each purchase, can the apparent randomness be attributed entirely to *random feasibility* of a rational agent? Specifically: (i) what behavioral conditions on stochastic choice data exactly characterize a deterministic-preference / random-feasible-set model, (ii) can preferences and the feasibility distribution be uniquely recovered, and (iii) how does such a model relate to random utility and to consideration-set models?

## Method / identification
The primitive is a random choice rule $P:X^*\times\mathcal{D}\to[0,1]$ on a *rich* domain $\mathcal{D}$ of menus (all binary menus present, closed under taking subsets), where $X^* = X\cup\{x^*\}$ and $x^*$ is an always-available default. The agent has a strict total order $\succ$ on $X$ and faces a random feasible set $F(A)\subseteq A$. Given a full-support distribution $\pi$ on $\mathcal{D}$, the conditional feasibility probability is
$$\Pr\big(F(A)=B\big)=\frac{\pi(B)}{\sum_{C\subseteq A}\pi(C)}.$$
Letting $A_a=\{B\subseteq A \mid a\in B,\ \forall b\in B\setminus\{a\}\ a\succ b\}$ be the subsets in which $a$ is the $\succ$-best element, the **RCCSR** sets
$$P_{\succ,\pi}(a,A)=\frac{\sum_{B\in A_a}\pi(B)}{\sum_{C\subseteq A}\pi(C)},$$
i.e., the probability $a$ is the best *feasible* alternative. Identification rests on a **sequential independence** relation: $b\,I_A\,a$ iff $P(b,A)=P\big(b,A\setminus\{a\}\big)\,P\big(A^*\setminus\{a\},A\big)$, equivalently the hazard-rate form $P\big(b,A\setminus\{a\}\big)=P(b,A)/\big(1-P(a,A)\big)$. Revealed preference is defined by $a\succ b \iff b\,I_A\,a$ for some $A$. The characterization uses four axioms: **ASI** (asymmetric sequential independence — exactly one of $a\,I_{\{a,b\}}\,b$ or $b\,I_{\{a,b\}}\,a$), **TSI** (transitivity of that relation), **ESI** (expansion from binary to union menus), and **IFO** (Increasing Feasible Odds). IFO is stated via successive marginal differences of the feasibility odds $O_A=P(A,A)/P(x^*,A)$ and is shown equivalent to a *multiplicative* Block–Marschak positivity condition on the default-choice probability:
$$\sum_{B\subseteq A}(-1)^{|A\setminus B|}\!\!\prod_{C\subseteq A:\,C\neq B}\!\!P(x^*,C)>0.$$
The sufficiency proof builds $\succ$ from ASI/TSI/ESI, pins down default-choice probabilities, and reconstructs $\pi$ from $P(x^*,\cdot)$ via **Möbius inversion** (Shafer 1976) on the subset lattice, normalizing the resulting set function $\lambda$ into a probability $\tilde\lambda=\pi$.

## Data
None — purely theoretical / axiomatic. The "grocery store" scanner-data setup is a motivating narrative and a worked numerical example (Table I), not an empirical dataset.

## Key findings
- **Theorem 3.1 (main characterization + uniqueness):** A random choice rule satisfies ASI, TSI, ESI, and IFO iff it is an RCCSR $P_{\succ,\pi}$; moreover the pair $(\succ,\pi)$ is *unique*.
- **Theorem 3.3 (nesting Manzini–Mariotti):** Replacing IFO with **MIDO** (Menu-Independent Default Option, $P(x^*,A\setminus\{a\})/P(x^*,A)=P(x^*,B\setminus\{a\})/P(x^*,B)$) characterizes exactly the random consideration set rule $P_{\succ,\gamma}(a,A)=\gamma(a)\prod_{b\in A:\,b\succ a}\big(1-\gamma(b)\big)$, with $(\succ,\gamma)$ unique. Hence the consideration-set rule is the special case $\pi(A)=\prod_{a\in A}\gamma(a)\prod_{b\in X\setminus A}\big(1-\gamma(b)\big)$, an axiomatic generalization differing in a single condition.
- **Theorem 3.2 (no content with menu-dependent parameters):** If feasibility weights are allowed to depend on the menu, $\nu(\cdot,A)$, then for *every* strict order $\succ$ and *every* random choice rule $P$ there is a representation $P=P_{\succ,\nu}$ — so menu-dependent parameters have no empirical content, motivating the menu-*independent* $\pi$.
- **Not a random utility model:** Example 1 violates regularity ($P(a,B)\ge P(a,A)$ for $B\subseteq A$ fails), so RCCSRs are not nested in RUMs; conversely the Luce rule (a RUM) violates the IIA-decrease an RCCSR forces on $\ge 3$-element menus, so RUMs are not nested in RCCSRs. The intersection is nonempty (the consideration-set rule lies in both).
- **Substitutes/complements via correlation:** $\pi$ over subsets permits $\Pr(a\in F(A)\mid b\in F(A))\neq\Pr(a\in F(A))$; negative correlation reads as substitutability. The worked example also exhibits a violation of MM's **i-Asymmetry**, with two goods each benefiting from the other's removal — behavior an RCCSR allows but the consideration-set rule forbids.
- **Limited data:** From two menus differing by one alternative $b$, one can rank $b$ against all others and bound $\Pr(b\in F(A))$; Lemma 3.1 shows the axioms force the default to satisfy sequential independence, so a default ranked above some alternative needs a different characterization.

## Contribution
Reframes "stochastic choice" as a problem of unobserved, correlated *availability* rather than randomness in tastes or attention. The RCCSR delivers a fully identified model ($\succ$ and $\pi$ both unique) with a transparent revealed-preference apparatus (sequential independence / hazard rates), gives a clean axiomatic embedding of the Manzini–Mariotti consideration-set rule (one swapped axiom), and uses subset-level probabilities to make substitutability/complementarity a primitive of the model. The Möbius-inversion route from default-choice probabilities to the feasibility measure is a reusable technique linking choice data to a capacity on the subset lattice.

## Limitations & open questions
- **Removing the default.** Without $x^*$ (i.e., $\pi$ on $\mathcal{D}\setminus\emptyset$), identification fails: $\succ$ is recovered only up to the two least-preferred alternatives. Whether the default can be removed by a Horan (2014)-style argument is left as an **explicit open question**.
- **Defaults that are not worst-ranked.** Lemma 3.1 forces the default to satisfy sequential independence; a model where $x^*$ is preferred to some real alternative "would require a different characterization."
- **Full-support $\pi$ is implausible for consideration.** The authors call full support "hardly defensible for consideration sets" and relegate a limited-support / pairwise-consideration variant to Appendix C of the Supplement.
- **No measurement / feasibility error** is modeled, mirroring much of the stochastic-choice literature.
- **Empirical discrimination.** Several stated routes to *distinguish* RCCSR from the regular perception-adjusted Luce model (rPALM) from data are flagged but not carried out; likewise the conjecture that RCCSR-like behavior could be micro-founded by a profit-maximizing firm choosing a costly stochastic-menu technology is raised as a direction, not a result.

## Connections
The direct parent is [[@Manzini2014|Manzini and Mariotti (2014)]], "Stochastic Choice and Consideration Sets" (*Econometrica*), strictly generalized here; Horan (2014) supplies the default-free consideration characterization the open question points back to, and Manzini, Mariotti, and Ülkü (2015) motivate correlation-based identification of substitutes/complements. The non-nesting results engage the random-utility tradition of Block and Marschak (1960), Falmagne (1978) and Fiorini (2004) (Block–Marschak polynomials), and Luce (1959) (IIA). Closest competitors using hazard-rate conditions are Echenique, Saito, and Tserenjigmid's regular perception-adjusted Luce model (rPALM) and Gul, Natenzon, and Pesendorfer (2014)'s attribute rule (every attribute rule is a RUM). A separate lineage — Machina (1985), Mattsson and Weibull (2002), and Fudenberg, Iijima, and Strzalecki (2015) — generates stochastic choice from deterministic preferences over lotteries; Aguiar (2015) studies the same Block–Marschak / capacity machinery for categorization. Methodologically the paper draws on Möbius inversion as used since Shapley (1953) and formalized in Shafer (1976).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
