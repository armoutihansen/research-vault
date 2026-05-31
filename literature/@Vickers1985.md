---
citekey: Vickers1985
title: Delegation and the theory of the firm
authors: ["Vickers, John"]
year: 1985
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/KTZGWWY2"
pdf: /Users/jesper/Zotero/storage/VP7LBQ2D/Vickers - 1985 - Delegation and the theory of the firm.pdf
tags: [literature]
keywords: [strategic-delegation, theory-of-the-firm, incentive-compatibility, cournot-oligopoly, principal-agent, stackelberg-leadership]
topics: ["[[strategic-delegation-firm-objectives]]"]
related: [Lazear1981, Nalebuff1983]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Vickers argues that when a principal delegates a decision to an agent whose objectives differ from his own, the principal may prefer the resulting outcome to what he would achieve acting on his own behalf. In strategic (interdependent) settings this is "almost always" true: a $u$-maximiser does not generally maximise $u$, because the equilibrium depends on every player's objective. Reframing delegation as an incentive-compatibility problem, the paper shows that committing to a manager with non-profit-maximising goals can earn a firm higher profits, and draws out implications for the separation of ownership and control, natural-selection justifications of profit maximisation, relative-performance incentive schemes, and horizontal/vertical organisation.

## Research question
When, and why, would a principal optimally appoint an agent whose preferences differ from his own? Equivalently: under what conditions on a game between firms is it *not* optimal for an owner to instruct managers to maximise profit, and what does this imply for the theory of the firm?

## Method / identification
The core is a two-stage game-theoretic argument borrowed from the mechanism-design literature on incentive compatibility (following d'Aspremont and Gérard-Varet 1980; Dasgupta, Hammond and Maskin 1979).

The "game between agents" is an $n$-person normal-form game $F(\alpha)=\{[X_i,U_i(\,\cdot\,;\alpha_i)];\, i=1,\dots,n\}$, where $\alpha=(\alpha_1,\dots,\alpha_n)$ is the vector of agent *types*, $X_i$ is agent $i$'s strategy space, and $U_i$ depends on the strategy profile $x\in X$ and the type $\alpha_i$. This is preceded by an **agent appointment game** $G(z)$ in which each principal $i$ (himself of type $\alpha_i$) chooses an agent type from a set $A_i$; an exogenous **outcome function** $z$ (justified by, e.g., Nash equilibrium of $F$) maps the chosen type vector to an outcome. $G(z)$ is **incentive compatible** for $i$ if, given that others appoint their own type, $i$ optimally appoints his own type $\alpha_i$ (i.e. does not wish to delegate). This mirrors truthful preference revelation.

The characterisation hinges on a generalised Stackelberg notion: $x\in X$ is a **Stackelberg point** for agent $i$ in $F(\alpha)$ if $x$ lies on the other players' joint reaction function and is at least as good for $i$ as any other point on it.

## Data
None — this is a pure theory paper. The Cournot example uses no empirical data; it is an analytical illustration with stylised parameters.

## Key findings
**Proposition (incentive-compatibility characterisation).** Assume $z$ is an undominated Nash outcome function and that for each $i$ there exists a deviating type making the outcome a Stackelberg point for $i$. Then $G(z)$ is incentive compatible for all principals if and only if $z(\alpha)$ is a Stackelberg point for every $i$ in $F(\alpha)$. Intuitively, no one wants to delegate exactly when self-representation already delivers each player his Stackelberg outcome. Much weaker conditions guarantee that delegation *is* strictly advantageous, and "almost always" $G(z)$ fails to be incentive compatible.

**Cournot illustration.** With $n$ firms, common constant unit cost $c$, linear inverse demand $p(Q)=A-Q$, and managers maximising $M_i=\pi_i+\theta_i q_i = p(Q)q_i-(c-\theta_i)q_i$, a positive $\theta_i$ makes the manager behave like a profit-maximiser with lower cost $c-\theta_i$, i.e. more aggressive. The owner-optimal type is
$$\theta_i=\frac{(n-1)(A-c-\theta_j)}{2n},$$
so the $\theta$-setting game is not incentive compatible whenever $n>1$ (it cannot be that $\theta_i=0$ for all $i$). At the symmetric Nash equilibrium $\hat\theta=\frac{(n-1)(A-c)}{n+1}$; relative to all-profit-maximisers, output per firm is higher, price lower, and profits lower. The optimal $\theta$ replicates Stackelberg leadership, and $\hat\theta$ falls to zero as $n\to\infty$, so the deviation from profit maximisation vanishes as competition intensifies. If only firm 1 delegates while rivals maximise profit, it earns $(A-c)^2/4n$ — more than all $n-1$ rivals combined, however many there are. The model also rationalises **relative-performance** objectives $M_1=\pi_1-\frac{1}{n-1}\sum_{j\neq 1}\pi_j$ and an **entry-deterrence** variant where commitment to a non-profit objective deters a profit-maximising entrant for a non-trivial parameter range $A-c>3\sqrt{F}>(A-c)/\dots$.

## Contribution
The paper is a foundational statement of **strategic delegation**: it shows that the separation of ownership and control can benefit owners, undermines Friedman's (1953) "natural selection" defence of profit maximisation (since profit-maximisers need not earn maximum profits, selection might eliminate them), supplies a strategic rationale for relative-performance pay distinct from the informational one in tournament/agency theory, and reinterprets horizontal divisionalisation and vertical non-integration (with vertical restraints) as commitment devices. It links delegation formally to Stackelberg leadership and incentive compatibility.

## Limitations & open questions
- Results are illustrated only in a stylised linear-Cournot model; the author repeatedly stresses "nothing general follows" and the examples are "suggestive" rather than conclusive.
- The outcome function $z$ is taken as exogenously given by game-theoretic considerations; endogenising it (and handling multiplicity of equilibria) is left open.
- Commitment to the agent's type is assumed observable and credible ("common knowledge"); the robustness of strategic delegation to unobservable or renegotiable contracts is not addressed.
- Costs of employing different agent types are assumed equal; relaxing this is flagged.
- The precise sense in which incentive compatibility "almost always" fails is asserted but only loosely formalised here.

## Connections
The mechanism-design machinery is taken from d'Aspremont & Gérard-Varet (1980) on Stackelberg-solvable games and pre-play communication, and Dasgupta, Hammond & Maskin (1979). The conceptual origin is Schelling (1960) on commitment through delegation. The paper directly contests Friedman (1953) and Alchian (1950) on economic natural selection (cf. Winter 1964). On managerial incentives it relates to [[@Lazear1981|Lazear & Rosen (1981)]], Holmström (1982), and [[@Nalebuff1983|Nalebuff & Stiglitz (1983)]] on relative-performance schemes. The horizontal-merger result draws on Salant, Switzer & Reynolds (1983); the vertical-integration discussion engages Williamson (1971, 1975) and Mathewson & Winter (1983). The work is contemporaneous with, and complementary to, Yarrow's forthcoming treatment, and anticipates the later strategic-delegation models of Fershtman & Judd and Sklivas.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
