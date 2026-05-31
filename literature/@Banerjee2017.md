---
citekey: Banerjee2017
title: "Other‐regarding principal and moral hazard: The single‐agent case"
authors: ["Banerjee, Swapnendu", "Sarkar, Mainak"]
year: 2017
type: journalArticle
doi: 10.1111/ijet.12131
zotero: "zotero://select/library/items/QUA2X5A4"
pdf: /Users/jesper/Zotero/storage/GJRMHGIR/Banerjee and Sarkar - 2017 - Other‐regarding principal and moral hazard The single‐agent case.pdf
tags: [literature]
keywords: [moral-hazard, other-regarding-preferences, inequity-aversion, optimal-contract, limited-liability, principal-agent]
topics: ["[[social-preferences-contract-theory]]"]
related: [Englmaier2010, Fehr1999, Itoh2004]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Using the classic moral hazard problem with limited liability, we characterize the optimal incentive contracts when first an other-regarding principal interacts with a self-regarding agent. The optimal contract differs considerably when the principal is "inequity averse" vis-a-vis the self-regarding case. Also the agent is generally (weakly) better-off under an "inequity averse" principal compared to a "status seeking" principal. Then we extend our analysis and characterize the optimal contracts when both other-regarding principal and other-regarding agent interact.

## Summary
This is a theory paper that takes the textbook single-agent, hidden-action, limited-liability moral hazard model and replaces the standard self-interested principal with an *other-regarding* principal whose utility depends on the payoff gap between herself and the agent. It then layers in an other-regarding agent. The central message: who is "inequity averse" versus "status seeking" reshapes the optimal wage contract in qualitatively distinct ways. A status-seeking principal reproduces the standard self-regarding contract, but an inequity-averse principal optimally pays a higher success wage (sometimes a positive failure wage), breaking limited liability and altering rent extraction.

## Research question
How do the predictions of the classic moral hazard contract change when the principal (not just the agent) has social preferences? Specifically, what are the optimal limited-liability incentive contracts when (i) an other-regarding principal faces a self-regarding agent, and (ii) both parties are other-regarding, and how do "inequity aversion" versus "status seeking" on either side alter contract form and the parties' welfare?

## Method / identification
Pure theory. A risk-neutral principal hires a risk-neutral, income-constrained agent for a binary-outcome project: success returns $b$, failure returns $0$. The agent chooses high effort $e_1$ (cost $d$) or low effort $e_0$ (cost $0$); success probabilities satisfy $1>p_1>p_0>0$, with $\Delta p=p_1-p_0$. The principal offers a contract $(w_1,w_0)$ with limited liability $w_j\ge 0$. Assumption 1 ($\Delta p\,b > p_1 d/\Delta p$) ensures high effort is optimal to elicit.

The benchmark self-interested principal maximizes $p_1 b-[p_1 w_1+(1-p_1)w_0]$ subject to participation $p_1\Delta w + w_0\ge d$, incentive compatibility $\Delta w\,\Delta p\ge d$, and limited liability.

The innovation is a Fehr-Schmidt / Neilson-Stowe piecewise-linear other-regarding utility for the principal:
$$U_P=\begin{cases} b_j-w_j-\pi\rho\, f(b_j-2w_j), & b_j-w_j\ge w_j\ \text{(principal ahead)}\\ b_j-w_j-\pi\, f(2w_j-b_j), & b_j-w_j\le w_j\ \text{(principal behind)}\end{cases}$$
with $\pi>0$ the weight on the gap, $f(0)=0$, $f'(z)>0$. The sign of $\rho$ classifies the principal: $\rho>0$ is *inequity averse*, $\rho<0$ is *status seeking*; when behind she is always inequity averse. In Section 4 the agent gets a symmetric structure with weight $\alpha$ and sign parameter $\gamma$, and effort-cost-adjusted incentive constraints (ICa) when ahead and (ICb) when behind. Optimal contracts are derived case-by-case via first-order conditions on $\partial U_P/\partial w_1$ and $\partial U_P/\partial w_0$, comparing the relative size of the "direct wage payment" effect ($-1$) and the "inequity reduction" effect ($2\pi\rho f'(\cdot)$).

## Data
None - this is an analytical contract-theory paper with no empirical or experimental component.

## Key findings
- **Benchmark (Claim 1):** the unique optimal contract is $(w_1^*=d/\Delta p, w_0^*=0)$; participation does not bind and the agent earns a rent $p_0 d/\Delta p$.
- **Proposition 1 (other-regarding principal, self-regarding agent, $b/2>d/\Delta p$):** (a) if status seeking ($\rho<0$), the standard contract $(d/\Delta p,0)$ remains uniquely optimal; (b) if inequity averse ($\rho>0$) and $2\pi\rho f'(b-2w_1)>1$, the unique optimum is the "bang-bang" $(w_1^*=b/2, 0)$ that equalizes net payoffs; (c) the knife-edge case $2\pi\rho f'(b-2w_1)=1$ yields interior or a continuum of optima depending on whether $f$ is linear.
- **Proposition 2:** the agent is (weakly) better-off under an inequity-averse principal than a status-seeking one.
- **Alternative specification (Lemma 1, Proposition 3, Claim 2):** when the principal compares *net* payoffs $b_j-w_j$ to $w_j-d$, limited liability need not bind; a sufficiently inequity-averse principal may optimally pay a positive failure wage $w_0=d/2$ and success wage $(b+d)/2$, otherwise the standard $(d/\Delta p,0)$ holds.
- **Proposition 4 (both other-regarding, $b/2\ge d/\Delta p$):** for a status-seeking principal, $(\tilde w_1,0)$ defined by binding (ICb) is the unique optimum if $1>2\pi\rho f'(z)$ and $1>2\alpha\gamma v'(z)$, replicating the [[@Itoh2004|Itoh (2004)]] structure.
- **Proposition 5:** a status-seeking principal is unambiguously worse-off the more other-regarding the agent; an inequity-averse principal is also worse-off iff $2\pi\rho f'(z)<1$.
- **Proposition 6 ($b/2<d/\Delta p$):** the principal is always behind, hence inequity averse, and always prefers a status-seeking agent (whom she can incentivize at lower wage cost).

## Contribution
[[@Itoh2004|Itoh (2004)]] studied a self-regarding principal facing an other-regarding agent and mentioned but did not analyze the other-regarding-principal case. This paper fills that gap, characterizing optimal limited-liability contracts when the *principal* is other-regarding, and then with both sides other-regarding. The key conceptual addition is that principal-side inequity aversion can endogenously break the limited-liability bound and raise the success (and even failure) wage above the standard incentive-compatible minimum, with welfare orderings over the principal's and agent's "type" combinations.

## Limitations & open questions
- The analysis is confined to a **single principal-single agent** interaction; the authors explicitly flag the **multi-agent case as the natural extension** (reserved for a companion / future paper), warning that defining the principal's other-regardingness across multiple agents is non-trivial.
- A **"pathological" sub-case** (Proposition 4 / footnote 20): when the principal is strongly inequity averse, $\pi f(2w_1-b)-\pi\rho f(b-2\tilde w_1)$ may be negative, admitting contracts with $w_1>b/2$ and $w_0>0$; uniqueness then requires the moderate-inequity-aversion restriction (Assumption 3).
- Risk neutrality of both parties, a binary outcome and binary effort, and a zero outside option are maintained throughout; relaxing these (continuum effort/outcomes, $u>0$, risk aversion) is left open.
- All derived contracts are inefficient (first-best is never implementable), so the welfare loss is not characterized beyond existence.

## Connections
The model is the direct successor to [[@Itoh2004|Itoh (2004)]], "Moral hazard and other-regarding preferences," whose self-regarding-principal results it nests and extends. The social-preference utility form is the piecewise-linear inequity-aversion model of [[@Fehr1999|Fehr & Schmidt (1999)]], adapted via Neilson & Stowe (2003)'s "incentive pay for other-regarding workers" and their status-seeking/inequity-averse terminology. Closely related contract-theoretic work includes [[@Englmaier2010|Englmaier & Wambach (2010)]] on optimal contracts under inequity-averse agents, Dur & Glazer (2008) on contracts when workers envy their bosses, Englmaier & Leider (2008) on reciprocal agents, and Hart & Moore (2008) on contracts as reference points (incomplete-contracting setting). The behavioral motivation draws on the ultimatum-game evidence of Guth, Schmittberger & Schwarze (1982), Forsythe et al. (1994), and the survey treatments by Camerer (2003) and Englmaier (2005).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
