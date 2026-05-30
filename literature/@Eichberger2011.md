---
citekey: Eichberger2011
title: Are the treasures of game theory ambiguous?
authors: ["Eichberger, Jürgen", "Kelsey, David"]
year: 2011
type: journalArticle
doi: 10.1007/s00199-011-0636-4
zotero: "zotero://select/library/items/GKVGI9BD"
pdf: /Users/jesper/Zotero/storage/9ULT9PAN/Eichberger2011.pdf
tags: [literature]
keywords: [ambiguity, choquet-expected-utility, neo-additive-capacity, nash-equilibrium, coordination-games, experimental-game-theory, optimism-pessimism]
topics: []
related: [Fehr1999, Goeree2001, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Goeree and Holt (Am Econ Rev 91:1402–1422, 2001) experimentally study a number of games. In each case, they initially find strong support for Nash equilibrium; however, by changing an apparently irrelevant parameter, they find results which contradict Nash equilibrium. In this paper, we study the five normal form games from Goeree and Holt (Am Econ Rev 91:1402–1422, 2001). We argue that their results may be explained by the hypothesis that subjects view their opponents' behaviour as ambiguous. Ambiguity-aversion causes players to avoid strategies, which give low out of equilibrium payoffs. Similarly, ambiguity preference can make strategies with high payoffs more attractive.

## Summary
Eichberger and Kelsey revisit the five one-shot normal-form games from Goeree and Holt's (2001) "Ten Little Treasures of Game Theory and Ten Intuitive Contradictions" and show that the celebrated deviations from Nash equilibrium (NE) — including the systematic effect of "payoff-irrelevant" parameter changes — can be reproduced by a parsimonious model in which players treat opponents' strategies as *ambiguous*. Beliefs are neo-additive (Choquet) capacities, and crucially the ambiguity parameters are not free: they are pinned to the empirical "KW-range" estimated by Kilka and Weber (2001) from non-interactive decision experiments. With those calibrated values the equilibrium under ambiguity (EUA) qualitatively, and often quantitatively, matches the GH data.

## Research question
Can the apparent failures of Nash equilibrium in one-shot games — where strategically irrelevant payoff changes shift behaviour dramatically — be explained by players perceiving their opponents' behaviour as ambiguous, using ambiguity parameters disciplined by independent decision-theoretic evidence rather than fitted to the game data?

## Method / identification
The model uses a 2-player normal-form game $\Gamma=\langle\{1,2\};S_1,S_2,u_1,u_2\rangle$. Each player's belief about the opponent is a **neo-additive capacity** (Chateauneuf, Eichberger & Grant 2007):
$$\nu(A\mid\alpha,\delta,\pi)=\delta\,\alpha+(1-\delta)\,\pi(A)\quad\text{for }\varnothing\subsetneq A\subsetneq S_{-i},$$
with $\nu(S_{-i})=1$, $\nu(\varnothing)=0$, where $\alpha,\delta\in[0,1]$ and $\pi$ is an additive prior. The Choquet expected utility (CEU) representation is
$$V_i(s_i;\alpha,\delta,\pi)=\delta\big[\alpha\max_{s_{-i}}u_i(s_i,s_{-i})+(1-\alpha)\min_{s_{-i}}u_i(s_i,s_{-i})\big]+(1-\delta)\,E_\pi u_i(s_i,s_{-i}).$$
Here $\delta$ measures the *degree of perceived ambiguity* (situation-dependent; expected to be high in one-shot games) and $\alpha$ is the *optimism/pessimism* attitude ($\alpha=1$ pure optimism, $\alpha=0$ pure pessimism), treated as a stable personal trait. An equivalent multiple-priors representation gives $V_i=\alpha\max_{p\in P}E_p u_i+(1-\alpha)\min_{p\in P}E_p u_i$ with $P=\{p\in\Delta(S_{-i}):p\geqslant(1-\delta)\pi\}$.

The solution concept is **equilibrium under ambiguity (EUA)**, extending Dow & Werlang (1994): a pair of capacities $\nu^*=(\nu_1^*,\nu_2^*)$ such that $\varnothing\neq\operatorname{supp}\nu_i^*\subseteq R_i(\nu_{-i}^*)$, i.e. the support of each player's beliefs contains only opponent best responses. Support is defined as $\operatorname{supp}\nu=\operatorname{supp}\pi$. With additive beliefs ($\delta=0$) EUA collapses to NE. Identification discipline comes from restricting $\alpha,\delta$ to the **KW-range** ($0.4\leqslant\alpha\leqslant0.62$, $0.41\leqslant\delta\leqslant0.61$) taken from Kilka and Weber (2001), whose data also rationalize a piecewise-linear inverse-S decision-weight function $w(p)=\delta\alpha+(1-\delta)p$. No estimation on the GH data is performed; the analysis is a calibration exercise.

## Data
None collected by the authors. The paper re-analyzes the published experimental choice frequencies from [[@Goeree2001|Goeree and Holt (2001)]] for five one-shot games (Kreps coordination game with a secure option NN, Traveller's Dilemma, asymmetric matching pennies, a coordination game with a secure option, and a minimum-effort/weakest-link game) and borrows ambiguity-parameter estimates from Kilka and Weber (2001).

## Key findings
For each game the authors derive parameter conditions under which the GH-observed behaviour is the EUA, and verify these hold in the KW-range.
- **Kreps game:** pessimism makes the secure strategy NN (played by ~68%) the EUA choice for Player 2 whenever $\delta(1-\alpha)\geqslant 3/29\approx0.103$, satisfied in the KW-range. Adding 300 to all payoffs (Game B) leaves play unchanged, arguing *against* loss aversion and *for* ambiguity aversion; the "Treasure" treatment (Game C) restores the Nash $\langle B,R\rangle$ play.
- **Proposition 1 (Traveller's Dilemma):** for high penalty $R=180$ the unique symmetric EUA has both claiming $180$ (the NE); for low penalty $R=5$ optimism produces a mixed EUA with best responses $299$ and $[\bar n]$ where $\bar n(\alpha,\delta,R)=300-\frac{1-\delta}{\alpha\delta}(2R-1)$, matching the observed clustering near 300.
- **Proposition 2 (matching pennies):** in symmetric Game D the unique EUA is the 50–50 NE; in asymmetric Game E optimism makes Player 1 overweight the unlikely high payoff (320) and play T almost exclusively, with Player 2 best-responding R — behaviour no NE captures.
- **Proposition 3 (coordination with secure option):** $\langle H,H\rangle$ is an EUA throughout the KW-range in Game F, but in Game G only when $\frac{\delta\alpha}{1-\delta}\leqslant0.82$, predicting a minority switch to L (model: ~21% with uniform $\eta$; data: 36%).
- **Minimum-effort game:** if $\delta\alpha>c$ the only equilibrium is the highest effort (matches $c=0.1$); if $c>\delta\alpha+(1-\delta)$ the only equilibrium is the lowest effort (matches $c=0.9$), explaining why a cost change that is NE-irrelevant shifts coordination.

## Contribution
Provides a unified, decision-theoretically grounded account of GH's anomalies using a single behavioural mechanism — strategic ambiguity with optimism/pessimism — rather than game-specific stories. Its central methodological claim is *parameter discipline*: unlike Quantal Response Equilibrium (a sensitivity parameter) or Cognitive Hierarchy / level-k (a rationality-level distribution), whose parameters lack meaning outside the game, the ambiguity parameters $\alpha,\delta$ are measurable in independent Ellsberg-type and decision experiments, so the explanation is in principle falsifiable and portable. The paper also revisits and motivates the support notion for neo-additive capacities needed once optimistic (not merely pessimistic) responses are allowed.

## Limitations & open questions
- The authors stress that the analysis is a *calibration*, not a structural estimation, and they do not claim ambiguity is the exclusive explanation.
- Ideally $\alpha$ and $\delta$ should be measured directly for the very subjects who play the games (e.g. eliciting ambiguity attitudes via Ellsberg-type pretests, then observing game play); running such experiments is explicitly "beyond the scope of this paper" and proposed as future work.
- For the coordination game with a secure option (Game G) only a *qualitative* prediction is possible because of multiple equilibria; the 21% vs 36% gap is left to either non-uniform $\eta$ or higher game-specific ambiguity ($\delta$ larger in games than in single-person decisions) — an untested conjecture.
- $\alpha$ and $\delta$ are assumed independently distributed because the joint distribution cannot be recovered from Kilka and Weber's data — an admitted approximation.
- No formal comparison of EUA against QRE and CHM on the same data exists ("to the best of our knowledge"); the authors note all flexible models will out-fit NE simply by adding parameters, so a properly constrained horse-race remains open.
- Existence of EUA is asserted via standard fixed-point arguments referenced elsewhere rather than proved in detail here.

## Connections
The target of the analysis is [[@Goeree2001|Goeree & Holt (2001)]]; the ambiguity representation is the neo-additive capacity of Chateauneuf, Eichberger & Grant (2007), building on Schmeidler (1989) Choquet expected utility and the maxmin/multiple-priors model of Gilboa & Schmeidler (1989). The equilibrium concept extends Dow & Werlang (1994), generalized to many players in Eichberger & Kelsey (2000) and to optimism in Eichberger & Kelsey (2009); related game-theoretic ambiguity solution concepts appear in Lo (1996, 1999), Marinacci (2000), Ryan (1997), and Jungbauer & Ritzberger (2011). The comparative-statics logic (strategic complements vs. substitutes) draws on Eichberger & Kelsey (2002) and is tested in Eichberger, Kelsey & Schipper (2008, "Granny versus game theorist"); see also the unified comparative-statics treatment of Schmutzler (2011). Empirical ambiguity parameters come from Kilka & Weber (2001), with decision-weight foundations in Tversky & Wakker (1995), Wakker (2001), Gonzalez & Wu (1999), and Ellsberg (1961). Competing explanations discussed include Quantal Response Equilibrium (McKelvey & Palfrey 1995; Goeree & Holt 2005; Haile, Hortaçsu & Kosenok 2008), level-k (Stahl & Wilson 1995) and the Cognitive Hierarchy Model (Camerer, Ho & Chong 2004), and social/fairness-based payoff transformations ([[@Fehr1999|Fehr & Schmidt 1999]]; [[@Rabin1993|Rabin 1993]]; Boylan & Grant 2008). The minimum-effort game is from Van Huyck, Battalio & Beil (1990), and the Traveller's Dilemma from Basu (1994); loss aversion as an alternative is from Kahneman, Knetsch & Thaler (1991).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
