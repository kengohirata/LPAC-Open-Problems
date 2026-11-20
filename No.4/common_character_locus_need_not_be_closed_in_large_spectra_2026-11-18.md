# The common-character locus need not be closed in a large spectrum

2026-11-18. Status: PROOF_RECONSTRUCTED; another research agent independently reconstructed the character-space calculation, recurring-type target cover, and full equalizer decomposition. The audit corrected the initial claim of point separation across diagonal blocks; the observation quotient and completion-failure witness below incorporate that correction. No further gap was found. Not externally reviewed or formally verified. This is a ZFC boundary example for the one-step common-character repair. Both the target and the equalizer below belong to M_bfs, so it is not a failure of M-equalizer closure.

Put c=2^aleph_0, λ=c^+, B=ω² with its coordinatewise M_1-action, and S=λ×B, the coproduct action. Let Y and R be the diagonal K-objects on S and B respectively, with p=q=id. Both lie in C_bfs.

Every equivariant B→ω is one of its two coordinate projections. Consequently

    H(Y_0)={0,1}^λ

with the product compact topology. Its weight is λ, beyond the continuum-weight hypothesis of the new repair theorem.

Form the diagonal tail target

    U=colim_(β<λ) E(([β,λ)×B)^Delta).

This is in M_bfs by the recurring-row-type proof: finitely many functions on a countable B have at most c row types, all types occurring only boundedly can be discarded at once, and the remaining positive types give a monic copower-of-R cover.

There are two actual P-maps

    a,b:E(Y)⇉U.

For F:S→ω, let a(F) be represented in row t by F(t,-), and let b(F) be represented in every row by F(0,-). Their two sort components are the same. Coordinatewise equivariance and the diagonal structural arrows make these P-maps.

## 1. The common characters form a dense proper subset

For h∈{0,1}^λ, equality a_0(h)=b_0(h) says exactly

    h(t)=h(0) for all sufficiently large t<λ.

Thus their common-character locus is

    L={h∈2^λ : h is eventually equal to h(0)}.

It is dense: any finite coordinate prescription extends to such an h by choosing the value at 0, if not already prescribed, and using that value outside a bounded set. It is proper: partition λ into two unbounded sets and choose h taking different values on them. Hence L is not closed in H(Y_0).

In particular it cannot equal H(Q_0) for any quotient Y_0↠Q_0 with Q_0 finite-support. Such a character image is compact and therefore closed. Since L is dense, its observation quotient is the same as that given by all of H(S). This quotient retains every off-diagonal point (t,(x,y)) with x≠y, but identifies (t,(n,n)) across all blocks t for each fixed n; the full character space does not separate those diagonal points.

The full power of this quotient is not equalized. Choose an unbounded A⊂λ with 0∉A and put F(t,(x,y))=χ_A(t)χ_[x≠y]. This function descends to the quotient, because it vanishes on every identified diagonal point. Nevertheless b(F)=0 whereas a(F) is nonzero, since its nonzero rows include every t∈A. This shows concretely which completion step fails beyond the small-spectrum hypotheses.

## 2. The actual equalizer still has bounded local C-witnesses

An element F belongs to the equalizer precisely when there is β<λ such that

    F(t,-)=F(0,-) for every t≥β.

For β>0, let q_β:S↠S_β identify (t,x) with (0,x) for every t≥β, while retaining the other blocks t<β. This is an equivariant quotient. Taking diagonal K-objects gives S_β^Delta∈C_bfs, and

    E(S_β^Delta) ↪ E(Y)

is exactly the full-power subobject with that tail agreement. Its dual carrier has size at most c, since β<λ=c^+.

These subobjects increase with β and their union is Eq(a,b). Thus the equalizer is an explicit directed union of D_bfs-objects, and in particular lies in M_bfs.

The corresponding compact character loci

    L_β={h∈2^λ:h(t)=h(0) for all t≥β}

increase to L; each has weight at most c. This illustrates that the correct general construction may need suitably chosen compact invariant character subsets, rather than the whole common locus at once. Here the character dynamics is the identity, so the compact pieces are already invariant. For the discontinuous ordinal dynamics, obtaining such pieces remains a substantive additional step.

## 3. Changing the dynamics does not defeat a stage-induced construction

There is a general limitation on modifying this example. Let R,Y∈C, let U_R be a regular tail quotient of copies of E(R), and suppose a,b:E(Y)⇉U_R are represented by actual K-row maps

    k_a,k_b:[γ,λ)·R⇉Y

on one common tail. For each β≥γ take the K-coequalizer

    [β,λ)·R ⇉ Y → Q_β.

Then Q_β∈C, and E(Q_β)↪E(Y) consists exactly of the functions agreeing under the two row maps on every row at least β. These subobjects increase with β, and

    Eq(a,b)=∪_(β≥γ) E(Q_β)∈M.                         (1)

Every finite family in the equalizer has a common tail bound, which proves the local-witness assertion directly. No carrier bound, continuity of character dynamics, or N is needed, since the maps were assumed to be actual dual row maps.

Thus replacing the diagonal template by an ordinal template with discontinuous dynamics, while retaining such row representations for both arrows, still gives a safe equalizer. An equalizer counterexample by this route requires at least one genuinely non-stage arrow.

## 4. A necessary restriction on arrows into a both-finite-support tail

If both sorts of R are finite-support and cf(λ)>ω, the right truncations e_n jointly separate both sorts of U_R. Indeed u·e_n=v·e_n for every n gives countably many tail bounds; beyond their supremum all these equalities hold simultaneously. Every r∈R_i is fixed by some e_n, so u(t,r)=v(t,r) on that common tail.

Consequently every P-map θ:E(Y)→U_R factors through restriction to the finite-support truncation:

    E(Y) ↠ E(Y_fs) → U_R,       Y_fs=((Y_0)_fs⇉(Y_1)_fs). (2)

If F,G agree on (Y_i)_fs, then F·e_n=G·e_n for every n, because e_n has finite rank and e_n y is finite-support. Right equivariance and the separation just proved imply θ_i(F)=θ_i(G). Restriction of functions is componentwise onto, so these component factorizations assemble uniquely to the P-map in (2).

This applies to the present Ω² tail target. It is an additional constraint on a prospective non-stage construction, not a new safety theorem for arbitrary sources: even when Y∈C, its truncation Y_fs need not satisfy the unique-extension condition defining C. In particular no C-coreflector is being assumed.
