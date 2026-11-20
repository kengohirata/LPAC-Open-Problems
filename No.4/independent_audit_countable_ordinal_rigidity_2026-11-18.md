# Independent audit: countable ordinal sources are rigid over M

2026-11-18. Status: **complete proof independently reconstructed; no gap found**. This is a research-agent proof audit, not external human review or formal verification.

The complete source checked was [countable_ordinal_sources_are_rigid_over_m_targets_2026-11-18.md](countable_ordinal_sources_are_rigid_over_m_targets_2026-11-18.md). The checked conclusion is ZFC: for a countable ordinal κ, maps a,b:E(Y_κ)→Z with Z∈M that agree on j₀:X→E(Y_κ) are equal.

## 1. Countable packing

The packing argument works for an arbitrary M₁-set S with no common fixed point; freeness or faithfulness is not needed. Injections b_n with disjoint ranges act injectively because their left inverses act as left inverses. If b_ns=b_mt=u, choose a transformation that fixes the first range and is constant k on the second. Then u=c_kt for every k. For any transformation r, this gives ru=c_(r(k))t=u, so u is fixed. Applying the left inverse of b_n gives s=u, contradicting the hypothesis. Thus the action images are disjoint, and arbitrary prescribed functions on them can be packed into one function on S.

This applies to both carriers of Y_κ: postcomposition by the two distinct constant maps gives distinct constant functions on the nonempty index set [0,κ].

## 2. Agreement on countable separators

M-membership provides a single monic D-image containing the finite list of images of the packing generators together with a(F),b(F). It consequently contains every common separator image. Its closure under the inherited finite pointwise operations follows from uniqueness of tuple coding. Thus unequal a(F),b(F) yield a point of the D-witness, and its singleton indicator supplies a nonzero binary w with the required inequalities.

The first-difference counter C_p is a function in the original full power, regardless of whether its profile p is realized. For N≥2, e_NC_p is determined by f₀,...,f_(N−2): it returns the first differing index plus one if that index is below N−1, and zero otherwise. On the Boolean support w, all those separators have the prescribed values p_n. Hence

    e_N(if w=1 then a(C_p) else 0)=0.

The corresponding pointwise identity is a finitary identity on Ω and is valid in the inherited finitary algebra of Z∈H_fg. Joint separation by the truncations gives

    if w=1 then a(C_p) else 0 = 0.

The Boolean consequence w≤a([C_p=0]) is therefore justified. The same holds for b. Nothing requires either C_p image to lie in the previously chosen monic D-image, and no countable-meet operation has been assumed in Z.

If the profile is unrealized, [C_p=0]=0, contradicting w≠0. If it is realized, separation makes its realization unique. The corresponding singleton indicator forces both a(F) and b(F) to take the same scalar value on w, contradicting the inequality used to select w. This proves the whole-sort agreement lemma.

Using only N≥2 in the truncation sentence avoids negative-index notation for N=0,1; these truncations are already jointly separating, so this is merely a harmless notational clarification.

## 3. Countable ordinal limit steps

Continuity of each g∈C([0,κ]) at a countable limit β ensures that the stated least stabilization threshold N(g) exists. It is allowed to be an arbitrary ω-valued function on the carrier. Packing the tuple codes (N,u_(β_n),u_β) into one source element makes both its a- and b-images a two-generator test.

For complete explicitness, the implication in the manuscript can be encoded by a unary map on each tuple code which returns 1 precisely when N≤n and u_(β_n)≠u_β, and returns 0 otherwise. Applied to the corresponding tuple element, this map gives the constant-zero element. Code projections and all these zero-test equations belong to the generated subpresheaf.

Factoring that subpresheaf through E(Q) preserves these unary equations. The first map is monic because its composite is the subpresheaf inclusion. At any point of Q₀, choose n above both lifted integer thresholds; the two implication tests and the common lifted u_(β_n) value then force the lifted u_β values to agree. They agree as functions on Q₀, and monicity reflects their equality. No finite-presentation assumption or simultaneous stage choice is involved.

This step uses only H_fg and the pointwise full-power witness in its definition, not the stronger monic factorization defining M.

## 4. Successors, induction, and ZFC scope

The balanced second-sort evaluation v_β maps under p to u_β. In H_fg, E(σ)-orthogonality makes p a bijection on the corresponding balanced elements. Its uniqueness part therefore carries agreement on u_β to agreement on v_β. Applying q gives agreement on u_(β+1). This characterization and the orthogonality inheritance are ZFC: the fixed test objects involved have countable coordinate sets, so their evaluation calculation does not require N.

Agreement on j₀ supplies the initial u₀. The successor argument and the countable-limit lemma prove agreement on every u_β and v_β for β≤κ, when κ is countable. These are countable point-separating families on the two source carriers. The packing and separator lemmas consequently give equality of the whole maps.

The argument makes no claim that countable evaluations separate a full power indexed by an uncountable ordinal, and it does not handle limit steps of uncountable cofinality. Those are genuine remaining limits of the theorem. No use of N, NC, external group-theoretic input, or cardinal-arithmetic hypothesis is hidden in the countable result.

**Audit conclusion:** the ZFC safe-source theorem and both auxiliary lemmas pass the independent audit. No theorem repair was needed. The result does not establish general equalizer closure of M.
