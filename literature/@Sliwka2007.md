---
citekey: Sliwka2007
title: Trust as a Signal of a Social Norm and the Hidden Costs of Incentive Schemes
authors: ["Sliwka, Dirk"]
year: 2007
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/BPDN8CUC"
pdf: /Users/jesper/Zotero/storage/G43MXKR4/Sliwka2007.pdf
tags: [literature]
keywords: [social-preferences, motivation-crowding-out, incentives, trust, signaling, social-norms, conformism]
topics: []
related: [Benabou2003, Bolton2000, Charness2002, Falk2006, Falk2006a, Fehr1999, Gneezy2000]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Sliwka offers a purely economic, signaling-based explanation for motivation crowding-out and the "hidden costs" of incentives and control. The key innovation is a third behavioral type — the **conformist** — who has social preferences only if he believes a sufficient share of others do too. Because a principal has superior information about the prevailing distribution of types (the social norm), her choice to *trust* (e.g., pay a fixed wage, impose no restriction) versus *control* (set a piece rate, restrict the choice set) becomes a credible signal about that norm. Trusting signals optimism that most people are fair, which makes conformists fair; controlling reveals pessimism, which makes conformists selfish. This rationalizes the experimental findings of [[@Falk2006|Falk and Kosfeld (2006)]] and others without appealing to psychological changes in task enjoyment.

## Research question
Can the "hidden costs" of incentives and control — motivation crowding-out, the counterintuitive result that giving incentives or restricting an agent's choice set lowers performance — be explained within an extended economic model of social preferences, rather than only by psychologists' task-enjoyment accounts? Specifically, when and why can choosing to *trust* an employee be beneficial even when *control* is a dominant strategy under full information about types?

## Method / identification
A game-theoretic **signaling model**. A risk-neutral principal employs an agent whose effort $e$ generates payoffs $\pi_P(\tau,e)$ for the principal and $\pi_A(\tau,e)$ for the agent, where $\tau\in\{T,C\}$ is the trust/control decision. There are three types:
- **Steadfast selfish** ("outsiders"): utility $U_S=\pi_A$.
- **Steadfast fair** ("insiders"): utility $U_F=\pi_A+\mu\,\pi_P$, $\mu>0$ — fixed moral convictions.
- **Conformists**: utility equals $U_F$ if they believe the median steadfast agent is fair (conditional expectation of the fair fraction $\phi$ exceeds $1/2$), and $U_S$ otherwise. This makes the game a *psychological game* (Geanakoplos, Pearce, Stacchetti 1989): payoffs depend on beliefs.

The fraction of fair agents among the steadfasts, $\phi$, is uncertain (prior mean $\bar\phi$). The principal privately learns a signal — $\phi_L$ (pessimistic) or $\phi_H$ (optimistic) — about $\phi$; she has superior information from experience with prior employees. Timing: principal observes signal and chooses $\tau$; conformists update beliefs on $\phi$ from $\tau$; agent chooses effort. The principal's continuation payoff $\Pi$ depends on $\tau$ and on whether the agent acts fairly ($\Pi_{\tau F}$) or selfishly ($\Pi_{\tau S}$). Three structural properties are assumed: (1) $\Pi_{\tau F}>\Pi_{\tau S}$ (better off when agent is fair); (2) $\Pi_{SC}-\Pi_{ST}>\Pi_{FC}-\Pi_{FT}$ (control protects more against shirking); (3) $\Pi_{SC}>\Pi_{FT}$ (control dominates under known types). The analysis derives conditions for a **separating equilibrium** where the principal trusts after the good signal and controls after the bad. Three applications instantiate the framework: (A) fixed wage vs. piece rate; (B) restriction on the choice set (the Falk–Kosfeld setup); plus a self-selection extension.

## Data
None — this is a pure theory paper. It uses no original data; it instead reinterprets prior laboratory evidence (notably [[@Falk2006a|Falk and Kosfeld 2006]]; Fehr and Gächter 2002; [[@Gneezy2000|Gneezy and Rustichini 2000)]] as motivating and confirming evidence.

## Key findings
- **Proposition 1** (existence of a separating equilibrium): Given $\Pi_{FT}\ge\Pi_{SC}$, a separating equilibrium exists — principal trusts after the good signal, controls after the bad — if and only if the fraction of conformists $\eta\in[\hat\eta(\phi_H),\hat\eta(\phi_L)]$, with $0<\hat\eta(\phi_H)<\hat\eta(\phi_L)\le 1$. Crucially this holds *even though control is a dominant strategy under full information*. There must be neither too few conformists (then even an optimist controls) nor too many (then even a pessimist mimics, destroying credibility). The cut-off is decreasing in $\phi$.
- **Proposition 2** (incentives and identification): An optimistic principal can credibly signal trust by raising the fixed salary by $\Delta$ instead of paying a piece rate $\beta$, provided $\Delta$ lies in a characterized interval and $\mu\ge\beta(1-\beta)$ with enough conformists. Hence performance pay can *crowd out* motivation while performance-independent payments support a *crowding in*. Insiders respond to incentives but less than outsiders.
- **Proposition 3** (trust and restrictions): In the Falk–Kosfeld choice-set-restriction setup with Fehr–Schmidt inequity-averse fair agents, when $e^*>R$ and conformists are neither too few nor too many, a separating equilibrium exists where the principal imposes *no* restriction iff she got the good signal — and observed average effort is higher under no restriction. This reproduces Falk–Kosfeld's "hidden costs of control" without invoking distrust aversion, and works despite the experiment's anonymity (the signal is about the *distribution* of types, not the individual).
- **Proposition 4** (self-selection): With outside offers, control drives out selfish types (beneficial) but may also drive out fair types (costly). Trust is always beneficial when conformists are sufficiently many. If the selection effect for fair types is strong enough ($F_F(U_{FC})$ large), trust can be optimal even absent the signaling motive. Under **organization-specific norms**, control can sometimes *strengthen* the work norm by repelling so many selfish agents that fair agents become the majority.

## Contribution
Provides the first economic (vs. psychological) mechanism for motivation crowding-out grounded in social-norm *signaling*: the principal's superior information about the type distribution makes trust/control a credible signal that endogenously shifts conformists' preferences. It unifies and rationalizes a set of puzzling experimental results (Falk–Kosfeld, Fehr–Gächter, Gneezy–Rustichini) and connects to identity economics (Akerlof–Kranton insiders/outsiders) and conformism models (Bernheim 1994). Importantly, the account works even when agents dislike effort — unlike Bénabou–Tirole or Frey, which require that the agent might enjoy the task.

## Limitations & open questions
- The mechanism requires genuine **uncertainty about the social norm**; the author notes it should be relevant in large firms or new departments but "less relevant in firms where all employees can mutually observe their respective efforts" — a scope condition and empirical test waiting to be run.
- The separating equilibrium can coexist with a **pooling equilibrium** when $E[\phi]\ge 1/2$; selection among equilibria is delicate (too many conformists destroys credibility).
- Under **population norms with conformists in the reference group**, there are typically *multiple equilibria* at the effort stage and different norms can be stable; the conformists play a coordination game requiring a refinement (focal median behavior) to restore separation.
- The principal's superior information is *assumed*; it is only endogenized in a two-period multi-agent working-paper version (Sliwka 2006), not the published model.
- The two notions of social norm — "be fair" (intention/type-based) vs. "choose a particular action" (action/reference-group-based) — yield different equilibrium structures, inviting empirical work on which governs behavior in given settings.

## Connections
The paper sits at the intersection of incentive theory and social preferences. It directly formalizes and explains **Falk and Kosfeld (2006)** "The Hidden Costs of Control," and motivates itself against **Fehr and Gächter (2002)**, **Fehr and Rockenbach (2003)**, and **[[@Gneezy2000|Gneezy and Rustichini (2000)]]** ("Pay Enough or Don't Pay at All"). The conformist type extends distributional social-preference models — **[[@Fehr1999|Fehr and Schmidt (1999)]]**, **[[@Bolton2000|Bolton and Ockenfels (2000)]]**, **[[@Charness2002|Charness and Rabin (2002)]]** — which alone cannot explain why trust raises trustworthiness. The "insiders/outsiders" language and identification motive draw on **Akerlof and Kranton (2005)** identity economics and **Bernheim (1994)** conformism. The signaling-via-incomplete-contracts logic parallels **Spier (1992)** and **Allen and Gale (1992)**, and the fixed-wage optimality echoes **Holmström and Milgrom (1991)** multitasking and **Bernheim and Whinston (1998)** strategic ambiguity. The alternative esteem-based explanation of Falk–Kosfeld in **Ellingsen and Johannesson (2005)** is contrasted (and argued to fit the anonymous design less well). It situates against the psychological crowding literature of **Deci (1971)**, **Frey (1997)**, **Frey and Oberholzer-Gee (1997)**, and **Bénabou and [[@Benabou2003|Tirole (2003)]]**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
