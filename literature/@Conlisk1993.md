---
citekey: Conlisk1993
title: The utility of gambling
authors: ["Conlisk, John"]
year: 1993
type: journalArticle
doi: 10.1007/BF01072614
zotero: "zotero://select/library/items/DTT7QXE3"
pdf: /Users/jesper/Zotero/storage/WFA3YR2R/Conlisk1993.pdf
tags: [literature]
keywords: [utility-of-gambling, expected-utility, risk-seeking, insurance-and-gambling, decision-under-risk, prospect-theory, reference-dependence]
topics: ["[[prospect-theory-loss-aversion]]"]
related: [Kahneman1979, Loewenstein1987]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A tiny utility of gambling is appended to an expected utility model for a risk-averse individual. It is shown that the model can explain small payoff gambles, large prize lotteries, and patterns of risk-seeking in the experimental evidence that are puzzling from the viewpoint of standard theory. At the same time, the model maintains expected utility theory's ability to explain insurance purchase, portfolio diversification, and other risk-averting behavior. The tiny utility of gambling could equally well be appended to models of risky choice other than the expected utility model.

## Summary
Conlisk argues that standard wealth-only theories of risky choice (Friedman–Savage, Markowitz, prospect theory, Machina) explain simultaneous insuring and gambling only for narrow, finely-tuned payoff structures. He instead appends a small, separable "utility of gambling" term $\epsilon V(G,p)$ to an otherwise standard expected-utility model for a strictly risk-averse agent. Because smooth utility is locally risk-neutral, the risk-aversion motive against a small fair bet is second-order small while the gambling term is first-order small, so *any* positive $\epsilon$ makes some gambles acceptable. Yet for large stakes the concave wealth utility dominates and the agent behaves risk-aversely (buys insurance, diversifies). The model thus reconciles widespread small-stakes risk-seeking with large-stakes risk aversion, and yields testable comparative-statics predictions that match existing experiments.

## Research question
Can the simultaneous willingness to pay to *reduce* risk (insurance, diversification) and to *increase* risk (gambling, lotteries) be explained without the strained "wiggles" in the wealth-utility function required by Friedman–Savage, Markowitz, prospect theory, and Machina-style theories? Conlisk's hypothesis: gambling confers direct utility from the pleasure of participation, and only a *tiny* amount of such utility is needed.

## Method / identification
Pure decision theory; no estimation. The agent faces a binary fair prospect: gain $G$ with probability $p$, loss $L=Gp/(1-p)$ with probability $1-p$, so that $pG-(1-p)L=0$. Because $p$ is monotone in the gain-to-loss ratio, $(G,p)$ encode the *size* and *skewness* of the bet. The **Fair Prospect Model** preference value of accepting is
$$E(G,p,K)=pU[K+G]+(1-p)U\left[K-\frac{Gp}{1-p}\right]+\epsilon V(G,p),$$
with the agent accepting iff $E(G,p,K)>E(0,0,K)=U(K)$. The wealth utility satisfies $U(0)=0$, $U'>0$, $U''<0$, $U<U_\infty<\infty$. The gambling term $\epsilon V(G,p)$ is continuous, with $V(0,p)=V(G,0)=0$, $V_1>0$, $V_{11}<0$, $V_2(G,0)>0$, and bounded above; $\epsilon>0$ scales its smallness. The gambling term is always present but may be overwhelmed by the EU terms, avoiding any need to label prospects "gambles" vs. "nongambles." Conlisk offers several candidate "excitement" functions $\sigma(G,p)$ with $V(G,p)=\bar V[\sigma(G,p)]$: standard deviation $\sigma=(GL)^{0.5}$, mean absolute deviation $\sigma=pG$, Cobb–Douglas $\sigma=G^\alpha L^{1-\alpha}$, a "fantasy expectation" $\sigma=\lambda p/(1-p)$ (playacting at influencing the odds), and Luce-style risk measures. Extensions handle multiple alternatives, multiple outcomes (via a Machina local-utility-function argument restoring the concavity–rejection link), and unfair prospects (decompose into a sure expected-value payment added to $K$ plus a fair bet about it — the **Unfair Prospect Model**, appendix C). Proofs analyze the benefit function $b(G)=E(G,p,K)-U(K)$ via its derivatives at the origin.

## Data
None for estimation — this is a theory paper. Conlisk does cite descriptive evidence: the Kallick et al. (1979) Survey of American Gambling (61% of adults bet in 1974; ~2% of personal income wagered; pleasure dominates the financial motive; most betting is small-payoff, not lotteries), and existing risky-choice experiments (Hershey–Kunreuther–Schoemaker 1982; Battalio–Kagel–Jiranyakul 1990; Hershey–Schoemaker 1980b, 1985) used to test the model's predictions. He also reports a small classroom experiment ($\$1$ sure vs. a fair coin flip for $\$2$): 63% and 55% of students chose the risky option.

## Key findings
- **Small Gamble Theorem.** Fixing $p$ and varying size $G$: the agent accepts small enough prospects for *any* $\epsilon>0$. If $\epsilon$ is small (inequality (7): $\epsilon\le[U(K)-pU(K/p)]/V[K(1-p)/p,\,p]$), there is a cutoff $C(K)$ such that $E>U(K)$ iff $0<G<C(K)$, and a unique most-preferred size $M(K)$ with $0<M(K)<C(K)$. Under declining absolute risk aversion ($U'''>0$), both $C(K)$ and $M(K)$ rise with wealth $K$. Mechanism: local risk neutrality makes $b''(0)$ (risk aversion) second-order while $b'(0)=\epsilon V_1(0,p)>0$ (gambling) is first-order.
- **Lottery Theorem.** If $\epsilon$ is not too small (condition (8): $\epsilon>GU'(K)/V_2(G,0)$ for all $G>0$), then for *any* gain $G$, however large, there is a threshold $D$ such that the agent accepts the lottery whenever $0<p<D$. For excitement functions of the form $V[Gf(p)]$ with $f'(0)=\infty$ (e.g. SD and Cobb–Douglas specs), condition (8) collapses to simply $\epsilon>0$.
- The model **predicts %RA (percent risk-averse) rises with $G$** for fixed $p$ in fair bets and in favorable unfair bets; Conlisk shows this monotone pattern holds across every Hershey et al. and Battalio et al. dataset he tabulates (e.g., $p=.01$: %RA climbs 16→35→60→70→81 as $G$ goes $100$→$10^6$).

## Contribution
Provides what Conlisk calls the literature's first non-peculiar formal model of a utility of gambling (contrasting Fishburn 1980, who let it affect only sure-vs-risky choices). It explains a *broad* range of simultaneous insuring and gambling — not just knife-edge magnitudes — while preserving EU's account of risk aversion at large stakes. It offers an alternative microfoundation for Markowitz-style reference dependence (gambling utility is defined over payoffs $(G,-L)$, wealth utility over final levels $(K+G,K-L)$). Crucially, it warns that if experimental subjects treat lab choices as gambling, prevailing risk-attitude interpretations of those experiments are confounded. The mechanism is modular — attachable to prospect theory or Machina's generalized EU, not only to EU.

## Limitations & open questions
- The $V$ function risks the very "abuse" Conlisk warns of: rigging the excitement function could fit almost anything (he explicitly declines to push the model onto the Allais paradox, calling such a fitted $V$ "artificial").
- The model is **static**: anticipation/suspense and time-to-resolution — central to gambling's appeal and to the excitement interpretation of $\epsilon V$ — are not explicitly modeled.
- For most unfair-prospect variations the predicted sensitivity of %RA is **ambiguous**, so the model cannot be tested against most existing experiments; only the favorable $(G,0,p)$ variation gives a sharp prediction.
- Assumption (c) of appendix C (at most one positive root of $b(G)=0$, ruling out multiple crossings) is stated inelegantly in terms of $b$ rather than primitives; no clean primitive condition is given.
- Very few experiments directly test the core fair-bet prediction (Conlisk found only two), inviting purpose-built experimental work.
- Whether the model can be empirically separated from prospect theory and Machina's theory is left open.

## Connections
The paper is framed against Friedman & Savage (1948) and Markowitz (1952), whose wiggly utility-of-wealth functions it seeks to replace, and against the skeptical remarks of Arrow (1951, 1974), Hirshleifer (1966), and Samuelson (1952), who anticipated the anticipation/suspense channel. It positions itself relative to [[@Kahneman1979|Kahneman & Tversky (1979)]] prospect theory and Machina (1982, 1987) generalized expected utility, arguing both explain joint insuring/gambling only for limited magnitudes, and uses Machina's local-utility-function method for the multiple-outcome extension. Fishburn (1980) is the closest prior formal utility-of-gambling model. Alternative "no-wiggle" devices appear in Ng (1965), Flemming (1969), Hakansson (1970), Kim (1973), Applebaum & Katz (1981), and Eden (1977, 1979, 1980); Landesberger & Meilijson (1990) study star-shaped utilities. The excitement specifications draw on Pollatsek & Tversky (1970), Luce (1980, 1981), and Luce & Weber (1986); anticipation utility connects to Pope (1983) and [[@Loewenstein1987|Loewenstein (1987)]]. Empirical testing relies on Battalio, Kagel & Jiranyakul (1990), Camerer (1989a, 1989b), Hershey & Schoemaker (1980b, 1985), Hershey, Kunreuther & Schoemaker (1982), and the Kallick et al. (1979) gambling survey; Heath & Tversky (1991) supply the illusion-of-control discussion.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
