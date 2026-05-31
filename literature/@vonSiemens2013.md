---
citekey: vonSiemens2013
title: Intention-based reciprocity and the hidden costs of control
authors: ["von Siemens, Ferdinand A."]
year: 2013
type: journalArticle
doi: 10.1016/j.jebo.2013.04.017
zotero: "zotero://select/library/items/L3UBX8N3"
pdf: /Users/jesper/Zotero/storage/SPQCR6XC/von Siemens - 2013 - Intention-based reciprocity and the hidden costs of control.pdf
tags: [literature]
keywords: [intention-based-reciprocity, hidden-costs-of-control, motivational-crowding-out, incomplete-information, psychological-game-theory, social-preferences]
topics: ["[[motivated-agents-intrinsic-motivation]]"]
related: [Benabou2003, Dufwenberg2004, Ellingsen2008, Falk2006, Rabin1993, Sliwka2007]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Empirical research suggests that – despite strengthening conventional incentives to put in effort – exerting control might reduce worker performance. The present paper shows that intention-based reciprocity can explain such hidden costs of control if individuals differ in their propensity for reciprocity and preferences are private information. Not being controlled might then be considered to be kind, because not everybody reciprocates not being controlled with high effort. This argument contrasts existing theoretical wisdom on the hidden costs of control that is almost exclusively based on signaling.

## Summary
Falk and Kosfeld (2006) document that imposing control on workers can lower, rather than raise, their effort — the "hidden costs of control." This poses a puzzle for intention-based reciprocity: if uncontrolled workers exert *more* effort, they thereby give their boss a *higher* payoff, so withholding control looks unkind and should not trigger high effort. Von Siemens resolves the puzzle by adding heterogeneous, privately-known reciprocity types. When most workers are selfish, *not* controlling is on average kind (selfish workers would otherwise shirk), so reciprocal workers respond to non-control with high effort. Crucially, this mechanism is entirely free of signaling: it works even though bosses' control choices reveal nothing payoff-relevant to workers.

## Research question
Can intention-based reciprocity — without any signaling channel — generate the empirically observed motivational crowding-out, whereby exerting control reduces voluntary worker effort? And what role does incomplete information about reciprocity preferences play in making this possible?

## Method / identification
The paper is purely theoretical: a psychological-game analysis in the tradition of [[@Rabin1993|Rabin (1993)]] and [[@Dufwenberg2004|Dufwenberg & Kirchsteiger (2004)]], extended to incomplete information. A boss first chooses control $a_b\in\{c,nc\}$; control is costless and merely removes the lowest effort, so the worker's action set is $A_w(c)=\{h,m\}$ and $A_w(nc)=\{h,m,\ell\}$. Payoffs satisfy $\pi_b(h)>\pi_b(m)>\pi_b(\ell)$ and $\pi_w(\ell)>\pi_w(m)>\pi_w(h)$ (more effort helps the boss, hurts the worker).

Each player is selfish or reciprocal, $\theta\in\Theta=\{s,r\}$, privately known, reciprocal with common-prior probability $\lambda\in(0,1)$. Kindness of a worker's effort is the standard Rabin index relative to the equitable payoff,
$$k_{wb}(a_b,a_w)=\frac{\pi_b(a_w)-\pi_b^{e}(a_b)}{\pi_b^{\max}(a_b)-\pi_b^{\min}(a_b)},\qquad \pi_b^{e}(a_b)=\tfrac{1}{2}\bigl(\pi_b^{\max}(a_b)+\pi_b^{\min}(a_b)\bigr).$$
Because the boss cannot observe $\theta$, the kindness of a *control choice* is the type-expected kindness, $E_\theta k_{bw}(a_b,\beta_w,\theta)=\mu\,k_{bw}(a_b,\beta_w,r)+(1-\mu)\,k_{bw}(a_b,\beta_w,s)$. Reciprocal utilities add a weighted product of own and other's kindness, e.g. for the worker $U_w(a_w,a_b,\gamma_w,\nu)=\pi_w(a_w)+\eta\,E_\theta k_{bw}(a_b,\gamma_w,\theta)\,k_{wb}(a_b,a_w)$, with reciprocity weight $\eta\ge 0$ ($\eta=0$ for selfish types). Equilibrium is a reciprocity (psychological Nash) equilibrium with belief consistency $\nu^\ast=\mu^\ast=\lambda$, kindness updated treating all observed actions as fully deliberate, and a tie-breaking rule (workers pick lowest effort, bosses control) that biases *against* the desired result.

## Data
None — this is a theory paper. It is motivated by, and seeks to rationalize, the experimental findings of Falk & Kosfeld (2006) and related lab evidence, but contains no original data or estimation.

## Key findings
- **Lemma 1–3** pin down beliefs-independent kindness values: a worker's high effort has kindness $+\tfrac12$ and shirking $-\tfrac12$; selfish workers always minimize effort ($\alpha_w^\ast(s,nc)=\ell$, $\alpha_w^\ast(s,c)=m$); hence controlling a selfish worker is unkind ($-\tfrac12$) and not controlling is kind ($+\tfrac12$).
- **Proposition 1 (High-Effort Reciprocation).** A pure-strategy equilibrium in which reciprocal workers play $\alpha_w^\ast(r,nc)=h$ and $\alpha_w^\ast(r,c)=m$ (i.e. crowding-out) exists *if and only if* $\lambda<\tfrac12$ and $\eta>\max\{\eta_1,\eta_2\}$. So crowding-out requires that selfish workers are a majority and that reciprocity is strong enough. The proposition also characterizes boss behavior via cutoffs $\lambda_1,\lambda_2$: for $\lambda\in(\lambda_1,\lambda_2)$ selfish bosses do *not* control while reciprocal bosses *do* — reciprocal bosses are *more* controlling, because offering kind non-control that goes unreciprocated hurts them, whereas controlling yields a "utility kick from spite."
- **Irrelevance of signaling.** Equilibrium behavior is independent of the probability workers assign to facing a reciprocal vs. selfish boss; revealed information about the boss's type has zero behavioral effect. This sharply separates the mechanism from existing accounts.
- **Sharp predictive structure.** The only other pure-strategy equilibria are intuitive (uniform medium effort for intermediate $\eta$; uniform minimum effort for low $\eta$). Reciprocal workers *never* exert more than the minimum once controlled, because control is at most kindness-neutral to them.

## Contribution
Provides the first explanation of the hidden costs of control grounded in intention-based reciprocity rather than signaling, and shows that private information about reciprocity *types* is what makes it possible (the puzzle has no solution under complete information). It is empirically distinguishable from signaling theories: signaling-based crowding-out should weaken when bosses hold little worker-relevant information (e.g. anonymous labs), whereas the reciprocity channel predicts undiminished deterioration. It also operationalizes Rabin's (1993) call to extend reciprocity to incomplete-information games.

## Limitations & open questions
- Results depend on the exact specification of reciprocity. The author shows robustness across alternatives — treating heterogeneity as a mixed strategy, the [[@Dufwenberg2004|Dufwenberg–Kirchsteiger (2004)]] / [[@Falk2006|Falk–Fischbacher (2006)]] conventions, inequality-augmented kindness, and Segal & Sobel (2007) — but the precise cutoffs (notably the $\lambda<\tfrac12$ threshold) are *not* invariant; under some specifications crowding-out can arise even with a reciprocal majority.
- Restricted to pure strategies; evaluating the kindness of mixed strategies in psychological games is acknowledged as non-trivial and is left aside.
- Guilt-aversion accounts (Battigalli & Dufwenberg, 2007; Schnedler & Vadovic) can also generate crowding-out but admit unreasonable equilibria; reconciling reasonable-expectations selection across these frameworks is open.
- The author explicitly flags intention-based reciprocity under incomplete information as "an interesting topic for future research" and notes the broader agenda of applying reciprocity models to organizational economics.

## Connections
Directly builds on and rationalizes Falk & Kosfeld (2006). The reciprocity machinery is that of [[@Rabin1993|Rabin (1993)]] and [[@Dufwenberg2004|Dufwenberg & Kirchsteiger (2004)]], with the incomplete-information extension anticipated by Geanakoplos, Pearce & Stacchetti (1989) and Battigalli & Dufwenberg (2009). It is positioned against the signaling-based crowding-out literature: [[@Sliwka2007|Sliwka (2007)]] and [[@Ellingsen2008|Ellingsen & Johannesson (2008)]] (closest competitors, both requiring heterogeneous beliefs), as well as Bénabou & [[@Benabou2003|Tirole (2003)]], Spier (1992), Suvorov & van de Ven (2009), and Herold (2010). Alternative reciprocity foundations are drawn from [[@Falk2006|Falk & Fischbacher (2006)]] and Segal & Sobel (2007), and guilt aversion from Battigalli & Dufwenberg (2007). Related applications of reciprocity in organizations include Englmaier & Leider (2008), von Siemens (2009), and İriş & Santos-Pinto (2010). The motivation-crowding background traces to Frey & Jegen (2001) and Deci–Ryan self-determination theory (Ryan & Deci, 2000).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
