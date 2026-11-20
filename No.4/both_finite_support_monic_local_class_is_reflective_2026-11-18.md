# The both-finite-support monic local class is reflective

2026-11-18. Status: **PROOF_RECONSTRUCTED**; the coordinating research agent and another research agent independently reconstructed the closure argument, the bounded-hull reflection, and its size estimate, finding no gap. Not externally reviewed, formally verified, or checked for novelty.

All statements below are in ZFC. Use the standing P, K, E, C, D and M, and put

    C_bfs={Y∈C : both Y₀ and Y₁ are finite-support},
    D_bfs=the replete image E(C_bfs^op).

Let M_bfs consist of those P-objects whose every finite family of elements is contained in a monic D_bfs-subobject. Thus D_bfs⊂M_bfs⊂M.

**Theorem.** If A∈M_bfs, B∈M and a,b:A⇉B, then Eq(a,b)∈M_bfs. Consequently M_bfs is closed under all small limits and directed unions, and is reflective in P.

The target in the equalizer statement may belong to the unrestricted M. The result does not prove equalizer closure or reflection of that larger class.

## 1. Inputs

The proof uses the following established results.

1. [Finite-support type completion](finite_support_type_quotients_are_m_epic_completions_2026-11-18.md): for Y∈C_bfs and a,b:E(Y)⇉B with B∈M, every finite seed in their equalizer is contained in a monic full-power subobject E(Q), for a componentwise quotient Y↠Q with both Q_i finite-support and |Q_i|≤c. Membership Q∈C was the remaining condition in that theorem.
2. [Bounded epimorphic compression](both_finite_support_accessibility_and_epi_compression_2026-11-18.md), §5: every finite family in E(Y), Y∈C_bfs, is contained in E(Y')↪E(Y), where Y↠Y' is componentwise onto, Y'∈C_bfs, and |Y'_i|≤c.
3. [Packed-separator monic factorization](packed_separators_force_monic_d_factorization_2026-11-18.md): if Y∈C, |Y_i|≤c, and H₁(Y₀)≠∅, then every equalizer E(Y)⇉B, B∈M, lies in D. If Y is both-finite-support, the resulting object lies in D_bfs, since its dual is a quotient of Y.

The last input follows by choosing a common monic D-cover of finitely many packed separator images, extracting genuine point maps into Y by the first-difference argument, and taking the dual coequalizer. It uses no N or NC.

## 2. Equalizers from a both-finite-support D-source

Fix Y∈C_bfs and a,b:E(Y)⇉B, with B∈M. We show that every finite family in Eq(a,b) is contained in a D_bfs-subobject of that equalizer.

### Case I: H₁(Y₀) is empty

Apply finite-support type completion to the chosen seed, giving Y↠Q and a monomorphism

    E(Q) ↪ Eq(a,b).

Precomposition with the componentwise quotient is injective on characters. In particular H₁(Q₀) embeds into H₁(Y₀)=∅, so H₁(Q₀)=∅. Since p_Q:Q₀→Q₁ exists, a character on Q₁ would give one on Q₀, hence H₁(Q₁)=∅ as well. Therefore H₁(p_Q) is a bijection between empty sets.

The first sort of Q is finite-support, so Q∈C; its second sort is also finite-support, so Q∈C_bfs. Thus the full-power witness already is the required D_bfs-witness. More generally, every componentwise quotient of a characterless C-object remains in C.

### Case II: H₁(Y₀) is nonempty

Choose one character h∈H₁(Y₀), viewed as an element of E(Y)₀. Add h to the finite family to be preserved by bounded epi-compression. This gives

    E(Y') --i mono--> E(Y),
    Y'∈C_bfs,     |Y'_i|≤c,

containing the original equalizer seed and h.

The auxiliary character h need not belong to Eq(a,b). It is used only in the source-compression list; the compressed source is allowed to contain elements on which the two maps differ.

Since h factors through the onto quotient Y₀↠Y'₀, it descends to an equivariant character h' of Y'₀. Thus H₁(Y'₀)≠∅. Apply packed-separator factorization to the restricted pair

    ai,bi:E(Y')⇉B.

Its equalizer belongs to D_bfs and contains the original finite seed. The composite of this equalizer inclusion with i is monic into Eq(a,b). This supplies the desired D_bfs-witness.

Both cases prove

    Eq(E(Y)⇉B)∈M_bfs       for Y∈C_bfs, B∈M.        (1)

The witnesses obtained in either case can have dual carriers bounded by c: in Case I this is the type-quotient bound, and in Case II the coequalizer is a quotient of the compressed Y'.

## 3. General source in M_bfs

Let A∈M_bfs, B∈M, and a,b:A⇉B. Given a finite family in Eq(a,b), take a monic D_bfs-cover i:E(Y)↪A of that family. Its elements lift uniquely into Eq(ai,bi). By (1), the lifted finite family has a monic D_bfs-cover inside that equalizer. Composing the two monomorphisms gives a D_bfs-cover inside Eq(a,b).

Thus Eq(a,b) belongs to M_bfs. This is the asserted relative equalizer closure.

## 4. Products and directed unions

C_bfs is closed under small coproducts, so D_bfs is closed under small products. For a finite family in a product of M_bfs-objects, choose a monic D_bfs-cover of its projection in each factor; the product of those witnesses is a monic D_bfs-cover of the family in the product. The empty product is included. Hence M_bfs is product-closed.

For a directed union of M_bfs-subobjects, a finite family lies in one stage, where it has a monic D_bfs-cover. Its composite into the union remains monic. Thus M_bfs is directed-union-closed.

Products and equalizers give all ambient small limits. These arguments do not require full faithfulness of E under N.

## 5. Bounded hulls give reflection

By bounded epi-compression, every finite family in an M_bfs-object has a D_bfs-subobject of presheaf size at most 2^c. The ambient signature has size c. The [bounded monic-local solution-set theorem](bounded_monic_local_witnesses_solution_sets_2026-11-18.md) therefore applies with κ=2^c.

In particular every map X→A with A∈M_bfs factors through an M_bfs-subobject of A of size at most

    max(|X|,2^c).

This supplies a solution set for every source X. The full subcategory M_bfs is complete by §4, and its inclusion preserves these limits. The initial-object lemma in X↓M_bfs, or equivalently the general adjoint functor argument with this solution set, gives the reflection of X.

The reflection itself can be taken of size at most max(|X|,2^c): first take the product yielding a weakly initial object, shrink it around the image of X using the bounded-hull theorem, and then equalize all its comma-endomorphisms. This equalizer is a subobject of the bounded weakly initial object and is initial by the standard complete-category proof.

## 6. Scope

This establishes a complete positive result for the both-finite-support monic local class, including its equalizer closure, which was previously missing. It is a ZFC theorem and does not use No.1's NC input or any no-measurable-cardinal hypothesis.

The unrestricted candidate M allows C-witnesses with a non-finite-support second sort. Neither the bounded compression theorem nor the finite-support type-completion argument covers those witnesses. Its equalizer question, and No.4 in general, remain open in this work.
