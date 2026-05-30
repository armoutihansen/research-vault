---
citekey: Sarver2012
title: Optimal Reference Points and Anticipation
authors: ["Sarver, Todd"]
year: 2012
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/4F2TH9IE"
pdf: /Users/jesper/Zotero/storage/2KJFFT7E/Sarver2012.pdf
tags: [literature]
keywords: [reference-dependent-utility, loss-aversion, anticipatory-utility, recursive-utility, equity-premium-puzzle, first-order-risk-aversion, decision-theory, epstein-zin]
topics: []
related: [Benartzi1995, Gul1991, Kahneman1979, Koszegi2006b]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper considers a model of reference-dependent utility in which the individual makes a conscious choice of her reference point for future consumption. The model incorporates the combination of loss aversion and anticipatory utility as competing forces in the determination of the optimal reference point: anticipating better outcomes boosts current utility but also raises the reference level for future consumption, making the individual more susceptible to losses. A central focus of the paper is on the implications of this model of Optimal Anticipation for attitudes toward risk in dynamic environments. The main representation is formulated in an infinite-horizon framework, and axiomatic foundations are provided. I also describe special cases and show in particular that recursive expected utility in the sense of Epstein and Zin (1989) and Kreps and Porteus (1978) can be reinterpreted in terms of optimal anticipation and loss aversion. Finally, I describe a homogeneous version of the model and apply it to a portfolio choice problem. I show that asset pricing for the Optimal Anticipation model is based on simple modifications of standard Euler equations. While maintaining tractability, this model is rich enough to permit first-order risk aversion and can overcome several deficits of standard expected utility, such as the equity premium puzzle and Rabin's paradox.

## Summary

Sarver proposes a third approach to reference-point formation in reference-dependent utility — *optimal anticipation* — alongside the history-dependent (Benartzi–Thaler) and expectations-based (Kőszegi–Rabin) approaches. The agent freely chooses her reference point (her "anticipation") for next-period consumption, trading off **anticipatory utility** (looking forward to good outcomes boosts current utility) against **loss aversion** (a higher reference point makes shortfalls more painful). This trade-off endogenously generates extra, often first-order, risk aversion. The model is given an axiomatic foundation in an infinite-horizon recursive (Epstein–Zin) framework, nests Kreps–Porteus expected utility as a special case, and yields modified Euler equations that resolve the equity premium puzzle, the risk-free rate puzzle, and Rabin's paradox while keeping the risk-free rate independent of the loss-aversion parameters.

## Research question

Where do reference points come from, and what are the consequences of treating them as a *deliberate, optimal choice* rather than as fixed by history or pinned down by rational expectations? Specifically: if an individual optimally chooses how much to "look forward to" future consumption, balancing anticipatory utility against loss aversion, what restrictions does this place on dynamic risk attitudes, and can the resulting model overcome the empirical failures of additively-separable expected utility?

## Method / identification

The paper is decision-theoretic / axiomatic. The two-period Optimal Anticipation representation is
$$u_t(c_t) + \beta \sup_{\phi\in\Phi} E_t\big[\phi(u_{t+1}(c_{t+1}))\big],$$
where $\Phi$ is a (possibly non-parametric) collection of nondecreasing gain-loss functions $\phi:\mathbb{R}\to\mathbb{R}$ satisfying the normalization $\sup_{\phi\in\Phi}\phi(u)=u$ for all $u$. This normalization guarantees the model collapses to standard additively-separable utility $u_t(c_t)+\beta u_{t+1}(c_{t+1})$ under deterministic consumption, while $\sup_\phi E_t[\phi(\cdot)]\le E_t[\sup_\phi\phi(\cdot)]=E_t[u_{t+1}]$ implies (weakly) higher risk aversion than expected utility under risk.

A leading parametric case is the **linear gain-loss function**
$$\phi(u\mid\gamma)=\gamma+\begin{cases}\lambda^l(u-\gamma) & \text{if } u<\gamma\\ \lambda^g(u-\gamma) & \text{if } u\ge\gamma,\end{cases}$$
with $\lambda^l\ge\lambda^g\ge 0$; standard expected utility is $\lambda^l=\lambda^g=1$, and the kink at $\gamma$ delivers **first-order risk aversion** in the sense of Segal–Spivak. A second is the **exponential gain-loss function** $\phi(u\mid\gamma)=\gamma+\frac1\theta-\frac1\theta\exp(-\theta(u-\gamma))$.

Identification rests on a recursive value function and seven axioms over preferences $\succeq$ on consumption-lottery pairs $(c,m)$. Axioms 1–3 (Weak Order, Nontriviality, Continuity) and Axiom 4 (Stationarity) are standard for recursive utility; Axiom 5 (Separability, applying Debreu's condition to today/tomorrow/lottery triples) and Axiom 6 (FOSD) deliver additive separability and monotonicity. The key behavioral axiom is **Axiom 7 (Convexity)**: making a better outcome *certain* (rather than merely more probable) yields a weakly larger utility gain, because the individual can then target her anticipation precisely. Convexity in $m$ is what encodes the "optimal anticipation" supremum structure via duality.

## Data

None — this is a theory paper. The only empirical inputs are the standard calibration targets used for illustration: the 1889–1978 US equity premium (~6%), equity return volatility (~16%), implied Sharpe ratio ~0.375 (postwar ~0.5), and consumption-growth volatility (~3.6%, postwar ~1%), drawn from Mehra–Prescott and Campbell, to demonstrate that the model can match Hansen–Jagannathan bounds.

## Key findings

- **Theorem 1 (Existence):** For $\beta\in(0,1)$, continuous nonconstant $u$, and a suitable family $\Phi$, a bounded lower-semicontinuous value function $V$ satisfying the recursion exists; the range of $V$ is determined by the range of $u$ (the interval $I=[a/(1-\beta),\,b/(1-\beta)]$).
- **Theorem 2 (Representation):** $\succeq$ satisfies Axioms 1–7 **iff** it admits an Optimal Anticipation representation $(V,u,\Phi,\beta)$.
- **Theorem 3 (Uniqueness):** Two representations coincide iff $\beta_1=\beta_2$ and $u,V$ agree up to a common positive affine transformation (with a corresponding transformation of $\Phi$).
- **Theorem 4 (Quantile rule):** For continuous $c_{t+1}$, the optimal anticipation $\gamma^*$ for the linear gain-loss function is the quantile $\Pr[u_{t+1}(c_{t+1})\le\gamma^*]=\frac{1-\lambda^g}{\lambda^l-\lambda^g}$.
- **Theorem 5 (EZKP equivalence):** For differentiable concave $h$ with $h'>0$, $h^{-1}(E_m[h(V)])=\max_\gamma E_m[\frac{h(V)}{h'(\gamma)}-\frac{h(\gamma)}{h'(\gamma)}+\gamma]$, maximized at $\gamma=h^{-1}(E_m[h(V)])$. As a corollary, **Epstein–Zin–Kreps–Porteus recursive expected utility is a special case of Optimal Anticipation**; e.g. the exponential gain-loss case equals Kreps–Porteus utility with an exp/log certainty equivalent.
- **Asset pricing:** The optimal-anticipation Euler equation is a simple modification of the standard one — for the linear case, the stochastic discount factor becomes $M_{t+1}=\beta(\lambda^g+(\lambda^l-\lambda^g)\mathbf{1}[c_{t+1}\le\gamma^*])$. With $\lambda^l=1+\kappa$, $\lambda^g=1-\kappa$, the Hansen–Jagannathan ratio is exactly $\kappa$, so $\kappa\ge 0.5$ matches the data; crucially $E_t(M_{t+1})=\beta$, so the **risk-free rate $r^f=1/\beta$ is independent of $\lambda^l,\lambda^g$** — matching the equity premium does *not* force up the risk-free rate.
- **Theorems 6–7 (Homotheticity):** Both gain-loss families combined with CES/log $u$ deliver homothetic preferences and (often) a unique, continuous value function, enabling tractable portfolio-choice and asset-pricing applications.

## Contribution

A novel, axiomatically-grounded theory of reference-point formation by *optimization*, distinct from history- and expectations-based approaches: the reference point is unconstrained and chosen by the agent, who therefore always *could* "prepare for the worst" but generally chooses not to, in order to enjoy anticipatory utility. The framework (i) micro-founds first-order risk aversion, (ii) reinterprets Epstein–Zin–Kreps–Porteus utility as reduced-form optimal anticipation plus loss aversion, giving a behavioral reading of the exp/log transforms, and (iii) resolves the equity premium, risk-free rate, Allais, and Rabin puzzles within a tractable recursive model whose pricing conditions only mildly generalize standard Euler equations.

## Limitations & open questions

- **Theorem 1 gaps (explicit):** existence of $V$ is not accompanied by *uniqueness* or *continuity* — only lower semicontinuity. Strengthening this in the general (non-homothetic) case is "left as an interesting open question for future research."
- **Calibration is incomplete (explicit):** "Expanding the analysis to obtain more complete qualitative predictions for asset prices and performing a calibration exercise to check the quantitative predictions of the model are the subject of ongoing research."
- The Hansen–Jagannathan bound is only a lower bound, so the required loss-aversion parameter $\kappa$ may need to exceed the illustrative $0.5$ if the SDF and excess returns are not perfectly negatively correlated.
- The model takes the anticipation technology $\Phi$ as primitive; what disciplines or estimates $\Phi$ empirically, and whether anticipation choices are observable, is left open.

## Connections

Builds directly on the recursive-utility machinery of **Epstein–Zin (1989)** and **Kreps–Porteus (1978)** (and Weil 1989/1990), which it nests and reinterprets. It is positioned against the two dominant reference-point theories: **history-dependent** formation ([[@Benartzi1995|Benartzi–Thaler 1995]]; Barberis–Huang–Santos 2001) and expectations-based formation (**Kőszegi–[[@Koszegi2006b|Rabin 2006]], 2007**). Loss aversion and gains/losses trace to **Markowitz (1952)** and **[[@Kahneman1979|Kahneman–Tversky (1979)]]**; the kink delivers first-order risk aversion à la **Segal–Spivak (1990)**. The asset-pricing puzzles addressed are Mehra–Prescott's equity premium, Weil's risk-free rate puzzle, and **Rabin (2000)**'s calibration paradox. The local-expected-utility reading of $\phi\circ u_{t+1}$ connects to **Machina (1982, 1984)**, and the paper relates the representation to **betweenness** preferences (Chew 1983; Dekel 1986), [[@Gul1991|Gul (1991)]] disappointment aversion, and to the induced-preference literature (Kreps–Porteus 1979; Ergin–Sarver 2011). Marinacci–Montrucchio (2010) supply the fixed-point results for the homothetic value function.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
