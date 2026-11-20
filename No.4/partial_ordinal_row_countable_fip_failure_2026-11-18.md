# A partial ordinal row can fail countable intersection compatibility

2026-11-18. Status: PROOF_RECONSTRUCTED; independently checked by another research agent, not externally reviewed or formally verified. This is an explicit obstruction to deducing countable completeness or successor compatibility from partial C-row data alone. It is not asserted to arise from an actual full-power monomorphism into a tail quotient.

Fix an ordinal kappa>=omega+1. Write X=[0,kappa], d for its successor map, and

    R=Y_kappa=(C(X,Omega) --inclusion,d*--> Omega^X).

Let D be the partial-row K-object

    D_0=C(X,Omega),       D_1=Fin(X,Omega),

with the inherited two arrows. The arrows do land in D_1 because continuous discrete-valued functions on compact X have finite image, and precomposition by d preserves finite image.

Choose a free ultrafilter U on omega. Define q_0=id and q_1:D_1->Omega^X by

    q_1(r)(xi)=r(xi)                 if xi!=omega,
    q_1(r)(omega)=lim_U r|omega.

The ultrafilter value exists because r has finite image. It commutes with every postcomposition by M_1, so q_1 is equivariant.

## 1. An actual C-target and partial K-map

Let tilde_d agree with d except that tilde_d(omega)=omega, and put

    Y=(C(X,Omega) --inclusion,tilde_d*--> Omega^X).

The map q=(q_0,q_1):D->Y is a K-map. It fixes every continuous first-sort function, because continuity at omega gives lim_U g(n)=g(omega). Moreover

    q_1(d*g)(omega)=lim_U g(n+1)=g(omega)
                  =(tilde_d*g)(omega),

and the two sides agree at every other coordinate as well.

The p-arrow of Y is unchanged from Y_kappa, so Y belongs to C whenever Y_kappa does. Taking kappa=omega+1 gives an entirely ZFC example: both relevant evaluation index spaces are countable. For arbitrary kappa the standing N hypothesis suffices, as in the ordinal-template construction. The map tilde_d need not be continuous for this C-membership statement; C's unique-extension condition uses p, not q.

## 2. Finite intersection compatibility without countable compatibility

Let h=ev_omega in H(Y_0). Its unique extension to Y_1 is also ev_omega. For k in omega put

    r_k=chi_[k,omega),

where the interval contains only natural ordinals and excludes omega. Then r_k belongs to D_1 and

    h_extended(q_1(r_k))=1       for every k.

Every finite collection of equations r_k(xi)=1 is realized by a sufficiently large natural ordinal xi. But

    intersection_k r_k^(-1)({1})=empty.

Thus the second-sort fibre family specified by the unique C-extension has the finite intersection property and fails the countable intersection property.

The entire mixed first/second-sort family still has the finite intersection property. Each selected fibre of an arbitrary finite-image r belongs to U, while each continuous first-sort equality holds on a cofinite set of naturals. Any finite intersection therefore remains in U and is nonempty. In particular one may choose a large natural n for finitely many continuous g_j and the displayed r_k constraints. However the full first-sort observations force the only possible evaluation point to be omega, where every r_k has value zero. Hence no evaluation extends the full mixed row.

## 3. The dynamical defect is visible even with a perfect first row

The first-sort row is the identity on all continuous functions. Its spectral map is therefore the identity map on [0,kappa], with no selection issue whatsoever. Nevertheless the target dynamics is tilde_d, while the source dynamics is d, and these differ at omega. The partial second row has converted the successor at omega into a fixed point by an ultrafilter limit.

Consequently a full first-sort row, equivariance, compatibility with both arrows on the partial domain, and membership of the target in C do not imply either countable mixed-fibre compatibility or intertwining with the original successor map.

An actual monomorphism E(Y)->W provides substantially more data: its images of all full-power functions preserve the encoded countable-partition relations. Any argument repairing the paired-tail obstruction must use such additional origin conditions. The example above establishes the insufficiency of abstract partial rows; it does not show that this particular row can be extracted from an actual monomorphism.

## 4. Countable intersection compatibility still does not force an evaluation

There is a stronger companion example. Let lambda be regular uncountable and put X=[0,lambda]. Let

    D_0=C(X,Omega),
    D_1={r:X->Omega : r is eventually constant on [0,lambda)},

allowing an arbitrary value at the endpoint lambda. This is an M_1-subact of Omega^X. Both arrows of Y_lambda restrict to D: continuous functions are eventually constant below lambda, and composition with successor preserves their eventual value and endpoint value.

Define q:D->Y_lambda by q_0=id and

    q_1(r)(xi)=r(xi)                 if xi<lambda,
    q_1(r)(lambda)=the eventual value of r below lambda.

This is equivariant and compatible with both p and the original successor arrow q. It fixes all continuous functions and also fixes d*g for continuous g, including their endpoint values. Thus, unlike the earlier ultrafilter example, it does not alter the target dynamics at all. Target membership in C follows under N, as for Y_lambda; the partial-map construction itself is ZFC.

For h=ev_lambda, its unique extension after q_1 assigns each r its eventual value below lambda. Every countable family of these fibre conditions is simultaneously realized by a point xi<lambda: take xi beyond the supremum of their countably many stabilization thresholds. This includes all countable mixed first/second-sort families.

Nevertheless no point realizes the full family. The continuous first-sort functions force xi=lambda, while the second-sort element

    r=chi_[0,lambda)

has assigned value 1 and satisfies r(lambda)=0. Thus the full mixed fibre is empty.

The resulting fibre constraints generate the proper countably complete filter of sets containing a final segment below lambda, with the endpoint excluded. A countably complete ultrafilter extension is not automatic. Under N there is no nonprincipal countably complete ultrafilter on the full powerset of [0,lambda), while no principal ultrafilter contains every such final segment.

Consequently even a full first row, compatibility with the unchanged successor dynamics, and the countable intersection property do not supply the evaluation extension needed for a genuine full row. This is the exact residual obstruction after an actual-monomorphism argument has improved finite intersection compatibility to countable compatibility. It still does not assert that the displayed partial row itself comes from an actual full-power monomorphism.

## 5. A lambda-sized version and the missing atomic labels

The domain in Section 4 can be reduced to cardinality lambda. Put

    S_0=p(R_0) union q(R_0),
    K_0={continuous g:X->Omega with an arbitrary replacement of g(lambda)},
    D_1=S_0 union K_0.

Both parts are M_1-stable, and their union has cardinality lambda. It contains both required structural images. The endpoint-correction map fixes S_0 and sends K_0 into p(R_0), so

    q_1(D_1)=p(R_0) union q(R_0),

also of size lambda. The element chi_[0,lambda) belongs to K_0 and is sent to the constant-one function. All the countable-intersection and non-realization statements from Section 4 remain valid.

This small-image version makes one additional limitation visible. The target point chi_[0,lambda) itself is never an image label of q_1. An actual monomorphism would have a nonzero singleton indicator for that target point and would require its atomic support to recur on unboundedly many retained rows. Thus this fixed partial model cannot supply the full recurring atomic data for every target point. Including additional atomic labels outside p(R_0) union q(R_0) is precisely extra information that may invalidate the model; such labels can themselves be finite-support, as chi_[0,lambda) is here. The example concerns what the selected first-sort and structural-image labels alone can establish.
