---
citekey: Kuziemko2014
title: "“Last-Place Aversion”: Evidence and Redistributive Implications *"
authors: ["Kuziemko, Ilyana", "Buell, Ryan W.", "Reich, Taly", "Norton, Michael I."]
year: 2014
type: journalArticle
doi: 10.1093/qje/qjt035
zotero: "zotero://select/library/items/WM68JNMI"
pdf: /Users/jesper/Zotero/storage/5KK45Y6C/Kuziemko2014.pdf
tags: [literature]
keywords: [last-place-aversion, relative-position, ordinal-rank, redistribution-preferences, distributional-preferences, inequality-aversion, minimum-wage]
topics: ["[[inequity-aversion-distributional-preferences]]"]
related: [Bolton2000, Charles2009, Charness2002, Fehr1999]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We present evidence from laboratory experiments showing that individuals are "last-place averse." Participants choose gambles with the potential to move them out of last place that they reject when randomly placed in other parts of the distribution. In modified dictator games, participants randomly placed in second-to-last place are the most likely to give money to the person one rank above them instead of the person one rank below. Last-place aversion suggests that low-income individuals might oppose redistribution because it could differentially help the group just beneath them. Using survey data, we show that individuals making just above the minimum wage are the most likely to oppose its increase. Similarly, in the General Social Survey, those above poverty but below median income support redistribution significantly less than their background characteristics would predict.

## Summary
People exhibit a distinctive aversion to being in *last place*: the disutility from a drop in ordinal rank is greatest for those already near the bottom of a distribution. Across two very different laboratory paradigms (rank-improving lotteries and multi-player modified dictator games) the authors isolate last-place aversion (LPA) from expected-utility risk preferences and from the major distributional-preference models. They then argue LPA helps explain a long-standing puzzle in political economy: why some low-income individuals oppose redistribution that would appear to serve their material interest. Survey evidence on the minimum wage and General Social Survey (GSS) data on general redistributive attitudes are both consistent with the LPA prediction.

## Research question
Does ordinal rank enter utility *nonlinearly* over the distribution, such that individuals are specifically averse to occupying (or falling into) last place? And if so, can this aversion explain why people near—but not at—the bottom of the income distribution exhibit softer-than-expected support for redistributive policies?

## Method / identification
The paper combines a behavioral theory with two lab experiments and two observational survey analyses.

**Formal model.** With distinct wealth levels $y_1 < y_2 < \dots < y_N$ ($y_1$ the last-place person), utility is assumed additively separable in absolute wealth and relative position:
$$u(y_i, r_i) = \alpha\, g(r_i) + (1-\alpha) f(\cdot), \qquad \alpha \in (0,1),$$
where $r_i$ is ordinal rank ($r_i = 1$ for last place). Strict LPA sets $g(r_i) = \mathbf{1}(r_i > 1) = \mathbf{1}(y_i > y_1)$—a step "bonus" paid to everyone but the last-place person. A weaker *low-rank* aversion arises when ranks are perturbed by noise $\varepsilon_i \sim N(0,1)$: $g$ becomes a concave function rising steeply at the bottom, so the second-to-last player also bears disutility from a nontrivial probability of falling into last place. The authors stay agnostic about $f(\cdot)$ and instead show that LPA's qualitative predictions *diverge* from a broad class of $f(\cdot)$ models near the bottom.

**Lottery experiment (Section III).** $N=84$ HBS-lab participants in 14 fixed groups of 6 are randomly assigned to the distribution $\{\$1.75,\dots,\$3.00\}$ each round and choose between a risk-free \$0.13 and an equal-expected-value lottery (win \$0.50 w.p. 0.75, lose \$1.00 w.p. 0.25) whose winning payoff lets them jump two ranks. Standard diminishing-absolute-risk-aversion predicts lottery-taking should *increase* with wealth; LPA predicts the *last-place* player chooses the lottery most often (under both naive "hold others constant" and level-$k$ strategic assumptions). Identification comes from this sharp sign reversal at the bottom.

**Modified dictator game (Section IV).** $N=42$ in seven 6-player groups assigned $\{\$1,\dots,\$6\}$. Each non-extreme player gives an extra \$2 (from a separate account) to the player directly above or below; because ranks are \$1 apart, giving below drops the giver one rank. The design *holds constant* own income, total surplus, and the Fehr–Schmidt inequality terms across ranks 1–5, so inequality aversion predicts uniform giving-down while LPA predicts the second-to-last player is least likely to give down. This separates LPA from [[@Fehr1999|Fehr–Schmidt (1999)]], [[@Bolton2000|Bolton–Ockenfels (2000)]], [[@Charness2002|Charness–Rabin (2002)]], total-surplus maximization, share-of-surplus utility, and a linear rank effect. Estimation uses a probit of "gave to lower rank" on rank fixed effects, clustered by player.

**Survey analyses (Sections V–VI).** A purpose-built online survey (Nov–Dec 2010) of prime-age employed workers (oversampling low-wage/hourly) records actual hourly wage plus support for a minimum-wage increase—LPA predicts a dip in support for those earning just above the \$7.25 minimum. The GSS analysis regresses redistributive support (the `helppoor` 5-point scale, recoded increasing) on income-decile indicators plus an "LPA group" dummy (6th–8th deciles: above bottom quintile, below median), with year and region fixed effects.

## Data
- Lab: 84 subjects (756 lottery decisions) and 42 subjects (336 dictator decisions) from the HBS CLER lab.
- Minimum-wage survey: own nationally-recruited online sample of employed workers (ages 23–64), oversampling low-wage/hourly, fielded twice in 2010.
- General Social Survey: repeated cross-sections (~1,500/year), `helppoor` redistribution question (most years 1975–2010), plus welfare-generosity, Democratic-vote, and government-assistance measures; income adjusted to 2011 dollars and equivalized by $\sqrt{\text{household size}}$.

## Key findings
- **Lottery:** lottery-taking is roughly uniform across the distribution *except* the last-place player, who chooses the rank-improving lottery significantly more often—contradicting diminishing absolute risk aversion and consistent with LPA.
- **Dictator:** overall ~75% give to the lower-ranked player (consistent with inequality aversion), ranging above 80% in the top half but falling below 60% for the second-to-last-place player; between one-half and one-fourth of second-to-last players give *up*, behavior that is rare elsewhere. This is the model-separating result.
- **Minimum wage:** support for an increase is ~80%+ overall, but significantly lower among workers earning between \$7.26 and \$8.25 (those most at risk of being tied for the "last-place" legal wage).
- **GSS:** redistributive support is negative-but-convex in income decile; the 6th–8th deciles deviate below trend. The estimated LPA-group drop ($-0.0958$) exceeds the per-decile effect ($-0.0870$); robust to year/region FE and holds for both whites and minorities, ruling out a pure racial-attitudes explanation.

## Contribution
Introduces and operationally identifies *last-place aversion*—a nonlinearity in how ordinal rank enters utility, concentrated at the bottom—and shows it survives controls that neutralize leading distributional-preference models. By using larger (six-player) distributions than the standard two- or three-player dictator games, it exposes shape features of distributional preferences that smaller designs cannot detect. Substantively, it offers a novel preference-based channel for the political-economy puzzle of weak redistributive support among the near-poor.

## Limitations & open questions
- LPA is hard to identify outside the lab because real-world "last place" and individuals' perceived reference groups are ill-defined; survey results "cannot eliminate all alternative theories" and are only *consistent with* LPA.
- The lab design may put subjects in a "game" mindset that unduly triggers (or, the authors argue, possibly dampens) status concerns; external validity of small-stakes lab risk-taking is contested (cf. Rabin 2000).
- Strict last-place vs. broader low-rank aversion cannot always be cleanly distinguished in the data.
- The authors flag open questions: whether the *level* of risk aversion and its relation to wealth depend on whether wealth is viewed in absolute vs. relative terms; and the broader behavioral consequences of LPA beyond redistribution and risk-taking (a hook for future work).
- How reference groups for "last place" form, and how policy framing makes a last-place group salient, is left unmodeled.

## Connections
The utility specification follows the relative-position literature beginning with Duesenberry (1949) and the additively-separable rank-and-wealth form used by [[@Charness2002|Charness & Rabin (2002)]]. The identification strategy is built explicitly to separate LPA from inequality aversion ([[@Fehr1999|Fehr & Schmidt 1999]]), the ERC model of [[@Bolton2000|Bolton & Ockenfels (2000)]], and total-surplus / maximin motives, addressing the few-player critique noted by Engelmann & Strobel (2004, 2007) and extended by Durante, Putterman & van der Weele. Rank-based well-being evidence comes from Boyce, Brown & Moore (2010), Clark, Westergård-Nielsen & Kristensen (2009), Luttmer (2005), Blanchflower & Oswald (2004), and the relative-pay experiment of Card et al. (2012); microfoundations for caring about rank appear in Cole, Mailath & Postlewaite (1992) and Eaton & Eswaran (2003), with neurobiological evidence in Raleigh et al. (1984) and Zizzo (2002). On redistributive preferences it connects to Benabou & Ok (2001) on mobility ("prospect of upward mobility"), Roemer (1998) and Lee & Roemer (2006) on dividing issues such as race, and Alesina & Giuliano (2011). Conspicuous-consumption work (Veblen 1899; Frank 1985; [[@Charles2009|Charles, Hurst & Roussanov 2009]]) and the level-$k$ framework of Stahl & Wilson (1995) and Holt & Laury (2002) on lab risk preferences round out the references.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
