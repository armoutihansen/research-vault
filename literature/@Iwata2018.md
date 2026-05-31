---
citekey: Iwata2018
title: Salience and limited attention
authors: ["Iwata, Yukinori"]
year: 2018
type: journalArticle
doi: 10.1007/s00355-017-1077-1
zotero: "zotero://select/library/items/47PCPJKY"
pdf: /Users/jesper/Zotero/storage/NG62RQF9/Iwata2018.pdf
tags: [literature]
keywords: [limited-attention, salience, revealed-preference, consideration-sets, bounded-rationality, choice-theory]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Bordalo2013, Cherepanov2013, Huber1982, Lleras2017, Loomes1991, Mandler2012, Manzini2007, Manzini2014, Masatlioglu2012, Ok2015, Rubinstein2012, Salant2008, deClippel2012]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In this study, we investigate how the salience of alternatives influences the attention of a decision maker in a natural extension of the model of choice with limited attention by Masatlioglu et al. (Am Econ Rev 102(5):2183–2205, 2012). We propose positive salience effects on the attention of a decision maker. For example, when an alternative to which a consumer pays attention becomes more salient in terms of the extent of product advertisement, she will still pay attention to it in a market. We manipulate the salience of alternatives to find choice reversals from observable choice data, which play an important role in our analysis. The advantages of our model over the Masatlioglu et al. (Am Econ Rev 102(5):2183–2205, 2012) model are that it broadens the application of the model of choice with limited attention, and improves the power of inferring the decision maker's preference and the alternatives to which she pays attention and does not pay attention.

## Summary
Iwata extends the [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay]] (2012; "MNO") model of choice with limited attention by attaching to each alternative a vector of objectively measurable, preference-irrelevant attributes whose values represent *salience* (e.g. advertising, shelf position, tax-inclusive vs. tax-exclusive pricing). The decision maker (DM) still chooses her most-preferred alternative from a consideration set, but that consideration set now responds to manipulations of salience rather than only to changes in feasibility (the menu). Because the analyst can now generate choice reversals by lowering salience as well as by deleting alternatives, the revealed-preference content of the data strictly expands: the resulting model — choice with salience-affected limited attention (CSLA) — nests MNO and can sometimes elicit the DM's preference *completely* where MNO leaves it incomplete.

## Research question
When and how can an analyst deduce both a boundedly rational DM's underlying preference *and* the alternatives to which she does (and does not) pay attention, from observable choice data — when the analyst can manipulate not only feasibility but also the salience of alternatives? And what single behavioral axiom characterizes choice data consistent with such a model?

## Method / identification
The primitive is a finite set $X=\{x_1,\dots,x_m\}$. Each alternative $x_j$ carries a $q\times 1$ salience vector $A_j$ of real numbers; attribute $1$ encodes feasibility ($I_1=\{0,1\}$, with $a_{1j}=1$ meaning available). A *profile* $A$ is the $q\times m$ matrix of these vectors, and $F(A)=\{x_j: a_{1j}=1\}$ is the induced menu. Writing $A\setminus a'_{ij}$ for the profile that replaces $a_{ij}$ with $a'_{ij}$, the analyst's observable data are pairs (profile, choice).

A consideration-set mapping $\Gamma:\mathcal{A}\to\mathcal{X}$ assigns a nonempty subset of $F(A)$ to each profile. The central restriction is the **salience-affected attention filter** (Definition 1): for any $A$, any attribute $i$, any $x_j$, and any $a'_{ij}\le a_{ij}$, if $x_j\notin\Gamma(A)$ then $\Gamma(A)=\Gamma(A\setminus a'_{ij})$ — lowering the salience of an *un*-attended alternative leaves the consideration set unchanged. This is equivalent to **positive salience effects**: if $x_j\in\Gamma(A\setminus a'_{ij})$ then $x_j\in\Gamma(A)$ (raising salience of an attended alternative keeps it attended). It generalizes the MNO attention filter, which is the special case $q=1$.

A **choice with salience-affected limited attention (CSLA)** is an extended choice function $c:\mathcal{A}\to X$ for which there exist a strict preference $\succ$ (complete, transitive, asymmetric) and a salience-affected attention filter $\Gamma$ with $c(A)=\max_\succ\Gamma(A)$ (Definition 2).

Identification mirrors MNO's revealed-reversal logic. Define $x_j\,P\,x_k$ if some salience decrease of $x_k$ ($a'_{ik}\le a_{ik}$) reverses the choice away from $x_j$: $c(A)=x_j\ne c(A\setminus a'_{ik})$. Because reversals occur only when the consideration set changes — which, under the filter, requires the manipulated alternative to be attended — a reversal reveals both that $x_k$ was attended and that $x_j\succ x_k$. Revealed preference $P_R$ is the transitive closure of $P$.

## Data
None — this is a pure axiomatic / revealed-preference paper. The "data" are abstract observable (profile, choice) pairs. The salience-manipulation logic is illustrated through worked examples (grocery tax-inclusive vs. tax-exclusive pricing, online search top-page links, department-store packaging "showiness," occupational gender stereotypes) rather than empirical datasets.

## Key findings
- **Theorem 1 (revealed preference):** $x_j$ is revealed preferred to $x_k$ if and only if $x_j\,P_R\,x_k$. The transitive closure of the reversal relation captures *all* revealed preference in the CSLA model.
- **Theorem 2 (revealed (in)attention):** $x_j$ is revealed *not* to attract attention at $A$ iff $x_j\,P_R\,c(A)$; and $x_j$ is revealed to attract attention at $A$ iff there exists a profile $B$ exhibiting a salience-induced reversal of $x_j$, with side conditions (b)–(c) ensuring $\Gamma(A)=\Gamma(C)=\Gamma(B)$ for $F(C)=F(A)\cap F(B)$, generalizing MNO's indirect attention-inference method to multiple attributes.
- **Theorem 3 (characterization):** $c$ is a CSLA if and only if it satisfies **WARP with salience-affected limited attention** (WARP(SLA)) — a generalization of MNO's weakening of Samuelson's WARP that allows the "witness" reversal to be triggered by a salience decrease, not only by removing the alternative.
- **Lemma 1:** $P$ is acyclic iff $c$ satisfies WARP(SLA), giving a tractable consistency test.
- Because MNO is the $q=1$ restriction, $P_R$ always *contains* the MNO revealed preference; Examples 5–7 reproduce MNO's attraction-effect, cyclical-choice, and choosing-pairwisely-unchosen anomalies and show CSLA recovers rankings MNO cannot (e.g. pinning down $x_1$ via an extra salience manipulation).

## Contribution
CSLA broadens the empirical reach of limited-attention models — many naturally occurring "frames" (advertising intensity, tax-inclusive pricing, search-result placement, gendered job wording) become analyzable manipulations even when the menu is held fixed — and strictly increases the model's identifying power, addressing the "Type 3 failure" (incomplete revealed preference under bounded rationality) that [[@Manzini2014|Manzini & Mariotti (2014)]] flag in MNO. For welfare and "nudge"-style policy, richer preference elicitation yields finer welfare judgments and tells a policymaker *which* external factors move attention without restricting choice sets.

## Limitations & open questions
The author lists explicit open problems: (i) salience values $a_{ij}$ are treated as *absolute*, so the manipulation $A\setminus a'_{ij}$ is incoherent for *relative* attributes such as market share; modeling relative salience is open. (ii) The maintained assumption that all attributes are preference-*irrelevant* may fail — advertisements or peer evaluations could shift both attention *and* preference; disentangling salience effects that operate on preference is left for future work. (iii) Like MNO, the analysis assumes a *full-domain* extended choice function; de Clippel & Rozen (2014) warn that with limited available choice data revealed preferences may not extend, and this concern is *more* severe under CSLA because gathering all profile-choice pairs is harder than gathering all menu-choice pairs.

## Connections
The paper is a direct generalization of [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] "Revealed Attention" and its companion Masatlioglu & Nakajima (2015) on completing incomplete revealed preference. It situates CSLA as a *salience-first, preference-second* two-stage procedure, contrasting with Tyson's (2015) preference-first/salience-second satisficing model, and relating to other two-stage and boundedly rational choice procedures: [[@Manzini2007|Manzini & Mariotti]] (2007, 2012), [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]], [[@Lleras2017|Lleras et al. (2017)]], and [[@Mandler2012|Mandler, Manzini & Mariotti (2012)]] "choosing by checklist." Salient framing connects to [[@Salant2008|Salant & Rubinstein (2008)]] "(A,f): Choice with Frames" and [[@Rubinstein2012|Rubinstein & Salant (2012)]] on eliciting welfare from behavioral data. The salience motivation draws on Chetty, Looney & Kroft (2009) on tax salience and [[@Bordalo2013|Bordalo, Gennaioli & Shleifer (2013)]] on salience and consumer choice. The reproduced anomalies link to the attraction-effect literature ([[@Huber1982|Huber, Payne & Puto 1982]]; de [[@deClippel2012|Clippel & Eliaz 2012]]; [[@Ok2015|Ok, Ortoleva & Riella 2015]] "Revealed (p)reference theory") and to intransitivity evidence (Tversky 1969; [[@Loomes1991|Loomes, Starmer & Sugden 1991]]). Welfare/policy framing references Thaler & Sunstein (2008) on libertarian paternalism, and methodological caveats invoke [[@Manzini2014|Manzini & Mariotti (2014)]] and de Clippel & Rozen (2014).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
