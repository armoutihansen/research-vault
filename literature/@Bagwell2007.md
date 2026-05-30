---
citekey: Bagwell2007
title: Chapter 28 The Economic Analysis of Advertising
authors: ["Bagwell, Kyle", "Armstrong, M.", "Porter, R."]
year: 2007
type: bookSection
doi: 10.1016/S1573-448X(06)03028-7
zotero: "zotero://select/library/items/K8W7H23P"
pdf: /Users/jesper/Zotero/storage/N3SGUX3I/Bagwell2007.pdf
tags: [literature]
keywords: [advertising, industrial-organization, persuasive-vs-informative, dorfman-steiner, quality-signaling, endogenous-sunk-costs, market-structure]
topics: []
related: [Milgrom1986, Nelson1974]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This chapter offers a comprehensive survey of the economic analysis of advertising. A first objective is to organize the literature in a manner that clarifies what is known. A second objective is to clarify how this knowledge has been obtained. The chapter begins with a discussion of the key initial writings that are associated with the persuasive, informative and complementary views of advertising. Next, work that characterizes empirical regularities between advertising and other variables is considered. Much of this work is conducted at the inter-industry level but important industry studies are also discussed. The chapter then offers several sections that summarize formal economic theories of advertising. In particular, respective sections are devoted to positive and normative theories of monopoly advertising, theories of price and non-price advertising, theories of advertising and product quality, and theories that explore the potential role for advertising in deterring entry. At this point, the chapter considers the empirical support for the formal economic theories of advertising. A summary is provided of empirical work that evaluates the predictions of recent theories of advertising, including work that specifies and estimates explicitly structural models of firm and consumer conduct. This work is characterized by the use of industry (or brand) and even household-level data. The chapter then considers work on endogenous and exogenous sunk cost industries. At a methodological level, this work is integrative in nature: it develops new theory that delivers a few robust predictions, and it then explores the empirical relevance of these predictions at both inter-industry and industry levels. Finally, the chapter considers new directions and other topics. Here, recent work on advertising and media markets is discussed, and research on behavioral economics and neuroeconomics is also featured. A final section offers some concluding thoughts.

## Summary
Bagwell's *Handbook of Industrial Organization* chapter is the definitive 130-page survey of how economists model and measure advertising. It organizes a century of work around the foundational question — *why do consumers respond to advertising?* — and the three answers economists have given: the **persuasive**, **informative**, and **complementary** views. Each view carries sharply different positive and (especially) normative implications, and the survey traces the field through alternating empirical, theoretical, and re-empirical phases, showing how each new IO method (regression, game theory, NEIO structural estimation, Sutton-style bounds) was first sharpened against advertising. The recurring lesson: no single view is valid everywhere, advertising is endogenous (so naive correlations mislead), and the welfare verdict depends on the *purpose* of advertising and the extent of *scale economies*.

## Research question
What is known about the economics of advertising, and how was that knowledge obtained? Concretely: Why do consumers respond to ads? What are the equilibrium relationships between advertising and concentration, profit, entry, price, and quality? Does advertising deter entry? Does the market supply too much or too little advertising? Bagwell treats advertising as a "case study" for charting methodological progress in industrial organization.

## Method / identification
This is a survey, but its analytical spine is a set of formal models presented with full derivations.

**Positive monopoly theory — the Dorfman-Steiner (1954) model.** A monopolist chooses price $P$ and advertising $A$ with constant per-ad cost $\kappa$, demand $D(P,A)$ ($D_P<0<D_A$), and profit $\Pi(P,A)\equiv PD(P,A)-C(D(P,A))-\kappa A$. The first-order conditions yield the Lerner markup $\frac{P-C'}{P}=\frac{1}{\varepsilon_P}$ and the celebrated **inverse-elasticity advertising rule**: the advertising-to-sales ratio equals the ratio of advertising to price elasticities,
$$\frac{\kappa A}{PD}=\frac{\varepsilon_A}{\varepsilon_P}.$$
Two parametric examples nest the views: a vertical-differentiation utility $\theta g(A)-P$ (persuasive: $\frac{d\varepsilon_P}{dA}<0$, ads make demand more inelastic) and a Butters (1977) reach example $D=N[1-e^{-A/N}]d(P)$ (informative: no elasticity effect). In both, $\operatorname{sign}\{P_M'(A)\}$ is governed by elasticity versus scale effects.

**Normative theory** uses the same framework: Braithwaite's consumption-distortion argument (consumer surplus gain $G$ from a lower price versus loss $L$ from distorted purchases at pre-advertising preferences) and Dixit-Norman (1978), who compare market and socially-optimal advertising and argue advertising may be *excessively* supplied.

**Quality-signalling models.** A monopolist privately knows quality $t\in\{L,H\}$, picks $(P,A)$, and consumers form belief $b(P,A)$. The **least-cost separating equilibrium** solves $\max_{P,A}\Pi(P,A,1,H)$ s.t. $\Pi(P,A,1,L)\le\pi_M(L)$. The [[@Milgrom1986|Milgrom-Roberts (1986)]] two-period extension adds a repeat-business effect: dissipative advertising signals quality only if marginal cost rises with quality ($c(H)>c(L)$). The survey also covers Bagwell-Ramey dissipative/multi-firm price models, loss-leader commitment/signalling models, Sutton's sunk-cost multi-stage entry games, and NEIO structural estimation (specify demand, marginal-cost, and supply first-order/conduct equations; estimate jointly via SCPP-vs-NEIO contrast).

## Data
None of its own — this is a survey. It catalogs others' data: inter-industry advertising/sales ratios (Bain, Telser, Comanor-Wilson); brand panels (Lambin's 107 brands, 16 classes, 8 countries); household scanner panels (Section 8.1); and industry structural studies on cigarettes (Roberts-Samuelson), cola (Gasmi-Laffont-Vuong), photographic film (Kadiyali), and saltine crackers (Slade).

## Key findings
- **Dorfman-Steiner inverse-elasticity rule** $\kappa A/PD=\varepsilon_A/\varepsilon_P$ is the canonical optimal-advertising condition and exposes the *endogeneity* of any advertising-profit correlation.
- **Chamberlin's verdict** (formalized): the price effect of advertising is theoretically ambiguous, decomposing into elasticity, cost, and scale effects; "the effect... depends upon the facts of the case."
- **Quality signalling**: dissipative ("burning money") advertising can signal high quality, but in the dynamic Milgrom-Roberts model *only when* $c(H)>c(L)$; otherwise high-quality firms signal with low price and zero advertising. Empirics offer only weak support for a systematic advertising-quality link.
- **Sutton's non-convergence theorem**: in *endogenous* sunk cost industries (advertising raises willingness-to-pay via fixed outlays), market structure does not fragment as market size $S\to\infty$. The maximal market share is bounded below: $\bar m\ge \frac{\alpha}{1+K}\equiv B$. By contrast, in *exogenous* sunk cost industries, the concentration lower bound $\to 0$ as $S$ grows.
- **Empirical regularity**: no single view of advertising holds across all markets; defensible patterns emerge only within narrow industry categories.

## Contribution
The first (and still standard) comprehensive, unified survey of the economic analysis of advertising — integrating the persuasive/informative/complementary trichotomy with a common formal monopoly framework, the modern game-theoretic theories (signalling, entry deterrence, dissipative advertising), the NEIO structural empirical program, and Sutton's bounds approach. It supplies the conceptual vocabulary and benchmark models that subsequent advertising research builds on.

## Limitations & open questions
Bagwell explicitly flags that "many of the most important questions remain unresolved":
- **Does advertising reinforce consumer experience and insulate pioneering firms from entry?** — a long-standing question household-panel work is only beginning to answer.
- **Does the market provide too much advertising?** No general theoretical answer; under multiple firms, *business-stealing* can make advertising excessive while uninternalized consumer surplus can make it inadequate.
- **Multi-product retailer advertising** of prices (loss leaders) is under-theorized given that retailers carry thousands of items.
- **Media markets** (two-sided): endogenous determination of the *price of advertising* and its welfare consequences is newly opened.
- **Behavioral / neuroeconomics**: two-system (deliberative/affective, "cold/hot") models of choice (Loewenstein-O'Donoghue, Bernheim-Rangel) and fMRI evidence (McClure et al. Coke/Pepsi) raise the question of *which preferences* should anchor welfare when ads activate affective systems — reopening the persuasive-view welfare debate on new foundations.

## Connections
The persuasive view descends from **Marshall (1890)**, **Chamberlin (1933)**, **Robinson (1933)**, **Braithwaite (1928)**, and **Kaldor (1950)**; the informative view from the Chicago School — **Stigler (1961)**, **Telser (1964)**, **[[@Nelson1974|Nelson (1974)]]** (search vs experience goods, signalling-efficiency); the complementary view from **Becker-Murphy (1993)**. Formal modeling rests on **Dorfman-Steiner (1954)** and **Dixit-Norman (1978)**; signalling on **Milgrom-Roberts (1986)**, **Kihlstrom-Riordan (1984)**, and **Schmalensee (1978)**; reach/dissipation on **Butters (1977)** and **Grossman-Shapiro (1984)**; the integrative bounds program on **Sutton (1991)** *Sunk Costs and Market Structure* and **Bresnahan (1989)** on NEIO. It sits alongside the earlier *Handbook* treatments by Schmalensee (1989) and Stiglitz (1989) and complements the Farrell-Klemperer chapter on switching costs and network effects.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
