# Countable actions and the both finite support coreflection of the ordinal examples

2026-11-18. Status: PROOF_RECONSTRUCTED. These are exclusions and structural reductions for the counterexample search, not a solution of Problem 4.

## 1. Every countable End omega action has finite support

Let M=End(ω), with its pointwise topology. Theorem 5.4(iv) in Elliott, Jonušas, Mesyan, Mitchell, Morayne, and Péresse, *Automatic continuity, unique Polish topologies, and Zariski topologies on monoids and clones*, states automatic continuity from M to second countable topological semigroups. See the [author's manuscript, p.15](https://academics.uccs.edu/zmesyan/papers/AutomaticContinuity.pdf) and [published article](https://doi.org/10.1090/tran/8987).

**Corollary.** Every left M-set A with countable underlying set is finite-support in the sense used in C.

Proof. The action homomorphism M→End(A) is continuous, since End(A) has a second countable pointwise topology. For a∈A, continuity at id gives a finite S⊆ω such that every m fixing S pointwise fixes a. Enlarge S if necessary to be nonempty, and choose a retraction e:ω→S fixing S. Then ea=a. If m|S=n|S, we have me=ne, and therefore ma=mea=nea=na. Thus S supports a. The empty A is immediate. □

This does not say that all actions of carrier ≤continuum are finite-support. In particular, ω^ω with postcomposition contains elements with no finite support.

## 2. The continuous dynamical factor of an ordinal successor

Fix an infinite ordinal κ≥ω. Give Xκ=[0,κ] its ordinal topology and put

    dκ(α)=α+1 for α<κ,   dκ(κ)=κ.

Let C∞ consist of the continuous functions f:Xκ→ω such that every f∘dκ^n is continuous. Equivalently, these are the functions whose restriction to the initial ω is eventually constant and whose value on [ω,κ] is that same constant. In particular C∞ is countable.

One direction is immediate. For the other, suppose f∈C∞ and f first differs from f(ω) somewhere above ω. Continuity forces the first such point to be a successor β+1. Write β=λ+n with λ a nonzero limit ordinal and n<ω. Then f∘dκ^(n+1) has the earlier constant value on all points sufficiently close to λ from below, but a different value at λ. This contradicts continuity. Continuity at ω gives eventual constancy on the initial ω. Thus the characterization holds.

The following equivalent dynamical observation is useful. If T is Hausdorff, v:T→T is continuous, and a continuous h:Xκ→T satisfies h dκ=v h, then h is constant on [ω,κ]. Indeed,

    v(h(ω)) = lim_n v(h(n)) = lim_n h(n+1) = h(ω).

Successor induction and continuity at limit ordinals now propagate this value to κ. No assumption on the cofinality of those later limit ordinals is needed.

## 3. An explicit coreflection at Yκ

Use K=(M-Set)^(0⇉1), H(A)=Hom_M(A,ω), and

    Yκ=(Cont(Xκ,ω) --inclusion,dκ*--> ω^Xκ),
    Y∞=(C∞ --id,dκ*--> C∞).

Let C_bfs be the full subcategory of C in which both sorts have finite support. Y∞ belongs to C_bfs. Its evident inclusion j:Y∞→Yκ is a K-map.

**Proposition (ZFC).** Every K-map k:R→Yκ with R∈C_bfs factors uniquely through j. Thus j is a C_bfs-coreflection of this particular K-object Yκ.

Proof. Set T=H(R0), S=H(R1). Both spaces are compact Hausdorff by the finite-support argument. The continuous bijection u=H(p_R):S→T is therefore a homeomorphism. Put

    v=H(q_R)u^(-1):T→T.

This is continuous. For each x∈Xκ let

    h(x)(a)=k0(a)(x),  a∈R0,
    ℓ(x)(b)=k1(b)(x),  b∈R1.

These are equivariant maps R_i→ω. The function h:Xκ→T is continuous because every k0(a) is continuous. Naturality of k gives

    uℓ=h,   H(q_R)ℓ=h dκ,

so ℓ=u^(-1)h is continuous and h dκ=v h. Section 2 makes h constant on [ω,κ], and hence makes ℓ constant there as well.

It follows that each k0(a) and each k1(b) is continuous and constant on [ω,κ], hence belongs to C∞. Thus both components of k land in Y∞, giving the required factorization. Uniqueness follows because j is componentwise injective. If T is empty, the assumed k cannot exist, since h would map the nonempty Xκ to T; this covers that case. □

This proof uses neither N nor the No.1 non-coreflectivity input. Yκ itself belongs to C under N, but this membership was not needed for the displayed universal property.

## 4. What this does and does not say about the union targets

For a countable R∈C, Section 1 places R in C_bfs. Consequently every actual K-map R→Yκ lands in Y∞, and the same holds for copowers of R. Thus maps E(Yκ)→E(T·R) explicitly in the image of E factor through E(Y∞).

This is not yet a factorization theorem for every map E(Yκ)→V^R into a directed union of such stages. A map to the union need not lift to a stage. Applying the coreflection pointwise without first producing genuine K-maps would assume the missing step.

For templates with p_R an isomorphism, an additional countable-orbit argument supplies that step; see [the separate proof](ordinal_witness_maps_to_piso_templates_2026-11-18.md). For general countable R, this lifting question remains open.

The next concrete family under examination uses R=Yω. Its first sort is countable, but its second sort ω^[0,ω] has cardinality continuum and is not finite-support. Thus neither Section 1 nor the both-finite-support compression theorem removes this template.
