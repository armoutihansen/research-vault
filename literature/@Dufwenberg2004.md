---
citekey: Dufwenberg2004
title: A theory of sequential reciprocity
authors: ["Dufwenberg, Martin", "Kirchsteiger, Georg"]
year: 2004
type: journalArticle
doi: 10.1016/j.geb.2003.06.003
zotero: "zotero://select/library/items/M6RTGGUL"
pdf: /Users/jesper/Zotero/storage/IQVULGY5/Dufwenberg2004.pdf
tags: [literature]
keywords: [reciprocity, psychological-game-theory, sequential-rationality, intention-based-preferences, extensive-form-games, social-preferences, equilibrium-existence]
topics: []
related: [Akerlof1982, Bolton2000, Charness2002, Fehr1993, Fehr1999, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Many experimental studies indicate that people are motivated by reciprocity. Rabin [Amer. Econ. Rev. 83 (1993) 1281] develops techniques for incorporating such concerns into game theory and economics. His theory is developed for normal form games, and he abstracts from information about the sequential structure of a strategic situation. We develop a theory of reciprocity for extensive games in which the sequential structure of a strategic situation is made explicit, and propose a new solution concept—sequential reciprocity equilibrium—for which we prove an equilibrium existence result. The model is applied in several examples, and it is shown that it captures very well the intuitive meaning of reciprocity as well as certain qualitative features of experimental evidence.

## Summary
This paper extends Rabin's (1993) normal-form theory of intention-based reciprocity to extensive (sequential) games. Using the apparatus of psychological game theory, the authors define belief-dependent kindness and perceived kindness that are updated as new subgames are reached, embed them in a utility function, and propose a new equilibrium concept—the sequential reciprocity equilibrium (SRE)—for which they prove existence. Applied to the sequential prisoners' dilemma, the centipede game, and the three-player "So Long, Sucker," the model reproduces qualitative features of experimental data that Rabin's normal-form construct cannot (notably, retaliation after an observed unkind move).

## Research question
How can a concern for intention-based reciprocity be modeled in *sequential* (extensive-form) games, where a player's beliefs—and therefore his assessments of others' kindness—must be revised as play unfolds? Rabin's normal-form theory can prescribe non-optimizing behavior at unreached information sets (e.g., it admits unconditional cooperation in the sequential prisoners' dilemma); the goal is a concept that imposes sequential rationality while letting reciprocity motives track belief revision.

## Method / identification
The construction is purely theoretical, built within psychological game theory (Geanakoplos, Pearce & Stacchetti 1989). The authors restrict attention to finite multi-stage games with observed actions and without nature. Starting from a standard game $\Gamma$ with material payoff functions $\pi_i$, they derive a psychological game $\Gamma^* = (\Gamma, (U_i)_{i \in N})$.

The key device is *history-indexed updating*: for a strategy $a_i$ and history $h$, $a_i(h)$ prescribes the same choices as $a_i$ except that the choices defining $h$ are assigned probability 1; beliefs $b_{ij}$ (i's belief about j's strategy) and $c_{ijk}$ (i's belief about j's belief about k's strategy) are updated analogously. Players treat observed moves as deliberate, so after observing $D$ a player judges it chosen with probability 1—this is what induces a retaliatory motive.

Kindness is measured relative to an equitable reference point computed over *efficient* strategies $E_i$. The equitable payoff is
$$\pi_j^{ei}\big((b_{ij})_{j\neq i}\big) = \tfrac{1}{2}\Big(\max\{\pi_j(a_i,(b_{ij})_{j\neq i}) \mid a_i \in A_i\} + \min\{\pi_j(a_i,(b_{ij})_{j\neq i}) \mid a_i \in E_i\}\Big).$$
Player i's kindness to j at history $h$ is the size of the "gift" relative to this reference:
$$\kappa_{ij} = \pi_j\big(a_i(h),(b_{ij}(h))_{j\neq i}\big) - \pi_j^{ei}\big((b_{ij}(h))_{j\neq i}\big).$$
Believed kindness $\lambda_{iji}$ (how kind i believes j is to i) is defined symmetrically from i's first- and second-order beliefs. Utility adds a sign-matching reciprocity term to material payoff:
$$U_i = \pi_i + \sum_{j \in N\setminus\{i\}} Y_{ij}\,\kappa_{ij}\,\lambda_{iji},$$
where $Y_{ij}\ge 0$ is i's reciprocity sensitivity toward j. Because $\kappa_{ij}\,\lambda_{iji}$ multiplies kindness by believed kindness, positive (negative) believed kindness rewards being kind (unkind) in return.

An SRE is a profile $a^* = (a_i^*)$ such that at every history $h$ each player's choice maximizes $U_i$ given correctly-anchored, updated beliefs, with initial first- and second-order beliefs correct ($b_{ij}=a_j^*$, $c_{ijk}=a_k^*$). The concept rules out profitable *local* one-shot deviations only; preferences may be dynamically inconsistent because belief updating changes kindness assessments mid-play.

## Data
None—this is a theory paper. It confronts no original dataset, instead comparing the model's *predictions* against qualitative stylized facts from existing experiments ([[@Fehr1993|Fehr et al. 1993]], 1998; Clark & Sefton 2001; ultimatum and gift-exchange literatures).

## Key findings
- **Existence Theorem:** an SRE exists in every psychological game with reciprocity incentives. The proof uses Kakutani's fixed-point theorem on a best-reply correspondence that distinguishes players *and* the histories at which they move; standard backward induction fails because kindness at $h$ depends on beliefs about play at histories not following $h$. The result is not covered by Geanakoplos et al. (1989), who restrict attention to games where only initial beliefs matter.
- With $Y_{ij}=0$ for all $i,j$, SRE reduces to subgame-perfect equilibrium of $\Gamma$ (via the one-shot-deviation property).
- **Sequential prisoners' dilemma:** if player 1 defects, player 2 defects in every SRE (Observation 1)—retaliation, which Rabin's normal-form theory fails to enforce. If 1 cooperates, 2 cooperates when $Y_2>1$, defects when $Y_2<0.5$, and mixes with $p=(2Y_2-1)/Y_2$ for intermediate $Y_2$. Player 1's behavior is more complex: high reciprocity sensitivities admit both cooperation and "self-fulfilling expectations" defection equilibria. SRE need not be unique or in pure strategies even with generic payoffs.
- **Centipede game:** the SRE can be unique even with many stages, and for large enough reciprocity parameters only positive emotions are predicted (players kind to one another)—the number of equilibria does not necessarily grow with the number of stages.
- **So Long, Sucker (three players):** demonstrates applicability beyond two players; in some games all moving players are unkind to one another along the equilibrium path.

## Contribution
First general theory of *intention-based* reciprocity for extensive-form games with a proven existence result, filling the gap [[@Rabin1993|Rabin]] (1993, p. 1296) flagged as "essential for applied research." It shows how to keep track of belief revision so that reciprocity motives respond to observed (un)kind moves, delivering retaliation predictions that match experiments. The companion paper (Dufwenberg & Kirchsteiger 2000) applies it to employer–employee relations, explaining employers' reluctance to hire workers offering below-prevailing wages.

## Limitations & open questions
- **Off-path belief revision is left unsolved:** the model does not address what a "surprised" player should infer from a move that equilibrium says should not occur (a general problem of sequential rationality; cf. Reny 1992).
- **Dynamically inconsistent preferences** are admitted; the SRE only precludes local deviations, and multi-stage deviations profitable from an early stage may exist (though they cannot be carried out without commitment).
- **Unit-dependence:** $U_i$ is not invariant to the monetary scale—the reciprocity term has the dimension of dollars-squared. A square-root reformulation fixes this only at considerable analytic cost.
- **Efficiency definition is debatable:** the authors discuss a critique (a "masochistic response" variant of $\Gamma_3$) under which adding a dominated option changes kindness assessments.
- The paper explicitly suggests **measuring beliefs in the laboratory** and testing Definitions 1–3 (the kindness/updating machinery) separately from the equilibrium hypothesis (Definition 4)—concrete hooks for empirical work.

## Connections
The direct antecedent is [[@Rabin1993|Rabin (1993)]], whose normal-form reciprocity model this paper extends to sequential games; the formal machinery comes from Geanakoplos, Pearce & Stacchetti (1989) on psychological games. It contrasts sharply with distributional/outcome-based models—[[@Fehr1999|Fehr & Schmidt (1999)]] and [[@Bolton2000|Bolton & Ockenfels (2000)]]—which are indifferent to intentions, and with Falk & Fischbacher (1998), [[@Charness2002|Charness & Rabin (2002)]], and Cox & Friedman (2002), which blend distributional and reciprocity elements. Segal & Sobel (1999) offer a related second-approach (reciprocity) model. The fair-wage-effort applications connect to [[@Akerlof1982|Akerlof (1982)]], Akerlof & Yellen (1988, 1990), Fehr & Kirchsteiger (1994), and Bewley (1999), and the experimental motivation draws on Berg et al. (1995), [[@Fehr1993|Fehr et al.]] (1993, 1997, 1998), and Clark & Sefton (2001). Dynamically inconsistent preferences relate to Strotz (1956) and Harris & Laibson (2001). The mass-action interpretation of mixed strategies follows Nash (1950) and Weibull (1994). The companion application is Dufwenberg & Kirchsteiger (2000).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
