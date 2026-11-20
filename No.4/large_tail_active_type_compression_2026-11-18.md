# Large tail quotients: small full-power witnesses and the remaining C condition

2026-11-18. Status: PROOF_RECONSTRUCTED; no external or formal verification. This complements the explicit c^+-tail separation. It does not establish M-membership or nonmembership for arbitrarily large tails.

Write c=2^aleph_0. Let lambda be regular with lambda>2^c, and let (R_t)_(t<lambda) be any family of C-objects. Put

    Z_beta=E(coproduct_(beta<=t<lambda) R_t),
    W=colim_(beta<lambda) Z_beta,

using tail restriction maps. All Z_beta lie in D, and W∈H_fg by sufficiently-filtered-colimit closure.

## 1. Uniform full-Isbell compression, independent of the template sizes

**Proposition (ZFC).** Every map f:F→W from an ambient finitely generated F factors as

    F→E(S)↪W,

where S is a K-object with total carrier at most 2^c, S_0 is finite-support, and H_1(p_S) is injective. Surjectivity of H_1(p_S) is not asserted.

### Proof

Since F is c^+-presentable, f factors through some tail stage Z_beta. Transpose this stage factorization to

    u:coproduct_(t>=beta) R_t→Q(F),

and write u_t:R_t→Q(F) for its restrictions. Each component of Q(F) has cardinality at most 2^c.

For each sort i, call s∈Q(F)_i active if

    {t>=beta : s∈im(u_(t,i))}

is unbounded in lambda. Let S_i be the active elements. There are fewer than lambda inactive elements in both sorts together, and the occurrence set of each is bounded. Regularity gives one gamma>=beta beyond all their occurrences.

The S_i form a K-subobject S⊂Q(F). Indeed, if an element occurs unboundedly often, so does its image under any M_1 operation or either diagram arrow, because every u_t is a K-map. For t>=gamma, the maps u_t land in S. Write

    q:coproduct_(t>=gamma) R_t→S

for the resulting map. Every element of S still occurs in unboundedly many of its component images.

The composite E(S) --E(q)--> Z_gamma→W is monic. Distinct functions on S_i differ at some s∈S_i; their pullbacks then differ in unboundedly many columns, so their germs remain distinct. Transposition of u followed by its factorization through S gives the desired factorization of f through this monomorphism.

Every element of S_0 is the image of an element of some (R_t)_0 and therefore has finite support. Finally, suppose h,h':S_1→omega are equivariant and h p_S=h' p_S. Precomposition with u_t gives two equivariant maps (R_t)_1→omega agreeing after p_(R_t). Since R_t∈C, they agree. The images of all u_(t,1), t>=gamma, jointly cover S_1, so h=h'. Hence H_1(p_S) is injective. □

The proof allows different and arbitrarily large R_t. Its threshold depends only on the ambient finitely generated test size and the fixed signature, not on the cardinalities of the templates.

## 2. The remaining obstruction is precisely extension across p_S

Given h_0:S_0→omega equivariant, each composite h_0 u_(t,0) has a unique extension h_(1,t):(R_t)_1→omega across p_(R_t). For h_0 to extend to S_1, these extensions must agree whenever two points, in the same or different tail copies, have the same image under u_(t,1).

No such agreement follows merely from the active-type construction. Thus the proposition proves the finite-support condition and uniqueness condition for C, but leaves its existence condition unresolved.

This is a real gap in that implication: the active image can be B=(omega⇉1), which is outside C. Take all R_t=Z_*=(omega --id,id--> omega), and all row maps u_t=s:Z_*→B with s=(id,!). Use the finitely generated F=X=E(B); its double dual identifies with B because both B components are countable. Every B-point occurs in every row, so the active image is exactly B.

Nevertheless this example's W lies in M by the fixed countable-template tail theorem. The monic X=E(B) subobject is covered by a different D-subobject, namely the constant-row copy of E(Z_*). Therefore exhibiting an active S outside C does not establish W∉M.

## 3. Why the c^+-antichain proof cannot simply be scaled up

The singleton-indicator argument in [the explicit separation](omega_template_tail_antichain_obstruction_2026-11-18.md) records, at a selected coordinate point r, the local orbit type

    m↦x_t(m r),    m∈M_1.

There are at most omega^c=2^c such types, regardless of the cardinality of (R_t)_1. For regular lambda>2^c, the union of bounded occurrence sets of all types is bounded. Hence a nonzero family of rows cannot avoid all recurring local types beyond this threshold.

More decisively, Section 1 already supplies a monic full-Isbell witness E(S) for every finitely generated map. Any proof of M-nonmembership for these larger tails must therefore use the requirement S∈C, or exclude all alternative C-witnesses. An obstruction that excludes every K-object Y as a possible monic E(Y)-witness is impossible here.

This does not prove a sufficiently large filtered-colimit closure theorem for M. It concerns these specific tail-restriction colimits and yields full-power witnesses, whose C-membership is not automatic.
