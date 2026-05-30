---
citekey: Bolton2000
title: "ERC: A Theory of Equity, Reciprocity, and Competition"
authors: ["Bolton, Gary E.", "Ockenfels, Axel"]
year: 2000
type: journalArticle
doi: 10.1257/aer.90.1.166
zotero: "zotero://select/library/items/J2VVQZTN"
pdf: /Users/jesper/Zotero/storage/73TMRN5G/Bolton2000.pdf
tags: [literature]
keywords: [social-preferences, inequity-aversion, relative-payoff, experimental-economics, ultimatum-game, reciprocity, bertrand-competition, behavioral-game-theory]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We demonstrate that a simple model, constructed on the premise that people are motivated by both their pecuniary payoff and their relative payoff standing, organizes a large and seemingly disparate set of laboratory observations as one consistent pattern. The model is incomplete information but nevertheless posed entirely in terms of directly observable variables. The model explains observations from games where equity is thought to be a factor, such as ultimatum and dictator, games where reciprocity is thought to play a role, such as the prisoner's dilemma and gift exchange, and games where competitive behavior is observed, such as Bertrand markets.

## Summary
This is the canonical "ERC" paper (Equity, Reciprocity, and Competition), one of the two foundational outcome-based social-preference models alongside Fehr-Schmidt inequity aversion. Bolton and Ockenfels posit that a player cares about both her own money and her *relative* share of the total pie, with a comparative term that peaks at the egalitarian split. With this single, parsimonious, incomplete-information apparatus — calibrated entirely on observable dictator/ultimatum thresholds — they reconcile behavior across equity games (dictator, ultimatum, impunity, best-shot), competitive markets (Bertrand, Cournot, auction), and reciprocity/dilemma games (PD, gift-exchange, investment) as one coherent pattern rather than disjoint behavioral regimes. I read the full extracted text (the PDF is a 163-page journal scan, but the article itself, pp. 166-189, was cleanly OCR'd: model, all four assumptions, Statements 1-13, the parametric fit, and the limitations section).

## Research question
Is there a *single* model of motivation that can simultaneously explain (i) equity/fairness in bargaining (positive offers and rejections in ultimatum, giving in dictator), (ii) competitive self-interest in markets (convergence to Nash/competitive prices), and (iii) reciprocity in dilemmas (conditional cooperation, wage-effort correlation)? Or are these distinct, unconnected "behavioral charts," each valid only on its own domain?

## Method / identification
The core is a **motivation function**. For an $n$-player game, player $i$ maximizes the expected value of
$$v_i = v_i(y_i,\sigma_i),$$
where $y_i\ge 0$ is own monetary payoff and $\sigma_i$ is the *relative share*
$$\sigma_i = \sigma_i(y_i,c,n) = \begin{cases} y_i/c & \text{if } c>0\\ 1/n & \text{if } c=0\end{cases},\qquad c=\sum_{j=1}^{n} y_j.$$
A player's payoff depends only on her *own* pecuniary and *own* relative payoff — not on the full distribution — which is what keeps the model coarse and tractable. Four assumptions discipline $v_i$:

- **A1 (Smoothness):** $v_i$ is continuous and twice differentiable.
- **A2 (Narrow self-interest):** $v_{i1}\ge 0$ and $v_{i11}\le 0$; fixing $\sigma$, more money is weakly preferred (and strictly chosen when payoffs differ). Note $v_i$ is *not* assumed strictly increasing in money, allowing pure relativists who split fifty-fifty.
- **A3 (Comparative effect):** $v_{i2}=0$ at $\sigma_i=1/n$ and $v_{i22}<0$ — i.e. $v_i$ is strictly concave in the relative share and peaks at the equal share. Equal division is thus the **social reference point**. (This rules out pure status-seeking, which would predict universal defection.)
- **A4 (Heterogeneity):** the full range of types is present in the population, with densities $f_r(r\mid c)>0$ on $[1/n,1]$ and $f_s(s\mid c)>0$ on $(0,1/n]$.

Heterogeneity is summarized by two **thresholds** recoverable directly from data: the dictator allocation $r_i(c)=\arg\max_{\sigma_i} v_i(c\sigma_i,\sigma_i)$ and the ultimatum rejection threshold $s_i(c)$ defined implicitly by $v_i(cs_i,s_i)=v_i(0,1/n)$ with $s_i\le 1/n$. For $n=2$, $r_i$ is what $i$ keeps in the dictator game and $s_i$ is $i$'s rejection cutoff in ultimatum. Crucially, types ($r$, $s$) are **private information** but their densities are common knowledge; equilibrium is **perfect Bayesian** (an "ERC equilibrium"). A worked **additively separable** example is used for illustration (not for proofs):
$$v_i(c\sigma_i,\sigma_i) = a_i c\sigma_i - \frac{b_i}{2}\left(\sigma_i - \frac{1}{2}\right)^2,\quad a_i\ge 0,\ b_i>0,$$
where the type is the single ratio $a_i/b_i$: $a/b=0$ is a strict relativist ($r=s=1/2$) and $a/b\to\infty$ is strict self-interest ($r\to 1$, $s\to 0$). For the dilemma/gift-exchange quantitative work, a one-parameter "$\alpha$-model" approximates the population as a fraction $\alpha$ of "relativists" (who minimize $\lvert u-\pi\rvert$, i.e. equalize payoffs) and $1-\alpha$ "egoists" (who maximize money).

## Data
None collected. The paper is purely theoretical/re-analytic: it derives comparative statics and then confronts them with **published** experimental datasets (Forsythe et al. 1994 dictator/ultimatum; Roth et al. 1991 four-country auction markets; Fehr et al. 1993 gift-exchange, generously shared by the authors; Berg et al. 1995 investment game; Bolton-Zwick 1995 impunity; Prasnikar-Roth 1992 best-shot; Cooper et al. 1996 and Andreoni-Miller 1993 PD). The Fehr et al. (1993) 276 wage-effort pairs are used to *fit* $\alpha$.

## Key findings
- **Statements 1-4 (Equity):** Dictators keep $\ge 1/2$ but on average give positive amounts ($1/2<\bar\sigma_D<1$). Ultimatum responders never reject the equal split, reject more as offers fall ($p$ strictly increasing in $\sigma_P$ over $(1/2,1)$), and rejection is non-increasing in cake size $c$. Ultimatum offers exceed dictator offers on average ($\bar\sigma_D>\bar\sigma_P$) — equity is partly *responder*-driven strategic anticipation, not just proposer altruism.
- **Statement 5 (Unknown pie):** With pie size uncertain, the rejection probability of a fixed offer lies *between* the known-small and known-large cases — matching Mitzkewitz-Nagel and Kagel et al.
- **Statements 6-7 (Impunity, best-shot):** ERC predicts more (3,1) outcomes and fewer rejections in impunity than ultimatum, and that best-shot moves toward but not to subgame-perfection — both borne out.
- **Statements 8-10 (Competition):** For Bertrand and Cournot, *all* Nash equilibria are ERC equilibria (deviating helps neither money nor relative standing since equilibria are symmetric). For large enough $n$, the competitive outcome is the *unique* ERC equilibrium in Bertrand and in the auction market (Statements 9, 9b) — **independent of the type distribution**, because one sufficiently self-interested undercutter suffices and everyone undercuts to protect relative position. Cournot duopoly has a unique pure-strategy ERC equilibrium equal to Nash (Statement 10), requiring only one player with $r_i(c)>1/2$; from dictator data ~80% qualify, implying ≥96% probability of the Nash outcome. ERC predicts asymmetric costs matter for Cournot but not Bertrand symmetry.
- **Reciprocity / dilemmas:** In sequential PD, cooperation requires *both* relativist second movers (tit-for-tat) *and* sufficiently money-motivated first movers willing to risk triggering cooperation; cooperation rises with the mpcr. The $\alpha$-model fits Fehr et al. (1993) gift-exchange closely (Statements 11-13: average effort, worker payoff increasing in wage; firm profit hump-shaped if $\alpha>\approx12\%$), yielding $\alpha\approx 0.5$. Strikingly, the **same $\alpha\approx0.42$-0.5** recurs in dictator giving (~0.23-0.27) and the Berg et al. (1995) investment game — strong out-of-sample robustness. ERC also rationalizes why reciprocity "paid" in gift-exchange (huge marginal efficiency gains) but investments lost money (factor-3 return needs $\alpha\ge0.5$ to break even), and why finitely repeated PD cooperation can persist (cooperative types genuinely exist, à la Kreps et al. 1982, but their proportion is endogenous to payoffs).

## Contribution
ERC is one of the two reference points (with Fehr-Schmidt 1999) for the entire literature on outcome-based / distributional social preferences. Its distinctive moves: (1) a deliberately *coarse* preference over one's *own relative share* rather than the full payoff vector, which is enough to dismiss strict egalitarianism (e.g. Güth-van Damme's dummy player gets nothing; the solidarity game); (2) genuine *incomplete information* with privately known types, matching anonymous lab conditions; (3) parameters that are *directly observable* from dictator and ultimatum thresholds, making the model falsifiable; and (4) a unification claim spanning fairness, competition, and reciprocity within one framework — including a clean account of why *markets* discipline self-interest while *bargaining* does not.

## Limitations & open questions
The authors are unusually explicit (Section VII):
- ERC is a theory of **local behavior** — stationary patterns in simple games, short time spans, constant frame. It is **static**: incorporating *learning* needs a dynamic theory; more complex games likely need **bounded-rationality** solution concepts; long horizons need age/experience effects on goals.
- ERC **omits intentions/reciprocity-of-type**. The authors concede experiments find evidence for intentions (Blount 1995; Kagel et al.; Charness 1996) that ERC, being purely outcome-based, cannot capture.
- The **social reference point (50-50) is "perhaps too simple."** When the equal split is made infeasible (e.g. all 60-40 to 40-60 splits removed), it is unclear what reference point people adopt; better data are needed for a more systematic reference point.
- The **appropriate reference group** is obvious in these lab games but not in richer social environments — an open modeling question.
- *Why* do people care about relative standing at all? The authors speculate (evolutionary biology, small-group living, punishment of free-riders) but leave this unresolved, pointing to evolutionary models (Güth 1995; Ellingsen 1997).
- The recurring $\alpha\approx0.5$ and the threshold stability across frames/cultures are flagged as the key empirical regularities a future *quantitative* ERC should explain — explicitly "requires new data."

## Connections
Directly compared in Section I to the other motivation models: **Rabin (1993)** fairness equilibrium (intentions-based, two-person complete-info — hard to extend to markets/incomplete info); **Levine (1998)** spite/altruism types (fails the dictator game); **Fehr-Schmidt (1999)** inequity aversion (the closest rival — also outcome-based, but penalizes deviation from each opponent's payoff rather than only own relative share, and is mostly complete-information); and Bolton's own (1991) complete-information comparative model, of which ERC is the incomplete-information generalization. ERC treats **learning models** (Roth-Erev 1995) as complementary rather than competing. Downstream, ERC and Fehr-Schmidt jointly anchor the debate between *distributional* and *intention-based* (reciprocity) preference models, later probed by Charness-Rabin (2002) and Falk-Fischbacher reciprocity theory; the markets-discipline-self-interest result connects to the experimental industrial-organization and market-design literature.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
