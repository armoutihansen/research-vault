---
citekey: Fehr2006a
title: "Chapter 8 The Economics of Fairness, Reciprocity and Altruism – Experimental Evidence and New Theories"
authors: ["Fehr, Ernst", "Schmidt, Klaus M."]
year: 2006
type: bookSection
doi: 10.1016/S1574-0714(06)01008-6
zotero: "zotero://select/library/items/25IKW42N"
pdf: /Users/jesper/Zotero/storage/94AADZY5/Fehr2006.pdf
tags: [literature]
keywords: [social-preferences, inequity-aversion, reciprocity, other-regarding-preferences, experimental-economics, psychological-game-theory]
topics: ["[[inequity-aversion-distributional-preferences]]"]
related: [Andreoni2002, Bolton2000, Charness2002, Dufwenberg2004, Falk2006, Fehr1999, Levine1998, Manzini2007, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Most economic models are based on the self-interest hypothesis that assumes that material self-interest exclusively motivates all people. Experimental economists have gathered overwhelming evidence in recent years, however, that systematically refutes the self-interest hypothesis, suggesting that concerns for altruism, fairness, and reciprocity strongly motivate many people. Moreover, several theoretical papers demonstrate that the observed phenomena can be explained in a rigorous and tractable manner. These theories then induced a first wave of experimental research which offered exciting insights into both the nature of preferences and the relative performance of competing fairness theories. The purpose of this chapter is to review these developments, to point out open questions, and to suggest avenues for future research. We also discuss recent neuroeconomic evidence that is consistent with the view that many people have a taste for mutual cooperation and the punishment of norm violators. We further illustrate the powerful impact of fairness concerns on cooperation, competition, incentives, and contract design.

## Summary
This is a Handbook chapter that surveys the experimental refutation of the self-interest hypothesis and the "first wave" of formal theories built to explain it. Fehr and Schmidt organize the field into three modeling strategies — distributional social preferences, interdependent (type-based) preferences, and intention-based reciprocity — present each model's utility function precisely, and then ask which experiments can discriminate among them. A recurring theme is that the interaction between selfish and fair-minded types, mediated by the strategic environment (especially competition), explains why the same people look purely selfish in some settings and strongly fairness-driven in others. (Coverage note: this is a 77-page chapter; I read targeted — front matter, the full introduction/overview, Section 3's formal models, and the model critiques — rather than ingesting every empirical and application subsection.)

## Research question
Under what conditions do other-regarding preferences (altruism, fairness, reciprocity) have important economic effects, and what is the best way to formally model these preferences so that they can be tested and discriminated against one another?

## Method / identification
A theory-survey and taxonomy, not new data. The authors formalize three departures from the self-interest model, in which agent $i$'s utility over an allocation $x=(x_1,\dots,x_N)$ depends not only on $x_i$:

1. **Social preferences** — utility is a function of the distribution of material payoffs. Variants include unconditional **altruism** ($\partial u/\partial x_j > 0$ for all $j$); **relative income / envy** (Bolton: $U_i = u_i(x_i, x_i/x_j)$, hurting only when behind); and **inequity aversion**. The [[@Fehr1999|Fehr–Schmidt (1999)]] model is the canonical specification:
$$U_i(x_1,\dots,x_N) = x_i - \frac{\alpha_i}{N-1}\sum_{j\neq i}\max\{x_j-x_i,0\} - \frac{\beta_i}{N-1}\sum_{j\neq i}\max\{x_i-x_j,0\}$$
with $0\le\beta_i\le\alpha_i$ and $\beta_i\le 1$; disadvantageous inequality ($\alpha$) hurts more than advantageous inequality ($\beta$). [[@Bolton2000|Bolton–Ockenfels (2000)]] and [[@Charness2002|Charness–Rabin]] (2002, quasi-maximin) are alternative distributional forms.

2. **Interdependent preferences** ([[@Levine1998|Levine 1998]]) — agents care about the opponent's *type* (selfish vs. altruistic); preferences are conditionally altruistic depending on the inferred type. Modelable with conventional game theory.

3. **Intention-based reciprocity** — agents care *why* an action was taken, requiring psychological game theory (Geanakoplos, Pearce & Stacchetti 1989) where payoffs depend on beliefs. Rabin's (1993) **fairness equilibrium** builds a kindness function comparing the payoff given to a "fair" benchmark (mid-range of feasible payoffs):
$$f_i(a_i,b_j) \equiv \frac{x_j(b_j,a_i) - x_j^{f}(b_j)}{x_j^{h}(b_j) - x_j^{l}(b_j)}$$
and utility $U_i = x_i(a,b_j) + f_j(b_j,c_i)\,[1 + f_i(a_i,b_j)]$. [[@Dufwenberg2004|Dufwenberg & Kirchsteiger (2004)]] extend this to $N$-person extensive-form games (Sequential Reciprocity Equilibrium); [[@Falk2006|Falk & Fischbacher (2006)]] merge intentions with inequity aversion; Charness & Dufwenberg (2004) add guilt aversion over promises.

A separate analytical move (Section 4) identifies decisive experimental designs — dummy-player vs. intentional treatments, choice-set manipulations — that can pry the predictions of these classes apart.

## Data
None — this is a synthesis. It reviews evidence from dictator, ultimatum, trust, gift-exchange, and public-good games (e.g. [[@Andreoni2002|Andreoni & Miller 2002]] GARP-consistent dictator choices; Fehr–Gächter punishment experiments), plus neuroeconomic imaging studies, but generates no new dataset.

## Key findings
- The self-interest hypothesis is robustly refuted in simple non-competitive games, yet the same models explain why competitive markets converge to the self-interested prediction — competition can make expressing other-regarding goals infinitely costly, so absence of fair behavior does not imply absence of fair preferences.
- Preference **heterogeneity** plus the strategic environment is the key mechanism: even a minority of fair-minded types can generate strong cooperation incentives for selfish types, and a population of only fair types cannot always prevent unequal outcomes.
- Among intention-based models, Rabin's fairness equilibrium suffers multiplicity (always a "nice" and a "hostile" self-fulfilling equilibrium) and cardinality problems (mixing dimensionless kindness with monetary payoffs). Falk–Fischbacher and Charness–Rabin gain fit by nesting both inequity aversion and intentions, but at the cost of many free parameters and near-untestability (Charness–Rabin's RFE is only defined in equilibrium).
- Discriminating evidence (dummy-player designs) shows intentions matter beyond pure distributional concerns, favoring hybrid models — but no single model dominates across all games.

## Contribution
Provides the field's organizing taxonomy of other-regarding-preference models, states each utility function rigorously, and frames the empirical agenda of *discriminating* between theories rather than merely fitting data — establishing that preferences can be studied scientifically. It also documents the economic reach of these preferences into contract design, incentives, collective action, and institution formation.

## Limitations & open questions
The authors explicitly flag: (i) who the relevant reference agents are is unresolved; (ii) the trade-off between equality and efficiency in preferences is unsettled (quasi-maximin vs. inequity aversion); (iii) whether reciprocity is driven by intentions, types, or outcomes needs sharper tests; (iv) intention-based models face equilibrium multiplicity with no selection criterion and strong/unappealing cardinal properties; (v) the hybrid models that fit best are too parameter-heavy to test cleanly; (vi) extending lab-calibrated preference models to field/real-world settings is an open and important next step; (vii) preferences for honesty and the neuroeconomic foundations of fairness are nascent.

## Connections
Builds directly on the inequity-aversion models of [[@Fehr1999|Fehr & Schmidt (1999)]] and [[@Bolton2000|Bolton & Ockenfels (2000)]], and the reciprocity models of [[@Rabin1993|Rabin (1993)]], [[@Dufwenberg2004|Dufwenberg & Kirchsteiger (2004)]], and [[@Falk2006|Falk & Fischbacher (2006)]]. The altruism/dictator-game evidence draws on [[@Andreoni2002|Andreoni & Miller (2002)]] and Cox, Sadiraj & Sadiraj (2001); type-based reciprocity on [[@Levine1998|Levine (1998)]]; guilt aversion on Charness & Dufwenberg (2004); and quasi-maximin preferences on [[@Charness2002|Charness & Rabin (2002)]]. The psychological-game-theory machinery comes from Geanakoplos, Pearce & Stacchetti (1989). The competitive-market benchmark traces to Smith (1962). The chapter complements structural mixture-estimation work that later quantifies type shares (e.g. Bruhin, Fehr-Duda & Epper 2019) and contrasts with revealed-preference / bounded-rationality choice models such as [[@Manzini2007|Manzini & Mariotti (2007)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
