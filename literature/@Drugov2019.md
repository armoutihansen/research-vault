---
citekey: Drugov2019
title: "Vague lies and lax standards of proof: On the law and economics of advice"
authors: ["Drugov, Mikhail", "Troya‐Martinez, Marta"]
year: 2019
type: journalArticle
doi: 10.1111/jems.12279
zotero: "zotero://select/library/items/8ZKG37I8"
pdf: /Users/jesper/Zotero/storage/EIWAARUP/Drugov and Troya‐Martinez - 2019 - Vague lies and lax standards of proof On the law .pdf
tags: [literature]
keywords: [persuasion, strategic-communication, consumer-protection, law-and-economics, credulous-consumers, signal-jamming]
topics: []
related: [Gabaix2006, Inderst2009, Nelson1974]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper analyzes a persuasion game where a seller provides (un)biased and (im)precise advice and may be fined by an authority for misleading the buyers. In the equilibrium, biasing the advice and making it noisier are complements. The advice becomes both more biased and less precise with a stricter standard of proof employed by the authority, a larger share of credulous consumers, and a higher buyers' heterogeneity. The optimal policy of the authority is characterized in terms of a standard of proof and resources devoted to the investigation.

## Summary

A seller advises buyers about a product whose match quality is unknown to both parties. The seller can distort communication along two dimensions: a hidden *bias* (lying, exaggerating quality) and a publicly observable *noise* (vagueness, imprecision). An authority later samples customers, runs a one-sided hypothesis test for positive bias against a "standard of proof," and fines guilty sellers in proportion to the estimated bias. The central, counterintuitive result is that bias and noise are *complements* in equilibrium: bigger lies are hidden behind vaguer advice. The paper then derives the authority's optimal joint choice of standard of proof and investigative resources.

## Research question

How does a seller strategically combine outright lies (bias) and vagueness (noise) when a regulator can investigate and sanction misleading advice, and given that equilibrium behavior, how should the authority set its standard of proof and the resources (sample size) devoted to investigation?

## Method / identification

A persuasion / signal-jamming model in the spirit of Holmström (1999), with the distinctive feature that the sender chooses *both moments* of the signal-distortion term. Match quality is $\theta\sim N(\mu,\sigma^2)$, unknown to both sides. The seller emits a signal $S=\theta+\varepsilon$ with $\varepsilon\sim N(\beta,\eta^2)$, secretly choosing bias $\beta$ and publicly choosing noise $\eta$ (bounded below by an experience-good floor and above by disclosure obligations). A share $c$ of buyers are *credulous* (take the signal at face value, posterior $=s$); the remaining $1-c$ are *rational*, observe $\eta$, hold a conjecture $\tilde\beta$ about the bias, and form the precision-weighted posterior

$$E[\theta\mid s;\beta,\tilde\beta]=\frac{\sigma^2(\tilde\beta)+\eta^2\mu}{\eta^2+\sigma^2}+\frac{\sigma^2}{\eta^2+\sigma^2}\,s.$$

Seller revenue $R(\beta,\eta)$ equals the buyer's expected valuation; rational buyers are not misled in equilibrium (since $\tilde\beta=\beta$), so revenue gains come only from credulous overpayment by $\beta$. The authority draws $N$ buyers/mystery shoppers, estimates $\hat\beta=\frac1N\sum\varepsilon_i\sim N(\beta,\eta^2/N)$, and tests $H_0:\beta=0$ against $H_1:\beta>0$ at significance level $\alpha$, convicting iff the standardized statistic exceeds threshold $z_\alpha$ (the "standard of proof"). The expected fine $C(\beta,\eta)$ rises in $\beta$ but is *U-shaped* in $\eta$: more noise lowers the conviction probability yet raises the conditional fine via truncation, minimized at $\eta=\sqrt{N}\,z_\alpha$ for given bias (Lemma 1). The seller maximizes profit $\Pi=R-C$ under a fixed-point conjecture; the authority then minimizes a loss combining credulous-consumer harm, type-I fines on honest sellers (share $h$), and investigation cost $I(N)$.

## Data

None — purely theoretical. The paper motivates assumptions with regulatory case material (EC 2011 retail-investment mystery shopping, FTC/OFT complaint rankings) and cites empirical evidence on credulous investors (Malmendier & Shanthikumar 2014) and coexisting honest/dishonest financial advisers (Egan, Matvos & Seru 2017), but estimates nothing.

## Key findings

- **Lemma 1**: the expected fine increases in bias and is U-shaped in noise (decreasing below $\sqrt{N}z_\alpha$, increasing above).
- **Proposition 1**: a closed-form interior equilibrium exists under two mild assumptions, with $\beta^*=\frac{1}{\sqrt{N}z_\alpha}\sqrt{\frac{\sigma^2}{\Gamma-c}}$ and $\eta^*=z_\alpha\sqrt{N}\,\beta^*$, so the bias-to-noise ratio is pinned at $\beta/\eta=\frac{1}{z_\alpha\sqrt{N}}$.
- **Corollary 1 (main result)**: bias and noise are *complements* — the seller tells "either an exact truth or a vague lie." Both rise with the standard of proof $z_\alpha$, the prior variance $\sigma^2$ (buyer heterogeneity), and the credulous share $c$; both are unaffected by average quality $\mu$. A larger sample $N$ lowers the bias but, surprisingly, leaves the equilibrium noise unchanged.
- **Proposition 2**: an interior optimal policy $(z_\alpha^*,N^*)$ exists. The optimal standard of proof is *higher* (stricter) with fewer credulous consumers, lower prior variance, higher honest-seller noise, and a larger honest share $h$. Optimal sample size rises with $c$, $\sigma^2$, and honest noise, but moves *non-monotonically* in $h$. An upper bound $z_{\max}$ exists beyond which the seller would choose infinite bias.
- **Proposition 3 / Corollary 2 (fixed price)**: with an exogenous price $p=\mu$ and all buyers rational, the same bias-to-noise ratio obtains, but comparative statics on $\sigma^2$ *reverse* (bias and noise now *decrease* in heterogeneity) and average quality $\mu$ now matters.

## Contribution

Three contributions. (1) To persuasion/advertising: it micro-founds "lying costs" via an endogenous regulatory fine rather than assuming exogenous costs (cf. Kartik 2009), and—unlike Johnson & Myatt (2006), where optimal disclosure is extreme—delivers *partial* information disclosure and the bias–noise complementarity. (2) To law and economics of litigation: it micro-founds the signal the court observes about the defendant's harmful action, lets the defendant control that signal's *variance*, and lets the authority's policy reshape the seller–buyer *equilibrium communication* rather than just an individual decision problem. (3) It characterizes optimal regulatory policy jointly in standard of proof and investigative resources.

## Limitations & open questions

- Rational buyers are assumed to observe noise; the working paper (Drugov & Troya-Martinez 2012) treats *unobserved* noise (fine print) where the analysis becomes "technically very hard" though Proposition 1 qualitatively survives — a hook for fully solving the unobservable-precision case.
- If rational consumers cannot tell honest from strategic sellers, they debias by $(1-h)\beta$, noise then serves both cost-reduction and revenue motives, and "the exact characterization is difficult" — left open.
- Welfare ignores noise per se; with risk-averse consumers or fixed prices noise enters welfare and the optimal standard of proof should fall — not fully developed.
- Extensions only sketched: informational externalities between sellers of related products (disciplining effect can *reverse* under correlated communication shocks), punitive/scaled damages $d$, and consumer-education policy reducing $c$.
- The authority uses a non-Bayesian "naked statistical evidence" test; optimality relative to a Bayesian rule is acknowledged as an open debate.
- The authors hope the micro-founded continuous-harmful-action framework "will be used in the future to enrich existing models of litigation."

## Connections

The signal-jamming structure is à la Holmström (1999) career concerns. The disclosure/precision logic builds directly on Johnson & Myatt (2006) and Lewis & Sappington (1994), inverting their "extreme disclosure" prediction. It sits in the strategic-communication-with-lying-costs tradition of Kartik (2009) and Kartik, Ottaviani & Squintani (2007), and the persuasion framework of Kamenica & Gentzkow (2011). On advice to buyers it relates to [[@Inderst2009|Inderst & Ottaviani]] (2009, 2013), where advice is binary ("buy"/"don't") so only bias and not noise can be chosen. False-advertising signalling links to [[@Nelson1974|Nelson (1974)]], Corts (2013), Piccolo, Tedeschi & Ursino (2015), and Rhodes & Wilson (2018); credulous-consumer advertising to Glaeser & Ujhelyi (2010) and Hattori & Higashida (2012); and behavioral-IO foundations to [[@Gabaix2006|Gabaix & Laibson (2006)]] and DellaVigna & Gentzkow (2010). The law-and-economics-of-evidence strand draws on Schrag & Scotchmer (1994), Lewis & Poitevin (1997), Demougin & Fluet (2008), Kaplow (2011), and Gennaioli & Shleifer (2007). The coexistence of honest and strategic advisers is grounded in Egan, Matvos & Seru (2017).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
