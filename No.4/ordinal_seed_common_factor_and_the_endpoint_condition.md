# A single ambient factor for all ordinal seeds and its membership test

**Subsequent result.** The least hull satisfies equation (1) below, and
the resulting maps identify all later least hulls whenever the target is
in \(\mathcal A\). [Proof of stabilization](ordinal_hulls_stabilize_via_a_relative_two_cut_test.md)

Keep the notation of the [explicit (EQ_C) obstruction](two_cuts_refute_eq_c_and_escape_nonmonic_factorization.md).
Let \(H_\delta\) be the intersection of all ambient subobjects of
\(E(Y_\delta)\) belonging to \(\mathcal A\) and containing the image of
\(j_0\). This is a set-indexed intersection in a presheaf category, so
\(H_\delta\in\mathcal A\) and \(H_\delta\subseteq L\). Write \(D_\gamma g\)
for the shift of \(g\) on \([0,\gamma]\) with endpoint fixed.

## What restriction has to preserve

For \(\kappa>\delta\), restriction of ordinal functions to \([0,\delta]\)
in each sort gives two functions \(r_i:(Y_\kappa)_i\to(Y_\delta)_i\).
Both are equivariant. Precomposing observations with these restrictions
respects the two actions and the first structural arrow. For a
second-sort observation \(F\), the second arrow requires exactly

\[
 F(D_\delta h)=F\big((D_\delta h)[\delta\gets a]\big)
 \qquad(h\in C([0,\delta],\omega),\ a\in\omega).
 \tag{1}
\]

Indeed, if \(h=g|_{[0,\delta]}\), the two shifted restrictions agree
strictly below \(\delta\), and their endpoint values are \(h(\delta)\)
and \(g(\delta+1)\). Every pair \(h,a\) occurs: extend \(h\) with the
constant value \(a\) on \([\delta+1,\kappa]\), which preserves continuity.
Consequently \(\kappa=\delta+1\) tests the same condition as every larger
\(\kappa\).

Take \(J_0=L_0\) and let \(J_1\) consist of those \(F\in L_1\) satisfying
(1). The condition is stable under both actions. For right relabeling
by \(m\), the pair in (1) becomes the same kind of pair for \(mh,ma\).
Since both structural arrows go into sort zero, this defines an ambient
subpresheaf \(J\). It contains the seed. Precomposition with \(r_i\)
therefore gives \(J\to E(Y_\kappa)\) over the seed for every \(\kappa>\delta\).
For \(\kappa\le\delta\) precompose observations with the dual map
\(Y_\kappa\to Y_\delta\) extending ordinal functions constantly after
\(\kappa\). That extension commutes with both structural arrows.
Thus one fixed set-sized \(J\) factors every ordinal seed map in the
ambient category. No claim that all ordinal targets lie in \(D\) is
needed for the factorization.

## An explicit failure and what is still open

Let \(w\) be zero below \(\delta\) and one at \(\delta\), and
\(F=\chi_{\{w\}}\) on \((Y_\delta)_1\). All five-piece rows of the
two-cut construction have a constant tail including \(\delta\); the
standard rows are constant everywhere. Hence both maps take \(F\) to
zero and \(F\in L_1\). Taking \(h=0,a=1\) gives opposite sides in (1).
In particular the proposed restriction map already fails on \(L\) at
\(\kappa=\delta+1\).

Nevertheless \(J\) has the same balanced elements in both sorts as \(L\).
In the ambient powers these are precisely the evaluations, by the ZFC
cardinal bound at \(\delta\). For \(\xi<\delta\) the two maps agree on
\(u_\xi\) and \(v_\xi\): on the large set \(t>\xi\) both second-sort
rows evaluate the first coordinate and both first-sort rows evaluate
the first projection. At \(\delta\) the two endpoint evaluations differ
under the two maps (also forced in sort one by their first structural
images). Each \(v_\xi\) for \(\xi<\delta\) satisfies (1). In particular
the unique balanced extension condition still holds in \(J\). Neither
this fact nor the ambient factorization establishes membership in
\(\mathcal A\).

The following statements are equivalent:

1. An \(\mathcal A\)-subobject of \(E(Y_\delta)\) containing the seed
   admits the two canonical restriction formulas as a map to
   \(E(Y_{\delta+1})\).
2. \(H_\delta\subseteq J\).
3. Those formulas are maps on \(H_\delta\) for every \(\kappa>\delta\).

For (1) intersect the proposed subobject with \(L\), and use minimality
of \(H_\delta\) and (1) above. The reverse implications follow from
the same restriction calculation. Deciding this inclusion is open.
Excluding just the displayed singleton indicator from the hull would
settle only one test. A positive answer would supply a single
\(\mathcal A\)-factor for the ordinal seeds. A solution set at \(X\)
must additionally cover maps to all objects of \(\mathcal A\).
