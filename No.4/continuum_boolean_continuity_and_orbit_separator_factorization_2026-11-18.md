# Continuum Boolean continuity and finite-orbit separator factorization

2026-11-18. Status: **PROOF_RECONSTRUCTED**. The coordinating agent and another research agent independently reconstructed the central Boolean-continuity argument and found no gap. The coordinating agent also read and checked the complete assembled proof, including whole-map factorization and unrestricted type completion. Not externally reviewed or formally verified.

All results are in ZFC. Use the standing categories P, K, C, D, H_fg and M, with Ω=ω and c=2^ω. Thus D consists of the objects E(Y), Y∈C, and Z∈M means that every finite family of its elements is contained in a monic D-subobject. The two commuting endomorphism actions are distinguished as M₁ and M₂, although both monoids are End(Ω). M₁ acts on the source sets; M₂ acts by postcomposition on their Ω-valued functions.

The main improvement over [packed countable separators](packed_separators_force_monic_d_factorization_2026-11-18.md) is that **a finite family whose full M₁-orbits separate points suffices**. Its orbit can have c members, and a source sort can have 2^c elements. No finite-support assumption is imposed on the second sort, or on either sort in the factorization theorem.

## 1. Finite operations and a countable preliminary

Objects of H_fg, and hence of M, inherit every finitary pointwise operation Ω^n→Ω by the unique tuple-coding construction. Maps between these objects preserve these operations. In particular binary elements form a Boolean algebra, and finite conditionals and equality predicates are available. Write [u=k] for the binary equality predicate and χ_U for a subset indicator. A monic E(T)-subobject reflects these operations and their equations.

We also use left joint separation: if e_N u=e_N v for every N, then u=v, where e_N fixes 0,...,N−1 and sends all other integers to 0. These facts were established in the [countable-separator argument](countable_ordinal_sources_are_rigid_over_m_targets_2026-11-18.md), §2. They do not assume the existence of any uncountable Boolean operation.

**Countable continuity.** For any M₂-map a:Ω^S→Z_i with Z∈H_fg, and subsets U_n⊂S, the element aχ_(∪_n U_n) is the supremum of the elements aχ_(U_n) in the binary Boolean algebra of Z_i.

To check this, put U=∪_n U_n. Suppose v is binary, v≤aχ_U, and v∧aχ_(U_n)=0 for every n. Define C(s)=0 outside U and C(s)=1+min{n:s∈U_n} on U. Each truncation e_N C is a finite operation of the first N−1 indicators. Thus all truncations of

    if v=1 then a(C) else 0

vanish. Joint separation makes this conditional zero. It follows that v≤aχ_(S\U), and hence v=0. Applying this to v=aχ_U∧¬b for an arbitrary upper bound b proves the supremum assertion. Complements give countable infima as well.

This preliminary requires neither a bound on S nor a condition on its fixed points.

## 2. A packing fact valid for arbitrary M₁-sets

Choose injections b_n:Ω→Ω with disjoint ranges and left inverses a_n. For any M₁-set S, every b_n:S→S is injective, and for n≠r,

    b_n S ∩ b_r S = S^M₁.                              (1)

For the nontrivial inclusion, suppose z=b_n x=b_r y. For every l∈Ω choose a transformation t with t b_n=id and t b_r=const_l. Then x=const_l y for every l. Consequently mx=x for every m, so x, and hence z, is fixed. The other inclusion is immediate.

It follows that if functions f_n:S→Ω have the same restriction to S^M₁, there is a single z:S→Ω with

    z·b_n=f_n        for every n.                        (2)

Define z(b_n s)=f_n(s); (1) makes this consistent. Set z arbitrarily off the union of the images. In particular arbitrary countably many functions can be packed when S has no fixed points. Functions all zero on the fixed points can always be packed.

## 3. Continuum-sized Boolean joins and meets

**Theorem 1.** Let S be an M₁-set with at most countably many fixed points. Let

    a:Ω^S→Z_i

commute with both monoid actions, where Z∈M. For every family (U_ξ)_(ξ∈I) of subsets with |I|≤c, aχ_(∪_ξ U_ξ) is their image supremum in the binary Boolean algebra of Z_i. By complements, a also preserves infima of at most c subset indicators.

**Proof.** Put U=∪_ξ U_ξ. It suffices to prove that a binary v satisfying

    v≤aχ_U,       v∧aχ_(U_ξ)=0 for all ξ                 (3)

is zero. Empty I is immediate. Let F=S^M₁, which is countable. Each singleton {s}⊂U∩F is contained in some U_ξ. Countable continuity, applied to these singletons, gives

    v∧aχ_(U∩F)=0,       hence v≤aχ_(U\F).              (4)

Choose a selector d:U\F→I with s∈U_(d(s)), and inject I into 2^ω. Let f_n:S→{0,1} be its coordinate bits on U\F, extended by 0 outside U\F. In particular every f_n is zero on F, so §2 gives a single function z with z·b_n=f_n.

Assume v≠0. Choose a monic local cover

    j:E(T)↪Z,       T∈C,

containing the two elements v and a(z). The unique lift v′ is binary and nonzero, so choose t∈T_i with v′(t)=1. Set

    w=j_i(χ_t)≠0,       p_n=f′_n(t),

where f′_n is the lift of a(f_n), obtained by translating the lift of a(z). Then

    w≤v,       w≤[a(f_n)=p_n] for every n.               (5)

For the profile p define C_p:S→Ω by setting it to zero where all f_n equal p_n, and otherwise to one plus the first differing index. Each e_N C_p is a finite operation of f_0,...,f_(N−2). Equation (5) therefore makes every truncation of the conditional

    if w=1 then a(C_p) else 0

zero. Joint separation implies

    w≤aχ_A,       A={s: f_n(s)=p_n for every n}.         (6)

Combining (4) and (6), w≤aχ_(A∩(U\F)). This intersection is either empty or is contained in a single selector cell d^−1{ξ}, hence in U_ξ. Either case contradicts (3) and w≠0.

Thus v=0. For any upper bound b of all aχ_(U_ξ), apply the result to v=aχ_U∧¬b to obtain aχ_U≤b. This proves the assertion. ∎

The counter C_p can be chosen after t and need not lie in the chosen D-cover. Its image under a exists in Z; finite operations and joint separation suffice for the conditional argument. There is no assumption that a general intrinsic target is in M, or that any proposed amalgam map into M exists.

The bound on fixed points is used only to remove U∩F by countable continuity. It is not replaced by an unsupported claim of arbitrary completeness of the target Boolean algebra.

## 4. Agreement on continuum many covered separators

Say that Y has finitely packed continuum separators if there is a finite list z_1,...,z_r of elements in the two sorts of E(Y), whose generated ambient subpresheaf contains, in sort i, a family

    (f_(i,ξ):Y_i→Ω)_(ξ∈I_i),       |I_i|≤c,

separating the points of Y_i. Assume also that each Y_i has countably many fixed points.

**Lemma 2.** Two maps a,b:E(Y)⇉Z with Z∈M that agree on the z_l agree everywhere.

Indeed they agree on the separating functions. If a_i(G)≠b_i(G), take a common monic D-cover of their finitely many generator images and of a_i(G),b_i(G). A point t in that cover where the latter two lifts differ gives a nonzero atom w. Let p_ξ be the value at t of the common lifted separator. Then

    w≤a_i[f_(i,ξ)=p_ξ],       w≤b_i[f_(i,ξ)=p_ξ]

for every ξ. Theorem 1 gives

    w≤a_iχ_A,       w≤b_iχ_A,
    A={y: f_(i,ξ)(y)=p_ξ for all ξ}.                    (7)

Separation makes A empty or a singleton. It cannot be empty because w≠0. If A={y}, both G images equal the constant G(y) on w, contradicting the choice of t. Hence no G can distinguish a and b. ∎

More generally the same proof applies whenever a,b agree on all the displayed separators and those separators are contained in finite ambient generated subpresheaves on both sides. Agreement on a prescribed finite generating list is a convenient sufficient condition.

## 5. Strong factorization through any cover of the generators

**Theorem 3.** Under the hypotheses of §4, let a:E(Y)→Z with Z∈M. If a monic D-cover j:E(T)↪Z contains the a(z_l), there is a K-map τ:T→Y with

    a=j E(τ).                                           (8)

Neither Y∈C nor finite support of its sorts is needed here.

**Proof.** Lift each a(f_(i,ξ)) to f′_(i,ξ):T_i→Ω. For t∈T_i set w=j_iχ_t and p_ξ=f′_(i,ξ)(t). Theorem 1 gives (7), now for a alone. Thus the separator profile has a unique realization s∈Y_i, and

    w≤a_iχ_s.                                           (9)

Define τ_i(t)=s. An empty source sort forces the corresponding T_i to be empty: the coincident source constants 0,1 remain equal, while monicity reflects that equality in Ω^(T_i). Thus the definition also covers empty sorts.

Whenever a_i(G)=j_i(G′), inequality χ_s≤[G=G(s)] and (9) imply

    G′(t)=G(τ_i(t)).                                   (10)

All right translates f_(i,ξ)·m remain covered. Applying (10) gives

    f′_(i,ξ)(m t)=f_(i,ξ)(m τ_i(t)).

The left side is f_(i,ξ)(τ_i(m t)); separator injectivity proves τ_i(m t)=mτ_i(t). For either structure arrow r:Y_0→Y_1, the pullbacks f_(1,ξ)∘r are also covered. Formula (10) gives

    f_(1,ξ)(τ_1(r_T t))=f_(1,ξ)(r_Y τ_0(t)),

so τ_1r_T=r_Yτ_0. Thus τ is a genuine K-map.

Now a and jE(τ) agree on all the separators. Lemma 2 gives equality on the entire E(Y), proving (8). Merely checking the covered atoms would not replace this last step: Lemma 2 excludes an additional difference invisible to those local atoms. ∎

**Corollary 4.** If moreover Y∈C, then every pair a,b:E(Y)⇉Z with Z∈M has equalizer in D.

Choose one cover j containing both finite lists of generator images and factor a=jE(τ_a), b=jE(τ_b). The ambient K-coequalizer Y→Q of τ_a,τ_b has Q∈C, since C is colimit-closed. Since E sends colimits to limits and j is monic,

    Eq(a,b)=E(Q)∈D.

Full faithfulness of E is not used; no N or NC is needed.

## 6. Finite orbit-separation automatically supplies the hypotheses

Suppose each sort Y_i admits a finite nonempty family h_(i,1),...,h_(i,k_i) whose full M₁-orbits separate points:

    y≠y′ ⇒ h_(i,l)(m y)≠h_(i,l)(m y′)
              for some l and m∈M₁.                    (11)

There are at most c such translates, and they are generated by the finite h-list. Moreover (11), restricted to fixed points, reduces to separation by the finite tuple of values h_(i,l)(y). Therefore

    |Y_i^M₁|≤|Ω^(k_i)|=ℵ₀.

Theorems 1–3 and Corollary 4 apply. We call this the **finite orbit-separation condition**. It implies |Y_i|≤Ω^c=2^c, but does not require |Y_i|≤c. Empty lists can be replaced by the constant-zero function when the carrier has at most one point.

### The coinduced source is safe

Let S=Ω^M₁ with (m·s)(r)=s(rm), and A=S_fs. The established coinduced source

    Y=(A --inc,inc--> S)∈C

has |A|=c and |S|=2^c; see the [coinduced construction](coinduced_sigma_amalgam_and_agreement_quotient_are_outside_m_2026-11-18.md), §1, and its source reference. The single observation h(s)=s(id) has translates h·m(s)=s(m), so these translates separate all of S and their restrictions separate A. The one sort-1 element h, together with its structural image, thus supplies the required separators.

Consequently every map E(Y)→Z∈M factors through any monic D-cover of the image of h, and every pair of such maps has equalizer in D. In particular two maps into M agreeing on h are equal. The previous explicit sigma-amalgam and countable-agreement quotient do not escape this theorem: as already proved separately, their targets are outside M.

## 7. Full type completion for an arbitrary finite seed

Let Y∈K be arbitrary, let a,b:E(Y)⇉Z with Z∈M, and choose finitely many elements in Eq(a,b). In sort 1 take the corresponding finite functions; in sort 0 take its seed functions and both structural pullbacks of the chosen sort-1 functions. Add constant zero if a family is empty. Denote these finite lists h_(i,l).

Define

    y~_i y′ ⇔ h_(i,l)(m y)=h_(i,l)(m y′)
                    for every l and m∈M₁.

These are M₁-congruences, and including the structural pullbacks makes them respected by p_Y,q_Y. Hence they give a componentwise onto K-map

    q:Y↠Q,       |Q_i|≤2^c.                             (12)

The descended h-functions have finite orbit-separation on Q. The two maps aE(q), bE(q) agree on those functions. Lemma 2 therefore proves

    E(Q) ↪ Eq(a,b),                                     (13)

and this monomorphism contains the prescribed finite seed. Thus M targets force completion from any finite observation seed to the **entire full power of its type quotient**, without a finite-support hypothesis.

When Y∈C, its finite-support first sort implies the sharper |Q_0|≤c: a countable dense submonoid of End(Ω) already tests equality of observations at finite-support points, as in the [earlier type-completion proof](finite_support_type_quotients_are_m_epic_completions_2026-11-18.md), §1. The second-sort bound remains 2^c in general.

## 8. The remaining C condition, and the empty-character case

Even if Y∈C, the quotient Q in (12) need not belong to C. The first sort remains finite-support. Injectivity of H(p_Q) is automatic: pull two Q_1-characters back along the onto q_1, use injectivity of H(p_Y), and descend the resulting equality. **Only surjectivity of H(p_Q) remains unproved.** Neither full type completion nor continuum Boolean continuity alone supplies that extension condition.

There is an immediate complete special case. If H(Y_0)=∅, then H(Q_0) embeds in H(Y_0), so it is empty. Since H(p_Q):H(Q_1)→H(Q_0) exists, H(Q_1) is empty too. Therefore Q∈C. Every finite seed in Eq(a,b) now has a monic D-cover by (13), so

    Y∈C, H(Y_0)=∅, Z∈M
       ⇒ Eq(E(Y)⇉Z)∈M.                                 (14)

There is no restriction on either source cardinality or the second-sort finite-support property in (14). The stronger local-class closure and reflection consequence is recorded in [the empty-character local-class theorem](empty_character_monic_local_class_reflective_2026-11-18.md).

For general characterful C-sources lacking finite orbit-separation, the missing C-surjectivity in §8 is a genuine remaining issue. This note does not prove unrestricted M-equalizer closure, reflection of M, or a counterexample to Problem 4.

## 9. A sharper sector result and the general bound's limitation

The subsequent [non-finite-support continuity theorem](nonfinite_support_sector_preserves_two_to_c_joins_2026-11-18.md), independently reconstructed by this note's author, strengthens Theorem 1 on the sector N=S\S_fs: the corner map P(N)→[0,aχ_N] preserves joins and meets of size at most 2^c, with no restriction on the fixed-point set. Almost-disjoint ranges of c injections intersect only at finite-support points, permitting c selector bits to be packed after they are made zero on S_fs. Applying relative c-continuity to those profiles proves the stronger bound.

This stronger statement does not hold on all of S. The same note, §5, constructs an actual map a:E((λ×Ω)^Delta)→U∈M_bfs, with λ=c^+, killing each individual block indicator χ_({α}×Ω) but sending their union to 1. Here S is entirely finite-support and has no fixed points. Thus the c-bound in Theorem 1 cannot generally be increased even to c^+, despite its improvement to 2^c on the non-finite-support sector.
