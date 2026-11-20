# Ordinal sources through the continuum are M-rigid

2026-11-18. Status: PROOF_RECONSTRUCTED. Another research agent independently reconstructed the c-continuity limit argument and the required second-sort covering argument. The complete proof below was assembled by the coordinating agent. No external review or formal verification. Everything is ZFC.

Let c=2^aleph_0 and let κ be an ordinal with |κ|≤c. Write

    Xκ=[0,κ],
    Yκ=(Cont(Xκ,ω) --inclusion,dκ*--> ω^Xκ),
    j0:E(B)→E(Yκ)

for the usual initial-evaluation seed. Then Yκ∈C in ZFC: the only potentially nontrivial input is that every countably complete ultrafilter on a set of size at most c is principal, which follows by a countable binary separating family. The character spaces of both sorts are Xκ by evaluation.

**Theorem.** For every Z∈M, two maps a,b:E(Yκ)⇉Z agreeing after j0 are equal. More generally every E(Yκ)→Z factors through a monic D-object, and all pairs with this source have their equalizer in D.

The latter two assertions are instances of [the small-character separated-source theorem](small_character_separated_sources_have_d_equalizers_2026-11-18.md): the first carrier has size at most c, the character space has size at most c, and the characters separate the full second carrier. Notice that the second carrier can have size 2^c; the old bound on both carriers does not suffice.

## 1. Agreement propagates through every ordinal of cardinality at most c

Let u_β and v_β denote evaluation at β on the first and second carriers. Agreement after j0 gives a_0(u_0)=b_0(u_0).

If agreement holds at u_β, the two images of its unique balanced extension v_β have the same first structural image. E(σ)-orthogonality of Z gives equality at v_β. Pullback along q then gives equality at u_(β+1), whenever β<κ.

Now let β≤κ be a nonzero limit. Choose an increasing cofinal sequence (β_i)_(i<μ), where μ=cf(β)≤c. For every n∈ω, continuity of g∈Cont(Xκ,ω) gives the pointwise identity

    [u_β=n] = union_(i<μ) intersection_(i≤j<μ) [u_(β_j)=n].

Every displayed union and intersection has at most c inputs. The first source sort has no fixed point, so [continuum Boolean continuity](continuum_boolean_continuity_and_orbit_separator_factorization_2026-11-18.md) applies to both a_0 and b_0. Agreement at all earlier evaluations therefore gives agreement on the binary fiber indicator [u_β=n]. As the unary fiber indicators jointly separate elements of Z_0, agreement holds at u_β itself.

Transfinite induction proves agreement at every u_β and, by unique extension, at every v_β, β≤κ. No operation indexed by c^+ is used.

## 2. Why agreement on all evaluations suffices here

The evaluations separate the first carrier, which has size at most c. Each of its singleton indicators is an intersection of at most c evaluation fibers, and every subset is a union of at most c singletons. Continuum meet and join preservation therefore gives a_0=b_0 on its whole full power, without requiring all the evaluations to fit into a finite generating list.

For completeness, the second sort needs a further local-cover step: equality on its characters alone is not automatically equality on all functions.

Choose one packed countable separator z_0 for Yκ,0. Suppose a_1(F)≠b_1(F) for some F:Yκ,1→ω. Take a monic D-cover of the common image a_0(z_0)=b_0(z_0) and of these two F-images. The one-sort factorization theorem puts the entire common first-sort map into this cover. C's unique-extension property then puts all the common second evaluations v_β into the same cover, without adding them to its finite seed.

Take a local atom w where the two F-lifts differ. Its values on the covered v_β give a profile p∈ω^Xκ. This is an actual point of the second carrier, which is the full power ω^Xκ. There are at most c evaluations, so continuum meet preservation places w below the images, under both maps, of the singleton {p}. Both F-images must have the same value F(p) there, a contradiction.

Hence a_1=b_1 as well, proving rigidity. The re-covering with the proposed difference is essential: merely comparing old singleton images would leave an unsupported assumption about their supremum in Z.

## 3. An alternative proof from the D-equalizer

The separated-source factorization theorem constructs the equalizer as E(Q)→E(Yκ), where Yκ↠Q is an actual componentwise-surjective K-map and Q∈C. It does not merely assert an abstract D-isomorphism.

If this equalizer contains j0, its character image H(Q_0) is a closed subset of Xκ containing 0 and closed under successor, by naturality and Q's unique extension. Transfinite induction using closedness shows it is all of Xκ. These evaluations separate Yκ,0, so the quotient on the first carrier is injective. Unique extension in C makes every second evaluation descend too, and these separate Yκ,1, so the second quotient is injective. Thus Yκ↠Q is an isomorphism.

This also proves rigidity in ZFC. It does not invoke general full faithfulness of E under N, because the quotient map was explicitly constructed by the factorization theorem.

## 4. Remaining boundary

The first uncovered regular ordinal for the limit propagation is c^+. At that endpoint the displayed eventual-value formula has c^+ terms, and continuum continuity cannot evaluate it. This is a genuine limitation: an actual M_bfs tail target fails preservation of a c^+-indexed join on a finite-support source, as proved in the [sharpness example](nonfinite_support_sector_preserves_two_to_c_joins_2026-11-18.md), §5.

The theorem excludes the continuum-sized ordinal sources as M-equalizer obstructions. It neither proves M-equalizer closure for larger ordinals nor constructs a Problem 4 counterexample.
