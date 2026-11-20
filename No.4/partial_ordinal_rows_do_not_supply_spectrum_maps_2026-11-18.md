# Partial ordinal rows do not automatically supply maps of compact spectra

2026-11-18. Status: explicit ZFC calculation. This is a counterexample to an intermediate extension step, not a nonlifting monomorphism E(Y)→W and not a Problem 4 counterexample.

Consider the ordinal template on [0,2]:

    R_0=R_1=omega^3,
    p_R=id,
    q_R(a_0,a_1,a_2)=(a_1,a_2,a_2).

Write sigma=q_R. Both sorts carry the diagonal postcomposition action of M_1=End(omega). Let

    f=(0,0,1),    g=(0,1,1),
    A=M_1 f ∪ M_1 g ⊂ omega^3.

The two orbits are

    M_1 f={(a,a,b):a,b∈omega},
    M_1 g={(a,b,b):a,b∈omega}.

Their intersection consists exactly of the constant triples. Moreover sigma(f)=g and sigma(g)=(1,1,1), so A is sigma-stable.

Thus

    Y=(A --id,sigma--> A)

is a K-subdiagram of R and belongs to C: A is finite-support and H_1(id) is bijective. The identity on this partial row Y→Y is a genuine K-map, and its first-sort spectrum T=H_1(A) is compact Hausdorff.

## 1. The spectrum has one extra point

An equivariant map A→omega can choose h(f) and h(g) independently in {0,1}. Each choice extends uniquely on the respective orbit, because that orbit is isomorphic to omega^2. The extensions agree on the common constant triples. Therefore

    H_1(A) ≅ {0,1}^2.

The three coordinate evaluations inherited from omega^3 yield respectively

    (h(f),h(g))=(0,0), (0,1), (1,1).

The fourth equivariant map h_* has

    h_*(f)=1,    h_*(g)=0.

It does not extend to an equivariant map omega^3→omega: every such map is one of the three coordinate projections, and none gives (1,0).

Equivalently, there is no map l:H_1(A)→[0,2] satisfying

    h(a)=a(l(h))    for every h∈H_1(A), a∈A.

At h=h_*, this would demand a coordinate where f has value 1 and g has value 0, and no such coordinate exists.

## 2. Compactness and the C condition do not repair this

The induced dynamics on H_1(A) is

    (a,b)↦(b,1).

The three ordinal evaluation points form the chain

    (0,0)→(0,1)→(1,1)→(1,1),

while the additional point (1,0) maps to (0,1). All spaces here are finite discrete, so there is no topological pathology. Both the ambient row R and the partial row Y belong to C, and the partial row is closed under all actual M_1 and diagram operations.

Nevertheless, pulling an arbitrary h∈H_1(Y_0) back along the partial row map does not necessarily give an evaluation on the whole ordinal row. Hence compactness of H_1(Y_0) and naturality on a partial row do not by themselves construct the maps l_t:H_1(Y_0)→[0,lambda] required by the paired-stage obstruction.

This identifies a precise missing hypothesis in a proposed extension from disjointified singleton-indicator rows to total spectrum maps. The example does not show that these partial-row data arise from an actual monomorphism into the large tail quotient. Such a monomorphism has additional full-power compatibility, and exploiting that extra compatibility remains a possible route.

The same example also illustrates why completing an observationally separated M_1-set to all continuous functions on its spectrum is not a quotient operation. A contains the two coordinate families above but omits functions depending essentially on both independent spectrum coordinates, such as their Boolean exclusive-or.
