---
citekey: Sliwka2001
title: On the costs and benefits of delegation in organizations
authors: ["Sliwka, Dirk"]
year: 2001
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/XEGPGEU2"
pdf: /Users/jesper/Zotero/storage/4SWCKTBR/Sliwka2001.pdf
tags: [literature]
keywords: [delegation, principal-agent, career-concerns, holdup-problem, empowerment, implicit-incentives, organizational-economics]
topics: ["[[strategic-delegation-firm-objectives]]"]
related: [Aghion1997, Gibbons1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We examine the question whether a decision should be delegated to a subordinate and whether this is done efficiently. We illustrate in a dynamic principal-agent model that delegation is useful for several reasons. First, it serves to test agents with unknown ability. Then, it may improve an agent's motivation when carrying out decisions as successful outcomes improve his reputation and hence his future wages. Costs of delegation arise from the risk of having decisions of lower quality and because after having made a successful decision a subordinate's power is increased. The latter effect may lead to inefficient delegation decisions. (JEL: D 23, M 12)

## Summary
A two-period principal-agent model in which delegation - defined as following the subordinate's recommendation - serves as an *investment* whose return is information about the agent's unknown decision-making ability. Because a successful agent gains bargaining power and a higher future wage, a holdup problem arises that can produce *under*-delegation relative to the social optimum. But when effort is non-contractible, the very same future bargaining gain becomes an *implicit incentive*, providing a contract-theoretic rationale for "empowerment": delegating a decision motivates the agent to exert effort because success raises his reputation and thus his future rents.

## Research question
Why should a decision in an organization be delegated to a subordinate rather than made by the superior, and does the principal delegate efficiently? The paper deliberately departs from the revelation-principle tradition (which asks why central mechanisms fail) and instead asks why decentralized information should be used in the first place, and how delegation interacts with motivation and monetary incentives.

## Method / identification
Dynamic principal-agent model. A principal $P$ hires an agent $A$ for two periods. Each period a method must be chosen (by $P$ or $A$) and then the task is carried out by $A$ at effort $e_t\in\{H,L\}$ with cost $c(H)=c$, $c(L)=0$. "Ability" is the probability of picking a good method. Principal ability $a_P$ is common knowledge; agent ability is symmetrically unknown, $a_A=a_h$ with probability $\tau$ and $a_A=a_l$ with probability $1-\tau$, ordered $a_l<E[a_A]<a_P<a_h$. The project succeeds with probability

$$\Pr\nolimits_{D_t}\{\pi_t=B\}=a_{D_t}\,p_{e_t},\qquad p_H>p_L>0,$$

paying $\pi_t=B>0$ on success and $0$ otherwise. The agent has limited liability and zero reservation wage; only short-term contracts (or long-term with opting-out) are feasible; no discounting. After a first-period success by the agent the posterior mean ability is

$$\hat a_A=E_{D_1=A}[a_A\mid \pi_1=B]=\frac{\tau a_h^2+(1-\tau)a_l^2}{E[a_A]}=E[a_A]+\frac{V[a_A]}{E[a_A]},$$

which is independent of first-period effort. Second-period wages are set by the Nash bargaining solution (equal split of the surplus above the principal's threatpoint of deciding herself). The analysis derives, for four informational regimes, a cutoff on the principal's own ability $a_P$ below which she delegates, writing $a_P=E[a_A]+\Delta$ and using the identity $E[a_A](\hat a_A-E[a_A])=V[a_A]$.

## Data
None - this is a purely theoretical paper. No empirical estimation; all results are propositions with appendix proofs.

## Key findings
- **Proposition 1 (efficient benchmark).** Socially optimal to delegate iff $a_P$ is below $E[a_A]+\dfrac{V[a_A]}{\frac{1}{p_H}+E[a_A]}$. The cutoff exceeds $E[a_A]$ and is increasing in the variance $V[a_A]$ of ability: more uncertainty about the agent means more value in experimentation. Delegation is "an investment whose return is knowledge about employees' abilities."
- **Proposition 2 (holdup, contractible effort).** With Nash bargaining the principal recoups only half the experimentation gain but bears the entire first-period quality loss, giving a strictly lower cutoff $E[a_A]+\dfrac{2V[a_A]}{\frac{1}{p_H}+E[a_A]}$ (denominator effectively halving the gain). Result: *under-delegation* - a holdup/underinvestment problem analogous to Klein-Crawford-Alchian / Williamson / Hart.
- **Proposition 3 (incomplete contracts, non-contractible effort).** With no performance-contingent contracts, delegation is the *only* way to motivate first-period effort: the agent works hard iff $\frac{1}{2}(\hat a_A-a_P)p_LB\ge \dfrac{c}{E[a_A](p_H-p_L)}$. Here the holdup effect *reverses sign* - there may be *more* delegation than efficient, because delegation acts as a commitment device to reward the agent. This formalizes the motivational ("empowerment") rationale.
- **Proposition 4 (spheres of competence).** The principal may *voluntarily acquire lower ability* (forgo competence) to credibly commit not to interfere, thereby strengthening the agent's future bargaining position and hence his incentives - profitable iff the maximal feasible ability $a_P^{\max}$ is below a derived cutoff. Related to Crémer (1995) on arm's-length relationships.
- **Proposition 5 (explicit incentive contracts).** When profits are verifiable, the reputation gain $S_A=\frac{1}{2}(\hat a_A-a_P)p_HB$ substitutes for the first-period bonus: implicit and explicit incentives are substitutes. If implicit incentives are insufficient, delegation restores the first-best cutoff (holdup mitigated, Proposition 1); if they suffice, delegation exceeds the no-moral-hazard case but never exceeds the reference. Mirrors the [[@Gibbons1992|Gibbons-Murphy (1992)]] result that explicit incentives rise over time as career-concern incentives decay.

## Contribution
Provides a unified principal-agent rationale for delegation that (i) frames delegation as experimentation/investment in learning about ability, (ii) identifies a reputation-driven holdup problem causing under-delegation, and (iii) shows that this same holdup effect endogenously generates incentives, giving a formal micro-foundation for "empowerment" and "job enrichment." It complements [[@Aghion1997|Aghion-Tirole (1997)]], whose authority-allocation model explains incentives to acquire information *before* a decision, by explaining improved incentives in *carrying out* the decision *after* it is made.

## Limitations & open questions
- The two-period horizon is a simplification; the author notes that, as in Holmström (1982), implicit incentives from career concerns decline as the principal learns the agent's ability over time - extending beyond two periods is left open.
- Symmetric uncertainty about the agent's ability is assumed for tractability; asymmetric or self-knowledge cases are not analyzed.
- Equal Nash bargaining power is assumed; a referee-prompted footnote notes that unequal bargaining power has a twofold, ambiguous effect (relaxing the incentive condition (7) but reducing the principal's benefit from delegation) - not formally worked out.
- Ability enters linearly in the success probability; richer technologies are not explored.
- The companion mimeo (Sliwka, "Delegation and Power in Hierarchies") extends the framework to hierarchies, where delegation also serves to reduce middle managers' power.

## Connections
The core experimentation logic builds directly on the career-concerns literature of Fama (1980) and Holmström (1982), and on the explicit-vs-implicit incentive interplay of [[@Gibbons1992|Gibbons & Murphy (1992)]]; the multi-task/information-structure extensions of Dewatripont, Jewitt & Tirole (1999a, 1999b) are cited as natural generalizations. The authority-allocation framing contrasts with [[@Aghion1997|Aghion & Tirole (1997)]], and the bargaining-power-as-source-of-incentives mechanism parallels Rajan & Zingales (1998) (asset access) and Stole & Zwiebel (1996) (intra-firm bargaining and organizational design). The holdup/underinvestment analogy invokes Klein, Crawford & Alchian (1978), Williamson (1985), and Hart (1995). The deliberate move away from the revelation principle situates the paper against Melumad, Mookherjee & Reichelstein (1995), Laffont & Martimort (1998), and Poitevin (1994). The voluntary-ignorance result connects to Crémer (1995) on arm's-length relationships, and the team-production learning angle to Meyer (1994).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
