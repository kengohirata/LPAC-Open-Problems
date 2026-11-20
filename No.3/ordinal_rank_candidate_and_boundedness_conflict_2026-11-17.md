# No.3 — Ordinal-ranked pointed sets: a counterexample candidate and an unresolved conflict with the published reduction

2026-11-17.

## Status: CANDIDATE_WITH_UNRESOLVED_SOURCE_CONFLICT

This note records an explicit category and proposed proofs of its properties. It is NOT an announcement that Open Problem 3 has been solved, or that its known Vopenka-positive statement has been disproved. The construction appears to satisfy the literal cocomplete/generated-strong-generator formulation in the original problem, but it has no small dense subcategory, in direct conflict with the boundedness reduction stated on pp.295–296. This discrepancy has not been independently resolved. Do not silently adopt both the proposed proofs below and that reduction.

No uncountable-measurable nonexistence assumption N, V=L, or large-cardinal principle is used in the construction. Thus, if the proposed proof is correct for the intended definitions, the conclusion would be a ZFC-negative result for the literal formulation, NOT the desired relative independence proof. Independent scrutiny is essential, particularly of Sections 3–5 and the comparison in Section 9.

The prior notes' theorems explicitly assuming a full reflective presheaf presentation are not contradicted by this candidate: Section 8 shows why that presentation cannot exist for it, if the present calculations are correct. The issue concerns deriving such a presentation from only the literal hypotheses.

## 1. Motivation and relation to previous work

The previous note constructs K_Gamma separately for every set ordinal Gamma. Its signature and generator family grow with Gamma. Here the ordinal is instead a tag on each object of ONE category, with ONE representing generator. No class of operation symbols is put into an individual object.

A literature search found a related ordinal-indexed construction in R. Boerger and W. Tholen, Total Categories and Solid Functors (1990), Example 4.3, pp.223–225. That paper establishes totality and a single strong generator together with failure of strong-quotient smallness. It is not cited as a proof of finite generatedness or as a solution of P3. The present simpler category is defined and checked below independently.

## 2. The proposed category C

Use the ordered class Ord together with a new symbol infinity, greater than every ordinal. Objects are of two types:

* Ordinal type: (alpha, X, b_X, c_X), where alpha is a set ordinal, X is a set, and b_X != c_X are two specified elements of X.
* Infinity type: (infinity, X, b_X), where X is a pointed set.

These are set-coded objects: an ordinal is a set, and the infinity type uses a finite tag, not a proper-class datum.

Write r(X) for the rank. A morphism f:X->Y is an underlying set function, subject to:

1. r(X) <= r(Y).
2. f(b_X)=b_Y.
3. If r(X)=r(Y)<infinity, then f(c_X)=c_Y.
4. If r(X)<r(Y), then X has ordinal type and f(c_X)=b_Y.

There is no additional marked element at infinity. There are no morphisms from infinity type to ordinal type, nor from a larger ordinal rank to a smaller one.

Identity functions are morphisms. Composition is ordinary function composition. To check the only nontrivial marked element, if alpha<gamma in a composable alpha<=beta<=gamma, either the first arrow already sends c to b or the second sends the intermediate c to b. Thus the composite sends c to b as required. Hom sets are subsets of ordinary function sets. Hence the proposed category is locally small.

Let U:C->Set forget rank and marked elements. U is faithful.

## 3. A single strong generator

Let

    G=(0,{b,c,x},b,c),    H=(0,{b,c},b,c).

For every object Y and every element y in UY, there is exactly one map f_y:G->Y taking x to y. Its values on b,c are forced by the rank rules:

    f_y(b)=b_Y;
    f_y(c)=c_Y if r(Y)=0, and b_Y if r(Y)>0.

Consequently evaluation at x gives a natural bijection

    C(G,Y) = UY.

More generally F(S)=(0,S disjoint-union {b,c},b,c) satisfies C(F(S),Y)=Set(S,UY), so F is left adjoint to U. This adjunction is not asserted to be monadic.

U reflects isomorphisms. Indeed a rank-increasing morphism identifies its source's two distinct marked elements, so is not injective. Thus an underlying bijective morphism has equal ranks; its inverse preserves the appropriate marked elements and is again a morphism.

It follows that {G} is a strong generator: its hom functor is faithful and conservative.

For clarity, the usual subobject test can also be checked directly. A morphism m is monic exactly when Um is injective. One direction uses representability of U; conversely an injective underlying function cancels all functions. A proper mono therefore omits an underlying element; the map from G selecting that element cannot factor through m.

## 4. Monomorphisms and finite generatedness

The preceding characterization has a special consequence:

    Every mono has equal source and target rank.

For ordinal rank-increasing maps the two marked elements are identified. For infinity-to-ordinal maps there is no morphism. Thus a directed diagram all of whose transitions are monos has one constant rank, since any pair of indices has a common upper bound.

At a fixed ordinal rank alpha, the objects and maps are just sets with two distinct marked points and maps preserving them. The set-colimit of a directed diagram of injections has two distinct marked points, and gives an object Z of that same rank.

This set-colimit is also a C-colimit, including against targets outside that rank. For a target of rank beta<alpha there is no cocone. For beta=alpha, a cocone induces a unique set map preserving both marks. For beta>alpha, all cocone maps send both marks to b, so their unique set-colimit map also sends both marks to b and is an allowed C-map. Infinity targets are handled by the same rule.

At constant infinity rank, directed mono-colimits are ordinary pointed-set unions, and there are no cones to ordinal ranks.

Thus U preserves all small directed colimits of monomorphisms. Since C(G,-)=U, the proposed proof gives:

    G is finitely generated in the categorical sense used in P3.

This is not a claim that G is finitely presentable. In fact the increasing-rank chains below show that it is not lambda-presentable for any regular lambda.

The apparent strength of this conclusion is precisely why the conflict in Section 9 cannot be ignored.

## 5. All small coproducts and coequalizers

### 5.1 Empty coproduct

H is initial. A map H->Y is uniquely forced on its two elements: it preserves b and sends c to c_Y at rank 0, and to b_Y at all higher ranks.

### 5.2 Nonempty set-indexed coproducts, all ranks ordinal

Take a SET-indexed family X_j of ordinal ranks alpha_j, and let delta=sup_j alpha_j. This is a set ordinal. Start with the disjoint union of the underlying sets and make the following identifications:

* identify all b_j to one point b;
* for alpha_j<delta, identify c_j with b;
* if the maximum delta is attained, identify all c_j with alpha_j=delta to one new marked point c, distinct from b;
* if delta is not attained, append a fresh point c, distinct from the quotient set.

The result, at rank delta with marks b,c, is the proposed coproduct. The canonical maps are morphisms.

For a target Y, any cocone implies r(Y)>=alpha_j for all j, hence r(Y)>=delta. If r(Y)=delta, the resulting map must send the new marked c to c_Y. If r(Y)>delta, it must send c to b_Y. All other values are fixed by the cocone. They are compatible with the imposed identifications by exactly the morphism rules. This gives a unique factorization. Thus the universal property holds also when delta is an unattained limit, where the new point c was absent from every source.

### 5.3 Coproduct with an infinity-type summand

Every possible target then has infinity type. Take the disjoint union, identify all basepoints, and collapse every ordinal summand's c to that basepoint. The resulting pointed set, at infinity rank, is the coproduct. No fresh second marked point is needed. Its universal property is that of the indicated pointed quotient.

### 5.4 Coequalizers

Let f,g:X=>Y be parallel, with rank(Y)=beta<infinity. Let pi:UY->Q be the set quotient by the equivalence relation generated by f(x)=g(x).

* If pi(b_Y)!=pi(c_Y), use (beta,Q,pi(b_Y),pi(c_Y)), and pi is the coequalizer.
* If pi(b_Y)=pi(c_Y), use (beta+1,Q disjoint-union {c_new},pi(b_Y),c_new), and take the quotient followed by inclusion as coequalizer map.

In the second case an equalizing map Y->Z necessarily identifies b_Y,c_Y. Such a map cannot have rank(Z)=beta, so rank(Z)>beta. It factors through Q on the old elements. The fresh point c_new must map to c_Z if rank(Z)=beta+1 and to b_Z if rank(Z)>beta+1. This is forced, gives an allowed morphism, and proves uniqueness. Infinity targets obey the latter rule.

If Y has infinity type, its coequalizer is simply the pointed-set quotient at infinity rank.

Small coproducts and coequalizers give all small colimits. The proposed proof of cocompleteness uses only SET-indexed coproducts; no proper-class coproduct or proper-class colimit is used.

## 6. Additional checks: completeness and well-poweredness

These properties are not needed for the literal counterexample attempt, but including them rules out merely missing completeness as an explanation.

The terminal object is T=(infinity,{b},b).

For a nonempty small family of objects, take their set product. If all ranks are infinity, give it infinity rank and the tuple of basepoints. Otherwise let alpha be the least ordinal rank occurring. Give the product rank alpha, basepoint the tuple of basepoints, and distinguished c the tuple whose components are c_j at rank alpha and b_j at larger ranks. This tuple differs from the basepoint in a minimum-rank component. Projections and the universal property follow by considering the rank of a source cone.

For equalizers of f,g:X=>Y, the set equalizer contains b_X and also c_X when present: both maps send each specified source point to the same forced target point. Equip it with the rank and marks of X. This is the categorical equalizer.

Thus all small limits exist. In particular pullbacks exist.

All subobjects of X have the rank of X and are represented by subsets containing its marked points. Hence C is well-powered.

## 7. One fixed source and a proper class of strong quotients

For each ordinal alpha put

    X_alpha=(alpha,{b,c},b,c).

For alpha>0 there is one map

    q_alpha:H=X_0 -> X_alpha,
    q_alpha(b)=q_alpha(c)=b.

For alpha=0 take the identity.

### 7.1 Direct strong-epi verification

Consider an arbitrary square with q_alpha on the left and a mono m:C->D on the right. A mono has equal source/target rank gamma and injective underlying function. The bottom map X_alpha->D implies gamma>=alpha.

If gamma=alpha<infinity, define the diagonal X_alpha->C by b->b_C,c->c_C. If gamma>alpha, define it by both points going to b_C. For gamma=infinity this is also the forced pointed constant map.

The top map H->C has the matching forced values, and m sends the marks of C to those of D, so both triangles commute. The diagonal is unique because a map out of X_alpha is fully determined on its two elements (or by monicity of m).

Therefore every q_alpha is a strong epi, not merely an ordinary epi.

Distinct ranks are nonisomorphic, since there are no descending arrows. Thus the fixed H has a proper class of strong quotient classes. If the construction and properties above are correct under the intended P3 definitions, C is not locally presentable.

Notice that U(X_alpha) always has only two elements. This does not contradict a size-bound argument in a fixed FULL presheaf embedding: U is only faithful and conservative, not full, and has a proper class of structures over this carrier. The relevant smallness assertion is about isomorphism classes, not U-cardinality alone.

### 7.2 The canonical tower

For alpha<beta, the map X_alpha->X_beta identifies its two points. Its kernel pair has underlying set {b,c}^2, rank alpha, marks (b,b),(c,c). Its coequalizer is exactly X_alpha->X_(alpha+1), by Section 5.4.

At a nonzero limit delta<=beta, the colimit of X_alpha for alpha<delta is X_delta. Every old c_alpha has been sent to b by the next stage; the unattained rank supremum delta contributes the fresh marked point c_delta. The universal-property proof is the same rank-by-rank argument as above, or follows by coproduct/coequalizer computation.

Consequently the proposed canonical tower for q_beta has exact length beta. Here the CATEGORY and H are fixed, unlike in K_Gamma from the previous note.

For q_infinity:H->T, the same tower never terminates at a set ordinal. This does not refute the previous individual-stopping theorem for full reflective presheaf subcategories, because Section 8 shows that C is not one of them.

## 8. No small dense subcategory: the exact point of conflict

Let D be any small full subcategory of C. Choose ordinals alpha<beta strictly larger than every ordinal rank of an object in D. Infinity-type objects in D are allowed.

For a finite/ordinal-rank object D in that subcategory, both hom sets C(D,X_alpha) and C(D,X_beta) consist of precisely the same functions to {b,c}: the two source marks must go to b, and all remaining elements are unrestricted. For infinity-type D both hom sets are empty.

These identifications commute with precomposition, since composition is underlying function composition. Thus

    C(-,X_alpha)|D  is naturally isomorphic to C(-,X_beta)|D.

But X_alpha and X_beta are not isomorphic; there is no arrow in the reverse direction. Hence the restricted Yoneda functor on D cannot be fully faithful. No small full subcategory is dense.

In particular C cannot be equivalent to a full reflective subcategory of any small presheaf category. Such a reflection would give a small family L(y d) whose restricted nerve is fully faithful by the adjunction.

Therefore, if Sections 2–7 are correct, they give a counterexample to the literal strong-generator formulation AND to the boundedness deduction asserted in the original comments. They do NOT give a counterexample already inside the reflective formulation. This is not a distinction to hide or repair by assuming the published equivalence without proof.

## 9. Published statements that must be reconciled

1. Adamek–Rosicky, Open Problems, p.295, Problem 3 explicitly uses a cocomplete category and a strong generator of generated objects. It states a positive answer under Vopenka's principle using boundedness.
2. Page 296 explicitly asserts equivalence with the reflective/LFP/union-closed formulation and claims that closure of the generated strong generator under lambda-small colimits is dense.
3. Positselski–Rosicky (2018), Nearly Locally Presentable Categories, introduction pp.253–254, repeats the Vopenka-positive statement and the question whether additional set theory is needed.
4. The author-hosted corrections document dated March 2026 was checked. It contains numerous corrections, but no correction resolving this particular Problem-3 discrepancy was located. In particular its correction of another colimit-density theorem is not automatically a correction of Problem 3.
5. Boerger–Tholen (1990), Example 4.3, provides a related ordinal-tagged construction with a strong generator and non-small strong quotients. We checked pp.223–224 as page images. This is relevant prior art, not independent confirmation of Sections 4–5 above and not evidence that the authors claimed it solved P3.

At present the proposed elementary arguments and these published claims have not been reconciled. It would be irresponsible to silently erase the known positive statement or announce an independent ZFC solution. Conversely, merely citing the age of the problem is not an identification of an error in the construction. The next mathematical audit should pinpoint a failed universal property/definition, or verify that the boundedness claim needs additional hypotheses.

## 10. Finite computational audit (not an infinite proof)

The accompanying Python program enumerates objects with ranks 0,1,2,3 and carriers of sizes 2,3,4, and tests selected universal properties against all such targets. It does not use infinity-type objects and does not test any transfinite claim.

Results in this run:

* 260 composition-closure checks;
* 1,080 coequalizer/target universal-property checks;
* 432 coproduct/target universal-property checks;
* 12 representability checks;
* 410 monomorphism-via-G checks;
* 18 direct strong-epi lifting-square checks.

All passed. These are supplementary checks of formulas, NOT evidence for the proper-class conclusions in place of the proofs.

Files in the conversation sandbox:

    no3_counterexample_checks/ranked_pointed_sets_check.py
    no3_counterexample_checks/results.json

## 11. Priorities for an independent mathematical audit

(A) Check cocompleteness against targets of strictly larger rank, especially the fresh marked point in coequalizers and unattained-supremum coproducts.
(B) Check whether the directed-mono-colimit computation in Section 4 matches the exact meaning of 'generated' in P3.
(C) Check the natural identification C(G,-)=U and the strong-generator criterion; do not replace strong by dense.
(D) Check the proper-class strong-quotient family by its direct lifting property, not just by absence of proper subobjects.
(E) Check the original boundedness claim independently. The finite-colimit closure of rank-0 objects only reaches bounded ranks, which is exactly why the density claim is problematic here.

None of these is to be treated as externally verified merely because it has a proposed proof above.

## References

- J. Adamek and J. Rosicky, Locally Presentable and Accessible Categories, 1994, Open Problems pp.295–296. Exact user-provided PDF was re-read via the Files connector.
- R. Boerger and W. Tholen, Total Categories and Solid Functors, Canadian Journal of Mathematics 42(2) (1990), 213–229, Example 4.3, pp.223–225.
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A842E456CD7FFF30360076B3FB3134D4/S0008414X00003540a.pdf/total-categories-and-solid-functors.pdf
- L. Positselski and J. Rosicky, Nearly Locally Presentable Categories, TAC 33(10) (2018), 253–264, introduction.
  https://tac.mta.ca/tac/volumes/33/10/33-10.pdf
- Author-hosted List of Corrections, March 2026.
  https://math.fel.cvut.cz/en/people/adamekj/corrections.pdf
- M. Husek and J. Rosicky, Factorization and local presentability in topological and uniform spaces, Section 6. Definitions compared, not invoked to assert that the candidate is verified.
  https://www.math.muni.cz/~rosicky/papers/husek3.pdf


## Follow-up audit — 2026-11-17

See `original_density_gap_audit_2026-11-17.md` for the follow-up. Status of that audit: **DIRECT_DENSITY_COUNTERCALCULATION / PROOF_RECONSTRUCTED**, with independent review and author confirmation still pending.

The source conflict has now been localized more precisely. The published proof of Theorem 1.11 (printed p.18) factors two maps from a generator through one stage of the canonical FILTERED diagram using finite PRESENTABILITY. The Problem-3 comment on p.296 asserts a corresponding density conclusion for GENERATED objects, but the canonical diagram need not have monomorphic transitions.

For this candidate, the finite-colimit closure of G is exactly the small skeleton of finite-carrier objects of finite ordinal rank. For K=X_(omega+1), its canonical diagram has a cofinal chain Z_n=(n,{b,c,z}), whose transition maps send b,c to b and z to z. Its colimit is Z=(omega,{b,d,z}), with d the new distinguished point. The canonical comparison Z->K sends b,d to 0 and z to 1, and is NOT monic. The G-map selecting d does not factor through any canonical injection. This is an explicit failure of the claimed density, not merely a missing justification of one attempted proof.

The cocompleteness/generatedness/strong-generator calculations were rechecked without identifying a failure in this audit. They are still direct proposed proofs, not independently refereed results. Theorem 1.11 itself assumes presentability and is NOT refuted. Prior arguments assuming a full reflective presheaf presentation must retain that presentation as an independent hypothesis rather than silently deriving it from the literal Problem-3 hypotheses.
