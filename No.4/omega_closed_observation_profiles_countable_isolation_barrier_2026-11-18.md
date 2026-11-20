# Omega-closed observation profiles: the singleton and cardinality barrier

2026-11-18. Status: PROOF_RECONSTRUCTED. This independently examines an attempted extension of the packed-countable-separator argument. It proves a precise obstruction to the proposed proof, not failure of the proposed categorical theorem and not a No.4 counterexample. Sections 1–5 and the source construction in Section 6 are ZFC; the minimal-D-hull conclusion at the end explicitly assumes N.

**Later improvement:** the [continuum Boolean-continuity theorem](continuum_boolean_continuity_and_orbit_separator_factorization_2026-11-18.md) uses the right action to overcome this proof barrier. It proves the Section 6 coinduced source safe: any two M-valued maps agreeing on h are equal, and all its M-valued equalizers belong to D. Thus Section 6 is a useful minimal-hull test but no longer an open counterexample construction. The scalar obstruction in Section 2 remains valid and does not satisfy the additional right-action hypotheses of that theorem.

## 1. Observation-closedness

Let F be a family of functions S→ω separating points. Write o:S→ω^F for the observation map. Say that o(S) is **omega-closed** if every p∈ω^F whose restriction to each countable subfamily F_0⊂F is realized by some point of S is itself realized by a point of S.

For the packed-profile argument, a local atom w supplies such a p. For any countable F_0, a first-difference counter proves

    w≤a(χ_(N(s,F_0))),
    N(s,F_0)={t∈S:f(t)=f(s) for every f∈F_0},

after omega-closedness identifies the full profile with its unique realizing point s.

The missing step is

    w≤a(χ_s).                                             (1)

There is generally an uncountable intersection between the displayed countable fibers and {s}. The finite-operation and left-truncation arguments do not perform that intersection.

## 2. A concrete failure of that inference

Take an uncountable index set I, S=ω^I, and let F be the coordinate projections. The observation image is all of ω^I, so it is omega-closed. Fix s∈S. No countable coordinate set isolates s.

Define an ideal of subsets of S by

    J_s={A⊂S : for some countable J⊂I,
                 A∩N(s,J)⊂{s}}.

This is a proper sigma-ideal. Downward closure is immediate. For a countable family with witnessing coordinate sets J_n, their union has the countable witness ⋃_n J_n. Properness follows because N(s,J) contains a point other than s for every countable J.

In the nonzero sigma-complete Boolean algebra

    B=P(S)/J_s,

the quotient map a satisfies

    a(N(s,J))=1       for every countable J⊂I,
    a({s})=0.

The first equality holds because the complement of N(s,J) belongs to J_s; the second holds directly from the definition. Thus w=1 lies below every countable profile fiber while failing (1).

Equivalently, the quotient map and the point-evaluation map P(S)→{0,1}→B agree on every coordinate fiber but differ on {s}. Omega-closedness has ensured that the common profile is an actual source point; it has not made the corresponding target element live under the image of that singleton.

### The scalar target already has monic local full-power covers

For a sigma-complete Boolean algebra B, let Part_ω(B) be its set of countable partitions of 1, with M_2=End(ω) acting by merging the partition blocks according to the selfmap. The quotient above induces an M_2-map ω^S→Part_ω(B).

Every finite family of elements of Part_ω(B) lies in a monic full-power subact. Take their common countable refinement, discard zero blocks, and denote the remaining nonzero blocks by (b_q)_(q∈Q). The map

    ω^Q→Part_ω(B),
    f↦(∨_(f(q)=n)b_q)_(n∈ω)

is equivariant and injective. Distinct f are distinguished by a nonzero block b_q. Thus the failure above persists in the one-monoid scalar setting even with finite-family monic full-power covers.

This does **not** assert membership in the actual two-sort class M. No compatible right M_1-action and C-condition have been supplied for this quotient target. Those additional conditions could matter to the categorical extension theorem.

## 3. Stability under arbitrary added observations forces countable isolation

Assume o(S) is omega-closed. The following conditions are equivalent.

1. For every x:S→ω, the enlarged observation image

       S→ω^(F∪{x})

   is omega-closed.
2. For every s∈S there is a countable F_s⊂F with N(s,F_s)={s}.

For 1⇒2, suppose s is not countably isolated. Adjoin x=χ_s and consider the extended profile whose F-coordinates equal o(s) but whose x-coordinate is 0. Every countable restriction of this profile is realized: choose t≠s agreeing with s on the countably many specified F-coordinates. The full profile is not realized, because F separates points. This contradicts 1.

For 2⇒1, let a candidate extended profile have every countable restriction realized. Its base profile is realized by some s, by omega-closedness of o(S). Applying consistency to F_s together with x forces its x-coordinate to equal x(s). Thus the full profile is realized by s.

In fact it suffices in condition 1 to adjoin only singleton indicators χ_s, one at a time.

## 4. Cardinal consequence for finitely generated observation families

If |F|≤c=2^aleph_0 and every point is countably isolated by F, then

    |S|≤c.

There are at most c countable subfamilies of F, and at most c assignments of natural-number values to each such subfamily. Every isolated point is uniquely determined by one such pair. Hence there are at most c points.

More generally, for infinite |F|=θ the same argument gives |S|≤θ^aleph_0.

The right orbit of a finite family has size at most |M_1|=c. Therefore requiring stability under arbitrary additional observations brings this method back to the already established small-carrier bound. It does not extend the packed-profile theorem to larger carriers.

## 5. The large, one-generator configuration is real

The omega-closed observation hypothesis by itself can occur for a large M_1-set with all observations in one right orbit. Let M=M_1 and take the coinduced M-set

    S=ω^M,       (m·s)(r)=s(rm).

Let h(s)=s(id). Then

    (h·m)(s)=s(m).

Thus the right orbit of h is the full coordinate family on ω^M. It separates S, its observation image is the whole product and hence omega-closed, and

    |S|=ω^c=2^c>c.

No point is isolated by countably many coordinates. This example shows that omega-closedness plus finite-orbit generation does not itself hide the small-carrier hypothesis.

It does not provide the missing two maps into an actual M-target. What it identifies exactly is the remaining task: eliminate, or realize in M, a local atom that has an actual full source profile while remaining disjoint from that source point's singleton image. The usual first-difference argument alone cannot decide this.

## 6. An actual C-object with this large observation sort

The coinduced example also supplies an actual C-source for a further equalizer test. Let A=S_fs be its finite-support part and put

    Y=(A --inc,inc--> S).

Choose the usual rank-n retraction e_n:ω→{0,...,n−1}. A point s∈S is fixed by e_n exactly when s(r)=s(re_n) for every r∈M. Such s are arbitrary functions on the countable set M e_n≅ω^n. Every finite-support point is fixed by some e_n, and conversely such a fixed point has finite support. Thus

    A=⋃_(n≥1) Fix(e_n),       |A|=c,       |S|=2^c.

Both A and S contain M-fixed points, namely constant profiles. Since ω has no M-fixed point, H_1(A)=H_1(S)=∅. Consequently Y∈C, in ZFC.

Regard h(s)=s(id) as one element of E(Y)_1. Its full right orbit separates S. On A, the restrictions of a countable dense submonoid of M already separate points, by finite support. Therefore, for maps a,b:E(Y)→Z with Z∈M, agreement on h forces a_0=b_0 by the existing countable-separator lemma. The possible disagreement is entirely in the second sort.

There is also a minimal-D-hull conclusion, now **assuming N** for full faithfulness of E. If a monic D-subobject E(Q)↪E(Y) contains h, write its dual as a componentwise-surjective K-map u:Y→Q. The factorization of h through u_1, together with equivariance, makes every right translate of h factor through u_1. Since those translates separate S, u_1 is injective, hence bijective. If u_0(x)=u_0(y), naturality gives u_1(p_Yx)=u_1(p_Yy); injectivity of u_1 and of p_Y then gives x=y. Thus u_0 is also bijective and the subobject is all of E(Y).

Accordingly, under N, any two distinct maps

    a,b:E(Y)⇉Z,       Z∈M,       a(h)=b(h),

would have an equalizer outside M. Otherwise the finitely generated subpresheaf generated by h would have a monic D-cover inside that equalizer, contradicting the minimal-hull conclusion.

No such pair is constructed here. This gives an explicit test source with first carrier c and second carrier 2^c, one generating observation, and an omega-closed full observation image. It avoids ordinal dynamics while remaining beyond the proved small-source factorization theorem.
