# Non-stage scalar maps require an inner model with a measurable cardinal

2026-11-18. Status: proof reconstructed and checked by a second research
agent, including an independent check of the cited primary source;
not externally reviewed or formally verified.
This is a conditional exclusion theorem for the V-template investigation,
not a P4 counterexample or a general M-equalizer theorem.

## 1. Assumption and statement

Write IM for the assertion that there is an inner model with an uncountable
measurable cardinal. The hypothesis ¬IM is stronger than the standing N
(no uncountable measurable cardinal in the universe). In particular V=L
implies ¬IM. We do not replace N by ¬IM without saying so.

Use the original coinfinite-injection system T_α, α<ω_1, and

    K = colim_(α<ω_1) Ω^(T_α),       Ω=ω, c=2^ℵ0.

**Theorem.** Under ¬IM, for every set S, every M_2-map
`φ:Ω^S→K` is a stage evaluation: there are α<ω_1 and τ:T_α→S such that

    φ(f) = [f∘τ]                 for all f:S→Ω.

Equivalently, the existence of a scalar map with no stage evaluation
representation implies IM. The theorem uses a published saturated-ideal
result in addition to the direct arguments below.

## 2. Boolean image and its cellularity

Let B be the Boolean part of K. It is the union of the Boolean algebras
P(T_α), with injective pullback transitions. Finitary tuple coding implies
that φ induces a Boolean homomorphism

    ψ:P(S)→B,       ψ(A)=φ(χ_A).

This is the same finite-operation argument as in the
[scalar lemma](v_codomain_equalizers_root_compression_2026-11-17.md), §4.2.
Let I be its kernel ideal.

Every antichain of nonzero elements of B has cardinality at most c.
Indeed assign each member to a stage in which it occurs. At a fixed
stage its representatives form disjoint nonempty subsets of T_α, so
there are at most |T_α|≤c of them. There are ω_1≤c stages.
Consequently P(S)/I, which embeds in B, also has cellularity at most c.

## 3. The kernel is c^+-complete

Let q:S→Q be any quotient partition with |Q|≤c. Precomposition gives
an M_2-map `q*:Ω^Q→Ω^S`. The already proved ZFC scalar lemma applies
to φq*, so this composite is evaluation by a function T_α→Q at one
stage.

It follows that ψ on the partition algebra q^*P(Q) preserves all joins:
pullback preserves unions in P(T_α), and those are also their joins in B.
For the latter assertion, any proposed upper bound in B can be compared
at a common higher stage, where pointwise union is still the least upper
bound.

Now take at most c members A_ξ of I. Disjointify them and add their
complement, obtaining a partition with at most c blocks. Every block
inside their union has ψ-image 0. The preceding paragraph shows that
the union also has ψ-image 0. Thus I is closed under unions of at most
c sets, i.e. I is c^+-complete.

Only the small-index scalar theorem is used here; no large-index
factorization has been assumed.

## 4. A nonprincipal remainder produces a saturated ideal

Put

    S_0={s∈S : ψ({s})≠0},       R=S\S_0.

The singleton images form an antichain, so |S_0|≤c. Suppose ψ(R)≠0.
Every singleton of R belongs to I. Hence there is a family of I-small
subsets of R whose union is I-positive.

Let κ be the least cardinality of such a family, say (A_ξ)_(ξ<κ),
and write A=∪_ξ A_ξ. Then κ≥c^+ and unions of fewer than κ I-small
subsets of R remain I-small. Disjointify the A_ξ to a partition
(D_ξ)_(ξ<κ) of A (empty blocks are allowed). Define an ideal on κ by

    J={U⊆κ : ∪_(ξ∈U) D_ξ ∈ I}.

Then J is proper, κ-complete, and contains every singleton. The
Boolean algebra P(κ)/J embeds in the relative algebra (P(S)/I)↾[A].
Thus it has cellularity at most c<κ, and in particular J is
κ^+-saturated. Minimality also makes κ regular: a shorter cofinal
grouping of the family would contradict its minimality.

We now use the published theorem that a proper κ-complete,
κ^+-saturated ideal on an uncountable κ containing all singletons
implies that κ is measurable in an inner model. Therefore ψ(R)≠0
implies IM.

For the exact source, Kanamori–Shelah, *Complete Quotient Boolean
Algebras*, §1, p.2, records this theorem of Kunen immediately after
Lemma 1.1. The definition of an ideal over κ, including completeness
and the singleton condition, is on p.1:

- [Author/arXiv version](https://arxiv.org/pdf/math/9401212).
- [Shelah's paper archive](https://shelah.logic.at/files/198174/390.pdf).

The present proof does not need to infer completeness of P(S)/I or
apply the more restrictive Theorem A of that paper.

## 5. Reduction to a small set and conclusion

Under ¬IM, §4 gives ψ(R)=0, hence ψ(S_0)=1. In particular S_0 is
nonempty whenever φ exists. If f,g:S→Ω agree on S_0, then

    ψ({s:f(s)=g(s)})=1.

Preservation of finite tuple coding and the equality-test operation
therefore gives φ(f)=φ(g). Equivalently, this is the component-kernel
filter criterion from
[the kernel note](mono_factorization_kernel_filters_2026-11-18.md).

Choose s_*∈S_0 and extend each h:S_0→Ω to S by giving every point
outside S_0 the value h(s_*). This extension is M_2-equivariant.
The preceding paragraph shows that φ factors through restriction
Ω^S→Ω^(S_0). Since |S_0|≤c, the original ZFC scalar lemma now gives
a stage evaluation on S_0, and hence on S. This proves the theorem. □

## 6. All templates are protected under ¬IM

Combine the theorem with
[coordinate stage uniformization](coordinate_stage_uniformization_by_pair_coloring_2026-11-18.md).
For every R,Y∈K, every P-map

    E(Y)→V^R=colim_(α<ω_1) E(T_α·R)

factors through one stage by a K-map T_α·R→Y. Neither R nor Y needs
to satisfy a cardinal bound. The stage maps are actual dual maps.

In particular, for R∈C and Z∈M, every equalizer of two arrows
`Z⇉V^R` lies in M under ¬IM. For an fg map into the equalizer,
first take its monic D-witness inside Z. The two restricted arrows
from that witness lift to a common stage. Their equalizer is the
dual of a C-coequalizer, and is a monic D-subobject containing the
chosen fg map.

The same argument applies when the codomain embeds in an arbitrary
set-indexed product of such V^R: use a separate stage in each
coordinate, then the product of those D-stages, which is again in D.

Thus under V=L there is no non-stage map in the entire fixed-template
V^R family, even with arbitrarily large dual templates. Under N alone,
the theorem does not eliminate such maps: N does not exclude measurable
cardinals in inner models. No conclusion about arbitrary codomains in
M is made here.
