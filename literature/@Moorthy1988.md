---
citekey: Moorthy1988
title: Product and Price Competition in a Duopoly
authors: ["Moorthy, K. Sridhar"]
year: 1988
type: journalArticle
doi: 10.1287/mksc.7.2.141
zotero: "zotero://select/library/items/LHWB3YHQ"
pdf: /Users/jesper/Zotero/storage/TSY2SST4/Moorthy1988.pdf
tags: [literature]
keywords: [vertical-differentiation, product-positioning, price-competition, duopoly, first-mover-advantage, hotelling, industrial-organization]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper examines the role of consumer preferences, costs, and price competition in determining the competitive product strategy of a firm. In the model studied here, there are two identical firms competing on product quality and price. They face consumers who prefer a higher quality product to a lower quality product, but differ in how much they are willing to pay for quality. The consumers can also choose a substitute if they don't like the product-price offerings of the two firms. For the firms, a higher quality product costs more to produce than a lower quality product. The paper shows that the equilibrium strategy for each firm should be to differentiate its product from its competitor, with the firm choosing the higher quality choosing the higher margin as well. This differentiation, however, is not efficient—that is, it is possible to choose two other products and offer them at prices that cover their marginal cost, and still satisfy consumers' "needs" better in the aggregate. A monopolist, by contrast, would differentiate his product line efficiently. This suggests that cannibalization has different effects on product strategy than competition. The paper also shows that if one firm enters the market first, then it can defend itself from later entrants, and gain a first-mover advantage, by preempting the most desirable product position.

## Summary
Moorthy builds a tractable vertical-differentiation duopoly in which two identical firms each pick one product *quality* and then a price, facing consumers who all prefer more quality but differ in marginal willingness to pay, plus an outside (substitute) option. Unlike the constant-cost vertical-differentiation models of Shaked and Sutton (1982), quality here is costly and marginal cost rises faster than any consumer's willingness to pay. The central result is that competing firms differentiate — but *inefficiently*, choosing qualities that are too high relative to the surplus-maximizing benchmark — whereas a multiproduct monopolist differentiates efficiently. Thus competition and cannibalization push product lines in genuinely different directions. With sequential entry, the first mover preempts a favorable position close to the monopolist's ideal and earns a first-mover advantage.

## Research question
What determines a firm's competitive product (quality) position when it must simultaneously trade off consumer preferences, increasing manufacturing costs, price competition with a rival, and competition from an outside substitute? Specifically: do firms move toward or away from a competitor, is the resulting differentiation efficient, how does competition differ from a monopolist's cannibalization problem, and is there a first-mover advantage under sequential entry?

## Method / identification
A two-stage game-theoretic (subgame-perfect Nash) model of vertical product differentiation. Setup: two firms $i=1,2$ each choose a quality $s_i\in[0,\infty)$, then choose prices $p_i$; quality is chosen first because it is the more committed variable, and the two-stage structure (Stokey 1980) restores existence of a pure-strategy equilibrium. A type-$t$ consumer is willing to pay $ts$ for quality $s$, with types distributed uniformly on $[a,b]$, $0<a<b$. Each consumer buys at most one unit, choosing whichever offer maximizes surplus $ts_i-p_i$, or the outside substitute (normalized to quality and price zero) if no surplus is positive. Marginal cost is quadratic, $c(s)=\alpha s^2$ with $\alpha>0$, so cost rises faster than any consumer's willingness to pay; this bounds the highest quality any consumer would buy, $s_0(t)$ solving $ts_0(t)-\alpha[s_0(t)]^2=0$.

Proposition 1 characterizes markets as adjacent intervals of types stacked by quality, with the marginal consumer between neighboring qualities at type $(p_2-p_1)/(s_2-s_1)$ and the substitute boundary at $p_1/s_1$. The author assumes the market is "diverse" ($b/a$ large, sufficient condition $b>5a$) so firms leave some share to the substitute. Two benchmarks are derived under one decision-maker: the **efficient solution** (maximize aggregate total surplus $\sum_i \int (ts-\alpha s^2)$ under marginal-cost pricing — the efficient product for type $t$ is $s^*(t)=t/2\alpha$), and the **monopolist's** two-product solution (maximize $\sum_i (t_{i+1}-t_i)(p_i-\alpha s_i^2)$). Then the price equilibrium is solved for fixed qualities, and best-response functions in quality are derived from the first-order conditions and intersected (Figure 4) to find the product equilibrium, distinguishing a *local* equilibrium (fixed quality ordering) from a *global* one (using each firm's global best-response, Figure 5). Section 6 re-solves with sequential quality choice.

## Data
None — this is a purely theoretical paper. Results are analytic, with closed-form and numerically-approximated equilibrium values for products, prices, margins, shares, profits, and consumer surplus expressed in $b/\alpha$ units; figures plot best-response and profit functions.

## Key findings
- **Proposition 1**: each firm's market is an interval of types; segment boundaries are the indifferent consumer types; segments stack in order of quality.
- **Proposition 2**: if both firms choose the same quality, the unique price equilibrium is marginal-cost pricing and both earn zero profit — the discontinuity driving differentiation.
- **Proposition 3**: regardless of the rival's position, each firm's best product is a *distinct* quality in $(0,s_0(b))$ — minimum differentiation is never optimal once price competition and costs are present.
- **Price equilibrium** (for $s_1<s_2$): margins solve $p_1-\alpha s_1^2=\big[\frac{s_1(s_2-s_1)}{4s_2-s_1}\big][b+\alpha(s_2-s_1)]$ and the analogous expression for the high-quality firm; firms are strategic complements (Bulow, Geanakoplos and Klemperer 1985).
- **Proposition 4 (simultaneous choice)**: for $b\ge 2.2705\alpha$ there are two (mirror-image) pure-strategy equilibria with qualities $\approx 0.2474 b/\alpha$ and $0.5288 b/\alpha$. The qualities are *too high* versus the efficient pair $0.2b/\alpha,\,0.4b/\alpha$, so the equilibrium is product- *and* coverage-inefficient. Contrary to Shaked–Sutton, being the higher-quality firm is *not* always better: for $s_2>0.2908b/\alpha$ a firm prefers to be the lower-quality supplier (high cost outweighs the gain from escaping the rival). The lower-quality firm earns the *higher* profit here.
- **Proposition 5 (sequential entry)**: for $b\ge 3.2383\alpha$ the first entrant chooses $\approx 0.2908b/\alpha$ (near the monopolist's single-product ideal $b/3\alpha$) and the second responds with $\approx 0.1477b/\alpha$. Foresight about future entry raises the first entrant's profit (value of foresight $\approx 0.0004 b^3/\alpha$), and there is a genuine first-mover advantage ($\approx 0.0111 b^3/\alpha$) from preempting a favorable position and controlling the rival's choice. Sequential entry yields higher coverage efficiency and higher consumer surplus than simultaneous choice, and the high-quality firm now earns more.

## Contribution
The paper supplies theoretical foundations for the marketing prescription to differentiate ("fill holes" / focus strategy of Porter 1980), but qualifies it sharply: differentiation is the equilibrium, yet it is *inefficient* under competition, in contrast to a monopolist who positions his two products efficiently. The driving insight is the tension between two forces — one pulling each firm toward the monopolist's best position (preferences, costs, substitute) and one pushing it away from the rival to soften price competition. It cleanly separates cannibalization (internalized by a monopolist) from inter-firm competition (not internalized), and it adds costly quality plus an outside substitute to the vertical-differentiation literature, breaking the Shaked–Sutton result that higher quality always dominates.

## Limitations & open questions
- Results lean on specific functional forms: linear willingness-to-pay $ts$, quadratic cost $\alpha s^2$, and a uniform type distribution. The author notes (footnote, citing Moorthy 1984) that the exact offsetting of cannibalization and substitute competition that makes the *monopolist* position efficiently is an artifact of linear, uniform preferences; with nonlinear or nonuniform preferences the monopolist's products may be higher or lower than efficient — leaving open how robust the duopoly inefficiency result is.
- Single product attribute and single unit of demand per consumer; perfect information (no distinction between perceptual and physical position).
- The substitute is *passive* (fixed quality and price); endogenizing it, or modeling more than two firms, is left open.
- Entry timing is not modeled explicitly (the monopoly interlude before entry is ignored); product changes are assumed prohibitively costly, ruling out post-entry repositioning à la Hauser and Shugan (1983).
- Equilibrium existence requires "diverse" markets ($b$ large relative to $a$); the market-covered regime and mixed-strategy equilibrium are noted but not the focus.

## Connections
The model is squarely in the Hotelling (1929) spatial-competition tradition, but converts horizontal to vertical differentiation: all consumers share the ideal point "infinite quality." It directly engages d'Aspremont, Gabszewicz and Thisse (1979), who repaired Hotelling's flawed minimum-differentiation argument and obtained maximal differentiation, and Shaked and Sutton (1982), whose constant-cost vertical model yields "quality always wins" — overturned here by costly quality. The benchmark monopoly/price-discrimination analysis builds on the author's own Moorthy (1984). Sequential-entry preemption parallels Prescott and Visscher (1977), Rao (1977), and Lane (1980), and contrasts with the reactive defensive strategy of Hauser and Shugan (1983); Hauser (1988) models product-and-price competition similarly but with Hotelling-like heterogeneous ideal points and constant cost. Strategic complementarity in prices invokes Bulow, Geanakoplos and Klemperer (1985), and the two-stage existence rationale follows Stokey (1980). Earlier non-equilibrium marketing treatments include Kuehn and Day (1962), with related work by Karnani (1983), Rao and Bass (1985), and Eliashberg and Jeuland (1986); the minimum-differentiation political analogy traces to Downs (1957) and Riker and Ordeshook (1973).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
