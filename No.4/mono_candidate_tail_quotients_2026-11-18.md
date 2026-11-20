# Mono-factorization candidate: tail quotients of bounded templates

2026-11-18. Status: PROOF_RECONSTRUCTED. This is a direct calculation for the new candidate, not a proof of its general filtered-colimit closure or a Problem 4 counterexample. No independent review or formal verification.

## 1. Setting

Use P, C, D=E(C^op), and Ω=ω from [the Isbell construction](negative_isbell_transport_fg_factorizations_equalizer_obstruction_2026-11-17.md). The unary signature of P has cardinality c=2^aleph_0.

Define M to be the full replete class of Z such that every map f:F→Z, with F ambient finitely generated, has a factorization

    F → D_0 ↪ Z,    D_0∈D,

whose last arrow is ambient monic. Thus M⊆H_fg.

The prior H_fg filtered-colimit argument does not automatically prove the corresponding statement for M: its last step composes D_0↪Z_i with Z_i→colim Z_j, and that composite need not remain monic. This is a gap in that attempted argument, not a proof that M fails filtered-colimit closure.

## 2. A class of nonmonic filtered colimits that nevertheless stay in M

Fix Y∈C. Put

    θ=max(aleph_0, |Y_0|, |Y_1|).

Let λ be regular with λ>max(c,2^θ). For α<λ let T_α=[α,λ), and consider the chain

    Z_α=E(T_α·Y),
    Z_α → Z_β   (α≤β)

induced by the inclusions T_β·Y→T_α·Y. Each Z_α belongs to D. These transition maps are componentwise surjective restriction maps, not monomorphisms in general.

Let W be their colimit in P. Each component of W consists of tail germs of functions T_α×Y_i→Ω: two functions represent the same germ iff they agree on some common tail.

**Proposition.** W∈M.

### Proof

Take ambient fg F and f:F→W. An ambient fg F has total carrier at most c and is c^+-presentable. Since λ>c, f factors through some Z_α. Equivalently, finitely many generators lift to one stage and the at most c relations between generated elements become true at one common later stage.

Choose generators g_1,...,g_n of F, where g_j has sort i_j. Their chosen images in Z_α are functions

    x_j:T_α×Y_(i_j)→Ω.

For t∈T_α, record the complete row pattern

    s(t)=(x_1(t,-),...,x_n(t,-)).

There are at most 2^θ such patterns. Let S be the set of patterns whose fiber in T_α is unbounded in λ. The union of all bounded fibers is bounded, since there are fewer than λ of them and λ is regular. Choose β≥α beyond this union.

Then s:T_β→S is surjective, and every fiber of s meets every later tail. The map

    q:T_β·Y→S·Y,
    (t,y)↦(s(t),y)

is a K-morphism between C-objects, since C is closed under coproducts. It gives

    E(S·Y) --E(q)--> Z_β → W.                       (*)

The composite (*) is monic in P. Indeed, if h,h' in a component of E(S·Y) differ at (s_0,y), their pullbacks differ at (t,y) for unboundedly many t with s(t)=s_0. Thus they never become equal on a tail. This proves injectivity componentwise.

Each x_j restricted to T_β×Y_(i_j) lies in the image of E(q): it is the pullback of the function assigning to (s,y) the j-th component of pattern s evaluated at y. The image of E(q) is a subpresheaf of Z_β containing the images of all generators of F. Hence F→Z_β factors through E(S·Y).

We have therefore factored f through the D-object E(S·Y) by the monomorphism (*), as required. □

Empty component sets cause no problem. If F has no generators, the same construction uses the single empty pattern and yields a D-subobject of W.

## 3. Consequences and limits

For the templates

    Z_*=(Ω --id,id--> Ω),
    R_2=(Ω² --id,id--> Ω²),

both carriers are countable. Hence every regular λ>c works in Proposition 2. These tail quotients do not separate M from H_fg and do not witness failure of M under sufficiently filtered colimits.

The proposition also explains why simply replacing the earlier mono chains by long chains of restriction quotients does not immediately reject the new candidate. Although a full stage map Z_α→W is nonmonic, the finitely many chosen generators are covered by a different D-subobject, obtained by grouping recurrent row patterns.

However, the cardinal threshold depends on |Y|. This does **not** prove that there is a single μ such that M is closed under all μ-filtered colimits. The C-objects used in the original non-coreflectivity construction have unbounded carrier sizes, even when their numbers of M_1-connected components are bounded.

## 4. Why the obvious image compression is insufficient

For fg F, its dual Q(F) has bounded carrier size (at most 2^c). A factorization F→E(Y) transposes to Y→Q(F). Passing to the image of this map does not guarantee a C-object.

The existing evaluation maps

    ψ_κ:Y_κ↠B,    B=(Ω⇉1),

already show the issue: Y_κ∈C while B∉C. Hence the image in the small target may lose C-membership. There is no valid inference from the bounded size of Q(F) to a bounded-size C-witness or a monic D-factorization.

Likewise, a bounded number of connected components of Y does not bound its carrier. The root compression lemma can improve the shape of a witness while leaving this size obstruction intact.

## 5. Current conclusion

No equality M=H_fg has been proved here, and no strict-inclusion witness has been constructed. No general sufficiently-filtered-colimit closure or failure has been proved either.

The established result is narrower and concrete: tail quotients of copowers of any fixed bounded-size template Y∈C remain in M once the filter completeness exceeds the number of possible generator row patterns. Any attempted rejection using that family must account for the recurrent-pattern D-subobject constructed above.

The proposition itself uses C's coproduct closure and elementary cardinal arithmetic. It does not use N or the No.1 input (NC). Those hypotheses remain relevant to the separate nonreflectivity claims about D and M.
