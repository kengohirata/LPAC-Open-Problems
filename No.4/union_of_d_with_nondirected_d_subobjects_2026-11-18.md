# A directed union of D whose D-subobjects are not directed

2026-11-18. Status: explicit construction; the union presentation is ZFC,
and the nonexistence of a common D-subobject uses N. No (NC) input is used.
This rejects the proposed D-image-bounded class L by failure of union
closure. It does not reject the mono-factorization class M or solve P4.

Use the actual presheaf category P, Isbell functor E, and D=E(C^op).
Write U(D) for the class of objects that are one directed union of
D-subobjects. This notation does not assume that U(D) is itself closed
under iterated directed unions.

## 1. The scalar quotient and the actual presheaf

Put I=omega_1 and let

    Q=Omega^I / (agreement outside a countable subset),
    pi:Omega^I→Q.

This is an M_2-set under postcomposition. Its finite pointwise operations
are well-defined, since a finite union of countable exceptional sets is
countable. Put

    A=Omega^I × Q.

Define Z in the actual two-sort presheaf category by taking A in both
sorts, trivial right M_1-actions, and both diagram arrows equal to the
identity of A.

For any set S, let R(S) be the K-object having S in both sorts with
trivial left M_1-actions and p=q=id. It belongs to C: its first sort is
finite-support, and H_1(p) is the identity. Hence E(R(S)) belongs to D;
it has Omega^S in both sorts, trivial right M_1-actions, and identity
diagram arrows.

## 2. Z is a directed union of cyclic D-subobjects

Take h=(f,[g]) in A, choosing a representative g:I→Omega. Set

    S_h=im(f) ∪ {n∈Omega : g^(-1)(n) is uncountable}.

For m,m'∈M_2,

    m h=m' h  iff  m|_(S_h)=m'|_(S_h).

For the first component this is immediate. In the second component,
disagreement is the union of those fibers g^(-1)(n) for which
m(n)≠m'(n). This union is countable exactly when none of its fibers is
uncountable: there are only countably many possible values n.

Every map S_h→Omega extends to an endomorphism of Omega. Therefore the
orbit M_2 h is isomorphic to Omega^(S_h) as an M_2-set. Taking that orbit
in both sorts gives a D-subobject E(R(S_h)) of Z.

These cyclic subobjects form a directed family. For h_1,h_2∈A, choose a
bijection b:Omega^2→Omega and define h=b(h_1,h_2) componentwise, using
representatives in Q. This is independent of the chosen representatives.
The two unary coordinate-decoding maps recover h_1,h_2 from h, so their
whole M_2-orbits are contained in M_2 h. Every element belongs to its own
orbit. Consequently

    Z is a directed union of D-subobjects;
    in particular Z∈U(D)⊆M.

This part of the construction is ZFC.

## 3. Two larger D-subobjects with no common D-upper bound

Split I into two uncountable sets B and I\B, and choose a permutation
sigma of I interchanging them. There are two monic maps E(R(I))→Z:

    a(f)=(f,pi(f)),
    b(f)=(f,pi(f∘sigma)).

Use the same map in both sorts. Their images, denoted D_a and D_b,
are D-subobjects. They differ: for f=chi_B, the two second coordinates
are pi(chi_B) and pi(chi_(I\B)), which are unequal.

**Proposition (N).** No D-subobject of Z contains both D_a and D_b.

Proof. More strongly, suppose j:E(Y)↪Z contains D_a. Consider sort 0,
and write

    j_0=(v,w):Omega^(Y_0)→Omega^I×Q.

The inclusion of D_a gives a map t:Omega^I→Omega^(Y_0) with

    v t=id,    w t=pi.

Under N, scalar Isbell full faithfulness gives set maps

    u:I→Y_0,    q:Y_0→I,

such that v is precomposition with u and t is precomposition with q.
The equation v t=id says q u=id_I.

All M_2-maps between the scalar algebras used here preserve the derived
finite pointwise operations. One can verify this using a fixed bijection
Omega^2→Omega and its two unary decoders: uniqueness of tuple coding
forces preservation of pairing, and every finite operation is a unary
operation after such a code. In particular w preserves the order on
binary-valued elements.

For each y∈Y_0, the pointwise inequality

    chi_y ≤ chi_(q(y))∘q

therefore gives

    w(chi_y) ≤ w(t(chi_(q(y)))) = pi(chi_(q(y))) = 0.

Thus w(chi_y)=0 for every y. If y were outside im(u), we would also have
v(chi_y)=0. This would make j_0(chi_y)=j_0(0), contradicting monicity.
Hence u is surjective. Since q u=id, u and q are inverse bijections.

It follows that t is an isomorphism and the entire sort-0 image of j is
exactly the graph of pi. That image cannot also contain the distinct
sort-0 graph of pi∘sigma*. This proves the proposition. □

Thus **the poset of all D-subobjects of an object in U(D) need not be
directed**. The directed cyclic family from Section 2 is not cofinal
among all D-subobjects: in particular it does not dominate D_a or D_b.
This is precisely the distinction between covering finite families of
elements and containing entire, possibly much larger, D-subobjects.

The proposition also proves Z∉D under N: otherwise Z itself would be a
common D-upper bound.

## 4. The stronger D-image condition fails directed-union closure

Consider the proposed class

    L={Z∈H_fg : every map D→Z, D∈D,
                  has image contained in some D-subobject of Z}.

Every D-object belongs to L, using its identity subobject as the bound.
But the Z above does not belong to L under N. Indeed, there is an
explicit componentwise surjection from a D-object,

    E(R(I⊔I))→Z,
    (f,g)↦(f,pi(g)).

If its image were contained in a D-subobject of Z, that subobject would
be all of Z, forcing Z∈D, contrary to Section 3.

Consequently Z∈U(D)\L, and L is not closed under directed unions of
monomorphisms: Section 2 presents Z as a directed union of D-objects,
all of which lie in L.

This proves no inclusion between L and U(D) beyond the displayed
noncontainment. It also does not prove that one-step U(D) fails
directed-union closure, or that U(D)=M. Those remain separate questions.
