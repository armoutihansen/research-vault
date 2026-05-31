---
citekey: Rey-Biel2008
title: Inequity Aversion and Team Incentives
authors: ["Rey-Biel, Pedro"]
year: 2008
type: journalArticle
doi: 10.1111/j.1467-9442.2008.00540.x
zotero: "zotero://select/library/items/T9H3EQ4K"
pdf: /Users/jesper/Zotero/storage/BW78JABP/Rey-Biel2008.pdf
tags: [literature]
keywords: [inequity-aversion, team-incentives, behavioral-contract-theory, social-preferences, principal-agent, relative-performance-pay]
topics: ["[[social-preferences-contract-theory]]"]
related: [Bolton2000, Charness2002, Fehr1999, Grund2005, Itoh2004]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We study optimal contracts in a simple model where employees are averse to inequity, as modeled by [[@Fehr1999|Fehr and Schmidt (1999)]]. A "selfish" employer can profitably exploit envy or guilt by offering contracts which create inequity off-equilibrium, i.e., when employees do not meet his demands. Such contracts resemble team and relative performance contracts. We derive conditions for inequity aversion to be in itself a reason to form work teams of distributionally concerned employees, even in situations in which effort is contractible.

## Summary
Rey-Biel embeds Fehr–Schmidt inequity aversion into a stripped-down principal–two-agent contracting problem with observable, verifiable, contractible effort (no moral hazard, no uncertainty). The central insight is that a purely selfish principal can use *inequity itself* as a second incentive instrument alongside money: by designing bonuses that generate inequity *off-equilibrium* (when an agent shirks), the principal exploits the shirker's envy or guilt and so induces high effort while paying a total bonus bill strictly below the agents' summed effort costs. This rationalizes team and relative-performance contracts even absent informational asymmetries or effort complementarities, and can make it profitable to hire and demand effort from an agent too unproductive to be worth employing under standard preferences.

## Research question
How should a selfish (non-distributionally-concerned) employer structure reward schemes when employees are inequity-averse and compare their welfare to that of co-workers? Specifically: can inequity aversion alone be a reason to form work teams and demand joint effort, even when effort is contractible and complementarities are absent?

## Method / identification
A complete-information principal–agent model with one principal and two agents $i,j\in\{1,2\}$. Each agent earns minimum wage $w>0$; baseline production is $K$. Agents choose to "work hard" or "shirk." Joint hard work yields normalized extra output $1$; only agent $i$ working hard yields $q_i$ with $0<q_i<1$; both shirking yields $0$. Effort is observable, verifiable, and contractible. The principal offers bonuses for every output realization: $\{b_1,b_2\}$ under joint hard work, $\{b_1^1,b_2^1\}$ when only agent 1 works hard, $\{b_1^2,b_2^2\}$ when only agent 2 works hard, zero when both shirk.

Standard agents have utility $w+U_i$, where direct utility $U_i$ equals bonus minus effort cost. Inequity-averse agents follow an adapted Fehr–Schmidt form:
$$U_i^{FS}=w+U_i-\alpha\max[U_j-U_i,0]-\beta\max[U_i-U_j,0],\quad i\neq j,$$
with $\alpha$ governing envy (disadvantageous inequity) and $\beta$ governing guilt (advantageous inequity). Assumptions: (U1) $\alpha\geq 0,\ \beta\geq 0$; (U2) $\alpha\leq 1,\ \beta\leq\tfrac{1}{2}$ (own direct utility dominates). Note he relaxes Fehr–Schmidt's $\beta\leq\alpha$. Further: (C) $0\leq c_i<q_i$ and $c_i+c_j<1$ (surplus exists); (R1) limited liability, bonuses $\geq 0$; (R2) budget constraints $b_i+b_j\leq 1$, $b_i^i+b_j^i\leq q_i$, imposed even off-equilibrium; (R3) $K\geq 2w$. The principal designs the contract so the desired output is the *unique* (dominance-solvable) equilibrium of the $2\times 2$ game played by agents (following Ma, Moore & Turnbull 1988, to avoid the Demski–Sappington 1984 multiplicity problem). Identification is purely theoretical: optimal bonuses are chosen to minimize the equilibrium bonus bill subject to incentive-compatibility and the constraints.

## Data
None — this is a pure theory paper. Motivating stylized facts are drawn from interview/survey studies (Bewley 1999; Blinder & Choi 1990; Campbell & Kamlani 1997; Agell & Lundborg 1999), not from own data.

## Key findings
- **Proposition 1.** To maximally punish a shirking inequity-averse agent, offer the shirker no bonus ($b_i^j=0$), following from (R1) and (U2).
- **Proposition 2.** To maximally punish a shirker, offer *extreme* bonuses to the agent who works hard individually. If envy dominates ($\alpha(q_i-c_i)\geq\beta c_i$), give the worker all extra output ($b_i^i=q_i$), generating envy $\alpha(q_i-c_i)$. If guilt dominates ($\alpha(q_i-c_i)<\beta c_i$), give the worker *nothing* ($b_i^i=0$), generating guilt $\beta c_i$.
- **Proposition 3.** Characterizes the optimal contract implementing joint production: shirkers get zero; the off-equilibrium bonus to the hard worker is extreme (all output under envy, zero under guilt), split into three cases (a) both-envy, (b) mixed envy/guilt, (c) both-guilt. In case (c) the punishment cannot be fully maximized because both-shirk would Pareto-dominate and break uniqueness, so one agent must be paid his effort cost. Equilibrium bonuses are pinned by the indifference condition.
- **Corollary 1.** The principal earns strictly higher profits implementing joint production with inequity-averse agents than with standard agents — the equilibrium sum of bonuses is always *below* $c_i+c_j$, because more equity in equilibrium than off-equilibrium substitutes for money.
- **Proposition 4 (main result).** Inequity aversion may *in itself* be a reason to demand joint effort, even from an agent so unproductive ($1-q_1<c_2$) that hiring him is unprofitable under standard preferences — adding him raises the other agent's off-equilibrium envy/guilt and thereby cheapens both incentive constraints.

## Contribution
Provides the simplest closed-form model isolating the *pure* effect of inequity aversion on optimal contracts, deliberately stripping out the risk/uncertainty present in [[@Itoh2004|Itoh (2004)]] to separate inequity aversion from risk aversion. It shows uncertainty is not necessary for inequity aversion to matter for contract design, that bonuses become interdependent and must specify rewards under all contingencies, and supplies a novel rationale for team and relative-performance contracts in deterministic, informationally symmetric environments. Results extend to continuous effort and to status-seeking ($\beta<0$) and efficiency-seeking ($\alpha<0$) preferences via parameter transformations. It frames "behavioral contract theory" as a lens on organizational design (pay secrecy, office layout, information availability shape the strength of welfare comparisons).

## Limitations & open questions
- Reduced-form social preference only: no reciprocity or intention-based motives, which the author flags as crucial in repeated firm interactions where agents would react to the principal's *intent* behind inequity threats.
- Off-equilibrium threats must be **credible** to provide incentives; (R1)/(R2) are imposed as natural benchmarks, but the credibility of extreme off-equilibrium bonuses is left open.
- The **participation constraint** under interdependent preferences is "especially tricky": the reference point when an agent takes the outside option is undefined (does a departing agent still feel envy/guilt toward those left behind?). For low $w$ (in particular $w\leq\beta c_j$) inequity aversion yields no cost saving.
- Whether **effort costs** enter welfare comparisons (vs. rewards only) is an unresolved, context-dependent empirical question (cf. Königstein 2000).
- Parameter symmetry across agents and observability/measurability of $\alpha,\beta$ are assumed away; endogenizing the *strength* of comparisons (e.g., via the firm's information policy) is posed as future work.

## Connections
The model adapts the inequity-aversion preferences of [[@Fehr1999|Fehr & Schmidt (1999)]], with status- and efficiency-seeking variants following [[@Charness2002|Charness & Rabin (2002)]] and the distributional taxonomy of Engelmann & Strobel (2004), [[@Bolton2000|Bolton & Ockenfels (2000)]], Andreoni & Miller (1998), and Cox & Friedman (2002). The contracting backbone descends from Holmström & Milgrom (1991) on multitask/job design; equilibrium-uniqueness implementation follows Ma, Moore & Turnbull (1988) and addresses Demski & Sappington (1984). The closest comparison is [[@Itoh2004|Itoh (2004)]] on moral hazard with other-regarding preferences (and Che & Yoo 2001 on team incentives), from which the paper distinguishes itself by removing uncertainty. Related behavioral-contracting and tournament work includes Fehr & Schmidt (2000a) on fairness and incomplete contracts, Englmaier & Wambach (2002), Demougin & Fluet (2003, 2006), [[@Grund2005|Grund & Sliwka (2005)]], Dur & Glazer (2003), Masclet (2002), Huck & Rey-Biel (2006), and Cabrales, Calvó-Armengol & Pavoni (2008). Motivating survey evidence comes from Bewley (1999), Blinder & Choi (1990), Campbell & Kamlani (1997), and Agell & Lundborg (1999); the personnel-economics framing draws on Lazear (1995).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
