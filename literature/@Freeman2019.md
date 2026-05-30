---
citekey: Freeman2019
title: Expectations-based reference-dependence and choice under risk
authors: ["Freeman, David J."]
year: 2019
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/J5VXFCD7"
pdf: /Users/jesper/Zotero/storage/52H2UH89/Freeman2019.pdf
tags: [literature]
keywords: [reference-dependent-preferences, expectations-based-reference-points, choice-under-risk, personal-equilibrium, revealed-preference, loss-aversion, axiomatic-characterization]
topics: []
related: [Abeler2011, Bell1985, Crawford2011, Freeman2017, Gul1991, Kahneman1979, Koszegi2006b, Loomes1986, Masatlioglu2016, Ok2015, Sarver2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero) — The published article abstract reads: "This article characterises the behavioural content of a model of choice under risk with reference-dependent preferences and endogenous expectations-based reference points based on the preferred personal equilibrium model of Kőszegi and [[@Koszegi2006b|Rabin (2006)]]. The combination of reference-dependent preferences and endogenous reference points leads to violations of the Independence Axiom and can also lead to violations of the Weak Axiom of Revealed Preference. An axiomatic characterisation shows that the model places testable restrictions on choice under risk."

## Summary
Freeman gives a revealed-preference (axiomatic) foundation for Kőszegi–Rabin's preferred-personal-equilibrium (PPE) model of expectations-based reference-dependence, restricted to choice under risk. The central tension he resolves is an identification puzzle: in a PPE the decision-maker's (DM) choice and her reference point coincide by construction, so it is not obvious that reference-dependence leaves any observable footprint in choice. By observing two primitives — a commitment ranking (CPE) and a no-commitment choice correspondence — and exploiting the partial separation between expectations and choice that risk allows, he shows the model is testable, can violate Independence, the Weak Axiom of Revealed Preference (WARP), and dynamic consistency, and yet still places sharp restrictions on choice that any analyst can check.

## Research question
What is the testable behavioural content of Kőszegi and Rabin's PPE model when applied to choice under risk, given that reference points and expectations are never directly observed and that, in equilibrium, choice and reference point coincide? Can the influence of expectations-based reference-dependence be identified from observable choice alone?

## Method / identification
Pure decision theory: an axiomatic characterisation, no data of the author's own. Let $X$ be a finite outcome set and $\Delta$ the lotteries over it; $\mathcal{D}$ is the set of finite choice sets $D\subseteq\Delta$. A reference-dependent utility $v:\Delta\times\Delta\to\mathbb{R}$ gives utility $v(\cdot\mid p)$ when the reference lottery is $p$. The personal equilibria of $D$ are $PE_v(D)=\{p\in D: v(p\mid p)\ge v(q\mid p)\ \forall q\in D\}$, the preferred PE refinement is $PPE_v(D)=\arg\max_{p\in PE_v(D)} v(p\mid p)$, and the choice-acclimating concept is $CPE_v(D)=\arg\max_{p\in D} v(p\mid p)$, so $PPE_v(D)=CPE_v(PE_v(D))$.

The analyst observes a *pair* of primitives: a CPE ranking $\succsim$ over lotteries (how a DM ranks when she can commit at $t=1$ to a choice resolving after $t=2$) and a choice correspondence $c:\mathcal{D}\rightrightarrows\Delta$ (how she chooses when she anticipates the set but cannot commit). An **EU-PPE representation** requires $c(D)=PPE_v(D)$ for a jointly continuous $v$ each of whose $v(\cdot\mid p)$ is an expected-utility (linear-in-probabilities) function. The key identification device is the *conditional choice under risk*: facing $\{p\}\alpha\{q,r\}$ (mixtures) with $\alpha$ small holds the reference point near $p$, so $v(\cdot\mid p)$ can be elicited from choices of the form $\{p\alpha q, p\alpha r\}$.

Six axioms characterise the model. A1 (CPE preferences complete/transitive/continuous); A2 (Non-Intrinsic Preference for Commitment: $p\in c(D)$, $p\in D'\subseteq D$, $q\in c(D')$ imply $q\succsim p$); A3$'$ (Conditional Exclusion Consistency) plus A3 (a continuity/upper-hemicontinuity strengthening that implies A3$'$); A4 (Best Prize Dominance: a single best prize $x^\star$ exists); A5 (Weak Reference Bias); and A6 (Transitive Limit, requiring conditional choice to look like a standard transitive model as expectations become fixed).

## Data
None — this is a decision-theory paper. It is calibrated against, but does not estimate from, third-party experimental and applied work: the mugs-and-pens between-subject endowment design of Ericson and Fuster (2011) and the random-sales pricing application of Heidhues and Kőszegi (2014), both with the linear loss-averse Kőszegi–Rabin form $\mu(z)=\eta z$ for $z\ge 0$ and $\mu(z)=\eta(1+\lambda)z$ for $z<0$.

## Key findings
**Anomalies (Section 2).** Worked examples in the linear loss-averse Kőszegi–Rabin form show EU-PPE choices can violate (i) the Independence Axiom, (ii) WARP — driven by an expectations-based attachment/endowment effect, as in the random-sales example where $\{a\}=c(\{a,s,r,n\})$ but $\{n\}=c(\{a,n\})$ — and (iii) dynamic consistency, since $c(D)$ at $t=2$ can differ from the CPE-preferred plan at $t=1$, generating a non-intrinsic preference for commitment.

**Theorem 1 (main).** $(\succsim,c)$ satisfies A1–A6 if and only if it has an EU-PPE representation consistent with $\succsim$ and increasing in $x^\star$. **Corollary 1** gives the matching uniqueness: any two continuous EU-PPE representations of the same $c$ induce the same reference-dependent and CPE preferences. The representation also forces $PE_v(D)\ne\varnothing$ for every $D$, equivalent to $v$ satisfying the **limited cycle inequalities** (Definition 6).

**Theorem 2.** Replacing A5 by the stronger A5$'$ (Strong Reference Bias: $p\in c(\{p,q\})$ implies $p\in c(\{p\}\alpha\{p,q\})$) characterises the EU-PPE representations that additionally *PPE-dislike mixtures*.

**Proposition 1.** Linear loss-averse Kőszegi–Rabin preferences satisfy the limited cycle inequalities and PPE-dislike mixtures — so the headline applied model is a special case of EU-PPE (and a pure-strategy PE always exists).

**Section 5 / Propositions 2–4.** Definition 8 gives a behavioural notion of exhibiting (strict) reference-dependence via Independence violations. Proposition 2: $c$ strictly exhibits reference-dependence iff some $v(\cdot\mid p)$, $v(\cdot\mid q)$ represent different preferences; any WARP-violating EU-PPE $c$ exhibits reference-dependence (sufficient, not necessary). Proposition 3: with the linear loss-averse form, strict reference-dependence holds iff $\eta\lambda>0$. Proposition 4: WARP violations imply dynamic inconsistency, but not conversely (a Strotzian $v(q\mid p)=w(q)+u(p)-w(p)$ is dynamically inconsistent yet WARP-consistent and not strictly reference-dependent). The Discussion stresses that allowing WARP violations is the most novel feature and is empirically untested.

## Contribution
First revealed-preference foundation for the *endogenous, choice-set-level* expectations-based reference point of PPE in the risk domain. Unlike prior disappointment-aversion models (where the reference point is fixed by each lottery itself, preserving a complete transitive preference), here a single reference lottery is determined for the whole choice set, which is exactly what lets the model break WARP and forces analysis of a choice *correspondence* rather than a single preference. It demonstrates that reference-dependence is identifiable from choice despite choice and reference point coinciding, shows the widely-applied linear loss-averse Kőszegi–Rabin form is a disciplined special case, and ranks the anomalies: Independence violations are more fundamental than WARP violations (the latter imply the former, not vice versa).

## Limitations & open questions
- No direct empirical test of the model's permission for WARP violations exists; experiments are needed to learn whether a descriptive theory should allow them and whether they take the forms the axioms permit (explicit in the Discussion).
- The two-period $t=1/t=2$ timing is a simplification; how reference points actually update over time is left to others (Song, 2016), and taking $t=1$ too close to $t=2$ could make axiom failures reflect insufficient updating time rather than the model.
- Continuity axioms A3 and A6 are not exactly testable, only approximately (Table 1 gives an approximate test of A6).
- The analysis assumes a choice is observed from *every* choice set, ruling out the non-existence of PE that arises under "grass-is-greener" preferences; characterising behaviour without this assumption is open.
- Existence questions for the Kőszegi–Rabin form beyond the linear loss-averse case (when randomisation is needed for a non-empty PE) are noted but not resolved.

## Connections
Builds directly on Kőszegi and [[@Koszegi2006b|Rabin]] (2006, 2007) (PE/PPE/CPE concepts) and Kőszegi (2010) (PE on rich domains). Closest decision-theoretic companions are [[@Freeman2017|Freeman (2017)]], which characterises PPE on unstructured alternatives via a lexicographic composition of two relations, and Gul and Pesendorfer (2008), which characterises PE choice as maximising a complete possibly-non-transitive relation; Dalton and Ghosal (2018) axiomatise a model nesting PE. The disappointment-aversion lineage — [[@Loomes1986|Loomes and Sugden (1986)]], [[@Gul1991|Gul (1991)]], [[@Bell1985|Bell (1985)]], Delquié and Cillo (2006), and [[@Masatlioglu2016|Masatlioglu and Raymond (2016)]] on the CPE form as rank-dependent utility — is contrasted because their reference points are lottery-specific. Observable-reference-point axiomatics include Sugden (2003), Masatlioglu and Ok (2005, 2014), Sagi (2006), and Apesteguia and Ballester (2009). The attraction-effect endogenous-reference models of [[@Ok2015|Ok, Ortoleva and Riella (2015)]] and Tserenjigmid (2017) are shown to intersect PPE only at rational choice. Foundational and related risk/menu work includes [[@Kahneman1979|Kahneman and Tversky (1979)]], Quiggin (1994) (rank-dependent utility), Loomes and Sugden (1982) on regret theory, [[@Sarver2008|Sarver (2008)]] and Gul and Pesendorfer (2001) on menu choice, and Segal and Spivak (1990) on the preference for certainty. Applications drawn on include Heidhues and Kőszegi (2008, 2014), Herweg and Mierendorff (2013), Herweg, Müller and Weinschenk (2010), Karle and Schumacher (2017), Rosato (2016), [[@Crawford2011|Crawford and Meng (2011)]], Pagel (2016, 2017), and the experiments of Ericson and Fuster (2011), [[@Abeler2011|Abeler et al. (2011)]], Gill and Prowse (2012), Baillon et al. (2017), and Song (2016). The Strotzian special case links to the literature on dynamic inconsistency.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
