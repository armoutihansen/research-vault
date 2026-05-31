---
citekey: Manzini2014
title: Stochastic Choice and Consideration Sets
authors: ["Manzini, Paola", "Mariotti, Marco"]
year: 2014
type: journalArticle
doi: 10.3982/ECTA10575
zotero: "zotero://select/library/items/ZRKKYKUK"
pdf: /Users/jesper/Zotero/storage/58FJZE89/Manzini2014.pdf
tags: [literature]
keywords: [stochastic-choice, consideration-sets, limited-attention, random-utility, revealed-preference, luce-model, identification, bounded-rationality]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Manzini2007, Masatlioglu2012]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We model a boundedly rational agent who suffers from limited attention. The agent considers each feasible alternative with a given (unobservable) probability, the attention parameter, and then chooses the alternative that maximizes a preference relation within the set of considered alternatives. We show that this random choice rule is the only one for which the impact of removing an alternative on the choice probability of any other alternative is asymmetric and menu independent. Both the preference relation and the attention parameters are identified uniquely by stochastic choice data.

## Summary
Introduces the **random consideration set model** (RCSM): a boundedly rational agent has a fixed strict preference $\succ$ and maximizes it over a *stochastically formed* consideration set, where each alternative $a$ enters that set independently with a menu-independent **attention parameter** $\gamma(a)\in(0,1)$. The paper gives a two-axiom characterization and shows that **both** $\succ$ and $\gamma$ are *uniquely identified* from stochastic choice data — a sharp identification that deterministic consideration-set models cannot deliver.

## Research question
Can the randomness in observed choice be attributed to **limited attention** (consideration errors) rather than utility noise, in a way that (i) is testable by simple axioms on choice frequencies and (ii) — unlike the deterministic attention model of [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay]] (2012, "MNO") — **uniquely recovers** both the preference ordering and the attention parameters from the choice data it generates?

## Method / identification
The primitive is a random choice rule $p(a\mid A)$ over menus $A$ from a rich domain, with a **default** option $a^*$ (the agent may pick nothing). The model posits a strict total order $\succ$ and attention parameters $\gamma:X\to(0,1)$ with

$$
p_\gamma(a\mid A) \;=\; \gamma(a)\!\!\prod_{b\in A:\,b\succ a}\!\!\bigl(1-\gamma(b)\bigr),
$$

i.e. $a$ is chosen iff it is considered (prob. $\gamma(a)$) and every $\succ$-better alternative is *not* considered. Identification is the core contribution:

- **Revealed preference**: $a\succ b$ iff *removing* $a$ raises the choice probability of $b$, i.e. $p(b\mid A\setminus\{a\}) > p(b\mid A)$. A higher raw frequency does **not** reveal preference, since it conflates ranking with attention.
- **Revealed attention**: $\gamma(a)=p(a\mid\{a\})$ when singletons are observed, or from binary menus
$$
\gamma(a) \;=\; 1-\frac{p(a^*\mid\{a,b\})\,p(a^*\mid\{a,c\})}{p(a^*\mid\{b,c\})}.
$$

The axioms constrain the **impact** of removing $b$ on $a$, $\dfrac{p(a\mid A\setminus\{b\})}{p(a\mid A)}$:

- **i-Asymmetry**: $\dfrac{p(a\mid A\setminus\{b\})}{p(a\mid A)}=1 \;\Rightarrow\; \dfrac{p(b\mid A\setminus\{a\})}{p(b\mid A)}=1$ — if $b$ is non-neutral for $a$, then $a$ is neutral for $b$.
- **i-Independence**: the impact of $b$ on $a$ is identical across menus — a menu-independence condition parallel to, but weaker/distinct from, Luce's IIA $\bigl(\tfrac{p(a\mid A)}{p(b\mid A)}=\tfrac{p(a\mid B)}{p(b\mid B)}\bigr)$.

**Theorem 1**: a random choice rule satisfies i-Asymmetry and i-Independence **iff** it is a random consideration set rule $p_\gamma$, and then $(\succ,\gamma)$ are **unique**.

## Data
None — purely theoretical/axiomatic. The paper relates its predictions to experimental regularities (choice-frequency reversals, stochastic-transitivity violations) but estimates nothing.

## Key findings
- **Theorem 1** plus unique identification of $(\succ,\gamma)$ from choice frequencies — the signature result.
- A weak **stochastic path-independence** property: whenever $b$ boosts $a$,
$$
p(a\mid A\setminus\{b\}) \;=\; \frac{p(a\mid A)}{1-p(b\mid\{b\})},
$$
so an alternative's boost depends only on its singleton "strength."
- The RCSM rationalizes patterns the **Luce/logit** rule cannot: violations of Luce's IIA, **choice-frequency reversals** (e.g. $p(a\mid\{a,b,c\})>p(b\mid\{a,b,c\})$ yet $p(b\mid\{a,b\})>p(a\mid\{a,b\})$), and **weak stochastic intransitivity** — all with a transitive underlying preference.
- Weak stochastic transitivity fails **exactly when** the attention ordering is opposite to $\succ$.
- A nuanced reading of the **blue-bus/red-bus** problem: duplicates of an *inferior* alternative are redundant, but duplicates of a *superior* one are not (each extra copy raises the chance it is noticed).
- **Theorem 2** (limits result): if attention may be **menu-dependent** $\bigl(\delta(a,A)\bigr)$, then *every* random choice rule is rationalizable for *every* $\succ$ — the model becomes empirically vacuous and $\succ$ unidentified.

## Contribution
The first stochastic consideration-set model that is simultaneously **axiomatically characterized** and **uniquely identified**, extending classical revealed-preference method to bounded-rationality-via-inattention. It reframes choice stochasticity as *consideration error* — a restricted form of Random Utility Maximization (the "mood" interpretation) — rather than *utility error* (Luce/logit), and shows exactly the empirical content this buys.

## Limitations & open questions
- **Menu-independent attention** is essential: Theorem 2 shows full menu dependence is too permissive, leaving open *which restricted forms* of menu dependence remain tractable and identified — a concrete modeling gap.
- Preferences are **deterministic and fixed**; only consideration is stochastic, so there is no account of genuine utility noise. Is a hybrid consideration-plus-utility-error model still identified?
- The companion **no-default** variant (re-consider until something is noticed) lacks the same identifiability; the authors **explicitly leave its axiomatic characterization open**.
- Identification leans on a **rich domain** (singletons/binary menus observed); weaker or field domains may break point identification.
- Empirically the model explains only **weak** stochastic-transitivity violations, not the more pervasive **strong** ones — its descriptive reach is bounded.

## Connections
Extends [[@Manzini2007|Manzini & Mariotti (2007)]] "shortlisting" and MNO (2012); contrasts with Luce (1959)/multinomial logit (McFadden 1974), the attribute rule of Gul–Natenzon–Pesendorfer (2010), and Tversky's Elimination-by-Aspects; situates the rule inside Block–Marschak/McFadden RUM.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
