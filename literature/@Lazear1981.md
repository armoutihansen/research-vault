---
citekey: Lazear1981
title: Rank-Order Tournaments as Optimum Labor Contracts
authors: ["Lazear, Edward P.", "Rosen, Sherwin"]
year: 1981
type: journalArticle
doi: 10.1086/261010
zotero: "zotero://select/library/items/VR8M3W63"
pdf: /Users/jesper/Zotero/storage/EW4PY6EP/Lazear and Rosen - 1981 - Rank-Order Tournaments as Optimum Labor Contracts.pdf
tags: [literature]
keywords: [tournament-theory, rank-order-incentives, piece-rates, relative-performance-evaluation, personnel-economics, risk-aversion, adverse-selection]
topics: []
related: [Nalebuff1983]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Lazear and Rosen show that paying workers by their *rank* in a contest — fixed prizes awarded for finishing first, second, etc., independent of the margin of victory — can be an optimal labor contract. With risk-neutral workers, rank-order tournaments replicate exactly the efficient resource allocation of an optimal piece rate, so the choice between them turns purely on monitoring costs: ranking workers may be cheaper than measuring each one's absolute output. When workers are risk-averse and luck has high variance, tournaments can strictly dominate piece rates because they cap gains and losses in advance. The paper thus rationalizes why executive and "superstar" pay can vastly exceed marginal product, and why earnings spread across workers far exceeds the spread in their productivities.

## Research question
Can a compensation scheme based on a worker's *relative position* within the firm, rather than the absolute level of output, be the optimal and naturally emerging outcome of a competitive labor market? And under what conditions does such a rank-order "prize" scheme dominate the standard piece rate?

## Method / identification
Pure theory. Worker $j$ produces lifetime output $q_j = \mu_j + \varepsilon_j$, where $\mu_j$ is a precommitted, costly investment in skill (the choice variable) and $\varepsilon_j$ is i.i.d. luck with $E(\varepsilon_j)=0$. Investment costs $C(\mu)$ with $C'>0$, $C''>0$. Firms are risk-neutral expected-value maximizers selling output at competitive price $V$; contracts are chosen to maximize worker utility subject to a zero-profit constraint, so the market equilibrium attains the unconditional maximum over conditional optima.

**Piece rate.** With wage $rq$, the worker sets $C'(\mu)=r$; competition bids $r=V$, giving the efficient condition $C'(\mu)=V$.

**Two-player tournament.** A fixed winner prize $W_1$ and loser prize $W_2$ are set in advance; the winner is whoever draws the larger $q$. Expected utility is $PW_1+(1-P)W_2-C(\mu)$ where $P=\mathrm{prob}(q_j>q_k)=G(\mu_j-\mu_k)$ and $G$ is the cdf of $\xi=\varepsilon_k-\varepsilon_j$ with density $g$. Under Nash–Cournot play (each optimizes against the opponent's equilibrium investment), the first-order condition is
$$(W_1-W_2)\,g(\mu_j-\mu_k)=C'(\mu_i).$$
By symmetry $\mu_j=\mu_k$ and $P=\tfrac12$ at equilibrium, so investment depends only on the *spread* $W_1-W_2$; the prize *levels* govern only entry. Existence requires the variance $\sigma_\varepsilon^2$ of luck to be large enough — "a difference of opinion is necessary for a horse race" — and is verified in an appendix.

**Risk aversion.** With concave $U$, the optimal piece rate and optimal prize structure are derived via second-order (Taylor) approximations under normal $\varepsilon$, yielding comparative statics in $V$, absolute risk aversion $s=-U''/U'$, $C''$, and $\sigma_\varepsilon^2$. The schemes are compared numerically with CARA ($U=-e^{-sy}$) and quadratic utility.

**Extensions.** The model is generalized to $N$-player tournaments (a second appendix shows only the win–show spread matters and that the middle prize $W_2$ is indeterminate under risk neutrality), to sequential elimination tournaments generating skewed reward structures, and to heterogeneous workers with private ability information.

## Data
None — this is a theoretical paper. The only numbers are illustrative simulations (Tables 1 and 2) solving the optimal piece-rate and prize equations for various values of $\sigma_\varepsilon^2$ under CARA and quadratic utility, confirming that piece rates yield higher expected utility for small $\sigma_\varepsilon^2$ and prizes dominate above a threshold.

## Key findings
1. **Equivalence (risk neutrality).** Competitive two-player tournaments and piece rates induce identical, efficient investment $C'(\mu)=V$, and the expected prize equals the expected value of product. The choice between them is governed solely by the relative cost of assessing rank versus measuring individual output.
2. **Prizes exceed marginal product.** Optimal prizes are set to manipulate incentives via the spread, so the winner's wage can greatly exceed his marginal product — explaining large observed pay differentials (relevant to executive pay).
3. **Spread, not level, drives effort.** Investment responds only to $W_1-W_2$ (and in $N$-player games only to the win–show spread); levels affect only participation.
4. **Tournaments dominate under risk and high variance.** When workers are risk-averse and $\sigma_\varepsilon^2$ is large, prizes — which fix maximum gain and loss in advance — yield higher expected utility than piece rates, which force workers to bear luck risk. The crossover threshold is characterized by comparing income variances (a $\pi$-vs-$\sqrt\cdot$ comparison in the approximations). This connects to Friedman's puzzle on skewness in the earnings distribution and preference for lotteries.
5. **Adverse selection.** With heterogeneous workers and asymmetric information, competitive contests do *not* sort workers efficiently: low-quality workers have an incentive to "contaminate" a pool of high-quality workers even absent production complementarities. This pushes high-quality firms toward non-price (handicapping, screening) job-allocation mechanisms.

## Contribution
The paper founded the economics of **rank-order tournaments** as a theory of incentive contracts and of the wage distribution. It supplied a tractable alternative to piece-rate and principal–agent moral-hazard models that explains why pay can be far more dispersed than productivity, why "prizes" attach to ranks (promotions, executive pay, superstar markets), and when relative-performance evaluation is preferable to absolute-performance pay. It remains the canonical reference for tournament theory in personnel and organizational economics.

## Limitations & open questions
- The model analyzes only **prior investment / skill acquisition**, explicitly ignoring **effort expended after skills are acquired** during the play of the game — left for future work.
- Workers can only affect the *mean* of output; the case where workers also affect the **variance** of output is "left for some other occasion."
- **Existence of the Nash equilibrium** is not guaranteed for arbitrary luck densities (the objective need not be concave); it is *assumed* throughout after a sufficient-variance condition, and the authors note marginal conditions cannot fully characterize existence.
- The two schemes are **difficult to "nest" analytically**, forcing reliance on approximations and numerical examples rather than a general dominance ranking.
- Collusion and communication among contestants are ruled out by assumption; the consequences of relaxing this are not explored.
- Efficient sorting under heterogeneity and asymmetric information is an open design problem — the non-price allocation mechanisms are only gestured at.

## Connections
The setup builds directly on the moral-hazard and incentive-contracting literature: Mirrlees (1976) and Stiglitz (1975) on optimal incentive structures within organizations, Ross (1973) and Harris & Raviv (1978) on agency, and Alchian & Demsetz (1972) on monitoring and the firm. The piece-rate benchmark draws on Cheung (1969). The risk-aversion application revisits Friedman (1953) on chance and the personal income distribution. The heterogeneity/adverse-selection discussion connects to the signalling and competitive-insurance-with-asymmetric-information work of Riley (1975), Rothschild & Stiglitz (1976), and Wilson (1977). Companion work by the authors includes Rosen's "Economics of Superstars" (1981) and Lazear's analyses of mandatory retirement and earnings profiles. The tournament framework was subsequently developed by Green & Stoeckenius (1983), [[@Nalebuff1983|Nalebuff & Stiglitz (1983)]] on relative performance evaluation, and Rosen (1986) on elimination tournaments, and tested experimentally by Bull, Schotter & Weigelt (1987).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
