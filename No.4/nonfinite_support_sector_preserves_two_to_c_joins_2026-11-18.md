# The non-finite-support sector preserves joins of size at most 2^c

2026-11-18. Status: PROOF_RECONSTRUCTED; the coordinating agent read the complete proof and independently checked the almost-disjoint overlap argument and both continuity steps. Another research agent independently reconstructed the full theorem and the sharpness example in Section 5. No external review or formal verification. The coordinating agent proposed the almost-disjoint packing argument. The relative formulation below removes any restriction on the number of fixed points. This is a ZFC restriction on maps into M, not a proof that M is equalizer-closed.

Let S be an arbitrary M_1=End(omega)-set, let Z belong to M, and fix a sort of Z. Suppose

    a:omega^S -> Z_i

commutes with left postcomposition and right precomposition. Put N=S\S_fs and c=2^aleph_0. Binary elements of Z_i have the usual finite Boolean operations supplied by tuple coding; write B(Z_i) for this Boolean algebra. The map a induces a Boolean homomorphism P(S)->B(Z_i).

**Theorem.** The homomorphism into the corner below a(chi_N),

    P(N) -> [0,a(chi_N)],       A |-> a(chi_A),

preserves all unions and intersections indexed by sets of cardinality at most 2^c. Neither S nor its set of fixed points is assumed small.

Equivalently, if U=union_(xi<kappa) U_xi, kappa<=2^c, and a binary v satisfies

    v <= a(chi_(U intersect N)),
    v meet a(chi_U_xi)=0                 for every xi,

then v=0. For the universal-property formulation, apply this criterion to the difference between a(chi_(U intersect N)) and any proposed upper bound of the individual images.

## 1. Countable meets are already preserved

Any M_2-map from a full power into a target with unique finite tuple coding and left point separation preserves countable Boolean meets. This applies to Z_i.

For completeness, let A_n subset S, and suppose w<=a(chi_A_n) for every n. Define C(s)=0 if s belongs to every A_n, and otherwise C(s)=1+min{n:s is not in A_n}. Each finite left truncation e_k C is a finite pointwise function of finitely many chi_A_n. Therefore the element which equals a(C) on w and zero off w has every left truncation zero. Left point separation makes it zero. Applying the unary test for C=0 proves

    w <= a(chi_(intersection_n A_n)).

The reverse inequalities follow from finite order preservation. Countable joins follow by complementation.

## 2. Packing observations that vanish on the finite-support part

Choose c injections b_r:omega->omega with infinite almost-disjoint ranges. For r!=s,

    b_r S intersect b_s S subset S_fs.                 (1)

To see this, choose a selfmap u of omega fixing range(b_r) pointwise and mapping range(b_s) outside the finite intersection into one fixed natural number. If x=b_r y=b_s z, then ux=x, while u b_s has finite range. Hence x lies in the image of a finite-rank action and is finite-support.

Consequently, any family (f_r:S->omega)_(r<c) that vanishes on S_fs can be packed into one z:S->omega satisfying

    z(b_r s)=f_r(s).                                    (2)

An injection has a left inverse, so the prescription is single-valued on each b_r S. If a point is in two such images, (1) and the left inverses show that both of its preimages are finite-support; both assigned values are zero. Set z=0 outside the union of the images.

The countable version follows either from this construction or from countably many injections with disjoint ranges. No finite-support assumption on S was used.

## 3. First step: joins of size at most c on N

Suppose kappa<=c and U=union_(xi<kappa) U_xi. Choose a selector xi(s) for s in U intersect N, and encode its values injectively by countable binary sequences. Let f_n be the resulting bits on U intersect N, extended by zero everywhere else. They vanish on S_fs, so Section 2 packs them into one z.

If a nonzero v satisfied the theorem's two displayed conditions, choose a monic D-cover containing v and a(z). In that full-power cover choose a point where the binary preimage of v is 1. Its singleton image w is nonzero and satisfies w<=v.

All a(f_n)=a(z)·b_n lie in this same cover. Evaluating their binary preimages at the chosen point determines a profile p in 2^omega and gives

    w <= a(chi_[f_n=p_n])              for all n.

Section 1 now gives w below the image of the full profile fibre. Intersecting with the already known support U intersect N leaves either the empty set or a subset of exactly one U_xi, because the selector codes are injective. Either possibility contradicts w!=0 and the assumed disjointness. This proves c-sized join preservation on N without any fixed-point hypothesis.

A useful equivalent consequence is the following relative c-meet rule: if w<=a(chi_N) and w<=a(chi_A_r) for every r<c, then

    w <= a(chi_(N intersect intersection_(r<c) A_r)).    (3)

Indeed, apply the proved join statement to the complements N\A_r and to the part of w supported on their union.

## 4. Second step: joins of size at most 2^c on N

Now let kappa<=2^c. Encode the selected indices xi(s), for s in U intersect N, injectively by c binary coordinates. Extend all these bits by zero on S\(U intersect N). Section 2 again packs the entire c-indexed family into one z.

As before, take a common monic D-cover of v and a(z), and choose a nonzero singleton image w<=v. The values of all its translated packed bits determine p in 2^c. Thus w lies below every one of the c corresponding profile-fibre images.

Since w<=a(chi_N), the relative c-meet rule (3) puts w below the image of the full profile fibre inside N. Intersecting also with U leaves either no point or points with one fixed selector index xi. The former contradicts nonzeroness; the latter puts w below a(chi_U_xi), contradicting w<=v. Therefore v=0.

Complements inside the corner [0,a(chi_N)] give the intersection statement. This completes the proof.

## 5. An actual M_bfs counterexample on the finite-support sector

The restriction to N is essential even when there are no fixed points. Put lambda=c^+ and take S=lambda times omega, the coproduct of lambda copies of the standard M_1-set omega. All of S is finite-support and it has no fixed point. Let S^Delta denote the diagonal K-object with both carriers S and p=q=id. Form

    U=colim_(beta<lambda) E(([beta,lambda) times omega)^Delta),

where the maps restrict to tails. Both U-sorts are the same reduced power, and p=q=id. The quotient maps give an actual P-map

    a:E(S^Delta)->U.

Here U belongs even to M_bfs. To prove this directly, represent any finite family of elements of U on a common tail. Each row t gives a finite tuple of functions omega->omega, so at most c different row types occur. The union of the bounded occurrence sets of all bounded row types is bounded, since lambda is regular and exceeds c. Discard that initial segment, and let P be the remaining set of types, each recurring unboundedly. Put Q=P times omega with its coproduct action. Assign row (t,n) to (type(t),n). This is an equivariant map on the retained tail and induces

    E(Q^Delta)->U.

It is monic: two functions on Q differing at (p,n) remain distinct on every row of type p, an unbounded set. The chosen finite family factors through this map by its definition. Since Q is finite-support and Q^Delta belongs to C_bfs, this is the required monic local cover.

For each alpha<lambda, however,

    a(chi_({alpha} times omega))=0,

whereas the image of the indicator of their union S is 1. Thus a fails to preserve this lambda=c^+-indexed join, and lambda<=2^c. This is an actual map into M_bfs, rather than merely an abstract Boolean-algebra obstruction.

Consequently c-sized continuity cannot in general be increased even to c^+-sized continuity on the finite-support sector. The stronger 2^c result on N isolates a real distinction.

## 6. Scope of the improvement

The first c-sized step used countable bit profiles and ordinary countable meet preservation. The second used c almost-disjoint injections and the relative c-meet rule proved in the first step. It did not assume an uncountable meet operation in Z in advance; the displayed full-power images are proved to have the required universal property.

The argument does not assert 2^c-sized join preservation on S_fs. The almost-disjoint images can overlap there, which is why the selector bits were set to zero on that entire sector. Thus an attempted completion using up to 2^c character observations has a new bound on its non-finite-support part, while the finite-support part may still need an independent argument.

Nor does this supply joins larger than 2^c: a single finite right-orbit generating family has only c translates, so this packing step provides c bits and no more. No claim that this bound is optimal is made.
