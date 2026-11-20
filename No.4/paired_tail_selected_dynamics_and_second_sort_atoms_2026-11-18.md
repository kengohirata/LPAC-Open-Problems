# Selected-character dynamics and second-sort atoms for paired ordinal tails

2026-11-18. Status: **PROOF_RECONSTRUCTED**, awaiting independent audit. This strengthens [the atomic spectral-extension reduction](paired_tail_atomic_rows_have_spectral_extensions_2026-11-18.md). It remains a necessary-condition reduction for a hypothetical nonlifting monic witness, not an exclusion of that witness.

Assume N, regular λ>c, R=Y_λ, and a hypothetical monomorphism j:E(Y)→W containing the paired seed, where Y∈C and |Y₀|≤λ. Write

    T=H₁(Y₀),   s_a=H₁(p_Y)^{-1}(a),
    D(a)=H₁(q_Y)(s_a)             (a∈T).

Thus D is a set selfmap of the compact space T. Let h,k∈T be the characters representing the two seed maps.

## 1. A simultaneous first- and second-sort reduction

Choose any M₁-subset B⊂Y₁ of size at most λ containing p_Y(Y₀)∪q_Y(Y₀). The following reduction is possible for this chosen B. In particular, B may include any preassigned set of at most λ further second-sort points and their orbits.

There are partial K-subdiagrams D_t⊂R and K-maps

    q_t:D_t→Y

whose images lie in Y₀ and B, respectively. Every point of Y₀ and every point of B occurs in the corresponding q_t-image on unboundedly many rows.

At each t there is a selected set H_t⊂T of size <λ, containing h,k and closed under D, and a function

    ξ_t:H_t→[0,λ]

satisfying

    ξ_t(Da)=d_λ(ξ_t(a)),
    ξ_t(h)=0,      ξ_t(k)=t.                         (1)

For all a∈H_t, one has the simultaneous pointwise identities

    a(q_(t,0)(g))=g(ξ_t(a))         (g∈(D_t)₀),
    s_a(q_(t,1)(r))=r(ξ_t(a))       (r∈(D_t)₁).      (2)

The H_t arise from a continuous increasing chain, so every member of the union of the selected chain belongs to all sufficiently late H_t. This union need not be all of T.

## 2. Choice of the parameter chains

Refine the continuous chain A_α⊂Y₀ from the previous note, and choose a continuous chain B_α⊂B, each of size <λ, with union B and

    p_Y(A_α)∪q_Y(A_α)⊂B_α.

Both chains can consist of M₁-subsets since |M₁|<λ. Choose H_α⊂T so that it realizes every finite pattern actually attained by the paired observations

    a|_(A_α),     s_a|_(B_α)       (a∈T),

and close it under all finite iterations of D. Include h and k from the beginning. Finitely many observed values have countably many possible patterns, and there are fewer than λ finite parameter sets at each stage. Hence |H_α|<λ remains possible. At a limit take unions: all relevant finite patterns and all D-closure equations appeared earlier.

For each selected a, the images j₀(a) and j₁(s_a) are balanced. Their c many action equations can be synchronized on a tail. A balanced row in sort 0 is an evaluation on the compact ordinal by the compact evaluation lemma. A balanced row in sort 1 is an evaluation on the same underlying ordinal by N. Naturality for p identifies their evaluation points. Naturality for q then gives

    ξ_t(Da)=d_λ(ξ_t(a)).

The representatives of j₀(h) and j₀(k) are the prescribed evaluations at 0 and t, respectively, giving the other two equations in (1). These are actual single-valued evaluations for selected characters, stronger than invariance of an arbitrary set-valued relation.

Choose binary row representatives for singleton indicators of all y∈Y₀ and z∈B. In addition to same-sort disjointness, action, and comparison equations, synchronize the implications

    χ_y≤χ_(p_Yy)∘p_Y,      χ_y≤χ_(q_Yy)∘q_Y.

After dualization these say that a first-sort atomic row point labelled y is sent by p_R and q_R to second-sort atomic row points labelled p_Yy and q_Yy. The continuous schedule from the preceding note handles fewer than λ equations at each stage and gives the asserted partial K-subdiagrams and recurrence. Equations (2) are the synchronized atom/character comparisons.

## 3. Arbitrary characters: a precise ultrafilter formulation

Fix a row t and any a∈T, which need not be selected. Consider the family of subsets of [0,λ]

    {ξ:g(ξ)=a(q_(t,0)(g))}           (g∈(D_t)₀),
    {ξ:r(ξ)=s_a(q_(t,1)(r))}         (r∈(D_t)₁).     (3)

This family has the finite intersection property. Any finite list involves finitely many labels in A_α and B_α at the scheduled stage. Some selected b realizes the same mixed finite pattern, and the point ξ_t(b) simultaneously satisfies the list by (2).

Consequently there is an ultrafilter U_(t,a) on [0,λ] containing all the sets (3). Its limit point in the compact ordinal satisfies all the first-sort equations, because those fibres are closed. The second-sort functions are arbitrary functions; their fibres need not be closed, and their prescribed values need not agree with evaluation at the limit point.

If this ultrafilter can be chosen countably complete, N makes it principal, and its point simultaneously satisfies both sorts of equations. No countable-completeness assertion has been established. The finite intersection property alone is insufficient, even though all the selected characters have principal realizations.

This isolates the issue precisely: the compact first-sort extension is already available, while arbitrary-character extension through the second sort requires more than finite-pattern realization. Adding p_Y(Y₀) and q_Y(Y₀) to the atomic schedule is permitted, but does not by itself make the second-sort fibres closed or produce a countably complete ultrafilter.

## 4. Exact relational dynamics alone would still be insufficient

There is a useful boundary example, distinct from the stronger single-valued condition (1). Take Y=R=Y_λ, with T=[0,λ], D=d_λ, h=ev₀ and k=ev_λ. Inside R let D_t be the copy of Y_t whose functions are extended constantly after t, and let q_t:D_t→Y be inclusion.

These are actual C-subdiagrams and K-maps: the retraction min(-,t):[0,λ]→[0,t] commutes with the two successor maps. Every first-sort point, and every point of p_Y(Y₀)∪q_Y(Y₀), occurs for all sufficiently large t. The spectral relation is

    L_t={(η,ξ):min(η,t)=min(ξ,t)}.

It is compact, surjects onto T, is exactly stable under (D,d_λ), and contains (h,0) and (k,t). Nevertheless these properties give no contradiction. A transfinite orbit can end at k=ev_λ, while L_t identifies t with λ. Thus replacing maps by invariant compact relations loses a distinction needed by the original stage proof.

This example does NOT satisfy (1): k is D-fixed, whereas ξ_t(k)=t<λ is not d_λ-fixed. It is therefore excluded by selected-character synchronization. It shows only that the compact relations and recurrence, even with exact relational dynamics and the indicated second-sort recurrence, cannot substitute for that stronger information.

## 5. Remaining tasks

The present reduction preserves successor equations exactly on a growing D-closed family of characters, and preserves all finite mixed first-/second-sort patterns for arbitrary characters. It still does not extend the single-valued maps ξ_t to all of T with enough continuity to run the full transfinite-orbit argument.

There are two concrete missing implications: control the ultrafilters in §3 strongly enough to obtain actual simultaneous evaluations for arbitrary characters, or exploit (1), (2), compactness, and recurrence without such a global choice. Neither implication is asserted here. In particular, the construction of the partial diagrams does not prove that D_t∈C; their notation denotes subdiagrams, not membership in the dual-image class.

## 6. A stronger first-sort model, and the one atom that rejects its naive completion

The following model was proposed by the coordinating agent and checked directly here. Put κ=λ·2 and take Y=Y_κ, so T=[0,κ], h=ev₀, and k=ev_λ. Define a continuous surjection π_t:[0,κ]→[0,λ] by

    π_t(α)=min(α,t)       for α<λ,
    π_t(λ+β)=t+β         for β≤λ.

Here t+λ=λ. The two definitions fit continuously at λ, and the second branch continuously covers [t,λ]. Every continuous y:[0,κ]→ω factors through π_t for all sufficiently large t: continuity at λ makes y constant on [t,λ], the only nontrivial fibre of π_t. Thus the row maps

    q_(t,0):R₀→Y₀,       g↦g∘π_t

give an actual full-power first-sort monomorphism into the tail quotient, since every point of Y₀ appears eventually in their images.

The maps π_t commute with successor at every α<t in the first block and at every point of the second block. Hence every fixed character eventually has the desired successor equation; any selected first-block set bounded below t satisfies it simultaneously. The marks also have the required values π_t(0)=0 and π_t(λ)=t. This proves that full first-sort rows, recurrence, and eventual selected-character dynamics still do not by themselves yield a contradiction.

Nevertheless the naive second-sort completion q_(t,1)(r)=r∘π_t fails one fixed atomic test. Let

    b=χ_[λ,κ]∈Y₁,
    F=χ_{b}:Y₁→ω,
    g_t=χ_(t,λ]∈R₀.

Direct calculation gives

    (g_t∘d_λ)∘π_t = χ_[t,κ] ≠ b,
    (g_t∘π_t)∘d_κ = b.

Thus F evaluates the two sides of the second structure square as 0 and 1 on every row. This is a genuine failure in the tail quotient, not just lack of a common stage for the balanced-character equations.

Moreover b belongs to q_Y(Y₀): it is d_κ* applied to the continuous function χ_(λ,κ]. It never factors through π_t, because b distinguishes source points within the collapsed fibre [t,λ]. Consequently the naive second-sort maps send its singleton indicator to zero. The atom recurrence required already on q_Y(Y₀) excludes this completion.

This example validates the stronger second-sort atomic constraints in §§1–3: they see a failure invisible to all the individual balanced-character successor equations. It does not show that every alternative nonlifting completion has the same defect.

## 7. A first-sort stage controls all structure collisions

There is another conditional reduction. Suppose j₀ has a stage representation by genuine equivariant row maps q_(t,0):R₀→Y₀ on a common tail. Put

    S=p_R(R₀)∪q_R(R₀)⊂R₁,
    R_S=(R₀ --p_R,q_R--> S).

After increasing the common tail, the prescriptions

    q_(t,1)(p_Rg)=p_Y(q_(t,0)(g)),
    q_(t,1)(q_Rg)=q_Y(q_(t,0)(g))

are well defined and give a K-map R_S→Y on every row. To see well-definedness, suppose collisions with different prescribed labels occur on unboundedly many rows. Choose one pair of unequal labels on each such row. The [pair-colouring lemma](coordinate_stage_uniformization_by_pair_coloring_2026-11-18.md) supplies one binary function F:Y₁→2 separating the selected labels on unboundedly many rows. Naturality for j, together with the genuine first-sort stage representation applied to F∘p_Y and F∘q_Y, says that the two labels have the same F-value on every sufficiently late collision. This is a contradiction. The same argument covers same-arrow as well as mixed-arrow collisions.

Equivariance of the resulting q_(t,1) follows from equivariance of q_(t,0) and of the structure arrows. For every F:Y₁→ω, the restriction of j₁(F) to S agrees as a germ with F∘q_(t,1). Thus restricting the hypothetical map to these structural rows really gives a stage-induced partial diagram map. No uniform equality bound for all F is assumed; equality of the resulting maps into the tail quotient is elementwise.

This does not recover a row map on all of R₁. Indeed R_S is not a C-object for the ordinal template when there is a nonzero limit β<λ. Besides ordinary evaluation at β, there is an equivariant map S→ω which sends

    p_R(g) ↦ g(β),       q_R(g) ↦ g(β).

The second prescription is well defined: two continuous g with the same g∘d_λ agree away from 0, since successor points are dense there, and β>0. On an overlap where g∘d_λ is continuous, continuity at β forces g(β+1)=g(β), so the two prescriptions agree. This gives a second extension of evaluation at β on R₀. It differs from ordinary evaluation on q_R(χ_(β,λ]), where their values are 0 and 1.

These are explicit limit-stalling extensions of H₁(p_(R_S)). The structural-row restriction therefore loses precisely a uniqueness condition that the full, non-finite-support second sort of R supplies. Its failure cannot be repaired by treating R_S as a C-template.
