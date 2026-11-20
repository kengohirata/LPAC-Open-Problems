# The No.3 ordinal rank candidate cannot be transported by a product preserving full embedding

2026-11-18. Status: direct proof reconstructed and self-checked. This excludes one route to a Problem 4 counterexample; it neither resolves No.3's separate source conflict nor proves Problem 4.

## 1. The relevant part of the No.3 construction

In the [ordinal-ranked pointed-set candidate](../No.3/ordinal_rank_candidate_and_boundedness_conflict_2026-11-17.md), let X_α be the object of rank α whose underlying set consists of its two marked points b,c. The defining calculations give:

- End(X_α) consists only of the identity.
- For α<β there is a map k_(α,β):X_α→X_β sending both marked points to b.
- For the binary product projections π_1,π_2:X_α×X_α⇉X_α,

      k_(α,β) π_1 = k_(α,β) π_2.

- X_α and X_β are not isomorphic when α≠β.

Only these elementary parts of that candidate are used below, not its claimed generatedness, cocompleteness, or density analysis.

## 2. A presheaf obstruction

**Proposition (ZFC).** A category containing such a proper-class family cannot have a fully faithful binary-product-preserving functor into any presheaf category P=Set^(A^op) on a small A.

Proof. Suppose E is such a functor, and put Z_α=E(X_α). For each α let S_α⊆1 be its support presheaf: S_α(a) is a singleton if Z_α(a) is nonempty and is empty otherwise. This is a subpresheaf because a presheaf restriction cannot map a nonempty set into an empty one. There is a canonical componentwise surjection Z_α→S_α.

The existence of E(k_(α,β)) implies S_α⊆S_β whenever α<β. Since A is small, there is only a set of subobjects of 1. Thus this increasing ordinal-indexed family of supports is eventually constant. More explicitly, the union of all supports is a subset of the set Ob(A); for each object in that union choose its least occurrence, and bound those set-many ordinals. Choose α<β beyond this bound, with S_α=S_β=S.

Product preservation and kπ_1=kπ_2 imply that E(k_(α,β)) is constant on each nonempty component Z_α(a). It therefore factors through the support quotient:

    Z_α → S --j--> Z_β.

The map j is natural: its component is the uniquely determined constant value of E(k_(α,β)), and naturality follows by taking any element in the relevant nonempty source component. It is monic because S is subterminal.

Let p:Z_β→S be the canonical support quotient. Then pj=id_S, so jp is an endomorphism of Z_β. Full faithfulness and rigidity of X_β force jp=id_(Z_β). Hence Z_β≅S.

Now apply the same argument to β<γ beyond the support bound. It gives Z_γ≅S as well, contradicting full faithfulness and the nonisomorphism of X_β and X_γ. □

## 3. Consequence for No.4

A full embedding of the No.3 rank candidate whose image is closed under the ambient limits would necessarily preserve its existing products. Section 2 rules this out for a presheaf ambient.

More generally, a locally presentable ambient admits its usual fully faithful limit-preserving restricted-Yoneda embedding into a presheaf category. Composing with that embedding would again contradict Section 2. Therefore the No.3 rank candidate cannot yield a P4 counterexample through a full limit-preserving embedding into any locally presentable category.

This obstruction is independent of the no-measurable-cardinal hypothesis. A general full graph embedding, even if available under an additional set-theoretic hypothesis, would not supply the product preservation required here.
