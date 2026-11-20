# The initial ordinal evaluation has no proper D-subobject hull

2026-11-18. Status: direct proof under N, checked by two other research
agents; not externally reviewed or formally verified.
No No.1 non-coreflectivity or cardinal lower-bound input is needed.

## 1. Statement

For an ordinal κ, use

    Y_κ=(C_κ --p=inclusion,q=d_κ^*--> B_κ),
    C_κ=Cont([0,κ],Ω_discrete),  B_κ=Ω^[0,κ],

and `j_0=E(ψ_0):X→E(Y_κ)`, where ψ_0:Y_κ→B evaluates at 0 in
sort 0. Assume N, so Y_κ∈C and E is fully faithful.

**Proposition.** Any D-subobject of E(Y_κ) containing the image of j_0
is the whole E(Y_κ).

Thus E(Y_κ) is the least D-subobject of itself containing this fixed
finitely generated seed. This is stronger than a lower bound on the size
of a possible D-subobject.

## 2. Dual reduction

Suppose a monomorphism E(Q)↪E(Y_κ), Q∈C, contains j_0. By fullness it
is E(v) for a K-map v:Y_κ→Q. Monicity of each power map implies that
each v_i is surjective: if a point of Q_i were missed, its singleton
indicator and zero would have the same pullback. The factorization of
j_0 gives a map Q→B whose composite with v is ψ_0.

Write H(A)=Hom_(M_1)(A,Ω), with the pointwise topology. For a
finite-support M_1-set A, H(A) is compact Hausdorff. Indeed, an
equivariant map must send each a to its finite support (or no map
exists), and the equivariance equations cut out a closed subset of the
resulting product of finite discrete sets.

Use the established identifications

    H(C_κ)≅[0,κ] as compact spaces,
    H(B_κ)≅[0,κ] as sets,

where both identifications send a point to its evaluation functional.
The second uses N. Under them H(p_κ) is the identity and H(q_κ) is d_κ.

## 3. The image on points is all of the ordinal interval

The continuous injection

    H(v_0):H(Q_0)→H(C_κ)≅[0,κ]

has closed image S, since Q_0 is finite-support and H(Q_0) is compact.
The factorization of ψ_0 implies 0∈S.

Moreover S is d_κ-stable. If x∈S is represented by h∈H(Q_0), choose
the unique h_1∈H(Q_1) satisfying h_1 p_Q=h, using Q∈C. Commutativity
with p gives

    h_1 v_1 = ev_x on B_κ.

Commutativity with q then gives

    (h_1 q_Q) v_0 = ev_x q_κ = ev_(d_κ x).

Thus d_κ x∈S.

A closed subset of [0,κ] containing 0 and closed under d_κ is all of
[0,κ]. Transfinite induction gives successor points; at a nonzero limit
δ the preceding points converge to δ in the ordinal topology. Hence
H(v_0) is surjective.

## 4. The quotient maps are isomorphisms

If v_0(f)=v_0(g), evaluate through all h∈H(Q_0). Since H(v_0) contains
every evaluation at x∈[0,κ], one obtains f(x)=g(x) for every x, so
f=g. Therefore v_0 is injective, and already surjective.

The p-square and the bijectivity of H(p_Q), H(p_κ) imply that H(v_1)
is surjective as well. The evaluations separate the functions in B_κ,
so the same argument makes v_1 injective. It too was already
surjective. Hence v is a K-isomorphism, proving the proposition. □

## 5. A sharper test for M-equalizer failure

Let W∈M, and suppose a,b:E(Y_κ)⇉W are distinct but satisfy

    a j_0=b j_0.

Then their equalizer L cannot belong to M. Otherwise the fg map X→L
would factor through a monic D-subobject of L. Its composite into
E(Y_κ) would be a D-subobject containing j_0, hence the whole object
by the proposition. This would force a=b, a contradiction.

Consequently, in
[the Y_(ω_1) non-stage reduction](yomega1_template_standard_maps_and_nonstage_reduction_2026-11-18.md),
one genuine non-stage map θ:E(Y_κ)→V^(Y_(ω_1)) would already give an
actual failure of M-equalizer closure, by comparison with θ_std.
There is no additional obligation to exclude a smaller D-witness in
that equalizer. Existence of such a non-stage map remains unproved;
under no inner model with a measurable cardinal it is excluded by
[the scalar theorem](nonstage_scalar_maps_require_inner_measurable_2026-11-18.md).

This is a test for rejecting the current M candidate if such maps
exist. It is not itself a P4 counterexample.
