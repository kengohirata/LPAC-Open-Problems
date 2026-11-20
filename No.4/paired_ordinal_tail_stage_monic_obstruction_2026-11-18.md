# Two ordinal evaluation seeds exclude every stage-induced monic C-witness

2026-11-18. Status: PROOF_RECONSTRUCTED; independently checked by a second research agent, not externally reviewed or formally verified. This is a C-specific obstruction valid for arbitrarily large regular tail cardinals. It excludes stage-induced monic witnesses, not arbitrary nonlifting monic witnesses. No general M-nonmembership or filtered-colimit failure above 2^c is claimed.

Assume N, so the ordinal templates Y_kappa lie in C and their second-sort equivariant maps to omega are point evaluations. No No.1 non-coreflectivity or factorization lower-bound input is used.

Fix a regular lambda>c and put R=Y_lambda. Form the tail quotient

    W=colim_(beta<lambda) E([beta,lambda)·R)∈H_fg.

For each t<lambda let the two row maps R→B be evaluation at 0 and at t. They define two maps X→W, hence a finitely generated test map

    f:X coproduct X→W.

**Theorem.** This f does not factor through any monomorphism j:E(Y)↪W, Y∈C, for which j factors through a tail stage. Under N, every such stage map is E(q) for an actual K-map q:[beta,lambda)·R→Y.

## 1. What a hypothetical stage-induced witness supplies

Suppose the required factorization exists. The two maps X→E(Y) correspond to equivariant maps

    h,k:Y_0→omega.

After increasing the initial tail index to beta_0 to make the two germ equalities hold pointwise, the row maps q_t:R→Y, t>=beta_0, satisfy

    h q_(t,0)=ev_0,
    k q_(t,0)=ev_t.                                  (1)

Monicity of E(Y)→W implies that every y∈Y_0 occurs in im(q_(t,0)) for unboundedly many t. Otherwise the zero function and chi_{y} on Y_0 would have the same image germ.

## 2. The induced dynamical maps on the compact spectrum

Let

    T=H_1(Y_0),    S=H_1(Y_1),
    u=H_1(p_Y):S→T,
    D=H_1(q_Y)u^(-1):T→T.

The set T is a compact Hausdorff Stone space because Y_0 is finite-support. The inverse u^(-1) exists as a set map by C-membership. No continuity of D is assumed.

Each q_t induces a continuous map

    l_t:T→[0,lambda],    l_t=H_1(q_(t,0)),

using H_1(R_0)≅[0,lambda]. Naturality with the two diagram arrows and the evaluation identification H_1(R_1)≅[0,lambda] imply

    l_t D=d_lambda l_t.

Equation (1) becomes

    l_t(h)=0,    l_t(k)=t.                            (2)

## 3. A single transfinite orbit seen by every row

Construct a_beta∈T for beta<=lambda by transfinite recursion. Put a_0=h and a_(beta+1)=D(a_beta). At a nonzero limit beta, choose an ultrafilter on beta containing every final segment and let a_beta be the corresponding ultrafilter limit of (a_alpha)_(alpha<beta) in the compact Hausdorff space T.

For every t>=beta_0 and every beta<=lambda,

    l_t(a_beta)=beta.                               (3)

The successor step follows from commutation with d_lambda. At a limit, continuity of l_t takes the chosen ultrafilter limit to the ultrafilter limit of alpha<beta in [0,lambda], which is beta. This argument does not require D to be continuous.

## 4. Recurrence turns the transfinite orbit into a continuous curve

Fix y∈Y_0. By recurrence, choose some t and g∈R_0=Cont([0,lambda],omega) with q_(t,0)(g)=y. Equation (3) gives, for every beta<=lambda,

    a_beta(y)=a_beta(q_(t,0)(g))=g(l_t(a_beta))=g(beta).

Thus the scalar function beta↦a_beta(y) is continuous on [0,lambda]. In particular, it is eventually constant at its endpoint value a_lambda(y).

For unboundedly many t, recurrence supplies a (possibly different) g_t∈R_0 with q_(t,0)(g_t)=y. For each such t, the same argument identifies g_t(beta)=a_beta(y) for all beta, and (1) gives

    k(y)=g_t(t)=a_t(y).

Choose such a t beyond the eventual-constancy threshold for this y. Then k(y)=a_lambda(y). Since this holds for every y∈Y_0, we have k=a_lambda.

But (2) and (3) now imply

    t=l_t(k)=l_t(a_lambda)=lambda

for every remaining t<lambda, a contradiction. This proves the theorem.

## 5. Exact remaining gap

The argument is not limited by the 2^c possible local M_1-orbit types: it uses the compact spectrum H_1(Y_0), C's unique-extension condition, and an entire transfinite orbit. Therefore it works for arbitrarily large regular lambda.

However, constructing the continuous maps l_t:T→[0,lambda] required actual row maps q_t:R→Y. For a general monomorphism E(Y)→W which does not factor through a tail stage, such row maps have not been produced. Singleton indicators recover only the relevant finitely or c-many equations on a common tail; they do not by themselves produce one common system of row maps for all points of H_1(Y_0).

Consequently the theorem leaves open whether f admits a genuinely nonlifting monic C-witness. Excluding those witnesses would prove an M-obstruction at every regular lambda>c. Their existence would instead provide a concrete family in which the local monic witness necessarily has no stage representation.

The single-evaluation repair in [the preceding ordinal note](ordinal_tail_evaluation_seeds_have_monic_witnesses_2026-11-18.md) does not apply to this pair: rebasing at the moving second mark no longer preserves evaluation at 0.

## 6. A normalization of arbitrary hypothetical paired witnesses

There is a useful normalization that does not require stage lifting. For any Y∈C, identify two points in either sort when every equivariant map from that sort to omega takes the same value on them. These equivalence relations respect the M_1-actions and both diagram arrows, so they give a componentwise onto K-map

    q:Y→Y_obs.

Every original equivariant map descends by construction, and precomposition with the surjection is injective. Hence each H_1(q_i) is bijective. The natural square for p therefore shows H_1(p_(Y_obs)) is bijective; finite support of its first sort is inherited from Y_0. Thus Y_obs∈C.

Both sorts of Y_obs are separated by their equivariant omega-valued maps. Consequently p_(Y_obs) is injective: if two first-sort points have the same p-image, surjectivity of H_1(p) makes all equivariant first-sort maps agree on them, so they coincide.

The two maps h,k:Y_0→omega defining an X coproduct X seed descend to Y_obs. Therefore a hypothetical monic witness E(Y)↪W can be replaced by

    E(Y_obs) --E(q) mono--> E(Y)↪W

without losing the seed. This is a ZFC construction once Y∈C is given.

Writing T=H_1((Y_obs)_0), the normalized diagram can be viewed as

    (Y_obs)_0 ⊂ Cont(T,omega),
    (Y_obs)_1 ⊂ omega^T,

with p an inclusion and q given on first-sort functions by precomposition with D=H_1(q)H_1(p)^(-1). These subsets need not be the full function spaces, and D need not be continuous. The normalization supplies no uniform carrier bound and no stage lifting; it only removes points invisible to all equivariant scalar observations.
