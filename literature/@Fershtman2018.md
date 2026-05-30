---
citekey: Fershtman2018
title: Preferences and Social Influence
authors: ["Fershtman, Chaim", "Segal, Uzi"]
year: 2018
type: journalArticle
doi: 10.1257/mic.20160190
zotero: "zotero://select/library/items/MKA62NVU"
pdf: /Users/jesper/Zotero/storage/9ZSICFEA/Fershtman2018.pdf
tags: [literature]
keywords: [social-influence, behavioral-preferences, endogenous-preferences, risk-aversion, group-polarization, decision-theory, fixed-point-existence]
topics: []
related: [Ariely2000, Chen2009, Fehr1999]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Interaction between decision makers may affect their preferences. We consider a setup in which each individual is characterized by two sets of preferences: his unchanged core preferences and his behavioral preferences. Each individual has a social influence function that determines his behavioral preferences given his core preferences and the behavioral preferences of other individuals in his group. Decisions are made according to behavioral preferences. The paper considers different properties of these social influence functions and their effect on equilibrium behavior.

## Summary
A decision theory / microeconomic theory paper proposing that an individual carries two preference relations: fixed *core* preferences $u_i$ and *behavioral* preferences $v_i$ on which actual choices are made. Behavioral preferences are determined by a *social influence function* mapping one's core preferences and the observed behavioral preferences of everyone else in the group into one's own behavioral preferences. The paper proves existence of an equilibrium profile of mutually-consistent behavioral preferences, axiomatizes a tractable functional form in which influence depends only on the *average* of others' behavioral utilities, and uses a single-parameter (risk-aversion) specialization to characterize when social interaction pushes agents toward or away from each other.

## Research question
When observable choices of others in a group reshape the preferences a decision maker acts on — even absent any informational, strategic, altruistic, or evolutionary channel — what structure must such "social influence" take, when does a consistent equilibrium of interacting behavioral preferences exist, and does influence make group members behaviorally *more extreme* (group polarization) or push them toward the mean? The motivating evidence is Ariely and Levav's restaurant experiment (group diners show higher variance in orders) and the social-psychology literature on group polarization.

## Method / identification
Pure axiomatic decision theory; no data, no estimation. The setup: $n$ individuals, outcomes in $[a,b]$. Each $i$ has two continuous vNM utilities, core $u_i$ and behavioral $v_i$, both normalized so $u_i(a)=v_i(a)=0$, $u_i(b)=v_i(b)=1$. All utilities live in $B=B_L([a,b])$, the set of increasing, continuous, onto functions that are *equi-Lipschitz* with a common constant $L$ (i.e. $|g(x)-g(y)|\le L|x-y|$); $L$ is interpreted as a hard physical/psychological cap on sensitivity to outcome changes. The space carries the supremum metric $d(w_1,w_2)=\sup_{x\in[a,b]}|w_1(x)-w_2(x)|$.

The core object is the **social influence function**
$$v_i = f_i(u_i, v_{-i}), \qquad f_i : B \times B^{n-1} \to B,$$
assumed continuous in the sup norm, where $v_{-i}=(v_1,\dots,v_{i-1},v_{i+1},\dots,v_n)$. Crucially this is interpreted as *interaction, not aggregation*: $i$ is influenced by others' behavior but is not a social planner averaging preferences, and does not act strategically even knowing he influences others. An **equilibrium** (Definition 1) is a profile $v^*(u)$ with $v_i^*(u)=f_i(u_i,v^*_{-i}(u))$ for every $i$ — a fixed point of $f(u,v)\equiv(f_1(u_1,v_{-1}),\dots,f_n(u_n,v_{-n}))$.

The identification of the functional form proceeds through three axioms on $f_i$: (i) **Symmetry** — $i$ cares about the unordered profile of others, ruling out gurus or personal reference groups; (ii) **Betweenness** — if $v_{-i}$ and $w_{-i}$ induce the same behavioral preference, so does $\tfrac12 v_{-i}+\tfrac12 w_{-i}$ (justified via a De Finetti "probabilities of probabilities" / compound-lottery argument on the probability-equivalent reading of vNM utilities); (iii) **Influence Probability Equivalence** — if $x,x'$ have the same probability equivalent under two core utilities $u_i,\tilde u_i$, they retain a common probability equivalent under the induced behavioral utilities $v_i=f_i(u_i,v_{-i})$ and $\tilde v_i=f_i(\tilde u_i,v_{-i})$.

## Data
None — this is a theoretical paper. The only empirical referents are cited motivation (Ariely–Levav restaurant choice; Myers and Aronson on group polarization), not analyzed data.

## Key findings
- **Claim 1 (Existence).** For every core profile $u$ there is a behavioral profile $v^*(u)$ with $v^*(u)=f(u,v^*(u))$. Proof: $B$ is convex and compact in $C([a,b])$ (Arzelà–Ascoli, using equi-Lipschitz $\Rightarrow$ equicontinuity), and the continuous self-map $f$ has a fixed point by the **Schauder–Tychonoff** theorem. The equi-Lipschitz restriction is essential: existence *fails* without it (e.g. $n=2$, $v_i=u_i+v_j$, whose slopes exceed $L$).
- **Claims 2–3 + Theorem 1 (Functional form).** Under symmetry and betweenness, $f_i$ depends on $v_{-i}$ only through the average $\bar v_{-i}$, where $\bar v_j=\frac{1}{n-1}\sum_{j\neq i}v_j$ (Claim 2, via a dyadic-density argument). Influence Probability Equivalence is equivalent to a *composition* form $f_i(u_i,v_{-i})=h^i_{v_{-i}}\circ u_i$ (Claim 3 — note this needs neither symmetry nor betweenness). Combined, **Theorem 1**: the three axioms hold iff $v_i = h^i_{\bar v_{-i}}\circ u_i$, i.e. behavioral utility is the core utility transformed by a function $h^i$ depending only on others' *average* behavioral utility. Importantly, equilibrium behavioral preferences still depend on the full *distribution* of core preferences (since each $i$ sees a different average $\bar v_{-i}$), not merely the population average. Remark 1 extends the result to completely-separable multivariate preferences ($v_i=\sum_\ell v_i^\ell$).
- **Single-parameter / risk-aversion model (Section 4).** Restrict utilities to a one-parameter family $W=\{w_\alpha\}$ where higher $\alpha$ = more risk averse. **Claim 4** shows the four natural conditions (normalization, continuity, mixture-closure, monotonicity in $\alpha$) force the *linear* family $w_\alpha=\alpha w_1+(1-\alpha)w_0$. The adjustment rule becomes $\beta_i=g(\alpha_i,\bar\beta_{-i})$ with assumed $0<g_1\le 1$ and $0\le g_2<1$.
- **Claim 5 (Uniqueness).** The equilibrium $(\beta_1,\dots,\beta_n)$ of $\beta_i=g(\alpha_i,\bar\beta_{j\neq i})$ is unique (driven by $g_2<1$).
- **Claim 6.** For identical agents with common core $\alpha$, the common behavioral equilibrium $G(\alpha)$ satisfies $G(\alpha)\gtrless\alpha \iff g(\alpha,\alpha)\gtrless\alpha$ — influence need not regress to the mean; everyone can become uniformly more (or less) risk averse than their core.
- **Claim 7 (Order preservation / comonotonicity).** $\beta$ and $\alpha$ are comonotone: $(\alpha_i-\alpha_j)(\beta_i-\beta_j)\ge 0$; influence never reverses the risk-aversion ranking.
- **Claim 8 (No divergence).** Social influence *never* makes two agents "more extreme" (it is impossible that $\alpha_i<\alpha_j$ with $\beta_i<\alpha_i$ while $\alpha_j<\beta_j$). With $\alpha_1\le\dots\le\alpha_n$, equilibria fall into exactly three types: all $\alpha_i\le\beta_i$, all $\alpha_i\ge\beta_i$, or a single crossover (type 3, which obtains whenever $g(\alpha,\alpha)\equiv\alpha$). Notably, *no divergence* does not preclude an increase in the *variance* of risk aversion when the upward adjustment is larger at high $\alpha$.

## Contribution
Introduces a clean, non-strategic theory of *endogenous, socially influenced preferences* that is distinct from (a) social/interdependent preferences (Fehr–Schmidt, Sobel — utility fixed but defined over others' outcomes), (b) social-status models (Bernheim, Veblen, Fershtman–Murphy–Weiss — status enters utility directly), and (c) evolutionary/cultural-transmission models (Bisin–Verdier, Becker) that require "success" or fitness. It is closest to Postlewaite's deep vs. reduced-form preferences but localizes influence to small, observable groups via frequent interaction, and the authors suggest a three-layer fusion (deep / reduced-form / behavioral). The technical payoff is a fixed-point existence result plus an axiomatic reduction (Theorem 1) to the tractable "average-influence composition" form, and a sharp polarization analysis (Claims 6–8) clarifying that the model rationalizes uniform shifts but rules out pairwise divergence.

## Limitations & open questions
The paper is explicit about its two strong maintained assumptions and several extensions (these are direct project hooks):
- **Symmetry → social networks.** Drop symmetry: let each $i$ be influenced only by a subset of others, encoded as a (possibly weighted) directed social-influence network with a link $i\to j$ iff $i$ affects $j$. Equilibrium is defined as before but restricted to the network structure; the sensitivity of the behavioral-preference distribution to network topology is flagged as "potentially interesting."
- **Full observability → beliefs.** Drop perfect observability of others' behavioral preferences: individuals instead hold *beliefs* about others' behavioral preferences, updated upon observing behavior, with $f_i$ a function of core preferences and those beliefs. Partial observation likely yields a *set* of admissible behavioral functions rather than a point.
- **Static → dynamic preference evolution.** The framework "may give rise to a dynamic model of preferences evolution," with behavioral (and possibly even core) preferences evolving over time as a function of interaction history.
- **Beyond risk aversion.** The leading example is risk aversion, but the authors note applicability to preferences for competition (Niederle–Vesterlund) and inequality aversion (Fehr–Schmidt) — open question: under what social-influence structures does group interaction make people more competitive or more/less inequality-averse?
- The base model also assumes a common preference over *sure* outcomes (increasing utilities), which excludes the menu/restaurant motivation itself; Remark 1's separable multivariate extension partially relaxes this.

## Connections
Directly builds on **Postlewaite (2001, 2011)** and **Mailath–Postlewaite (2003)** (deep vs. reduced-form preferences). It positions itself against the **social/interdependent preferences** tradition — **[[@Fehr1999|Fehr–Schmidt (1999)]]**, **Fehr–Gächter (2000)**, **Sobel (2005)**, **Charness–Kuhn (2011)**, and **Gul–Pesendorfer** on intentions — and against **status/conformity** models (**Bernheim 1994**, **Veblen 1899**, **Fershtman–Murphy–Weiss 1996**, **Frank 1985**, **Cole–Mailath–Postlewaite 1992**) and **fashion/anti-conformity** (**Karni–Schmeidler 1990**). The endogenous-preferences lineage cited includes evolutionary sociobiology (**Becker 1970**, **Dawkins 1976**, **Frank 1987**, **Samuelson 2001**) and cultural transmission (**Bisin–Verdier 2001**, **Boyd–Richardson 1985**, **Cavalli-Sforza–Feldman 1973**). Empirical/psychological anchors: **[[@Ariely2000|Ariely–Levav (2000)]]** and the group-polarization work of **Myers (1975)**, **Myers–Lamm (1976)**, and **Aronson**. The committee-deliberation application connects to the **Condorcet (1785)** jury tradition and the survey by **[[@Chen2009|Li–Suen (2009)]]**. Mathematically it rests on **Arzelà–Ascoli** and the **Schauder–Tychonoff** fixed-point theorem (Dunford–Schwartz 1958), the De Finetti (1977) compound-probability argument, and Blackorby–Primont–Russell (1978) on separability.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
