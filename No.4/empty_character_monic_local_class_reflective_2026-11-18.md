# Empty-character local witnesses form a reflective class

2026-11-18. Status: PROOF_RECONSTRUCTED; another research agent independently reconstructed the entire argument, including the terminal-object and hull steps, and found no gap. No external review or formal verification. This is a ZFC consequence of the new finite-orbit type-completion theorem. It does not settle the unrestricted class M.

Use the standing C, D, and M, and put

    C_empty={Y∈C : H(Y_0)=∅},
    D_empty=E(C_empty^op).

Let M_empty consist of the P-objects whose every finite family, including the empty family, lies in a monic D_empty-subobject, and let A_empty be M_empty together with the terminal P-object 1, up to isomorphism.

## 1. The equalizer theorem for empty-character sources

Let Y∈C_empty and let a,b:E(Y)⇉Z with Z∈M. Choose a finite family in their equalizer. In sort 1 take its given observations and their full M_1-orbits. In sort 0 include the given observations and both structural pullbacks of the sort-1 generators, and take full orbits. If needed include constant zero so the family is nonempty.

Form the componentwise observation-type quotient q:Y→Q. It is a K-quotient, Q_0 remains finite-support, |Q_0|≤c, and |Q_1|≤2^c. In each sort the finite generating observations and their right translates separate Q_i. The new general type-completion theorem therefore gives the full monomorphism

    E(Q) ↪ Eq(a,b),

containing the prescribed family. No finite-support assumption on Y_1 is used.

Since q_0 is onto, H(Q_0) embeds in H(Y_0)=∅. The existence of p_Q:Q_0→Q_1 implies H(Q_1)=∅ as well. Hence H(p_Q) is a bijection between empty sets, Q∈C_empty, and the displayed cover is in D_empty.

Consequently Eq(E(Y)⇉Z)∈M_empty. More generally, restricting to a local D_empty-cover of a finite equalized family shows

    A∈M_empty, Z∈M  ⇒  Eq(A⇉Z)∈M_empty.

The local covers just constructed have both ambient carriers bounded by

    K=2^(2^c).

This is a bound on finite-family witnesses, independent of the original Y and of its second sort.

## 2. Products, the terminal object, and directed unions

Nonempty products of M_empty-objects belong to M_empty: choose a local D_empty-cover for the projected finite family in each factor and take their product. Its dual is the coproduct of the corresponding C_empty-objects; its first character space is a nonempty-indexed product of empty sets and hence empty.

Directed unions of M_empty-objects belong to M_empty because a finite family occurs at one stage and its local cover remains monic in the union.

No object of M_empty admits a map from 1. Indeed every Y∈C_empty has Y_0 nonempty. In a monic E(Y)-cover the constant-zero and constant-one elements in sort 0 are distinct. Any M_2-fixed element in a putative M_empty-object could be included in a cover; its lift would be fixed in ω^(Y_0), which is impossible. A map from 1 would supply just such a fixed element.

Adding 1 therefore causes no new equalizer problem: a pair with source 1 and target in A_empty can only have target 1; a pair from M_empty to 1 is identical. Products containing some nonterminal factor reduce to the preceding nonempty-product argument. A directed diagram of monomorphisms in A_empty cannot mix 1 with an M_empty-object: a common upper stage would either admit a forbidden map from 1 or a monomorphism of a nontrivial M_empty-object into 1. Thus A_empty remains directed-union-closed and is closed under all small limits.

## 3. Uniform hulls and reflectivity

Every finite family in a nonterminal A_empty-object has an A_empty-subobject of size at most K by Section 1 applied to the identity pair. Given a set S of its elements, intersect all A_empty-subobjects containing S; small-limit closure puts this hull in A_empty. The hull of a finite family has size at most K, because it lies in a small cover. Directed-union closure identifies the hull of S with the directed union of its finite-subset hulls. Therefore

    |hull(S)|≤max(|S|,K).

The same bound is immediate for the terminal object. For a fixed X, every map X→A with A∈A_empty factors through the hull of its image, of size at most max(|X|,K). There is a set of isomorphism classes of such small presheaves and a set of maps from X to them. This is a solution set for X↓A_empty. Completeness and the usual initial-object argument give a reflection.

Thus A_empty is reflective in P, in ZFC. In particular the empty-character sector, even with arbitrary non-finite-support second sorts, cannot supply the intended P4 counterexample.

## 4. What remains outside this theorem

For the unrestricted problem, finite-seed type completion now supplies E(Q) inside an equalizer. If H(Y_0) is nonempty, H(Q_0) can also be nonempty, and the extensions of its characters need not yet descend to Q_1. Adding all of them may require further first-sort refinement through q_Y and may destroy finite orbit-separation. That unique-extension repair is the remaining step; it is not inferred from the theorem above.
