---
citekey: Charness2002
title: Understanding Social Preferences with Simple Tests
authors: ["Charness, Gary", "Rabin, Matthew"]
year: 2002
type: journalArticle
doi: 10.1162/003355302760193904
zotero: "zotero://select/library/items/39MN3DI7"
pdf: /Users/jesper/Zotero/storage/MU7TD2PN/Charness2002.pdf
tags: [literature]
keywords: [social-preferences, inequality-aversion, reciprocity, social-welfare-preferences, experimental-economics, distributional-preferences, behavioral-game-theory]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Departures from self-interest in economic experiments have recently inspired models of "social preferences." We design a range of simple experimental games that test these theories more directly than existing experiments. Our experiments show that subjects are more concerned with increasing social welfare—sacrificing to increase the payoffs for all recipients, especially low-payoff recipients—than with reducing differences in payoffs (as supposed in recent models). Subjects are also motivated by reciprocity: they withdraw willingness to sacrifice to achieve a fair outcome when others are themselves unwilling to sacrifice, and sometimes punish unfair behavior.

## Summary
Charness and Rabin run 29 deliberately simple distribution and response games (467 subjects, 1697 decisions) engineered to break the confounds that plague the canonical games (ultimatum, prisoner's dilemma) used to motivate inequality-aversion models. They show that subjects care far more about raising total social welfare—and especially the payoff of the worst-off party—than about shrinking payoff differences. Difference aversion is rare: almost nobody pays to lower an ahead-of-them opponent, and Pareto damage is observed *more* often when it increases inequality (retaliation) than when it reduces it. Layered on top of distributional motives is **reciprocity**, but of an asymmetric kind: positive reciprocity is essentially absent, whereas negative reciprocity—particularly "concern withdrawal" (ceasing to sacrifice for someone who was themselves unfair)—is strong. The paper packages these findings into a parsimonious three-parameter utility model and a more elaborate multiperson "reciprocal-fairness equilibrium."

## Research question
Do the "social-preference" theories that explain laboratory departures from self-interest actually capture the *right* motives? Specifically, is Pareto-damaging behavior (e.g., rejecting unfair ultimatum offers) and helpful sacrifice (e.g., cooperation) driven by an intrinsic taste for **reducing payoff differences** (difference/inequality aversion), or by a concern for **social welfare / efficiency plus reciprocity**? The authors argue the existing game menu cannot tell these apart because (i) inequality-reducing Pareto damage is only ever available when a retaliation motive is aroused, and (ii) the only Pareto damage permitted is inequality-reducing—so difference aversion, reciprocity, and self-interest make coincident predictions.

## Method / identification
The core analytical device is a stylized two-person utility function for the responder B as a weighted sum of own and other's money payoff, with weights that depend on relative standing and on whether A "misbehaved":
$$U_B(\pi_A,\pi_B) = (\rho\, r + \sigma\, s + \theta\, q)\,\pi_A + \big(1 - \rho\, r - \sigma\, s - \theta\, q\big)\,\pi_B,$$
where $r=1$ if $\pi_B > \pi_A$ (B is ahead) else $0$; $s=1$ if $\pi_B < \pi_A$ (B is behind) else $0$; and $q=-1$ if A has misbehaved else $0$. The parameter $\rho$ is the weight on A's payoff when B is ahead, $\sigma$ the weight when B is behind, and $\theta$ a reciprocity shift. This single form **nests** the competing theories as parameter regions:
- **Competitive preferences:** $\sigma \le \rho \le 0$ (B always wants to do relatively better).
- **Difference aversion** (Fehr–Schmidt, Bolton–Ockenfels): $\sigma < 0 < \rho < 1$ — B will lower A's payoff when A is ahead.
- **Social-welfare preferences:** $1 \ge \rho \ge \sigma > 0$ — B always likes both payoffs higher but weights the worse-off party more; nests Andreoni–Miller.
- **Reciprocity** enters crudely via $\theta>0$: when A misbehaves ($q=-1$), both $\rho$ and $\sigma$ fall by $\theta$.

Identification strategy: design games so each pairwise hypothesis makes *opposite* predictions, and so that "free" inequality reduction, costly inequality-increasing efficient sacrifice, and Pareto damage with vs. without a retaliation motive can each be isolated. Seven two-person dictator games strip out reciprocity; twenty response games hold B's choice set fixed while varying A's forgone outside option (using the **strategy method**, contingent choices, plus role reversal), so that B's response to *identical* payoffs as a function of A's prior move identifies reciprocity. Estimation is two-pronged: (1) counting the share of choices *consistent* with each model's parameter restrictions (allowing heterogeneity), and (2) a maximum-likelihood logit-style fit of fixed $\rho,\sigma,\theta$ with a precision parameter $\gamma$, comparing nested models by likelihood-ratio tests.

Appendix 1 builds the deeper structure: a disinterested social-welfare criterion $W = \delta\min[\pi_1,\dots,\pi_N] + (1-\delta)\sum_i \pi_i$ (with $\delta=1$ Rawlsian maximin, $\delta=0$ pure surplus-maximization), embedded into individual utility via a self-interest weight $\lambda$. This maps exactly onto the Section II parameters: $\rho = \lambda/(1+\lambda(1-\delta))$ and $\sigma = \lambda(1-\delta)/(1+\lambda(1-\delta))$, with ratio $\rho/\sigma = 1/(1-\delta)$. Reciprocity is added through endogenous "demerit" weights $d_k$ and a psychological-game fixed point, yielding two solution concepts: a **social-welfare equilibrium (SWE)** and the full **reciprocal-fairness equilibrium (RFE)**, in the framework of Geanakoplos, Pearce, and Stacchetti.

## Data
467 subjects making 1697 decisions across 29 games (12 in Barcelona / Universitat Pompeu Fabra, 20 at UC Berkeley), conducted Oct–Nov 1998 and Feb–Mar 1999. Stakes: 100 lab units = 100 pesetas (~$0.70) in Barcelona, = $1 at Berkeley; average net earnings ~$6 / ~$11. Each subject played each role (A and B) via role reversal; responders used the strategy method. No pilots; all stakes-played data reported. Five of the games are three-player.

## Key findings
- **Difference aversion is weak and rare.** The strongest case (Berk29, a *free* refusal to earn less) yields only ~1/3 difference-averse choices (and that pool includes competitive types). When reducing inequality requires sacrifice it nearly vanishes; e.g., 0 of 36 subjects chose $(0,0)$ over $(800,200)$ absent retaliation. Pareto-damaging behavior was observed *more* often when it increased inequality than when it decreased it.
- **Social-welfare preferences dominate.** In dictator games social welfare explains far more behavior than difference aversion or competitive preferences (e.g., 97% vs. lower; 87% vs. 46% on uniquely-predicted choices in Table III). About half of subjects make *inequality-increasing* sacrifices when efficient and cheap (choosing $(750,375)$ over $(400,400)$).
- **Charity/asymmetry.** Regression (Table VI) shows a B who is *ahead* of A puts large positive weight on A's payoff ($\rho$ large), but a B who is *behind* with no reciprocity at stake puts weight near 0 on A's payoff ($\sigma \approx 0$, insignificant). A "charity" model ($\sigma$ restricted) fits as well as the full distributional model; difference aversion's $\sigma<0$ has *no* explanatory power beyond self-interest, contradicting Bolton.
- **Asymmetric reciprocity.** Positive reciprocity is essentially absent (helping *falls* slightly after a kind A move, 44% with no play vs. 36% after help). But **concern withdrawal** is strong: helpful sacrifice collapses from ~48–50% to ~7–18% once A behaves selfishly, and to 11% when A has hurt B (Table VII). When A misbehaves, B's estimated weight on A's payoff drops sharply or goes negative ($\theta$ significantly positive); allowing $\theta\neq0$ improves fit far more than freeing $\sigma$.
- **Multiperson:** Subjects care about the distribution *among others* (54% sacrifice to equalize three-way payoffs in Berk24, contradicting Bolton–Ockenfels), trade off minimum payoff against total surplus, and punish a greedy first mover by assigning him the low payoff (the 1200/400/100-vs-200 share jumps from 14% to 80% depending on who is hurt).
- **Theorems (Appendix 1):** *Theorem 1* — an RFE exists for all parameter values and all games (Kakutani fixed point on best-response × demerit maps). *Theorem 2* — when the selflessness standard $\lambda^* \le \lambda$, every social-welfare equilibrium is an RFE, so SWE is a useful heuristic for the "cooperative" equilibria, with negative (concern-withdrawal) equilibria arising when standards are high or under disequilibrium/heterogeneity.

## Contribution
Provides a clean, confound-free experimental refutation of the claim that inequality aversion is the primary driver of non-self-interested lab behavior, repositioning **social-welfare preferences plus negative reciprocity** as the better organizing account. Methodologically, it (i) introduces a unifying three-parameter model that nests competitive, difference-averse, and social-welfare preferences plus a reciprocity shift, enabling direct horse-race comparison; (ii) demonstrates the value of "simple, diagnostic" games over the ultimatum-game-dominated menu; and (iii) supplies a formal multiperson reciprocal-fairness equilibrium. It became one of the most cited behavioral/experimental economics papers and a standard reference distinguishing distributional from intention-based theories.

## Limitations & open questions
The authors are explicit that they do *not* claim to have disproven difference aversion: behavior is heterogeneous, and a minority (Fehr–Schmidt suggest ~40%) may be difference-averse in some settings—arguably consistent with the data. Stated open problems and hooks:
- **Heterogeneity and individual differences.** Neither the analysis nor the formal model handles preference heterogeneity or cross-game correlation in individual play; good-fitting future models must.
- **The "complicity"/responsibility-alleviation effect.** Merely having another player involved makes subjects more self-interested; this is unmodeled.
- **Eliciting beliefs/intentions.** First-mover motives could not be pinned down because the authors could not observe beliefs about responders; they call for designs that directly measure participants' beliefs about others' intentions.
- **The Barc7 puzzle.** Only 6% damage payoffs after a kind move vs. ~30% otherwise — a provocative hint of *positive* feelings suppressing difference aversion (positive reciprocity reducing difference aversion when self-interest is absent), which they flag as needing models where kindness blocks petty Pareto damage. They view such "wealthy party helps, hopes not to be punished" games (employer–employee) as more economically relevant than the ultimatum game.
- **Tractability vs. realism.** The RFE model is admittedly too complex for calibration yet still too restrictive (homogeneous preferences, equilibrium-only, omits complicity); the authors frame the trade-off between simple applicable models and psychologically accurate ones as unresolved. The strategy method, role reversal, and the relatively low rate of retaliation also caution against extrapolation.

## Connections
Directly contests the **difference/inequality-aversion** program of Fehr & Schmidt (1999) and Bolton & Ockenfels (2000), and the earlier Bolton (1991) model that posited $\rho=0$. It extends **Andreoni & Miller (2002)**, whose dictator-menu evidence of giving to richer recipients the authors recast as social-welfare preferences, and builds on **Rabin (1993)** intention-based reciprocity (while arguing helpful sacrifice is *not* mostly positive reciprocity). The reciprocity formalism adopts the psychological-games apparatus of **Geanakoplos, Pearce & Stacchetti (1989)** and relates to **Dufwenberg & Kirchsteiger** and **Falk & Fischbacher (1998)** (which blends difference aversion with reciprocity), differing by omitting sequential-rationality refinements. The social-welfare/maximin criterion echoes **Yaari & Bar-Hillel (1984)** and Rawlsian fairness. Corroborating evidence on inequality-reduction's weak role is cited from Kagel & Wolfe (1999) and Engelmann & Strobel (2001); on inequality-increasing giving from Charness & Grosskopf (2001) and Kritikos & Bolle. The lone counter-note on positive reciprocity comes from McCabe, Rigdon & Smith (2000).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
