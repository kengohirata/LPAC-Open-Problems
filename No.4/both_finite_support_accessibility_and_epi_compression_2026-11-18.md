# Both-finite-support witnesses admit uniformly bounded epimorphic compression

2026-11-18. Status: PROOF_RECONSTRUCTED; independently checked by a second research agent, not externally reviewed or formally verified. This proves a bounded-witness theorem for a proper restricted class of C-objects, not closure of the general mono-factorization candidate M. The compression theorem uses ZFC, Stone duality, and cited accessibility theorems. Only the explicitly conditional boundary corollary in Section 5 uses N and the adopted No.1 factorization lower bound.

Write c=2^aleph_0 and kappa=aleph_1. Let FS be the full category of finite-support M_1-sets, where M_1=End(omega). Let

    K_bfs=FS^J,
    C_bfs={Y in K_bfs : H_1(p_Y) is bijective}.

Thus C_bfs consists exactly of those Y in the original C for which Y_1 is also finite-support. Unlike the original C, this restricted category is locally presentable.

## 1. The finite-support category is locally finitely presentable

FS is closed under ambient small colimits. An element in a colimit is represented by an element of one stage, and any finite support of that representative remains a support. Thus its colimits are computed in M_1-Set.

The countable family

    G_n=omega^n,    1<=n<omega,

with diagonal action is a strong generator. If a in A has a nonempty finite support S={s_1,...,s_n}, define G_n→A by sending a tuple (t_1,...,t_n) to m a for any m with m(s_j)=t_j. Support makes this independent of m. Its image contains a. Empty supports can always be enlarged to nonempty supports.

For completeness, suppose f:A→A' induces bijections on Hom(G_n,-) for every n. The preceding maps show that f is surjective. If f(a)=f(b), take one nonempty finite support containing supports of both a and b. The associated two maps G_n→A have identical composites with f, so are equal; evaluating at the support tuple gives a=b. Hence f is an isomorphism.

Each G_n is a retract of the free M_1-act M_1. Choose a rank-n idempotent e_n:omega→omega. The left ideal M_1 e_n is isomorphic to G_n, and right multiplication by e_n is an equivariant retraction M_1→M_1 e_n. Hence G_n is finitely presentable and projective in M_1-Set, and remains so in FS because the inclusion creates colimits. The small-strong-generator criterion makes FS locally finitely presentable. See Adamek–Rosicky, *Locally Presentable and Accessible Categories*, Theorem 1.20 ([publisher's chapter summary](https://www.cambridge.org/core/books/abs/locally-presentable-and-accessible-categories/locally-presentable-categories/7C005833BDB95AA2D19654FE35806077)).

In fact the G_n are small-projective: Hom(G_n,A) identifies with the fixed points of e_n on A, and this idempotent fixed-point functor preserves all colimits. Surjectivity of the colimit comparison follows by replacing a representative a by e_n a; injectivity follows by applying e_n to any zigzag witnessing equality in a set-colimit.

The category G of the G_n is countable: Hom(G_n,G_m) consists of m-tuples of coordinate projections and has n^m elements. The canonical G-diagram of a countable FS object A is countable, since each Hom(G_n,A) injects into A by evaluation at a generating tuple. This diagram has colimit A. Directly, all elements occur. Given representatives x in G_n and y in G_m with the same image in A, enumerate a finite set T containing all coordinates of x and y. Coordinate projections G_|T|→G_n and G_|T|→G_m send the generating tuple enumerating T to x and y. Their composites into A agree on that generating tuple and therefore agree everywhere. This gives a common canonical-diagram object identifying the two representatives.

It follows that FS objects with countable carrier are aleph_1-presentable. Conversely, aleph_1-presentables are retracts of countable colimits of the G_n and therefore have countable carrier. There are at most c isomorphism classes of these objects, since there are at most c countable diagrams in the countable category G.

The same conclusions hold for K_bfs=FS^J. Its aleph_1-presentables have countable carriers, and there are at most c isomorphism classes: J is finite and maps between countable underlying sets have at most c possibilities.

## 2. A Boolean-algebra functor detects the C condition

For A in FS, give H_1(A)=Hom_(M_1)(A,omega) the subspace topology from omega^A, with omega discrete. Choose a nonempty finite support S_a for every a in A. Any equivariant h:A→omega satisfies h(a) in S_a: an element outside S_a can be moved by a selfmap fixing S_a, while h(a) must be fixed by every such selfmap.

Consequently H_1(A) is a closed subspace of the compact product of finite discrete sets product_a S_a. Closedness is given by the equations h(m a)=m(h(a)). Thus H_1(A) is a Stone space, allowing the empty Stone space.

Put

    B(A)=Clop(H_1(A)),

allowing the degenerate Boolean algebra. This is a covariant functor FS→BA: an equivariant map induces a continuous map of H-spaces in the opposite direction, and then inverse image on clopens.

The functor H_1 takes any small colimit in FS to the corresponding limit of Stone spaces. The usual bijection of Hom-sets is continuous, and is a continuous bijection between compact Hausdorff spaces, hence a homeomorphism. Stone duality therefore shows that B preserves all small colimits.

Every clopen subset of H_1(A) is a finite union of basic finite-coordinate cylinders: it is open and compact. Hence

    |B(A)| <= max(aleph_0,|A|).

In particular B takes kappa-presentables of FS to kappa-presentables of BA: for countable A, B(A) is countable, and a countable Boolean algebra has a countable presentation. The functor B is strongly kappa-accessible and preserves countable-chain colimits.

Since H_1(p_Y) is a continuous map between compact Hausdorff spaces,

    H_1(p_Y) bijective  iff  B(p_Y) is an isomorphism.

This is precisely where finite support on Y_1 is used.

## 3. C_bfs is locally kappa-presentable

Start with K_bfs. Form the inserter whose objects are pairs

    (Y,v),    v:B(Y_1)→B(Y_0).

Impose the two equations

    v B(p_Y)=id_(B(Y_0)),
    B(p_Y) v=id_(B(Y_1)).

The resulting category is equivalent to C_bfs, because the inverse is unique and its naturality follows from naturality of B(p).

Apply Positselski, *Notes on limits of accessible categories*, Theorem 4.1 (inserter) and Theorem 3.1 (equifier), with the smaller chain cardinal lambda=aleph_0 and kappa=aleph_1 ([author's paper, arXiv:2310.16773v3](https://arxiv.org/pdf/2310.16773)). The participating functors preserve kappa-filtered and countable-chain colimits and take kappa-presentables to kappa-presentables, as proved above. The inserter and successive equifiers have these colimits created by the forgetful functors. Their kappa-presentable objects have kappa-presentable underlying objects.

It follows that C_bfs is kappa-accessible, and its kappa-presentable objects have countable carriers. It has all small colimits, computed in K_bfs, since B preserves colimits and a colimit of a diagram of isomorphisms is an isomorphism. Therefore C_bfs is locally kappa-presentable.

Choose a skeleton G of its kappa-presentables. Section 1 gives

    |Ob G| <= c,    |G_0|+|G_1| <= aleph_0 for G in G.

## 4. Explicit bounded epimorphic quotients

Let Y in C_bfs and let g:Y→S be any K-map, where the total carrier of S has cardinality at most c. Express Y as a small kappa-filtered colimit of G-objects,

    Y=colim_(i in I) G_i,

with structure maps k_i:G_i→Y. For each i record the label

    (G_i, g k_i:G_i→S).

Let L be the full subcategory of (G↓S) on the labels that occur. This comma notation uses ambient K-maps to S; S need not lie in C_bfs. Define

    Y'=colim_(G,a) in L G,

with this colimit computed in C_bfs and hence in K. The original I-diagram factors through L, giving q:Y→Y'. The maps a:G→S give g':Y'→S, with g=g'q.

The map q is componentwise surjective. Every object of L is represented by at least one original index i, and its colimit map G_i→Y' equals q k_i. Since ambient presheaf colimits are generated componentwise by the images of their objects, every element of Y' is in the image of q.

Finally, L has at most c objects: there are at most c choices of G and at most c^aleph_0=c maps from any such G into S. Each G has countable carrier. Therefore

    |Y'_0|+|Y'_1| <= c.

We have proved the following ZFC theorem.

**Bounded epi-compression theorem.** Every g:Y→S with Y in C_bfs and |S|<=c factors as

    Y --q onto--> Y' --g'--> S,
    Y' in C_bfs,    |Y'|<=c.

This construction does not assume that an ambient image of a C-object is again in C. The quotient is constructed as a colimit inside C_bfs.

## 5. Consequence for the mono-factorization search

For ambient finitely generated F in P, each finite-support part Q(F)_(i,fs) has carrier at most c, by [the finite-support dual-Hom lemma, Section 6.4](mono_local_compression_and_v_equalizers_2026-11-18.md). These parts form a K-subobject Q(F)_fs. Transpose any map f:F→E(Y), where Y in C_bfs, to g:Y→Q(F). Since equivariant maps preserve finite support, g factors through Q(F)_fs. Apply the theorem to that factorization and transpose back. This yields

    F → E(Y') --E(q) mono--> E(Y),
    Y' in C_bfs,    |Y'|<=c.

The monicity is componentwise injectivity of precomposition along the componentwise surjection q. Thus both-finite-support witnesses have a uniform carrier bound, even when the original Y has arbitrarily large carrier.

This is substantially stronger than bounding the number of connected components. It does not apply to general Y in C, whose second sort can fail finite support. It does not prove M=H_fg, retract closure, equalizer closure, or sufficiently-filtered-colimit closure for the actual M.

**Conditional strict boundary.** Assume N and the adopted No.1 factorization lower bound stated in [the compression note, Section 6.7](mono_local_compression_and_v_equalizers_2026-11-18.md). If kappa_0>2^c, the evaluation map

    j_0:X→E(Y_(kappa_0))

does not factor through E(Y) for any Y in C_bfs. Indeed, a hypothetical factorization can first be compressed to X→E(Y')→E(Y_(kappa_0)) with |Y'|<=c. Full faithfulness under N dualizes this to a factorization Y_(kappa_0)→Y'→B of the original evaluation map. The No.1 lower bound then gives

    kappa_0 <= |H_1(Y'_0)| <= 2^c,

a contradiction. Thus the existing distinction for p-isomorphism witnesses extends to all both-finite-support witnesses, at the same cardinal threshold. This corollary alone uses N and the No.1 lower-bound input; Sections 1–4 and the compression theorem are ZFC results.

The root's separate automatic-continuity argument shows that countable M_1-sets are finite-support. Combined with that theorem, every countable-carrier C template lies in the bounded-compression subclass treated here. No automatic-continuity theorem is needed for the proof of this note itself.
