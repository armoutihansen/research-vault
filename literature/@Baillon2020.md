---
citekey: Baillon2020
title: Searching for the Reference Point
authors: ["Baillon, Aurélien", "Bleichrodt, Han", "Spinu, Vitalie"]
year: 2020
type: journalArticle
doi: 10.1287/mnsc.2018.3224
zotero: "zotero://select/library/items/QNRFSCJB"
pdf: /Users/jesper/Zotero/storage/AGAGE697/Baillon2020.pdf
tags: [literature]
keywords: [reference-dependence, prospect-theory, decision-under-risk, bayesian-hierarchical-modeling, loss-aversion, reference-point, experimental-economics]
topics: []
related: [Barber2008, Bell1985, Gul1991, Kahneman1979, Koszegi2006b, Loomes1986, Masatlioglu2016, Tversky1992]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Although reference dependence plays a central role in explaining behavior, little is known about the way that reference points are selected. This paper identifies empirically which reference point people use in decision under risk. We assume a comprehensive reference-dependent model that nests the main reference-dependent theories, including prospect theory, and that allows for isolating the reference point rule from other behavioral parameters. Our experiment involved high stakes with payoffs up to a week's salary. We used an optimal design to select the choices in the experiment and Bayesian hierarchical modeling for estimation. The most common reference points were the status quo and a security level (the maximum of the minimal outcomes of the prospects in a choice). We found little support for the use of expectations-based reference points. This paper was accepted by David Simchi-Levi, decision analysis.

## Summary
Reference-dependent theories (prospect theory, Köszegi–Rabin, disappointment models) are agnostic about *which* reference point a decision maker adopts, which leaves them under-identified and hard to test. Baillon, Bleichrodt, and Spinu treat the reference point as an estimable latent parameter inside one comprehensive model that nests these theories, and let a high-stakes risky-choice experiment (139 subjects in Moldova, payoffs up to a week's salary) reveal which of six candidate rules people use. Using an optimal experimental design and Bayesian hierarchical estimation, they find the Status Quo and MaxMin (a security level) dominate, jointly covering ~60% of subjects (~70% among sharply classified ones), while expectations-based / stochastic reference points get little support.

## Research question
Which reference point do people actually use when choosing between risky prospects? Concretely, among six theory-motivated reference-point rules, which best describes individual behavior once all *other* behavioral parameters (utility curvature, probability weighting, loss aversion, choice noise) are held fixed?

## Method / identification
The paper builds a *general reference-dependent (RD) model* that nests prospect theory, the Köszegi–Rabin (KR) model, and disappointment models as special cases, so that the reference-point rule can be isolated ceteris paribus from other parameters. Prospect theory with reference point $r$ is
$$\text{PT}_r(F) = \int_{x\ge r} U(x-r)\,dw^{+}(1-F) + \int_{x\le r} U(x-r)\,dw^{-}(F).$$
Allowing a stochastic reference point $R$ and adding (linear) consumption utility yields the comprehensive model
$$\text{RD}(F) = \int x\,dF + \int \text{PT}_r(F)\,dR,$$
which reduces to KR/disappointment models and to expected utility ($\text{EU}_r(F)=\int U(x-r)\,dF$) under appropriate restrictions. The KR choice-acclimating personal equilibrium (CPE) takes the prospect itself as reference point: $\text{KR}(F)=\int x\,dF + \int \text{EU}_x(F)\,dF$.

Six **reference-point rules** are compared (Table 1), classified by choice-specific vs. prospect-specific, deterministic vs. stochastic, and whether probabilities are used: Status Quo, MaxMin (max of the minimal outcomes — the amount obtainable for sure, a security level), MinMax (its bold counterpart), X at Max P (outcome with highest probability), Expected Value, and Prospect Itself (the only stochastic rule). All rules are "portable" — derivable from outcomes and probabilities alone, no introspective data.

Functional forms: power gain-loss utility $U(x)=(x-r)^{\alpha}$ for $x\ge r$ and $-\lambda(r-x)^{\alpha}$ for $x<r$ (same curvature $\alpha$ for gains/losses; $\lambda$ is loss aversion); one-parameter Prelec weighting $w(p)=e^{-(-\ln p)^{\gamma}}$; and a Luce (1959) logistic choice rule $P(F,G)=1/(1+e^{\xi[\text{RD}(G)-\text{RD}(F)]})$ with precision $\xi$.

**Estimation** is Bayesian hierarchical: each subject $i$ has behavioral parameters $B_i$ and a latent categorical reference-point rule $\text{RP}_i$, with population-level hyperparameters $\theta_B,\theta_{RP}$ drawn from hyperpriors $\pi_B,\pi_{RP}$. This shrinks noisy individuals toward the group mean, down-weights error-prone subjects, and yields both population shares and per-subject posterior probabilities over rules (so a subject can mix rules). $\text{RP}_i$ and $B_i$ are a-priori independent but dependent in the posterior.

## Data
Original lab experiment: 139 students and employees at the Technical University of Moldova (49 female, ages 17–47, mean 22). Each made 70 binary choices between prospects with one to four strictly positive outcomes. A 50 Lei (~$4; $8 PPP) participation fee was paid for sure; with probability 1/3 a randomly chosen subject had one choice played for real, so realized payoffs were substantial (mean 330 Lei, ~half a week's salary; two subjects won ~600 Lei, a full week's salary). Choices were drawn by a computationally intensive optimal design minimizing pairwise correlation across an 8-group 20×20 outcome-probability grid, maximizing orthogonality for efficient, robust estimates. Five choices were repeated for consistency; two embedded a stochastic-dominance test.

## Key findings
- **Status Quo and MaxMin dominate.** Median population shares (Table 2): Status Quo 0.30, MaxMin 0.30, Prospect Itself 0.20, MinMax 0.10, Expected Value 0.06, X at Max P 0.01. Together Status Quo + MaxMin describe ~60% of subjects.
- **Sharp classification.** 107 of 139 subjects had posterior probability ≥50% on a single rule; among these, ~70% used Status Quo or MaxMin. X at Max P had no sharply classified subjects.
- **Weak support for expectations-based / stochastic reference points.** At most 20% used an expectations-based rule (Prospect Itself or Expected Value); the only stochastic rule (Prospect Itself) got limited support. This directly challenges the dominant Köszegi–Rabin CPE model.
- **Behavioral parameters.** S-shaped gain-loss utility (concave gains, convex losses), inverse-S probability weighting, and population loss aversion $\lambda \approx 2.34$. Loss aversion varied strikingly by rule: ~0.50 in the optimistic MinMax group (gains weighted twice as much as losses — a reflection of MaxMin caution) up to ~2.44 for Expected Value. Fewer than 10% of subjects were expected-utility maximizers; only three were expected-value maximizers.
- **Robustness (six model variants, Table 6).** Choice-specific-reference-point models do *not* benefit from consumption utility — excluding it raised precision $\xi$, supporting [[@Kahneman1979|Kahneman–Tversky's (1979)]] conjecture that utility over changes alone suffices. Conversely, probability weighting matters greatly for prospect-specific models: dropping it from the Prospect-Itself model cut its share to ~10% and pushed MaxMin up to ~44%. Robustness to exponential utility, two-parameter Prelec, and IBeta weighting confirmed the main conclusions.
- **Stochastic dominance and KR.** Subjects who violated first-order stochastic dominance were more likely to use prospect-specific reference points (12% Expected Value, 30% Prospect Itself) than those who never violated it (5%, 18%) — consistent with [[@Masatlioglu2016|Masatlioglu–Raymond (2016)]] showing prospect-specific models can violate dominance.

## Contribution
The paper offers the first clean empirical identification of reference-point *formation* in risky choice by (i) embedding all competing theories in one nesting model so the reference-point rule is isolated ceteris paribus, avoiding the apples-to-oranges problem of mixture models or AIC horse races; (ii) using portable rules requiring only outcomes and probabilities, so they transfer to applied decision analysis; (iii) combining optimal experimental design with Bayesian hierarchical estimation to get robust individual- and population-level inferences; and (iv) using genuinely high stakes. Substantively, it provides quantitative validity bounds on the common Status-Quo assumption (only 30–40% use it), elevates the security-based MaxMin rule, and casts empirical doubt on the now-standard Köszegi–Rabin expectations-based model.

## Limitations & open questions
The authors are explicit about several open problems, each a project-idea hook:
- **More than two prospects.** Results are established only for binary choices; do they replicate for choice sets with three or more prospects?
- **Continuous distributions.** Only simple discrete prospects were used; applied decisions often involve continuous distributions.
- **Small probabilities.** The minimum probability was 5%; many real-world risks (e.g., annual risk of a fatal disease) are far smaller. It is unclear whether MaxMin survives when the worst outcome has tiny probability.
- **Untested reference points.** Rules requiring introspective inputs were excluded by design — goals (Heath et al. 1999), aspirations (Diecidue & Van de Ven 2008), and **history-dependent rules** based on previous choices (which add degrees of freedom: which past choices, how far back, how to update).
- **Other domains.** Findings are for decision under risk only; extension to intertemporal choice (habit formation), consumer choice (reference prices), and marketing is non-obvious because past experiences likely matter there.
- **Multiattribute choice.** An open conceptual question: is there a reference point per attribute (in which case MaxMin extends naturally) or a single reference *alternative* (more complex)?
- **PPE not estimable.** The preferred-personal-equilibrium rule (reference point = preferred prospect) was excluded because the model becomes recursive and cannot be estimated — an unresolved methodological gap.
- **Priors and dominance violations.** Prior choice could in principle affect estimates (found negligible here); and consumption utility mitigates but does not eliminate stochastic-dominance violations in prospect-specific models.

## Connections
The comprehensive model is built on prospect theory ([[@Tversky1992|Tversky & Kahneman 1992]]) and its stochastic-reference-point extensions by Sugden (2003), Köszegi & [[@Koszegi2006b|Rabin]] (2006, 2007), and Schmidt et al. (2008), and connects to the disappointment models of [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes & Sugden (1986)]], [[@Gul1991|Gul (1991)]], and Delquié & Cillo (2006); [[@Masatlioglu2016|Masatlioglu & Raymond (2016)]] formally link CPE to rank-dependent and quadratic utility and characterize its dominance violations. MaxMin draws on the security-seeking evidence of Hershey & Schoemaker (1985), Bleichrodt et al. (2001), and van Osch et al. (2004, 2006), and on Schneider & Day (2018); salience-based rules invoke Bordalo et al. (2012), [[@Barber2008|Barber & Odean (2008)]], and Chetty et al. (2009). The "portability" stance follows Rabin (2013); the Bayesian-hierarchical methodology builds on Rouder & Lu (2005), Nilsson et al. (2011), and Murphy & ten Brincke (2018), with functional-form choices from Stott (2006), Prelec (1998), Luce (1959), and Wilcox (2012). The motivating challenge — that reference-point formation remains unsolved — is voiced by Markowitz (1952) and Barberis (2013).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
