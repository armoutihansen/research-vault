---
citekey: Benabou2009
title: "Over My Dead Body: Bargaining and the Price of Dignity"
authors: ["Bénabou, Roland", "Tirole, Jean"]
year: 2009
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/397JHVQB"
pdf: /Users/jesper/Zotero/storage/9K5PIBFY/Benabou2009.pdf
tags: [literature]
keywords: [motivated-beliefs, self-image, bargaining-impasse, coasian-bargaining, dignity, identity-economics, nash-demand-game]
topics: []
related: [Akerlof1982, Brunnermeier2005, Caplin2001, Loewenstein1987, Loewenstein1992]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
A short AEA Papers & Proceedings piece (8 pp.) in which Bénabou and Tirole build a stylized model of how concerns for self-image, dignity, and "hope" can make even fully symmetric-information Coasian bargaining break down. Two partners who jointly know they have produced a poor outcome each try to avoid being identified as the one "to blame." Because individual contributions are softly recalled, refusing an "insulting" offer lets a party self-infer a flattering type. As identity/anticipatory concerns become more salient, the set of mutually acceptable sharing rules shrinks and, past a threshold, no agreement is possible despite gains from trade. Self-enhancement is a zero-sum game over images that nets only destroyed surplus.

## Research question
Why do parties walk away from reasonable, mutually beneficial deals - in divorces, strikes, labor disputes, ethnic conflict, wars - even under symmetric information, accompanied by wishful rationalizations and self-serving delusions? Can a tractable model explain inefficient bargaining impasses driven not by private information or strategic delay, but by each side's desire to preserve pride, dignity, and a hopeful self-view?

## Method / identification
A three-period game-theoretic model, an application of the authors' general "beliefs as assets" framework (Bénabou and Tirole 2007). A risk-neutral partnership of two agents, each type $H$ with probability $p$ or $L$ with probability $1-p$, with reservation values $v_H > v_L$. The technology is Leontief/complementary: joint output is $y \in \{y_B, y_G\}$ with $y = y_G$ if and only if both partners are type $H$; otherwise $y = y_B$. Parameters satisfy
$$y_G > 2v_H > y_B > v_H + v_L > 2v_L,$$
so staying together is efficient for all team compositions (HH, HL, LL), but an unbalanced HL pair needs a compensating transfer (a share of $y_B$ above $1/2$) to retain the high type.

Two behavioral assumptions drive the results. **Assumption 1 (Self-inference):** at date 1 each player recalls the true individual contributions $v_i$ only with probability $\lambda$; with probability $1-\lambda$ he has forgotten them and must infer his own and his partner's type from the negotiation outcome (which offers were made, accepted, or rejected). Players are Bayesian, so $1-\lambda$ measures the malleability of beliefs. A player's date-1 belief $p_i$ yields a subjective worth $v_i = p_i v_H + (1-p_i) v_L$. **Assumption 2 (Motivated beliefs):** agents derive utility from anticipatory feelings about future income (or from pure self-esteem), so date-0 payoff is
$$U_i^0 = E_0^i[\, s\, u_i^1 + U_i^2\,],$$
with $u_i^1 = E_1^i[U_i^2]$ in the anticipatory-utility case and $u_i^1 = E_1^i[v_i]$ in the pure self-esteem case; the salience parameter $s$ weights the "mental consumption" of self-image. Bargaining is a standard **Nash demand game**: at date 0, players simultaneously demand shares $\theta_1, \theta_2$ of future output $y$; if $\theta_1 + \theta_2 \le 1$ each gets his demand, while if $\theta_1 + \theta_2 > 1$ the match dissolves and each receives his outside option. Out-of-equilibrium beliefs are pinned down with a $D1$-style refinement (the strong type has less to lose from breakup, so a unilateral high demander is assigned image $v_H$). The solution concept is symmetric pure-strategy Perfect Bayesian equilibrium, with shares $\theta_H^* > 1/2 > \theta_L^*$ in HL pairs and $1/2$ in balanced pairs.

## Data
None - this is a pure theory note. The model is motivated by field evidence (Bewley 1999 on wage/morale dynamics; Woods, Lacey, and Murray 2006 on Saddam-era war delusions) and laboratory work (Babcock et al. 1995; [[@Loewenstein1992|Thompson and Loewenstein 1992]] on egocentric/self-serving fairness judgments; Dana, Weber, and Kuang 2007 on moral wiggle room; Konow 2000), but no original empirical analysis is performed. The authors note the model yields testable predictions because salience $s$ and the productivity gap $v_H/v_L$ are manipulable.

## Key findings
HH pairs always agree and split equally. The interesting cases are low-output ($y = y_B$) pairs.

- **Proposition 1 (agreement ranges and thresholds).** (i) For salience $s$ below a critical $s^*$, unbalanced HL pairs successfully negotiate any sharing rule $\theta_L^*$ in the mutually agreeable interval; this interval shrinks as $s$ rises, and for $s > s^*$ the HL match is inefficiently destroyed. (ii) For $s < s^{**}$, balanced LL pairs agree on a 50-50 split; for $s > s^{**}$ they too dissolve. The HL threshold is
$$s^* = \frac{y_B - v_H - v_L}{v_H + \lambda v_L + (1-\lambda)\bar v - y_B},$$
(and $s^* = +\infty$ when the denominator is non-positive); a parallel expression $s^{**}$ governs LL pairs. (iii) With $y_B = \phi v_L$, for any $s$ the bargaining set shrinks and both impasse types become more likely as the inequality $v_H/v_L$ grows. Intuitively, higher $s$ makes "admitting blame" more costly for the L type, who then demands compensation the H type will not grant.
- **Proposition 2 (comparative statics of breakdown).** Inefficient breakdowns are more likely (i) the more salient agents' identity concerns (higher $s$), and (ii) the more malleable their memories/beliefs (lower $\lambda$).
- **Proposition 3 (welfare).** Greater malleability of beliefs ($1 - \lambda$) always *lowers* normalized ex ante welfare $W = E[U_1^0 + U_2^0]/(1+s)$, as does greater salience $s$. In any dissolving pair both sides demand the same $\theta_H^* > 1/2$ and self-assign image $v_H$, but the average inferred worth over dissolutions equals the true average, so there is **no net gain in self-esteem - only a zero-sum transfer of image plus a real loss of surplus** averaging $(1+s)(y_B - 2\bar v) > 0$.
- **A functional twist (Section IIB).** If date-1 effort is subject to a self-control problem ($\beta < 1$) and returns rise with self-view $v$, then pooling (rejecting realistic offers) boosts the low type's confidence and motivation while sapping the high type's. When the self-control problem is *moderate* (binds the L type more), belief malleability yields a net efficiency gain - dignity can be socially useful; when it is *severe* (binds the H type more), the result is again a net loss. So the normative verdict hinges on whether self-image serves hedonic or functional ends.

## Contribution
Identifies a novel limit to Coasian bargaining: not asymmetric information, transaction costs, or strategic delay, but the endogenous preservation of dignity, pride, and hope. It formalizes self-serving belief generation (à la Babcock et al.) inside an equilibrium bargaining model where memory itself is the strategic object, and shows that the *ability* to manage one's own identity can make a person worse off. It thereby links the cognitive-dissonance / motivated-beliefs literature ([[@Akerlof1982|Akerlof and Dickens 1982]]; Rabin 1994; [[@Brunnermeier2005|Brunnermeier and Parker 2005]]), anticipatory utility ([[@Loewenstein1987|Loewenstein 1987]]; [[@Caplin2001|Caplin and Leahy 2001]]), and self-signaling (Bodner and Prelec 2003) to distributive conflict.

## Limitations & open questions
The authors are explicit about scope and extensions. (1) The model is a deliberately simple one-shot Nash demand game; it abstracts from the *dynamic* offer/counteroffer structure central to the heterogeneous-priors bargaining literature (Yildiz 2004; Ali 2006). (2) Beliefs are managed only via imperfect recall and Bayesian self-inference; relaxing full Bayesian rationality is flagged as easy but not done here. (3) Social-reputation (signaling to an outside audience) is largely "shut off" and treated as empirically distinct from self-reputation, though acknowledged as complementary - integrating the two is left open. (4) The pure self-esteem vs. anticipatory-utility cases are shown to be qualitatively identical, but the hedonic-vs-functional distinction (which flips welfare conclusions) deserves fuller treatment. Suggested **further applications**: contracts and organizational design; and the political economy of reforms (trade opening, labor-market liberalization), where the binding constraint may be not whether winners can credibly compensate losers but that losers do not want to *see themselves*, or be seen, as losers dependent on "handouts."

## Connections
This is a compact companion to the authors' fuller program: Bénabou and Tirole (2002, "Self-Confidence and Personal Motivation"), (2004, "Willpower and Personal Rules"), (2006, "Incentives and Prosocial Behavior"; "Belief in a Just World"), and especially (2007, "Identity, Dignity and Taboos: Beliefs as Assets"), from which the framework is drawn. It dialogues with the identity economics of Akerlof and Kranton (2005) - here identity arises from cognitive belief management rather than chosen group membership, yielding the contrasting welfare result. The empirical backbone is the self-serving-bias bargaining experiments of Babcock, Loewenstein, Issacharoff, and Camerer (1995) and [[@Loewenstein1992|Thompson and Loewenstein (1992)]], and the fairness/wiggle-room evidence of Konow (2000) and Dana, Weber, and Kuang (2007). It sits adjacent to, but methodologically apart from, the heterogeneous-priors delay literature (Yildiz 2004; Ali 2006), where beliefs are exogenous rather than endogenously managed.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
