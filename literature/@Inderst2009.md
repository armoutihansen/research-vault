---
citekey: Inderst2009
title: Misselling through Agents
authors: ["Inderst, Roman", "Ottaviani, Marco"]
year: 2009
type: journalArticle
doi: 10.1257/aer.99.3.883
zotero: "zotero://select/library/items/7CHDE84X"
pdf: /Users/jesper/Zotero/storage/4D38G7Y4/Inderst2009.pdf
tags: [literature]
keywords: [misselling, multi-task-agency, suitability-standard, sales-commissions, consumer-protection, cheap-talk-advice, credence-goods, salesforce-compensation]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This paper analyzes the implications of the inherent conflict between two tasks performed by direct marketing agents: prospecting for customers and advising on the product's "suitability" for the specific needs of customers. When structuring salesforce compensation, firms trade off the expected losses from "misselling" unsuitable products with the agency costs of providing marketing incentives. We characterize how the equilibrium amount of misselling (and thus the scope of policy intervention) depends on features of the agency problem including: the internal organization of a firm's sales process, the transparency of its commission structure, and the steepness of its agents' sales incentives. (JEL M31, M37, M52)

## Summary
Inderst and Ottaviani recast "misselling" — selling a product ill-matched to a customer's needs — not as the misconduct of an entrepreneurial credence-goods seller, but as a symptom of an **internal multi-task agency problem** inside the selling firm. A single risk-neutral agent must both *prospect* for customers (costly hidden effort) and *advise* on whether the product suits the customer (using a private signal). The commission needed to motivate prospecting simultaneously tempts the agent to recommend purchase indiscriminately. The firm sets a compensation scheme that implements a **suitability standard** $s^*$ (sell only when the signal $s\ge s^*$), trading expected misselling penalties against the agency rent it must pay. The central message: the equilibrium standard — and hence the scope for regulation — depends on organizational variables (prospecting difficulty, monitoring quality, commission transparency, task separation, contract resale, competition) that are invisible if one models the firm as a self-employed professional. A firm that sells through agents under-provides suitability relative to a social planner even when it can commit to penalties exactly as a regulator could.

## Research question
When a firm sells complex products through agents who both find customers and advise them, what determines the equilibrium amount of misselling, and how does the *internal* principal–agent relationship (rather than firm–customer conflict alone) shape the optimal compensation scheme and the appropriate scope of policy intervention?

## Method / identification
A fully specified **game-theoretic principal–agent model** with cheap-talk advice, solved for perfect Bayesian equilibrium using Grossman–Hart's (1983) two-stage approach (first the agency cost of any standard, then the optimal standard).

Setup: a risk-neutral firm and a risk-neutral, limited-liability agent. Exerting prospecting effort at private cost $c_S>0$ yields a customer contact with probability $\mu$. There are two customer types $\tau=l,h$ with utilities $u_l<0<u_h$, prior $\Pr[\tau=h]=q$, and possibly type-dependent serving cost $k_\tau$. The agent privately observes a presale signal $s\in[0,1]$ drawn from type-dependent distributions $F_\tau$, with $F_h$ dominating $F_l$ in the **monotone likelihood ratio** order, so the posterior $q(s)=\Pr[\tau=h\mid s]$ is strictly increasing, with $q(0)=0$, $q(1)=1$. A post-sale signal reveals a sale to a type-$l$ customer with probability $\phi\in(0,1)$ (e.g. a verifiable complaint); the firm then pays an expected penalty $L$, a fraction $\gamma\in[0,1]$ of which is rebated to the customer. Timing: firm sets price $p$, then compensation; agent prospects, observes $s$, advises; customer buys or not; penalty is realized on bad post-sale signals.

The contract reduces to a base salary $w$ (paid when no sale) and a commission $b$ (paid for an uncontested sale); paying zero after a bad post-sale signal is optimal. The agent's expected pay from a sale at signal $s$ is $V(s)=[1-\phi(1-q(s))](w+b)$. The marginal-customer indifference condition pins the standard:
$$\frac{b}{w}=\frac{\phi[1-q(s^*)]}{1-\phi[1-q(s^*)]},$$
and a binding prospecting-incentive constraint $\int_{s^*}^{1}[V(s)-w]f(s)\,ds=c_S/\mu=:C$ closes the contract. The key friction is an **attribution problem**: a no-sale outcome could mean the agent failed to prospect *or* correctly advised against buying, so the firm cannot reward the two tasks separately. The customer's willingness to pay under anticipated standard $s^*$ is $\hat p(s^*)=\int_{s^*}^{1}u(s)\frac{f(s)}{1-F(s^*)}ds$ with $u(s)=q(s)u_h+[1-q(s)](u_l+\gamma L)$; equilibrium is the fixed point of the firm's willingness-to-sell curve $\hat s^*(p)$ and the willingness-to-pay curve $\hat p(s^*)$ (Figure 1). Extensions add a private advising cost $c_A$, task separation across two agents, contract resale, and elastic/competitive demand $\rho(z^*)$. Appendix A gives a discrete "toy" version where the agent perfectly observes the type.

## Data
None — this is a pure theory paper. Institutional motivation is drawn from FINRA/NASD suitability rules (Conduct Rule 2310), the UK pension- and endowment-mortgage misselling scandals (reportedly £12 billion in compensation), MiFID commission-disclosure rules, and the US subprime mortgage market; an empirical regularity from Hubbard (1998) on vehicle inspections and Minton–Sanders–Strahan (2004) on loan retention is cited as consistent with the predictions, but nothing is estimated.

## Key findings
- **Proposition 1 (optimal compensation):** implementing standard $s^*>0$ requires the base salary $w=\frac{C[1-\phi[1-q(s^*)]]}{\int_{s^*}^1\phi[q(s)-q(s^*)]f(s)ds}$ and commission $b$ given correspondingly; paying zero after a bad post-sale signal minimizes wage cost.
- **Proposition 2 (agency rent comparative statics):** the agent earns a positive rent equal to $w$, which rises in the standard $s^*$ and in prospecting cost $C$, and falls in monitoring quality $\phi$. The firm's marginal cost of raising the standard $dw/ds^*$ rises in $C$ and falls in $\phi$.
- **Proposition 3 (equilibrium standard):** the equilibrium $s^*$ increases in the penalty $L$ and in monitoring effectiveness $\phi$, and decreases in prospecting cost $C$ and in the customer-compensation fraction $\gamma$. At the optimum the firm makes a *loss on the marginal sale*, $\pi(s^*)<0$, because a lower standard cuts ex-ante agency costs.
- **Proposition 4 (agency vs. policy):** if a firm could self-impose penalties with the same technology as a regulator, an *entrepreneurial* firm would choose exactly the planner's standard, but a firm selling **through an agent chooses a strictly lower** $L$ and standard $s^*$ than the planner — the agent's rent is a transfer to the planner but a cost to the firm. Self-regulation is therefore insufficient.
- **Proposition 5 (transparency):** credibly disclosing the commission scheme raises the standard for any $L$; the new first-order condition gains a term $\frac{d\hat p}{ds^*}[1-F(s^*)]$ capturing the price benefit of a visible higher standard. Transparency acts as a commitment device that entrepreneurial firms lack — though voluntary disclosure may not be credible.
- **Propositions 6–7 (sales organization):** an extra advising cost $c_A$ raises both salary and commission needed for a given standard; crucially, **separating prospecting and advising across two agents yields a strictly higher standard** than bundling both tasks in one agent, because the attribution problem disappears.
- **Proposition 8 (contract resale):** when $k_l>k_h$, the more contracts a firm resells, the lower the equilibrium standard and the steeper the agent's incentives ($b/w$) — rationalizing why commission-paid finance-company loan officers may missell more than salaried bank officers.
- **Proposition 9 (competition):** with elastic residual demand $\rho(z^*)$, a reduction in demand lowers the standard through two channels (higher marginal agency cost, and less weight on the ex-post loss $\pi(s^*)<0$); multiple equilibria can arise. Contrary to Bolton–Freixas–Shapiro (2007), **more competition can worsen misselling** when it makes prospecting harder.

## Contribution
The paper opens up the *internal agency problem* in the analysis of misselling and credence goods, a dimension absent from the prior literature (which treated sellers as entrepreneurs). It shows that the level of misselling, and the very *list of variables* that affect it — prospecting difficulty/competition, monitoring quality, commission transparency, the division of sales labor, and contract resale — are determined by the firm-agent relationship. This delivers two policy lessons: (i) self-regulation cannot reach the efficient standard because firms do not internalize agency rents as social costs, justifying regulatory penalties and mandated commission disclosure; and (ii) because firms in the same industry differ in organization, a *uniform* policy instrument is generically miscalibrated, calling for a finer-tuned, organization-contingent regulatory approach.

## Limitations & open questions
- The authors explicitly note a **policy implementation problem they do not solve**: because the efficient standard differs across firms that organize their sales process differently (single vs. separated agents) or resell contracts to different degrees, a single uniform penalty $L$ cannot implement firm-appropriate standards — "a uniform policy may be too harsh on some but too lenient on other firms."
- **Future work could adapt the framework to particular industries** to explain cross-country differences in regulation and industry organization; the authors flag a two-way feedback between policy and the equilibrium organization of an industry (competition, vertical integration, use of independent intermediaries) that is left unmodeled.
- The disclosure result is fragile: voluntary commission transparency "may not be credible" because customers lack means to monitor remuneration and firms can substitute toward *implicit/less observable* incentives — how policy can make disclosure credible is left open.
- Under elastic demand the model admits **multiple equilibria**, and the net competitive effect on the standard "depends on specific circumstances" (intensified rivalry among incumbents vs. entry that erodes market share) — an equilibrium-selection and empirical question.
- The monitoring technology is stylized (a single noisy post-sale signal $\phi$, with a footnoted audit-fraction alternative); richer compliance/auditing designs are not explored.

## Connections
The model is a direct-marketing instance of the **multi-task agency** problem of Holmström & Milgrom (1991), in the spirit of Levitt & Snyder (1997) and Dewatripont & Tirole (1999), and uses the Grossman & Hart (1983) two-stage method. Its advice stage is a **cheap-talk / strategic information transmission** game in the lineage of Crawford & Sobel (1982), Dessein (2002), and Alonso & Matouschek (2008), but here the agent–customer preference divergence is *endogenous* to the firm's commission choice rather than exogenous; it relates to the "delegated expertise" models of Lambert (1986), Demski & Sappington (1987), Lewis & Sappington (1997), Garicano & Santos (2004), and Gromb & Martimort (2007). The firm-bears-responsibility assumption draws on the **vicarious liability** literature (Pitchford 1995; Che & Spier 2006). The paper extends the **credence/experience goods** tradition of Darby & Karni (1973) (surveyed by Dulleck & Kerschbamer 2006) by adding the internal agency problem, and contrasts sharply with **Bolton, Freixas & Shapiro (2007)** on competition and advice and with **DeMarzo, Fishman & Hagerty (2005)** on self-regulatory anti-fraud standards. A signaling-through-observable-commissions antecedent is Kalra, Shi & Srinivasan (2003); the empirical touchstones are Hubbard (1998) and Mian & Sufi (2008). The disclosure analysis speaks to Jackson's (2007) "trilateral dilemma" in retail-finance regulation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
