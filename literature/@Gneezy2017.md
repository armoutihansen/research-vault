---
citekey: Gneezy2017
title: The Limits of Expectations-Based Reference Dependence
authors: ["Gneezy, Uri", "Goette, Lorenz", "Sprenger, Charles", "Zimmermann, Florian"]
year: 2017
type: journalArticle
doi: 10.1093/jeea/jvw020
zotero: "zotero://select/library/items/NTNNPSAF"
pdf: /Users/jesper/Zotero/storage/FIK6PM2T/Gneezy2017.pdf
tags: [literature]
keywords: [reference-dependence, expectations, loss-aversion, real-effort-experiment, koszegi-rabin, nonmonotonicity]
topics: ["[[expectations-based-reference-dependence]]"]
related: [Abeler2011, Bell1985, Benartzi1995, Crawford2011, Gul1991, Heidhues2008, Kahneman1979, Koszegi2006b, Loomes1986, Shalev2000]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Theories of expectations-based reference-dependent preferences have provided a critical modeling innovation, incorporating a structured theory of the formation of reference points. An important prediction of these models is a monotone response in behavior to changes in expectations. To test such models we conduct a real-effort experiment manipulating expectations and examining consequences on effort provision. In contrast to the theory, we document substantial nonmonotonicities in the effort response to changing expectations. Our results provide some evidence on the limitations of expectations-based reference dependence. (JEL: D81, D84, D12, D03)

## Summary

Gneezy, Goette, Sprenger, and Zimmermann put expectations-based reference dependence (the Kőszegi–Rabin program) to a stricter test than the supportive prior literature. Building on the real-effort design of [[@Abeler2011|Abeler et al. (2011)]], they manipulate the *level* and the *probability* of stochastic outside payments while holding the neoclassical incentive (expected piece-rate wage) fixed. The theory predicts effort responds *monotonically* to these expectation shifts. Instead the authors document pronounced **U-shaped (nonmonotone)** effort responses: lowering a fixed payment to $0 *raises* effort relative to $3, and increasing the probability of a high outcome *lowers* effort before it rebounds. These departures falsify the model's central comparative-static predictions while replicating Abeler et al.'s result over the positive-payment range.

## Research question

Do expectations-based reference-dependent preferences correctly predict the *direction* (monotonicity) of effort responses when expectations over outside payments are manipulated along dimensions—zero payments and payment probabilities—that leave neoclassical incentives unchanged?

## Method / identification

A real-effort lab experiment (UCSD Rady Behavioral Lab, z-Tree) with nine between-subject treatments, each indexed by a vector $(p,q,H,L)$. Stage 2 earnings: with probability $p$ a high fixed payment $H$ (effort-independent), with probability $q$ a low fixed payment $L<H$ (effort-independent), and with probability $1-p-q=0.5$ a piece rate $w=\$0.20$ per table solved. Crucially, uncertainty is resolved only *after* the subject stops working, so during the task subjects hold only expectations; the effort measure is Accumulated Earnings $we^{\*}$ at the stopping point.

The neoclassical benchmark uses additively separable, linear-in-earnings utility:
$$U(e)=(1-p-q)\,we+pH+qL-c(e),$$
with strictly convex $c(e)$ ($c'>0$, $c''>0$). The optimum equates marginal cost to the neoclassical marginal benefit $MB_S=(1-p-q)w=c'(e)$. Since $L$ and $H$ are paid only in effort-irrelevant states, the standard model (and any *status-quo* reference model) predicts $\partial e^{\*}/\partial L=0$ and $(\partial e^{\*}/\partial p)_{1-p-q}=0$.

Under Kőszegi–Rabin (KR) expectations-based preferences with a stochastic reference distribution, total utility integrates gain–loss comparisons of each outcome against each expected referent:
$$U(e)=p\,E[u(e\mid H)]+q\,E[u(e\mid L)]+(1-p-q)\,E[u(e\mid we)]-c(e),$$
with reference-dependent utility $u(x\mid r)=m(x)+\mu(m(x)-m(r))$, $m$ linear, and piecewise-linear gain–loss utility
$$\mu(y)=\begin{cases}\eta\,y & \text{if } y\ge 0,\\ \eta\,\lambda\,y & \text{if } y<0,\end{cases}$$
where $\lambda>1$ is loss aversion. This induces *kinks* in the marginal benefit of effort at $e=L/w$ and $e=H/w$. The authors adopt the "Choice-Acclimating Personal Equilibrium" (CPE) solution concept and derive two signed predictions for a convex cost: $\partial e^{\*}/\partial L\ge 0$ and $(\partial e^{\*}/\partial p)_{1-p-q}\ge 0$. Online Appendix robustness covers diminishing sensitivity, Personal Equilibrium (PE) with its multiplicity, a stopping-problem refinement, and the [[@Bell1985|Bell (1985)]] / [[@Loomes1986|Loomes–Sugden (1986)]] disappointment-aversion formulation—all preserving monotonicity. Estimation: OLS of Accumulated Earnings on treatment indicators with robust standard errors, plus Ranksum tests, controlling for productivity, time of day, demographics, quarter, and envelope implementation.

## Data

Original experimental data: 265 subjects across nine treatments (29–30 each), run Spring 2011, Fall 2011, Winter 2012. Stage 1 (4-min paid practice counting zeros in tables of 150 binary digits) measures productivity; Stage 2 is the free-stopping effort task. Outside-payment uncertainty implemented physically via two or eight sealed envelopes. Across all treatments subjects solved 39.64 tables on average ($7.93 accumulated, 33.30 min worked).

## Key findings

- **Prediction 1 (effort increasing in $L$):** Replicating [[@Abeler2011|Abeler et al. (2011)]], effort rises from $L=\$3$ to $L=\$7$ (stopping at $9.08 vs. $2.59 lower; Ranksum $z=2.24$, $p<0.05$). But at $L=\$0$ effort is *higher* than at $L=\$3$ (difference $\approx\$2.97$, $z=1.90$, $p<0.10$), tracing a U-shape. **Result 1: the monotone increase in effort in $L$ is rejected.** The violation occurs exactly at $L=0$, where KR predicts only negative gain-loss incentives—suggesting the $0 payment is *ignored* rather than treated as a binding low referent (also contradicting a value-inference/signaling reading à la Ericson and Fuster 2011).
- **Prediction 2 (effort increasing in $p$, fixing $1-p-q$, with $H=14$, $L=0$):** Effort is again U-shaped in $p$, falling to a minimum at $(0.25,0.25,14,0)$—subjects work about *half* as much when the outside payment is a 50–50 gamble over $0 and $14 as when it is $0 for sure or $14 for sure—then rebounding. **Result 2: no support for a monotone increase in effort in $p$.** Neoclassical zero-difference null strongly rejected (e.g., $F(4,165)=4.53$, $p<0.01$).
- Together the data are inconsistent with neoclassical preferences, standard prospect theory, *and* expectations-based reference dependence.

## Contribution

The paper sharpens the empirical test of the KR program by exploiting design margins ($L=0$ and probability variation) that hold neoclassical incentives constant yet generate clean KR comparative statics. Where prior lab evidence ([[@Abeler2011|Abeler et al. 2011]]; Ericson and Fuster 2011; Gill and Prowse 2012; Banerji and Gupta 2014) was supportive, this study isolates *falsifying* nonmonotonicities, demonstrating that fixed payments shape reference points in ways more complex than expectations-based formation alone captures. It is an explicit Popperian falsification exercise that constrains future theory.

## Limitations & open questions

The authors are candid that they offer **no full theoretical account** for the nonmonotonicities. They flag two project-idea hooks: (i) *zero/low payments appear to be ignored*—suggesting reference points may require an outcome that is "not immediately surpassed" to be attended to, i.e., a constraint on which expectations become referents; and (ii) *residual uncertainty is discouraging*—when certainty cannot be attained by tuning effort (as in the 50–50 $0/$14 condition), effort collapses, resonating with the Gneezy, List, and Wu (2006) "uncertainty effect." The unifying conjecture is that the **available set of actions and the attainable outcome distribution** jointly determine what is held as a referent and how strongly losses are felt. Future research linking reference dependence to choice sets—experimentally varying available actions and tracing reference-dependent responses—is proposed as the promising avenue.

## Connections

The design directly extends [[@Abeler2011|Abeler, Falk, Goette, and Huffman (2011)]] on reference points and effort provision. The theoretical backbone is Kőszegi and [[@Koszegi2006b|Rabin]] (2006, 2007) expectations-based reference dependence, with the CPE/PE equilibrium concepts and the broader lineage of disappointment aversion in [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes and Sugden (1986)]], [[@Gul1991|Gul (1991)]], and [[@Shalev2000|Shalev (2000)]] loss-aversion equilibrium. It situates against supportive lab tests—Ericson and Fuster (2011), Gill and Prowse (2012), Banerji and Gupta (2014), Heffetz and List (2014)—and contrary exchange evidence in Goette, Harms, and Sprenger (2014) and Smith (2012). Applications cited include the disposition effect (Shefrin and Statman 1985; Odean 1998), housing (Genesove and Mayer 2001), the endowment effect (Kahneman, Knetsch, and Thaler 1990), the equity premium ([[@Benartzi1995|Benartzi and Thaler 1995]]; Barberis, Huang, and Thaler 2006), cab-driver labor supply (Camerer, Babcock, Loewenstein, and Thaler 1997; Fehr and Goette 2007; [[@Crawford2011|Crawford and Meng 2011]]), and contracting (Herweg, Müller, and Weinschenk 2010; Kőszegi and [[@Heidhues2008|Heidhues 2008]]). The uncertainty-effect link is to Gneezy, List, and Wu (2006); foundations trace to [[@Kahneman1979|Kahneman and Tversky (1979)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
