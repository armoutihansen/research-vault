---
citekey: Rabin1993
title: Incorporating fairness into game theory and economics
authors: ["Rabin, Matthew"]
year: 1993
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/SMM6MFXL"
pdf: /Users/jesper/Zotero/storage/7L3535MX/Rabin1993.pdf
tags: [literature]
keywords: [fairness, reciprocity, psychological-games, game-theory, behavioral-economics, fairness-equilibrium, social-preferences]
topics: []
related: [Akerlof1982, Bolton2000, Dufwenberg2004, Falk2006, Fehr1999]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> People like to help those who are helping them, and to hurt those who are hurting them. Outcomes reflecting such motivations are called fairness equilibria. Outcomes are mutual-max when each person maximizes the other's material payoffs, and mutual-min when each person minimizes the other's payoffs. It is shown that every mutual-max or mutual-min Nash equilibrium is a fairness equilibrium. If payoffs are small, fairness equilibria are roughly the set of mutual-max and mutual-min outcomes; if payoffs are large, fairness equilibria are roughly the set of Nash equilibria. Several economic examples are considered, and possible welfare implications of fairness are explored. (JEL A12, A13, D63, C70)

## Summary
Rabin builds the first general game-theoretic model of reciprocity-based fairness. He formalizes three stylized facts from psychology: people sacrifice material payoff to (A) reward kindness and (B) punish unkindness, with (C) both motives weakening as the material stakes rise. Crucially, fairness is *intentional* and belief-dependent — how I treat you depends on how kind I believe you are being to me, which cannot be captured by simply re-specifying payoffs over actions. Using the "psychological games" apparatus of Geanakoplos, Pearce, and Stacchetti (GPS, 1989), he derives a solution concept, **fairness equilibrium**, and shows it interpolates between cooperative/spiteful coordination at small stakes and ordinary Nash play at large stakes. The paper is theoretical (no data), illustrated with battle-of-the-sexes, prisoner's dilemma, chicken, monopoly pricing, and a gift-exchange labor model.

## Research question
Can the psychological regularities that people reward kind behavior and punish unkind behavior — even at a cost to themselves — be incorporated into a *general* (not context-specific) noncooperative game-theoretic framework? And if so, when does adding fairness substantively change the predictions of standard economic models, in which direction, and what are the welfare consequences?

## Method / identification
The formal contribution is a solution concept built atop GPS psychological games, in which payoffs depend on beliefs (and higher-order beliefs), not just actions. Rabin's innovation is to *derive* the psychological game from an underlying two-player, finite-strategy "material game" with payoffs $\pi_i(a_i,b_j)$, using assumptions about fairness, so the model can be compared directly to standard analysis.

The core construction is the **kindness function**. Given player $j$'s strategy $b_j$, the feasible payoff set is $\Pi(b_j)=\{(\pi_i(a,b_j),\pi_j(b_j,a)):a\in S_i\}$. Let $\pi_j^h(b_j)$ be $j$'s highest payoff in $\Pi(b_j)$, $\pi_j^l(b_j)$ the lowest Pareto-efficient payoff, and define the **equitable payoff** $\pi_j^e(b_j)=[\pi_j^h(b_j)+\pi_j^l(b_j)]/2$, with $\pi_j^{\min}(b_j)$ the worst feasible payoff. Player $i$'s kindness to $j$ is

$$f_i(a_i,b_j)=\frac{\pi_j(b_j,a_i)-\pi_j^e(b_j)}{\pi_j^h(b_j)-\pi_j^{\min}(b_j)}$$

(set to $0$ if the denominator is $0$). It measures whether $i$ gives $j$ more ($f_i>0$) or less ($f_i<0$) than the equitable payoff; by normalization $f_i\in[-1,\tfrac12]$, and it is invariant to positive affine transforms of payoffs. Player $i$'s belief about $j$'s kindness, $\tilde f_j(b_j,c_i)$, is defined analogously over the second-order belief $c_i$. Utility is

$$U_i(a_i,b_j,c_i)=\pi_i(a_i,b_j)+\tilde f_j(b_j,c_i)\cdot[1+f_i(a_i,b_j)].$$

The multiplicative cross-term is the heart of reciprocity: if $i$ believes $j$ is unkind ($\tilde f_j<0$), $i$ raises utility by making $f_i$ low (retaliation); if $j$ is kind, $i$ wants $f_i$ high. Because kindness terms are bounded, the *material* term dominates as stakes grow — encoding stylized fact C. **Fairness equilibrium** (Definition 3) is the psychological Nash equilibrium of GPS: $a_i\in\arg\max U_i(a,b_j,c_i)$ with the belief-consistency conditions $c_i=b_i=a_i$ for $i=1,2$. Two outcome classes organize the results: a **mutual-max** outcome has $a_i\in\arg\max_a \pi_j(a,a_j)$ for both $i$, and a **mutual-min** outcome has $a_i\in\arg\min_a \pi_j(a,a_j)$.

## Data
None — this is a pure theory paper. Empirical motivation is borrowed from prior public-goods and ultimatum-game experiments (e.g., Dawes and Thaler 1988 report one-shot public-good contribution rates of 40–60% of the social optimum; ultimatum-game rejections of unfair offers). The applications (monopoly, labor) are stylized illustrative models, not estimated.

## Key findings
- **Proposition 1**: Any Nash equilibrium that is *also* a mutual-max or mutual-min outcome is a fairness equilibrium. (E.g., the coordinated outcomes of battle-of-the-sexes survive; the strict Nash equilibria of Chicken do not satisfy the premise.)
- **Proposition 2**: Every fairness equilibrium is either strictly positive ($f_i>0$ both) or weakly negative ($f_i\le 0$ both) — there is always a *symmetry of attitude*; one player is never kind while the other is unkind.
- **Propositions 3 & 4 (small stakes)**: Every strictly positive mutual-max outcome and every strictly negative mutual-min outcome is a fairness equilibrium for $X$ small enough (Prop. 3); outcomes that are neither mutual-max, mutual-min, nor a "can't-lower-the-other's-payoff" Nash equilibrium are *not* fairness equilibria for small $X$ (Prop. 4). Together: at small stakes, fairness equilibria are roughly the union of mutual-max and mutual-min outcomes.
- **Proposition 5 (large stakes)**: Strict Nash equilibria become fairness equilibria for $X$ large; non-Nash outcomes do not. So at large stakes the set collapses (roughly) onto Nash equilibria.
- **Proposition 6 ("unkind equilibrium")**: *Every* game has at least one weakly negative fairness equilibrium. There is no game in which players are guaranteed to part with positive feelings — a structural *bias toward negative feelings*, because being kind always requires sacrificing material self-interest, whereas being mean never does.
- **Monopoly application**: The highest price sustainable in a fairness equilibrium is $z^{*}=[2v^{2}-2cv+c]/[1+2v-2c]<v$ whenever $v>c$ — a profit-maximizing monopolist prices strictly *below* the classical monopoly price, and consumers will pay more to a high-cost firm ($dz^{*}/dc>0$). As stakes grow large, however, the extracted surplus share $\to 1$.
- **Labor / gift-exchange application**: In a simultaneous effort-benefit game, the unique Nash (and mutual-min) outcome is $(e=L,b=0)$, but a "gift-giving" equilibrium with high effort and bonus $b^{*}=R/(1+4R)$ exists iff $R\le 0.25[1/(0.5+y)^{1/2}-1]$; if disutility $y\ge 2$ no gift-exchange equilibrium exists for any $R$.

## Contribution
Provides the foundational formal model of *intention-based reciprocity*, distinct from unconditional ("pure") altruism and from inequity-aversion-by-outcome. By grounding fairness in beliefs and deriving psychological games from material games, it gives economists a general, transferable language for fairness in any two-person complete-information game, and a sharp comparative-statics prediction (fairness matters most at small stakes, vanishes at large stakes). It reframes welfare analysis: the full utility (material plus fairness payoffs) is the correct welfare object, so unhappiness from being treated unkindly is itself an efficiency concern. This paper is the direct intellectual ancestor of Dufwenberg–Kirchsteiger and Falk–Fischbacher reciprocity models and a counterpoint to Fehr–Schmidt and Bolton–Ockenfels outcome-based inequity aversion.

## Limitations & open questions
Rabin is explicit about the model's shortfalls and the extensions needed for applied work:
- **Status quo / reference points**: notions of fairness are heavily shaped by reference points (e.g., a firm's past prices); the model omits this.
- **Multi-person games**: the central unresolved issue is behavior when one is hostile to some players but friendly to others — e.g., do you contribute to a public good to *reward* contributors or withhold to *punish* free-riders?
- **Incomplete information**: because behavior hinges on inferred motives, and motives depend on beliefs about others' payoffs/information, incomplete information will dramatically alter decision-making; extending here is "essential for applied research."
- **Sequential games**: past behavior can *change* (not just reveal) motivations; can a first-mover "force" positive emotions, possibly overturning Proposition 6?
- **Additional emotions**: the model misses, e.g., rewarding *trust* — in his Example 6 partnership game it predicts inefficient dissolution because trusting is "self-interested," yet $(trust, share)$ seems behaviorally plausible.
- The model currently assumes a single shared kindness function and de-emphasizes mixed strategies; results are only *qualitative* (units of material payoff are undetermined), and the text's kindness function is not everywhere continuous, so the GPS existence theorem applies only to continuous variants (used to prove Prop. 6).

## Connections
Built directly on **Geanakoplos, Pearce, and Stacchetti (1989)** psychological games (and Gilboa–Schmeidler 1988); motivated empirically by **Kahneman, Knetsch, and Thaler (1986)** on fairness as a constraint on profit-seeking, **Dawes and Thaler (1988)** on public goods, and ultimatum-game evidence surveyed by **Thaler (1988)**. The labor application formalizes **[[@Akerlof1982|Akerlof's (1982)]]** gift-exchange view of employment. It departs sharply from simple-altruism models by making concern for others *conditional on their intentions*. Downstream, it anchors the reciprocity literature ([[@Dufwenberg2004|Dufwenberg & Kirchsteiger 2004]]; [[@Falk2006|Falk & Fischbacher 2006)]] and sits in contrast to outcome-based distributional models ([[@Fehr1999|Fehr & Schmidt 1999]]; [[@Bolton2000|Bolton & Ockenfels 2000)]]. Rabin (1992) is the companion working paper with additional labor examples and the multiple-kindness-function results.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
