# Countably generated dual templates still have safe self-equalizers

2026-11-18. Status: direct ZFC proof, independently checked by the
mono-equalizer agent. This extends the previously proved countable-carrier
template result; it does not prove general retract closure of M.

**Later strengthening on the same date:** the
[coordinate-stage uniformization theorem](coordinate_stage_uniformization_by_pair_coloring_2026-11-18.md)
removes the countable-generation assumption on the target template from
Section 2. The source carrier bound remains necessary for the currently
proved scalar input. The arguments below are valid special cases.

## 1. Setting

Use the original \(\omega_1\)-chain

\[
T_\alpha=\{t:\alpha\hookrightarrow\omega:
\omega\setminus\operatorname{im}(t)\text{ is infinite}\},
\qquad\alpha<\omega_1,
\]

with surjective restriction maps, and put

\[
K=\operatorname*{colim}_{\alpha<\omega_1}\Omega^{T_\alpha}.
\]

The scalar factorization lemma in
[the V compression note](v_codomain_equalizers_root_compression_2026-11-17.md)
says that every \(M_2\)-map \(\Omega^S\to K\), with \(|S|\leq\mathfrak c\),
is induced at one stage by a map \(T_\alpha\to S\). This lemma is ZFC.

For \(R\in\mathcal C\), put

\[
V^R=\operatorname*{colim}_{\alpha<\omega_1}E(T_\alpha\cdot R).
\]

All stage inclusions are monic, and \(V^R\in\mathcal M\). Assume now
that each \(R_i\) is countably generated **as an \(M_1\)-act**. Its
carrier need not be countable. Since \(|M_1|=\mathfrak c\), its carrier
is nevertheless at most \(\mathfrak c\).

## 2. Stage factorization

Let \(Y\in\mathcal K\) have both carriers at most \(\mathfrak c\), and
let \(u:E(Y)\to V^R\) be a morphism. Then \(u\) factors through one
stage \(E(T_\beta\cdot R)\).

Choose countable generating families \((r_{i,j})_j\) for each \(R_i\).
For every such generator, evaluate the output at that coordinate:

\[
u_{i,j}:\Omega^{Y_i}\xrightarrow{u_i}(V^R)_i
\xrightarrow{\operatorname{ev}_{r_{i,j}}}K.
\]

The scalar lemma supplies a stage factorization for each \(u_{i,j}\).
Choose one common \(\beta<\omega_1\) above their countably many stages,
and write their scalar lifts as precomposition by

\[
\tau_{i,j}:T_\beta\to Y_i.
\]

For \(r=m r_{i,j}\), equivariance gives

\[
\operatorname{ev}_r u_i(f)
=\operatorname{ev}_{r_{i,j}}u_i(f\mathbin{\cdot}m).
\]

The right-hand side is represented at stage \(\beta\) by

\[
t\longmapsto f(m\tau_{i,j}(t)).
\tag{1}
\]

If \(r\) has two representations by generators, the two resulting
functions in (1) have the same image in \(K\). Since the scalar map
\(\Omega^{T_\beta}\to K\) is injective, they agree already at stage
\(\beta\), for every \(f\). Thus the formulas assemble to a map

\[
u_{\beta,i}:\Omega^{Y_i}\to\Omega^{T_\beta\times R_i}.
\]

Its composite into \((V^R)_i\) is \(u_i\). To check equality here, use
joint injectivity of the coordinate maps

\[
(V^R)_i\longrightarrow K^{R_i}.
\tag{2}
\]

Indeed, two elements of \((V^R)_i\) are represented at a common stage;
if all their scalar coordinates agree in \(K\), injectivity of that
stage's scalar inclusion makes all coordinates agree at the common stage.
This proves (2), even for uncountable \(R_i\).

Finally, all \(M_1\)-equivariance and diagram-arrow equations for the
assembled \(u_{\beta,i}\) follow from the corresponding equations for
\(u\), because \(E(T_\beta\cdot R)\to V^R\) is monic. The assembled
map is therefore a morphism in \(\mathcal P\).

The scalar lifts in (1) are explicitly coordinate-induced, so this stage
factorization does not invoke N or full faithfulness of E on arbitrary
large sets.

## 3. Equalizers and retracts

Let \(R,S\in\mathcal C\) be countably generated in each sort as
\(M_1\)-acts. Every stage dual \(T_\alpha\cdot R\) has carrier at most
\(\mathfrak c\). Therefore, for two maps

\[
a,b:V^R\rightrightarrows V^S,
\]

their restrictions to each source stage factor through a common target
stage. Their stage factorizations are coordinate-induced, and the
equalizer is the E-image of a coequalizer of the corresponding
\(\mathcal C\)-objects. It belongs to \(\mathcal D\), since
\(\mathcal C\) is closed under colimits.

The intersections of \(\operatorname{Eq}(a,b)\) with the source stages
form an increasing chain of these \(\mathcal D\)-subobjects, whose union
is the whole equalizer. Thus

\[
\operatorname{Eq}(a,b)\in\mathcal M.
\]

In particular every self-equalizer, and every retract, of \(V^R\) belongs
to \(\mathcal M\).

## 4. Application to the first non-finite-support ordinal template

For the ordinal template

\[
R=Y_\omega=
\bigl(\operatorname{Cont}([0,\omega],\Omega)
\rightrightarrows\Omega^{[0,\omega]}\bigr),
\]

the first sort is countable: its elements are sequences eventually
constant at the value at \(\omega\). The second sort has size
\(\mathfrak c\) and is not finite-support, but it is a cyclic
\(M_1\)-act. A bijection \([0,\omega]\to\Omega\) is a generator,
since every function on \([0,\omega]\) is obtained by postcomposition
with an endomorphism of \(\Omega\).

Thus \(Y_\omega\) satisfies the hypotheses above. The original
\(\omega_1\)-union \(V^{Y_\omega}\) has no retract or self-equalizer
counterexample to \(\mathcal M\)-membership.

The original argument above does not cover \(Y_{\omega_1}\), whose
full-function sort is not countably generated. The later uniformization
theorem does cover its self-equalizers and retracts when
\(2^{\aleph_1}=\mathfrak c\), because then the dual carriers of all
source stages satisfy the scalar bound. Neither argument automatically
covers a longer
\(\mathfrak c^+\)-chain of injections into \(\mathfrak c\), where the
sets \(T_\alpha\) can have size \(2^{\mathfrak c}\) and the source
carrier bound in the scalar lemma fails.
