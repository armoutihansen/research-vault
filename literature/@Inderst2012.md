---
citekey: Inderst2012
title: Competition through Commissions and Kickbacks
authors: ["Inderst, Roman", "Ottaviani, Marco"]
year: 2012
type: journalArticle
doi: 10.1257/aer.102.2.780
zotero: "zotero://select/library/items/FLDTHBWC"
pdf: /Users/jesper/Zotero/storage/XQ3BIWYY/Inderst2012.pdf
tags: [literature]
keywords: [commissions, kickbacks, information-intermediation, disclosure-regulation, suitability-advice, hotelling-competition, cheap-talk]
topics: ["[[advice-misselling-disclosure]]"]
related: [Biglaiser1993, Inderst2009]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In markets for retail financial products and health services, consumers often rely on the advice of intermediaries to decide which specialized offering best fits their needs. Product providers, in turn, compete to influence the intermediaries' advice through hidden kickbacks or disclosed commissions. Motivated by the controversial role of these widespread practices, we formulate a model to analyze competition through commissions from a positive and normative standpoint. The model highlights the role of commissions in making the advisor responsive to supply-side incentives. We characterize situations when commonly adopted policies such as mandatory disclosure and caps on commissions have unintended welfare consequences. (JEL D21, D82, D83, G21, L15, L25)

## Summary

Two firms selling horizontally differentiated products compete not for customers directly but for the favorable recommendation of a single privately informed advisor, whom they pay through per-sale commissions (kickbacks if hidden, commissions if disclosed). The paper shows that commission-steering is formally isomorphic to Hotelling price competition, with the advisor's concern for suitability $w$ playing the role of the unit transport cost. The central message is normative and contrarian: commonly mandated remedies (commission disclosure, caps, and penalties for unsuitable sales) can lower allocative efficiency, because their effects on the two firms' incentives to steer are asymmetric and interact with how strongly the advisor cares about suitability.

## Research question

What is the allocative (positive) and welfare (normative) role of commissions and kickbacks when product providers compete by paying an information intermediary to steer a customer's purchase? Specifically, how do mandatory disclosure of commissions, caps on commissions, and penalties for unsuitable sales affect the quality of advice and social welfare?

## Method / identification

A four-stage game-theoretic model solved for perfect Bayesian equilibrium (pure strategies, informative advice, passive beliefs à la Hart–Tirole). Two firms $n=A,B$ produce at costs $c_n$ with $c_B\ge c_A$ (firm $A$ weakly more cost-efficient). A binary state $\theta=A,B$ determines which product matches the customer; the customer gets $v_h$ on a match and $v_l<v_h$ otherwise (utility $0$ from not buying). An advisor privately observes a posterior $q=\Pr(\theta=A)$ drawn from a continuous $G(q)$ that is symmetric about $1/2$ and satisfies an increasing hazard rate $\frac{d}{dq}\frac{g(q)}{1-G(q)}\ge 0$ (which, with symmetry, also makes the reverse hazard rate $\frac{g(q)}{G(q)}$ decreasing). The advisor has a "concern for suitability" $w=w_h-w_l>0$: utility $w_h$ if the suitable product is bought, $w_l$ otherwise, with $w_0<w_l<w_h$ ruling out a no-purchase recommendation in the baseline.

Timing: ($t=1$) firms simultaneously set commissions $f_n$ paid only on a sale; ($t=2$) firms set prices $p_n$; ($t=3$) the advisor sends message $m\in\{A,B\}$; ($t=4$) the customer buys. The advisor recommends $A$ iff $q>q^*$ with cutoff
$$q^*=\frac{1}{2}-\frac{f_A-f_B}{2w},$$
which mirrors the marginal-customer condition $q=\tfrac12-(p_B-p_A)/[2(v_h-v_l)]$ in a Hotelling model where the customer privately observes $q$ — so $w$ is the analog of transport cost and $1/(2w)$ measures the advisor's responsiveness to commissions. Firms set prices to extract the conditional valuations $P_A(q)=E[v_A(q)\mid q>q^*]$ and $P_B(q)=E[v_B(q)\mid q<q^*]$. Two disclosure regimes are compared: hidden commissions (baseline) versus disclosed commissions. The advisor's suitability concern $w$ is given three microfoundations, analyzed separately: a regulatory/professional penalty for unsuitable sales (Section V); reputational/franchise loss in a dynamic model (Section VI); and an intrinsic professional weight $\gamma$ on the customer's welfare, $w=\gamma(v_h-v_l)$ (Section VII). An extension (Section VIII) endogenizes the advisor's information quality.

## Data

None — this is a pure theory paper. Institutional motivation is drawn from documented practices in pharmaceutical detailing, insurance brokerage, mortgage origination, and the UK FSA commission ban; no estimation is performed.

## Key findings

- **Proposition 1 (baseline / hidden kickbacks).** A unique equilibrium exists. Commissions are strategic complements; lower suitability concern $w$ raises both firms' commissions. With symmetric costs $c_A=c_B$, advice is balanced ($q^{ND}=1/2$) for every $w$. With $c_A<c_B$, the cost-efficient firm $A$ has a larger market share ($q^{ND}<1/2$), increasing as $w$ falls. The equilibrium cutoff solves $[E[v_A(q)\mid q>q^{ND}]-c_A]-[E[v_B(q)\mid q<q^{ND}]-c_B]=w(1-2q^{ND})+2\frac{1-2G(q^{ND})}{g(q^{ND})}$.
- **Proposition 2 (disclosure).** A unique equilibrium exists with the same comparative statics, but disclosure unambiguously lowers commissions (strictly when positive without disclosure). Best responses now use marginal valuations $v_A(q^*),v_B(q^*)$ instead of conditional valuations: raising a disclosed commission forces a one-for-one price cut, "chilling" commissions — amplified because commissions are strategic complements.
- **Proposition 3 (disclosure and advice).** Disclosure leaves advice unchanged under symmetry ($q^D=q^{ND}=1/2$). Under asymmetry it chills the cost-efficient firm $A$ more (key inequality (14): $E[v_A(q)\mid q>q^*]-v_A(q^*)>E[v_B(q)\mid q<q^*]-v_B(q^*)$ for $q^*<1/2$), so $A$'s market share falls.
- **Proposition 4 + Corollary 1 (welfare).** First best is $q^{FB}=\tfrac12-\frac{c_B-c_A}{2(v_h-v_l)}$. Symmetric advice is always efficient. Under asymmetry: with disclosure $A$'s share is always inefficiently too low ($q^D>q^{FB}$, and setting $w=0$ restores $q^D=q^{FB}$); without disclosure there is a threshold $w^{FB}$ where advice is efficient, $A$ over-sells for $w<w^{FB}$ and under-sells for $w>w^{FB}$. Hence disclosure *raises* welfare when $w$ is small but *reduces* it when $w$ exceeds a threshold $w^D<w^{FB}$.
- **Policy.** Higher penalties and binding caps push asymmetric outcomes toward symmetry; both can reduce efficiency. With full disclosure, imposing penalties is counterproductive — disclosure alone makes firms internalize the price feedback.
- **Information acquisition (Section VIII).** Without disclosure, a more informed advisor extracts more of the surplus through higher commissions; disclosure stifles the advisor's incentive to invest in information.

## Contribution

Provides the first equilibrium model in which the *information content* of advice is endogenous to competing firms' commissions, embedding an information intermediary into Hotelling (1929) price competition. Unlike cheap-talk models the advisor's bias is endogenized by the commissions, so disclosure feeds back into firms' commission-setting. It delivers a clean normative result that the standard pro-transparency intuition is conditional: disclosure, caps, and penalties have ambiguous and potentially perverse welfare effects depending on the advisor's suitability concern, with direct relevance to financial-advice and health-care regulation (MiFID, FINRA suitability rules, the UK FSA commission ban).

## Limitations & open questions

The authors explicitly flag several open problems, each a project hook: (i) the disclosure-restores-efficiency result hinges on customers rationally inferring advice quality from commissions and on disclosure being a perfect commitment device — soft/"in-kind" commissions undermine this; (ii) behavioral frictions (information overload from disclosed commissions; disclosure morally licensing biased advice, citing Cain, Loewenstein & Moore) are noted but not modeled; (iii) the single-advisor assumption could be replaced by *tied* product-specific advisors, forcing customers to search and turning recommendations into private information; (iv) endogenizing product characteristics (cost/quality investment), which only pay off with sufficient market access; (v) relational/unconditional gifts under repeated firm–advisor interaction are left to future work; (vi) commissions' effect on the agent's incentive to *acquire customers* under common-agency free-riding.

## Connections

Builds directly on Hotelling (1929) price competition and relates the advisor's cutoff to the privately-informed-customer variant of Moscarini & Ottaviani (2001). It connects to seller-incentive-to-provide-information work — Lewis & Sappington (1994), Johnson & Myatt (2006), Ganuza & Penalva (2010), Bar-Isaac, Caruana & Cuñat (2010) — but routes information through an intermediary, contrasting with the vertical-quality intermediaries of [[@Biglaiser1993|Biglaiser (1993)]] and certification of Lizzeri (1999). It departs from common-agency models following Bernheim & Whinston (1986) by adding a privately informed advisor who communicates with a customer. On strategic communication it endogenizes the sender's bias relative to Crawford & Sobel (1982), Morgan & Stocken (2003), and Li & Madarász (2008), and contrasts with Durbin & Iyer (2009) and Li (2010). It departs from the credence-goods/advice setup of Bolton, Freixas & Shapiro (2007) and from the authors' own seller-compensation analysis in [[@Inderst2009|Inderst & Ottaviani (2009)]]. Early antecedents on kickbacks include Owen (1977) and Pauly (1979); behavioral evidence on disclosure draws on Cain, Loewenstein & Moore (2005) and Lacko & Pappalardo (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
