---
citekey: Masatlioglu2016
title: A Behavioral Analysis of Stochastic Reference Dependence
authors: ["Masatlioglu, Yusufcan", "Raymond, Collin"]
year: 2016
type: journalArticle
doi: 10.1257/aer.20140973
zotero: "zotero://select/library/items/8G4BVXVV"
pdf: /Users/jesper/Zotero/storage/NG7DRVEE/Masatlioglu2016.pdf
tags: [literature]
keywords: [reference-dependence, loss-aversion, rank-dependent-utility, choice-acclimating-personal-equilibrium, non-expected-utility, risk-preferences]
topics: []
related: [Abeler2011, Bell1985, Crawford2011, Gul1991, Heidhues2008, Kahneman1979, Koszegi2006b, Koszegi2007, Loomes1986, Pope2011, Quiggin1982, Sydnor2010, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We examine the reference-dependent risk preferences of [[@Koszegi2007|Koszegi and Rabin (2007)]], focusing on their choice-acclimating personal equilibria. Although their model has only a trivial intersection (expected utility) with other reference-dependent models, it has very strong connections with models that rely on different psychological intuitions. We prove that the intersection of rank-dependent utility and quadratic utility, two well-known generalizations of expected utility, is exactly monotone linear gain-loss choice-acclimating personal equilibria. We use these relationships to identify parameters of the model, discuss loss and risk aversion, and demonstrate new applications. (JEL D11, D81)

## Summary
This is a decision-theoretic paper that locates Koszegi and Rabin's (2007) choice-acclimating personal equilibrium (CPE) within the taxonomy of non-expected-utility theories. The central result is a representation equivalence: with linear gain-loss utility, the class of monotone CPE preferences coincides exactly with the intersection of rank-dependent utility (RDU) and quadratic utility (Q). This unexpected bridge means correct-beliefs-but-nonstandard-utility (CPE) is behaviorally identical to a form of distorted-beliefs-but-standard-utility (RDU). The authors exploit the equivalence to pin down the model's parameters, reinterpret loss aversion as pessimism / first-order risk aversion / mixture aversion, and show that CPE inherits a version of the Rabin (2000) calibration critique unless gain-loss utility is nonlinear.

## Research question
How does Koszegi and Rabin's (2007) CPE model of stochastic, expectations-based reference dependence relate, behaviorally, to other non-expected-utility models of choice under risk? In particular, can CPE be distinguished from other reference-dependent theories ([[@Bell1985|Bell 1985]]; [[@Loomes1986|Loomes and Sugden 1986]]; [[@Gul1991|Gul 1991]]) and from non-EU models grounded in different psychological intuitions (rank-dependent, quadratic, betweenness)? And what do the model's primitives $u$ and $\lambda$ actually mean in terms of observable behavior?

## Method / identification
Pure axiomatic / representation-theoretic analysis on the space $\Delta_X$ of simple lotteries over a money interval $X=[w,b]$. The CPE value of lottery $f$ is
$$V_{CPE}(f)=\sum_x u(x)f(x)+\sum_x\sum_y \mu\big(u(x)-u(y)\big)f(x)f(y),$$
with linear gain-loss kernel $\mu(z)=z$ for $z\ge 0$ and $\mu(z)=\lambda z$ for $z<0$, where $\lambda$ is the coefficient of loss aversion ($\lambda=1$ gives EU). The comparison classes are: quadratic preferences $V_Q(f)=\sum_x\sum_y \phi(x,y)f(x)f(y)$; rank-dependent utility $V_{RDU}$ with a strictly increasing weighting function $w:[0,1]\to[0,1]$, $w(0)=0,w(1)=1$; betweenness $V_B$; and Bell–Loomes–Sugden disappointment $V_{BLS}$. Proofs use the result of Chew, Epstein, and Segal (1991) characterizing first-order stochastic dominance (FOSD) for quadratic functionals, and a constructive argument (equal-probability lotteries dense in $\Delta_X$) to build the RDU weighting function. Comparative statics on $u$ and $\lambda$ are connected to second-order risk aversion (mean-preserving spreads), first-order risk aversion (via Segal and Spivak 1990), and the Rabin (2000) / Safra and Segal (2005) calibration apparatus. Section IV generalizes to a nonlinear gain-loss function $v$ (GCPE) with diminishing sensitivity ($v$ concave).

## Data
None - this is a theory paper. The authors note that the RDU equivalence (Theorem 1) lets researchers reuse over 20 years of existing experimental data designed to test RDU as tests of CPE, but they run no estimation themselves.

## Key findings
- **Proposition 1 (monotonicity):** a CPE preference respects FOSD iff $0\le\lambda\le 2$. Many applications set $\lambda>2$, which (with the linear form) makes preferences non-monotone.
- **Theorem 1 (main equivalence):** a preference has both a $Q$ and an RDU representation iff it has a monotone CPE representation. CPE is exactly $Q\cap RDU$.
- **Proposition 2 (identification):** for monotone CPE, $u$ is unique up to affine transformation and $\lambda$ is unique.
- **Proposition 3:** CPE satisfies mixture aversion iff $\lambda>1$ (mixture loving iff $\lambda<1$), a corollary of Wakker (1994).
- **Proposition 4 (loss aversion = pessimism):** any monotone CPE $(u,\lambda)$ has an RDU representation with weighting function $w_\lambda(z)=(2-\lambda)z+(\lambda-1)z^2$; for $\lambda\in[1,2]$ this is convex, so loss aversion is overweighting of bad outcomes.
- **Proposition 5 (distinctness):** a preference represented by both $V_{CPE}$ and $V_{BLS}$ (or $V_B$) must be EU - CPE intersects the other endogenous-reference models only at expected utility, because they differ in attitudes toward randomization.
- **Proposition 6 (risk aversion):** if $\lambda<1$ not risk-averse; if $1<\lambda<2$, risk-averse iff $u$ concave; if $\lambda>2$, risk-averse iff $u$ linear.
- **Proposition 7 (first-order risk aversion):** with $u$ everywhere differentiable, the DM is first-order risk-averse at all wealth levels iff $\lambda>1$ (loving iff $\lambda<1$), supporting Koszegi and Rabin (2005, 2007)'s reading of $\lambda$.
- **GCPE (Props 8–10):** with nonlinear $v$, FOSD holds iff $-1<(1-\lambda)v'(0)<1$; GCPE always admits a $Q$ representation but generally NOT an RDU one; indifference curves on the 3-outcome simplex are ellipses and mixture aversion still tracks $\lambda\gtrless 1$. Mean-variance preferences arise as the special case $v(z)=z^2$ with linear $u$.
- **Rabin critique (Section V):** monotone (linear-gain-loss) CPE inherits the Safra and Segal (2005) extension of the Rabin (2000) calibration critique; only nonlinear gain-loss utility can escape it.

## Contribution
Provides the first axiomatic-grade map of where CPE sits among non-EU theories, giving Koszegi and Rabin's model previously missing axiomatic foundations (via $Q$ and RDU). It supplies an identification result for $u$ and $\lambda$, reinterprets loss aversion simultaneously as probabilistic pessimism, first-order risk aversion, and mixture aversion, and clarifies that the various endogenous-reference-point models are empirically distinguishable essentially only through attitudes toward randomization (mixing). It also imports the Rabin calibration critique into the CPE setting and shows nonlinearity of gain-loss utility is the escape hatch.

## Limitations & open questions
- The clean RDU equivalence and the calibration result hold only for **linear** gain-loss utility; the nonlinear GCPE case loses the RDU toolkit (no RDU representation), and risk-aversion conditions there are hard to interpret/verify because they depend on global properties.
- The rank-dependent representation of CPE forces a **strictly convex** weighting function - a prediction the authors flag as at odds with much existing empirical evidence (e.g., Gonzalez and Wu 1999), inviting empirical testing.
- The authors single out **attitudes toward randomization / mixing** as "a potentially useful area of research" to distinguish models of reference-point formation, since most behaviors (small-stakes risk aversion) cannot separate them.
- Results assume uncertainty resolves later (so the chosen lottery becomes the reference point); behavior under immediate resolution is outside scope.
- On restricted domains (e.g., two-outcome certainty-equivalent elicitations common in experiments) CPE, Gul, and BLS all collapse into RDU, so much existing experimental data is uninformative for separating the models - a caution for calibration and a design challenge.

## Connections
Builds directly on [[@Koszegi2006b|Koszegi and Rabin]] (2006, 2007) and Bowman, Minehart, and Rabin (1999); the linear-gain-loss CPE form was independently derived by Delquie and Cillo (2006). The comparison classes draw on [[@Quiggin1982|Quiggin (1982)]] and Abdellaoui (2002) for rank-dependent utility; Machina (1982) and Chew, Epstein, and Segal (1991, 1994) for quadratic utility; and Chew (1989), Fishburn (1983), and Dekel (1986) for betweenness. The rival reference-dependent theories are [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes and Sugden (1986)]], and [[@Gul1991|Gul (1991)]]; foundational reference dependence traces to Markowitz (1952) and [[@Kahneman1979|Kahneman and Tversky (1979)]], with cumulative prospect theory from [[@Tversky1992|Tversky and Kahneman (1992)]]. The risk-attitude analysis uses Segal and Spivak (1990) on first-order risk aversion, Wakker (1994) on pessimism and mixture aversion, and the calibration critique of Rabin (2000) with the extension of Safra and Segal (2005) and the related RDU critique of Neilson (2001). Freeman (2012) characterizes Koszegi and Rabin's preferred personal equilibrium. Applications of the broader framework include [[@Heidhues2008|Heidhues and Koszegi]] (2008, 2014), [[@Sydnor2010|Sydnor (2010)]], Herweg, Muller, and Weinschenk (2010), [[@Abeler2011|Abeler et al. (2011)]], Card and Dahl (2011), [[@Crawford2011|Crawford and Meng (2011)]], [[@Pope2011|Pope and Schweitzer (2011)]], Carbajal and Ely (2012), Karle and Peitz (2014), and Eliaz and Spiegler (2014).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
