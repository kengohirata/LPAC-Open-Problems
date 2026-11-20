# An intrinsic subobject of D outside both M and H_fg

2026-11-18. Status: PROOF_RECONSTRUCTED; independent audit requested. This is a ZFC counterexample to the proposed strengthening that M should be closed under subobjects satisfying finite tuple coding, left joint separation, first-sort FS-separation, and E(sigma)-orthogonality. It does not show failure of M's equalizer closure.

Put Omega=omega and let

    Z_*=(Omega --id,id--> Omega),       Z=E(Z_*).

Then Z_* belongs to C in ZFC, so Z belongs to D and M. Both sorts of Z are Omega^Omega, with left M_2 postcomposition and right M_1 precomposition, and both structural maps are identities.

Let A be its subpresheaf with both sorts

    A_i=Fin(Omega,Omega)
       ={f:Omega->Omega : im(f) is finite},

and again p_A=q_A=id. This is closed under both monoid actions.

**Theorem (ZFC).** A has all four listed intrinsic properties, but A is outside M and outside H_fg. In fact every map E(Y)->A, for arbitrary K-object Y, has only constant functions in its image.

## 1. The intrinsic properties hold

Finite tuple coding preserves A: the joint range of finitely many finite-image functions is finite, so applying any fixed coding bijection Omega^n->Omega again gives a finite-image function. Uniqueness and left joint separation are inherited pointwise from Omega^Omega.

First-sort FS-separation also holds directly. If f e_n=g e_n for every standard finite-rank truncation e_n, then for every k choose n>k to obtain f(k)=g(k).

Finally A is orthogonal to E(sigma):X=E(B)->E(U). Both Hom(X,A) and Hom(E(U),A) are empty. Indeed, a map out of X would send the identity generator of X_0=Omega^Omega to a finite-image function f satisfying

    f m=m f       for every m:Omega->Omega.

Taking m to be the constant map at n forces f(n)=n for every n. Thus f would be the identity, which does not have finite image. The same argument applies to the identity generator of E(U)_1=Omega^Omega. Consequently the orthogonality map is the bijection between two empty sets.

This explicitly shows how E(sigma)-existence can become vacuous: this subobject has no balanced first-sort element on which the existence clause can act.

## 2. A short direct proof that A is outside M

First observe that a monomorphism of M_2-sets

    phi:Omega^S -> Fin(Omega,Omega)

forces S finite. Otherwise choose a surjection h:S->Omega. The image phi(h) has finite range K. Choose a nonidentity selfmap r of Omega fixing K pointwise. Then

    phi(r h)=r phi(h)=phi(h),

so monicity gives r h=h. Surjectivity of h would make r the identity, a contradiction.

Suppose j:E(Q)->A is a monomorphism. The observation makes both Q_i finite. Neither Q_i can be empty, since a one-element trivial M_2-set has no map to Fin(Omega,Omega). For finite nonempty S, every M_2-map Omega^S->Omega is coordinate evaluation: take an injection h:S->Omega; equivariance under maps fixing im(h) puts the image of h in im(h), and every f:S->Omega is m h for some m.

Apply this fact to the coordinate maps of the composite E(Q)->A->E(Z_*). They give an actual K-map

    u:Z_* -> Q

whose E-image is that composite. Monicity forces u to be componentwise onto.

The M_1-set Omega has only the equality and total congruences. If an equivariant quotient identifies distinct a,b, then for arbitrary c,d choose m with m(a)=c and m(b)=d; equivariance identifies c,d. Since each Q_i is finite, an onto map Omega->Q_i must therefore have singleton image. Thus both Q_i are singleton, and j has only constant functions in its image.

The nonconstant binary function chi_{0} belongs to A. No monic D-image covers it, so A does not belong to M. No full-faithfulness assumption N was used.

## 3. Every full-power map into A has constant image

The preceding argument used monicity. The following strengthens it to arbitrary maps and proves A is outside H_fg.

### Scalar maps and ultrafilters

Every M_2-map ell:Omega^S->Omega determines an ultrafilter

    U_ell={T subset S : ell(chi_T)=1}.

It preserves finite pointwise operations: code a finite tuple by a bijection with Omega and use its unary coordinate projections. Hence U_ell is indeed an ultrafilter. Moreover, for every f:S->Omega,

    f^(-1)({ell(f)}) belongs to U_ell,                    (1)

by applying the unary indicator of ell(f). Thus the ultrafilter uniquely determines ell. This also shows that U_ell is countably complete, although only (1) is needed below. The case S empty admits no such ell.

### Finitely many coordinate maps

Let phi:Omega^S->Fin(Omega,Omega) be any M_2-map and write

    ell_n=ev_n phi.

There are only finitely many distinct ell_n. Otherwise their distinct ultrafilters form an infinite subset of the Stone space of P(S). One can choose a sequence of them, U_(n_k), and pairwise disjoint subsets T_k of S with T_k in U_(n_k). For completeness, repeatedly split an infinite remaining family by a clopen set into a nonempty part and an infinite part, retain the former as the next disjoint clopen and continue inside the latter; choose one ultrafilter in each retained part.

Define f:S->Omega by f=k+1 on T_k and f=0 outside their union. Equation (1), or the unary indicator of k+1, then gives

    ell_(n_k)(f)=k+1.

This contradicts the finite range of phi(f).

### Right equivariance makes all coordinates equal

Now assume S is an M_1-set and phi also respects the right M_1 action. Define n~n' when ell_n=ell_(n'). This is an M_1-congruence on Omega, since

    ell_(m n)(f)=ell_n(f·m).

It has finitely many equivalence classes by the preceding paragraph. The simplicity argument from Section 2 makes it the total congruence. All ell_n are therefore equal, so every function phi(f) is constant.

Applying this to either component of a P-map E(Y)->A proves the strengthened assertion of the theorem. If the finitely generated subpresheaf of A generated by chi_{0} factored through any D-object, its image in A would consequently consist of constant functions, a contradiction. Hence A is outside H_fg in ZFC.

## 4. Consequences and exact limitation

We have an explicit inclusion

    A -> Z in D subset M

where A satisfies all the proposed intrinsic conditions but fails even H_fg membership. Therefore intersecting a D-subobject cover with such an intrinsic subobject cannot in general be repaired to a monic C-quotient cover. For the seed chi_{0}, every available full-power map into the intersection has constant image.

The obstruction arises before any cardinal-rank issue: E(sigma)-orthogonality is vacuous on A. Thus an attempted proof of relative subobject closure must add a hypothesis that excludes this loss of balanced elements, or use a property of actual equalizers stronger than the four listed intrinsic conditions.

This is not an equalizer counterexample for M. In fact A->Z is epic relative to every left-joint-separated target: if a,b agree on A, then for every f the finite-image functions e_n f lie in A, so e_n a(f)=e_n b(f) for all n and hence a(f)=b(f). Thus A cannot be a proper equalizer with any such codomain. The stronger relative-subobject closure proposal is false; the original equalizer-closure question remains separate.

The [truncation-closed subobject reduction](truncation_closed_subobjects_and_sigma_boolean_reduction_2026-11-18.md) isolates the missing membership condition and proves a positive theorem for countable dual sources.

## 5. An exact equalizer classification at this source

There is a sharper distinction from actual equalizers. Recall the class L_full from [the antichain strengthening](antichain_seed_cannot_survive_in_m_targets_2026-11-18.md), Section 6: every ambient fg subpresheaf embeds into some E(Y), with Y arbitrary. It contains H_fg and LimUnion(D).

**Proposition (ZFC).** For any W in L_full and f,g:Z=E(Z_*)->W, their equalizer, as a subobject of Z, is one of:

    Z itself;
    X=E(B), whose sort 0 is Omega^Omega and sort 1 is the constants;
    E(T), the constants in both sorts, with T=(1 --id,id--> 1).

If W is also E(sigma)-orthogonal, the middle case is impossible. Thus all such equalizers belong to D even under these weaker target hypotheses.

Proof. The subpresheaf I of W generated by im(f) and im(g) is fg, because Z is fg. Choose a monomorphism I->E(Y) by L_full. Composing f and g with it does not change their equalizer. Every map E(Z_*)->E(Y) is E of a K-map Y->Z_* in ZFC: each scalar component Omega^Omega->Omega is evaluation at the image of the identity function. Thus the equalizer is E(Q), where Q is the K-coequalizer of two maps Y->Z_*.

Each Q_i is a quotient of the simple M_1-set Omega, hence is Omega or 1. Naturality with the identity structural arrows implies that if Q_0=1 then Q_1=1, and otherwise the two quotient structural arrows coincide. The possibilities for Q are exactly Z_*, B=(Omega⇉1), and T, yielding the stated list.

Orthogonality to a fixed map is preserved by all limits. Since Z is E(sigma)-orthogonal, so is its equalizer into an E(sigma)-orthogonal W. But X is not E(sigma)-orthogonal: it has a balanced element in sort 0 and none in sort 1. This excludes the middle case. □

Equivalently, let B_2 be the subpresheaf of Z consisting of functions with at most two values in both sorts. It is generated by chi_{0}. If two maps Z->W, W in L_full, agree on B_2, they agree everywhere: neither proper equalizer in the list contains B_2. Hence the inclusion A->Z, which contains B_2, is epic relative to all L_full targets. It cannot be a proper equalizer with such a codomain.

Thus the finite-image example identifies a genuine failure of intrinsic-subobject closure while also giving a concrete safe equalizer theorem. The local ability to embed the two fg images into a full power is stronger than the four intrinsic conditions and is exactly what the classification uses.
