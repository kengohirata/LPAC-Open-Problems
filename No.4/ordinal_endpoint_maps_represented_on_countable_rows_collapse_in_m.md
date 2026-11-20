# Ordinal maps represented on countable rows agree after mapping into M

Write Y for the usual ordinal diagram on X=[0,κ]: its first carrier consists of continuous ω-valued functions on X, its second carrier consists of all ω-valued functions, and its arrows are inclusion and precomposition with the successor map fixing κ. Write u₀ for evaluation at 0 on the first carrier. This argument is in ZFC and applies in particular at κ=(2^aleph₀)^+. It concerns a specific class of maps to M.

## Statement

Let I be a set with a proper filter and R_i arbitrary diagrams of left End(ω)-sets. Form the two-sort reduced product

    W=(∏_i E(R_i))/filter,

where equality in each sort means equality of the entire row functions on a filter-large set of indices. Choose two families of genuine diagram maps A_i,B_i:R_i→Y. They induce P-maps a,b:E(Y)⇉W by precomposition on each row. Assume that in each row the joint image of (A_i,B_i):R_i→Y×Y has countable carriers in both sorts. In particular, all countable R_i are allowed, and their diagram structures may vary with i.

**Theorem.** For every map k:W→Z with Z∈M,

    k a(u₀)=k b(u₀)   implies   k a=k b.

Here and below a first-sort subscript at u₀ is implicit. Neither W nor the row diagrams are required to satisfy the local C-cover condition. The filter need not be countably complete. The hypothesis on u₀ is imposed only after applying k. Equality follows on the whole second sort as well as at the endpoint.

## A fact about two maps from a C-object

If U∈C and L,N:U⇉Y agree after evaluation at 0 in sort 0, then L=N. For each ξ≤κ, evaluation at ξ after either sort-1 map is an equivariant character on U₁. Its restriction along p_U is evaluation at ξ after the corresponding sort-0 map. Equality of those sort-0 characters forces equality of their sort-1 extensions, by injectivity of H(p_U). Pullback along q_U then gives equality at ξ+1 when ξ<κ. At a limit, for every y∈U₀ the two functions L₀(y),N₀(y) are continuous and agree below the limit, so they agree there. Transfinite induction gives agreement at every first- and second-sort evaluation, and these evaluations separate functions pointwise. This reasoning requires no assumption on κ or its cofinality.

## Compressing the rows for one requested observation

Fix a sort j and any function F:Y_j→ω. In each row replace R_i by its joint image S_i in Y×Y, and write e_i:R_i↠S_i for the quotient and L_i,N_i:S_i⇉Y for the two projections.

Mark S_i by four ω-valued functions, keeping track of their sorts and order:

    u₀ L_(i,0),   u₀ N_(i,0),   F L_(i,j),   F N_(i,j).

Only c=2^aleph₀ isomorphism types of these marked diagrams are possible. To verify this for the uncountable monoid End(ω), first observe that every point of S_i in either sort is finite-support. Such a point is a pair of ω-valued functions. If either function had infinite range, its postcomposition orbit would contain c distinct functions (already binary postcompositions suffice), contrary to countability. The finite union of the ranges supports the pair.

On countable carriers a finite-support action is determined by its restriction to a fixed countable pointwise dense subset of End(ω). Indeed, to compare two actions agreeing on that subset at an element, approximate any m by a member agreeing with m on the union of finite supports for that element in the two actions. There are at most c tables on countable carriers for the restricted actions, the two arrows and the four marked functions. This gives the asserted bound without a classification of countable monoid actions.

Select one representative row for each occurring marked type and put Q equal to the coproduct of the selected S_i. Both carriers of Q have cardinal at most c. Neither carrier has a monoid-fixed point, because it maps to the corresponding carrier of Y, where distinct constant postcompositions give different functions. Empty carriers cause no difficulty. Define L,N:Q⇉Y by the two projections of the representative rows. The unmarked parts of these maps may differ from their counterparts on other rows of that type.

For every i choose a marked isomorphism from S_i to the corresponding representative. Composing it with e_i and the summand inclusion gives t_i:R_i→Q. Rowwise pullback defines a P-map h:E(Q)→W. The four markings give exact equalities in W:

    h E(L)(u₀)=a(u₀),     h E(N)(u₀)=b(u₀),
    h E(L)(F)=a(F),       h E(N)(F)=b(F).

No simultaneous factorization of a,b on unmarked functions is used. The coproduct, the representatives and h may depend on F.

## The local C-cover forces agreement

The fixed-point-free small-source factorization theorem applies to k h:E(Q)→Z even though Q need not be in C. It supplies U∈C, a monomorphism m:E(U)↪Z and a genuine map τ:U→Q such that k h=m E(τ). See [the factorization proof, Sections 1–4 and 6](packed_separators_force_monic_d_factorization_2026-11-18.md).

The initial-mark equalities and monicity of m say exactly that Lτ,Nτ agree at u₀. By the C-object argument above, Lτ=Nτ. The other two markings therefore imply k a(F)=k b(F). Since F was arbitrary, the theorem follows.

## Scope of the exclusion

This rules out the entire countable-row construction for an endpoint split, including attempts to first produce a split in a larger reduced product and then map that product into M. For the earlier glued example there is an explicit pair of balanced extensions already in the subpresheaf generated by the two images. The general proof here uses h:E(Q)→W. A map defined only on that generated subpresheaf is covered by the proof if it also has the required domain on h(E(Q)) for each observation, for example by extension to W. Such an extension is not automatic.

In particular, taking k to be the identity excludes any separating pair represented in this manner when W itself belongs to M. Two arbitrary maps to an M-object have not been shown to admit a joint row representation with countable joint images. Thus the unrestricted endpoint question remains open. See [the structural-kernel obstruction and the glued example](endpoint_disagreement_forces_a_large_antichain_in_every_subinterval.md).
