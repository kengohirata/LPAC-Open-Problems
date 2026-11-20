# Independent audit: the empty-character local class is reflective

2026-11-18. Status: INTERNAL_PROOF_AUDIT_PASSED. mono_equalizer independently reconstructed the argument in [the empty-character reflection note](empty_character_monic_local_class_reflective_2026-11-18.md), using the new general finite-orbit type-completion theorem. No gap was found. This is not external peer review or formal verification.

## Scope and input

The input used is: for any Y∈C, any pair E(Y)⇉Z with Z∈M, and any finite equalized family, its componentwise finite-orbit observation quotient q:Y↠Q has a monic E(Q) inside the equalizer. Also Q_0 is finite-support with |Q_0|≤c and |Q_1|≤2^c.

The argument for this input uses c-continuity for M-target maps whose source has countably many fixed points, followed by the finite-orbit separator argument. The countably-fixed-point reduction and both arguments were separately reconstructed in the active research discussion. The audit here does not assume a general equalizer theorem for M.

As usual, “every finite family” includes the empty family. This convention excludes vacuous membership of the initial presheaf and agrees with testing all ambient finitely generated sources, including the initial source.

## 1. Empty character spaces survive the relevant quotient

If H(Y_0)=∅ and q_0:Y_0↠Q_0 is onto, precomposition embeds H(Q_0) into H(Y_0), so H(Q_0)=∅. The map p_Q induces a function H(Q_1)→H(Q_0), forcing H(Q_1)=∅ as well. Thus Q∈C_empty without any additional extension argument.

The finite type-completion cover is consequently a D_empty-cover. Restricting a pair with source in M_empty to any local D_empty-subobject establishes equalizer closure for M_empty sources and M codomains. This uses no full faithfulness of E and no N hypothesis.

The cardinal bound on the **ambient presheaf witness** E(Q) is 2^(2^c): the dual second carrier Q_1 has size at most 2^c, and ω^(Q_1) has size at most 2^(2^c). These two bounds must not be confused.

## 2. Terminal adjunction and limits

Every Y∈C_empty has Y_0 nonempty, because H(∅) is a singleton. Hence E(Y)_0 has distinct constant-zero and constant-one elements and no M_2-fixed point.

If an M_empty-object had an M_2-fixed element in sort 0, a monic local cover of that element would lift it to an M_2-fixed function in E(Y)_0, a contradiction. In particular there is no P-map 1→A for A∈M_empty. Also A contains a local E(Y)-subobject, so A→1 cannot be monic.

These facts handle every case after adding the terminal object:

- A pair with source 1 can only have target 1.
- A pair from M_empty to 1 is identical.
- Nonterminal factors determine a product; if there are none, it is 1.
- A directed mono diagram cannot contain both a terminal stage and an M_empty-stage, because a common upper stage would contradict one of the two facts above.

Nonempty products and directed unions inside M_empty follow from local monic covers. Thus adjoining 1 preserves the required unions and gives all small limits.

## 3. Hulls and the solution set

P is well-powered. Therefore, for a fixed A and seed set S, the intersection of all A_empty-subobjects of A containing S is a set-indexed limit, and belongs to A_empty. The collection is nonempty because it includes the identity subobject of A.

For a finite seed, the hull lies inside a witness of size at most K=2^(2^c), so it has that bound. The hulls of finite subsets of S form a directed system of subobjects. Their union belongs to A_empty, contains S, and lies in hull(S). Minimality gives equality with hull(S). Therefore

    |hull(S)|≤max(|S|,K).

For a fixed presheaf X, every map X→A factors through a subobject of this bounded size. Presheaves of bounded carrier size, their structure maps for the fixed small signature, and maps from X into them form a set up to isomorphism. This gives the required solution set. The comma category is complete because A_empty is limit-closed in P; the usual weak-initial-set/initial-object argument therefore gives a reflection.

No class-sized intersection, class-sized product, or unproved accessibility assertion is needed. The terminal case is immediate and has the same bound.

## Conclusion

Subject to the stated new type-completion input, A_empty=M_empty∪{1} is reflective and closed under all small limits and directed unions in ZFC. This excludes the empty-character sector from the intended No.4 counterexample search, including witnesses with arbitrary second sorts. It does not settle the nonempty-character case or the unrestricted M.
