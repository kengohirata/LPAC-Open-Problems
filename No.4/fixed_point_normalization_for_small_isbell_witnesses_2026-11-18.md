# Fixed-point normalization for small Isbell witnesses

2026-11-18. Status: PROOF_RECONSTRUCTED; the coordinating agent checked the normalization and packing argument, not externally reviewed or formally verified. This removes the fixed-point obstruction from the packed-separator theorem locally at a finite seed. No N or NC assumption is used.

## 1. At most countably many fixed points suffice for packing

Let A be any M_1-set, not necessarily finite-support, with |A|<=c and at most countably many M_1-fixed points F. Choose an injection eta:F->2 omega and an injection xi:A\F->2^omega. Define a countable separating family by

    f_n(a)=eta(a)                 if a is fixed,
           2 xi(a)(n)+1          otherwise.

All f_n agree on F, and they jointly separate A.

Choose injections b_n:omega->omega with disjoint images. Their actions on A are injective, because each b_n has a left inverse, and

    b_n A intersect b_m A = F       (n!=m).

For the nontrivial inclusion, write z=b_n x=b_m y and choose, for every l, a transformation t with t b_n=id and t b_m=const_l. Then x=const_l y for every l, so x is fixed and z=x. This argument does not require finite support.

Therefore the prescriptions

    z(b_n a)=f_n(a)

are consistent: their only overlaps occur at fixed points, where all f_n have the same value. Extend z arbitrarily elsewhere. Its right translates z·b_n=f_n form a countable separating family. Applying this in both sorts supplies packed countable separators for every K-object with carriers at most c and countably many fixed points in each sort.

The [strong packed-separator factorization theorem](packed_separators_force_monic_d_factorization_2026-11-18.md) consequently applies to all such objects. In particular, for such Y in C and Z in M, every map E(Y)->Z factors through one monic D-object by an actual E-image, and every equalizer E(Y)⇉Z belongs to D.

## 2. Collapsing only fixed points while preserving a finite seed

Let Y belong to C and choose finitely many functions on its two sorts. Enlarge the sort-0 list by the p_Y- and q_Y-pullbacks of the sort-1 list. Define a quotient q_i:Y_i->Q_i by identifying two fixed points exactly when their values on the chosen finite list agree, and leaving every nonfixed point in a singleton class.

These are M_1-congruences. The enlarged sort-0 list makes the structural maps descend, so q:Y->Q is a K-map. Every chosen function factors through q. The set of fixed-point classes in each Q_i is countable, since it injects into a finite power of omega.

No new fixed point appears: a nonfixed point has singleton equivalence class, so its class could be fixed only if every transformation had already fixed that point. Thus a sort has a fixed point after quotienting exactly when it had one before.

The quotient Q remains in C. Its first sort is finite-support as a quotient of Y_0. In each sort with no fixed points the quotient is unchanged. In a sort with fixed points, both its original and quotient character sets are empty. Thus the quotient maps induce bijections on both character sets, and bijectivity of H(p_Y) transfers to H(p_Q).

For a finitely generated presheaf map F->E(Y), apply the construction to its finite list of generator images and the indicated structural pullbacks. The map factors through the monomorphism E(Q)->E(Y). Preservation of relations follows because this latter map is monic, or directly by transposing the factorization through q.

If both Y_i are finite-support, so are both Q_i. If |Y_i|<=c, that bound is also preserved.

## 3. Local equalizer closure for every small C-source

**Corollary (ZFC).** If Y belongs to C, |Y_i|<=c, and Z belongs to M, then

    Eq(a,b) belongs to M       for all a,b:E(Y)->Z.

Moreover its finite families have monic D-covers whose dual carriers are at most c. If Y belongs to C_bfs, these covers also belong to C_bfs.

Proof. Take a finite family in the equalizer. Section 2 gives a quotient Y->Q in C preserving that family, with carriers at most c and countably many fixed points. Restrict a,b to the monic E(Q)-subobject. Section 1 and the strong factorization theorem show that the restricted equalizer is E(R), where R is a K-coequalizer of maps between C-objects and hence lies in C. It contains the chosen family and is monic in the original equalizer.

The coequalizer R is a quotient of Q, so its carriers remain at most c; if Q is both-finite-support, so is R. This proves the corollary. □

This is a local statement when Y has uncountably many fixed points: the entire equalizer need not have been shown to be one D-object. The stronger whole-equalizer conclusion remains available when Y itself has packed countable separators.

## 4. Relation to the both-finite-support result

The established C_bfs epi-compression theorem first replaces any finite seed in a C_bfs witness by a monic witness with dual carriers at most c. Section 2 then normalizes its fixed points, and Section 3 supplies its required equalizer cover. This is a uniform alternative to separating the characterless and characterful cases in the proof of M_bfs equalizer closure.

Together with products, directed-union closure, and the bounded-hull solution-set theorem, this yields reflectivity of M_bfs in ZFC. See [the main BFS closure/reflection theorem](both_finite_support_monic_local_class_is_reflective_2026-11-18.md). This note records the more general fixed-point normalization mechanism and the small-source corollary.
