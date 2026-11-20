# Independent audit of the No.1 dependency NC

2026-11-18. Status: **the proof of NC was independently reconstructed and no gap was found**. This is an independent check by a second research agent, not external human review, formal verification, or a novelty audit. The original No.1 manuscript has not been edited.

## 1. Exact scope and notation

The complete source read was [parallel_actions_counterexample_2026-11-16.md](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md). The dependency checked for No.4 is its Corollary 9, including every lemma needed for that corollary.

Write \(\Omega=\omega\), \(M=\operatorname{End}(\Omega)\), and \(\mathcal K=(M\text{-Set})^{(0\rightrightarrows1)}\). The No.1 manuscript calls this ambient category \(\mathcal D\) and its coorthogonality class \(\mathcal A\). To avoid confusion with the dual image used in No.4, this audit writes the latter class as \(\mathcal C\):

\[
Y\in\mathcal C\quad\Longleftrightarrow\quad
Y_0\text{ has finite support and }H(p_Y):H(Y_1)\longrightarrow H(Y_0)\text{ is bijective},
\qquad H(A)=\operatorname{Hom}_M(A,\Omega).
\]

Let \(B=(\Omega\rightrightarrows1)\), and let N mean that there is no uncountable measurable cardinal. The checked conclusion is

\[
\boxed{\mathrm{ZFC}+\mathrm N\ \vdash\ \mathcal C\downarrow B\text{ has no weakly terminal set}.}
\tag{NC}
\]

The two maps defining \(\mathcal C\), the ambient category, and \(B\) are fixed independently of the cardinal used in a witness.

## 2. Isbell evaluation calculation

The direct argument in §1.1 is sufficient; no unverified appeal to an external formulation of Isbell's theorem is needed for this dependency.

For an equivariant \(\phi:\Omega^X\to\Omega\), every \(\phi(f)\) belongs to \(\operatorname{im}f\): the selfmaps fixing that image pointwise have precisely that image as their common fixed points. Thus the characteristic functions define a proper ultrafilter

\[
\mathscr U_\phi=\{A\subseteq X:\phi(\chi_A)=1\}.
\]

Complementation follows from the unary exchange of 0 and 1. Coding two characteristic functions into one finite-valued function gives preservation of their conjunction. These facts also give upward closure. For every \(f:X\to\omega\), the fibre at \(\phi(f)\) belongs to \(\mathscr U_\phi\). Consequently every countable partition has a selected cell. Partitioning into an intersection and the first failures proves countable completeness.

The reduction from a nonprincipal countably complete ultrafilter to a measurable cardinal was checked. Let \(\kappa\) be the least size of a partition into ultrafilter-small sets. Singleton cells ensure that this cardinal exists, and countable completeness gives \(\kappa>\omega\). Failure of \(\kappa\)-completeness would give a smaller partition by the first-failure construction. Pushforward along a minimal partition therefore gives a nonprincipal \(\kappa\)-complete ultrafilter on \(\kappa\). This is the measurable cardinal excluded by N. No regularity of \(\kappa\) was assumed in this argument.

Under N, \(\mathscr U_\phi\) is principal, and the selected-fibre property gives \(\phi=\operatorname{ev}_x\) for its unique principal point. When \(X=\varnothing\), the source \(\Omega^X=1\) is fixed and \(\Omega\) has no common fixed point, so both sides of the evaluation correspondence are empty.

The topological distinction in the source is essential and correctly maintained: \(H(\Omega^X)\cong X\) is a set bijection, and its inherited topology is discrete. It is not identified topologically with the compact ordinal space later put on the same underlying set.

## 3. The fixed finite-support test

The finite-support/stabilizer equivalence in Lemma 1 is valid for the full transformation monoid. Given maps agreeing on finite \(S\), choose an extension \(w\) of their common restriction with all fibres infinite, then write them as \(wu,wv\), with \(u,v\) fixing \(S\). This proves the converse direction, including the empty-support case.

For \(K=2^M\), the cofree action \((n\chi)(m)=\chi(mn)\) has the correct orientation. Its finite-support elements are exactly the functions depending on the restriction of \(m\) to some finite subset of \(\Omega\). They form the indicated subobject \(j:U\hookrightarrow K\).

For the converse detection argument, each point \(a\in A\) gives the equivariant map

\[
\Phi_a(x)(m)=[mx=a].
\]

If \(A\perp j\), then \(\Phi_a(a)\) has finite support. A transformation fixing that support fixes \(\Phi_a(a)\); evaluating at the identity forces it to fix \(a\). Lemma 1 then supplies finite support for \(a\). The colour map changes with \(a\), but the single test \(j\) does not.

The right adjoint \(R_0(W)=(W\rightrightarrows1)\) and the two Hom calculations in §3 are correct. In particular, the second test induces exactly \(H(p_Y)\), with no extra condition on \(q_Y\). All sets and test maps are set-sized and independent of ordinal witnesses.

## 4. Compactness and witness membership

For finite-support \(A\), each \(h\in H(A)\) sends \(a\) into any chosen finite support \(S_a\). Thus \(H(A)\) is the closed equivariance locus in the compact Hausdorff product \(\prod_a S_a\). Empty supports give an empty Hom space; an empty carrier gives the singleton empty product. Both cases are consistent with the proof.

For compact zero-dimensional Hausdorff \(X\), every continuous \(\Omega\)-valued function has finite image. An equivariant functional on \(C(X)=\operatorname{Cont}(X,\Omega)\) chooses a value in each image. Finite tuple coding gives the finite intersection property for the corresponding closed fibres. Compactness gives a common point and clopen separation gives its uniqueness. Evaluation is continuous, so the resulting bijection

\[
X\cong H(C(X))
\]

is a homeomorphism. The empty-space case is explicitly valid.

For an arbitrary set map \(d:X\to X\), the diagram

\[
Y_{X,d}=\bigl(C(X)\mathrel{\substack{\xrightarrow{i_X}\\[-.5ex]\xrightarrow[d^*]{}}}\Omega^X\bigr)
\]

is well defined even when \(d\) is discontinuous. The map \(d^*\) takes values in all functions. Under N, both sides of \(H(i_X)\) are setwise evaluations, so \(H(i_X)\) is bijective. This proves \(Y_{X,d}\in\mathcal C\). The proof neither makes the second sort finite-supported nor assumes continuity of \(d\).

## 5. Theorem 8: arbitrary factorization targets

For a factorization \(Y_{X,d}\xrightarrow a Z\xrightarrow b B\) in which \(Z\in\mathcal C\) and \(ba=\psi_{x_0}\), put

\[
T=H(Z_0),\quad S=H(Z_1),\quad u=H(p_Z),\quad v=H(q_Z),
\quad h=H(a_0):T\to X,\quad \ell=H(a_1):S\to X.
\]

Both naturality squares were checked with their contravariant directions. They give

\[
hu=\ell,\qquad hv=d\ell.
\]

Since \(u\) is bijective, \(k=vu^{-1}\) is a set selfmap of \(T\) and \(hk=dh\). Continuity of \(k\) is unnecessary. The space \(T\) is compact, and \(h\) is continuous by precomposition followed by the homeomorphism of §4. Hence \(h(T)\) is closed in \(X\), forward invariant under \(d\), and contains \(x_0\), since \(h(b_0)=x_0\).

When the closed forward-invariant hull of \(x_0\) is \(X\), it follows that \(h\) is onto and

\[
|X|\leq |H(Z_0)|\leq\omega^{|Z_0|}.
\]

This argument applies to every factorization target in \(\mathcal C\), without assuming a quotient presentation, a monomorphism, or finite support of \(Z_1\). That unrestricted quantifier is exactly what the subsequent solution-set obstruction needs.

## 6. Ordinal witnesses and Corollary 9

For every infinite cardinal \(\kappa\), the ordinal space \([0,\kappa]\) is compact, Hausdorff, and zero-dimensional. The initial intervals \([0,\beta]\) for \(\beta<\kappa\), suitable differences of them, and terminal intervals supply the clopen neighbourhoods, including the endpoint cases.

The successor map, with \(\kappa\) fixed, has all of \([0,\kappa]\) as the closed forward-invariant hull of 0. Transfinite induction uses invariance at successors and closedness at limits. This works for singular as well as regular \(\kappa\), and never uses continuity of the successor map.

Given a set-indexed family \(b_i:Z_i\to B\), choose an infinite \(\kappa\) larger than every \(|H((Z_i)_0)|\). The ordinal witness \(\psi_\kappa\) cannot factor through any \(b_i\), by Theorem 8. Thus the family is not weakly terminal. A coreflection would supply a terminal object, so NC follows.

This is a failure of the solution-set condition at the fixed target, not just an unbounded collection of witness carriers. No additional large-cardinal hypothesis beyond N enters this deduction.

## 7. Additional checks and limits

The internal-monomorphism argument in Lemma 10 and the test-deletion comparison in §9.1 were also reconstructed without finding a gap. In Lemma 10, the agreement locus is closed because \(H(T_0)\) is Hausdorff; compactness of that space is not required. Injectivity of \(H(p_T)\) makes the locus successor-stable. Coordinate evaluations then separate both components. These are monomorphisms internal to the uniqueness class, not ambient monomorphisms. In §9.1, restriction to the initial \(\omega\) gives the stated common factorization, and the identity in \(\Omega^\omega\) indeed lacks finite support.

The assertion about monocoreflectivity of arbitrary mono-test classes, the external positive implication VP⇒P, the surrounding independence packaging, bibliographic novelty, and the rendered PDF were not audited here. None is used in the proof of NC. No finite computation or formal prover was used as a substitute for the all-cardinal argument.

**Audit conclusion:** all dependencies of NC through Corollary 9 pass this independent agent proof audit. No correction or missing lemma was required. This upgrades the checked dependency status for No.4; it does not itself establish any unproved closure property of the No.4 candidate class.
