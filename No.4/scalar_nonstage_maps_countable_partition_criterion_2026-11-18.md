# An exact countable-partition criterion for non-stage scalar maps

2026-11-18. Status: direct structural reduction. No non-stage map or
idempotent is constructed here.

Let \(\Omega=\omega\), \(M=\operatorname{End}(\Omega)\), and let
\((T_\alpha)_{\alpha<\omega_1}\) be the original coinfinite-injection
inverse system. Write

\[
K=\operatorname*{colim}_{\alpha<\omega_1}\Omega^{T_\alpha}.
\]

## 1. Decomposition into countable quotient powers

For a set \(S\), let \(\operatorname{Part}_\omega(S)\) be the poset of
partitions of \(S\) with at most countably many blocks, ordered by
refinement. Write \(q:S\twoheadrightarrow Q_q\) for the quotient map.
This poset is directed: finitely many countable partitions have a common
countable refinement.

There is a directed-union presentation in \(M\)-Set:

\[
\Omega^S=
\operatorname*{colim}_{q\in\operatorname{Part}_\omega(S)}\Omega^{Q_q},
\tag{1}
\]

where each inclusion is precomposition with \(q\). Indeed, any function
\(S\to\Omega\) factors through its countable image partition.

For nonempty countable \(Q\), the \(M\)-act \(\Omega^Q\) is cyclic.
Choose an injection \(b:Q\to\Omega\); every \(Q\to\Omega\) is
\(m b\) for some \(m\in M\). Therefore any map
\(\Omega^Q\to K\) factors through one stage: the image of its generator
lies in a stage, and that stage is a subact. Relations are preserved
because the stage inclusion is monic.

Furthermore, every \(M\)-map \(\Omega^Q\to\Omega\) is evaluation at a
point of \(Q\), in ZFC. To see this, its value on \(b\) must lie in
\(b(Q)\), since all selfmaps fixing \(b(Q)\) pointwise fix \(b\).
Equivariance then determines the map as evaluation at the corresponding
point. Componentwise this gives

\[
\operatorname{Hom}_M(\Omega^Q,\Omega^{T_\alpha})
\cong\operatorname{Set}(T_\alpha,Q).
\]

The empty \(Q\) case has the same formula: \(\Omega^\varnothing=1\)
has no map into the nontrivial scalar powers or their union, because the
constant endomorphisms have no common fixed point there.

Combining these facts with (1) gives the ZFC identity

\[
\operatorname{Hom}_M(\Omega^S,K)
\cong
\lim_{q\in\operatorname{Part}_\omega(S)}
\operatorname*{colim}_{\alpha<\omega_1}
\operatorname{Set}(T_\alpha,Q_q).
\tag{2}
\]

Here the transition maps in the colimit are precomposition with the
surjective restrictions between the \(T_\alpha\). If \(q'\) refines
\(q\), with \(q=rq'\), the compatibility condition for the family on
the right is

\[
[\tau_q]=[r\tau_{q'}].
\]

Thus a scalar map is exactly a coherent selection of a countable-partition
block at some stage for every countable partition. The stage can depend
on the partition.

## 2. Which such maps factor through one stage?

Under N, the Isbell theorem identifies all maps between arbitrary full
powers with coordinate maps. Consequently the stage-factorizing maps in
(2) are exactly the image of

\[
\operatorname*{colim}_{\alpha<\omega_1}
\operatorname{Set}(T_\alpha,S)
\longrightarrow
\lim_q\operatorname*{colim}_{\alpha<\omega_1}
\operatorname{Set}(T_\alpha,Q_q),
\tag{3}
\]

where \(\tau\) is sent to \(([q\tau])_q\).

Therefore an actual non-stage scalar map would be witnessed by a
compatible family on the right of (3) that does not arise from one stage
and one \(S\)-valued coordinate function. The existing scalar theorem
shows that no such family exists when \(|S|\leq\mathfrak c\). It does
not settle larger \(S\).

## 3. The remaining scalar obstacle at the template Y_omega_1

Let

\[
R=Y_{\omega_1}=
\bigl(\operatorname{Cont}([0,\omega_1],\Omega)
\rightrightarrows\Omega^{[0,\omega_1]}\bigr).
\]

Its first carrier has cardinality \(\aleph_1\), and its second carrier
has cardinality \(2^{\aleph_1}\). The latter may exceed
\(\mathfrak c\); equality is not decided by ZFC.

Neither sort is countably generated as an \(M_1\)-act. For the first
sort, every continuous function is eventually constant. Countably many
such functions have a common bounded initial segment after which all are
constant, and postcomposition cannot introduce a new variation later.
They therefore cannot generate all continuous functions.

For the second sort, take any countable family \((r_n)\). Recursively
choose disjoint pairs of coordinates \(\xi_n\ne\eta_n\) on which
\(r_n\) has the same value; an uncountable fiber exists because the
coordinate set is uncountable and the range is countable. A binary
function separating every chosen pair belongs to none of the orbits
\(M_1r_n\). This proof also covers the cardinal-arithmetic case
\(2^{\aleph_1}=\mathfrak c\).

The initially suggested second obstruction—unbounded stages across an
uncountable target generating family—has now been eliminated. The
[coordinate-stage uniformization theorem](coordinate_stage_uniformization_by_pair_coloring_2026-11-18.md)
proves that if all scalar coordinates of a map \(E(Y)\to V^R\) have
coordinate-induced stage lifts, then they have lifts at one common stage,
regardless of the size or generating rank of \(R\). Its proof uses a
binary coloring separating uncountably many pairs; it does not require a
countable target generating family.

Thus for a proposed map \(E(T_\alpha\cdot R)\to V^R\), the remaining
possibility is that an individual scalar coordinate fails to factor,
because its source coordinate set has size \(2^{\aleph_1}\), outside
the currently proved bound \(\mathfrak c\).

In particular, if \(2^{\aleph_1}=\mathfrak c\), all source-stage dual
carriers have size at most \(\mathfrak c\). The scalar theorem and
coordinate-stage uniformization then imply that all self-equalizers and
retracts of the original \(V^{Y_{\omega_1}}\) belong to \(\mathcal M\).
No such conclusion is established here when
\(2^{\aleph_1}>\mathfrak c\).

To produce an endomorphism of \(V^R\), such coordinate families must also
respect the \(M_1\)-actions, the two arrows \(p,q\), and the source-stage
transition maps. To produce a retract counterexample, the assembled
endomorphism must additionally be idempotent and have a fixed image
outside \(\mathcal M\). None of these existence assertions follows
merely from the failure of the previous size bounds.
