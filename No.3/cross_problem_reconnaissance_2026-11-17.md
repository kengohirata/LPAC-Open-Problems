# No.3 preliminary reconnaissance: reusable ideas from No.1 and No.2 (2026-11-17)

**Scope:** Reconnaissance only. No new theorem or proof of No.3 is claimed. Do not treat this note as mathematical verification of No.1/2.

## Checked source status
- `../No.1/codex_sset_handoff/RESEARCH_STATUS.md` and `CLAIMS_LEDGER.md` updated 2026-11-17, especially
  `investigations/measurable_thresholds_and_strong_compactness_2026-11-17.md`. No.1 reports
  **proper class strongly compact cardinals => P1 => proper class measurable cardinals**,
  both recent directions marked PROOF_RECONSTRUCTED; no independent referee audit.
- `../No.2/no2_presheaf_presentation_Kfs_2026-11-17.md`,
  `../No.2/no2_direct_presheaf_kernel_proof_2026-11-17.md`:
  under absence of uncountable measurables, a direct presheaf counterexample for Problem 2(b).
  Also PROOF_RECONSTRUCTED.
- `positive_quotient_bounds_and_regular_towers_2026-11-17.md`:
  No.3's current reduction. For a cocomplete K with a set G of lambda-generated strong generators,
  let H be <lambda coproducts of G. P3 reduces to a uniform set bound on strong epi quotients
  e:H->B for every H in this set, equivalently a uniform termination bound for canonical
  regular-quotient towers. Distinguish strong from regular epi.

## Ranked techniques and actual transfer limitations

### Priority A — Compactness/purity and boundedness from No.1, applied to No.3's Q
No.1 (2026-11-17 §§6–8) uses one strongly compact cardinal above a **fixed set of test data**
to make test targets and kernel pairs kappa-pure-injective, prove closure under kappa-pure
subobjects, then show small local pieces generate an accessible class.
For No.3 the analogous desideratum is a cardinal bound on the codomain B of every
strong epi from a fixed H. This is formally the right *scale* for strong compactness:
the initial data H and its presheaf representation are small.
However, no fixed small set of tests describing all strong quotients of H is
currently available. 'B is an arbitrary strong quotient of H' is not obviously
the orthogonality condition treated in No.1. Cannot infer strong compact
class => P3 without a new definability/compactness bridge.
Specific reconnaissance target: check whether the category/class of
strong quotients of H has a bounded-signature axiomatization or a
small witness property stable under appropriate elementary/pure subobjects.

### Priority B — No.2's presheaf engineering, for possible NEGATIVE candidates
No.2 constructs the presheaf category K_fs (finite-support zeroth component),
with explicit small projective generators P_n and Q, and proves the N-conditional
non-coreflectivity and two-coreflective intersection obstruction.
Technique: move a support restriction into the ambient locally presentable
category; use pushouts and kernels of double-dual evaluation maps to constrain
all possible factorization targets.
For No.3 a possible candidate is a cocomplete colimit-closed full subcategory
such as A={}^perp sigma from No.1/2, but it is **not** enough to show it
is cocomplete or non-coreflective. One must prove it possesses a SET of
GENERATED STRONG GENERATORS, and show failure of local presentability (or
unbounded strong quotients). Nothing read establishes those requirements.
Likewise, taking opposites of non-wellpowered coreflective classes does
not automatically give a counterexample: check cocompleteness, strong vs
ordinary epis, and generated strong generators.

### Priority C — Nonterminating towers / WVP from No.1 vs regular-quotient tower of No.3
No.1 (tower_bound_and_weak_vopenka) derives an Ord^op full embedding from
nontermination *because* the tower maps are internal monomorphisms in a
special quotient-closed category.
No.3 already has a canonical transfinite regular-epi quotient tower, and
its uniform stopping bound is equivalent to Q. This suggests a possible
ordinal-embedding or reflection argument.
But the orientation and mono/epi conditions differ. No.3's original
H-kernel pairs stabilize at the first stage even if the tower continues.
Neither No.1's 'Ord^op' embedding nor WVP=>stopping automatically transports.
Specific target: identify a category of quotients/structured slices in which
the No.3 tower enjoys the needed internal monicity/rigidity.

### Priority D — No.2's pushout / kernel-pair classification
No.2's final proof forces a comparison map into a right lifting class
via pushout and class closure; Isbell duality then constrains kernel pairs
to coordinate-identification kernels. This is useful as a **proof pattern**
for proving a restricted class of strong epis is regular or has controlled
quotient size, not as a general result about No.3 strong quotients.
The test map sigma in No.2 is regular epi, but a regular-epi
*coorthogonality test* being pathological is not the same as having
unbounded strong-epi *quotients* of a fixed generated object.

### Priority E — No.1 measurable / ultrafilter counterexample
Varying Omega with rho and using a rho^+-complete ultrafilter threshold
is a precise template for distinguishing a fixed set of parameters
from the growing ordinal witnesses [0,theta]. The use of compact
dual H(Z_0) and successor-closed image yields lower bounds for
factorization targets of Y_theta->B.
For No.3, the quantifier pattern differs: fixed SMALL source H,
arbitrarily large strong quotient B. Existing No.1 witnesses grow
in their sources Y_theta and cannot simply be reused or dualized.
A construction must enforce largeness of the quotient of a fixed H.

## Adjacent literature lead, not an identified solution
The distinct problem 'every accessible category is co-wellpowered' reportedly
has the same broad large-cardinal sandwich (proper class strongly compacts
sufficient; proper class measurables necessary): Makkai–Paré 1989,
Thm. 6.3.8, and Adámek–Rosický Example A.19; cited in
https://mathoverflow.net/questions/455750/ .
Important: No.3 does not assume accessibility, **it seeks to prove it**,
so one cannot invoke an accessible-category co-wellpoweredness theorem
on K without circularity. This is a literature route to audit,
not a new implication for No.3.

## Conservative decision for next research turn
1. Positive priority: can strongly compactness (with large enough kappa)
   furnish Q by recognizing and shrinking the class of strong quotients
   of fixed H? First inspect possible infinitary positive-existential
   characterization of a strong epi and how a reflection affects substructures.
2. Cross-problem negative priority: inspect A={}^perp sigma of No.2 as
   a cocomplete category and test whether it has any small strong generator
   of generated objects. Do not assume such a generator exists.
3. Tower priority: test whether the No.3 quotient tower embeds a forbidden
   ordinal pattern analogous to No.1, with explicit checks of internal
   mono/epimorphism directions.

No new mathematical claim, theorem, cardinal implication, or independence
result about No.3 has been established in this reconnaissance.

## Relation to the original book's Open Problem 11
Problem 11 asks about (strong-epi) co-wellpoweredness of **accessible** categories.
The cardinal-strength sandwich reported for that statement is particularly close
in form to No.1's new result, and the core technical issue is the same
strong-quotient size bound as No.3. But it cannot directly solve No.3, because
No.3 must first establish accessibility; do not assume it.
