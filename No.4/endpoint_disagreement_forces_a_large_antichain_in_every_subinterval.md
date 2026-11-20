# Endpoint disagreement forces large antichains below the difference

Let `c=2^aleph_0`, `λ=c^+`, `S=Cont([0,λ],ω)`, and let `u_β(g)=g(β)`. Use the ordinal object Y with first carrier S and second carrier all functions. For a target Z in M, write B for the Boolean algebra of binary elements of its first sort. All results below use ZFC. This argument was checked directly, without a separate independent audit.

**Claim.** Let a,b:E(Y)⇉Z agree on the initial evaluation. If their images of the endpoint evaluation differ, there is a nonzero w below that difference such that **every nonzero Boolean element below w contains λ pairwise disjoint nonzero elements**. In fact one of the two first-sort maps induces, below w, a Boolean homomorphism out of P(λ) that preserves joins of at most c elements and kills all bounded subsets.

Thus the endpoint agrees whenever every nonzero element of B has a nonzero subelement whose Boolean interval has no antichain of size λ. This includes atomic B of arbitrary size and every B with the λ-chain condition. It constrains only the first sort of Z.

## Proof

By the successor and short-limit arguments in [ordinal rigidity](ordinal_sources_through_continuum_are_m_rigid_2026-11-18.md), a and b agree on u_β for each β<λ. At this point the argument only needs the two first-sort maps and those agreements. The [continuum continuity theorem](continuum_boolean_continuity_and_orbit_separator_factorization_2026-11-18.md) applies because S has no fixed points.

For g∈S let r(g) be the least η<λ such that g is constant on [η,λ]. It exists by continuity at the endpoint. Put C_η={g:r(g)≤η}. For brevity write a(A), b(A) for the binary images of indicators. Let v=[a(u_λ)≠b(u_λ)]. If v≠0, finite pointwise operations give

    v ∧ a(C_η) ∧ b(C_η) = 0     for every η<λ.

Indeed on C_η the evaluations at η and λ agree, and the two images at η are equal. If v∧a(C_η)=0 for every η, take w=v and θ=a. Otherwise choose η with w=v∧a(C_η)≠0 and take θ=b. For any γ, the displayed identity at max(η,γ) gives w∧b(C_γ)=0. Thus a single choice θ works simultaneously for all bounds.

For arbitrary 0<d≤w define

    Φ_d(A)=d ∧ θ(r^{-1}(A))       (A⊂λ).

This is a Boolean homomorphism with interval unit d. Its ambient joins of at most c images are preserved. Meeting an existing Boolean supremum with d preserves that supremum in the interval, by the Boolean upper-bound property. Φ_d kills every bounded subset of λ. No equivariance of r is needed, since θ is defined on indicators of all subsets of S.

For each t<λ choose an injection i_t:t→c. Set

    A_(α,j)={t>α:i_t(α)=j},       α<λ, j<c.

For fixed α these c sets partition a final segment, so their images have join d. Choose j(α) with Φ_d(A_(α,j(α)))≠0. Since λ=c^+ is regular, the same j occurs for λ distinct α. The corresponding sets are pairwise disjoint by injectivity of i_t. Their images are the required antichain below d. This proves the claim, including its assertion for every nonzero subinterval. The matrix argument is also used for a different target obstruction in [the scalar cogeneration note](monic_local_tail_object_not_cogenerated_by_v_templates_2026-11-18.md).

## First-sort example and its failure in the second sort

The first-sort assumptions alone allow endpoint disagreement, even when the target sort is taken from an actual M-object. Put T=ω² with the coordinatewise action and use the diagonal tail target U on λ rows with template (T,id,id,T). This target belongs to M_bfs by the recurring finite-row-type argument in [the diagonal example](common_character_locus_need_not_be_closed_in_large_spectra_2026-11-18.md).

For t<λ and (x,y)∈T define two continuous functions on [0,λ]:

    s_t(x,y)(ξ)=x for all ξ;
    h_t(x,y)(ξ)=x for ξ≤t, and y for ξ>t.

Both families commute with postcomposition on their source points. Pullback row by row, followed by the quotient modulo bounded rows, gives bi-equivariant maps a_0,b_0:ω^S⇉U_0. On each fixed u_β, β<λ, the two representatives agree on all rows t≥β. On u_λ the two representatives are respectively the first and second projections at every row. They are distinct.

The first map extends to a diagram map by the same constant functions in the second carrier. The second map **cannot** extend with this diagonal target. Let F be the indicator of the subset of continuous functions in the full second carrier. Then F∘p_Y=1. On each nonzero limit row t and (x,y) with x≠y, the function h_t(x,y)∘d_λ is discontinuous at t, since its value there is y and its values immediately below t are x. Thus b_0(F∘q_Y) differs from 1 on unboundedly many rows, whereas b_0(F∘p_Y)=1. The two target structure maps are identical, so naturality would force these two images to be equal.

This shows that the Boolean obstruction derived above can occur in the first sort of an actual M-target. The following stronger test uses both structural arrows.

## A large antichain must occur in the kernel of the structural map

Write B_i for the binary Boolean algebra of Z_i. Let p_Z,q_Z:B_1→B_0 be the two structural homomorphisms. If the endpoint images differ, there must be λ pairwise disjoint elements x_i of B_1 with

    p_Z(x_i)=0,       q_Z(x_i)≠0.

In particular the endpoint agrees if ker(p_Z) has no antichain of size λ, regardless of the cellularity of B_0. This strengthens the endpoint consequence of the known result for monic p_Z. It asks only about the zero fiber on binary elements.

**Proof.** Write Dg=g∘d_λ, acting on the full second carrier. For n≥0 let L_n be the continuous functions g for which g,Dg,...,D^n g are continuous but D^(n+1)g is discontinuous. If none of these failures occurs, g is constant on [ω,λ], hence r(g)≤ω. For a direct verification, continuity at ω gives eventual constancy below ω. If g first departs from g(ω) above ω, this first departure is a successor ξ=δ+k, with δ≥ω a limit and k a positive integer. D^k g agrees with g(ω) on a final segment below δ and has a different value at δ. This contradicts the assumed continuity. See also [the continuous dynamical factor calculation](countable_actions_and_ordinal_bfs_coreflection_2026-11-18.md).

Take θ and w as in the first proof. Here θ is the first component of one of the two original P-maps. Write its components as θ_0,θ_1. We have w∧θ_0(C_ω)=0. Countable join preservation therefore gives an n with

    d=w∧θ_0(L_n)>0.

Apply the Ulam argument above using this d. It gives a disjoint family (A_i)_(i<λ) of subsets of λ with d∧θ_0(r^{-1}A_i)≠0 for every i. We may remove [0,ω] from every A_i, because d∧θ_0(C_ω)=0. For k=0,...,n+1 put

    V_i^k={D^k g : g∈L_n, r(g)∈A_i}.

For k≤n these are subsets of the continuous carrier. At k=n+1 they are disjoint from that carrier. At each fixed k the sets V_i^k are pairwise disjoint, including at the final discontinuous stage. Here it matters that all *preceding* iterates are continuous. If D^k g=D^k g′, then g and g′ agree on [k,λ]. To see this, whenever f,f′ are continuous and Df,Df′ agree on [j,λ] for a finite j, f,f′ agree on [j+1,λ]: the successor points in that interval belong to d_λ([j,λ]) and are dense there, including approximation at limit points. Apply this implication backwards k times. Since r(g),r(g′)>ω, agreement on [k,λ] implies r(g)=r(g′), proving disjointness across distinct A_i.

For each i, θ_0(V_i^0)≠0 by the choice of d and A_i. If k≤n and θ_0(V_i^k)≠0, then

    q_Z θ_1(V_i^(k+1)) = θ_0({g∈S:Dg∈V_i^(k+1)}) ≥ θ_0(V_i^k)>0.

If k+1≤n, then p_Z θ_1(V_i^(k+1))=θ_0(V_i^(k+1)) because p_Y is inclusion. If k+1=n+1, that p-image is zero because V_i^(n+1) has no continuous members.

Thus for each i there is a first step j in {1,...,n+1} at which x_i=θ_1(V_i^j) has p-image zero and q-image nonzero. On λ indices this step j is the same, by finite pigeonhole. On those indices the x_i are pairwise disjoint by the disjointness just proved at fixed j. Their nonzero q-images are also pairwise disjoint, since q_Z is a Boolean homomorphism. This proves the structural test.

## An endpoint split obeying both naturality squares

There is a second explicit test. Let R_0=T=ω² and let R_1 be two copies of T identified on their diagonal, with p_R and q_R the two inclusions. Form the corresponding tail quotient W on λ rows. For t<λ put γ_t=t+ω, a nonzero limit below λ. Use the previous step function h with cutoff γ_t, writing g=h_(γ_t)(x,y). On the first copy of T in R_1 assign the function g, and on the second assign Dg. These assignments agree on the glued diagonal because g is constant there. They commute with the action on values and, together with the first-sort assignment (x,y)↦g, define a genuine K-map R→Y on each row. Using the constant function with value x instead defines a second K-map on each row. Dualizing and taking tail germs gives two genuine P-maps b,a:E(Y)⇉W. Their images at all earlier evaluations agree and their endpoint images are respectively the second and first coordinate projections, as in the one-sort test.

The unique-extension axiom already fails inside the images. Define a single F on the full second carrier by

    F(r)=r(0) if r is continuous, and F(r)=r(λ) otherwise.

Then b_1(F) is represented on every row by the function whose restrictions to the two legs are respectively x and y. On the second leg this follows because Dg is discontinuous at γ_t when x≠y, and both prescriptions agree for x=y. In particular this image is balanced (the two restrictions are equivariant), although F itself need not be balanced on the full second carrier. The image b_1(v_0) of evaluation at 0 is also balanced and has leg restrictions x and x, since d_λ(0)=1≤γ_t.

Thus b_1(F) and b_1(v_0) have identical p-images. Their q-images are respectively b_0(u_λ) and a_0(u_λ). Under any map into an E(σ)-orthogonal object, including any member of M, the two balanced extensions with the same p-image must become equal. Their q-images must therefore become equal as well. This works even for a map defined only on the subpresheaf generated by the two images, since both elements and the equalities exhibiting balance belong to it.

Consequently this explicit two-sort split cannot survive postcomposition into M. A successful split must supply the large structural-kernel antichain proved above while avoiding this forced identification of its endpoints. The unrestricted case remains open here.
