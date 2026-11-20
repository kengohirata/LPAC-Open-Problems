# Paired tails have a canonical ordinal orbit; the endpoint gap remains

2026-11-18. Status: **PROOF_RECONSTRUCTED**. Another research agent independently read the full proof and reconstructed the partition argument, limit recursion, endpoint criterion and its stated gap, finding no error. The same agent subsequently checked the binary finite-support refinement in §4.1. Not externally reviewed or formally verified. This is a new necessary-condition reduction for a hypothetical monic paired-tail witness, not its exclusion. It uses actual full-power maps, rather than an assumed extension of a proper countably complete filter.

Put Ω=ω, c=2^ω, and λ=c^+. Use the trimmed ordinal template R∈C from [the trimmed-template note](trimmed_ordinal_templates_bound_both_witness_sorts_2026-11-18.md):

    R_0=C([0,λ],Ω),
    R_1={r:[0,λ]→Ω : r is constant on some [β,λ]},
    p_R=inclusion,       q_R=d_λ^*.

At this λ its C-membership is ZFC. Let

    W=colim_(γ<λ) E([γ,λ)·R).

Its elements are row functions modulo equality on a tail; its binary Boolean algebra in sort i is P(λ×R_i) modulo the bounded-row ideal. Suppose

    j:E(Y)↪W,       Y∈C,

contains the paired seed. Write T=H(Y_0), s_a=H(p_Y)^−1(a), D(a)=s_a q_Y. Let h,k∈T represent the two seed characters. Thus j_0(h) is row evaluation at 0 and j_0(k) is row evaluation at t in row t. Denote the constant-row evaluation at β by e_β, in either sort as appropriate.

## 1. Tail targets preserve c-sized Boolean operations without M-membership

The [continuum-continuity theorem for M targets](continuum_boolean_continuity_and_orbit_separator_factorization_2026-11-18.md) does not directly apply to j: W is known to belong to H_fg, not to M. Nevertheless tail targets have the required c-continuity by a different argument.

**Lemma 1.** For arbitrary sets S,A, every M₂-map

    a:Ω^S→V_A,       V_A=colim_(γ<λ) Ω^([γ,λ)×A),

preserves Boolean joins and meets indexed by at most c elements. There is no M₁-action or fixed-point hypothesis.

**Proof.** The bounded-row ideal is closed under unions of fewer than λ sets. Therefore the binary Boolean algebra of V_A has all joins and meets of size at most c, computed by rowwise union and intersection of representatives. In particular the quotient maps from the full powers preserve these operations.

If q:S→I is a partition with |I|≤c, the composite Ω^I→Ω^S→V_A has a stage evaluation representation by the [small-power tail-lifting theorem](small_power_maps_into_tail_quotients_lift_to_a_stage_2026-11-18.md). Its Boolean part therefore preserves all joins on P(I), since |I|≤c and a stage evaluation is a pullback map.

For subsets U_ξ⊂S, ξ∈I with |I|≤c, put U=∪_ξ U_ξ. Disjointify the family, adding S\U as one further partition cell. Each cell inside U is contained in its corresponding U_ξ. The partition result shows that aχ_U is the join of the images of those cells. It is therefore below every upper bound of the aχ_(U_ξ), and it is plainly an upper bound itself. This proves join preservation; complements give meets. Empty and degenerate cases are immediate. ∎

In particular each j_i preserves all these joins and meets as operations in the *ambient* Boolean algebra of W_i, not merely in its own image.

## 2. Eventual limits of short families are respected

For a nonzero limit ordinal α<λ and functions f_β:S→Ω, β<α, the subset where the family is eventually constant is

    E = ∪_(n<ω) ∪_(γ<α) ∩_(γ≤β<α) [f_β=n].             (1)

Every operation displayed in (1) has at most c inputs. Thus Lemma 1 preserves this expression. If E=S, its eventual-value function f has fibres

    [f=n] = ∪_(γ<α) ∩_(γ≤β<α) [f_β=n].                (2)

Again these expressions are preserved. Consequently a(f) is represented by the pointwise eventual value of simultaneous row representatives of the a(f_β), whenever those representatives have such values on every point of a tail.

More generally, when a is monic and the row representatives are eventually constant along β at every row coordinate, (1) gives aχ_E=1 and hence E=S. Thus the existence of the source eventual limit can itself be reflected from these row representatives.

No λ-indexed join or meet is used here. The bound α<λ is essential.

## 3. Construction of the full orbit below λ

**Theorem 2.** There are uniquely recursively determined characters a_α∈T for all α≤λ such that

    a_0=h,
    a_(α+1)=D(a_α)                  (α<λ),
    a_δ(y)=eventual_(α<δ) a_α(y)    (0<δ≤λ limit),     (3)

and, for every α<λ,

    j_0(a_α)=e_α,
    j_1(s_(a_α))=e_α.                                  (4)

The map α↦a_α from [0,λ] to T with its pointwise topology is continuous. The characters a_α, α<λ, are pairwise distinct. Equation (4) is **not** asserted at λ.

**Proof below λ.** Start with h. Whenever j_0(a)=e_α, the unique balanced extension in W is the second-sort evaluation e_α, so j_1(s_a)=e_α. One can check uniqueness directly: synchronize the c balancing equations of a representative of j_1(s_a); on every sufficiently late row it is a character of R_1. Restriction along p_R is evaluation at α, and the bijection H(p_R) forces the character itself to be evaluation at α. Naturality for q then gives

    j_0(Da)=e_(α+1)       for α<λ.

Now let δ<λ be a nonzero limit and assume (3)–(4) below δ. Because |δ|≤c<λ, all the equalities j_0(a_α)=e_α, α<δ, can be represented simultaneously on one tail. For every g∈R_0, continuity of g at δ makes g(α), α<δ, eventually constant, with value g(δ). Apply §2 to the monic scalar map j_0. It follows that a_α(y), α<δ, is eventually constant for every y∈Y_0.

Define a_δ by this eventual value. It is M₁-equivariant: for any m and y, use the eventual-value equations at y and my and pass a_α(my)=m a_α(y) to the common tail of α. Thus a_δ∈T. Equation (2), together with the synchronized evaluation representatives, gives j_0(a_δ)=e_δ. The balanced-extension calculation again gives the second equation in (4). This completes the recursion below λ.

Every coordinate α↦a_α(y) is continuous on [0,λ): successors are isolated, and continuity at each limit was built into (3). Any continuous map [0,λ)→Ω is eventually constant because cf(λ)>ω. Indeed, otherwise choose an increasing sequence of points with successive values unequal. Its supremum is below λ, contradicting continuity there. Hence every coordinate has an eventual value at λ. Define a_λ by those values. The same equivariance argument shows a_λ∈T, and the resulting map on [0,λ] is continuous.

Finally e_α≠e_β for distinct α,β<λ, since continuous functions on the ordinal separate them. Equation (4) therefore makes the a_α distinct. ∎

This construction uses no witness-cardinality estimate, GCH, atomic-row lifting, or countably complete ultrafilter extension. It supplies one canonical continuous ordinal orbit directly from the actual monomorphism.

## 4. What would produce the missing endpoint character

For each z∈Y_1 consider its second-sort orbit profile

    b_z(α)=s_(a_α)(z),       α<λ.                       (5)

These profiles need not be continuous in α. Suppose, as an additional hypothesis, that every b_z is eventually constant. Then

    ℓ(z)=eventual_(α<λ) b_z(α)

defines an M₁-character ℓ:Y_1→Ω. On p_Y(Y_0) its value is a_λ, so C's unique-extension property forces

    ℓ=s_(a_λ).

For y∈Y_0, the successor identity gives

    ℓ(q_Y y)=eventual_(α<λ) a_(α+1)(y)=a_λ(y).

Consequently D(a_λ)=a_λ. Balanced row synchronization now shows

    j_0(a_λ)=e_λ,       j_1(s_(a_λ))=e_λ:               (6)

on a tail their common row evaluation point ξ satisfies d_λ(ξ)=ξ, and λ is the only fixed point of d_λ.

If one also proved k=a_λ, (6) would contradict the paired seed, since row evaluation at t and constant endpoint evaluation at λ are different germs. In row t the continuous function χ_(t,λ] distinguishes them.

Thus a concrete sufficient endpoint completion consists of two assertions:

1. Every profile (5) is eventually constant, producing the left-limit extension ℓ.
2. The moving seed character k equals the continuous limit a_λ.

Neither assertion is established here. C supplies uniqueness **once ℓ exists**; it does not prove that the profiles stabilize. Even existence of ℓ alone does not identify k with a_λ.

### 4.1 Stabilization is already decided on binary finite-support points

The first assertion is equivalent to eventual constancy of (5) only for the points z fixed by the finite-rank idempotent e_2 which fixes 0,1 and sends everything else to 0. Such points are finite-support.

Indeed, for arbitrary z∈Y_1 and n∈Ω, let δ_n:Ω→{0,1} be the indicator of {n}. Then δ_n z is fixed by e_2, and its profile is exactly the indicator [b_z(α)=n]. If all these binary profiles are eventually constant, either one is eventually 1, making b_z eventually n, or all are eventually 0. The latter case is impossible: the countably many stabilization bounds have supremum below λ, after which b_z would have none of its possible integer values. Thus b_z is eventually constant.

Consequently any failure to construct ℓ is already witnessed on the finite-support part of the second sort, even when the original witnessing point was non-finite-support. The stronger 2^c continuity restricted to non-finite-support points therefore cannot by itself remove this endpoint obstruction.

## 5. Why the existing partial-row model remains instructive

In the [two-block obstruction model](trimmed_partial_rows_recurrence_versus_unique_extensions_2026-11-18.md), the canonical orbit is evaluation along the first ordinal block, and a_λ is evaluation at the middle point. Every second-sort profile has an eventual value below that middle point. This gives the character ℓ, distinct from evaluation there, so the model fails C precisely at the use of uniqueness in §4.

An arbitrary actual monic witness has not yet been shown to enjoy that stabilization property. Its trimmed row functions stabilize only after row-dependent bounds, and recurrence by itself does not make those bounds yield eventual values of (5). Likewise, c-continuity is insufficient for the λ-long operation defining a_λ. The new non-finite-support 2^c-continuity theorem for M targets cannot simply be applied: W is still only known to lie in H_fg.

The contribution of this note is the canonical path (3)–(4) and the exact endpoint reduction in §4. A general paired monic-witness exclusion remains open.
