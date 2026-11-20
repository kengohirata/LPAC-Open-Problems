# An increasing sequence of equationally closed spectra has a nonclosed limit under ecl

2026-11-18. Status: PROOF_RECONSTRUCTED; the coordinating agent read and reconstructed the complete example, including the partial-operation explanation, and found no gap. No external review or formal verification. This is an explicit ZFC counterexample to a proposed omega-stage stabilization step. The source M_1-set is countable and finite-support, and its character space is compact metrizable.

For an M_1-set S and K⊂H_1(S), write

    ecl(K)={h∈H_1(S): h(s)=h(t) whenever
                        k(s)=k(t) for every k∈K}.

Equivalently, ecl(K) is the character space of the quotient of S by equality of its K-evaluation profiles, viewed as a subset of H_1(S).

The example below disproves

    ecl(closure(⋃_n K_n))=closure(⋃_n K_n)

even when K_n is an increasing sequence of compact ecl-closed subsets.

## 1. The finite-support M-set and its compact spectrum

Take the coproduct

    S=Ω²_x ⊔ Ω²_y ⊔ ⨿_(m<ω) Ω³_m,

with diagonal M_1=End(Ω) actions on each summand. It has countable carrier and every point is finite-support. The equivariant maps Ω^r→Ω are exactly the r coordinate projections. Therefore

    X=H_1(S)={0,1}²×{0,1,2}^ω,

with its product Stone topology. Write a point as (x,y,(z_m)).

Let

    R={(0,0),(0,1),(1,0)},
    code(0,0)=0, code(0,1)=1, code(1,0)=2.

Define

    K_n={ (x,y,z)∈X : (x,y)∈R and
                         z_m=code(x,y) for every m≥n }.

## 2. Each K_n is equationally closed

In Ω²_x choose the element u_x=(0,1), and in Ω²_y choose u_y=(0,1). In the m-th Ω³ summand choose

    a_m=(0,0,1),       b_m=(0,1,0).

The subset K_n is exactly the simultaneous solution set

    h(u_x)=h(a_m),       h(u_y)=h(b_m)       (m≥n).

The two values at coordinate z_m record precisely the three allowed pairs in R. Thus K_n is an intersection of character-equality clopens, and ecl(K_n)=K_n. Each K_n is compact, and K_n⊂K_(n+1).

## 3. The closure of their union

The topological closure is

    L=closure(⋃_nK_n)=R×{0,1,2}^ω.

One inclusion follows because R is closed in the first two coordinates. Conversely, a basic neighborhood of a point of L specifies only finitely many z-coordinates. Choose n beyond those coordinates, retain their assigned values, and set every later z_m to code(x,y). This gives a point of K_n in that neighborhood.

The subset L is proper: it omits every point with (x,y)=(1,1).

## 4. Nevertheless ecl(L)=X

Consider two elements s,t∈S whose evaluations agree at every point of L.

If they belong to the same summand, every projection of that summand occurs among the characters in L. Their coordinate tuples must therefore be identical, and their evaluations agree on all of X.

If they belong to the x- and y-summands, write their two coordinates as (a_0,a_1) and (b_0,b_1). Equality on the three corners of R gives

    a_0=b_0,       a_0=b_1,       a_1=b_0.

Hence all four values are equal, so the evaluations also agree at the missing fourth corner.

If one belongs to an Ω³ summand and the other to a different summand, the corresponding two character coordinates vary independently on L. Equality forces both tuples to be constant with the same value. Again their evaluations agree everywhere on X.

Thus every character equality holding on L already holds on X. It follows that

    ecl(L)=X≠L.

In particular equational closure does not commute with topological closure of an increasing countable union of its closed subsets.

## 5. The finite partial-operation explanation

Let D⊂Ω³ consist of triples with at least two equal entries. Define the partial minority operation μ:D→Ω to return the exceptional entry when exactly two agree, and the common value when all three agree. D is M_1-stable and μ is equivariant: postcomposition either preserves the two-value pattern or collapses it to a constant triple.

It induces a partial pointwise operation on H_1(S), defined when the three character values at every element of S lie in D. Whenever defined, its result is again an equivariant character. Any ecl-closed subset is closed under this partial operation, since its defining equalities are preserved pointwise.

Now take the following three points of L, all with every z_m=0:

    a=(0,0,0,0,...),
    b=(0,1,0,0,...),
    c=(1,0,0,0,...).

The partial operation is defined on (a,b,c): in each Ω² summand two of the three characters choose the same coordinate, and in each Ω³ summand all three choose coordinate 0. Its result is

    μ(a,b,c)=(1,1,0,0,...),

which lies outside L.

There are approximating triples a_n,b_n,c_n all belonging to K_n: keep the first n z-coordinates zero and thereafter use the respective codes 0,1,2. These triples converge to (a,b,c), but μ is undefined on every approximating triple. At any tail summand, its values on the element (0,1,2) are three distinct numbers.

The domain of this induced partial operation is closed but need not be open. Thus continuity of a partial operation does not make topological closure of a directed union of partial subalgebras into a partial subalgebra. This is the concrete missing step in the proposed stabilization argument.

The example does not contradict the separate weight bound: both L and ecl(L)=X still have countable weight. Nor does it by itself prove failure of any C-quotient repair or of No.4. It rules out this specific omega-limit commutation principle.
