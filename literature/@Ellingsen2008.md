---
citekey: Ellingsen2008
title: "Pride and Prejudice: The Human Side of Incentive Theory"
authors: ["Ellingsen, Tore", "Johannesson, Magnus"]
year: 2008
type: journalArticle
doi: 10.1257/aer.98.3.990
zotero: "zotero://select/library/items/SG6L8IPX"
pdf: /Users/jesper/Zotero/storage/3ZS4LRVG/Ellingsen2008.pdf
tags: [literature]
keywords: [social-esteem, prosocial-behavior, motivational-crowding-out, principal-agent, signaling, gift-exchange, reciprocity]
topics: []
related: [Akerlof1982, Benabou2006, Besley2005, Bolton2000, Charness2002, Dufwenberg2004, Falk2006, Fehr1993, Fehr1999, Levine1998, Rabin1993, Sliwka2007]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Desire for social esteem is a source of prosocial behavior. We develop a model in which actors' utility of esteem depends on the audience. In a principal-agent setting, we show that the model can account for motivational crowding out. Control systems and pecuniary incentives erode morale by signaling to the agent that the principal is not worth impressing. The model also offers an explanation for why agents are motivated by unconditionally high pay and by mission-oriented principals. (JEL D01, D82)

## Summary

Ellingsen and Johannesson build an incomplete-information signaling model of motivation in which agents care about social esteem, and crucially the *value* of that esteem depends on *who* provides it: people care more about the approval of those they themselves esteem. In a sequential principal-agent game, the principal's choice of incentive scheme partly reveals the principal's character (altruistic vs. selfish), which changes how much the agent values impressing them. The model delivers a unified microfoundation for "Theory Y" phenomena: motivational crowding out under control and pecuniary incentives, the wage-level puzzle (high unconditional pay raises effort), and the appeal of mission-oriented principals. It is fit to three landmark experiments — the voluntary/involuntary trust game, the hidden costs of control, and gift exchange.

## Research question

Why do stronger material incentives and tighter control sometimes *reduce* effort (the incentive-intensity puzzle), and why does unconditionally high pay sometimes *raise* it (the wage-level puzzle) — both contrary to the standard principal-agent model? Can a single, parsimonious preference model explain these "Theory Y" patterns and the documented role of the principal's *intentions*?

## Method / identification

A two-stage game between a principal $P$ (first mover) and agent $A$. Each player has a privately known, unidimensional type $\theta_i \in \{\theta_L, \theta_H\}$ with $1 > \theta_H > \theta_L > 0$; the type indexes altruism. The materialistic part of utility is own payoff plus a weight on the opponent's payoff, $m_i + \theta_i m_j$. The crucial addition is *esteem*: players prefer being classified as the altruistic type $H$. Let $\hat{\theta}_{ji} = E[\theta_j \mid \theta_i, h]$ be $i$'s esteem for $j$ (the opponent's expectation about $i$'s type, on the equilibrium path). The value of being esteemed is scaled by the *salience* $\sigma_j = \sigma(\theta_j)$ of the opponent's regard, with $\sigma_H > \sigma_L > 0$ — esteem from an altruist counts for more. Full utility is

$$u_i = m_i + \theta_i m_j + \sigma_j \hat{\theta}_{ij}.$$

Priors $p_i^H$ may be positively correlated with own type (to capture consensus effects in beliefs), and are common knowledge with Bayesian updating. The solution concept is perfect Bayesian equilibrium refined by the Cho-Kreps (1987) Intuitive Criterion ("intuitive equilibria"). Because $P$ moves first, $P$'s action reveals $P$'s type and thus shifts $A$'s incentive to signal: a more-likely-altruistic principal is more worth impressing. The model is then applied analytically to three experimental games, with separating (and semi-separating) equilibria constructed by minimum-cost incentive-compatibility conditions.

## Data

None of its own. The paper is purely theoretical but is *calibrated qualitatively and partly quantitatively* to existing experimental datasets: McCabe, Rigdon, and Smith (2003) voluntary vs. involuntary trust game; Falk and Kosfeld (2006) control game (agent endowed with 120, control imposes a compulsory transfer of 10); and the gift-exchange evidence of [[@Fehr1993|Fehr, Kirchsteiger, and Riedl (1993)]] and Charness (2004).

## Key findings

- **Proposition 1 (Trust Game):** There is an open set of parameters with a unique intuitive equilibrium reproducing McCabe-Rigdon-Smith — agents play "reward" $R$ more in the voluntary trust game (where the principal *chose* to trust, signaling altruism) than in the involuntary trust game where trust is mechanical. No parameters generate the reverse, so the model has testable bite.
- **Proposition 2:** Generically, any vector of parameters yielding the qualitative Trust-Game pattern requires $\theta_H > \theta_L$ and $\sigma_H > \sigma_L$ — i.e., both heterogeneous altruism and source-dependent esteem salience are necessary.
- **Proposition 3 (Hidden Costs of Control):** An open set of parameters yields a separating equilibrium reproducing Falk-Kosfeld: the selfish agent transfers the minimum, the altruistic agent transfers more when *trusted* than when *controlled* ($y > x$, the defining feature of Theory Y), the selfish principal controls and the altruistic principal trusts. Endogenous control signals selfishness and erodes esteem; exogenously imposed control does not (the agent cannot infer the principal's type), matching the disappearance of the crowding-out effect. Heterogeneous priors are *necessary* to fit the full evidence, including that controlling principals underpredict effort under trust.
- **Proposition 4 (Gift Exchange):** A unique intuitive equilibrium where the altruistic principal pays $w^* > 0$ and the selfish principal pays $0$; the altruistic agent exerts higher effort after a high wage ($a_2 > a_1$). High wages signal altruism, and altruistic workers value esteem from altruistic employers more — a microfoundation for Akerlof's (1982) gift exchange and Besley and Ghatak's (2005) mission-motivation argument.

## Contribution

Provides a single signaling mechanism — esteem whose value is audience-dependent — that simultaneously rationalizes intention-based reciprocity, motivational crowding out, the wage-level and incentive-intensity puzzles, and mission orientation. Its key advance over [[@Benabou2006|Benabou and Tirole (2006)]] is dispensing with multidimensional types: a one-dimensional type suffices, and the model uniquely predicts that incentives erode motivation *more* when the principal *chose* the scheme than when it is exogenously imposed. It offers a new, preference-based (rather than action-based) formalization of reciprocity that is simpler than [[@Rabin1993|Rabin (1993)]]-style psychological game theory while capturing intention sensitivity.

## Limitations & open questions

The authors flag explicitly: (i) Is concern for esteem less important in field settings than in the lab? (ii) How do people choose to signal their characteristics in the field, if at all? (iii) To what extent do people take pride in characteristics other than prosociality? (iv) To what extent is concern for pride shaped by social context? They warn against the mechanical reading that esteem always weakens optimal material incentives: with multiple signaling channels, or a larger audience (esteem sought from peers rather than the principal), esteem can *strengthen* the case for material incentives — e.g., a CEO who values employees' regard over owners' may need strong pay incentives to undertake cost-cutting. The two-type restriction precludes quantitative comparison across games, and linear-in-money utility makes pride negligible at high stakes (a nonlinear specification is "probably preferable").

## Connections

Closely related to [[@Benabou2006|Benabou and Tirole (2006)]], who also use signaling to show material incentives can crowd out esteem, but via multidimensional types and dilution of signaling value (the Titmuss 1970 blood-donation logic; field test in Mellstrom and Johannesson). [[@Sliwka2007|Sliwka (2007)]] similarly explains why the *set* of feasible schemes matters, but through internal conformity rewards rather than external esteem. The reciprocity modeling builds on and contrasts with [[@Levine1998|Levine (1998)]] belief-dependent altruism and the psychological-game-theory tradition of Geanakoplos, Pearce, and Stacchetti (1989), [[@Rabin1993|Rabin (1993)]], [[@Dufwenberg2004|Dufwenberg and Kirchsteiger (2004)]], and [[@Falk2006|Falk and Fischbacher (2006)]]; also Charness and Dufwenberg (2006) on guilt aversion. Alternative social-preference foundations include [[@Fehr1999|Fehr and Schmidt (1999)]], [[@Bolton2000|Bolton and Ockenfels (2000)]], and [[@Charness2002|Charness and Rabin (2002)]]. It draws on the peer-monitoring models of Hollander (1990) and Kandel and Lazear (1992), [[@Akerlof1982|Akerlof (1982)]] gift exchange, [[@Besley2005|Besley and Ghatak (2005)]] mission-oriented incentives, and Andreoni (1989, 1990) warm glow. Empirical anchors are McCabe, Rigdon, and Smith (2003), Falk and Kosfeld (2006), [[@Fehr1993|Fehr, Kirchsteiger, and Riedl (1993)]], Charness (2004), and Dana, Cain, and Dawes (2006) on anonymous-dictator exit.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
