---
citekey: Faure-Grimaud2003
title: Risk Averse Supervisors and the Efficiency of Collusion
authors: ["Faure-Grimaud, Antoine", "Laffont, Jean-Jacques", "Martimort, David"]
year: 2003
type: journalArticle
doi: 10.2202/1534-5971.1055
zotero: "zotero://select/library/items/E7S6RQHY"
pdf: /Users/jesper/Zotero/storage/YEMN7KMF/Faure-Grimaud et al. - 2003 - Risk Averse Supervisors and the Efficiency of Coll.pdf
tags: [literature]
keywords: [collusion, supervision, risk-aversion, mechanism-design, principal-agent, organizational-design, cara-utility]
topics: []
related: [Prendergast1996]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper studies the efficiency of collusion between supervisors and supervisees. Building on Tirole (1986)'s results that deterring collusion with infinitely risk averse supervisors is impossible, while it is costless to do so under risk neutrality, we develop here a theory of collusion based on a trade-off between the risk premia required by (less extreme) risk attitudes and incentives. This allows us to link the efficiency of collusion to the supervisor's risk aversion and to various parameters characterizing the economic environment in which collusion may take place. We are then able to derive implications for the design of organizations, like determining how the number of tasks/agents per supervisor or the level of competition may impact on the cost of collusion, studying the impact of vertical integration on those same costs, or characterizing the role of uncertainty on side-contracting.

## Summary
The paper builds a tractable theory of supervisor–agent collusion in which the frictions deterring collusion arise endogenously from the supervisor's risk aversion rather than from exogenous transaction costs. A principal must reward a supervisor for reporting a revealing signal and punish him otherwise; deterring a bribe requires a wage spread that exceeds the collusive stake, which imposes risk on a risk-averse supervisor and hence costs a risk premium. This insurance-versus-incentives trade-off makes the cost of fighting collusion continuous in the degree of risk aversion $r$, interpolating between Tirole's two polar cases ($r=0$, costless; $r=\infty$, supervision useless). The framework then yields comparative statics linking collusion costs to information accuracy, span of control, market competition, vertical integration, and environmental uncertainty.

## Research question
How does a supervisor's (finite) degree of risk aversion determine the efficiency of supervisor–agent collusion inside an organization, and how can the principal's optimal collusion-proof contract — and broader organizational design choices — be linked to parameters of the firm's economic environment? The paper explicitly aims to fill the gap between Tirole (1986), with no side-contracting frictions and only polar risk attitudes, and Tirole (1992), with exogenous transaction costs that cannot be tied to the environment.

## Method / identification
A static three-tier mechanism-design model: principal (owner), risk-averse supervisor, and productive agent. The agent has marginal cost $\theta\in\{\theta_1,\theta_2\}$, $\Delta\theta=\theta_2-\theta_1>0$, with $\mathrm{Pr}(\theta_1)=\nu$. The supervisor observes a partially verifiable hard signal $\sigma\in\{\sigma_1,\sigma_2\}$ (à la Green & Laffont 1986): the revealing signal $\sigma_1$ arrives with probability $\epsilon$ when the agent is efficient and can be concealed, while $\sigma_2$ cannot be manipulated. Joint probabilities are $p_{11}=\nu\epsilon$, $p_{12}=\nu(1-\epsilon)$, $p_{21}=0$, $p_{22}=1-\nu$. The supervisor has CARA utility $v(s)=\frac{1}{r}(1-e^{-rs})$; the agent is risk-neutral above zero wealth and infinitely risk-averse below it. The principal earns $\Pi=R(q)-s-t$ with $R$ increasing, concave, Inada conditions.

Identification rests on the Revelation Principle plus a Collusion-Proofness Principle (Tirole 1986; Laffont & Tirole 1993): the principal optimizes over collusion-proof grand-contracts in which the supervisor-led coalition (the supervisor makes a take-it-or-leave-it side-offer with full bargaining power, side-transfers frictionless) prefers truthful reporting. The binding coalition incentive-compatibility constraint is $s_{11}+u_{11}\ge s_2+u_{22}+\Delta\theta q_{22}$, where collusion-proofness forces $s_{12}=s_{22}=s_2$. The supervisor's ex ante participation constraint is $\nu\epsilon\,v(s_{11})+(1-\nu\epsilon)\,v(s_2)\ge 0$. Lagrangian first-order conditions characterize the optimum; comparative statics use the envelope theorem and Arrow–Pratt second-order (small-$\Delta\theta$) approximations of the risk premium.

## Data
None — this is a pure theory paper. No empirical estimation; results are propositions derived from the contracting model, with illustrative closed-form expressions and one figure depicting optimization in the $(s_2,s_{11})$ plane.

## Key findings
- **Proposition 1 (optimal collusion-proof contract).** All relevant constraints bind; the efficient agent's output is undistorted while the inefficient agent's output is distorted downward, $$R'(q_{22}^c(r))=\theta_2+\frac{\nu}{1-\nu}\Delta\theta\left(1-\frac{\epsilon e^{-r\Delta\theta q_{22}^c(r)}}{1-\nu\epsilon+\nu\epsilon e^{-r\Delta\theta q_{22}^c(r)}}\right).$$ Wages satisfy $s_{11}^c=s_2^c+\Delta\theta q_{22}^c(r)$ with $s_{11}^c>0>s_2^c$ (reward for revealing, penalty otherwise).
- **Proposition 2 (risk aversion).** $q_{22}^c(r)$ is decreasing in $r$, with $q_{22}^c(0)=q_{22}^d$ (collusion-free outcome — collusion has no bite under risk neutrality) and limit $q_{22}^u$ as $r\to\infty$. The principal's welfare is monotonically decreasing in $r$. For small stakes the extra agency cost of deterring collusion is the risk premium $\frac{r}{2}\nu\epsilon(1-\nu\epsilon)\Delta\theta^2 (q_{22}^c(r))^2$ — convex (quadratic) in the collusive stake.
- **Proposition 3 (information accuracy).** The principal's welfare is increasing in $\epsilon$; better supervisory information always helps, even though the per-output collusion cost is hump-shaped (inverted-U) in $\epsilon$. There is substitutability between accuracy and risk aversion.
- **Proposition 4 (span of control / irrelevance).** Under CARA, the principal's profit is the same whether one supervisor controls both independent product lines or each line has its own supervisor — a benchmark irrelevance result driven by additivity of independent CARA risks.
- **Proposition 5 (competition).** Greater supervisor risk aversion reduces the sensitivity (elasticity) of the firm's equilibrium output to competitive pressure; $r$ acts like an increase in the number of competitors.
- **Proposition 6 (vertical integration).** Integration eases collusion but improves information accuracy; it dominates separation only when the supervisor is not too risk-averse.
- **Proposition 7 (uncertainty / timing).** With a verifiable demand shock $\beta$, the principal strictly prefers reports made before $\beta$ realizes (ex ante collusion), because the convexity of the risk premium makes insuring the supervisor against $\beta$ cheaper; this is an "informativeness principle for collusion." Ex ante reporting yields output plans that fluctuate more across states.

## Contribution
Endogenizes the frictions of side-contracting through a single, interpretable primitive — the supervisor's risk aversion — replacing Tirole (1992)'s exogenous transaction costs and superseding Tirole (1986)'s polar cases with a continuous insurance–incentives trade-off. This makes the efficiency of collusion respond systematically to environmental parameters (information precision, competition, integration, uncertainty), turning the theory of collusion into a tool for comparative statics and organizational design that parallels Holmstrom & Milgrom's (1990) moral-hazard theory of task allocation.

## Limitations & open questions
- The model is **static** and assumes side-contracts are enforceable; enforceability is justified only informally via a repeated-game appeal (Tirole 1992; Martimort 1999), pointing to a dynamic foundation as open work.
- **Strong commitment** is required; the authors note the principal would want to renegotiate to give the supervisor more insurance once collusion is deterred (the renegotiation-vs-collusion conflict of Felli & Villas-Boas 2000) — left unaddressed.
- CARA is assumed for tractability; wealth effects would overturn the span-of-control irrelevance result (Prop. 4) and complicate the others.
- Collusion here is under **complete information** (the revealing signal pins down $\theta$); the asymmetric-information / soft-signal case is only sketched and developed elsewhere (Faure-Grimaud, Laffont & Martimort 2001).
- The organizational-design section (competition, integration, uncertainty) is explicitly described as "exploratory."
- The broader research program — linking transaction costs of collusion to the external environment via alternative microfoundations (asymmetric information, repeated self-enforcement, cultural transmission, non-monetary exchange) — is flagged as future work.

## Connections
The paper sits directly between Tirole (1986) and Tirole (1992) on collusion in hierarchies, and uses the Collusion-Proofness Principle from Laffont & Tirole (1993). The information structure with partially verifiable signals draws on Green & Laffont (1986), with evidence-disclosure modeling in Bull & Watson (2000). The CARA insurance-incentive logic parallels moral-hazard foundations in Holmstrom (1979), Shavell (1979), and Grossman & Hart (1983), and the multitask/span-of-control irrelevance echoes Holmstrom & Milgrom (1990); related collusion-among-risk-averse-agents work includes Itoh (1993) and the favoritism model of [[@Prendergast1996|Prendergast & Topel (1996)]]. Adverse selection with ex ante contracting and the incentives-vs-insurance trade-off connects to Salanié (1990) and Laffont & Rochet (1999). Alternative friction theories appear in Kofman & Lawarrée (1996), Laffont & Martimort (1999), Laffont & Meleu (1997), Martimort (1997, 1999), Martimort & Verdier (2000, 2002), and Felli (1997); the vertical-integration information argument is from Arrow (1975). The authors' companion papers — Faure-Grimaud, Laffont & Martimort (1999, 2000, 2001) and Faure-Grimaud & Martimort (2001) — extend the delegation, auditing, and intermediation variants.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
