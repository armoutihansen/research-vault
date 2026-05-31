---
citekey: Eliaz2011a
title: Consideration Sets and Competitive Marketing
authors: ["Eliaz, Kfir", "Spiegler, Ran"]
year: 2011
type: journalArticle
doi: 10.1093/restud/rdq016
zotero: "zotero://select/library/items/LPKR7GWA"
pdf: /Users/jesper/Zotero/storage/N675FXCF/Eliaz2011.pdf
tags: [literature]
keywords: [consideration-sets, bounded-rationality, competitive-advertising, limited-attention, vertical-differentiation, revealed-preference]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Bagwell2007, Manzini2007]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We study a market model in which competing firms use costly marketing devices to influence the set of alternatives which consumers perceive as relevant. Consumers in our model are boundedly rational in the sense that they have an imperfect perception of what is relevant to their decision problem. They apply well-defined preferences to a "consideration set", which is a function of the marketing devices employed by the firms. We examine the implications of this behavioural model in the context of a competitive market model, particularly on industry profits, vertical product differentiation, the use of marketing devices, and consumers' conversion rates.

## Summary

Eliaz and Spiegler embed a consideration-set model of bounded rationality into a competitive duopoly. Consumers have stable preferences but an imperfect perception of which alternatives are relevant; firms spend on costly marketing devices (primarily advertising messages) to manipulate which products enter a consumer's consideration set. The headline result is that, despite consumers' exploitable irrationality, competition (including marketing competition) drives firms back down to the rational-consumer profit benchmark, while consumers are left strictly worse off. The framework jointly pins down vertical product differentiation, marketing intensity, and consumer conversion/switching rates, and extends to positioning, packaging, advertising intensity, and "attention-grabber" products.

## Research question

Does consumers' bounded rationality (their resistance to considering new products) let firms earn profits above the rational-consumer benchmark, or does marketing competition compete that rent away? Related: what is the link between a firm's marketing strategy and its product-quality choice; do profits necessarily fall as consumers become "more rational"; and what determines the equilibrium fraction of consumers who switch supplier (and the conversion rate conditional on having considered a new product)?

## Method / identification

Pure theory. Consumer choice is a two-stage procedure over ordered pairs of extended products $((x^s,M^s),(x^n,M^n))$ where $x\in X$ is a product and $M\in\mathcal{M}$ a marketing strategy. Primitives are a linear order $\succ$ on $X$ ("true" quality preferences, impervious to marketing) and a consideration function $\varphi(x^s,M^n)\in\{0,1\}$. Stage 1: the consideration set is $\{x^s,x^n\}$ if $\varphi(x^s,M^n)=1$, else $\{x^s\}$ (the default/status quo alone). Stage 2: the consumer picks the $\succ$-maximal product in the consideration set. This induces a "beating" relation $\succ^*$ — $(y,N)\succ^*(x,M)$ iff $\varphi(x,N)=1$ and $y\succ x$ — which can be intransitive and incomplete, yielding a distinctive status-quo bias located in the perception stage rather than in preferences.

The market is a symmetric simultaneous-move game between two firms facing a continuum of identical consumers. Each consumer is randomly assigned a default firm; the rival is the contender. A strategy is $(x,M)\in A\subseteq X\times\mathcal{M}$ with fixed cost $c(x,M)=c_x+\sum_{m\in M}c_m$, all costs positive, $c(x,M)<\tfrac{1}{2}$, and $x\succ y\Rightarrow c_x\ge c_y$. Firms maximize market share minus cost. Marketing strategies are subsets of a finite message set $D$, i.e. $\mathcal{M}=2^D$. Two structural assumptions: (P1) separability — $\varphi(x,M)=1$ iff some single $m\in M$ is effective against $x$; and (P2) for every $x\ne x^*$ some message is effective, so a firm using the grand set $D$ guarantees consideration. The model is analyzed as a generalized all-pay auction with limited comparability of bids. Section 4 extends $\varphi$ to depend on the full profile $\varphi(x^s,M^s,x^n,M^n)$; Section 5 gives a revealed-preference axiomatization.

## Data

None — this is a theoretical paper. The authors cite empirical marketing work (e.g. Hoyer 1984 on detergent purchases; Shum 2004 on uninformative advertising) to motivate the two-stage consideration process, but conduct no estimation.

## Key findings

- **Proposition 2 (existence):** As long as costs are not too high, there exists a symmetric Nash equilibrium in which firms earn the rational-consumer (max–min) pay-off $\tfrac{1}{2}-c_{x^*}$. Equilibrium is mixed; only $x^*$ is advertised; vertical differentiation is extreme (only $x^*$ and the worst product $x_*$ offered in the simplest case). The outcome is Pareto-inferior to the rational benchmark: firms earn the same profit but consumers are strictly worse off.
- **Lemmas 1–2:** In any symmetric equilibrium $\beta_\sigma(x^*)\in(0,1)$ and active marketing ($M\ne\emptyset$) occurs with positive probability.
- **Proposition 3 (marketing efficiency):** Messages used together target disjoint sets of offered products — firms use a minimal set of messages.
- **Proposition 4 (partitional characterization):** When $\{X_\varphi(m)\}_{m\in D}$ partitions $X\setminus\{x^*\}$, *every* symmetric equilibrium yields rational-consumer pay-offs, with closed forms $\alpha_\sigma(m)=2(c_{x^*}-c_{y^*(m)})$ and $\beta_\sigma(y^*(m))$, where $y^*(m)$ is the $\succ$-minimal product in the cell. Costlier messages raise the offer probability of their inferior target; costlier $x^*$ raises its advertising intensity.
- **Proposition 5 (effective marketing / 100% conversion):** Any equilibrium with rational-consumer pay-offs satisfies the effective marketing property — whenever marketing persuades a consumer to consider a new product, he buys it. Overall switching rate $=4\sum_{m\in D}c_m(c_{x^*}-c_{y^*(m)})$, increasing in advertising costs and quality-cost gaps.
- **Targeting:** Finer partitions (more targeted advertising) shift the equilibrium quality distribution upward.
- **Comparative statics on rationality (non-monotonicity):** Adding a small group of rational consumers *raises* firms' profits; making the consideration function "more rational" can create new equilibria with higher, collusive profits. So industry profit is not monotonically decreasing in consumer rationality.
- **Extended model (Section 4):** With $\varphi(x^s,M^s,x^n,M^n)=1$ iff $M^n\ge M^s$ (advertising intensity), Proposition 7 again gives rational-consumer pay-offs, advertising serves a *defensive* role (high intensity need not signal high quality), but the effective marketing property can fail. A second application uses payoff-irrelevant "attention-grabber" products and positioning.
- **Choice theory (Section 5):** The beating relation is characterized by irreflexivity, quasi-completeness (QC), and quasi-transitivity (QT) (Remark 1). The procedure is a special case of Masatlioglu–Nakajima "Choice by Iterative Search".

## Contribution

Introduces a tractable framework for the "persuading to consider" role of marketing — distinct from informative and persuasive (preference-shifting) advertising — and shows it generates rich, empirically suggestive predictions about the joint determination of quality differentiation, marketing, and conversion. It reframes advertising as manipulation of the perceived feasible set rather than of beliefs or tastes, and delivers the sharp competitive-erosion result that exploitable bounded rationality need not yield supra-competitive profits.

## Limitations & open questions

The authors flag explicitly: (1) **No prices** — the value of a customer is held fixed; incorporating price competition is deferred (motivated by media/non-profit markets where this fits). (2) **Exogenous default assignment** — the probability a firm is a consumer's default is independent of its marketing, abstracting from marketing's role in winning initial attention and in industry-wide awareness; endogenizing this is left for future work. (3) **Consumer homogeneity** — the 100% conversion result is an extreme benchmark that relies on homogeneity; the authors call for richer theories with heterogeneous consumers and preferences. (4) Several richer extended-model applications (packaging/knock-offs, attention grabbers) are developed only in companion papers.

## Connections

The choice procedure generalizes the status-quo-bias model of Masatlioglu & Ok (2005), differing in that the bias sits in the consideration stage rather than as a switching cost; it is a special case of the Choice by Iterative Search procedure of Masatlioglu & Nakajima (2008), and relates to consideration-set identification in Masatlioglu, Nakajima & Ozbay (2009). The intransitive/incomplete revealed preferences connect to boundedly rational choice models such as [[@Manzini2007|Manzini & Mariotti (2007)]]. On the industrial-organization side it builds on the advertising-as-information tradition of Butters (1977) and the survey by [[@Bagwell2007|Bagwell (2007)]], and contrasts with signalling views where advertising intensity signals quality (Ackerberg 2003); the defensive-advertising mechanism parallels Chioveanu (forthcoming) and Varian-style loyalty/persuasive-advertising models. The marketing-science consideration-set literature (Alba, Hutchinson & Lynch 1991; Roberts & Lattin 1997) and supporting evidence (Hoyer 1984; Shum 2004) motivate the two-stage structure. Companion analyses appear in Eliaz & Spiegler (forthcoming) and Piccione & Spiegler (2009).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
