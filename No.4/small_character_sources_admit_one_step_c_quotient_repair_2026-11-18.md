# Small character spaces admit a one-step C-quotient repair

2026-11-18. Status: PROOF_RECONSTRUCTED. The coordinating agent read and reconstructed the detailed one-step proof; mono_retract also independently reconstructed it and found no gap. This is an internal proof audit, not external review or formal verification. All results are ZFC. This proves equalizer closure for a genuinely characterful restricted source class, not for unrestricted M.

Use the standing categories and c=2^aleph_0. The principal inputs are [continuum Boolean continuity and general finite-seed type completion](continuum_boolean_continuity_and_orbit_separator_factorization_2026-11-18.md).

## 1. The theorem

Let Y∈C with

    |H_1(Y_0)|≤c.

Neither carrier of Y is required to be small, and Y_1 need not be finite-support or Ω-cogenerated. For any pair

    a,b:E(Y)⇉Z,       Z∈M,

every finite family in Eq(a,b) has a monic D-cover inside that equalizer. The cover can be chosen E(Q) with

    |Q_0|≤c,       |Q_1|≤2^c,
    |E(Q)_i|≤2^(2^c).

Thus Eq(a,b)∈M, with a uniform bound on its finite-family witnesses.

The empty-character case is already proved in [the empty-character theorem](empty_character_monic_local_class_reflective_2026-11-18.md). Below assume X=H_1(Y_0) is nonempty. Then both sorts of Y have no M_1-fixed point, so continuum Boolean continuity applies to both component maps a_i,b_i.

## 2. Two elementary bounded-completion facts

### Continuous evaluation profiles on a small compact spectrum

Finite support makes X a compact Stone space. Every y∈Y_0 gives a continuous function

    ev_y:X→Ω,       h↦h(y).

If |X|≤c, there are at most c such continuous functions. Indeed a compact Hausdorff space of cardinality at most c has a base of size at most c; each clopen is a finite union of basic opens, and every continuous map to discrete Ω has finite image. Hence

    |Cont(X,Ω)|≤c.                                     (1)

This bounds the number of evaluation profiles even when Y_0 itself has arbitrarily many observationally indistinguishable points.

### Completing a small quotient from at most c common observations

Suppose S has no fixed point and a,b:Ω^S⇉Z_i agree on a family F of at most c functions. Let q:S↠Q be the quotient by their value profiles, and suppose |Q|≤c.

For every q-point, its fiber is an intersection of at most c observation equality sets. Continuum meet preservation makes its indicator common under a,b. Every subset of Q has at most c points, so continuum join preservation then makes the indicator of its full inverse image common. Unary fiber indicators and left joint separation give

    a(fq)=b(fq)       for every f:Q→Ω.                  (2)

This step uses no monic cover of the entire observation family. The c-meets and c-joins are the image suprema and infima furnished by the continuity theorem.

## 3. Add all common characters at once

Choose the finite equalized seed. Let O_1 be the full right orbits of its sort-1 functions. Let O_0 be the full right orbits of the sort-0 functions and of both structural pullbacks of the chosen sort-1 functions. Add constant zero when a finite generating list is empty. Both O_i have size at most c.

The initial sort-0 observation quotient has cardinality at most c, by finite support and the countable dense-submonoid argument.

Now define the set of **all common first-sort characters**

    L={h∈X:a_0(h)=b_0(h)}.

It has size at most c. Define q_0:Y_0↠Q_0 by the observations O_0 together with L. These observations define an M_1-congruence: O_0 is orbit-closed, while for a character h, equality of h-values is preserved by the M_1-action.

The carrier of Q_0 has size at most c. Its profile records an initial type, of which there are at most c, together with the restriction of ev_y to L. By (1) the latter has at most c possibilities. Thus Q_0 embeds as a set into a product of two sets of size at most c.

All defining observations are common under a_0,b_0. Apply (2) to obtain the entire first full power:

    a_0(fq_0)=b_0(fq_0)       for every f:Q_0→Ω.        (3)

Under the injective pullback H_1(Q_0)→X, we have the exact equality

    H_1(Q_0)=L.                                        (4)

One inclusion follows because every h∈L was included among the defining observations and descends equivariantly through q_0. Conversely, every character of Q_0 is one of the functions covered by (3), so its pullback is common.

In particular L is a closed subspace of X: H_1(Q_0) is compact and its embedding in X is continuous. No closedness of L was assumed beforehand.

## 4. The character extensions respect both structure arrows

For h∈L let h̃:Y_1→Ω be its unique extension along p_Y. Its images a_1(h̃),b_1(h̃) are balanced and have the same p_Z-image a_0(h)=b_0(h). E(σ)-orthogonality of Z therefore gives

    a_1(h̃)=b_1(h̃).                                   (5)

Consequently h̃q_Y is also a common first-sort character, hence belongs to L. Thus L is invariant under the character dynamics

    h↦h̃q_Y.

Define q_1:Y_1↠Q_1 by the observations O_1 and all h̃ with h∈L. There are at most c observations, and therefore |Q_1|≤Ω^c=2^c.

Their p_Y-pullbacks and q_Y-pullbacks factor through q_0. This is true for O_1 by the initial choice of O_0, and for h̃ by h∈L and h̃q_Y∈L. Hence q_0,q_1 form a componentwise-surjective K-map

    q:Y↠Q.

The quotient Q_0 remains finite-support. Every character of Q_0 corresponds by (4) to an h∈L, and its extension h̃ is one of the observations defining Q_1, so it descends to Q_1. This proves surjectivity of H_1(p_Q).

Injectivity is inherited from Y: pull two characters of Q_1 back along the onto q_1, use their equality after p_Y and injectivity of H_1(p_Y), and descend again. Thus

    Q∈C.                                               (6)

This is the actual C-surjectivity repair. It uses all common characters once, rather than an unbounded iteration or an assumed coreflector for C.

## 5. The second full power is also equalized

It remains to prove that E(q) lands in the equalizer in sort 1.

If L is empty, Q is exactly the initial finite-orbit observation quotient. The general finite-seed type-completion theorem supplies the entire E(Q) inside the equalizer directly.

Assume L is nonempty. By (4), Q_0 has no fixed point. Since |Q_0|≤c, choose a packed countable separator z_0:Q_0→Ω. Equation (3) makes its pullback a common first-sort element.

Suppose, contrary to the claim, that some f:Q_1→Ω has distinct images under a_1E(q)_1 and b_1E(q)_1. Choose a monic D-cover j:E(T)↪Z containing:

- the common image of z_0q_0;
- the common images of the original finite sort-1 seed;
- the two images of fq_1 whose equality is in question.

The strong one-sort small-source factorization argument places the whole common map Ω^(Q_0)→Z_0 inside j_0. Every h∈H_1(Q_0)=L therefore has its first image in the cover. Since T∈C and Z is E(σ)-orthogonal, its unique balanced second extension (5) lies in j_1 as well.

Thus all observations defining Q_1 have common images in this one cover: the original seed orbits by ambient closure, and all characters by unique extension. Their number is at most c.

Choose an atom of E(T)_1 at which the two f-lifts differ, and let w≠0 be its image. Reading the common observations gives a profile p. Apply continuum meet preservation to the two maps

    Ω^(Q_1)⇉Z_1.

It applies because Q_1 has a character, hence no fixed point. The full observation profile fiber is empty or a singleton, since these observations define Q_1. It cannot be empty because w is nonzero. Both images of f must therefore equal the same source value on w, a contradiction.

This proves all of E(Q) is contained in Eq(a,b). The map E(q) is monic because q is componentwise onto, and it contains the original seed. Together with (6) and the cardinal estimates, this proves the theorem.

## 6. Exact scope

The argument permits arbitrarily large carriers and an arbitrary second sort. Its restriction is the cardinality of the **whole first character space**, not finite support on the second sort and not a global continuity assumption on the character dynamics.

The class of these source witnesses is not asserted to be closed under arbitrary coproducts: the corresponding character space is a product, whose cardinality can exceed c. Consequently no reflection theorem for their entire monic-local class is inferred here.

The unrestricted problem still allows |H_1(Y_0)|>c. In that situation the simultaneous common-character family can be larger than the proved global Boolean-continuity bound, and (1) need not bound the evaluation-profile quotient by c. This note does not claim to repair that case.
