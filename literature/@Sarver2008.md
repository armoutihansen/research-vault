---
citekey: Sarver2008
title: "Anticipating Regret: Why Fewer Options May Be Better"
authors: ["Sarver, Todd"]
year: 2008
type: journalArticle
doi: 10.1111/j.1468-0262.2008.00834.x
zotero: "zotero://select/library/items/YC8U3H9I"
pdf: /Users/jesper/Zotero/storage/IRU9Y9LN/Sarver2008.pdf
tags: [literature]
keywords: [regret, preference-over-menus, subjective-state-space, preference-for-commitment, temptation, decision-theory, axiomatic]
topics: ["[[disappointment-regret-nonexpected-utility]]"]
related: [Sugden1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We study preferences over menus which can be represented as if the agent selects an alternative from a menu and experiences regret if her choice is ex post inferior. Since regret arises from comparisons between the alternative selected and the other available alternatives, our axioms reflect the agent's desire to limit her options. We prove that our representation is essentially unique. We also introduce two measures of comparative regret attitudes and relate them to our representation. Finally, we explore the formal connection between the present work and the literature on temptation.

## Summary
Sarver provides an axiomatic, preference-over-menus foundation for *anticipated regret*. An agent picks a menu in period 0 and later selects a lottery from it in period 1, all *before* a subjective taste shock resolves; she then suffers regret if her choice turns out to be ex post inferior to another menu element. Because adding an alternative can only raise the benchmark against which regret is measured, such an agent may strictly prefer *smaller* menus — explaining "why fewer options may be better." Four axioms (weak order, strong continuity, independence, and a new *dominance* axiom) characterize an essentially unique "regret representation." The paper also defines comparative measures of regret-proneness and regret-aversion, and shows that regret is formally entangled with the temptation/self-control models of Gul and Pesendorfer.

## Research question
Can a preference for fewer options be rationalized as the anticipation of ex post regret, and what behavioral (preference-over-menus) restrictions exactly characterize an agent who behaves *as if* she maximizes expected utility minus regret? Can the strength of regret be identified from menu choice, and how does regret relate formally to temptation?

## Method / identification
The primitive is a binary relation $\succeq$ over menus $A$, the closed subsets of $\Delta(Z)$ (lotteries over a finite prize set $Z$), endowed with the Hausdorff metric, following Dekel, Lipman, and Rustichini (2001, "DLR"). A *regret representation* is a pair $(\mu, K)$ — a Borel probability measure $\mu$ over a canonical state space $U$ of normalized vNM utility functions and a constant $K \ge 0$ — with
$$V(A) = \int_U \max_{p\in A}\,[\,u(p) - R(p, A, u)\,]\,\mu(du), \qquad R(p,A,u) = K\Big(\max_{q\in A} u(q) - u(p)\Big).$$
Here states $u \in U$ are subjective ex post tastes and $K$ scales the strength of regret. A key algebraic rewriting,
$$V(A) = \max_{p\in A}\Big[(1+K)\int_U u(p)\,\mu(du)\Big] - K\int_U \max_{q\in A} u(q)\,\mu(du),$$
shows the utility-maximizing lottery also *minimizes* expected regret, so regret never distorts choice *from* a menu (only choice *of* menu). The identifying axiom is **Dominance**: if $\{p\}\succeq\{q\}$ and $p\in A$, then $A\succeq A\cup\{q\}$ — relaxing the standard model's indifference $A\sim A\cup\{q\}$ to allow $A\succ A\cup\{q\}$. The proof embeds the regret representation as a special case of DLR's additive-EU representation (a signed measure $\nu$): Dominance forces all "positive states" to share the commitment ranking $v$, leaving the remaining "negative states" to generate regret. Uniqueness is studied via the commitment utility $v(p)=V(\{p\})$ and the minimal-expected-regret function $r(A)$; $(v,r)$ are unique up to a common positive scalar, while $(\mu,K)$ are jointly identified only under a *singleton nontriviality* axiom. Comparative regret notions ("more regret prone," "more regret averse") are characterized via support inclusion of $\mu$ and via singleton-menu benchmarks, paralleling comparative ambiguity aversion.

## Data
None — this is a pure decision-theory paper; results are representation and uniqueness theorems plus a numerical restaurant example (beef vs. chicken).

## Key findings
- **Theorem 1 (Representation):** $\succeq$ has a regret representation iff it satisfies weak order, strong continuity, independence, and dominance.
- **Theorem 2 (DLR, restated):** the first three axioms alone give an additive-EU representation; Lemma 1 shows every regret representation is such a representation.
- **Theorem 3 (Uniqueness of $v,r$):** two representations give the same $\succeq$ iff $v'=\alpha v$ and $r'=\alpha r$ for some $\alpha>0$.
- **Theorem 4 (Parameter uniqueness):** under singleton nontriviality, $\mu$ and $K$ are jointly identified; absent it, $\mu$ is pinned down but $K$ is not. Crucially, strength of regret $K$ and degree of uncertainty cannot be separated in general — a near-certain agent with strong regret is indistinguishable from an uncertain agent with weak regret.
- **Lemma 3 / Monotonicity:** a regret preference satisfies Kreps (1979) monotonicity iff $r\equiv 0$ (no regret, no value of flexibility) — dominance and monotonicity intersect only trivially.
- **Theorems 5–6 (Comparative attitudes):** more regret prone $\iff$ larger support of $\mu$; more regret averse characterized via singleton benchmarks.
- **Theorem 7:** the *no-uncertainty* temptation representation of DLRS (2007) is equivalent to a *state-dependent regret representation*; positive set betweenness preferences admit a regret reading. **Lemma 5:** every regret preference satisfies positive set betweenness.

## Contribution
Introduces the first preference-over-menus axiomatization of anticipated regret, yielding a tractable, essentially unique functional form that identifies regret even when it leaves choice from menus undistorted — something classical regret theory (which detects regret only through its distortion of choice) cannot do. It supplies comparative measures of regret attitudes and exposes a deep formal observational equivalence between regret and temptation/self-control, clarifying that menu data alone cannot disentangle the two.

## Limitations & open questions
- **Regret–temptation non-separation:** menu preferences (even with period-1 choice added) cannot distinguish state-dependent regret from no-uncertainty temptation; richer primitives or extra information are needed.
- **$K$ vs. uncertainty non-identification:** the strength of regret and the degree of subjective uncertainty are not separately identified absent further structure.
- **Regret over the choice of menu:** the baseline model normalizes period-0 regret to zero ($R(p,A,u)=0$ for singletons). The extension over *menus of menus* shows the identified $K=K_1/(1+K_0)$ is only the regret of choice-from-menu *relative to* prior decisions; fully identifying it requires the richer domain.
- **Dynamics:** Sarver proposes extending to dynamic/staged models (as Gul–Pesendorfer 2004 and Noor 2007 did for temptation) to correctly identify stagewise regret strength — an explicit open direction.

## Connections
Built directly on the menu-preference / subjective-state-space tradition of Kreps (1979), Dekel, Lipman, and Rustichini (2001), and Dekel, Lipman, Rustichini, and Sarver (2007), whose additive-EU representation is the technical backbone. It reinterprets the self-control and temptation representations of Gul and Pesendorfer (2001, 2004) and Noor (2007a, 2007b), showing positive set betweenness admits a regret reading. It contrasts sharply with classical "regret theory" of Bell (1982), Loomes and Sugden (1982, 1987), and [[@Sugden1993|Sugden (1993)]], which identifies regret through nonlinear distortion of choice from menus, and with the minimax-regret approaches of Savage (1954), Hayashi (2007), and Stoye (2007), where the agent uses only a worst-case criterion and (in the multiple-prior case) ambiguity rather than Bayesian uncertainty. The comparative-regret measures are explicitly modeled on the comparative ambiguity-aversion definitions of Epstein (1999), Ghirardato and Marinacci (2002), and Ahn (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
