# The two-cycle does not receive the ordinal seed hull

**Theorem (ZFC).** Let \(T_0=T_1=\omega^2\) with componentwise
relabeling, \(p_T=\mathrm{id}\), and \(q_T(a,b)=(b,a)\). Let
\(j_{\rm cyc}:X\to E(T)\) be the seed given by the first projection.
Writing \(\eta:X\to H_\delta\) for the
[stabilized ordinal seed](ordinal_hulls_stabilize_via_a_relative_two_cut_test.md),
there is no \(k:H_\delta\to E(T)\) with \(k\eta=j_{\rm cyc}\).
In fact \(\mathcal P(H_\delta,E(T))=\varnothing\). The earlier
factorization of every initial ordinal evaluation through \(H_\delta\)
still holds.

Here \(\mathcal A\) is the least full replete class containing
\(D=\operatorname{Repl}(E(C^{op}))\) and closed under small limits and
directed unions. We prove an operation exists in every object of
\(\mathcal A\). Merely writing down a function on the ambient ordinal
power would leave open whether it belongs to \(H_\delta\).

## 1. Finite iterates and the first mismatch

For \(Y\in C\), a seed \(f:X\to E(Y)\) is an equivariant function
\(h_0:Y_0\to\omega\). There is a unique character
\(\widetilde h_n:Y_1\to\omega\) such that \(\widetilde h_n p_Y=h_n\),
and we set \(h_{n+1}=\widetilde h_n q_Y\). For \(y\in Y_0\) call
\((h_n(y))_{n<\omega}\) its trace from \(f\).

This iteration has a functorial meaning on every \(Z\in\mathcal A\).
Put \(B=(\omega\rightrightarrows 1)\), \(X=E(B)\), and
\(U=(\omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\omega)\).
Let \(u,v:X\to E(U)\) be dual to the maps \(U\to B\) with first
components \(\pi_0,\pi_1\), respectively. Every \(X\to Z\) extends
uniquely along \(u\): this holds on \(D\) by character extension, on
limits by uniqueness, and on directed unions of monomorphisms since
both \(X\) and \(E(U)\) are finitely generated. For existence put the
seed in one stage; for uniqueness put the images of both proposed
extensions in one stage and reflect equality there by monicity.
Precomposing the unique extension with \(v\) gives the next seed.
Denote the values of its iterates on the sort-zero identity generator
by \(z_0,z_1,\ldots\). On \(E(Y)\) these are the \(h_n\).
The [finite tests and their presentations](general_equalizers_finite_orthogonality_and_quotient_reduction_2026-11-17.md)
give the maps explicitly.

Two more properties transfer from the powers to \(\mathcal A\).

* Every finitary operation \(\omega^k\to\omega\), \(k\ge1\), acts
  naturally on a sort. For a fixed bijection \(\omega^k\cong\omega\)
  a tuple has a unique code with the prescribed unary projections.
  This existence and uniqueness is preserved by limits, and by directed
  unions since the tuple and any two proposed codes fit in a stage.
  Apply the desired operation as a unary map to the code.
* The unary tests \(d_n(t)=\mathbf1_{\{n+1\}}(t)\), \(n<\omega\),
  jointly distinguish elements of a sort. They distinguish natural
  numbers, hence functions in every power. Limits inherit this property
  componentwise; in a directed union, two elements are in one stage
  and the inclusion reflects each equality there.

Fix a word \(w\in\omega^\omega\). For a seed in a full power,
define a sort-zero element pointwise by

\[
 C_w(f)(y)=
 \begin{cases}
  0 & \text{if } h_i(y)=w_i\ \text{for every }i,\\
  1+\min\{i:h_i(y)\ne w_i\} & \text{otherwise}.
 \end{cases}
\]

For all \(Z\in\mathcal A\) and all seeds \(f:X\to Z\), a unique element
\(C_w(f)\in Z_0\) is characterized by the equations

\[
 d_n(C_w(f))=b_{n,w}(z_0,\ldots,z_n)\qquad(n<\omega),
\]

where the finitary operation \(b_{n,w}\) has value one precisely when
the first \(n\) entries match \(w\) and the entry at \(n\) differs.
Uniqueness is joint separation by the \(d_n\). A map between objects
with such elements preserves them, by naturality of finite iterates and
finitary operations followed by uniqueness. Existence holds on \(D\)
by the displayed pointwise formula. For a limit of objects with this
existence property, the elements for the projected seeds are compatible
by uniqueness and hence define a limit element. For a directed union
the single seed \(f\) lands in a stage because \(X\) is finitely
generated. Its element at that stage satisfies every equation in the
union. Thus the class with existence is closed under both operations.
This proves the assertion without assuming general closure under
countable operations on independently specified elements.

## 2. The obstruction

Take \(w=(0,1,0,1,\ldots)\) and the unary maps
\(e(t)=\mathbf1_{\{0\}}(t)\), \(c_0(t)=0\). In \(E(Y_\delta)\) the
iterates of the initial seed give \(h_n(g)=g(n)\). Continuity into
discrete \(\omega\) at the ordinal \(\omega\) makes this sequence
eventually constant for every \(g\in(Y_\delta)_0\). Hence no \(g\)
realizes \(w\), and in sort zero

\[
 e(C_w(j_0))=c_0(C_w(j_0)).
\]

The inclusion \(H_\delta\hookrightarrow E(Y_\delta)\) preserves the
constructed element and is monic, so the same equation holds at
\(\eta\) inside \(H_\delta\). In \(E(T)\), the iterates of \(j_{\rm cyc}\)
on \((a,b)\) give \(a,b,a,b,\ldots\). At \((0,1)\) its counter is zero.
The two sides of the equation therefore have values one and zero at
that point. A map over \(X\) would preserve the equation.

The other projection also realizes \(w\), at \((1,0)\). These are the
only two seeds \(X\to E(T)\): an equivariant \(\omega^2\to\omega\)
is a projection by checking the generating tuple \((0,1)\) and all
relabelings fixing it. The seed identification uses only countable
carriers in \(B\). Also \(T\in C\) since \(p_T=\mathrm{id}\) and a pair
has finite support. This proves the empty Hom-set assertion as well as
failure of the chosen extension.

Every finite prefix of \(w\) does occur on the ordinal: extend that
prefix by zeros on the rest of \([0,\delta]\). The countable family of
tests on a single element is what distinguishes this target.

## 3. Consequences for other orbits

More generally let \(K\hookrightarrow E(Y)\) be an \(\mathcal A\)-subobject
containing a seed \(f\), where \(Y\in C\). If \(K\to E(Y')\) sends this
seed to \(f'\), \(Y'\in C\), then every first-sort trace realized in
\((Y',f')\) is realized in \((Y,f)\). For any missing word \(w\) the
same equation for \(C_w\) holds in \(K\) and hence at \(f'\).
In particular, any seed reached from \(H_\delta\) in a \(D\)-object
has only eventually constant first-sort traces.

For a deterministic system on a set \(S\), put
\[
 Y_d=(\operatorname{FinIm}(S,\omega)
     \overset{\mathrm{id},d^*}{\rightrightarrows}
     \operatorname{FinIm}(S,\omega)),\qquad d:S\to S .
\]
Here the symbol \(\operatorname{FinIm}\) denotes all finite-image
functions, \(d^*g=g\circ d\), and \(Y_d\in C\). For \(s\in S\),
the seed given by evaluation at \(s\) extends across \(\eta\) **if
and only if \(d^m(s)=d^{m+1}(s)\) for some finite \(m\)**.

Indeed, an orbit with no repetitions admits a binary observable
alternating on its successive states. A finite orbit that enters a
cycle of length greater than one admits an observable that takes
distinct values on the cycle. In either case a non-eventually-constant
trace is realized. Conversely, if the orbit reaches a fixed point at
step \(m\), the map \(Y_d\to Y_m\) sends \(g\) in either sort to the
word \( (g(d^i(s)))_{0\le i\le m}\). Both structural squares hold,
including at \(m\), and initial evaluation pulls back to evaluation
at \(s\). Dualize and precompose with the known \(H_\delta\to E(Y_m)\).
This proves sufficiency even when \(S\) is infinite.

## 4. A joint factor after adding the missing traces

There is also a concrete way to retain the ordinal result while covering
the two-cycle. Put \(F=\operatorname{FinIm}(\omega,\omega)\) and use the
finite-image sequence template \(P=(F\overset{\mathrm{id},\mathrm{shift}}
{\rightrightarrows} F)\), rooted at evaluation at zero. This template
also appears in [the earlier reduced-power analysis, §3](../No.1/codex_sset_handoff/investigations/lower_bound_reduced_powers_accessibility_boundary_2026-11-17.md).
It lies in \(C\). Sending a pair \((a,b)\) to its alternating word in
both sorts gives a rooted map \(T\to P\).

More generally, for a rooted \(Y\in C\) use
\[
 y\longmapsto(h_n(y))_{n<\omega}\quad\text{in sort zero},\qquad
 v\longmapsto(\widetilde h_n(v))_{n<\omega}\quad\text{in sort one}.
\]
The first sequence has finite range: all its entries belong to a
finite support of \(y\), since a relabeling fixing that support fixes
\(y\). If every second sequence has finite range too, these formulas
define a rooted \(Y\to P\). They are equivariant, and the squares are
exactly \(\widetilde h_n p_Y=h_n\) and
\(\widetilde h_n q_Y=h_{n+1}\). In particular this covers every seed
in every \(Y\in C\) with both sorts finite-support.

Take the least \(\mathcal A\)-subobject of \(H_\delta\times E(P)\)
containing the diagonal seed. Its two projections give a single rooted
object of \(\mathcal A\) which factors every initial ordinal seed and
all the seeds just covered by \(P\). Its projection to \(H_\delta\)
has no section over \(X\), since composing such a section with the map
to \(E(T)\) would give the impossible extension. Whether the enlarged
object covers every rooted \(Y\in C\) is open here, as is Problem 4.

The proof was checked directly. It has not had independent review or
formal verification.
