# Long unions obstruct cogeneration by fixed-length V templates

2026-11-18. Status: direct conditional argument. The application below uses
the separate theorem that every map from a full Isbell object into the
original V-template union factors through a stage. It does not provide a
Problem 4 counterexample or a retract counterexample.

**Later strengthening:** the
[tail-object Ulam-matrix argument](monic_local_tail_object_not_cogenerated_by_v_templates_2026-11-18.md)
gives a different \(\mathcal M\)-object with no nonterminal
\(V^R\)-valued maps in ZFC, without the conditional stage theorem used
here. That result is the stronger obstruction to the proposed
cogeneration family. The cofinality argument below remains valid.

## 1. An elementary cofinality obstruction

Let \(\lambda\) be a regular cardinal, \(\mu<\lambda\) an infinite
cardinal, and suppose

\[
Z=\bigcup_{\alpha<\lambda}D_\alpha,\qquad
W=\bigcup_{\beta<\mu}W_\beta
\]

are increasing unions of subobjects in a presheaf category. Assume every
map \(D_\alpha\to W\) factors through some \(W_\beta\). Then every
map \(u:Z\to W\) also factors through one \(W_\beta\).

Indeed, let \(b(\alpha)<\mu\) be the least stage containing the image
of \(u|_{D_\alpha}\). The function \(b\) is nondecreasing. For each
value in its range, take its first occurrence. There are at most \(\mu\)
such ordinals, and regularity of \(\lambda>\mu\) bounds them below
some \(\alpha_*<\lambda\). Monotonicity implies that \(b(\alpha_*)\)
is a maximum of the entire range. Hence every restriction, and therefore
\(u\), lands in \(W_{b(\alpha_*)}\).

The argument uses only monic stage inclusions and the displayed
stage-factorization assumption.

## 2. A longer actual M-object with no D-valued maps

Put \(\kappa=\mathfrak c\) and \(\lambda=\kappa^+\). For
\(\alpha<\lambda\), define

\[
S_\alpha=\{s:\alpha\hookrightarrow\kappa:
|\kappa\setminus\operatorname{im}(s)|=\kappa\}.
\]

Every \(S_\alpha\) is nonempty. Restriction
\(S_\beta\to S_\alpha\), \(\alpha\leq\beta<\lambda\), is
surjective: divide the remaining \(\kappa\) points into two sets of size
\(\kappa\), use one to extend the injection over \(\beta\setminus\alpha\),
and reserve the other. But

\[
\lim_{\alpha<\lambda}S_\alpha=\varnothing,
\]

since a compatible family would unite to an injection
\(\kappa^+\hookrightarrow\kappa\).

Let \(R_*=(\Omega\mathrel{\substack{\xrightarrow{1}\\[-.5ex]\xrightarrow[1]{}}}\Omega)\in\mathcal C\),
and set

\[
Z_{\mathrm{long}}
=\operatorname*{colim}_{\alpha<\lambda}E(S_\alpha\cdot R_*).
\]

This is a directed union of \(\mathcal D\)-subobjects, so
\(Z_{\mathrm{long}}\in\mathcal M\) in ZFC. Both its components are
nontrivial, since constant zero and constant one remain distinct through
the monic transitions.

Under N, Isbell full faithfulness and the colimit-to-limit property of
\(\operatorname{Hom}_{M_2}(-,\Omega)\) give, in each sort,

\[
\operatorname{Hom}_{M_2}((Z_{\mathrm{long}})_i,\Omega)
\cong\lim_{\alpha<\lambda}(S_\alpha\times\Omega)
=\varnothing.
\tag{1}
\]

Consequently a map \(Z_{\mathrm{long}}\to E(Y)\) is possible only
when both \(Y_i\) are empty: a point \(y\in Y_i\) would supply a
coordinate evaluation contradicting (1). Thus the only full Isbell
codomain admitting a map from \(Z_{\mathrm{long}}\) is the terminal
one.

## 3. Consequence under the full stage-factorization theorem

Let \(V^R\) denote the **original** \(\omega_1\)-length union based on
coinfinite injections into \(\omega\), allowing arbitrary
\(R\in\mathcal C\). Assume the following statement:

> Every map \(E(Y)\to V^R\), for arbitrary \(Y\in\mathcal K\),
> factors through a stage \(E(T_\beta\cdot R)\), \(\beta<\omega_1\).

The separate [large-kernel-ideal analysis](nonstage_scalar_maps_require_inner_measurable_2026-11-18.md)
proposes this conclusion under the absence of an inner model with a
measurable cardinal. The present argument is conditional on that precise
stage statement, so does not re-audit its set-theoretic input.

Apply Section 1 with \(\mu=\omega_1\) and
\(\lambda=\mathfrak c^+>\omega_1\). Any map
\(Z_{\mathrm{long}}\to V^R\) then factors through one full Isbell
stage. Equation (1) implies that both sorts of \(R\) must be empty.

Therefore, under N and the stated full stage-factorization theorem,
\(Z_{\mathrm{long}}\) has no maps into any nonterminal original
\(V^R\). In particular it cannot embed in any product of such templates,
even when the \(R\)'s vary arbitrarily: every factor admitting a map is
terminal, whereas \(Z_{\mathrm{long}}\) is nontrivial.

Thus cogeneration of all \(\mathcal M\)-objects by the original
\(\omega_1\)-length V templates cannot complete the equalizer argument.
This does not exclude a broader family in which the lengths and inverse
systems themselves vary, or a different kind of target.
