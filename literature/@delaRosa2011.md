---
citekey: delaRosa2011
title: Overconfidence and moral hazard
authors: ["de la Rosa, Leonidas Enrique"]
year: 2011
type: journalArticle
doi: 10.1016/j.geb.2011.04.001
zotero: "zotero://select/library/items/D85EWFFJ"
pdf: /Users/jesper/Zotero/storage/68WPXEVD/de la Rosa - 2011 - Overconfidence and moral hazard.pdf
tags: [literature]
keywords: [overconfidence, moral-hazard, principal-agent, incentive-contracts, heterogeneous-beliefs, behavioral-contract-theory]
topics: ["[[social-preferences-contract-theory]]"]
related: [Akerlof1982]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In this paper, I study the effects of overconfidence on incentive contracts in a moral-hazard framework. Agent overconfidence can have conflicting effects on the equilibrium contract. On the one hand, an optimistic or overconfident agent disproportionately values success-contingent payments, and thus prefers higher-powered incentives. On the other hand, if the agent overestimates the extent to which his actions affect outcomes, lower-powered incentives are sufficient to induce any given effort level. If the agent is moderately overconfident, the latter effect dominates. Because the agent bears less risk in this case, there are efficiency gains stemming from his overconfidence. If the agent is significantly overconfident, the former effect dominates; the agent is then exposed to an excessive amount of risk, and any gains arise only from risk-sharing under disagreement. An increase in optimism or overconfidence increases the effort level implemented in equilibrium.

## Summary
This is a theoretical principal–agent paper that injects overconfidence into the standard moral-hazard model by letting a risk-neutral principal and a risk-averse agent knowingly "agree to disagree" about the success probability of a project. The paper's central insight is that overconfidence decomposes into two distinct biases with opposing effects on the equilibrium contract: an *incentive effect* (overestimating the marginal productivity of effort) that pushes toward lower-powered incentives, and a *wager effect* (overestimating the level of success probability) that pushes toward higher-powered incentives. Which dominates depends on whether the agent is "slightly" or "significantly" overconfident overall. Moderate overconfidence can be efficiency-enhancing because it lets the principal provide more insurance without destroying incentives.

## Research question
How does agent overconfidence shape the *power of incentives* and the *implemented effort level* in an optimal second-best moral-hazard contract, and when does such overconfidence improve efficiency rather than merely redistribute surplus?

## Method / identification
A two-outcome (success/failure) principal–agent model. Revenue is $x_1>x_0$; the success probability is linear in non-contractible effort $e$. The principal believes $\Pr(x_1\mid e)=q+ve$; the agent believes $\widetilde{\Pr}(x_1\mid e)=\tilde q+\tilde v e$. Two belief asymmetries are separated: the agent is *optimistic* if $\tilde q>q$ (overestimates the level of success probability) and *overconfident* if $\tilde v>v$ (overestimates the marginal contribution of effort). Both parties are mutually aware of the disagreement, so there are no signaling/screening or adverse-selection channels — these are deliberately shut down to isolate the contracting effect. The agent is risk-averse with separable utility $u(s)-c(e)$, $u'>0$, $u''<0$; the principal is risk-neutral. The solution concept is subgame-perfect Nash equilibrium. The author uses the Grossman & Hart (1983) two-step method: compute the second-best cost of implementing each action, then pick the more profitable action. The participation constraint and incentive-compatibility constraint are evaluated *under each party's own beliefs*. The IC constraint reduces to $\tilde v\,(u(s_1)-u(s_0))\ge c$, so the power of incentives needed to induce effort falls in $\tilde v$ but is independent of $\tilde q$. Section 4 extends to a continuum of effort with convex cost $c(e)$, $c'>0$, $c''>0$, using the first-order approach; the IC becomes $\tilde v[u(s_1)-u(s_0)]=c'(e)$.

## Data
None — this is a pure theory paper. The conclusion sketches an empirical test using CEO overconfidence measures (e.g. Malmendier & Tate, 2005), splitting samples into slightly vs. significantly overconfident, but no data are analyzed.

## Key findings
- **Proposition 1 (first-best risk sharing).** With heterogeneous beliefs, the first-best contract no longer fully insures the agent; it generalizes the Borch (1962) rule so that $\frac{\tilde q+\tilde v e}{1-(\tilde q+\tilde v e)}\frac{u'(s_1^{FBe})}{u'(s_0^{FBe})}=\frac{q+ve}{1-(q+ve)}$. A relatively optimistic agent takes a "long" position (bears risk, betting on success); a pessimistic agent takes a "short" position.
- **Corollary 1 (wager effect, first-best).** Under non-decreasing $\frac{1}{u'(s)}-\frac{u''(s)}{u'(s)}$, first-best power of incentives $u(s_1)-u(s_0)$ rises with optimism $\tilde q$ and overconfidence $\tilde v$ — pure side-betting against disagreement.
- **Proposition 2 + Corollary 2 (incentive effect dominates).** If the agent is *slightly* overconfident overall, the IC constraint binds and the second-best contract $\langle\bar s_1,\bar s_0\rangle$ has power of incentives $u(\bar s_1)-u(\bar s_0)=c/\tilde v$, which *decreases* in $\tilde v$ and is unaffected by $\tilde q$. Overconfidence lets the principal provide more insurance without destroying incentives, lowering the cost of agency. Underconfidence ($\tilde v<v$) raises it.
- **Proposition 3 + Corollary 3 (wager effect dominates).** If the agent is *significantly* overconfident overall, the first-best contract $\langle s_1^*,s_0^*\rangle$ is itself incentive-compatible (IC slack); the agent willingly bears excessive risk. Here power of incentives *increases* in both $\tilde q$ and $\tilde v$, and there is no cost of agency. The power of incentives is therefore *non-monotonic* in overconfidence.
- **Welfare (Section 3.3).** If the principal captures all surplus, the agent is always hurt by mistaken beliefs. But if the agent captures the gains from trade (e.g. competing principals), slight overconfidence yields genuine welfare gains via the reduced cost of agency — distinct from production-externality channels (cf. Gervais & Goldstein, 2007).
- **Effort (continuous case).** The implemented effort level $e^*$ unambiguously increases in both optimism ($de^*/d\tilde q>0$) and overconfidence ($de^*/d\tilde v>0$), since both effects lower the marginal cost of implementing effort. The non-monotonicity of incentive power survives if the agent is sufficiently risk-averse and marginal effort cost does not rise sharply.

## Contribution
The paper's main contribution is to characterize *the shape* of the optimal incentive contract under agent overconfidence — not just its profit consequences — and to cleanly decompose overconfidence into the incentive and wager effects, which move power-of-incentives in opposite directions but reinforce each other on implemented effort. It distinguishes itself from contemporaneous work (Santos-Pinto, 2008, who studies profits but not contract shape; Adrian & Westerfield, 2009, who study dynamics with one-sided belief updating about profitability rather than effort-effectiveness overconfidence) and from the adverse-selection branch of the overconfidence literature.

## Limitations & open questions
- The author flags that designing an empirical test is *not* straightforward precisely because the overconfidence–power-of-incentives relationship is non-monotonic; one must first sort agents into slightly vs. significantly overconfident sub-samples (a measurement hook).
- The linear success-probability specification is acknowledged as restrictive in the continuous-effort case, retained only for tractability.
- The continuous-action comparative static for overconfidence on power of incentives is only signed under additional assumptions (sufficient risk aversion, well-behaved marginal cost); the general case is left open.
- The model assumes an exogenous outside option unaffected by overconfidence; relaxing this (overconfidence about the outside option) is noted as an unexplored extension.
- A footnote on potential principal "sabotage" when $(x_1-s_1)<(x_0-s_0)$ is assumed away, leaving the sabotage-feasible case unanalyzed.
- The conclusion conjectures that procyclical overconfidence (Gervais & Odean, 2001) and self-selection into risky jobs (Akerlof & Dickens, 1982) generate testable macro/sorting predictions, inviting empirical and experimental follow-up.

## Connections
The contracting backbone is the moral-hazard / principal–agent tradition surveyed by Prendergast (1999), built on Holmström (1979) and the Grossman & Hart (1983) characterization method, with the optimal risk-sharing rule generalizing Borch (1962). The heterogeneous-priors foundation draws on Morris (1995) and Van den Steen (2004), with learned overconfidence from Gervais & Odean (2001), self-deception from Bénabou & Tirole (2002), and the cursedness/belief-survival logic of Eyster & Rabin (2005). On the typology of overconfidence it cites Moore & Healy (2008). Closest substantive relatives are Santos-Pinto (2008), Adrian & Westerfield (2009), and Gervais, Heaton & Odean (2009); related overconfidence-in-organizations work includes Bernardo & Welch (2001), Gervais & Goldstein (2007), Goel & Thakor (2008), and Manove & Padilla (1999). The adverse-selection counterpart literature includes Maskin & Tirole (1990, 1992), de Meza & Southey (1996), Villeneuve (2000), and Koufopoulos (2008). Empirical/experimental motivation comes from Malmendier & Tate (2005), Cooper et al. (1988), Camerer & Lovallo (1999), Weinstein (1980), Taylor & Brown (1988), Larwood & Whittaker (1977), and [[@Akerlof1982|Akerlof & Dickens (1982)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
