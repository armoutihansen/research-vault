---
citekey: Simester2010
title: Why Are Bad Products So Hard to Kill?
authors: ["Simester, Duncan", "Zhang, Juanjuan"]
year: 2010
type: journalArticle
doi: 10.1287/mnsc.1100.1169
zotero: "zotero://select/library/items/NKR7J778"
pdf: /Users/jesper/Zotero/storage/ARWNZTC4/Simester and Zhang - 2010 - Why Are Bad Products So Hard to Kill.pdf
tags: [literature]
keywords: [managerial-incentives, moral-hazard, product-development, principal-agent, information-acquisition, limited-liability, escalation-of-commitment]
topics: ["[[career-concerns-subjective-evaluation]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> It is puzzling that firms often continue to invest in product development projects when they should know that demand will be low. We argue that bad products are hard to kill because firms face an inherent conflict when designing managers' incentives. Rewarding success encourages managers to forge ahead even when demand is low. To avoid investing in low-demand products, the firm must also reward decisions to kill products. However, rewarding managers for killing products effectively undermines the rewards for success. The inability to resolve this tension forces the firm to choose between paying an even larger bonus for success and accepting continued investment in low-demand products. We explore the boundaries of this argument by analyzing how the timing of demand information affects product investment decisions.

## Summary
A principal-agent model explaining why firms persist in funding product-development projects their managers already know will fail. The mechanism is not behavioral bias but an incentive incompatibility: a success bonus needed to motivate effort makes it expensive to also pay managers to kill bad products, because a termination bonus erodes the success incentive. When that joint cost is high enough, the firm rationally prefers to keep funding low-demand products. The paper then shows the timing of demand information governs whether the tension bites: early information dissolves it, while firm uncertainty about that timing amplifies it.

## Research question
Why do firms continue investing in product-development projects when (the manager knows) demand will be low? More precisely: can a firm that anticipates managerial distortions simply contract them away, and if not, what feature of the optimal incentive contract makes "killing bad products" inherently costly?

## Method / identification
A single-principal, single-agent moral-hazard model with hidden effort and hidden (privately observed) demand. A risk-neutral firm hires a risk-neutral manager to develop a product returning $Y>0$ on success and $0$ on failure. Success probability depends on effort and on demand (Table 2): with effort, $a$ if demand is high and $b_E$ if low; without effort, $b_D$ if high and $0$ if low, with $0<b_i<a<1$. Demand is high with prior probability $s$. Continued development costs $Z$, with the maintained Condition (1): $b_i Y < Z < aY$ for $i\in\{D,E\}$, so continuation is efficient only under high demand plus effort. Effort costs $c$; the manager has limited liability (minimum wage $0$) and a zero outside option.

Timing (baseline): the manager is hired, chooses effort (cost $c$) before observing demand, observes demand, recommends kill/continue; if killed the manager receives a fixed termination bonus $X\ge 0$, otherwise the firm invests $Z$ and the manager earns success bonus $W\ge 0$ on success, $0$ on failure. The firm chooses only $(W,X)$ — a fixed wage is dominated, and the menu interpretation follows endogenously.

The firm compares two regimes by solving constrained profit-maximization programs. The "kill" program maximizes $\Pi_K = s(aY-Z) - saW - (1-s)X$ subject to three incentive constraints: continue high-demand $aW\ge X$ (IC1), kill low-demand $X\ge b_E W$ (IC2), and exert effort (IC3). The "no-kill" program replaces IC2 with $b_E W\ge X$ so low-demand products continue. The paper proves binding constraints pin down closed-form contracts, e.g. $W_K^*=c/[s(a-\max(b_D,b_E))]$ and $X_K^*=b_E W_K^*$, with $W_{NK}^*<W_K^*$. Extensions: a continuous-effort/continuous-demand version, and reinterpretations covering information distortion, discrediting, and forgone collection. Timing variants reverse the effort/demand order and introduce firm uncertainty $q$ about whether information arrives early, plus endogenous information acquisition.

## Data
None — this is a theory paper. The model assumptions are motivated by qualitative background interviews with product-development and market-research participants (e.g., a healthy-snacks manager avoiding market tests; a manager staging a field test by installing point-of-sale displays), used illustratively rather than as estimated data.

## Key findings
- Benchmarks: under full integration (first-best) or verifiable effort, the firm achieves $s(aY-Z)-c$ using infinitesimal $W,X$ with $aW\ge X\ge b_E W$. The tension exists only when effort is non-contractible.
- Proposition 1: if the firm can observe neither effort nor demand, it may be optimal to keep investing after the manager learns demand is low. The kill-vs-continue choice reduces to Condition (2), trading the expected loss $(1-s)(Z-b_E Y)$ against the payroll saving from dropping the termination bonus. The wage premium $ck$ over effort cost rises in both $b_D$ and $b_E$ — any chance a bad product succeeds makes it costlier to induce termination.
- Proposition 2: in the continuous model, contractible effort yields first-best, but unobservable effort forces overcompensation and rules out efficient termination — confirming the discrete result is not an artifact.
- Behavioral biases are complementary, not causal: an anticipating firm can contract around belief distortions, but optimism raises the required termination bonus and so amplifies the tension.
- Proposition 3: if the manager observes demand before choosing effort, the firm invests only in high-demand products — a manager indifferent about working on a high-demand product strictly prefers shirking on a low-demand one, so bad products die cheaply (supporting "gated"/"phased" development).
- Proposition 4: mere firm uncertainty about whether the manager receives early information ($0<q<1$) can make continued investment in low-demand products more profitable; higher $q$ favors paying a lower salary and tolerating occasional bad investments.
- Endogenous timing: with no acquisition cost the manager always acquires information early ($U_A\ge U_N$), eliminating bad investment; even with positive cost, the option of early acquisition can make killing bad products more likely.

## Contribution
Reframes the well-documented "escalation of commitment" / failure-to-kill phenomenon as a rational contracting outcome rather than a psychological pathology. The novel point is the structural conflict between a reward for success (to elicit effort) and a reward for termination (to elicit truthful demand reporting): the two cannot be cheaply satisfied at once under limited liability and hidden effort. It unifies several observed managerial behaviors (suppressing, distorting, discrediting, not collecting information) under one mechanism, and delivers managerial implications: phased/gated development and small sequential market tests help kill bad products, whereas firm uncertainty about information timing hurts.

## Limitations & open questions
- Limited liability is assumed; with sufficiently large punishments for recommending a failed investment, the firm would not need to reward success and the tension could vanish — the authors flag how negative-wage bounds drive results.
- Effort is binary in the core model (effort/no-effort, zero success without effort); robustness to high-vs-very-high effort and to monitoring is argued but the main exposition relies on conveniences.
- Random monitoring is shown to be non-credible (the firm must be indifferent about monitoring), leaving open richer commitment or auditing technologies.
- The authors propose future work on alternative resolution mechanisms — e.g., the Guedj and Scharfstein (2004) portfolio mechanism (firms with more drugs in development abandon weak ones faster), which they note may discipline firm-level decisions but not individual managers given the depth of involvement a single project demands.
- They suggest extending the intuition to other marketing decisions (pricing experiments, product-line design, channel-relationship investments) where rewarding success may invite abuse.

## Connections
The paper contrasts itself with the escalation-of-commitment literature (Brockner & Rubin 1985; Brockner 1992; Boulding et al. 1997) and belief-bias accounts such as Biyalagorsky et al. (2006) on "belief inertial distortion" and March & Shapira (1987) on "managerial conceit," arguing biases complement rather than cause the inefficiency. It builds on the hidden-effort/hidden-information contracting tradition: Holmstrom & Milgrom (1987) on multitask incentives, Demski & Sappington (1987) and Baiman & Sivaramakrishnan (1991) on contractibility of reports, and Hauser (1998) and Hauser et al. (1997) on R&D metrics and side payments. Related capital-allocation and information-acquisition work includes Bernardo, Cai & Luo (2001), Laux (2008), Shin (2008), Guo (2009), Levitt & Snyder (1997), Desai & Srinivasan (1995), and Friebel & Raith (2010). The risk-aversion-as-barrier-to-innovation strand (Sung 1995; Bergmann & Friedl 2008; Lambert 1986; De Paola & Scoppa 2006; Bester & Krahmer 2008; Im & Nakata 2008; Maine 2008) is contrasted, since the present model is risk-neutral. Random-monitoring impossibility draws on Townsend (1979) and Border & Sobel (1987); the portfolio mechanism on Guedj & Scharfstein (2004).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
