---
citekey: Peters2019
title: The ergodicity problem in economics
authors: ["Peters, Ole"]
year: 2019
type: journalArticle
doi: 10.1038/s41567-019-0732-0
zotero: "zotero://select/library/items/T5WMMSCL"
pdf: /Users/jesper/Zotero/storage/STXDW63G/Peters2019.pdf
tags: [literature]
keywords: [ergodicity-economics, expected-utility-theory, time-average-growth, non-ergodicity, geometric-brownian-motion, risk-aversion, st-petersburg-paradox]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> The ergodic hypothesis is a key analytical device of equilibrium statistical mechanics. It underlies the assumption that the time average and the expectation value of an observable are the same. Where it is valid, dynamical descriptions can often be replaced with much simpler probabilistic ones — time is essentially eliminated from the models. The conditions for validity are restrictive, even more so for non-equilibrium systems. Economics typically deals with systems far from equilibrium — specifically with models of growth. It may therefore come as a surprise to learn that the prevailing formulations of economic theory — expected utility theory and its descendants — make an indiscriminate assumption of ergodicity. This is largely because foundational concepts to do with risk and randomness originated in seventeenth-century economics, predating by some 200 years the concept of ergodicity, which arose in nineteenth-century physics. In this Perspective, I argue that by carefully addressing the question of ergodicity, many puzzles besetting the current economic formalism are resolved in a natural and empirically testable way.

## Summary
Peters argues that mainstream economics rests on a hidden, unjustified assumption of ergodicity: it treats the expectation value of wealth as if it told us what happens to an individual over time. Because wealth typically follows a non-ergodic (multiplicative) growth process, this is wrong, and the patch historically applied — concave utility functions justified by "psychology" — masks a physical error rather than fixing it. The proposed alternative, "ergodicity economics," replaces expectation-maximization with maximization of the time-average growth rate of wealth. This recovers expected-utility-like equations through a formal mapping (linear utility ↔ additive dynamics, logarithmic utility ↔ multiplicative dynamics) but reinterprets the "utility function" as a feature of the wealth *dynamic* rather than of the agent's psyche. A Copenhagen lab experiment in which the same subjects faced additive and multiplicative environments supports the dynamic interpretation: every subject became more risk-averse under multiplicative dynamics, as predicted.

## Research question
Is the time average of an economically relevant observable (notably wealth, or its growth rate) equal to its expectation value? More pointedly: when economic theory maximizes expected wealth or expected utility, is it computing the right object for an individual decision-maker who lives through time rather than across an ensemble? Peters asks whether explicitly posing this "ergodicity question" dissolves long-standing puzzles (St. Petersburg paradox, equity premium / volatility puzzle, the apparent need for psychological utility and discounting functions).

## Method / identification
This is a conceptual Perspective combined with one reported experiment. The formal core is the contrast between two ways of evaluating a gamble $\Delta x$ (a random wealth change). An observable $f$ is *ergodic* when it satisfies Birkhoff's equation,
$$\lim_{T\to\infty}\frac{1}{T}\int_0^T f(\omega(t))\,dt = \int_\Omega f(\omega)\,P(\omega)\,d\omega,$$
i.e. when its time average equals its expectation value. Peters builds ergodic observables for non-ergodic growth processes. Starting from the deterministic growth rate $g=\Delta v(x)/\Delta t$, where $v(x)$ is a monotonic transform chosen so $g$ is time-constant, he perturbs in $v$-space with constant-amplitude noise:
$$dv = \gamma\,dt + \sigma\,dW.$$
Integrating recovers Brownian motion for the additive case $v_a(x)=x$ and geometric Brownian motion for the multiplicative case $v_e(x)=\ln x$. The growth rate is then ergodic by construction even though wealth itself is not. The central theoretical result is the **mapping**: the appropriate growth rate equals the rate of change of a specific utility function,
$$g=\frac{\Delta v(x)}{\Delta t}=\frac{\Delta u(x)}{\Delta t},$$
and the time-average growth rate equals the rate of change of the expected utility — *because* the growth rate (not wealth) is ergodic. Thus expected utility theory "accidentally" constructed an ergodic observable two centuries before ergodicity was defined. The experimental design (the Copenhagen study, ref. 11) is a within-subject manipulation of the wealth dynamic: subjects start with ~\$150 and make 312 consequential choices in an additive environment (fixed dollar stakes) and 312 in a multiplicative environment (fixed proportional stakes). Choices are fit to the isoelastic utility $u(x;\eta)=\frac{x^{1-\eta}-1}{1-\eta}$ via a Bayesian hierarchical model that returns a posterior over the risk-aversion parameter $\eta$ for each person in each environment.

## Data
The experimental dataset (reproduced from Meder et al., ref. 11) comprises 11,232 individual binary choices — roughly 18 subjects × 2 environments × 312 choices. Each subject contributes a posterior density over $\eta$ in each environment (Fig. 3). The Outlook also cites empirical checks on stock indexes and bitcoin (growth-rate/volatility relationship), and on Bernie Madoff's fund as a fraud-detection example, but these are referenced rather than presented as new data here.

## Key findings
1. **The mapping theorem.** $g=\Delta v(x)/\Delta t=\Delta u(x)/\Delta t$: growth-rate optimization and expected-utility maximization yield formally near-identical equations, with $v_a=x\leftrightarrow$ linear utility and $v_e=\ln x\leftrightarrow$ logarithmic utility. The two frameworks coincide mathematically yet differ entirely conceptually.
2. **Dissolution of puzzles.** The St. Petersburg paradox disappears under the time-average treatment; the equity premium ("volatility") puzzle, discounting, and the shape of the wealth distribution are recovered as consequences of growth-rate maximization rather than as separate psychological or institutional add-ons. A standard inequality measure (Theil) equals the time-integrated gap between ensemble and time-average growth rates in geometric Brownian motion.
3. **Experimental discrimination.** All tested individuals shifted toward higher risk aversion ($\eta$) under multiplicative dynamics, with posteriors clustering near the null predictions $\eta\approx 0$ (additive) and $\eta\approx 1$ (multiplicative), and a change in $\eta$ of order 1 — the qualitative, directional, and magnitude predictions of ergodicity economics. This falsifies the expected-utility prediction that $\eta$ is a fixed personality trait insensitive to the dynamic.
4. **Reinterpretation of "irrationality."** Apparent risk aversion is not a quirk of psychology but the correct response to a multiplicative environment; the same agent looks "brave" ($v_a$) under additive and "scared" ($v_e$) under multiplicative dynamics. Observed cross-sectional differences may reflect differing circumstances, not differing utility.

## Contribution
Peters reframes a cluster of classical results — the geometric-vs-arithmetic-mean gap (Euclid, Jensen 1906), gambling/investment growth (Whitworth 1870, Itô 1944, Kelly 1956) — as a single question about ergodicity. The claimed novelty is not the mathematics of geometric means but the *perspective*: enforcing physical realism by forbidding interactions among ensemble members, allowing growth dynamics beyond additive/multiplicative, and supplying a "Homo ergodicus" null model that is more parsimonious and less reliant on idiosyncratic psychology than discounted expected utility. The paper positions growth-rate maximization as a replacement for, not a correction to, the expected-utility null model.

## Limitations & open questions
- Peters states a criticism of expected utility he is **"unable to resolve"**: expecting over an ensemble physically corresponds to pooling and sharing across many entities (or "copies of oneself in parallel universes"), which does not describe a lone decision-maker — open conceptually about when ensemble averaging is ever legitimate for an individual.
- The experiment's evidentiary weight is explicitly hedged: subjects had only a one-hour training phase, the 11,232 choices "may be happenstance," and "the experiment may be flawed in a way we don't yet understand."
- He concedes ergodicity economics is itself a **null model** with "all the shortcomings that null models have"; adding detail "would require careful checks against overfitting," leaving the boundary of the model's validity open.
- The general program — characterizing growth rates for arbitrary processes $v(x)=x_1^{(-1)}(x)$ beyond linear/log (e.g. sigmoidal biological growth) — is gestured at but not developed.
- Whether the reframing genuinely *predicts* (rather than redescribes) discounting, the equity premium, market stability, and inequality is asserted via preprints (refs. 18–22) rather than demonstrated in this article.

## Connections
The intellectual lineage runs from Cardano, the Fermat–Pascal correspondence (1654), Nicolas Bernoulli's St. Petersburg gamble (1713), and Daniel Bernoulli's logarithmic utility (1738), through von Neumann–Morgenstern's axiomatization (1944) and Samuelson's (1937) discounted-utility formalism. The time-average machinery connects to Kelly's (1956) criterion and the Itô calculus, and to Jensen's inequality. The companion technical paper is Peters & Gell-Mann, "Evaluating gambles using dynamics" (*Chaos*, 2016); the experiment is Meder et al. (2019). The broader research program (London Mathematical Laboratory / Santa Fe Institute) spans microfoundations of discounting (Adamou et al. 2019), the time interpretation of expected utility (Peters & Adamou 2018), leverage efficiency and the equity premium (Peters & Adamou 2011), cooperation as growth-optimal (Peters & Adamou 2018), and wealth-distribution models (Bouchaud & Mézard 2000; Marsili et al. 1998; Berman et al. 2017). The work sits in direct tension with behavioural economics' "human irrationality" narrative and with prospect theory's psychological framing of risk attitudes.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
