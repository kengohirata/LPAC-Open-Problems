# Large injection unions: the generic inverse does not define a powerset map

2026-11-18. Status: PROOF_RECONSTRUCTED; no external or formal audit. This excludes a specific proposed non-stage scalar construction. It does not establish that all maps to a large injection union factor through a stage.

Let κ be an infinite cardinal and put λ=κ^+. For α<λ define

    T_α={t:α→κ : t is injective and |κ\im(t)|=κ}.

The complement condition must have cardinality κ. Merely requiring an infinite complement is insufficient for the restriction maps to be surjective when κ is uncountable.

Restriction T_β→T_α is surjective for α≤β<λ: split the unused κ-set into two κ-sets, use one for the at-most-κ many new arguments, and retain the other. Define

    V_κ=colim_(α<λ) ω^(T_α),
    B_κ=colim_(α<λ) P(T_α),

with injective transition maps given by precomposition. B_κ is the Boolean skeleton of V_κ.

## 1. Completeness and cardinal bounds

Every family of at most κ elements of B_κ lies in one stage, because λ is regular. Its stagewise union is its supremum in B_κ: any other proposed upper bound can be compared at a later common stage. Thus B_κ is κ-complete.

For each α<λ, |T_α|≤κ^κ=2^κ. An antichain in B_κ can be separated according to its least stage, and each stage contributes at most 2^κ disjoint nonzero subsets. Hence

    cell(B_κ)≤2^κ.

Also |B_κ|≤2^(2^κ). These larger bounds do not reproduce the original scalar argument with cellularity at most c.

## 2. A κ^+-long disjoint family

Fix r∈κ. For ξ<λ let e_ξ be the element represented at any stage α>ξ by

    {t∈T_α : t(ξ)=r}.

The elements e_ξ are nonzero and pairwise disjoint. Moreover their supremum in B_κ exists and equals 1.

Indeed, suppose b is an upper bound, represented at stage α. If t∈T_α lies outside b and already uses r, its unique argument ξ with t(ξ)=r is below α, contradicting e_ξ≤b. If t omits r, extend t at a later argument ξ≥α by assigning r there. The extension lies in e_ξ and still outside b, again a contradiction. Thus b=1.

This argument uses only a single new prescribed value and leaves κ unused values available.

## 3. Exactly which subfamilies have suprema

For A⊂λ, the supremum of {e_ξ:ξ∈A} exists in B_κ if and only if A is bounded or its complement is bounded.

If A is bounded, all events lie in one stage and their union is the required supremum.

If λ\A is bounded, let c be the bounded-stage union of the events for λ\A. Then 1−c is an upper bound for the A-events. If b is another upper bound, any nonzero portion of (1−c)\b can be examined at one stage containing the bounded complement. A point in that portion either already assigns r to an A-coordinate, a contradiction, or omits r and can be extended to assign it to a later A-coordinate, again a contradiction. Thus 1−c≤b.

Conversely suppose both A and λ\A are unbounded, and a supremum b exists at stage α. Every t∈T_α omitting r must belong to b: otherwise extend it at an argument ξ∈A above α with value r. Choose such a t and then ζ∈λ\A above α. Extend t so that t(ζ)=r. This extension still belongs to b. However 1−e_ζ is also an upper bound for all A-events, and the chosen extension does not belong to it. This contradicts minimality of b.

## 4. Consequence for the naive scalar map

The tempting prescription sends the singleton {ξ} of λ to e_ξ, interpreting ξ as the unique preimage of r under a generic injection. It cannot be the restriction of any Boolean homomorphism

    ψ:P(λ)→B_κ.

To see this, take A and its complement both unbounded. A hypothetical ψ(A) is an upper bound for every e_ξ with ξ∈A, and ψ(λ\A) is an upper bound for all complement events. At a common stage α representing these two complementary elements, a point t omitting r can be extended to assign r to an A-coordinate or to a complement-coordinate. The first extension forces t into ψ(A), while the second forces t into ψ(λ\A), contradicting disjointness.

This last argument does not presume that a Boolean homomorphism preserves an uncountable join. It uses only preservation of inclusions and complements. Therefore the failure already occurs before imposing the countable-completeness required for a map of the full-power M_2-sets.

For scalar maps ω^S→V_κ, the exact compatible-countable-partition formulation remains the one in [the scalar criterion](scalar_nonstage_maps_countable_partition_criterion_2026-11-18.md), with the stage index ω_1 replaced by κ^+. A successful construction must assign coherent values to every countable partition, including all binary partitions. The generic inverse family above does not do this.
