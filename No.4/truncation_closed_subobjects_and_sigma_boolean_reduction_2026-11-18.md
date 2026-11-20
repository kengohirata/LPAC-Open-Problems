# Truncation-closed subobjects and a sigma-Boolean reduction

2026-11-18. Status: PROOF_RECONSTRUCTED; independent audit requested. This supplies an additional condition satisfied by actual equalizers, and proves a relative subobject theorem for countable dual sources. It does not prove general equalizer closure of M.

Fix e_n:Omega->Omega, n>=1, fixing 0,...,n-1 and sending every larger integer to 0. These act on the left by postcomposition. Say A subset Z is **truncation-closed** if, in each sort,

    [e_n z belongs to A for every n] implies z belongs to A.

This condition concerns membership in the subobject, not the first-sort FS-separation axiom, which concerns equality after the right actions by e_n.

## 1. Actual equalizers have this property

Let a,b:Z->W, where W is left-joint-separated for (e_n). If e_n z belongs to Eq(a,b) for every n, then

    e_n a(z)=a(e_n z)=b(e_n z)=e_n b(z)

for every n. Left separation gives a(z)=b(z), so z belongs to the equalizer.

In particular the [finite-image intrinsic subobject](finite_image_intrinsic_subobject_counterexample_2026-11-18.md) fails this necessary condition: all e_n id are finite-image, while id is not. More generally, the finite-image inclusion Fin(Y_i,Omega) subset Omega^(Y_i) is epic relative to all left-joint-separated targets: agreement on finite-image functions forces agreement after every truncation and hence on every function.

## 2. Truncation-closed subobjects of a full power

Let A be a subpresheaf of E(Y) which contains the constant functions in both sorts and is closed under finite pointwise operations. The latter follows, for example, from inherited unique finite tuple coding. For each sort put

    B_i={U subset Y_i : chi_U belongs to A_i}.

**Proposition.** A is truncation-closed if and only if each B_i is a countably complete Boolean subalgebra of P(Y_i) and

    A_i={f:Y_i->Omega : f^(-1)({n}) belongs to B_i for every n}.

Thus such A are precisely the objects of Omega-valued partitions Gamma(B_i) for sigma-Boolean subalgebras of the coordinate powersets, with the inherited right actions and structural maps.

Proof of the forward implication. Finite-operation closure makes B_i a Boolean algebra. For U_n in B_i, define

    h(y)=0 if y belongs to none of the U_n,
         1+min{n:y belongs to U_n} otherwise.

Each e_N h is a finite pointwise operation of chi_(U_0),...,chi_(U_(N-2)), so belongs to A_i. Truncation closure gives h in A_i, and the nonzero indicator of h gives chi_(union_n U_n) in A_i. Hence B_i is countably complete.

If f belongs to A_i, its fibers belong to B_i by unary indicators. Conversely, if all fibers belong to B_i, every e_N f is a finite operation of the first finitely many fiber indicators, so lies in A_i. Truncation closure recovers f.

For the reverse implication, if every e_N f has B_i-measurable fibers, then for each k>=1 the fiber f=k is the fiber e_N f=k for N>k. The zero fiber is the complement of the countable union of positive fibers. Thus all fibers of f lie in B_i, so f belongs to A_i. □

The inherited inverse-image maps along the right M_1 actions and along p_Y,q_Y preserve these Boolean subalgebras and all their countable joins. This is therefore a reduction of the whole diagram, not only of its underlying sets.

The constant-function assumption is explicit: empty sorts can satisfy some of the listed intrinsic axioms vacuously and need not be full powers. Actual equalizers between the nonempty finite-tuple objects considered here contain the shared constant functions.

## 3. The countable-dual subobject theorem

**Theorem (ZFC).** Let Y belong to C, with both Y_i countable. Let A subset E(Y) contain the constants, be closed under finite tuple coding, be truncation-closed, and be E(sigma)-orthogonal. Then

    A=E(Q)

as a subobject of E(Y), for a componentwise quotient Y->Q with Q in C. In particular A belongs to D and M.

Proof. By Section 2 each B_i is a countably complete Boolean subalgebra of P(Y_i). On Y_i identify points having the same membership pattern in B_i. Each equivalence class belongs to B_i: for a fixed y, separate it from every point not equivalent to it and take the countable intersection of the chosen separating sets. Since Y_i is countable, every union of equivalence classes is a countable union and also belongs to B_i. Thus B_i is the full powerset algebra of the quotient Q_i, pulled back to Y_i.

Stability of B_i under the right-action inverse images makes the equivalence relation an M_1-congruence. Stability under the structural inverse images makes the quotient maps into a K-map Y->Q. Section 2 identifies A with E(Q).

The sort Q_0 is finite-support, as a quotient of the finite-support M_1-set Y_0. Orthogonality of E(Q) to E(sigma) is exactly bijectivity of H_1(p_Q), using the direct countable-index evaluation correspondence for E(B) and E(U). Hence Q belongs to C. No N or NC is required. □

In particular, equalizers with countable-dual source E(Y) and target in H_fg belong to D: finite tuple closure, truncation closure, and E(sigma)-orthogonality are all inherited by that equalizer.

## 4. The remaining uncountable obstruction

For uncountable Y_i, a countably complete Boolean subalgebra of P(Y_i) need not contain the intersections defining its point-pattern atoms, nor all unions of its atoms. The conclusion B_i=P(Q_i) therefore does not extend formally.

The general monic-cover question is now concrete. For a finite seed and its M_1-orbits in Gamma(B_i), can one find a K-quotient q:Y->Q with Q in C such that every inverse image q_i^(-1)(U), U subset Q_i, belongs to B_i and the seed functions factor through q? Such a quotient gives the required full-power D-subobject of A. Sigma-completeness alone gives only countable unions, whereas a monic full-power witness requires all unions of its partition blocks.

The E(sigma)-condition constrains balanced Omega-valued partitions and supplies their unique extension between the sorts. It does not by itself assert that these sigma-Boolean algebras contain the required complete atomic subalgebras. This is the precise gap remaining after the finite-image counterexample is excluded by truncation closure.
