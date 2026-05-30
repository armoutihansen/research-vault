---
citekey: Englmaier2012
title: Contractual and organizational structure with reciprocal agents
authors: ["Englmaier, Florian", "Leider, Stephen"]
year: 2012
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/VF4SPKX9"
pdf: /Users/jesper/Zotero/storage/L5XETHTS/Englmaier and Leider - 2012 - Contractual and organizational structure with reciprocal agents.pdf
tags: [literature]
keywords: [reciprocity, gift-exchange, optimal-contracts, moral-hazard, social-preferences, principal-agent, incentive-pay]
topics: []
related: [Akerlof1982, Bolton2000, Dufwenberg2004, Englmaier2010, Falk2006, Fehr1999, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We solve for the optimal contract when agents are reciprocal, demonstrating that generous compensation can substitute for performance-based pay. Our results suggest several factors that make firms more likely to use reciprocal incentives. Reciprocity is most powerful when output is a poor signal of effort and when the agent is highly reciprocal and/or productive. Similarly, reciprocal incentives are attractive when firm managers have strong incentive pay and discretion over employee compensation. While reciprocal incentives can be optimal even when identical firms compete, a reciprocity contract is most likely when one firm has a match-specific productivity advantage with the agent. (JEL D23, D86, J33, M12, M52)

## Summary
Englmaier and Leider embed intention-based reciprocity into a standard moral-hazard principal-agent model and show that a firm has two distinct levers for inducing effort: explicit pay-for-performance (wage spread across output states) and "reciprocal incentives" (a generous wage level that leaves the agent a rent and triggers gift exchange). These two levers are substitutes in the optimal incentive mix. Reciprocal incentives dominate when output is a noisy signal of effort, when the agent is highly reciprocal, and when the agent's effort is highly valuable to the principal. The framework rationalizes the empirical prevalence of weak monetary incentives, and is extended to derive testable predictions about firm hierarchy (collocation of incentive pay and decision rights) and about labor-market competition for scarce reciprocal workers.

## Research question
Why do so many real-world labor contracts use weak or no explicit monetary incentives yet still elicit substantial effort? Specifically: what does the optimal contract look like when the agent is reciprocal, and under what job/firm/market conditions will a firm choose to rely on reciprocity ("generous compensation") rather than on performance-based pay?

## Method / identification
The core is a single-principal, single-agent moral-hazard model. A risk-neutral principal hires a risk-averse agent who chooses one of two effort levels $a_1<a_2$ with costs $c(a_1)<c(a_2)$. Effort induces probabilities $\pi_i(a)$ over $n$ output states $q_i$; the monotone likelihood ratio property (MLRP) holds. A contract $(w,a)$ specifies a wage $w(q_i)$ in each state plus a non-binding requested action $a$ that pins down the agent's beliefs about the principal's intended generosity.

The agent's utility has three parts: (i) expected monetary utility $\sum_i \pi_i(a')u(w(q_i))$; (ii) reciprocal utility $\eta\big(\sum_i \pi_i(a)u(w(q_i))-c(a)-u_0\big)\big(\sum_i \pi_i(a')q_i\big)$ — i.e., the agent's reciprocity parameter $\eta\in[0,\infty)$ times the rent the firm grants him times the expected revenue he returns; and (iii) effort cost $c(a')$. The outside option $u_0$ is the reference point defining a "fair" offer; any rent above it reads as kindness. The agent is assumed risk-neutral over the principal's revenue (justified by experimental evidence on choices over others' lotteries).

Following Grossman and Hart (1983), the authors solve the implementation problem for $a_2$ via the standard change of variables $u_i=u(w(q_i))$, $h(\cdot)=u^{-1}(\cdot)$ (so $h'>0$, $h''>0$), yielding a convex program with linear constraints — an individual-rationality constraint [IR], an incentive-compatibility constraint [IC], and an equilibrium-belief constraint [EB] that rules out babbling/destructive equilibria. Karush-Kuhn-Tucker conditions are necessary and sufficient. The two key aggregates are $\Delta c$ and $\mathrm{AER}=\sum_i\pi_i(a_2)q_i-\sum_i\pi_i(a_1)q_i$, the difference in expected revenue across actions. Comparative statics on information use mean-preserving spreads of likelihood-ratio distributions (Rothschild-Stiglitz 1970) and a custom partial order $\succeq_{mu}$ ranking contracts by "sharpness" of marginal-utility spreads across states. Appendix A generalizes to multiple actions under the convexity-of-distribution-function condition (Rogerson 1985). Two further extensions add (a) a three-manager organizational-hierarchy model and (b) a two-firm sequential-offer competition model.

## Data
None — this is a pure theory paper. The authors note that companion work (Englmaier and Leider 2010, 2012) tests the predictions in lab and field experiments, but no data are analyzed here.

## Key findings
- **Observations 1-2:** At $\eta=0$ the model collapses to the standard contract; the standard contract implements $a_2$ for any $\eta$, because it leaves zero rent so the reciprocal term drops out (a reciprocal agent paid only his outside option behaves selfishly).
- **Lemma 1 / Proposition 1 / Corollary 1:** If a contract implements $a$ for $\eta_1$ it does so for all $\eta_2>\eta_1$; the value function (expected wage bill) $V(\eta,\mathrm{AER};a)$ is nonincreasing in both $\eta$ and $\mathrm{AER}$. Because $\eta$ always enters as $\eta\,\mathrm{AER}$, productivity and intrinsic reciprocity act identically.
- **Observations 3-4:** A flat wage with a large enough rent implements high effort if $u\ge \Delta c/(\eta\,\mathrm{AER})$; as $\eta\to\infty$ the first best is approached with an infinitesimal rent.
- **Lemma 2 / Proposition 2:** The [IC] always binds. There is a finite threshold $\eta^*$: below it the optimal contract is the zero-rent standard contract, above it the optimal contract is a "reciprocity contract" with strictly positive rent.
- **Proposition 3:** characterizes the optimal reciprocity contract via ratios of marginal utilities $u'(w_i)/u'(w_j)$ that depend on relative likelihood ratios plus a reciprocity term in $\eta\,\mathrm{AER}$.
- **Proposition 4 / Corollary 2:** As $\eta$ (or $\mathrm{AER}$) rises the optimal contract flattens — explicit incentives weaken — with marginal-utility ratios tending to 1.
- **Proposition 5:** When output becomes a more informative signal of effort (a mean-preserving spread of likelihood ratios), the optimal contract uses sharper explicit incentives. Hence explicit and reciprocal incentives are substitutes.
- **Proposition 6:** Higher $\eta$ pushes implemented effort toward the first best.
- **Organizational extension:** stronger managerial incentive pay, more narrowly targeted managerial incentives, and giving the supervisor whose pay depends most on the agent discretion over the agent's contract all raise the effectiveness of reciprocal incentives — predicting a collocation of incentive pay and decision rights.
- **Competition extension:** reciprocity contracts can survive competition even between ex ante identical firms; they are most attractive when one firm has a match-specific productivity advantage, since a rival finds it too costly to bid the reciprocal agent away.

## Contribution
Provides one of the first tractable optimal-contracting treatments of intention-based reciprocity under moral hazard, nesting the classic Holmstrom/Grossman-Hart contract as the $\eta=0$ special case. It formalizes the substitutability of generous pay and performance pay, and uniquely translates a social-preference assumption into observable, testable predictions about firm hierarchy and labor-market competition, guiding empirical gift-exchange research toward the settings where reciprocity should matter most (noisy production, productive workers, screenable reciprocity, strong managerial incentives, weak competition).

## Limitations & open questions
- The authors flag that it is "hard in our framework, without imposing strong assumptions, to make statements on which effort level will be implemented" in the multi-action case; the monotone-comparative-static condition on $V(\eta,a)$ is "difficult to ensure."
- For tractability the agent values reciprocity over the principal's gross revenue rather than profit net of wages, and is assumed risk-neutral over principal revenue; relaxing these is left as a robustness footnote rather than fully developed.
- The outside option is taken as the unique fair reference point; if "fair" requires a specific positive rent, some results need a sufficiently large $\eta$ and the firm might prefer hiring a selfish agent — left unmodeled.
- Only positive reciprocity is analyzed; destructive/negative reciprocity is assumed away via [EB] and the [IR].
- The organizational and competition models use specific simple functional forms for managerial payoffs; general forms are not solved.
- The central empirical implications are explicitly left for future field work in the suggested high-reciprocity settings.

## Connections
The reciprocity formalization builds on [[@Rabin1993|Rabin (1993)]] for normal-form games and on [[@Dufwenberg2004|Dufwenberg and Kirchsteiger (2004)]] and [[@Falk2006|Falk and Fischbacher (2006)]] for sequential games, with Cox, Friedman, and Sadiraj (2008) grounding reciprocity in demand theory. The gift-exchange motivation traces to [[@Akerlof1982|Akerlof (1982)]]. The contracting backbone is Holmstrom (1979), Grossman and Hart (1983), and Holmstrom and Milgrom (1991); information comparative statics use Rothschild and Stiglitz (1970), Kim (1995), and Rogerson (1985, CDFC). Outcome-based alternatives are [[@Fehr1999|Fehr and Schmidt (1999)]] and [[@Bolton2000|Bolton and Ockenfels (2000)]], with applications in Dur and Glazer (2008) and [[@Englmaier2010|Englmaier and Wambach (2010)]]; Englmaier (2005) surveys this literature. Empirical motivation comes from Lemieux, MacLeod, and Parent (2009), Prendergast (1999), Belfield and Marsden (2003), and Piekkola (2005). Field/lab gift-exchange evidence includes Falk (2007), Leuven et al. (2005), Gneezy and List (2006), Kube, Marechal, and Puppe (2006), Bellemare and Shearer (2009), and Dohmen et al. (2009); Dur, Non, and Roelfsema (2010) offer a complementary attention-based model. Dufwenberg and Kirchsteiger (2000) is cited as the notable prior theoretical exception. The model's predictions are tested in the authors' companion papers Englmaier and Leider (2008, 2010, 2012).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
