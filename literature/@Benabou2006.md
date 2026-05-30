---
citekey: Benabou2006
title: Incentives and Prosocial Behavior
authors: ["Bénabou, Roland", "Tirole, Jean"]
year: 2006
type: journalArticle
doi: 10.1257/aer.96.5.1652
zotero: "zotero://select/library/items/BNIAUNST"
pdf: /Users/jesper/Zotero/storage/SBAVYRLG/Benabou2006.pdf
tags: [literature]
keywords: [prosocial-behavior, intrinsic-motivation, crowding-out, social-signaling, social-norms, reputation, self-image, public-goods]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We develop a theory of prosocial behavior that combines heterogeneity in individual altruism and greed with concerns for social reputation or self-respect. Rewards or punishments (whether material or image-related) create doubt about the true motive for which good deeds are performed, and this "overjustification effect" can induce a partial or even net crowding out of prosocial behavior by extrinsic incentives. We also identify the settings that are conducive to multiple social norms and, more generally, those that make individual actions complements or substitutes, which we show depends on whether stigma or honor is (endogenously) the dominant reputational concern. Finally, we analyze the socially optimal level of incentives and how monopolistic or competitive sponsors depart from it. Sponsor competition is shown to potentially reduce social welfare. (JEL D11, D64, D82, Z13)

## Summary
A signaling model in which an agent's observed prosocial action reflects an unobservable mix of three motives: intrinsic altruism, extrinsic (material) reward, and reputation (social esteem or self-image). Because rewards and visibility shift how observers parse those motives, extrinsic incentives can spoil the reputational value of good deeds and crowd out supply; the same machinery generates multiple social norms (when actions are strategic complements), a reluctance to turn down rewards, and welfare-reducing sponsor competition. The paper unifies a wide range of puzzles — perverse incentive effects, the prestige of anonymous giving, codes of honor, stigma — that no single prior model captured.

## Research question
What is the broader set of motives that shape prosocial conduct (volunteering, voting, donating, refraining from antisocial acts), and how do intrinsic, extrinsic, and reputational motives interact with the informational and economic environment? Concretely: when do explicit rewards/punishments *backfire* (crowding out), when do multiple social norms arise, why are donations rarely anonymous, and how should sponsors optimally set incentives?

## Method / identification
A Bayesian signaling / signal-extraction model with multidimensional private types. Each agent chooses participation $a\in A\subseteq\mathbb{R}$ at utility cost $C(a)$, earning direct payoff $(v_a+v_y y)a-C(a)$, where $v_a$ is intrinsic prosocial valuation, $v_y$ the valuation of money, and $y\ge 0$ the sponsor-set incentive rate. The two-dimensional type $v\equiv(v_a,v_y)$ is private. Observers form posteriors, and the agent's reputational payoff is linear in those posteriors:
$$R(a,y)\equiv x\big[\gamma_a\,E(v_a\mid a,y)-\gamma_y\,E(v_y\mid a,y)\big],$$
with visibility $x>0$ and image weights $\mu_a\equiv x\gamma_a$, $\mu_y\equiv x\gamma_y$. The agent solves
$$\max_{a\in A}\ \{(v_a+v_y y)a-C(a)+\mu_a E(v_a\mid a,y)-\mu_y E(v_y\mid a,y)\}.$$
The first-order condition $C'(a)=v_a+v_y y+r(a,y;\mu)$ shows the action reveals the *sum* of the three marginal motives, hence a signal-extraction problem. A key reinterpretation: with imperfect recall of one's own motives, $R$ becomes a *self*-image payoff, making the model formally identical for self-signaling (a la Bem; cognitive dissonance).

For closed-form results the authors use a normal-learning specification: $C(a)=ka^2/2$, $A=\mathbb{R}$, and $(v_a,v_y)$ bivariate normal with covariance $\sigma_{ay}$. Posteriors are linear with updating weights $\rho(y)$ on social orientation and $\chi(y)$ on greed (where $y\chi(y)=1-\rho(y)$); raising $y$ acts like increasing the noise-to-signal ratio $\theta\equiv\sigma_y/\sigma_a$. A second specification uses discrete choice $a\in\{0,1\}$ to study norms, defining honor $M^{+}(v_a)$ and stigma $v_a-M^{-}(v_a)$ and the reduced-form $\Psi(v_a)=v_a+\mu_a(M^{+}-M^{-})(v_a)$. Heterogeneous image concern $\mu$ enters as an additional, endogenous noise term $\Omega(y)^2=\mathrm{Var}(r(y;\mu))$ via a fixed point. The welfare section adds public-good spillovers ($v_a=u_a+w_a/n^{\kappa}$) and sponsor objective functions (planner, monopoly, competitive), solved as a screening/pricing problem.

## Data
None — this is a pure theory paper. It invokes published empirical and experimental findings as motivation and as out-of-sample tests, notably: Gneezy-Rustichini day-care fines and charity-collection experiments; Titmuss on paid blood; Funk (2005) on Swiss mail-voting lowering turnout in small communes; and especially Mellstrom-Johannesson (2005), whose blood-donor experiment (women's participation collapsing under a $7 payment but rebounding when the fee can be donated) the model matches via a higher $\mu_a$ for women (Proposition 2 / Figure 2A).

## Key findings
- **Proposition 1 (equilibrium):** With common image concern there is a unique differentiable-reputation equilibrium; contribution $a=(v_a+v_y y)/k+\mu_a\rho(y)-\mu_y\chi(y)$, with constant net reputational return $\bar r(y)=k(\mu_a\rho(y)-\mu_y\chi(y))$.
- **Proposition 2 (overjustification & crowding out):** For independent types ($\sigma_{ay}=0$), incentives are counterproductive ($\bar a'(y)<0$) over a range; for $\mu_a$ above a threshold there is an interval $[y_1,y_2]$ on which aggregate supply is *decreasing*. Rewards raise the noise-to-signal ratio, lowering $\rho(y)$ and raising $\chi(y)$, so good deeds get attributed to the reward or to greed.
- **Proposition 3 (signal reversal / small rewards):** Small net incentives can be counterproductive ($\bar a'(0)<0$); as $\sigma_a/\sigma_y\to 0$ the supply slope at $y=0$ tends to $-\infty$, producing a downward *discontinuity* at zero. Even a tiny aversion to appearing greedy ($\mu_y>0$) suffices.
- **Publicity/praise/shame:** Greater visibility strengthens signaling but, with heterogeneous image concern, also raises noise — limiting the power of image-based rewards.
- **Propositions 4-5 (multiple norms):** With heterogeneous $\mu$, equilibrium is a fixed point in $\Omega(y)$; existence always holds, uniqueness when $\omega_{ay}=0$. When $\Psi$ is increasing there is a unique (upward-sloping) equilibrium; when $\Psi$ is decreasing there are three equilibria (full, none, unstable interior) — multiple social norms.
- **Propositions 6-7 (stigma vs. honor):** Whether actions are strategic complements or substitutes depends on the sign of $\Delta'(v_a)=\mu_a(M^{+}-M^{-})'(v_a)$. Increasing density of $v_a$ (few "bad apples") -> stigma dominates -> complementarities -> multiplicity/volatility (e.g., crime). Decreasing density (few saints) -> honor/distinction dominates -> substitutes (e.g., heroism). Unobserved *forced participation* fosters complementarity; unobserved *involuntary nonparticipation* (valid excuses) inhibits it; symmetric results for undetected abstention vs. unnoticed good deeds.
- **Proposition 8 (no turning down):** Agents may never decline an offered reward, even when refusal is observable, because declining would identify them as image-driven (pooling at the prior mean is worse than pooling with image-indifferent participants).
- **Proposition 9 (optimal incentives & sponsors):** The socially optimal rate is strictly below the Pigouvian subsidy $y^{P}$; it subtracts a "tax" on socially wasteful reputation-seeking, $y^s=y^{P}-\Delta(c-y^{P})$ when taxation is non-distortionary. A monopoly sponsor may set *too generous* rewards (excess participation); competition raises rewards further and can reduce welfare.
- **Proposition 10 (holier-than-thou competition):** A monopolist serving the whole market never imposes inefficient screening sacrifices, but competing sponsors engage in "cream-skimming," requiring high-types to make costly sacrifices that are pure deadweight loss — reducing welfare with no increase in public-good supply.

## Contribution
Provides the first unified, micro-founded account of crowding out, social norms, and sponsor behavior built on *multidimensional* signaling — the essential ingredient (uncertainty about both altruism $v_a$ and greed $v_y$) that prior single-dimension signaling models (Bernheim 1994; Corneo 1997; Seabright 2002; Denrell 1998) lacked and that generates genuine overjustification and net crowding out. It gives formal content to the psychologists' "overjustification effect" as a signal-extraction problem; endogenizes social norms, stigma/honor, and the complement/substitute distinction rather than assuming payoff complementarities; rationalizes the prestige of anonymous giving and modesty; and derives a normative correction to Pigouvian subsidies plus a welfare critique of sponsor competition.

## Limitations & open questions
The authors flag (Section VI) three explicit extensions: (1) **organizations** — how high-powered incentives or performance pay conflict with signaling motives arising from teamwork or career concerns; (2) **sponsor objectives** — sponsors in practice have their own signaling concerns, not modeled here; (3) **identity** — the self-image reading connects to refusals of economically advantageous transactions felt to be insulting to dignity (pursued in Benabou-Tirole 2006). Internal modeling caveats: reputation is assumed *linear* in posteriors with type-independent coefficients (tractability, not generality); normality lets variables take implausible negative values, so distributions are "local approximations"; for the heterogeneous-image and norms cases only the *linear-reputation* class of equilibria is solved, and the existence of other nonlinear equilibria cannot be excluded; the welfare/competition results lean on $v_y$ being known (relaxing it reverses Bertrand competition, analyzed in the companion working paper Benabou-Tirole 2004a).

## Connections
The closest antecedents are signaling models of social interaction: Bernheim (1994) on conformity to the mainstream, Corneo (1997) on union membership (sharing the stigma/honor and concave-vs-convex-esteem insight), Seabright (2002) and Denrell (1998) on payment discontinuities at zero — all unidimensional and hence yielding standard upward-sloping responses without true crowding out. It extends the authors' own informed-principal work (Benabou-Tirole 2003) and self-signaling/imperfect-recall line (Benabou-Tirole 2002, 2004b; Bodner-Prelec 2003), and connects to Akerlof-Kranton (2000) on identity, Brekke et al. (2003) on moral motivation, Andreoni's warm-glow/impure-altruism tradition, and Glazer-Konrad (1996) and Bagwell-Bernheim (1996) on conspicuous giving/consumption. Empirically it speaks to the crowding-out literature surveyed by Frey (1997) and Frey-Jegen (2001), Gneezy-Rustichini, Fehr-Gachter on contracts and fines, and Funk (2005) on observability and voting. The proof of Proposition 6.1 draws on Jewitt (2004).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
