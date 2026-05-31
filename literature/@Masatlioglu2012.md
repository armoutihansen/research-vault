---
citekey: Masatlioglu2012
title: Revealed Attention
authors: ["Masatlioglu, Yusufcan", "Nakajima, Daisuke", "Ozbay, Erkut Y."]
year: 2012
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/X29WH9LR"
pdf: /Users/jesper/Zotero/storage/LDBBKK7J/Masatlioglu2012.pdf
tags: [literature]
keywords: [limited-attention, revealed-preference, consideration-sets, bounded-rationality, welfare-analysis, choice-theory]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Caplin2011, Eliaz2011, Eliaz2011a, Hauser1990, Huber1982, Lehmann1994, Manzini2007, May1954, Salant2008, Samuelson1938, Tversky1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The standard revealed preference argument relies on an implicit assumption that a decision maker considers all feasible alternatives. The marketing and psychology literatures, however, provide well-established evidence that consumers do not consider all brands in a given market before making a purchase (Limited Attention). In this paper, we illustrate how one can deduce both the decision maker's preference and the alternatives to which she pays attention and inattention from the observed behavior. We illustrate how seemingly compelling welfare judgments without specifying the underlying choice procedure are misleading. Further, we provide a choice theoretical foundation for maximizing a single preference relation under limited attention.

## Summary
Classical revealed preference assumes the decision maker (DM) considers every feasible alternative, so any choice reversal is read as irrationality. This paper drops the full-attention assumption: the DM maximizes a single, fixed, complete and transitive preference but only over a *consideration set* she actually attends to. By imposing one minimal, model-free restriction on how consideration sets move with the feasible set—the *attention filter*—the authors show that both the DM's preference *and* her (in)attention can be uniquely identified from ordinary choice data, that the model is testable via a single weakening of WARP, and that model-free welfare criteria (Bernheim–Rangel) can give exactly the wrong answer when attention is limited.

## Research question
Can one recover a DM's welfare-relevant preference from observed choices when she does not consider all feasible alternatives? Specifically: what minimal structure on consideration-set formation makes preference and attention jointly identifiable, what choice data are consistent with such a model, and how does the resulting welfare ranking differ from model-free approaches?

## Method / identification
The setting is abstract choice theory over a finite set $X$ with a deterministic choice function $c:\mathcal{X}\to X$, $c(S)\in S$. A *consideration set mapping* $\Gamma$ assigns to each feasible $S$ a nonempty $\Gamma(S)\subseteq S$. The central primitive is:

- **Attention filter (Definition 1):** $\Gamma(S)=\Gamma(S\setminus x)$ whenever $x\notin\Gamma(S)$. Removing an *unattended* item leaves the consideration set unchanged. This is justified both normatively (unawareness; rational costly consideration) and descriptively (heuristics such as "top $N$", "top on each criterion", "most popular category").
- **Choice with Limited Attention (CLA, Definition 2):** there exist a complete, transitive $\succ$ and an attention filter $\Gamma$ such that $c(S)$ is the $\succ$-best element of $\Gamma(S)$.

Identification runs off choice reversals. Define the direct revealed-preference relation
$$xPy \iff \exists\, T:\ c(T)=x \ne c(T\setminus y).$$
A reversal upon deleting $y$ proves $y$ was attended yet not chosen, so $x\succ y$. Welfare preference is the transitive closure $P_R$. Revealed (in)attention is read symmetrically: $x$ is revealed *not* attended at $S$ when $c(S)=c(S\setminus x)$; revealed attended via Theorem 2's conditions involving $P_R$-dominated items in the symmetric difference of feasible sets. Testability comes from a weakened axiom:

- **WARP(LA):** for any nonempty $S$ there is $x^*\in S$ such that for any $T\supseteq\{x^*\}$, if $c(T)\in S$ and $c(T)\ne c(T\setminus x^*)$, then $c(T)=x^*$.

## Data
None—this is a pure decision-theory paper. Identification is illustrated through stylized examples (a supermarket-aisle display, attraction-effect decoys, cyclical choice); empirical implementation is left as nonparametric revealed-preference testing à la Samuelson on real choice datasets.

## Key findings
- **Theorem 1 (Revealed Preference):** if $c$ is a CLA, then $x$ is revealed preferred to $y$ iff $xP_Ry$. The transitive closure of the reversal relation is exactly the model's welfare ranking, independent of how the consideration set forms.
- **Theorem 2 (Revealed (In)Attention):** full characterization of when $x$ is revealed (not) to attract attention at $S$, again driven by $P_R$.
- **Theorem 3 (Characterization) + Lemma 1:** $c$ is a CLA iff it satisfies WARP(LA), which is equivalent to $P$ being acyclic. So the entire model rests on one behavioral postulate weaker than WARP.
- **Welfare reversal (Example 1):** a supermarket-aisle example where $y$ is chosen whenever $x$ is present and $x$ is never chosen over $y$, so Bernheim–Rangel call $y$ welfare-improving—yet Theorem 1 correctly recovers $x\succ y$ (the true preference). Model-free welfare judgments can be exactly inverted.
- **Anomalies accommodated by fixed preference + limited attention alone:** the attraction effect (including the two-decoy generalization $c(xyd_xd_y)=x$ that defeats most rival models), cyclical choice, and "choosing pairwisely unchosen" ($c(xyz)=z$ but $z$ never wins a binary contest).
- **Model comparison:** CLA is neither nested in nor nests Rationalization (Cherepanov–Feddersen–Sandroni) or Rational Shortlist (Manzini–Mariotti); examples violate Weak WARP, separating CLA from sequentially-rationalizable models.

## Contribution
Provides a choice-theoretic foundation for maximizing a single, stable preference under limited attention, with joint identification of preference and attention from standard choice data and a one-axiom test. Crucially, it shows model-free welfare analysis can mislead precisely when consideration is incomplete, and it explains classic context-dependent anomalies without invoking changing or context-dependent preferences. Policy payoff: it lets a firm/planner distinguish "not liked" from "not noticed."

## Limitations & open questions
- **Coarse/incomplete welfare:** under WARP-satisfying data, Theorems 1–2 identify *nothing*—behavior is equally consistent with full attention or with never considering anything but the chosen item. Choice data alone cannot then pin down preference.
- The authors propose three explicit routes to sharpen identification: (i) **additional non-choice data** (eye-tracking, fMRI, online tracking) to certify attention; (ii) **imposing more structure on the attention filter**; (iii) **combining with other methods** whose revealed preference contains $P_R$. Each is a concrete project hook.
- Determinism: $c$ is single-valued and deterministic; stochastic consideration/choice is outside the model.
- The attention-filter property can fail when the feasible set itself conveys information that shifts beliefs or costs (noted explicitly).

## Connections
The paper sits in the bounded-rationality revealed-preference program. It directly contrasts with Bernheim & Rangel (2007, 2009) model-free welfare and with [[@Samuelson1938|Samuelson (1938)]]/Varian (2006) classical revealed preference. Its consideration-set lineage runs through Simon (1957), Stigler (1961), Wright & Barbour (1977), and [[@Hauser1990|Hauser & Wernerfelt (1990)]]. Closest decision-theoretic rivals are [[@Manzini2007|Manzini & Mariotti (2007)]] "sequentially rationalizable choice" and their categorization work, Cherepanov, Feddersen & Sandroni (2010) "rationalization", [[@Salant2008|Salant & Rubinstein (2008)]] "choice with frames", and Lleras et al. (2010) "when more is less". Related limited-consideration and search models include Masatlioglu & Nakajima (2009) iterative search and [[@Caplin2011|Caplin & Dean (2011)]] / Caplin, Dean & Martin (2011) choice-process data; [[@Eliaz2011a|Eliaz & Spiegler (2011)]] and [[@Eliaz2011|Eliaz, Richter & Rubinstein (2011)]] study consideration-set manipulation and observable finalists. The attraction effect draws on [[@Huber1982|Huber, Payne & Puto (1982)]], [[@Tversky1993|Tversky & Simonson (1993)]], and [[@Lehmann1994|Lehmann & Pan (1994)]]; cyclical choice on [[@May1954|May (1954)]] and Tversky (1969). Rational inattention (Sims 2003) is a complementary information-theoretic cousin.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
