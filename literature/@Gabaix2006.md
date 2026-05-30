---
citekey: Gabaix2006
title: "Shrouded attributes, consumer myopia, and information suppression in competitive markets"
authors: ["Gabaix, Xavier", "Laibson, David"]
year: 2006
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/3Q3ACI65"
pdf: "/Users/jesper/Zotero/storage/UPDGQUIA/Gabaix and Laibson - 2006 - Shrouded attributes, consumer myopia, and information suppression in competitive markets.pdf"
tags: [literature]
keywords: [shrouded-attributes, add-on-pricing, consumer-myopia, behavioral-io, curse-of-debiasing, information-suppression, loss-leader-pricing]
topics: []
related: [Milgrom1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Bayesian consumers infer that hidden add-on prices (e.g., the cost of ink for a printer) are likely to be high prices. If consumers are Bayesian, firms will not shroud information in equilibrium. However, shrouding may occur in an economy with some myopic (or unaware) consumers. Such shrouding creates an inefficiency, which firms may have an incentive to eliminate by educating their competitors' customers. However, if add-ons have close substitutes, a "curse of debiasing" arises, and firms will not be able to profitably debias consumers by unshrouding add-ons. In equilibrium, two kinds of exploitation coexist. Optimizing firms exploit myopic consumers through marketing schemes that shroud high-priced add-ons. In turn, sophisticated consumers exploit these marketing schemes. It is not possible to profitably drive away the business of sophisticates. It is also not possible to profitably lure either myopes or sophisticates to nonexploitative firms. We show that informational shrouding flourishes even in highly competitive markets, even in markets with costless advertising, and even when the shrouding generates allocational inefficiencies.

## Summary
Gabaix and Laibson formalize Ellison's conjecture that some consumers ignore "add-on" prices (printer ink, hotel phone charges, bank fees) when choosing a base good. They show that with a positive share of such *myopic* consumers, competitive firms shroud high add-on prices and set loss-leader base-good prices — and that this shrouding is robust even with free advertising and many competitors. The key mechanism is a **curse of debiasing**: educating a rival's myopic customer turns her into a sophisticate who learns to substitute away from the overpriced add-on while still enjoying the loss-leader base price, so she has *no* reason to defect to a transparent, marginal-cost firm. Educating consumers helps consumers but lowers the educating firm's profit, so no firm does it. Two kinds of exploitation coexist in equilibrium: firms exploit myopes, and sophisticates exploit the firms' myope-targeted pricing. I read the full 36-page article (model, all propositions, extensions, measurement/regulation section, and conclusion).

## Research question
When does competition force firms to *unshroud* (reveal) costly add-on prices, and when does shrouding instead survive — even in highly competitive markets with costless advertising? Equivalently: why do firms gratuitously hide information that rational-consumer theory says competitors should profitably reveal (the Milgrom-Jovanovic unraveling logic, echoed by Shapiro 1995)?

## Method / identification
A three-period, symmetric-information *game* of price-setting with boundedly rational consumers. Population fractions: myopes $\alpha$ and sophisticates $1-\alpha$. Each firm chooses (i) whether to **shroud** or **unshroud** the add-on (binary, unshrouding is free, equivalent to advertising the price), and (ii) a base-good price $p$ and add-on price $\hat p$. Sophisticates always account for the add-on, forming Bayesian posteriors $E\hat p$ when it is shrouded; uninformed myopes ignore it entirely. Unshrouding informs all sophisticates and a fraction $\lambda\in(0,1]$ of myopes (informed myopes then behave exactly like sophisticates). The add-on fee is bounded above by $\bar p$, and a consumer can pay effort cost $e$ to *substitute away* from the add-on (she does so iff $e<E\hat p$); avoidability requires $\bar p>e$.

Demand at firm $i$ depends on net-surplus difference $x_i$ relative to rivals' (starred) prices: for sophisticates $x_i=-p_i+p^\*$, while uninformed myopes use only $x_i=-p_i+p^\*$ on the base good and neglect the add-on. The demand function $D(x_i)$ is increasing in $[0,1]$, with competition parameterized by $\mu=D(0)/D'(0)$ (equal to average profit per consumer; $\mu=0$ is perfect competition). The solution concept is **symmetric sequential equilibrium**, with sophisticates holding consistent off-path beliefs that a shrouding firm charges $\hat p=\bar p$. Section III.B generalizes to *continuous* add-on demand; an extension allows myopes to *learn* (purchase the add-on $T_{MM}$ times before becoming sophisticated).

## Data
None — this is a theory paper. It is, however, heavily motivated by stylized facts and cites supporting empirical work: Cruickshank (2000) on UK bank-fee ignorance; Hall (2003) that only 3% of printer buyers know ink costs at purchase; Agarwal et al. (2005) that bank add-on fees decline with customer tenure (consistent with learning); Hausman (1979), Barber-Odean-Zheng, Hossain-Morgan, and Choi et al. (2005) on muted consumer response to delayed/shrouded costs.

## Key findings
- **Proposition 1 (discrete demand).** Define the myopia threshold $\alpha^\dagger\equiv e/\bar p$ and $\mu=D(0)/D'(0)$. If $\alpha>\alpha^\dagger$, a **Shrouded Prices Equilibrium** exists with $p=-\alpha\bar p+\mu$ and $\hat p=\bar p$: firms charge the maximal add-on markup, only myopes buy it, and the allocation is inefficient (sophisticates burn effort $e$ to substitute away). If $\alpha<\alpha^\dagger$, an efficient **Unshrouded Prices Equilibrium** exists with $p=-e+\mu$, $\hat p=e$. Industry profit is $\mu$ in both. With small $\mu$ the base good is a loss leader ($p\approx-\alpha\bar p<0$) — the add-on is the profit center.
- **The curse of debiasing.** Under perfect competition ($\mu=0$), a sophisticate at a shrouding firm earns surplus $-p-e=\alpha\bar p-e>0$, strictly more than the $0$ she gets at a marginal-cost transparent firm. So educated consumers *prefer* high-markup firms, are subsidized by myope-targeted pricing, and cannot be profitably attracted away or driven off. No firm has an incentive to unshroud, even for free.
- **Proposition 2 (welfare).** Social welfare loss in the Shrouded equilibrium is $\Lambda=(1-\alpha)e$ (the avoidance effort of all sophisticates); sophisticates are $\bar p-e$ units better off than myopes. The Unshrouded equilibrium is efficient. Distortions are largely redistributive.
- **Proposition 3 (learning).** With learning, the threshold becomes $\alpha^{\dagger\dagger}\equiv \frac{e}{\bar p}\frac{\max(T_S,\,T_{MM}+T_{MS})}{T_{MM}}$ and $p=-\alpha\bar p T_{MM}+\mu$; shrouding persists despite consumers eventually becoming sophisticated.
- **Debiasing ratio.** Generalizing across attributes, an attribute is shrouded iff $B=\alpha\bar p/e>1$; with a fixed unshrouding cost $C$ the numerator gains $kC$, so shrouding is more pervasive in less competitive markets — yielding a testable cross-market prediction ($B$ high $\Rightarrow$ more shrouding).

## Contribution
Provides the canonical behavioral-IO model in which voluntary *information suppression* survives perfect competition and free advertising — overturning the Milgrom-Jovanovic unraveling and Shapiro's conjecture that competition eliminates aftermarket markups. Unlike search-cost or commitment-based rational explanations of high add-on markups, shrouding here is endogenous and gratuitous, driven solely by a minority of myopic consumers. The curse of debiasing explains why firms refuse to educate consumers even when doing so is costless, and the framework underpins much subsequent work on naive/sophisticated heterogeneity and consumer protection.

## Limitations & open questions
The authors flag several explicit hooks: (i) the propensity to *become* sophisticated should increase with the cost of behaving myopically — "an interesting extension of the framework" they do not pursue; (ii) **narrow framing** — if unshrouding by one firm only makes consumers think about *that* firm's add-on (not rivals'), unshrouding is impeded; (iii) costly education/advertising ($C>0$) impedes unshrouding and makes shrouding more pervasive in less competitive markets; (iv) long-run dynamics — whether learning and innovation (new add-ons) reach a steady state of shrouding; (v) heterogeneous tastes plus heterogeneous add-ons can *favor* informative advertising and unshrouding; (vi) third-party education (Consumer Reports) is imperfect because nonprofits are underfunded and for-profit advisors have incentives to mislead. On measurement they propose five diagnostic strategies and discuss the pitfalls of regulatory remedies (markup caps, mandated disclosure, pro-competitive entry rules).

## Connections
Directly formalizes a conjecture of Ellison (2005) on add-on pricing and price discrimination, and contrasts with rational add-on theories based on exogenous search costs (Diamond 1971; Salop & Stiglitz 1977; Stahl 1989; Lal & Matutes 1994; Hortacsu & Syverson 2004) and on commitment failure (Klemperer 1987; Borenstein, MacKie-Mason & Netz 1995; Farrell & Klemperer 2005). It overturns the unraveling logic of [[@Milgrom1981|Milgrom (1981)]] and Jovanovic (1982) and Shapiro's (1995) competitive-debiasing claim. The naive/sophisticated cross-subsidy mechanism parallels DellaVigna & Malmendier (2004), where it arises from self-control problems rather than myopia, and connects to Heidhues & Koszegi work on exploitative contracting, Mullainathan & Shleifer (2005) on persuasion, Spiegler (2006) on competition with boundedly rational agents, and the broader behavioral-IO surveys. Empirical companions include Agarwal et al. (2005), Hall (2003), Choi et al. (2005), Barber, Odean & Zheng, and Hossain & Morgan.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
