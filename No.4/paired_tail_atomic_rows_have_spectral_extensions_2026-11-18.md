# Atomic partial rows have spectral extensions, under a first-sort size bound

2026-11-18. Status: **PROOF_RECONSTRUCTED**, independently checked by the coordinating research agent; not externally reviewed or formally verified. This strengthens the reduction for a hypothetical nonlifting paired-ordinal witness. It does not exclude that witness, prove membership in M, or settle No.4.

Use the [paired ordinal tail](paired_ordinal_tail_stage_monic_obstruction_2026-11-18.md): λ>c is regular, R=Y_λ, X=[0,λ], R₀=C(X), and W is the bounded-tail quotient of copies of E(R). Suppose

    j:E(Y) ↪ W,     Y∈C,     |Y₀|≤λ.

The extra cardinal hypothesis is satisfied under V=L/GCH for any such monomorphism: |R₀|=λ, hence |W₀|≤2^λ, whereas |E(Y)₀|=ω^{|Y₀|}; GCH and injectivity give |Y₀|≤λ. The argument below itself uses only the displayed cardinal bound, finite support of Y₀, and the first-sort full-power map. It does not use N or the second-sort extension condition separately, once the objects and map are given.

Put T=H₁(Y₀), a compact Hausdorff space.

## 1. The new reduction

After removing an initial tail, there are M₁-stable subsets D_t⊂R₀ and equivariant maps

    q_t:D_t→Y₀

with the following properties.

1. Every y∈Y₀ lies in im(q_t) for unboundedly many t<λ.
2. For every t and every h∈T, there exists ξ∈[0,λ] such that

       h(q_t(g))=g(ξ)      for every g∈D_t.             (1)

3. The relation

       L_t={(h,ξ)∈T×[0,λ] : (1) holds}

   is compact and its projection to T is onto.
4. If the paired seed factors through j, with corresponding characters h,k∈T, then

       (h,0)∈L_t,       (k,t)∈L_t.

Equivalently, set Q_t to be the compact image of the evaluation map [0,λ]→ω^{D_t}. There is a continuous map T→Q_t with coordinates h↦h(q_t(g)), and L_t is its pullback along the continuous surjection [0,λ]→Q_t.

In particular the missing-evaluation phenomenon in the [finite partial-row example](partial_ordinal_rows_do_not_supply_spectrum_maps_2026-11-18.md) cannot persist in these suitably scheduled atomic rows of an actual full-power monomorphism. The remaining issue is a compatible continuous and dynamical choice of the extensions (1).

## 2. Representatives and the equations to synchronize

For each y∈Y₀, choose a binary row representative v_y(t,g) of j₀(χ_{y}). Its support is nonempty on unboundedly many rows: otherwise j₀(χ_y)=j₀(0), contradicting monicity.

Choose a row representative f_a of j₀(a) for every character a used below. Since a:Y₀→ω is equivariant, it is balanced for the two actions. There are only c action equations. Thus, for each a separately, after some tail all its row functions

    f_a(t,-):R₀→ω

are equivariant. The compact-space evaluation lemma, which is valid in ZFC, then supplies ξ_t(a)∈[0,λ] such that

    f_a(t,g)=g(ξ_t(a))      for all g∈R₀.             (2)

The following additional equations hold eventually for each indicated set of parameters:

- v_y and v_z have disjoint supports when y≠z;
- v_y(t,g)=1 implies v_(my)(t,mg)=1;
- v_y(t,g)=1 implies f_a(t,g)=a(y).

The first is disjointness of singleton indicators. The second comes from χ_y≤χ_(my)·m. The third comes from χ_y≤[a=a(y)]. These are finite-operation equations, preserved by j into W∈H_fg. Each involves actual row representatives, so a germ equation is pointwise on a sufficiently late tail.

## 3. A continuous schedule of small parameter sets

Choose an increasing continuous chain (A_α)_(α<λ) of M₁-subsets of Y₀, each of size <λ, with union Y₀. This is possible since |M₁|=c<λ and |Y₀|≤λ. For each α choose H_α⊂T, also of size <λ, such that every pattern of values on a finite subset of A_α realized by any h∈T is realized by some a∈H_α.

These choices can be made increasing and continuous. At a successor add representatives of all finite patterns; their number is at most max(|A_α|,ℵ₀). At a limit take the union: any finite subset of the union already appeared earlier. In the paired case include h and k from the start.

For each stage, fewer than λ equations are involved: disjointness for A_α, equivariance implications for A_α×M₁, the character action equations for H_α×M₁, and comparisons for A_α×H_α. Regularity therefore gives a common tail bound.

Choose increasing continuous bounds b_α<λ, with b_α≥α, such that all these equations hold for parameters in A_α,H_α on every row t≥b_α. At a successor enlarge the bound as needed. At a limit, the supremum of previous bounds suffices, because every individual equation already appeared at an earlier stage. Starting indices of all representatives can be included among the bounds.

For t≥b₀, let α(t) be the greatest α with b_α≤t. Such a greatest index exists by continuity of the bounds, and α(t) tends cofinally to λ. Define

    D_t={g∈R₀ : v_y(t,g)=1 for some y∈A_(α(t))},
    q_t(g)=that unique y.

Disjointness makes q_t well defined. The equivariance implications and M₁-stability of A_(α(t)) make D_t stable and q_t equivariant. Every fixed y eventually belongs to every A_(α(t)); its nonzero atom still occurs on unboundedly many rows. This proves recurrence.

The continuity of the schedule is useful: choosing unrelated row bounds and then taking arbitrary smaller parameter sets would not by itself preserve recurrence on all unbounded atom supports.

## 4. Finite-pattern realization and compactness

Fix t and h∈T. For each g∈D_t impose the closed condition

    g(ξ)=h(q_t(g))      on ξ∈[0,λ].

Take any finite list g₁,...,g_n and write y_i=q_t(g_i). Choose a∈H_(α(t)) with a(y_i)=h(y_i) for every i. Its row is an evaluation by (2), and the synchronized atom comparisons give

    g_i(ξ_t(a))=f_a(t,g_i)=a(y_i)=h(y_i).

Thus the closed conditions have the finite intersection property. Compactness of [0,λ] gives a common ξ, proving (1).

For each fixed g, the equation h(q_t(g))=g(ξ) defines a closed subset of T×[0,λ], since both sides depend continuously on their respective variables. Therefore L_t is compact. Its projection to T is onto by the preceding argument.

For the paired seed, use its prescribed row representatives f_h(t,g)=g(0) and f_k(t,g)=g(t). Their germ identities and the atom comparisons are among the synchronized equations, giving the last property directly.

## 5. Why extension existence does not finish the stage argument

An extension ξ in (1) need not be unique. The proof gives a continuous map into Q_t and a compact nonempty fibre of the quotient [0,λ]→Q_t; it does not give a continuous lift into [0,λ]. Nor has it supplied an intertwining relation with the set selfmap D=H₁(q_Y)H₁(p_Y)^{-1} of T. The original stage proof needs both.

Continuous selection is a real additional issue for this form of relation, even among compact ordinal spaces. Let X' be the disjoint union of two copies of [0,ω], equivalently [0,ω·2], and let π:X'→T' identify their two limit points and no isolated points. Then T' is the one-point compactification of a countable discrete set, hence homeomorphic to [0,ω]. The map π is a continuous surjection with no continuous section: all isolated points have unique preimages, and the sequences from the two branches would force the section's value at the common limit to equal both distinct source limits.

Take A=C(T') and regard π* A⊂C(X') as a partial row with q(π*a)=a. The associated relation

    {(h,ξ): h(q(g))=g(ξ) for all g∈π*A}

is exactly the graph relation π(ξ)=h under H₁(A)≅T'. Every character has an evaluation extension, but no continuous choice exists. Both A and C(X') are finite-support M₁-sets; using identity structure arrows gives actual C-objects if desired. This example concerns the first-sort extension/selection issue, not the successor dynamics of the paired construction, and it is not asserted to arise from a monomorphism into W.

Thus the new reduction removes one precise obstruction—existence of evaluation extensions on the recurrent partial rows—while retaining two explicit tasks: obtain a suitable continuous selection, or replace it by a sufficient compact-relation argument; and recover compatibility with the C-induced dynamics. No general nonlifting witness has yet been excluded.
