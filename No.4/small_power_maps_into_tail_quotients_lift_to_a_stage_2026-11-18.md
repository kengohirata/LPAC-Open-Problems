# Powers indexed by at most c points lift through ordinal tail quotients

2026-11-18. Status: **PROOF_RECONSTRUCTED**; the coordinating research agent independently reconstructed the argument and found no gap. Not externally reviewed or formally verified. The theorem is ZFC and supplies a new restriction on the remaining paired-ordinal witnesses.

Let λ>c be regular. For a set R put

    W_R=colim_(β<λ) ω^([β,λ)×R),

with restriction along tails, the left postcomposition action of M₂=End(ω), and equality of functions modulo a bounded set of rows.

## 1. Scalar lifting theorem

**Theorem.** If |S|≤c, every equivariant map θ:ω^S→W_R is induced, on one tail, by a set map

    τ:[β,λ)×R→S.

In other words θ(F) is the germ of F∘τ for every F:S→ω. The tail β is common, although the equality of a chosen representative of θ(F) with F∘τ may begin later, depending on F.

Assume first S and R are nonempty. Choose a countable point-separating family f_n:S→ω. For every p∈ω^ω define

    C_p(s)=0                          if all f_n(s)=p_n,
           1+min{n:f_n(s)≠p_n}        otherwise.

There are only c such profiles and counters. The zero fibre of C_p is either empty or a singleton. For N≥2, the truncation e_NC_p is a finite pointwise function of f₀,...,f_(N−2).

The target W_R has unique finite tuple coding, so θ preserves all finitary pointwise operations. Choose row representatives for the f_n-images, all the C_p-images, all singleton indicators, and the constants. Synchronize the truncation identities and the unary identities identifying [C_p=0] with the corresponding singleton or zero. There are at most c functions and equations, so regularity gives one tail on which every one of them holds pointwise.

At a point (t,r) of that tail, let p_n be the value of the chosen f_n-image. Every truncation of the C_p-image is then zero at (t,r), so its value is zero. The zero-fibre identity rules out an unrealized p, and shows that the image of the unique realized singleton is 1 there. Define τ(t,r) to be that uniquely realized point of S.

Now fix an arbitrary F:S→ω. The source identities

    χ_s≤[F=F(s)]       (s∈S)

give the corresponding identities of germs under θ. There are at most c such identities, so they hold simultaneously on a tail depending on F. At every point there, the singleton of τ(t,r) has image 1, forcing θ(F)(t,r)=F(τ(t,r)). This proves the theorem.

The argument does not synchronize all ω^S, which may have size 2^c. It synchronizes c profiles once, and then uses c singleton comparisons separately for each F.

If R is empty the target is a singleton and the unique map on the empty row domain gives the result. If S is empty and R is nonempty, no θ exists: its source is an M₂-fixed singleton, whereas W_R has no common fixed point. These cases complete the statement.

## 2. Lifting the entire P-map

Let R,Y∈K and put

    W^R=colim_(β<λ) E([β,λ)·R).

If both |Y_i|≤c, every P-map θ:E(Y)→W^R factors through a single stage by an actual dual K-map:

    θ=tail-quotient map ∘ E(q),
    q:[β,λ)·R→Y.

Apply §1 in each sort to obtain total set row maps q_(t,i) on a common tail. To prove their eventual naturality, fix m∈M₁. For every F:Y_i→ω, naturality of θ gives eventual equality of

    F(q_(t,i)(mr))  and  F(m q_(t,i)(r))

uniformly in r. If the two source points differed on unboundedly many rows, choose one unequal pair on each such row. There are at most c possible unequal pairs, so regularity gives one pair occurring on an unbounded set of rows. A single binary function F separating that pair contradicts the preceding germ equality. Thus equivariance holds pointwise after one tail for this m. Synchronize the c choices of m and the two sorts.

For each of the two structure arrows, apply the same unequal-pair argument to its naturality equation. There are only two more bounds. The row maps now form K-maps on one common tail, proving the asserted factorization. This proof does not use full faithfulness of E or N.

## 3. Consequences for paired ordinal tails

The [paired-stage obstruction](paired_ordinal_tail_stage_monic_obstruction_2026-11-18.md) excludes stage-induced monic C-witnesses for the two marks 0,t. Combining it with §2 shows that any hypothetical monic witness must have at least one carrier strictly larger than c.

More strongly, no both-finite-support C-witness can contain that paired seed. If such a witness existed, [bounded epi-compression](both_finite_support_accessibility_and_epi_compression_2026-11-18.md) would replace it by a monic subwitness with both carriers at most c and the same seed. Section 2 would lift that subwitness to a stage, contrary to the paired-stage theorem.

These conclusions apply both to the original ordinal template and to a trimmed template whenever its first-sort compact spectrum and second-sort evaluation classification are the same ordinal and its structure map induces successor. They rule out small or both-finite-support witnesses; they do not exclude the remaining large non-finite-support witnesses.
