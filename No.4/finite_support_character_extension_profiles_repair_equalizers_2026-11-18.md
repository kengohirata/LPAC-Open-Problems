# Controlled finite-support character profiles repair equalizers

2026-11-18. Status: PROOF_RECONSTRUCTED. mono_collapse independently reconstructed the entire proof, including the profile-specific meet, common-character closure, and final application on the original second sort, and found no gap. This is internal review, not external peer review or formal verification. All statements are ZFC. This extends the [one-step small-character repair](small_character_sources_admit_one_step_c_quotient_repair_2026-11-18.md) to certain first character spaces with as many as 2^c points. It uses the stronger continuity on the non-finite-support sector, while explicitly controlling the remaining finite-support profiles.

Write X=H_1(Y_0) for Y∈C, and assume X is nonempty. Put c=2^aleph_0. Let Y_fs=(Y_0⇉(Y_1)_fs) denote the finite-support truncation; both arrows land there.

## 1. Sufficient source conditions

Suppose the compact Stone space X has weight at most c. Either of the following additional assumptions is sufficient:

1. |(Y_1)_fs|≤c.
2. The canonical extension/restriction map

       e:X→H_1((Y_1)_fs),       h↦h̃|_(Y_1)_fs

   is continuous, where h̃ is the unique extension of h to Y_1.

Then, for every pair a,b:E(Y)⇉Z with Z∈M, the equalizer belongs to M. Every finite seed has a monic E(Q)-cover with

    Q∈C,
    |Q_0|≤c,       |Q_1|≤2^(2^c),
    |E(Q)_i|≤2^(2^(2^c)).

The first-space weight hypothesis holds in particular if |Y_0|≤c. Assumption 2 holds in particular when Y_fs∈C_bfs: H_1(p_(Y_fs)) is then a continuous bijection between compact Hausdorff spaces, hence a homeomorphism, and its inverse is e.

Neither condition asserts arbitrary 2^c-continuity on a large finite-support sector. The proof below uses only the number of profiles visible there.

## 2. A profile-specific large-meet lemma

Let S be an M_1-set with at most countably many fixed points, and let a:Ω^S→Z_i commute with both monoid actions, with Z∈M. Let F be a family of at most 2^c functions on S. Suppose

    |{(f(s))_(f∈F):s∈S_fs}|≤c.                         (1)

For any profile p∈Ω^F and binary w with

    w≤a[f=p_f]       for every f∈F,

we then have

    w≤aχ_P,       P={s:f(s)=p_f for every f∈F}.         (2)

To prove this, select at most c observations F_0⊂F distinguishing p from every different profile realized on S_fs. Then

    S_fs∩⋂_(f∈F_0)[f=p_f]=S_fs∩P.

Split w into its parts below aχ_(S_fs) and aχ_(S\S_fs). On the first part apply global c-meet preservation to F_0. On the second part apply relative 2^c-meet preservation from [the non-finite-support-sector theorem](nonfinite_support_sector_preserves_two_to_c_joins_2026-11-18.md). Both pieces lie below aχ_P, which proves (2).

The two pieces may differ when this argument is applied to two different maps. No equality of their images of χ_(S_fs) is required. Each application proves domination by the same full source profile fiber separately.

## 3. The first quotient from common characters

Choose a finite equalized seed, and let O_0,O_1 be the original finite families' full orbit observations, with both structural pullbacks included in O_0 as in the one-step repair. Put

    L={h∈X:a_0(h)=b_0(h)}.

A compact Stone space of weight at most c has at most c continuous Ω-valued functions and at most 2^c points. Thus |L|≤2^c, while the set of all evaluation profiles y↦(h↦h(y)) of Y_0 on X has size at most c.

Choose L'⊂L of cardinality at most c dense in the closure of L in X. For any y,y'∈Y_0, the set

    {h∈X:h(y)=h(y')}

is closed. Hence equality of their evaluations on L' is equivalent to equality on all of L.

Define Q_0 by O_0 together with all L-character observations. The same quotient is defined by O_0 and L', at most c common observations. Its carrier has size at most c: the initial finite-orbit type quotient has that bound by finite support, and the full X-evaluation profile has at most c possibilities.

The small-quotient c-meet/c-join completion argument therefore places the full Ω^(Q_0) in the first-sort equalizer. Exactly as in the one-step proof, pullback identifies

    H_1(Q_0)=L.                                        (3)

In particular L is now known to be closed and compact, not merely an arbitrary subset. Its weight is at most c. Unique second extension gives agreement on every h̃ with h∈L and makes L invariant under h↦h̃q_Y.

## 4. The C-condition is repaired as before

Define Q_1 by the observations

    F=O_1∪{h̃:h∈L}.

Their number is at most 2^c. Both structural pullbacks factor through Q_0, by the original choice of O_0 and by the invariance of L. Thus q:Y↠Q is a K-quotient.

Every character of Q_0 is represented by an h∈L, whose extension is explicitly included in F. This proves surjectivity of H_1(p_Q). Injectivity follows by pulling back to Y. Consequently Q∈C and |Q_1|≤Ω^(2^c)=2^(2^c).

If L is empty, this is the initial finite-orbit quotient and the existing general type-completion theorem already finishes the proof. Assume from now on that L is nonempty.

## 5. The finite-support profiles are bounded

Under assumption 1, the F-profile image of (Y_1)_fs has size at most c immediately.

Under assumption 2, each y∈(Y_1)_fs determines a continuous Ω-valued function on L,

    h↦h̃(y),

because it is the composite of the continuous e|_L and coordinate evaluation on H_1((Y_1)_fs). There are at most c such continuous functions on the compact space L of weight at most c.

The additional O_1-profiles on (Y_1)_fs also have at most c possibilities: O_1 is generated by finitely many observations, and a countable dense submonoid determines their types on finite-support points. Combining the two profile records still gives at most c possibilities. Thus (1) holds in either case for S=Y_1 and this particular F.

## 6. Complete the second power inside the equalizer

Choose a packed countable separator z_0 on Q_0; this is possible because |Q_0|≤c and H_1(Q_0)=L is nonempty, so Q_0 has no fixed point. Its first-sort image is common.

For any proposed second-sort difference a_1(fq_1)≠b_1(fq_1), take a monic D-cover containing that pair, the common z_0q_0 image, and the common original finite second-seed images. The first-sort strong factorization puts all Ω^(Q_0) images in this cover. C's unique extension then puts every common h̃-image for h∈L in the same second-sort cover. The original seed orbit images are there by ambient closure. Thus all F observations are covered simultaneously.

At a cover point where the two lifts differ, its nonzero singleton image w determines a common F-profile p. Apply the profile-meet lemma of Section 2 to a_1 and b_1 on the **original source Y_1**. It gives

    w≤a_1χ_P,       w≤b_1χ_P,

where P is the same full F-profile fiber. It is empty or a single q_1-fiber. It cannot be empty, and fq_1 has a constant value on it. The two images therefore agree on w, a contradiction.

This proves all of E(Q) lies in the equalizer. It is a monic D-cover of the chosen seed, completing the theorem.

Applying the continuity lemma to the original Y_1 is deliberate. A quotient Q_1 can acquire new finite-support points; the argument does not assume its finite-support carrier has the bound from Section 5.

## 7. Continuity of character dynamics alone is weaker

Assumption 2 implies continuity of the character dynamics h↦h̃q_Y, because q_Y lands in (Y_1)_fs. The converse is false.

For example, take I=[0,ω] and

    Y=(C(I,Ω) --inclusion,inclusion--> Ω^I).

The dynamics is the identity. The finite-support part of Ω^I consists of finite-range functions, whose character space is the Stone space of ultrafilters on the discrete set I. The canonical e sends each point of the compact ordinal I to its principal ultrafilter. This map is not continuous: the clopen determined by {ω} has inverse image {ω}, which is not open in I.

This example is itself safe by the small-character theorem. Its purpose here is only to distinguish continuity of the dynamics from continuity of the entire finite-support character-extension map. The latter is the condition used in the profile bound above.

No general C-coreflector or unrestricted M-equalizer theorem is inferred.
