# Trimmed ordinal templates bound both witness sorts

2026-11-18. Status: **PROOF_RECONSTRUCTED**. The coordinating agent proposed this refinement; its membership, cardinal calculations, and transfer of the stage obstruction were independently checked here. No general nonlifting-witness exclusion is claimed.

Let λ be a regular uncountable cardinal and X=[0,λ]. Define

    R₀=C(X,ω),
    R₁={r:X→ω : ∃β<λ, r(ξ)=r(λ) for every β≤ξ≤λ}.

Use postcomposition actions, p the inclusion, and q=d_λ* the successor precomposition. Thus R₁ contains arbitrary behaviour on a bounded initial interval, but the eventual value below λ must agree with the endpoint value.

## 1. Membership in C

The two arrows land in R₁. Every continuous discrete-valued function is eventually constant at the endpoint, and successor precomposition preserves eventual endpoint constancy. R₀ is finite-support.

Under N, every equivariant functional φ:R₁→ω is evaluation at a point of X. Here is a direct proof. The binary functions in R₁ correspond to the Boolean algebra consisting of bounded subsets of λ and their complements in X. Finite tuple coding and the usual range argument produce an ultrafilter U_φ on this algebra, and the fibre at φ(r) belongs to it for every r∈R₁.

If U_φ contains a bounded A⊂λ, its restriction to P(A) is countably complete. Indeed, every countable partition of A extends to an ω-valued function on X which is constant outside A and therefore lies in R₁. The selected-fibre property selects one cell; the usual first-failure partition proves countable completeness. Under N this restricted ultrafilter is principal, at some ξ∈A, and then φ(r)=r(ξ) for every r.

If U_φ contains no bounded subset, it selects exactly the subsets containing an endpoint tail. For every r the fibre at r(λ) contains such a tail, so φ(r)=r(λ).

These evaluations are distinct, and restriction along p identifies them with the compact-space evaluations on R₀. Hence H₁(p) is bijective and R∈C.

For λ=c⁺ the same conclusion is ZFC, without N. Each bounded A has size at most c. A countably complete ultrafilter on a set of size at most c is principal: choose a countable binary separating family, take the selected side of each coordinate, and intersect; countable completeness yields a nonempty set with at most one point. Thus the only use of N in the preceding proof is unnecessary at this λ.

Equivalently, R is the ambient union of the ordinal templates Y_β, β<λ, embedded by extension constantly beyond β. The clipping maps min(-,β) commute with successor. Both sorts are precisely the corresponding unions. This also proves membership whenever the smaller ordinal templates belong to C, by C's colimit closure.

## 2. Cardinalities and the new witness bound

The continuous first-sort functions have finite image and clopen fibres; compactness makes each such fibre a finite union of ordinal intervals. Hence |R₀|=λ. The second sort satisfies

    |R₁|≤λ·2^{<λ}.

Under 2^{<λ}=λ, in particular under GCH, both carriers have size λ. Therefore both sorts of the associated tail quotient

    W=colim_(β<λ) E([β,λ)·R)

have size at most 2^λ.

If GCH holds and j:E(Y)↪W is monic, then both |Y_i|≤λ: otherwise 2^{|Y_i|}>2^λ contradicts injectivity. This improves the original full-power ordinal template, whose second carrier had size 2^λ and allowed a larger bound on the second sort of a witness.

For λ>c and R∈C, W belongs to H_fg by the existing sufficiently-filtered-colimit theorem. These cardinal bounds do not by themselves show that W belongs to, or lies outside, M.

## 3. The paired stage obstruction survives

The row maps R→B at 0 and t still define the paired finitely generated seed X⊔X→W. The [stage-induced monic-witness obstruction](paired_ordinal_tail_stage_monic_obstruction_2026-11-18.md) carries over without change: its proof uses only

- R₀=C([0,λ]) and its compact spectrum;
- H₁(R₁)=[0,λ] by evaluation;
- the fact that q induces successor;
- recurrence of every first-sort source point under a monic stage-induced map.

All four properties hold for the trimmed template. Thus a paired monic C-witness, if one exists, must still be genuinely non-stage.

The [small-power tail-lifting theorem](small_power_maps_into_tail_quotients_lift_to_a_stage_2026-11-18.md) additionally excludes all witnesses with both carriers at most c, and bounded epi-compression excludes all both-finite-support witnesses.

## 4. Full atomic recurrence can now be retained

Under the cardinal bound in §2, the chosen set B in the [sparse-block countable-filter construction](paired_tail_sparse_blocks_give_countably_complete_filters_2026-11-18.md) may be all of Y₁. For λ=c⁺, this construction requires no further cardinal arithmetic beyond the bound on the hypothetical witness itself.

Thus one can retain sparse blocks on which the partial K-rows recur at every point of both source sorts, while every arbitrary-character mixed fibre family has the countable intersection property and generates a proper countably complete filter.

In this case restriction to the retained row set preserves monicity of the entire j. If F≠G in a source sort, choose y with F(y)≠G(y). The singleton of y is supported on unboundedly many retained rows. Its inequality χ_y≤[F≠G] holds under j on a tail; a later retained positive row therefore distinguishes the restricted images of F and G. This is stronger than retaining recurrence only on the structural second-sort subset.

It still does not show that those filters have countably complete ultrafilter extensions, or that the partial rows become total K-rows.

## 5. What trimming removes, and what it does not

The endpoint-wrong element χ_[0,λ), used in the previous endpoint-correction partial-row obstruction, is absent from the trimmed R₁. Thus that exact obstruction cannot simply be reused at the top endpoint. Interior discontinuities and partial-row phenomena remain possible, however, since bounded initial intervals are unrestricted.

A proposed partial-row model using q₀(g)=g∘min(-,t) and replacing a second-sort tail by the eventual value below t does have countable intersection compatibility and can recur at all trimmed source points. But with target Y=R its seed k=ev_λ is D-fixed, while the required row value is t<λ. It therefore violates the selected-character equation ξ_t(Dk)=d_λξ_t(k), which an actual j supplies. Such a model illustrates insufficiency of bare recurrence and countable filters, but does not survive the full current reduction.

The remaining prospective witness must simultaneously satisfy C's unique character extension, exact selected-character dynamics, both-sort atomic recurrence, and all full-power map relations. No construction or contradiction satisfying all of these has yet been established.
