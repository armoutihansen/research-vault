---
citekey: Loomes1987
title: Testing for Regret and Disappointment in Choice Under Uncertainty
authors: ["Loomes, Graham", "Sugden, Robert"]
year: 1987
type: journalArticle
doi: 10.2307/3038234
zotero: "zotero://select/library/items/KM2WV5J2"
pdf: /Users/jesper/Zotero/storage/B6JRRFMA/Loomes1987.pdf
tags: [literature]
keywords: [regret-theory, disappointment-theory, common-ratio-effect, expected-utility-violations, allais-paradox, non-expected-utility]
topics: []
related: [Bell1985, Kahneman1979]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Loomes and Sugden design an incentivised experiment to separate two psychologically-motivated, non-expected-utility theories of choice under risk: their own *regret theory* and *disappointment theory*. Both explain the Allais common-ratio effect, but through different channels — regret operates through the statistical *overlap* $\omega$ between the states in which two prospects pay off, while disappointment operates through the probability $p$ of winning. By independently varying $\omega$ and $p$ across four subsamples, the authors isolate a "pure disappointment effect" and a "pure regret effect". They find expected utility theory performs poorly, a strong and significant disappointment effect, and a weaker, inconsistent regret effect.

## Research question
Can the common-ratio (Allais-type) violations of expected utility theory be attributed to regret/rejoicing, to disappointment/elation, or to both — and what is their relative importance? The key methodological problem is that regret theory and disappointment theory (and related theories such as Bell's, Fishburn's SSB, and Machina's) generate near-identical predictions on the choice problems used in prior experiments, so a design is needed in which the two theories yield *distinct* predictions.

## Method / identification
Both theories share a structure over actions $A_i$ (n-tuples of state-contingent consequences $x_{ij}$ in states $S_j$ with probabilities $p_j$), each consequence carrying a Bernoullian "basic utility" $c_{ij}$.

Regret theory adds a regret/rejoice term: the modified utility of experiencing $x_{ij}$ while the foregone action would have given $x_{kj}$ is $c_{ij}+R(c_{ij},c_{kj})$. Defining the skew-symmetric $\Psi(x_{ij},x_{kj})=c_{ij}-c_{kj}+R(c_{ij},c_{kj})-R(c_{kj},c_{ij})$, the decision rule is
$$A_i \succeq A_k \iff \sum_j p_j\,\Psi(x_{ij},x_{kj}) \geq 0.$$
The crucial restriction is **convexity**: for $C(x)<C(y)<C(z)$, $\Psi(z,y)+\Psi(y,x)<\Psi(z,x)$.

Disappointment theory compares the realised consequence to a prior expectation $\bar{c}_i=\sum_j p_j c_{ij}$. A decrement applies when $c_{ij}-\bar{c}_i<0$ (disappointment) and an increment when positive (elation), via $D(\cdot)$, giving the rule
$$A_i \succeq A_k \iff \sum_j p_j\big[(c_{ij}-c_{kj})+D(c_{ij}-\bar{c}_i)-D(c_{kj}-\bar{c}_k)\big]\geq 0,$$
with $D(\cdot)$ increasing, convex for positive and concave for negative arguments, gradient $<1$.

The identification trick: for prospects $A$ (pays $a$ with prob $\lambda p$) and $B$ (pays $b<a$ with prob $p$), introduce the overlap parameter $\omega$ = probability that $B$ gives $b$ conditional on $A$ giving $a$. Regret theory makes the $A$-vs-$B$ preference depend on $\omega$ but *not* on $p$; disappointment theory makes it depend on $p$ but *not* on $\omega$. Under statistical independence $\omega=p$, so ordinary common-ratio experiments confound the two. The design breaks this by constructing choice matrices over 24 equiprobable states where $\omega$ and $p$ are set separately.

The experiment used "triples": each subject answered a Type 1 ($p=1$), a Type 2 ($p=0.5$) and a Type 3 ($p=0.167$) problem, with $\lambda=0.75$. Variants (i) set $\omega=0$ and (ii) set $\omega=1$. Four subsamples received different combinations, allowing within- and between-subsample tests. Choices were real-money incentivised: one randomly selected problem per subject was played out using a pre-drawn sealed ticket (1–24).

## Data
Original experimental data: 120 undergraduates at the University of Newcastle upon Tyne (excluding those who had had lectures on choice under uncertainty), split into four subsamples of 30. Each faced two triples with payoffs $(a,b)=(\pounds4.50,\pounds3.00)$ and $(\pounds24.00,\pounds16.00)$. Each triple has 8 logically possible choice patterns, of which only $\{A',A'',A'''\}$ and $\{B',B'',B'''\}$ are EU-consistent.

## Key findings
- **EU theory fails badly:** only 42/120 (small triple) and 38/120 (large triple) chose an EU-consistent pattern — barely above chance.
- **Violations are systematic, not random "mistakes":** under the null that subjects are true EU-preferrers making symmetric independent errors, the three ways of choosing "2 B's and 1 A" should be equiprobable. Instead ~80–83% of such subjects chose the specific common-ratio pattern $\{B',B'',A'''\}$, and ~80–84% of "1 B, 2 A" subjects chose $\{B',A'',A'''\}$. The mistakes hypothesis is rejected at $p<0.001$.
- **Disappointment effect is significant:** holding $\omega=1$, switching from $B\succ A$ to $A\succ B$ as $p$ falls is significant, concentrated in the fall from $p=0.5$ to $p=0.167$ ($p<0.005$), suggesting the indifference point $p^*$ lies in that range. Notably weak effect as $p$ first leaves certainty — contradicting Kahneman–Tversky's emphasis on a special role for certainty.
- **Regret effect is weaker and inconsistent:** for Type 2 problems the association between $\omega$ and the $A'':B''$ ratio is decisively in the predicted direction; but for Type 3 problems it is negligible (large triple) or even *reversed* (small triple, $\chi^2=0.003$). The authors call this contrast "puzzling".

## Contribution
First experimental design explicitly constructed to *discriminate* between regret and disappointment as competing explanations of the common-ratio effect, rather than merely to reject expected utility. It supplies real-money evidence that the common-ratio effect is robust and orderly, and offers tentative support that disappointment (a $p$-driven, independence-axiom-violating mechanism) is the stronger driver, with regret playing a secondary, less reliable role.

## Limitations & open questions
- Small sample makes findings "far from definitive" and "suggestive" only.
- The design gives no exactly analogous test of a pure regret effect, because no subsample saw problems with the same $p$ but different $\omega$; regret tests rely on between-subsample comparisons.
- The reversed/negligible Type 3 regret result is unexplained: the authors conjecture that disappointment, by producing so many independence violations as $p$ falls to 0.167, may swamp any extra regret effect — but admit this cannot explain the *perverse* Type 3 small-triple result. "Some other explanation, or some further evidence, is required."
- Whether regret and disappointment are truly complementary (co-occurring) versus substitutes is left open.

## Connections
The paper synthesises and tests the authors' own regret theory (Loomes & Sugden, 1982; 1986b) and disappointment theory (Loomes & Sugden, 1984; 1986a), the latter building on [[@Bell1985|Bell (1985)]]; Bell (1982) is the parallel regret formulation. The regret apparatus is shown equivalent in predictions to Fishburn's (1982, 1983) nontransitive SSB utility theory. The common-ratio effect originates with Allais (1953) and is connected to broader non-EU work by Chew & MacCrimmon (1979) and to Machina's (1982) "Hypothesis II". Empirical antecedents on the common-ratio effect include [[@Kahneman1979|Kahneman & Tversky (1979)]], MacCrimmon & Larsson (1979), and Hagen (1979); surveys by Schoemaker (1982) and Machina (1983) frame the literature. The certainty-effect discussion engages directly with prospect theory of [[@Kahneman1979|Kahneman & Tversky (1979)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
