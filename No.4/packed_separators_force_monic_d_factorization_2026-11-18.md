# Packed separators force factorization through a monic D-object

2026-11-18. Status: **PROOF_RECONSTRUCTED**; the coordinating agent independently reconstructed the proof, including equivariance and naturality, and found no gap. Another research agent checked the atom-extraction mechanism. Not externally reviewed or formally verified.

Use the standing P, K, E, C, D, H_fg, and M. The result is ZFC and strengthens [the agreement-on-packed-separators lemma](countable_ordinal_sources_are_rigid_over_m_targets_2026-11-18.md), §2.

## 1. Hypothesis and theorem

Say Y∈K has packed countable separators if there are finitely many elements z₁,...,z_r of the two sorts of E(Y) such that their ambient generated subpresheaf contains, in each sort i, a countable family

    f_(i,n):Y_i→ω       (n∈ω)

separating the points of Y_i.

**Theorem.** Suppose Y has packed countable separators, a:E(Y)→Z, and Z∈M. If a monomorphism j:E(T)↪Z, T∈C, contains the images a(z_l), then there exists a K-map τ:T→Y such that

    a=j E(τ).

Such a monomorphism j exists by M-membership. The same j can be chosen for any finite family of maps a by covering all their generator images at once.

Neither Y∈C nor finite support of Y is needed in this factorization statement. The essential hypotheses are the packed countable separators and the monic local D-cover in the target.

## 2. A local atom determines an actual source point

Let f'_(i,n) be the unique lifts of a(f_(i,n)) to E(T)_i; these lifts exist because the generators' images lie in j. Fix t∈T_i and put

    w=j_i(χ_t)≠0,      p_n=f'_(i,n)(t).

Then w≤[a(f_(i,n))=p_n] for every n. Define C_p:Y_i→ω to be zero where all f_(i,n) equal p_n, and otherwise one plus the first differing index.

For N≥2, e_NC_p is a finite operation of the first N−1 separators. Therefore every truncation of

    if w=1 then a_i(C_p) else 0

is zero. Left joint separation in Z gives w≤a_i([C_p=0]). If the profile p is not realized, the latter is zero, a contradiction. Since the separators distinguish points, the profile has a unique realization s∈Y_i. Thus

    w≤a_i(χ_s).                                      (1)

Define τ_i(t)=s. If Y_i is empty, the same argument rules out every t∈T_i, giving the unique map between empty sets.

There is a useful strengthening of (1). Whenever a_i(F)=j_i(F') for a function F:Y_i→ω, the pointwise implication χ_s≤[F=F(s)] gives

    F'(t)=F(τ_i(t)).                                  (2)

Indeed combine it with (1), and then reflect the resulting finite-operation inequality through j. Formula (2) applies to every function whose image is covered, not just to the original countable separators.

## 3. Equivariance and naturality

Every right translate f_(i,n)·m remains covered. Apply (2) to it. Naturality of j and a gives

    f'_(i,n)(m t)=f_(i,n)(m τ_i(t)).

The defining separator equality at m t gives the left side as f_(i,n)(τ_i(m t)). Separation therefore proves

    τ_i(m t)=m τ_i(t).

For a structure arrow r:Y₀→Y₁, the pullback f_(1,n)∘r is also covered, since the generated subpresheaf is closed under the corresponding P-arrow. Formula (2), at t∈T₀, gives

    f'_(1,n)(r_T t)=f_(1,n)(r_Y τ₀(t)).

Its left side is f_(1,n)(τ₁(r_T t)). Again separation proves τ₁r_T=r_Yτ₀. Thus the two component maps form a genuine K-map τ:T→Y.

These steps avoid assuming that countably many action equations alone determine an arbitrary T_i-point. Formula (1) first upgrades the recovered source profile to all covered translates, and that supplies full equivariance.

## 4. Equality of the entire maps

The maps a and jE(τ) agree on all f_(i,n), by construction. They are now both P-maps into Z∈M. Apply the agreement-on-packed-separators lemma in each sort to conclude a=jE(τ).

Agreement only on the local atoms would not be a sufficient substitute for this final step: a hypothetical additional part invisible to those atoms has not been excluded pointwise. The existing separator lemma is exactly what upgrades the agreement to the whole maps.

## 5. Equalizers from such C-sources are in D

Assume also Y∈C and let a,b:E(Y)⇉Z with Z∈M. Choose a common monic D-cover j:E(T)↪Z containing both finite lists of generator images. The theorem gives

    a=jE(τ_a),       b=jE(τ_b),       τ_a,τ_b:T⇉Y.

Take the K-coequalizer Y→Q of τ_a,τ_b. Both T and Y lie in C, and C is closed under ambient small colimits, so Q∈C. Since E sends colimits to limits, and j is monic,

    Eq(a,b)=E(Q)∈D.

All these facts hold in ZFC; full faithfulness of E under N is unnecessary.

## 6. Important sufficient conditions

If |Y_i|≤c and Y_i has no M₁-fixed point in each sort, choose a countable separating family by embedding each carrier in ω^ω. The disjoint-injection packing lemma packs that family into one element per sort. Thus the theorem applies.

For Y∈C, the condition H₁(Y₀)≠∅ implies that neither sort has an M₁-fixed point: a character to ω cannot take a value on a common fixed point, and H₁(p_Y) is bijective. Consequently

    Y∈C, |Y_i|≤c, H₁(Y₀)≠∅
       ⇒ Eq(E(Y)⇉Z)∈D for every Z∈M.

This includes the diagonal source Y=(C([0,ω₁]) --id,id--> C([0,ω₁])). Its compact character space is the nonseparable [0,ω₁], but its carriers have size ω₁≤c and are fixed-point-free. Nonseparability therefore does not produce an equalizer obstruction for this source.

It also includes all countable ordinal sources Y_κ, since their first-sort carriers are countable and second-sort carriers have size at most c. The result controls their entire equalizers, not only maps agreeing at the distinguished evaluation.
