---
citekey: Krakel2007
title: Doping and cheating in contest-like situations
authors: ["Kräkel, Matthias"]
year: 2007
type: journalArticle
doi: 10.1016/j.ejpoleco.2006.11.003
zotero: "zotero://select/library/items/E4FIJ2B6"
pdf: /Users/jesper/Zotero/storage/RCLP6NAE/Krakel2007.pdf
tags: [literature]
keywords: [doping, contests, rank-order-tournaments, cheating, heterogeneous-players, drug-testing]
topics: []
related: [Lazear1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Individuals who compete in a contest-like situation (for example, in sports, in promotion tournaments, or in an appointment contest) may have an incentive to illegally utilize resources in order to improve their relative positions. We analyze such doping or cheating within a tournament game between two heterogeneous players. Besides the direct and indirect costs of doping, three major effects are identified which determine a player's decision to deviate from a no-doping situation — a cost effect, a likelihood effect and a base-salary effect. Moreover, the influence of heterogeneity and exogenous performance risk on a no-doping outcome, and the influence of ex-ante and ex-post doping tests on the players' investments are discussed.

## Summary
Kräkel models doping/cheating as a binary illegal-input choice embedded in a two-player rank-order tournament between a favorite and an underdog who also choose a legal input (effort/training). The paper characterizes when no doping survives as an equilibrium, decomposing the deviation incentive into three forces — a likelihood effect, a cost effect, and a base-salary effect — and shows that greater player heterogeneity and greater exogenous performance risk both stabilize the no-doping outcome. It then compares ex-ante versus ex-post drug testing and sketches the (deliberately incomplete) endogenous-prize problem.

## Research question
Which factors determine a contestant's incentive to deviate from a no-doping situation? Specifically: does large heterogeneity between players protect a no-doping outcome; how does exogenous performance risk affect doping decisions; and should drug tests be administered before (ex-ante) or after (ex-post) the tournament to implement high legal input? The paper deliberately does *not* solve the contest organizer's design problem, noting it is not even clear the organizer wants to deter doping.

## Method / identification
A two-stage game between two risk-neutral, heterogeneous players $i \in \{U, F\}$ (underdog, favorite). Output is multiplicative in doping, talent, and legal investment plus noise:
$$q_i = d_i\, t_i\, \mu_i + \varepsilon_i$$
with $t_U = 1$, $t_F = \tau > 1$, and the doping variable binary: $d_i = 1$ (clean) or $d_i = d > 1$ (doped). Doping and investment are thus *complements*. Legal-input cost $c(\mu_i)$ is increasing and convex; doping carries direct cost $\bar\kappa_i > 0$ and an indirect loss $L_i$ (reputation/future income) realized with the detection probability $1 - \delta$, where $\delta \in (0,1)$ is the non-detection probability when doped (and $\delta_i = 1$ when clean). The noise differences $\varepsilon_j - \varepsilon_i$ have symmetric density $f(\cdot)$ with unique mode at zero.

Timing: (1) players simultaneously choose $d_i$ (unobserved by the opponent); (2) they choose $\mu_i$; (3) nature draws noise; (4) a doping test defaults a doped player with probability $1 - \delta$. The game is solved by backward induction; because doping is private, it is equivalent to a one-stage game where each $i$ picks $(d_i, \mu_i)$. The tournament stage yields the asymmetric first-order conditions
$$c'(\mu_U^\ast) = d_U\,\Delta w\, f(d_U \mu_U^\ast - d_F \tau \mu_F^\ast)\,\delta_U \delta_F$$
$$c'(\mu_F^\ast) = d_F\,\tau\,\Delta w\, f(d_U \mu_U^\ast - d_F \tau \mu_F^\ast)\,\delta_U \delta_F$$
with $\Delta w = w_1 - w_2$ the prize spread. For closed-form results, Corollary 1 specializes to quadratic costs $c(\mu_i) = \tfrac{c}{2}\mu_i^2$ and uniform noise (triangular convolution with parameter $\gamma$), under second-order/existence conditions including $c > d^2 \tau^2 \Delta w \gamma^2 \delta$ and $d^2\delta > 1$.

## Data
None — this is a purely theoretical contest-theoretic paper. Empirical motivation is anecdotal (Tour de France doping scandals, the Hwang Woo-suk cloning fraud, and the Martinson et al. (2005) survey reporting that 33% of scientists admitted some fraudulent research practice).

## Key findings
- **Proposition 1** (comparative statics on equilibrium investment): the effect of doping on investment hinges on whether competition sits on the LHS ($d_U\mu_U^\ast < d_F\tau\mu_F^\ast$) or RHS of $f(\cdot)$. Doping acts through a *productivity effect* (complementarity raises the marginal return to $\mu_i$) and an opposing *competition effect* (it shifts $|d_U\mu_U^\ast - d_F\tau\mu_F^\ast|$, changing the marginal winning probability). A favorite who dopes can even *lower* his own investment when the competition effect dominates; an underdog who dopes comes "back into the race," raising both players' investments.
- **Proposition 2 / Corollary 1**: the no-doping profile $(d_U^\ast, d_F^\ast) = (1,1)$ is an equilibrium iff neither player's deviation gain exceeds its cost. The deviation incentive decomposes into three effects: a **likelihood effect** (doping raises one's winning probability if undetected — works *against* no-doping), a **cost effect** (doping changes legal-investment costs — typically *supports* no-doping when it raises costs), and a **base-salary effect** $(1-\delta)w_2$ (deviating forfeits the base salary $w_2$ with probability $1-\delta$ — *always supports* no-doping).
- **Heterogeneity stabilizes honesty**: there exist cutoffs $\hat\tau_U, \hat\tau_F$ such that for $\tau > \hat\tau_i$ player $i$ never dopes — when talent gaps are large, doping barely moves the outcome yet still risks disqualification.
- **Risk stabilizes honesty**: as $\gamma \to 0$ (more exogenous luck/quality uncertainty), there is a critical $1/\hat\gamma$ beyond which no one dopes, since outcomes are luck-dominated and doping only adds default risk.
- **Reliable testing** ($\delta \to 0$) always sustains no-doping; both likelihood and cost effects vanish while the default penalty becomes near-certain.
- **Prize design**: the effect of the winner prize is *ambiguous*, but a high loser prize $w_2$ deters doping through two channels (shrinking $\Delta w$ and strengthening the base-salary effect).
- **Ex-ante vs ex-post testing** (Section 4): for a given $(d_U, d_F)$, equilibrium investments are always *higher* under ex-ante testing, but the tournament then occurs only with probability $\delta_U\delta_F$ — a trade-off between guaranteed competition (ex-post) and higher conditional effort (ex-ante).

## Contribution
Unlike most prior doping models, Kräkel simultaneously incorporates (i) heterogeneous players, (ii) an endogenous legal input alongside the doping decision, and (iii) a positive probability of getting defaulted, with doping, ability, and investment all complementary. This lets him isolate the three-way decomposition (likelihood/cost/base-salary) and derive how heterogeneity, exogenous risk, test reliability, and prize structure jointly govern the no-doping equilibrium — generalizing earlier sport-contest doping papers that abstracted from legal effort or from default risk.

## Limitations & open questions
- Doping is restricted to a **binary** choice; the author explicitly flags that endogenizing the *continuous* optimal doping level (trading off effectiveness against detection probability and health costs) is a non-trivial open extension.
- The analysis focuses only on the **no-doping equilibrium**, leaving the other three pure-strategy configurations (mutual doping; only-underdog; only-favorite doped) uncharacterized.
- The contest **organizer's design problem is not solved** — endogenous prizes are only sketched, and it is left open whether the organizer or society even wants to deter doping (e.g., underdog-only doping can raise competitive balance and total performance).
- The paper suggests this is best pursued within a **closed model with a concrete objective function**, possibly tied to a specific professional sport where broadcasting revenue makes the objective tractable.
- Pure-strategy equilibrium existence is *assumed* in general and only guaranteed under the parametric (quadratic-cost, uniform-noise) specialization.

## Connections
The model is built on the seminal rank-order tournament of [[@Lazear1981|Lazear & Rosen (1981)]]. Within the doping literature it directly extends Eber & Thépot (1999), Haugen (2004), Berentsen (2002), and especially Konrad (2005), who likewise allows both doping and legal inputs but with homogeneous players and zero default probability; Berentsen et al. (2004) study doping in an evolutionary game, and Preston & Szymanski (2003) survey doping, sabotage, and match-fixing as forms of cheating. The doping mechanism parallels the sabotage-in-tournaments literature — Lazear (1989), Konrad (2000), Chen (2003), and Kräkel (2005) — where relative advantage comes from lowering a rival's output rather than illegally raising one's own. Related institutional applications include influence activities (Fairburn & Malcomson, 1994), fraudulent accounting (Berentsen & Lengwiler, 2004), the economics of corruption (Tirole, 1996), and the two-input complementary contest of Epstein & Hefeker (2003). Asymmetric equilibria in heterogeneous contests connect to Baik (1994) and Nti (1999), and the sport-contest objective-function discussion draws on Fort & Quirk (1995) and Szymanski (2003).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
