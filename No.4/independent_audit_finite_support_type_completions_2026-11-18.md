# Independent audit of finite-support type completions

2026-11-18. Status: **complete proof independently reconstructed; no gap found**. This is a research-agent audit, not external human review or formal verification.

Sources read in full:

- [Finite-support type quotients are completed inside M-equalizers](finite_support_type_quotients_are_m_epic_completions_2026-11-18.md).
- Its [σ-Boolean reduction](truncation_closed_subobjects_and_sigma_boolean_reduction_2026-11-18.md).

The central theorem and the full-power monic witness in its application are correct in ZFC. The unresolved C condition can be sharpened: **only surjectivity of H(p_Q) can fail for the quotient produced there; injectivity is automatic.**

## 1. Countable observation coordinates

Eventually constant selfmaps of ω, together with the identity, form a countable dense submonoid of End(ω). Their compositions remain eventually constant. At a finite-support point, the action depends on finitely many input coordinates, so checking a profile on this dense monoid checks it on every transformation. The orbit-observation relation is an M-congruence, and the resulting quotient Q is finite-support and has at most c points.

A sequence of dense-monoid approximations to any transformation eventually agrees with it on each point's finite support. Therefore all the translated observation functions are measurable for the countably generated σ-algebra B, as are the action maps of Q. The equalizer of the two component maps contains the B-measurable functions: its finite-operation and truncation closure give precisely the σ-Boolean calculation in the cited dependency.

The σ-Boolean calculation itself checks. A first-hit counter for a sequence of measurable subsets has finitely determined truncations, which supplies countable unions; reconstructing a function from its countably many fibres uses the same truncations. Constants are present in the actual equality set, so the stated constant assumption is met.

## 2. Packing in the presence of fixed points

For injections b_n with disjoint ranges and left inverses a_n, b_nQ is exactly Fix(b_na_n). Both these images and Q^M are B-measurable by the countable separating coordinates; fixedness under the dense monoid is equivalent to fixedness under all M because Q is finite-support.

The intersection identity b_nQ∩b_rQ=Q^M for n≠r is correct. A transformation acting as a left inverse on one range and as an arbitrary constant on the other gives x=c_l y for all l. Applying any transformation then fixes x, and hence also the common image. Conversely every fixed point belongs to every image.

The piecewise functions z_j are measurable on a countable measurable partition. On the fixed-point part all coordinates agree with h_j, so the pieces fit and z_j(b_nq)=φ_(j,n)(q) holds there as well as on the other pieces. Thus the countable separator family is packed into finitely many functions whose images already agree. This avoids any assumption that the action is fixed-point-free.

## 3. The monic local atom and counter

The symmetric difference of two unequal binary images is nonzero in the inherited finite-operation algebra. A monic D-cover containing this difference and the common z_j-images gives a point where the difference is 1. Its singleton indicator supplies a nonzero w and the common coordinate profile p.

The first-difference counter H_p is B-measurable: its positive fibres depend on finitely many coordinates and its zero fibre on a countable intersection. It therefore has a common image under the two maps. For N≥2, its truncation uses only the first N−1 coordinates. The conditional truncation argument gives w≤[c_p=0] using finite identities and left joint separation, without assuming countable meets in the target.

The zero fibre is empty or a singleton. In the former case w vanishes; in the latter, the corresponding common binary fibre makes both images of χ_U constant with the same value on w. Either case contradicts the chosen symmetric difference. Agreement on all subsets follows. Fibre indicators and joint separation then give agreement on every Ω-valued function on Q.

All operations needed are either unary actions or finite operations uniquely encoded by tuple projections. The maps under consideration need only commute with the two monoid actions in the chosen sort, as the theorem states; they need not extend to maps of the whole diagram.

## 4. The quotient diagram and its exact remaining condition

In the application, adding the structural images of the sort-1 seeds to the sort-0 family ensures that the observation equivalences respect both p_Y and q_Y. If either family is empty, one may add the constant-zero function; this meets the theorem's nonempty-family convention and leaves the corresponding equivalence relation unchanged.

The result is a componentwise surjection q:Y→Q. Each Q_i is finite-support and has size at most c. Agreement on every function factoring through q in each sort gives an actual P-monomorphism E(Q)→Eq(a,b) containing the seed. No C-membership follows merely from this full-power description.

There is, however, an automatic uniqueness lemma for every such quotient, with no finite-support or cardinal restriction beyond Y∈C. If s,t:Q₁→Ω are equivariant and s p_Q=t p_Q, then

    (s q₁)p_Y=s p_Q q₀=t p_Q q₀=(t q₁)p_Y.

Injectivity of H(p_Y) gives s q₁=t q₁. Since q₁ is onto, s=t. Therefore H(p_Q) is injective. The missing C property is exactly its surjectivity.

For a both-finite-support quotient Q, both Hom spaces are compact Hausdorff. Hence H(p_Q) identifies H(Q₁) homeomorphically with a closed subspace of H(Q₀). Completion must supply the missing characters in this compact space; no repair of uniqueness is needed.

## 5. Limits of the audit

The example (Ω --id,id--> Ω)→(Ω⇉1) correctly exhibits failure of surjectivity after quotienting a C-object. Orthogonality of the whole equalizer supplies the missing balanced extensions there, but does not place them in the particular full-power subobject E(Q).

The proof does not establish that adding all these extensions retains a finite or countably packed observation family. It also does not prove termination of a refinement process or C-membership of its limit. These are actual remaining steps, not gaps in the completed type-quotient theorem.

**Audit conclusion:** the finite-support completion theorem and its monic full-power application pass. The open refinement problem can be stated more precisely as surjectivity of H(p_Q), since injectivity is inherited from Y.
