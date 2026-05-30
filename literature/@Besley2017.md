---
citekey: Besley2017
title: Profit with purpose? A theory of social enterprise
authors: ["Besley, Timothy", "Ghatak, Maitreesh"]
year: 2017
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/5HA2APZ7"
pdf: /Users/jesper/Zotero/storage/R5A8EP8A/Besley and Ghatak - 2017 - Profit with purpose A theory of social enterprise.pdf
tags: [literature]
keywords: [social-enterprise, motivated-agents, organizational-form, mission-integrity, principal-agent, assortative-matching, nonprofit, pro-social-motivation]
topics: []
related: [Aghion1997, Benabou2006, Besley2005]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> When social benefits cannot be measured, an organization that selects managers based on pro-social motivation can be used to balance profits with a social purpose. This paper develops a model of social enterprise based on selection of citizen-managers to run firms with flexible missions. We analyze organizational choice between social enterprise, for-profits, and nonprofits. The paper also develops the implications of matching between founders and managers based on their preferences for the mission. (JEL D21, L21, L31)

## Summary
Besley and Ghatak build a theory of social enterprise as a hybrid organizational form that resolves a "mission integrity problem": balancing profit against an unmeasurable social objective when only profit is contractible. Because the social payoff cannot be written into a contract, the firm instead *selects* intrinsically motivated "citizen-managers" and *delegates* the profit-versus-mission decision to them. The model compares for-profits (FP), nonprofits (NP), and social enterprises (SE), and shows SE strictly dominates on effort incentives over a middle range of managerial motivation. A matching extension shows that, even under competition for managers, stable assortative matching has selfish pairs in FPs, mid-motivation pairs in SEs, and highly motivated pairs in NPs.

## Research question
When can a hybrid "profit with purpose" organization (a social enterprise) be the optimal organizational form, and how does the choice among for-profit, nonprofit, and social enterprise depend on the motivation of managers and founders? Can social enterprises survive in a competitive market for managerial talent?

## Method / identification
A principal-agent model with transferable utility and risk neutrality. A firm has a founder and a manager. The manager chooses effort $e\in[\underline{e},1]$ (private, convex cost $c(e)$ with $c'''(e)>0$) and a binary action $x\in\{0,1\}$, where $x=1$ is the pro-social action (profit sacrificed for the mission) and $x=0$ is the profit-maximizing action. Effort first-order stochastically shifts the high state: with probability $e$ the high state $r=H$ obtains (profit feasible), with probability $1-e$ the low state $r=L$ obtains. A second, independent state $s\in\{h,l\}$ (probability $q$ of $h$) governs the social value of the pro-social action. Financial profit is $\pi>0$ or $0$; the per-capita social payoff $\theta_s$ enters founder and manager payoffs weighted by motivation parameters $\gamma_F,\gamma_M\ge 0$. Defining $\beta_s=N\theta_s/\pi$, the interesting region is $\beta_h N>1>\beta_l N$, so the efficient state-contingent rule is $x=1$ when $s=h$ and $x=0$ when $s=l$.

Both states $r,s$ and effort are private to the manager; the social payoff is non-contractible (a credence good). Only $x$ and profit $\pi$ are verifiable, so contracts pay one of three observed $(x,\pi)$ pairs. The key analytical device is the **mission integrity** (incentive-compatibility) constraint on $x$. Restricting the profit share to $a\in\{0,1\}$ yields three forms: FP (rigid $x=0$, full residual claimancy), NP (rigid $x=1$, flat wage), SE (manager has discretion over $x$ and is full residual claimant). The SE action is

$$x(\gamma_M;s)=\arg\max_{x\in\{0,1\}}\{\gamma_M\beta_s x+(1-x)\}\cdot\pi.$$

Section IV embeds this in a competitive two-sided matching model (Roth-Sotomayor one-to-one matching function $\phi$) with three founder and three manager types, transfers $T$ adjusting to clear the market, and stable assortative matching as the equilibrium concept.

## Data
None for the core theory. Section V references a companion lab experiment (Besley, Ghatak, and Marden 2015) in which subjects play a keep-earnings game, a donate game, and a discretion game, with Perry public-service-motivation tests used to measure pro-social motivation.

## Key findings
- **Observation 2**: in an SE, action depends on $\gamma_M$ — managers with $\gamma_M\in[\underline{\gamma},\overline{\gamma}]$ choose state-contingent actions, $\gamma_M>\overline{\gamma}$ always choose $x=1$, $\gamma_M<\underline{\gamma}$ always choose $x=0$. SE only adds value over FP/NP for the intermediate range.
- **Proposition 1**: effort in an SE is weakly higher than in an FP or NP, strictly higher for $\gamma_M\in(\underline{\gamma},\overline{\gamma})$, because delegated discretion lets the manager pick the payoff-maximizing action in each state, raising the return to effort.
- **Proposition 2** (organizational choice): for a given pair, whether FP/NP/SE is optimal trades off the SE's superior effort incentives against the founder's valuation of the non-rival social payoff $\gamma_F$. Higher $\gamma_F$ pushes toward NP; $\gamma_F<0$ (founder dislikes the mission) makes FP optimal — formalizing Friedman's (1970) view as a special case.
- **Proposition 4** (matching): under an elasticity-of-effort condition (effort elasticity $\varepsilon(z)<1$ plus a sufficient bound), the unique stable matching has $J(f_0,m_0)=\text{FP}$, $J(f_1,m_1)=\text{SE}$, $J(f_2,m_2)=\text{NP}$ — selfish pair in for-profit, mid-motivation pair in social enterprise, highly motivated pair in nonprofit. SEs survive competition for managers.
- A government with the same information could replicate the optimum via a state-contingent Pigouvian subsidy, but since $s$ is private this is infeasible — there is an implicit government failure that SEs partially address, most effectively when the cause is local (insiders value it far more than outside society).

## Contribution
The paper moves beyond the standard for-profit-versus-nonprofit (multitasking/nondistribution-constraint) framing by introducing heterogeneous, self-selecting motivated managers, so that social enterprise emerges endogenously as a third form. It reverses the usual "motivation substitutes for incentives" intuition ([[@Besley2005|Besley and Ghatak 2005]]): here, greater motivation *mitigates* the mission-integrity problem and thereby *permits higher-powered* financial incentives. It also delivers a matching model showing SEs are sustainable under competition, plus testable empirical predictions about which sectors should host SEs.

## Limitations & open questions
The authors flag several explicit open problems. (1) **Financing**: unlike NPs, SEs can issue equity — does shareholder influence undermine the profit-purpose balance over time (the "mission drift" concern)? (2) **Partial residual claimancy**: restricting $a\in\{0,1\}$ is for tractability; allowing $a\in(0,1)$ expands the SE region but lowers SE effort, modifying the headline effort ranking. (3) **Private politics**: outside citizens' valuations $\sum_i\gamma_i\theta_s$ could be made to influence the mission directly (Baron 2001), with strategic delegation by founders (Besley and Coate 2001). (4) **Self-selection under asymmetric information about types**: stable assortative matching does not by itself guarantee managers self-select back if types are concealed. (5) Applications beyond classic social enterprise to sports franchises and media ownership. (6) Whether pro-social values are hardwired or pliable determines what is achievable.

## Connections
The model extends the motivated-agents framework of [[@Besley2005|Besley & Ghatak (2005)]] and the broader motivation-and-incentives literature (Bénabou & [[@Benabou2006|Tirole]] (2006, 2010); Akerlof & Kranton (2005); Francois (2000); Delfgaauw & Dur (2010); Kosfeld & von Siemens (2011)). It builds on the nonprofit/nondistribution-constraint tradition of Hansmann (1980), Weisbrod (1988), and Glaeser & Shleifer (2001), and the multitasking logic of Holmstrom & Milgrom (1991). The delegation-improves-incentives channel echoes [[@Aghion1997|Aghion & Tirole (1997)]]. Founder/manager motivation is interpreted as warm glow in the sense of Andreoni (1990), with heterogeneity as in Andreoni & Payne (2013). The CSR literature (Baron (2001); Bagnoli & Watts (2003); Besley & Ghatak (2007); Kotchen (2006)) is contrasted, since it stresses profitability of pro-social action rather than a profit-mission trade-off. The state-contingent action problem parallels political agency models (Besley (2004); Maskin & Tirole (2004); Smart & Sturm (2013)), and the matching uses Roth & Sotomayor (1989). The framing engages directly with Friedman's (1970) critique of corporate social responsibility.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
