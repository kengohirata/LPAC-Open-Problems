# Ordinal witness maps into targets with monic p

2026-11-18. Status: reconstructed and checked by a second research agent;
not externally reviewed or formally verified.

## 1. Factorization theorem

For κ≥ω use the ordinal K-object

    Y_κ=(C_κ --p=inclusion,q=d_κ^*--> B_κ),
    C_κ=Cont([0,κ],Ω),    B_κ=Ω^[0,κ].

Put

    C_0=C_κ,
    C_(n+1)={f∈C_κ : d_κ^*f∈C_n},
    C_∞=intersection_(n<ω) C_n,
    Y_∞=(C_∞ --id,d_κ^*--> C_∞).

As proved in [the p-isomorphism template note](ordinal_witness_maps_to_piso_templates_2026-11-18.md),
C_∞ consists of functions which are eventually constant on the initial
ω and constant on [ω,κ], with matching values at ω. It is countable.
It is an M_1-subact stable under d_κ^*, so Y_∞∈C and there is a
K-inclusion Y_∞↪Y_κ. Its dual is the componentwise surjective restriction

    r:E(Y_κ)↠E(Y_∞).

**Theorem (ZFC).** If Z∈H_fg and its structural arrow
`p_Z:Z_1→Z_0` is monic, then every P-map θ:E(Y_κ)→Z factors uniquely
through r.

No size condition on Z or presentation of Z by templates is required.
The statement does not require N; Y_κ is simply a K-object here.

## 2. Proof by countably complete kernel ideals

The [kernel-filter theorem](mono_factorization_kernel_filters_2026-11-18.md)
applies to θ. In each sort, the sets whose indicator is sent to zero
form a countably complete ideal; equality of images of two functions
is controlled by the ideal of their disagreement set. Finite pointwise
operations and constants are preserved.

We prove inductively

    θ_0(χ_(C_κ\C_n))=0,
    θ_1(χ_(B_κ\C_n))=0.                         (1)

The first equation for n=0 is tautological. Given the first equation
for n, p-naturality gives

    p_Z θ_1(χ_(B_κ\C_n))
       = θ_0(χ_(C_κ\C_n))=0=p_Z(0).

Since p_Z is monic, the second equation follows. Applying q-naturality
to it gives

    θ_0(χ_(C_κ\C_(n+1)))
       = θ_0(E(q_κ)(χ_(B_κ\C_n)))
       = q_Z θ_1(χ_(B_κ\C_n))=0.

Thus (1) holds for all n. Countable completeness of the two kernel
ideals now gives

    θ_0(χ_(C_κ\C_∞))=0,
    θ_1(χ_(B_κ\C_∞))=0.

Consequently each θ_i depends only on the restriction of a function
to C_∞. The resulting set maps on Ω^(C_∞) respect all actions and
structure arrows, since θ and r do and r is componentwise onto.
They therefore form the unique P-map θ_∞ with θ=θ_∞r. □

## 3. Equalizers with this ordinal source

Since both sorts of Y_∞ are countable, E(Y_∞) is ambient finitely
generated: choose an injective Ω-valued function on each sort; the
left M_2-orbits already contain all functions in those sorts.

If Z∈M and p_Z is monic, two maps a,b:E(Y_κ)⇉Z therefore factor
through r and then, jointly, through one monic D-subobject of Z.
Indeed the two induced maps E(Y_∞)⇉Z together have a finitely
generated coproduct as domain.

Under N, E(Y_κ) and that common D-subobject are D-objects. D's limit
closure then proves

    Eq(a,b)∈D.

In particular, if a j_0=b j_0, the
[minimal-D-hull theorem](ordinal_evaluation_has_no_proper_d_hull_2026-11-18.md)
forces a=b. Thus **no target in M with monic p can witness failure of
M-equalizer closure using the ordinal source E(Y_κ)**.

This does not prove general M-equalizer closure for p-monic targets:
the factorization theorem is specific to these ordinal source objects.
Targets with nonmonic p, including the larger ordinal-template tail
quotients, remain available for investigation.
