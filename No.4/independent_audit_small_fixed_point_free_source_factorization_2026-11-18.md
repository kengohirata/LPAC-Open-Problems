# Small fixed-point-free sources: independent audit of monic D-factorization

2026-11-18. Status: PROOF_RECONSTRUCTED. The factorization mechanism proposed by mono_collapse was independently reconstructed by mono_equalizer. This is an internal mathematical audit, not external peer review or formal verification. All statements below use ZFC; neither N nor finite support is needed.

Use the standing categories K, P, C, D=E(C^op), and M. Put c=2^aleph_0. The ingredients concerning finite tuple operations and left joint separation, and the agreement-on-countable-separators lemma, are in [the countable ordinal note, Sections 1–2](countable_ordinal_sources_are_rigid_over_m_targets_2026-11-18.md).

## 1. Statement

Let Y be any K-object. Suppose each Y_i has cardinality at most c and has no M_1-fixed point. Then every P-map

    a:E(Y)→Z,   Z∈M,

factors through a monic D-subobject of Z. More precisely, in each sort choose a countable separating family and pack it into a single element h_i of E(Y)_i. If

    j:E(T)↪Z,   T∈C,

is any monic D-cover of a(h_0),a(h_1), there is an explicit K-map τ:T→Y such that a=jE(τ).

The case of an empty Y_i causes no problem. The equality of its constant zero and constant one functions forces T_i to be empty for any such cover; then τ_i is the empty map. In the proof below assume the relevant Y_i is nonempty.

## 2. Every cover point has a unique source profile

For a fixed sort choose functions f_n:Y_i→ω separating points. Such a countable family exists because |Y_i|≤c. Choose disjoint-image injections b_n:ω→ω. Fixed-point-freeness implies the subsets b_nY_i are disjoint, so h_i can be chosen with

    h_i·b_n=f_n.

Write h'_i:T_i→ω for the lift of a(h_i). For t∈T_i let

    w_t=j(χ_t),        p_n=(h'_i·b_n)(t).

The element w_t is nonzero and binary. It lies below [a(f_n)=p_n] for every n.

Define C_p:Y_i→ω to be zero on the points with full profile p, and otherwise one plus the first index where the profile differs. Each left truncation e_N C_p is a finite operation of finitely many f_n. Thus all left truncations of the conditional element

    if w_t=1 then a(C_p) else 0

vanish. Left joint separation gives

    w_t≤a([C_p=0]).

If p is omitted by Y_i, the right side is zero, a contradiction. If p is realized, its realizing point is unique because the f_n separate points. Denote it τ_i(t). We have proved

    w_t≤a(χ_(τ_i(t))).                                      (1)

The counter C_p need not lie in the selected D-cover. Its image under a exists in Z, and finite operations plus left separation in Z suffice.

## 3. Equivariance and structure maps

There is a useful step beyond the countable profile equalities. For every r∈M_1, the function h_i·r has its image in the chosen D-cover. Evaluating the pointwise singleton identity on (1) gives

    h'_i(r t)=h_i(r τ_i(t))       for every r∈M_1.             (2)

This includes all r, not only the injections used for packing. Comparing (2) at mt and at t shows that τ_i(mt) and mτ_i(t) have the same values under every h_i·r. In particular their f_n-values agree, so

    τ_i(mt)=mτ_i(t).

For a structure map p_Y:Y_0→Y_1, the functions (h_1·r)p_Y have images in the cover because it is a P-subobject. Using (1) in sort 0 and (2) in sort 1 gives

    h_1(r p_Yτ_0(t))=h_1(r τ_1p_T(t))

for every r. Separation therefore gives p_Yτ_0=τ_1p_T. The same argument applies to q. Thus τ:T→Y is an actual K-map.

Taking r=id in (2) shows h'_i=h_iτ_i. Consequently a and jE(τ) agree on h_i, and hence on every f_n. The agreement-on-countable-separators lemma proves equality on the entire sort. This proves a=jE(τ).

One must use that last lemma. Agreement after meeting with all the cover atoms alone is not a valid substitute: a larger target could contain an element invisible at every one of those atoms.

## 4. Equalizers and actual directed unions

If a,b:E(Y)⇉Z are two maps, choose one monic D-cover of their four packed-generator images. The proof produces explicit τ_a,τ_b:T⇉Y with

    a=jE(τ_a),       b=jE(τ_b).

If Y∈C, form the coequalizer Q of τ_a,τ_b in K. Both T and Y belong to C and C is colimit-closed, so Q∈C. Since E takes colimits to limits and j is mono,

    Eq(a,b)≅E(Q)∈D.

No full-faithfulness theorem is used: the dual maps were constructed explicitly, so the conclusion is ZFC.

There is also an arbitrary-stage-index consequence. If U is an actual directed union of D-subobjects and a:E(Y)→U, choose one stage containing the two packed-generator images. That stage mono can serve as j in Section 1. Hence a factors through a single stage. The index need not be countable, and the stages need not be copies of a fixed template.

## 5. Boundary of the proposed ordinal-diagonal test

For S=C([0,ω_1],ω), every continuous function is eventually constant and has finite range. Thus |S|≤c, and S has no M_1-fixed point. For the diagonal Y=(S id,id S)∈C, every pair E(Y)⇉Z with Z∈M has its equalizer in D by Section 4.

In particular, this source cannot exhibit two maps agreeing in sort 0 but differing in sort 1. Indeed, after common factorization, a_0=b_0 gives equality of τ_(a,0),τ_(b,0). Composing the two second-sort maps with any character of S gives two characters of T_1 agreeing on p_T(T_0). Injectivity of H_1(p_T) makes them equal. The evaluations on [0,ω_1] separate S, so τ_(a,1)=τ_(b,1), hence a=b.

This excludes the proposed test despite the nonseparability of H_1(S)≅[0,ω_1]. Nonseparability of that spectrum by itself is insufficient: the countable family used in the proof consists of arbitrary functions on the carrier S, rather than characters of S.

The theorem does not cover sources with larger carriers or with unrestricted fixed-point sets. It does not settle general M-equalizer closure or No.4.
