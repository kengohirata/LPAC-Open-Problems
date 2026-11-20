# Scalar stage bounds automatically become a common stage

2026-11-18. Status: direct proof, checked independently by two other research
agents; not externally reviewed or formally verified. No P4
counterexample is claimed.

This strengthens the stage-assembly argument in
[the countably generated template note](countably_generated_dual_templates_safe_retracts_2026-11-18.md).
The number of target generators is unnecessary once every scalar coordinate
map is represented by an actual stage evaluation.

## 1. A pair-coloring lemma

Let λ be an infinite regular cardinal and let `(a_α,b_α)`, α<λ, be pairs of
distinct elements of a set S. There is a binary function `f:S→2` for which

    {α<λ : f(a_α)≠f(b_α)}

is unbounded in λ.

Proof. Regard the unordered pairs as edges. If fewer than λ distinct edges
occur, one edge occurs on λ indices, by regularity; separate its endpoints.
Otherwise choose λ distinct occurring edges, giving a graph with λ edges.
Take a maximal matching. If it has λ edges, color the two endpoints of
each matched edge differently. If it has fewer than λ edges, their endpoints
form a vertex cover of size less than λ. Regularity then gives a vertex
incident with λ edges. Color that vertex 0 and all other vertices 1.
In each case λ distinct selected edges, hence λ indices, are separated. □

The conclusion concerns arbitrary colorings of S, not just equivariant
colorings. This is exactly why it can be applied to all elements of a full
power Ω^S.

## 2. Setting

Let `(T_α,r_βα)`, α≤β<λ, be an inverse system of nonempty sets with
surjective transition maps. Put

    K_λ = colim_(α<λ) Ω^(T_α),
    V_λ^R = colim_(α<λ) E(T_α·R).

All transitions in these colimits are monic. For each r∈R_i, evaluation
at r gives an M_2-map

    ρ_r : (V_λ^R)_i → K_λ.

The joint map `(V_λ^R)_i→K_λ^(R_i)` is monic: two elements have a common
stage, and coordinate equality in the monic scalar union implies equality
at that stage. No assertion that this joint map is surjective is needed.

Suppose θ:E(Y)→V_λ^R is a P-map and that, for each sort i and r∈R_i,
there are α_r<λ and a set map `τ_r:T_(α_r)→Y_i` such that

    ρ_r θ_i(F) = [F∘τ_r]       for every F:Y_i→Ω.       (1)

## 3. Common-stage theorem

**Theorem.** Under (1), θ factors through one stage by an actual dual map:

    θ = inclusion ∘ E(k),   k:T_α·R→Y in K,

for some α<λ.

Proof. First fix a sort i. Say that the scalar map indexed by r descends
to α if it is represented by a map T_α→Y_i. Suppose no α works for every
r. For each α choose r=r(α) whose map does not descend to α. Necessarily
α_r>α. Since r_(α_r,α) is surjective, failure of descent gives t,t'∈T_(α_r)
with

    r_(α_r,α)(t)=r_(α_r,α)(t'),
    a_α:=τ_r(t) ≠ τ_r(t')=:b_α.

For any F:Y_i→Ω, the element θ_i(F) belongs to one stage β_F<λ. If
α≥β_F, equality of the two representations of its r-coordinate implies

    F(a_α)=F(b_α).

Indeed, both expressions can be compared at stage α_r, because
α_r>α≥β_F; the two points t,t' have equal restrictions to β_F. The
monicity of the scalar stage inclusions makes that comparison pointwise.

The pair-coloring lemma produces a binary F violating this eventual
equality. Thus there is a common α for all r in this sort. Choose one
common upper stage for the two sorts and write the descended maps as
τ_r:T_α→Y_i.

Define `k_i(t,r)=τ_r(t)`. Naturality of θ for right M_1-actions implies

    F(k_i(t,mr)) = F(m k_i(t,r))

for every F:Y_i→Ω. Equality in the scalar union is pointwise equality
at stage α, and all such F separate points, so k_i is M_1-equivariant
in r. The same argument applied to the two structure arrows gives

    k_1(t,p_R r)=p_Y k_0(t,r),
    k_1(t,q_R r)=q_Y k_0(t,r).

Hence k is a K-map. Formula (1) and joint coordinate monicity then give
θ=inclusion∘E(k). Empty sorts cause no difficulty: (1) supplies the
necessary maps wherever a target coordinate exists. □

## 4. Consequences for the original ω_1 system

For the coinfinite-injection system T_α used in V, the existing ZFC scalar
lemma says that any M_2-map Ω^S→K factors as an actual stage evaluation
when |S|≤c. Therefore:

**Corollary (ZFC).** If both |Y_i|≤c, then every map E(Y)→V^R factors
through one stage by a dual K-map, for every template R. No bound on
the cardinality or number of M_1-generators of R is required.

More generally, a non-stage map E(Y)→V^R must have at least one scalar
coordinate which itself admits no stage evaluation representation.
Under N this is equivalent to failure of scalar stage factorization,
since every map between full powers is a coordinate evaluation map.

Thus the second prospective obstacle in
[the countable-partition criterion](scalar_nonstage_maps_countable_partition_criterion_2026-11-18.md)
is not independent: unbounded coordinate stages alone cannot assemble into
a map with values in V^R. The remaining issue is existence of a genuinely
non-stage scalar map from a power indexed by a set larger than c.

The theorem concerns these monic unions of powers. It does not apply to
tail quotients, whose stage maps are not monic, or to arbitrary objects
of M.

The later [saturated-ideal argument](nonstage_scalar_maps_require_inner_measurable_2026-11-18.md)
removes all source cardinal bounds under the stronger assumption that no
inner model has a measurable cardinal (in particular under V=L).
