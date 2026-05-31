---
citekey: Milgrom1986
title: Price and Advertising Signals of Product Quality
authors: ["Milgrom, Paul", "Roberts, John"]
year: 1986
type: journalArticle
doi: 10.1086/261408
zotero: "zotero://select/library/items/QLRDSBDI"
pdf: /Users/jesper/Zotero/storage/MBV6FNYS/Milgrom1986.pdf
tags: [literature]
keywords: [signaling, advertising, product-quality, experience-goods, equilibrium-refinement, industrial-organization, repeat-purchases]
topics: ["[[advertising-signaling-quality]]"]
related: [Nelson1970]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We present a signaling model, based on ideas of Phillip Nelson, in which both the introductory price and the level of directly "uninformative" advertising or other dissipative marketing expenditures are choice variables and may be used as signals for the initially unobservable quality of a newly introduced experience good. Repeat purchases play a crucial role in our model. A second focus of the paper is on illustrating an approach to refining the set of equilibria in signalling games with multiple potential signals.

## Summary
Milgrom and Roberts formalize Nelson's conjecture that conspicuously "uninformative" advertising for a new experience good can credibly signal high quality. Unlike Nelson, they let the monopolist choose *both* the introductory price $P$ and dissipative advertising $A$, so price could in principle convey the same information and make advertising redundant. Working with a repeat-purchase model and a sequence of equilibrium refinements (sequential equilibrium, sequential elimination of dominated strategies, the Kreps "intuitive criterion"), they show that generically a *unique* separating equilibrium exists in which the high-quality firm distorts price and may *also* burn money on advertising, because using two signals separates types at lower total cost than price alone. A corollary: banning purely dissipative advertising can be Pareto-worsening.

## Research question
Can apparently content-free advertising serve as a credible signal of product quality once the firm can *also* set price freely? If price and advertising are both choice variables, when is each used as a signal, and is advertising ever used given that price could carry the same information? More broadly, how can the notorious multiplicity of equilibria in signaling games with multiple signals be refined to a small or unique set?

## Method / identification
A two-type ($q\in\{H,L\}$) signaling game of incomplete information in extensive form. A monopolist who has developed a new experience good of exogenous, privately known quality chooses an introductory price $P$ and dissipative advertising $A\ge 0$; customers observe $(P,A)$, form a belief $p(P,A)$ that quality is $H$, buy, learn quality through use, and repeat-purchase. Let $\Pi(P,q,p)-A$ be the firm's expected present value of profit. The paper proceeds in two layers.

First, a **reduced-form/diagrammatic analysis** in $(P,A)$ space using isoprofit curves of $\pi(P,q,Q)\equiv\Pi(P,q,1\text{ or }0)$, with full-information prices $P^q=\arg\max_P\pi(P,q,q)$. Equilibrium is pinned down by a *cascade of refinements*: (i) **sequential equilibrium** (Kreps–Wilson) forces explicit off-path beliefs; (ii) **sequential elimination of dominated strategies** forces off-path beliefs to assign zero probability to types for whom a $(P,A)$ choice is dominated, enlarging the set of choices read as $H$ as far as possible; (iii) the **Kreps (1984) intuitive criterion** kills pooling equilibria where the firm could profitably deviate to a point only $H$ would want. These restrictions reduce play to: the $L$ firm picks its full-information optimum $(P^L,0)$; the $H$ firm does *just enough* signaling. The $H$'s choice solves the constrained program
$$\max_{P,A}\ \pi(P,H,H)-A \quad\text{s.t.}\quad \pi(P,L,H)-A\le \pi(P^L,L,L),\ P,A\ge 0.$$
When the advertising constraint binds with $A^*>0$, the price solves $\max_P\ \pi(P,H,H)-\pi(P,L,H)$, i.e. it sits at a *tangency* $P^T$ of the two types' isoprofit curves.

Second, a **fully specified repeat-purchase example**: customers indexed by valuation on $[0,R]$ uniform; quality $q\in(0,1]$ is the probability a unit is satisfactory; constant marginal cost $C_q$ (with $C_H>C_L$ *not* assumed); common discount factor $\delta$ and horizon $T$, with $A=\sum_t\delta^t$. A satisfied marginal customer has $r^*=P/Q(p)$ where expected quality $Q(p)=pH+(1-p)L$, giving first-period demand $R-P/Q(p)$ and postintroductory demand $q(R-r^*)$. This generates closed-form $\Pi$ and comparative statics in $C_H$.

## Data
None — this is a pure game-theoretic / industrial-organization paper. The "Diet Coke" and "1984 Ford Ranger" television campaigns are motivating anecdotes, not data.

## Key findings
- **Proposition 1.** A separating *sequential* equilibrium exists iff some $(P,A)\ge 0$ satisfies $\pi(P,H,H)-\pi(P^H,H,L)\ge A\ge\pi(P,L,H)-\pi(P^L,L,L)$. Typically a whole region of such equilibria exists, most supported by implausible beliefs.
- **Proposition 2.** Imposing immunity to sequential elimination of dominated strategies, the $H$ firm's equilibrium $(P^H,A^H)$ must solve the constrained program above; off-path, $p(P,A)=1$ exactly on/above the curve $A(P)$ defined by $\pi(P,L,H)-A=\pi(P^L,L,L)$.
- **Proposition 3.** Under regularity conditions (4)–(6) — chiefly that $L$ would pay to be seen as $H$, a relevant tangency exists, and a pseudoconcavity condition holds — there is a separating equilibrium with *positive* advertising, unique under strict pseudoconcavity. If the price differential alone suffices, or condition (7) holds, all separating equilibria have $A=0$.
- **Proposition 4.** Under a generalized single-crossing condition (8) — a multidimensional analog of Spence's condition asserting there is always a feasible direction in $(P,A)$ space cheaper for $H$ than $L$ — a separating equilibrium exists *and* no pooling equilibrium survives the Kreps criterion.
- **Substantive results.** Both price and advertising are generically used as signals; price may be *raised or lowered* from its full-information level depending on whether $P^H\gtrless P^L$. With $C_H<C_L$ (high quality cheaper, e.g. a breakthrough), the firm signals only via low introductory prices / free samples and uses *no* advertising. Advertising appears only for moderate $C_H>C_L$, where the equilibrium ad level first rises then falls in cost. A ban on dissipative advertising is **Pareto-worsening**: the $H$ firm raises price, profits fall for $H$, are unchanged for $L$, and customers get the same information at higher prices.

## Contribution
First fully specified formal model jointly endogenizing price *and* dissipative advertising as quality signals with explicit repeat purchases, closing the gap in Nelson's informal argument and correcting its intuition: the "marginal benefit of an extra initial sale" is *not* well defined once price is a choice variable, so Nelson's claim that $H$ always benefits more from an initial sale (and hence advertises) does not survive. Methodologically, the paper is an early and influential demonstration of how to refine signaling games with *multiple* signals to a unique equilibrium, layering sequential equilibrium, iterated dominance, and the Kreps intuitive criterion — connecting them to Kohlberg–Mertens strategic stability.

## Limitations & open questions
- **Monopoly only.** The analysis assumes a single seller; the authors explicitly note that "treating the intermediate case of oligopoly would involve significant additional problems."
- **Two qualities, exogenous quality.** Quality is binary and *given*, not chosen — so there is no moral-hazard / quality-cheating dimension (contrast Klein–Leffler 1981, Shapiro 1983). Wilson (1985) is cited as extending to a continuum of qualities and any finite number of signals; generalizing the refinement machinery there is left open.
- **New products only.** Strictly applicable to newly introduced experience goods; "says little about advertising for established brands."
- **Residual pooling.** Because the single-crossing condition (8) holds only *almost everywhere* in the explicit example (failing exactly at prices $P^T(p)$), some pooling equilibria survive the Kreps criterion — full uniqueness is not achieved, an acknowledged loose end.
- **Endogenous conditions.** Propositions 1–4 are stated on the endogenous $\Pi$ function; whether they hold must be checked in primitive-based models, done only for one example.

## Connections
The paper is the formal completion of **[[@Nelson1970|Nelson]] (1970, 1974, 1978)** on search vs. experience goods and advertising as a quality signal. It is the multidimensional, price-inclusive counterpart to **Kihlstrom and Riordan (1984)**, where firms do not choose prices, and is contrasted with **Schmalensee (1978)** (rule-of-thumb consumers, low-quality firms advertise) and **Johnsen (1976)** (no existence with two signals). On the quality-as-choice / repeat-business side it complements **Klein and Leffler (1981)** and **Shapiro (1983)**. The signaling structure descends from **Spence (1973)**; the refinement apparatus draws on **Kreps and Wilson (1982)** (sequential equilibrium), **Moulin (1979)** and **Pearce (1982)** (dominance), **Kreps (1984)** (intuitive criterion), and **Kohlberg and Mertens (1984)** (strategic stability), with **Milgrom and Roberts (1982)** as the authors' related limit-pricing/entry-signaling work. **Wilson (1985)** extends the model to a quality continuum and arbitrarily many signals.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
