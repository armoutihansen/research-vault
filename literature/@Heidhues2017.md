---
citekey: Heidhues2017
title: "Naïveté-Based Discrimination*"
authors: ["Heidhues, Paul", "Kőszegi, Botond"]
year: 2017
type: journalArticle
doi: 10.1093/qje/qjw042
zotero: "zotero://select/library/items/VA3YPJXV"
pdf: /Users/jesper/Zotero/storage/T368CWNZ/Heidhues and Kőszegi2017.pdf
tags: [literature]
keywords: [naivete-based-discrimination, behavioral-industrial-organization, price-discrimination, present-bias, shrouded-prices, consumer-welfare]
topics: []
related: [Gabaix2006]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We initiate the study of naïveté-based discrimination, the practice of conditioning offers on external information about consumers' naïveté. Knowing that a consumer is naive increases a monopolistic or competitive firm's willingness to generate inefficiency to exploit the consumer's mistakes, so naïveté-based discrimination is not Pareto-improving, can be Pareto-damaging, and often lowers total welfare when classical preference-based discrimination does not. Moreover, the effect on total welfare depends on a hitherto unemphasized market feature: the extent to which the exploitation of naive consumers distorts trade with different types of consumers. If the distortion is homogeneous across naive and sophisticated consumers, then under an arguably weak and empirically testable condition, naïveté-based discrimination lowers total welfare. In contrast, if the distortion arises only for trades with sophisticated consumers, then perfect naïveté-based discrimination maximizes social welfare, although imperfect discrimination often lowers welfare. If the distortion arises only for trades with naive consumers, then naïveté-based discrimination has no effect on welfare. We identify applications for each of these cases. In our primary example, a credit market with present-biased borrowers, firms lend more than is socially optimal to increase the amount of interest naive borrowers unexpectedly pay, creating a homogeneous distortion. The condition for naïveté-based discrimination to lower welfare is then weaker than prudence.

## Summary
Heidhues and Kőszegi introduce *naïveté-based discrimination*: firms conditioning their offers on external information about how likely a consumer is to mispredict the fees or charges she will incur. Whereas classical preference-based discrimination can raise welfare and even be Pareto-improving, naïveté-based discrimination is *never* Pareto-improving, can be Pareto-damaging, and often lowers total welfare. The key novel insight is that the welfare effect hinges on *which side of the market the exploitation distorts*: a homogeneous distortion (e.g., credit), a sophisticated-side distortion (e.g., mobile-phone overage avoidance), or a naive-side distortion (e.g., useless add-ons). Because exploiting a naive consumer is more profitable when the firm is certain she is naive, better targeting raises firms' willingness to generate inefficiency.

## Research question
What are the welfare effects of firms acquiring and using information about *consumer naïveté* (rather than preferences) to design discriminatory offers? When does sharper information about who is naive lower total welfare, redistribute it, or leave it unchanged, and how does this differ from classical preference-based price discrimination?

## Method / identification
A reduced-form Hotelling pricing model with horizontally differentiated products in the tradition of [[@Gabaix2006|Gabaix & Laibson (2006)]]. Consumers have tastes $y\sim U[0,1]$, gross value $v$, and are independently naive with probability $\alpha$, sophisticated with $1-\alpha$. Two firms with marginal cost $c$ at locations $l\in\{0,1\}$ simultaneously choose an *anticipated price* $f_l$ (understood by all) and an *additional price* $a_l\in[\underline a,a_{max}]$ that naive consumers ignore at the purchase stage but still pay. Transport cost is $t\mid y-l\mid$ with $t>0$ governing market power; the outside option (following Bénabou & Tirole 2016) has utility $-t\min\{y,1-y\}$. The additional price carries a distortionary impact $k(a_l)$ with $k(\underline a)=k'(\underline a)=0$, $k''>0$, $k'(a_{max})\ge 1$. The paper distinguishes three cases by which trades $k$ falls on: (i) **homogeneous** (both types), (ii) **sophisticated-side** (only sophisticated trades, via costly avoidance), (iii) **naive-side** (only naive trades). It solves for symmetric pure-strategy Nash equilibria where firms correctly anticipate behavior. Discrimination sorts the single pool $\alpha_{ns}$ into a more-naive pool $\alpha_n>\alpha_{ns}$ and a more-sophisticated pool $\alpha_s<\alpha_{ns}$, with $\alpha_{ns}=\mu_n\alpha_n+\mu_s\alpha_s$; perfect discrimination is $\alpha_n=1,\alpha_s=0$. The framework is microfounded in three applications (credit, add-ons, car extras) and opened with a numerical monopoly bank-overdraft example contrasting the preference-based vs. naïveté-based interpretation of the *same* demand data.

## Data
None — this is a theory paper. Empirical evidence is invoked only to motivate assumptions (Stango & Zinman 2009 on avoidable fees; Grubb & Osborne 2015 and Ausubel 1991 on mispredicted usage/teaser rates; OFT 2008 on unexpected overdrafts) and to argue prudence is empirically supported (Parker & Preston 2005; Deck & Schlesinger 2014).

## Key findings
- **Equilibrium additional price.** Under homogeneous and sophisticated-side distortions the equilibrium satisfies the first-order condition $k'(a(\alpha))=\alpha$, so $a(\alpha)=(k')^{-1}(\alpha)$, and deadweight loss is $\mathrm{DWL}(\alpha)=k(a(\alpha))$ (homogeneous case).
- **Proposition 1 (homogeneous).** Naïveté-based discrimination strictly *lowers* welfare for all $\alpha_{ns},\alpha_n,\alpha_s$ iff $\mathrm{DWL}(\alpha)$ is strictly convex, equivalently iff $k'(a)/k''(a)$ is strictly increasing ("decreasing absolute convexity"); it strictly *raises* welfare iff $k'/k''$ is strictly decreasing. Intuition: raising the distortion in the naive pool costs more than the equal reduction in the sophisticated pool gains.
- **Proposition 2 (sophisticated-side).** Perfect discrimination *maximizes* social welfare (knowing a consumer is sophisticated, the firm imposes no additional price, hence no distortion; knowing she is naive, it exploits her without triggering inefficiency). Yet *imperfect* discrimination at low $\alpha$ can still lower welfare.
- **Proposition 3 (naive-side).** Discrimination has *no effect* on welfare; the firm charges the maximal additional price regardless of $\alpha$.
- **Corollary 1.** Discrimination is never Pareto-improving: under monopoly it either has no effect or strictly lowers naive consumers' welfare; under imperfect competition it strictly lowers the more-sophisticated pool's welfare (naive consumers cross-subsidize sophisticated ones via aggressive competition on the anticipated price).
- **Proposition 4 / Pareto-damage.** Under homogeneous distortions and imperfect competition, perfect discrimination leaves firm profits unchanged yet can make *both* types worse off — a Pareto-damaging outcome impossible under basic preference-based discrimination.
- **Proposition 5 (credit application).** If consumption utility $u(\cdot)$ satisfies *prudence* ($u'''(b)\ge 0$, the precautionary-savings condition), the induced $k(\cdot)$ exhibits decreasing absolute convexity, so naïveté-based discrimination strictly lowers welfare — and the actual threshold condition is weaker than prudence. Lenders overlend to extract unexpected interest; discrimination amplifies overlending to the naive pool.
- **Welfare independent of competition.** For the additional (hidden) price, total welfare distortion is invariant to market power $t$; competition only redistributes (via the anticipated price), so naïveté-based discrimination matters even under perfect competition. In the overdraft example, naive consumers can bear *over 100%* of the social welfare loss — a sharply adverse distributional effect given that financially mistaken consumers tend to be lower-income (Calvet, Campbell & Sodini 2007).

## Contribution
The paper opens a new research program by separating discrimination based on *naïveté* from the classical literature's focus on *preferences*, showing the two have qualitatively opposite welfare logics. It supplies a tractable reduced-form model nesting three economically distinct distortion structures, derives sharp necessary-and-sufficient conditions ($k'/k''$ monotonicity; prudence in the credit case) for welfare to fall or rise, and microfounds each case in a canonical behavioral-IO application. It thereby gives regulators a diagnostic: identify which trades the exploitation distorts and test the (empirically checkable) convexity condition.

## Limitations & open questions
The authors explicitly flag several open problems as project hooks:
- **Participation distortions.** The analysis ignores that consumers respond to the "wrong" perceived prices when deciding whether to buy at all; at the perfect-competition limit $t\to 0$ perceived price falls below marginal cost, generating possibly massive overparticipation (cf. Heidhues & Kőszegi 2015). Discrimination can mitigate or exacerbate this; if $v<c$ no one should be served, yet discrimination may let firms profitably serve the naive pool.
- **Multiple coexisting distortions.** Each market is assumed to feature only one of the three distortion types; in reality homogeneous, sophisticated-side, and naive-side distortions can coexist (e.g., insurance) and interact — only briefly treated in the Online Appendix.
- **Interaction with other discrimination.** How naïveté-based discrimination interacts with preference-based third-degree discrimination and with naïveté-based *screening* (second-degree) is unknown.
- **Endogenous information acquisition / direct empirical evidence** that firms actually engage in this practice remains limited.

## Connections
Builds directly on Heidhues & Kőszegi (2010) on exploitative credit contracts, and on the shrouded-attributes framework of [[@Gabaix2006|Gabaix & Laibson (2006)]]; the add-on application draws on Grubb (2015) and Grubb & Osborne (2015). Hyperbolic-discounting preferences follow Laibson (1997) and O'Donoghue & Rabin (1999), with earlier exploitation models in DellaVigna & Malmendier (2004) and Eliaz & Spiegler (2006, 2008) (the latter on belief-based screening). Prudence as a utility property traces to Leland (1968). The Hotelling outside-option formulation is from Bénabou & Tirole (2016). The screening-with-third-degree-discrimination point connects to Herweg & Müller (2014) and Bergemann, Brooks & Morris (2015). Empirical motivation cites Ausubel (1991), Shui & Ausubel (2004), Stango & Zinman (2009), Agarwal et al. (2008), and Calvet, Campbell & Sodini (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
