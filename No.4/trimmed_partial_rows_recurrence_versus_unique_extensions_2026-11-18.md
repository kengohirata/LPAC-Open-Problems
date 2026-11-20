# Trimmed partial rows: recurrence versus uniqueness of character extensions

2026-11-18. Status: PROOF_RECONSTRUCTED; another research agent independently reconstructed the full argument and found no gap. Not externally reviewed or formally verified. This gives a precise obstruction model for the trimmed ordinal route. It is not an actual monomorphism into the tail quotient and not a No.4 counterexample. The model simultaneously has recurrence of every point in both sorts, countable mixed-fibre consistency, and the two selected moving marks. Its exact failure is injectivity of H(p).

Let lambda be a regular uncountable cardinal admitting an unbounded set of t<lambda with cf(t)>omega; in particular lambda=c^+ works. Put X=[0,lambda], let d_X be successor with the endpoint fixed, and use the trimmed source

    R_0=C(X,omega),
    R_1={r:X->omega : r is constant on some [beta,lambda]},
    p_R=inclusion, q_R=d_X^*.

These are the carriers of the [trimmed ordinal template](trimmed_ordinal_templates_bound_both_witness_sorts_2026-11-18.md). The constructions below are ZFC; identifying all characters of R and asserting R in C uses N as in that note.

## 1. A target with two ordinal blocks

Let T=[0,lambda+lambda], with successor d_T and fixed endpoint. Define

    Y_0=C(T,omega),
    Y_1={f:T->omega :
           f is eventually constant on [0,lambda), and
           f is constant on some final segment including lambda+lambda}.

The first eventual-constancy requirement does not constrain f(lambda). Put p_Y=inclusion and q_Y=d_T^*. These arrows land in Y_1, and Y_1 is M_1-stable. The first sort is finite-support.

For t<lambda of uncountable cofinality, let

    (D_t)_0=R_0,
    (D_t)_1={r in R_1 : r is eventually constant on [0,t)}.

This is an M_1-stable partial K-subobject of R containing both structural images. Write L_t(r) for the eventual value below t. Define the continuous map l_t:T->X by

    l_t(xi)=min(xi,t)          (xi<lambda),
    l_t(lambda+alpha)=t+alpha (alpha<=lambda).

Here alpha -> t+alpha is the order isomorphism [0,lambda] -> [t,lambda], and t+lambda=lambda. Define q_t:D_t->Y by

    q_(t,0)(g)=g composed with l_t,

    q_(t,1)(r)(xi)=r(xi)                  (xi<t),
                       L_t(r)            (t<=xi<lambda),
                       r(t+alpha)        (xi=lambda+alpha).

The second formula lies in Y_1. It commutes with postcomposition because eventual values do. For continuous g, eventual g below t is g(t), so q_t respects p. For the q-arrow, eventual d_X^*g below t is again g(t). On the first plateau d_T stays in that plateau, and on the second block

    l_t(d_T(lambda+alpha))=d_X(l_t(lambda+alpha)).

These identities, together with the identical calculation below t, prove that q_t is a partial K-map. Thus both structural arrows are respected, rather than only p.

## 2. Every point in both target sorts recurs

Fix f in Y_1 and choose beta<lambda beyond its stabilization threshold on the first block. For every t>beta of uncountable cofinality define r on X by

    r(xi)=f(xi)                      (xi<t),
    r(t+alpha)=f(lambda+alpha)        (alpha<=lambda).

The order isomorphism [0,lambda]->[t,lambda] makes this definition unambiguous and exhaustive. The function r lies in R_1, is eventually constant below t, and satisfies q_(t,1)(r)=f. Hence every target second-sort point occurs in every sufficiently late eligible row.

If f is continuous on T, the same r is continuous on X: continuity at t follows because the first-block eventual value is f(lambda), which is also the value assigned to r(t). Continuity elsewhere follows from the two continuous pieces. Thus every point in Y_0 likewise occurs in every sufficiently late eligible row.

This is stronger than unbounded recurrence and includes all second-sort labels, not only the structural images.

## 3. Exact selected marks and countable mixed-fibre consistency

Use the evaluation characters a_xi=ev_xi of Y_0 and, for now, their evaluation extensions s_xi=ev_xi on Y_1. Let

    h=a_0,       k=a_lambda.

For h the mixed row is evaluation at 0, and for k it is evaluation at t. Their finite successor iterates also have exact evaluation rows: h+n is evaluated at n once t>n, while k+n is evaluated at t+n. More generally every character in the second block is evaluated exactly on every row; any fixed character in the first block is evaluated exactly on all sufficiently late rows.

Any chosen set of fewer than lambda first-block evaluation characters is bounded in lambda. Taking t above that bound therefore makes all its mixed rows genuine point evaluations simultaneously. This reproduces the selected-character feature that the simpler min-truncation model failed to satisfy.

For an arbitrary a_xi, consider all equations

    g(eta)=a_xi(q_(t,0)(g)),
    r(eta)=s_xi(q_(t,1)(r)),

for g in R_0 and r in (D_t)_1. Outside the first plateau t<=xi<lambda they are all realized by eta=l_t(xi). On that plateau the prescribed values are g(t) and L_t(r). Every countable family of these equations is realized by some eta<t: use cf(t)>omega to exceed all countably many stabilization thresholds. Thus all mixed families have the countable intersection property.

Nevertheless the full mixed family at a plateau character has no common point. All continuous observations force eta=t. But

    r=chi_[0,t)

belongs to (D_t)_1, has L_t(r)=1, and has r(t)=0. This excludes the only point selected by the first sort. Notice that this r is allowed in the trimmed source: it is zero on [t,lambda], including the endpoint.

## 4. The exact failure: two extensions at the middle ordinal

There are two distinct M_1-equivariant maps Y_1->omega:

    epsilon(f)=f(lambda),
    ell(f)=the eventual value of f on [0,lambda).

Both restrict to ev_lambda on the continuous first sort. They are distinct, as witnessed by f=chi_[0,lambda), extended by zero on the second block. Therefore

    H(p_Y):H(Y_1)->H(Y_0)

is not injective, and Y is not in C.

In particular, the evaluation extension used for k in Section 3 is not unique. The other extension ell would give the non-evaluating plateau profile. An actual C-witness cannot make this choice: uniqueness identifies the two extensions, and the displayed function prevents that identification in this model.

The second-sort carrier above is exactly large enough for all the displayed row images to recur. Enlarging it to all trimmed functions on T removes the automatic definition of ell, but then points whose restriction to [0,lambda) is not eventually constant are never in any row image. Such an enlargement loses recurrence of all second-sort atoms.

Thus this particular construction cannot satisfy recurrence and C-membership simultaneously. It shows why both conditions matter: recurrence alone, even together with all selected-character equations and countable mixed-fibre consistency, does not force the remaining fibres to have a common point. The actual trimmed-tail problem retains the additional unique-extension condition, which excludes this concrete obstruction model. No general elimination theorem for all partial-row systems is asserted.
