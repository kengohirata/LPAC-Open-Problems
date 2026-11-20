# All evaluation seeds in ordinal-template tail quotients have monic D-witnesses

2026-11-18. Status: PROOF_RECONSTRUCTED; independently checked by a second research agent, not externally reviewed or formally verified. This excludes a concrete larger-cardinal counterexample strategy. It does not prove M-membership of the whole tail quotient.

Use the ordinal diagrams

    Y_kappa=(Cont([0,kappa],omega_discrete) --p,q--> omega^[0,kappa]),
    p=inclusion, q(f)=f composed with d_kappa,

where d_kappa(alpha)=alpha+1 for alpha<kappa and d_kappa(kappa)=kappa. Finite ordinals, including kappa=0, are allowed. Assume that the diagrams used below lie in C. This follows from N for arbitrary ordinal indices; no separate No.1 non-coreflectivity input is used.

Let lambda be a regular infinite cardinal and (kappa_t)_(t<lambda) any ordinal family. Form

    W=colim_(beta<lambda) E(coproduct_(t>=beta) Y_(kappa_t)).

For each t choose an arbitrary point xi_t∈[0,kappa_t]. The row evaluation maps psi_(xi_t):Y_(kappa_t)→B determine a map f:X=E(B)→W.

**Theorem.** This f factors through a monomorphism E(Y*)↪W with Y*∈C. Neither monotonicity of kappa_t nor coherence of the marked points xi_t is required.

## 1. Rebase each evaluation at the initial point

The closed interval [xi_t,kappa_t] has a unique ordinal order type [0,eta_t]. Let

    a_t:[0,eta_t]→[xi_t,kappa_t]⊂[0,kappa_t]

be the order isomorphism. It is continuous and commutes with the respective successor maps, including their fixed endpoints. Precomposition gives a K-map

    r_t:Y_(kappa_t)→Y_(eta_t).

This map is componentwise surjective. An arbitrary function on the closed interval extends to the whole ordinal by a constant value on the initial segment. If the original function is continuous, extending constantly with its value at xi_t also gives a continuous function. Therefore surjectivity holds for both sorts.

The original evaluation factors as

    psi_(xi_t)=psi_0 r_t.

## 2. Canonical inclusions of the rebased diagrams

For alpha<=gamma, the truncation map

    b_(alpha,gamma):[0,gamma]→[0,alpha],
    b_(alpha,gamma)(zeta)=min(zeta,alpha)

is continuous and commutes with the successor maps with fixed endpoints. Precomposition gives a componentwise injective K-map

    i_(alpha,gamma):Y_alpha↪Y_gamma.

It extends functions constantly after alpha. These maps compose coherently and preserve evaluation at 0.

## 3. An eventual supremum gives a recurrent target

The ordinal-valued function

    beta↦sup{eta_t:t>=beta}

is nonincreasing, and its range has a minimum. Hence after some beta_0 it is constant; call the constant eta*.

There are two cases.

If eta_t=eta* for unboundedly many t, put Y*=Y_(eta*). Every remaining eta_t is at most eta*, so the maps i_(eta_t,eta*) are defined. Every point of Y* belongs to the image for unboundedly many t, namely the t with eta_t=eta*.

Otherwise, discard the bounded set of occurrences eta_t=eta*. All remaining eta_t are below eta*. In this case eta* is a nonzero limit ordinal. Put

    Y*=colim_(alpha<eta*) Y_alpha

using the coherent inclusions from Section 2. Then Y*∈C by colimit closure. Every point y of either sort is represented in some Y_alpha, alpha<eta*. The set of t with eta_t>=alpha is unbounded: otherwise a later tail supremum would be at most alpha<eta*. Thus y belongs to the image of Y_(eta_t)→Y* for unboundedly many t.

In either case, after discarding one initial tail we have K-maps

    q_t:Y_(kappa_t) --r_t onto--> Y_(eta_t)→Y*

such that every point of Y* is in im(q_t) for unboundedly many t. The compatible evaluations at 0 induce g:Y*→B, and g q_t=psi_(xi_t).

## 4. Dualization gives the monic witness

The q_t combine to a K-map from a tail coproduct to Y*, hence give

    E(Y*)→W.

This map is monic: if two functions on a component of Y* differ at a point y, their pullbacks differ in unboundedly many columns, because y occurs in unboundedly many im(q_t). Their germs cannot be equal.

Dualizing g:Y*→B gives the desired factorization

    X --E(g)--> E(Y*)↪W

of f. This proves the theorem.

## 5. Every X-map is covered when lambda>c

Suppose additionally lambda>c. Then X is lambda-presentable, so every X→W factors through one tail stage. Since the coordinate sets of B are countable, the countable-index Isbell calculation gives, in ZFC,

    Hom_P(X,E(coproduct_t Y_(kappa_t)))
      ≅ Hom_K(coproduct_t Y_(kappa_t),B).

Each component map Y_(kappa_t)→B is evaluation at some xi_t: the equivariant maps from Cont([0,kappa_t],omega) to omega are precisely point evaluations. Applying Sections 1–4 proves that every X→W is monically D-covered.

Consequently, increasing ordinal sizes or moving the marked evaluation points do not produce an M-obstruction at the fixed source X in these tail quotients. A different finitely generated source, or a different family of C-diagrams, is needed to detect possible failure.

This does not contradict the explicit H_fg\M example based on Y_omega: that example uses a sort-1 characteristic-function seed, not an evaluation X-seed.
