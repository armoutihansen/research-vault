---
citekey: Levine1998
title: Modeling Altruism and Spitefulness in Experiments
authors: ["Levine, David K."]
year: 1998
type: journalArticle
doi: 10.1006/redy.1998.0023
zotero: "zotero://select/library/items/342PITR8"
pdf: /Users/jesper/Zotero/storage/LBDVCKX4/Levine1998.pdf
tags: [literature]
keywords: [social-preferences, altruism, spitefulness, reciprocity, ultimatum-game, centipede-game, public-goods, signaling-games]
topics: []
related: [Bolton2000, Charness2002, Fehr1999, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We examine a simple theory of altruism in which players' payoffs are linear in their own monetary income and their opponents. The weight on the opponent's income is private information and varies in the population, depending, moreover, on what the opponent's coefficient is believed to be. Using results of ultimatum experiments and the final round of a centipede experiment, we are able to pin down relatively accurately what the distribution of altruism (and spite) in the population is. This distribution is then used with a reasonable degree of success to explain the results of the earlier rounds of centipede and the results of some public goods contribution games. In addition, we show that in a market game where the theory of selfish players does quite well, the theory of altruism makes exactly the same predictions as the theory of selfish players. Journal of Economic Literature Classification Numbers: C70, C72, D90, D92.

## Summary
Levine proposes a parsimonious, fully game-theoretic model of other-regarding preferences in which each player's adjusted utility is linear in their own and their opponents' monetary payoffs, with a private "coefficient of altruism" drawn from a population distribution. Crucially, the weight a player puts on an opponent's payoff is not fixed but is *adjusted* by what the player believes about the opponent's coefficient, turning ordinary games into signaling games. Using a single fixed distribution of types calibrated on ultimatum and final-round centipede data, the model quantitatively explains earlier centipede rounds and public-goods contributions, while collapsing to the selfish prediction in a competitive market game. The headline empirical surprise is a substantial mass (about 20%) of strongly *spiteful* players.

## Research question
Can a single, simple, internally consistent model of non-selfish preferences—staying entirely within standard Bayesian/sequential-equilibrium game theory—quantitatively (not merely qualitatively) explain the anomalous results of ultimatum bargaining, the centipede game, and public-goods contribution games, using *one* fixed population distribution of preference types across all of them?

## Method / identification
The formal model: in an $n$-person extensive-form game, player $i$ receives direct utility $u_i$ at terminal nodes and maximizes an adjusted utility
$$v_i = u_i + \sum_{j \neq i} \frac{a_i + \lambda a_j}{1 + \lambda}\, u_j,$$
where $-1 < a_i < 1$ is $i$'s private coefficient of altruism ($a_i>0$ altruistic, $a_i=0$ selfish, $a_i<0$ spiteful) and $0 \le \lambda \le 1$ governs how much the weight on $j$'s payoff is pulled toward $j$'s own type. With $\lambda=0$ this is pure altruism (à la Ledyard); with $\lambda>0$ it embeds a "fairness" flavor—players are kinder to opponents believed to be kind—without requiring any exogenous notion of a "fair" outcome (contrast Rabin's $b_{ij}=\gamma_i(u_i - u_i^f)$).

Coefficients $a_i$ are drawn i.i.d. from a common-knowledge CDF $F(a_i)$, so each game is a Bayesian game; the solution concept is sequential equilibrium (equivalent here to perfect Bayesian) refined by a monotonicity restriction on off-path beliefs (the type most likely to deviate is the one for whom deviation is least costly). Identification is the paper's core craft: a three-point support $\bar{a} > a_0 > \underline{a}$ (altruistic/normal/spiteful) is pinned by matching equilibrium demand frequencies and acceptance rates in the ultimatum data; the spiteful/normal coefficients and $\lambda$ come from six incentive constraints (Lemma A), while the altruistic coefficient $\bar{a}$—unidentified from ultimatum—is fixed by the indifference condition at the final centipede node. The market and public-goods predictions then use *no free parameters*.

## Data
Re-analysis of published experimental data (no new experiments): ultimatum bargaining across four countries from Roth et al. (final of 10 rounds, pooled); a competitive market/auction game from the same Roth et al. study; the McKelvey & Palfrey centipede (grab-a-dollar) experiment (29 sessions, last 5 of 10 rounds); and the Isaac & Walker public-goods contribution game (four treatments varying $n$ and marginal per-capita return $g$, final round).

## Key findings
- **Proposition 1:** Regardless of $F$, no demand below \$5.00 is made and any demand of \$5.00 or less is accepted (since $x + b(10-x)$ is increasing in $x$ for $b>-1$). The data conform.
- **Proposition 3:** No sequential equilibrium exists with $\lambda=0$—pure altruism *cannot* fit ultimatum, because matching rejection rates forces players to be spiteful, yet spiteful players would not make the modest observed demands. Reciprocity-type belief dependence ($\lambda>0$) is essential.
- **Proposition 4:** The equilibrium bounds are $-0.301 \le a_0 \le -0.095$, $-1 < \underline{a} < -0.73$, and $0.584 \ge \lambda \ge 0.222$; the authors adopt $\lambda=0.45$, $\underline{a}=-0.9$, $a_0=-0.22$.
- **Proposition 5:** Pooling equilibria at \$7 and \$8 survive (predictive power is limited, as typical of signaling models), but pooling at \$5, \$6, \$9, \$10 is ruled out.
- **Proposition 6 (market game):** There exist sequential equilibria in which buyer offers are independent of altruism and the seller always sells; the set of such equilibria is independent of $F$. Thus in competitive environments where utility cannot be cheaply transferred, the altruism model reproduces the selfish/competitive prediction exactly.
- **Centipede test:** With $\bar{a}=2/7\approx 0.29$ calibrated at the final node, earlier-round choices match the data; the per-player expected loss relative to the model is about 1.5¢ versus about 14.5¢ for the selfish model—nearly an order of magnitude better.
- **Public goods:** A cutoff rule $a^* = \frac{(1-g)(1+\lambda)}{(n-1)g} - \lambda \hat{a}$ determines who contributes; aggregate contribution rates across treatments are broadly consistent with the same ~28% altruistic share.

## Contribution
A unifying, quantitatively disciplined "type-dependent linear altruism" model that (i) stays inside standard game theory while capturing reciprocity through belief-dependent weights, (ii) imposes the strong cross-game restriction of one fixed type distribution, and (iii) reconciles pro-social behavior in ultimatum/centipede/public-goods with selfish-looking behavior in competitive markets. It is an important precursor to the distributional and reciprocity models that followed, and a methodological template for cross-game structural estimation of social preferences.

## Limitations & open questions
- The linear specification predicts contributions should be all-or-nothing, contradicting observed *partial* public-goods contributions (rationalized only via near-indifference randomization).
- The model **cannot explain dictator-game giving**: with linear utility and $a_i<1$ it predicts zero transfers, yet positive giving is observed.
- Van Huyck et al. find far *less* spitefulness than the estimated distribution implies, raising the question of whether the spite coefficient is stable or really reflects "competitiveness" that scales with the number of opponents.
- Multiplicity of equilibria (pooling) limits sharp prediction; the parameter choice within the admissible range is "somewhat arbitrary."
- The paper explicitly leaves open *why* players are altruistic/spiteful, speculating that an evolutionary account of these preferences is a target for future research.
- Whether systematic departures of non-zero-sum mixed-strategy equilibria from Nash play can be explained by the recovered altruism distribution is left as an open question.

## Connections
The model is positioned against [[@Rabin1993|Rabin (1993)]] and Geanakoplos, Pearce & Stacchetti (1989) on psychological games and fairness/reciprocity, offering a simpler belief-dependent alternative. It builds on Ledyard's linear pure-altruism specification and parallels Andreoni & Miller's nonlinear-altruism estimation of public-goods data. The signaling/reputation mechanism draws on Fudenberg & Levine's work on reputation, and the loss-metric comparison uses Fudenberg & Levine's approach to measuring departures from equilibrium. Empirically it re-analyzes Roth et al. (ultimatum and market), McKelvey & Palfrey (centipede and mixed-strategy anomalies), Isaac & Walker (public goods), and Van Huyck et al. Equilibrium-failure explanations of the same anomalies (Binmore & Samuelson) are contrasted with the preference-based account. The paper is a direct intellectual antecedent of the inequity-aversion and reciprocity models of [[@Fehr1999|Fehr & Schmidt (1999)]], [[@Bolton2000|Bolton & Ockenfels (2000)]], and [[@Charness2002|Charness & Rabin (2002)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
