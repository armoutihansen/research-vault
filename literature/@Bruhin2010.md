---
citekey: Bruhin2010
title: "Risk and Rationality: Uncovering Heterogeneity in Probability Distortion"
authors: ["Bruhin, Adrian", "Fehr-Duda, Helga", "Epper, Thomas"]
year: 2010
type: journalArticle
doi: 10.3982/ECTA7139
zotero: "zotero://select/library/items/J5TG63CF"
pdf: /Users/jesper/Zotero/storage/K4P44RMK/Bruhin2010.pdf
tags: [literature]
keywords: [prospect-theory, probability-weighting, finite-mixture-model, risk-preferences, latent-heterogeneity, expected-utility, behavioral-types]
topics: []
related: [Kahneman1979, Quiggin1982, Tversky1992]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> It has long been recognized that there is considerable heterogeneity in individual risk taking behavior, but little is known about the distribution of risk taking types. We present a parsimonious characterization of risk taking behavior by estimating a finite mixture model for three different experimental data sets, two Swiss and one Chinese, over a large number of real gains and losses. We find two major types of individuals: In all three data sets, the choices of roughly 80% of the subjects exhibit significant deviations from linear probability weighting of varying strength, consistent with prospect theory. Twenty percent of the subjects weight probabilities near linearly and behave essentially as expected value maximizers. Moreover, individuals are cleanly assigned to one type with probabilities close to unity. The reliability and robustness of our classification suggest using a mix of preference theories in applied economic modeling.

## Summary
Bruhin, Fehr-Duda and Epper use a finite mixture model to uncover *latent heterogeneity* in risk taking across three experimental data sets (Zurich 2003, Zurich 2006, Beijing 2005; 448 subjects, ~18,000 certainty-equivalent observations). Without imposing type identities a priori, the estimator endogenously recovers two robust groups whose proportions are nearly identical across all three samples: about 20% of subjects weight probabilities near linearly and behave as expected-value maximizers ("EUT types"), while about 80% display the inverted-S probability weighting of cumulative prospect theory ("CPT types"). Individuals are assigned to one type with posterior probability close to 0 or 1 (near-zero entropy), and a three-group refinement splits the CPT majority into a moderate (~50%) and an extreme (~30%) subtype. The headline policy message: applied models should mix preference theories rather than impose one.

## Research question
What is the *distribution of risk-preference types* in a population? Specifically, can a parsimonious, empirically grounded, and robust characterization of risk taking be recovered without committing a priori to a single decision theory (EUT vs. CPT)? And does the recovered type composition replicate across designs and across radically different cultures (Swiss vs. Chinese)?

## Method / identification
The behavioral primitive is cumulative prospect theory (CPT), which nests EUT as a special case. An individual of type $c$ values a binary lottery $G_g=(x_{1g},p_g;x_{2g})$ with $|x_{1g}|>|x_{2g}|$ as
$$v(G_g)=v(x_{1g})\,w(p_g)+v(x_{2g})\,(1-w(p_g)),$$
with certainty equivalent $\widehat{ce}_g=v^{-1}\!\big(v(x_{1g})w(p_g)+v(x_{2g})(1-w(p_g))\big)$. The value function is a sign-dependent power function, $v(x)=x^{\alpha}$ for $x\ge 0$ and $v(x)=-(-x)^{\beta}$ otherwise. Probability weighting uses the two-parameter Goldstein–Einhorn / Lattimore–Baker–Witte form
$$w(p)=\frac{\delta\,p^{\gamma}}{\delta\,p^{\gamma}+(1-p)^{\gamma}},\qquad \delta\ge 0,\ \gamma\ge 0,$$
where $\gamma$ governs *sensitivity* (curve slope; $\gamma<1$ is an index of departure from linear/"rational" weighting) and $\delta$ governs *elevation/optimism*. Linear weighting corresponds to $\gamma=\delta=1$; parameters are sign-dependent (separate values for gains and losses).

Crucially, **loss aversion $\lambda$ is not identified** here: with only single-domain (non-mixed) lotteries, $\lambda$ cancels in the certainty-equivalent equation for loss lotteries, so it is neither feasible nor meaningful to estimate. They likewise assume a zero reference point, noting near-linear value functions create severe identification problems for reference-point estimation.

Observed certainty equivalents satisfy $ce_{ig}=\widehat{ce}_g+\varepsilon_{ig}$ with normally distributed, heteroskedastic errors: $\sigma_{ig}=\xi_i\,|x_{1g}-x_{2g}|$, where the s.d. scales with lottery range and carries individual- and domain-specific components $\xi_i$ (both restrictions $\xi_i=\xi$ and domain-equality are rejected at $p\approx 0$). For $C$ types with mixing proportions $\pi_c$, the type-$c$ density is $f(ce_i,G;\theta_c,\xi_i)=\prod_{g=1}^{G}\frac{1}{\sigma_{ig}}\phi\!\big(\frac{ce_{ig}-\widehat{ce}_g}{\sigma_{ig}}\big)$, and the mixture log-likelihood is
$$\ln L(\Psi;ce,G)=\sum_{i=1}^{N}\ln\sum_{c=1}^{C}\pi_c\,f(ce_i,G;\theta_c,\xi_i).$$
Estimation is by a customized Expectation-Maximization (EM) algorithm, which also returns each individual's posterior probability $\tau_{ic}$ of belonging to group $c$ via Bayesian updating. Classification quality is judged by the normalized entropy criterion (NEC); model size $C$ is chosen by comparing AIC, BIC, NEC, and the integrated completed likelihood (ICL), guided by the substantive research question rather than a single statistic. Standard errors come from a bootstrap with 4000 replications.

## Data
Three lab experiments eliciting certainty equivalents for two-outcome lotteries over real money. Zurich 2003 (179 subjects, 50 lotteries, 8,906 obs), Zurich 2006 (118, 40, 4,669), Beijing 2005 (151, 28, 4,225); total 448 subjects and ~17,800–18,000 observations. Lotteries spanned gains and losses (no mixed gain/loss lotteries), with probabilities of the extreme outcome from 5% to 95%; Zurich outcomes 0–150 Swiss francs, Beijing 4–55 yuan. Certainty equivalents were elicited via a 20-row choice list (computerized z-Tree in Zurich; paper-and-pencil in Beijing). Half the subjects faced abstract gamble framing, half a contextual framing (investment gains, repair costs, insurance premiums). Incentivized: one randomly selected row determined payment.

## Key findings
- **Two robust endogenous types.** Type I (~20%) has $\gamma,\delta\approx 1$ and $\alpha,\beta\approx 1$ (confidence intervals include unity), i.e., near-linear probability weighting *and* near-linear value functions — essentially expected-value maximizers, labeled EUT types. Type II (~80%) shows pronounced inverted-S weighting (pooled CPT $\gamma\approx 0.38$ for gains), labeled CPT types. EUT shares: 17.1% (ZH03), 22.3% (ZH06), 20.3% (BJ05).
- **Clean segregation.** Posterior probabilities $\tau_{ic}$ are almost all near 0 or 1; NEC $\approx 0$ for $C\in\{1,2,3\}$. Hardly any "mixed" types exist.
- **Robustness / replication.** The hypothesis of an identical type distribution across all three data sets cannot be rejected; group sizes are statistically indistinguishable across samples and stable as $C$ grows. EUT membership is especially stable — only ~2% of individuals switch into/out of Type I when $C$ goes from 2 to 3.
- **Three-group refinement.** The CPT majority decomposes into CPT-II (~50%, moderate inverted-S, $\delta$ near 1) and CPT-I (~30%, more extreme), differing chiefly in elevation/optimism $\delta$, not slope.
- **Cultural difference.** Type *proportions* match across cultures, but Chinese CPT subjects are less sensitive to probabilities (lower $\gamma$) and the Chinese CPT-I minority is strongly *optimistic* (overweights gain probabilities, underweights loss probabilities), making them risk seeking over a wide range — a microfoundation for the stylized fact that Chinese are more risk seeking than Westerners. The Swiss CPT-I minority shows the opposite (pessimistic) pattern.
- **Gender.** The only demographic systematically related to parameters is being *female*, associated with lower $\gamma$ (less probability sensitivity). Men's groups differ mainly in degree of rationality ($\gamma$); women's groups differ mainly in degree of optimism ($\delta$). The female CPT-II group has the widest region of pessimistic weighting, plausibly driving women's higher average risk aversion.
- **Behavioral validation.** Sorting subjects by type reproduces the fourfold pattern of risk attitudes; type-specific certainty-equivalent distributions differ significantly (Mann–Whitney, 5%) for 75% of lotteries. Differences vanish near $p=0.5$, where CPT and EUT choices are observationally close.
- **Robustness to wealth integration.** Re-estimating with a type-specific background parameter $k$ (value over $x+k$) leaves EUT proportions essentially unchanged and reassigns *not a single one* of 448 subjects, confirming nonlinear probability weighting (not value-function curvature) is the driver of classification.

## Contribution
The paper delivers the first demonstration of a *nearly identical* endogenous classification of risk-preference types across three independent data sets and two cultures, and the first to let EUT types *emerge endogenously* (rather than imposing one type to be EUT, as in Harrison and colleagues' choice-sorting approach). The unit of classification is the *individual* (the whole vector of a person's choices), not the single choice — a conceptual distinction the authors emphasize against Andersen-Harrison-Rutström and Harrison-Rutström. The practical payoff is a parsimonious, transportable set of group sizes and group-specific parameters usable as inputs to applied models, plus a sharp methodological warning (echoing Wilcox 2006) that basing predictions on a single preference theory is biased when heterogeneity is of a substantive kind.

## Limitations & open questions
- **Student samples only.** Whether the ~20% near-rational EUT share holds in a *representative population* sample is explicitly flagged as needing further research.
- **Task complexity.** Whether greater complexity of decision tasks alters type assignment is left open.
- **Loss aversion and reference point not identified.** Because the design has no mixed lotteries, $\lambda$ and the reference point cannot be estimated; the zero-reference assumption is a maintained, untested restriction.
- **Model-size indeterminacy.** Selection criteria conflict (NEC favors $C=2$, AIC/BIC/ICL lean to $C=3$); beyond three groups the likelihood becomes multimodal/possibly unbounded, so finer segmentation "may ask too much of our data."
- **Wealth-integration parameter $k$ poorly identified** when value functions are near-linear (it acts as an anti-index of concavity, confounded with $\alpha,\beta$).
- **Drivers of CPT heterogeneity underexplored.** Beyond gender, what determines probability-weighting curvature is "still underresearched."
- **Aggregate consequences.** The authors conjecture (citing strategic-complementarity literature) that even a minority of near-rational actors may be decisive for market outcomes — an empirical hypothesis they do not test.

## Connections
The behavioral backbone is [[@Tversky1992|Tversky and Kahneman's (1992)]] cumulative prospect theory and [[@Kahneman1979|Kahneman and Tversky (1979)]]; the weighting function is Goldstein and Einhorn (1987) and Lattimore, Baker and Witte (1992), with alternatives by [[@Quiggin1982|Quiggin (1982)]] and Prelec (1998), and functional-form guidance from Stott (2006). The EUT-types result is interpreted through Rabin's (2000) calibration theorem (EU maximizers should be near risk-neutral for small stakes). The finite-mixture/type-classification methodology builds on El-Gamal and Grether (1995), Stahl and Wilson (1995), and Houser and collaborators; ICL/NEC model selection follows Biernacki, Celeux and Govaert (1999, 2000) and Celeux and Soromenho (1996). The paper positions itself explicitly against the choice-sorting mixture approach of Andersen, Harrison and Rutström (2006) and Harrison and Rutström (2009), and reports corroborating British evidence from Conte, Hey and Moffatt (2010). Heteroskedastic-error modeling draws on Hey and Orme (1994) and Wilcox (2006, 2010); gender findings extend Fehr-Duda, de Gennaro and Schubert (2006); the Chinese-optimism result speaks to Kachelmeier and Shehata (1992) and Hsee and Weber (1999).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
