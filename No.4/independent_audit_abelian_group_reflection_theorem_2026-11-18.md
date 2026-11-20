# Independent audit: the reflection theorem for Ab

2026-11-18. Status: **complete proof independently reconstructed; no gap found**. This is an independent research-agent audit, not external human review, formal verification, or a novelty assessment.

The complete manuscript checked is [abelian_groups_limit_countable_union_reflection_theorem_2026-11-18.md](abelian_groups_limit_countable_union_reflection_theorem_2026-11-18.md). Its theorem says that a full replete subcategory A⊂Ab closed under all ambient small limits and countable ascending unions is reflective. For μ=max(|X|,ℵ₀), it also gives a reflection of X of cardinality at most μ^ℵ₀.

## 1. Classical inputs checked against their stated sources

The bounded decomposition and bounded-pure-subgroup splitting statements used in the manuscript are exactly those stated in [Milne, Lemma 1(a),(b)](https://www.jmilne.org/math/articles/2015b.pdf), PDF p.1. The references there are Fuchs 17.2, 27.5 and Kaplansky Theorem 7. The argument uses splitting only after establishing purity; it never treats a bounded group as injective in Ab.

The classification of divisible groups as direct sums of Q and Prüfer groups, and the equivalence between divisibility and injectivity, are explicitly recalled in [Goldsmith–Kelly–Wallutis, pp.25–26](https://www.maths.tcd.ie/pub/ims/bull54/R5401.pdf). Existence of an essential injective hull is the precise content of [Stacks, Lemma 47.5.2](https://stacks.math.columbia.edu/tag/08Y1). These three sources were opened independently for this audit. The underlying classical structure theorems are accepted inputs, not reproved here.

## 2. Only two countable unions are used

If a nonzero torsion-free K lies in A, the subgroups (1/n!)K inside Q⊗K form an ascending countable chain, each isomorphic to K. Their union is the nonzero Q-vector space Q⊗K; Q is a retract. Thus Q∉A excludes every nonzero torsion-free A-object.

If the allowed p-primary exponents are unbounded, each G[p^n] is an A-object by kernel closure. Some such bounded group has an element of order p^n. Its cyclic decomposition therefore has a summand of order exactly p^n. Retract closure puts C_(p^n) in A, and their standard countable ascending union puts C_(p∞) in A.

No arbitrary directed-union closure is needed for divisible direct sums. The direct sum of any set of divisible A-objects is divisible, hence injective. Its inclusion into their product splits by injectivity of the domain. It is therefore a retract of an A-object and belongs to A. This direction of the injectivity argument is correct.

When at least one Prüfer group is available, its countable product is divisible and has an element of infinite order, obtained by letting coordinate orders tend to infinity. The divisible decomposition must then have a nonzero Q summand. This proves the manuscript's implication U≠∅⇒Q∈A.

## 3. Bounded primary parts really split

For p in the bounded set B, a global exponent n_p gives T_p(G)=G[p^(n_p)]∈A. The entire primary subgroup T_p(G), rather than an arbitrary bounded subgroup, is pure in G. Indeed, for a positive integer m and my∈T_p(G), the element y is torsion. Decomposing y into its finitely many primary components shows my=my_p. Hence T_p(G)∩mG=mT_p(G).

The bounded-pure splitting theorem now supplies r_p:G→T_p(G). A homomorphism to a p-primary group kills every q-primary component for q≠p. The chosen r_p therefore separate all elements of the direct sum of the selected primary parts. The cases n_p=0 and T_p(G)=0 cause no problem.

## 4. Both ambient embeddings are valid

If Q∉A, all primes are bounded. The kernel of G→∏_p T_p(G) belongs to A and has no nonzero torsion element, because the r_p separate torsion. It is therefore zero by the torsion-free argument. This yields the required monomorphism without asserting that G itself is torsion.

If Q∈A, write T_B=⊕_(p∈B)T_p(G). Any element of G/T_B of finite order lifts to a torsion element of G: if ng∈T_B, then some positive multiple of ng is zero. Thus

    t(G/T_B)=t(G)/T_B=⊕_(p∈U)T_p(G).

An essential injective hull E of this quotient has no B-primary torsion. Otherwise a subgroup of order p, for p∈B, would meet the original quotient nontrivially, contrary to its torsion calculation. The divisible decomposition of E therefore has only the allowed Q and U-Prüfer summands, so E∈A by the preceding product/retract argument.

The map G→E×∏_(p∈B)T_p(G) is monic: the first factor has kernel T_B and the other factors separate T_B. Neither T_B nor G/T_B was assumed to belong to A. The injective hull construction takes place in Ab, and its A-membership is established afterwards by classification. This avoids any unproved quotient-closure assumption.

## 5. The uniform cardinal bound

For S⊂G and μ=max(|S|,ℵ₀), each r_p(S) meets at most μ coordinates in a cyclic decomposition of T_p(G). The sum H_p of those coordinates is a direct summand, lies in A, and has cardinality at most μ.

In the second case, start with the subgroup generated by q(S) in E and repeatedly add one chosen n-th root of every current element for every positive n. Each step adds at most μ elements; the countable union has cardinality at most μ and is divisible. This E₀ has no forbidden primary torsion since E₀⊂E, so its classification again proves E₀∈A. Intermediate subgroups need not lie in A, and the proof never assumes otherwise.

There are only countably many primes. Thus P₀=E₀×∏H_p, omitting the E₀ factor in the first case, belongs to A and has size at most μ^ℵ₀. Its inverse image H in G is a pullback of A-objects and therefore belongs to A. Since G→P is monic, H→P₀ is monic. Consequently

    S⊂H⊂G,    H∈A,    |H|≤μ^ℵ₀.

The use of a pullback is essential and valid: arbitrary subgroup closure of A is not needed. The cardinal estimate holds for every infinite μ, including singular μ, with no continuum hypothesis or regularity assumption.

## 6. Solution sets, uniqueness, and the reflection's size

For fixed X, there is a set of isomorphism types of groups of size at most ν=(max(|X|,ℵ₀))^ℵ₀. Taking all maps from X into the A-objects among these gives a solution set by the local bound. The comma category X↓A is complete and locally small, so its product gives a weakly initial object. Shrinking this object around the image of X via the local bound preserves weak initiality and produces a weakly initial W of size at most ν.

The manuscript's explicit initial-object argument checks. Let e:I→W equalize every endomorphism of W with the identity, in the comma category. Weak initiality gives v:W→I, and e v e=e implies v e=id_I. For any endomorphism t of I, e t v is an endomorphism of W, so e t v e=e and hence t=id_I. Equalizing any two maps from I and using weak initiality then makes that equalizer split epic as well as monic, proving uniqueness of maps out of I. Existence follows from e and weak initiality of W.

Thus I is the reflection object. Its inclusion into W also gives |I|≤ν; the extra reflection-size assertion is justified, rather than merely a bound on a weak reflection.

## 7. Audit conclusion

The whole theorem, including the weakening to countable ascending unions and the bound μ^ℵ₀, passes this independent audit. All uses of splitting, classification, and external injective hulls have their hypotheses satisfied. No missing subgroup, quotient, arbitrary-union, or filtered-colimit closure assumption was found.

This rules out full subcategories of Ab satisfying the stated hypotheses as counterexamples to No.4. It does not settle the problem for arbitrary locally presentable categories or other module categories. Whether this theorem is already in the literature was not investigated in this audit.
