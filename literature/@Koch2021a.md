---
citekey: Koch2021a
title: Contract design with socially attentive preferences
authors: ["Koch, Simon", "Weinschenk, Philipp"]
year: 2021
type: journalArticle
doi: 10.1016/j.geb.2021.10.002
zotero: "zotero://select/library/items/SUE79YET"
pdf: /Users/jesper/Zotero/storage/JLL498HU/Koch and Weinschenk - 2021 - Contract design with socially attentive preferences.pdf
tags: [literature]
keywords: [principal-agent-model, social-preferences, moral-hazard, incentive-contracts, adverse-selection, limited-liability]
topics: ["[[social-preferences-contract-theory]]"]
related: [Andreoni2002, Benabou2006, Besley2005, Englmaier2010, Itoh2004]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The standard agency model assumes that the agent does not care how his decisions influence others. This is a strong assumption, which we relax. We find that, although monetary incentives are also effective with socially attentive agents, the principal may optimally set none. This could explain the puzzle why empirically only a fraction of employees experiences monetary incentives. Furthermore, in case the agent's type is private information, the principal optimally offers a single pooling contract, i.e., never screens for different types, no matter how rich the set of possible attentiveness levels is and what shape the underlying distribution function has.

## Summary
Koch and Weinschenk embed "socially attentive" preferences (the agent places weight $\beta\in[0,1]$ on the utilities of the principal and a third party) into an otherwise standard risk-neutral, limited-liability moral-hazard model. Monetary incentives remain effective, but because a socially attentive agent responds less strongly to them, the principal optimally provides either no incentives or rather weak ones once $\beta$ is high enough. Under adverse selection over $\beta$, screening is never optimal: the principal always offers a single pooling contract, regardless of the richness of the type set or the shape of the distribution. The paper frames both results as theoretical explanations for empirical puzzles—the scarcity/weakness of performance pay and the uniformity of observed contracts.

## Research question
How does relaxing the standard assumption that agents are indifferent to how their effort affects others (the principal and an external third party) change the structure of the optimal incentive contract, both when the agent's degree of social attentiveness is observable and when it is private information?

## Method / identification
Theoretical principal–agent model. A risk-neutral principal hires a risk-neutral agent who exerts non-contractible effort $e\in[0,e_{\max}]$, generating a probability distribution $p_i(e)$ over outcomes $\{1,\dots,n\}$. Outcome $i$ yields return $R_i$ to the principal and payoff $V_i$ to a third party (customers, environment, coworkers). A contract is a vector of outcome-contingent payments $(t_1,\dots,t_n)$ bounded below by a limited-liability floor $t_i\ge\underline{t}\ge 0$. The agent's utility under outcome $i$ is

$$u_A = t_i - c(e) + \beta u_P + \beta u_T,$$

with $u_P=R_i-t_i$ and $u_T=V_i$, so expected agent utility is $E[u_A]=\sum_i p_i(e)\,(t_i+\beta(R_i-t_i+V_i))-c(e)$. This is the weighted-utilitarian formulation (justified via Balasubramanian 2015). Standard assumptions: $c$ convex with $c(0)=c'(0)=0$ and $\lim_{e\to e_{\max}}c'(e)=\infty$; the monotone likelihood ratio property $p'_i(e)/p_i(e)<p'_{i+1}(e)/p_{i+1}(e)$; and $p_n$ increasing and concave in $e$.

The solution uses a first-order (relaxed) approach. Limited liability makes the participation constraint slack automatically. A reduction argument (Proposition 1, generalizing Demougin & Fluet 1998) shows only the maximal-likelihood-ratio outcome is ever rewarded, collapsing the problem to two outcomes with payment spread $\Delta t:=t_2-t_1$, return spread $\Delta R$, and externality spread $\Delta V$. The incentive constraint becomes the local FOC $p'(\hat e)(\Delta t+\beta(\Delta R-\Delta t+\Delta V))-c'(\hat e)=0$. The principal then maximizes $E[u_P]$ over $\Delta t\ge 0$, using $\partial\hat e/\partial\Delta t$ from implicit differentiation and a concavity refinement ($c'''\ge 0$, $p'''\le 0$) for monotone-comparative-statics results. Under adverse selection, $\beta\sim F$ on $[\underline\beta,\bar\beta]$; the pooling-optimality proof (Appendix A) replaces any candidate menu of binary contracts with a single contract that weakly improves every type and strictly improves at least one, handling both finite and infinite menus (the latter via a supremum construction). A closed-form quadratic-cost example ($c(e)=\alpha e^2$, $p(e)=e$) illustrates throughout.

## Data
None—this is a pure theory paper. It does, however, motivate and interpret its predictions against external empirical evidence on performance pay (Lemieux, MacLeod & Parent 2009: only 37% of US workers in performance-pay jobs; Bryson et al. 2012; Gittleman & Pierce 2013) and on the prevalence of altruism/warm-glow ([[@Andreoni2002|Andreoni & Miller 2002]]; Engel 2011).

## Key findings
- **Proposition 1 (binary structure).** It is optimal to reward at most the single outcome with the maximal likelihood ratio: $t_i^*=\underline{t}$ for $i<n$ and $t_n^*\ge\underline{t}$. The $n$-outcome problem reduces to two outcomes.
- **Incentive effectiveness.** $\partial\hat e/\partial\Delta t>0$ for all $\beta\in[0,1)$: incentives raise effort even for socially attentive agents, but the response is scaled by $(1-\beta)$, so attentive agents react more weakly.
- **Proposition 2 (when to set incentives).** If $\beta=0$ or $\beta$ is small, the principal optimally provides incentives ($\Delta t^*>0$). If $\beta$ is sufficiently high, she optimally sets none ($\Delta t^*=0$, i.e., a fixed wage). This is not a limit result—zero incentives can be optimal at moderate $\beta$.
- **Proposition 3 (monotonicity).** Under the concavity condition, whenever $\Delta t^*>0$ it is monotonically decreasing in attentiveness: $\partial\Delta t^*/\partial\beta<0$.
- **Example.** With quadratic costs, $\Delta t^*=\frac{\Delta R}{2}$ for $\beta<\frac{\Delta R}{2\Delta R+\Delta V}$ and $\Delta t^*=0$ otherwise; the threshold lies in $(0,1/2)$ and equals $1/3$ when $\Delta R=\Delta V$.
- **Proposition 4 (pooling under adverse selection).** When $\beta$ is private, screening is never optimal—any menu is dominated by a single pooling contract, regardless of how rich the type space is or the shape of $F$.
- **Averaging / FOSD result.** The pooling design weighs the average effect of incentives; if higher $\beta$ is more likely (first-order stochastic dominance), optimal incentives are weaker. Whenever $F(\beta=0)<1$, incentives are strictly below the surely-egoistic benchmark; e.g., a fixed wage is optimal even when there is a one-in-three chance the agent is egoistic and $\beta\sim U[0,1]$.

## Contribution
The paper relaxes the egoism assumption of the canonical moral-hazard model with a tractable, axiomatically grounded weighted-utilitarian preference. Substantively it offers two theory-based resolutions of empirical puzzles: (i) the widespread absence or weakness of performance pay, and (ii) the observed uniformity of contracts (most firms post a single contract rather than menus). Methodologically, Proposition 4's pooling result is notably general—it holds for arbitrarily rich type sets and any distribution—because the limited-liability floor pins $t_1^*=\underline{t}$ across all types, making any separating menu unravel.

## Limitations & open questions
- Equal weights $\beta$ are placed on the principal's and the third party's utilities "without much loss of generality"; allowing distinct weights (and signed externalities, $\Delta V<0$ harmful third parties) is left informal.
- Both principal and agent are risk-neutral; risk aversion is not analyzed.
- The third party is passive—no strategic or market response is modeled.
- The first-order/relaxed approach relies on concavity of the agent's program; global validity for general $p,c$ outside the stated conditions is not fully resolved (e.g., Proposition 3 needs the extra $c'''\ge 0,\,p'''\le 0$ condition).
- Social attentiveness is exogenous and fixed; endogenous formation, crowding-out of intrinsic motivation (flagged via Bénabou & [[@Benabou2006|Tirole 2006]]), and dynamics are outside scope.

## Connections
The model directly generalizes the sufficient-statistic/limited-liability agency results of Demougin & Fluet (1998). It sits within the literature embedding social preferences in agency: [[@Itoh2004|Itoh (2004)]], [[@Englmaier2010|Englmaier & Wambach (2010)]], and Bartling (2011) on inequity-averse and status-seeking agents; Kräkel (2016) on peer effects; [[@Besley2005|Besley & Ghatak (2005)]] on mission-motivated agents; and Cassar & Armouti-Hansen (2020) on misaligned project missions and endogenous mission choice. On adverse selection with social preferences it relates to Delfgaauw & Dur (2007), Arce (2013), and Non (2012). The preference foundation draws on weighted utilitarianism (Balasubramanian 2015) and on evidence for altruism and warm-glow (Andreoni, Harbaugh & Vesterlund 2008; [[@Andreoni2002|Andreoni & Miller 2002]]; Engel 2011; DellaVigna, List & Malmendier 2019). The empirical motivation rests on the performance-pay incidence literature (Lemieux, MacLeod & Parent 2009; Bryson et al. 2012; Gittleman & Pierce 2013) and on the broader incentive-strength puzzle (Williamson 1985; Holmström & Milgrom 1990; Che & Yoo 2001). The mixed moral-hazard/adverse-selection framework follows Laffont & Martimort (2001).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
