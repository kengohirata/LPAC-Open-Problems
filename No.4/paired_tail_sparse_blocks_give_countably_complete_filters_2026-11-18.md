# Sparse row blocks give proper countably complete character filters

2026-11-18. Status: **PROOF_RECONSTRUCTED**; another research agent independently checked the sparse-block scheduling mechanism and found no gap. Not externally reviewed or formally verified. This improves the [mixed-fibre reduction](paired_tail_selected_dynamics_and_second_sort_atoms_2026-11-18.md): countable intersection consistency can be obtained while preserving recurrence. It does not produce countably complete ultrafilters or global point evaluations.

## 1. Setting and result

Assume N and λ=c⁺. Let R=Y_λ and let W be its bounded-tail quotient. Suppose j:E(Y)↪W is a hypothetical monic C-witness of the paired seed, with |Y₀|≤λ. Choose an M₁-subset B⊂Y₁ of size at most λ containing p_Y(Y₀)∪q_Y(Y₀). Any preassigned set of at most λ additional second-sort points may be included.

Put T=H₁(Y₀), s_a=H₁(p_Y)^{-1}(a), and D(a)=H₁(q_Y)(s_a). The earlier reduction supplies recurrent atomic partial rows and finite-pattern realization. Here the row construction can be strengthened as follows.

There is an unbounded union I of pairwise disjoint bounded row intervals, and partial K-maps q_t:D_t⊂R→Y for t∈I, such that:

- Every point of Y₀ and every point of B occurs in the appropriate image for unboundedly many t∈I.
- The selected character sets are D-closed and satisfy the exact single-valued evaluation/dynamics equations of the earlier note, including the two marks 0,t.
- For every retained row t and every a∈T, the entire mixed family

      {ξ:g(ξ)=a(q_(t,0)(g))}          (g∈(D_t)₀),
      {ξ:r(ξ)=s_a(q_(t,1)(r))}        (r∈(D_t)₁)       (1)

  has the countable intersection property: every countable subfamily has nonempty intersection.

Consequently (1) is contained in a proper countably complete filter on [0,λ]. No claim that the original full j remains monic after arbitrary row restriction is needed; recurrence is explicitly preserved for all the chosen source points. In fact that recurrence also preserves first-sort injectivity when the restricted j₀ is considered, since all first-sort points are included.

## 2. Why a continuous all-row schedule was unnecessarily restrictive

For a continuous chain of small parameter sets, finite patterns at a limit already occur earlier. Countable patterns can first appear at limits of countable cofinality, so adding all their representatives may require a new row bound at that limit. A naive preceding-stage choice on every row need not remain cofinal; the familiar regressive-function obstruction explains this difficulty.

We instead allow gaps in the retained rows. After the equations for a parameter stage have stabilized, we deliberately choose positive rows for every current atom. This directly protects recurrence, rather than relying on an eventually cofinal parameter assignment at every ordinal row.

## 3. Parameter sets and countable patterns

Enumerate Y₀ and B by at most λ indices. For α<λ choose increasing M₁-subsets A_α⊂Y₀ and B_α⊂B, of size at most c, covering the enumerated points through α and satisfying

    p_Y(A_α)∪q_Y(A_α)⊂B_α.

Their unions are Y₀ and B. Such sets exist because |α|≤c, |M₁|=c, and c·c=c. They may be taken continuous, although continuity will not be needed for the row bounds.

At stage α, include in H_α⊂T a representative of every realized mixed profile on every countable subset of A_α⊔B_α:

    a(y) for y∈A_α,       s_a(z) for z∈B_α.

There are at most c countable subsets or sequences of these parameters, and at most c possible ω-valued profiles on any one of them, because c^ℵ₀=c. Thus at most c representatives suffice. Include the previously selected characters, the seed characters h,k, and all their finite D-iterates. Since α<λ has cardinality at most c, H_α still has size at most c.

This selection includes representatives for genuinely new countable patterns at limit stages; no assertion that those representatives occurred earlier is made.

## 4. Synchronization followed by deliberate recurrence

For the current A_α,B_α,H_α, synchronize exactly the equations from the mixed-fibre note:

- binary singleton representatives, pairwise disjointness, and all M₁-action implications;
- the two structural singleton implications from A_α into B_α;
- atom comparisons with a and s_a for a∈H_α;
- balanced row equations for the selected characters and their extensions;
- naturality for p,q and the paired seed identities.

There are at most c equations. Regularity of λ gives a row bound after which they all hold. Choose the beginning b_α of the new interval beyond this bound and beyond the ends of all earlier intervals. This is possible at every α<λ, including limits.

For each current source point u∈A_α⊔B_α, its singleton image under the original monomorphism has nonempty support on unboundedly many rows. Choose one such row t_(α,u)≥b_α. There are at most c choices, so their supremum is below λ. Choose e_α<λ strictly above that supremum and above b_α, and retain the whole interval

    I_α=[b_α,e_α).

On each row of I_α construct the atomic partial K-map using the current A_α,B_α, exactly as in the earlier note. All its equations hold throughout the interval. At subsequent stages choose the next beginning strictly beyond e_α. Put I=⋃_(α<λ)I_α.

Every fixed source point u is included at all sufficiently late parameter stages, and at each such stage the row t_(α,u) explicitly witnesses its occurrence. These rows tend unboundedly to λ. This proves recurrence despite the gaps. No common tail bound for all λ stages, and no continuous sequence of row bounds, was used.

## 5. Countable intersection property

Fix t∈I_α and a∈T. Any countable subfamily of (1) mentions countably many labels in A_α and B_α. Choose b∈H_α realizing the same mixed countable profile as a on these labels.

The synchronized balanced-row calculation supplies a single ξ_t(b)∈[0,λ] simultaneously evaluating both row sorts for b. The atom comparisons therefore show that ξ_t(b) belongs to every set in the chosen countable subfamily. This proves the countable intersection property.

Let F_(t,a) consist of all subsets U⊂[0,λ] containing an intersection of countably many sets from (1), with the empty intersection allowed. The countable intersection property makes this filter proper. A countable intersection of members has a witness obtained by taking the union of their countable lists of constraints; that union is countable. Thus F_(t,a) is countably complete.

## 6. What is still missing

A proper countably complete filter need not extend to a countably complete ultrafilter. Under N, any such ultrafilter on a set would be principal. In this setting, therefore, the desired ultrafilter extension exists exactly when all the mixed fibres have a common point.

The proper co-bounded filter on a regular uncountable ordinal already illustrates the distinction: it is countably complete and has empty total intersection. No countably complete ultrafilter can extend it under N.

The [companion partial-row examples](partial_ordinal_row_countable_fip_failure_2026-11-18.md), §§4–5, show that this distinction persists even with genuine C-targets, full first-sort rows, and compatible p/q maps. There the first row is the identity, while the second row corrects the endpoint to the eventual value below λ. Countably many constraints have a common point below λ, but the full first-sort family forces the endpoint and one second-sort constraint excludes it. The domain and the chosen structural image can both be kept of size λ. These examples are not asserted to be restrictions of an actual full-power monomorphism. That extra compatibility, especially recurrence of additional second-sort atoms outside the chosen structural subset, remains available for further work.

The present improvement removes countable intersection failure from a carefully chosen recurrent system arising from an actual j. It leaves an uncountable total-intersection/principal-realization problem, rather than an unproved countable-completeness assertion about the generated filter.

## 7. Cardinal generalization

The same argument works for any regular λ>c satisfying

    μ^ℵ₀<λ       for every infinite μ<λ,

with |Y₀|,|B|≤λ. At stage α use parameter sets of size <λ; their countable mixed profiles and the selected character family still have size <λ by the displayed condition. Regularity bounds the synchronization equations and the selected positive rows. The sparse-block recursion is otherwise unchanged.

The case λ=c⁺ satisfies this hypothesis in ZFC, since every μ<λ is at most c and c^ℵ₀=c. No generalized continuum hypothesis was used in that case. For a regular λ failing the displayed exponent bound, this proof does not assert a simultaneous countable-pattern realization set of size <λ at every stage.
