# An explicit ZFC counterexample to (EQ_C)

Write \(c=2^{\aleph_0}\) and \(\delta=(2^c)^+\). Use the two arrows
\(\theta,b:E(Y_\delta)\rightrightarrows U\) and their ambient equalizer
\(L\) from the [two-cut construction](two_cuts_give_an_actual_m_equalizer_failure.md).
Here \(Y_\delta\) has first carrier the continuous functions on the compact
ordinal \([0,\delta]\) with values in discrete \(\omega\), second carrier
all such set-functions, and arrows inclusion and successor pullback.
Denote the two evaluations at \(\xi\) by \(u_\xi,v_\xi\).
The map \(j_0:X\to E(Y_\delta)\) sends the identity generator to \(u_0\).
It factors through \(L\), whereas \(u_\delta\notin L_0\).

**Theorem.** These specific data refute [(EQ_C) as originally
defined](general_equalizers_finite_orthogonality_and_quotient_reduction_2026-11-17.md)
in ZFC. Moreover \(L\notin H_{\rm fg}\) even if arbitrary presheaf maps
from arbitrarily large intermediate objects \(E(Q)\) are allowed.
Every full replete class containing \(D\) and closed under directed unions
and small limits contains \(L\).

## 1. A short proof for the stated (EQ_C)

Both carriers of \(Y_\delta\) have one action component. Relabeling by the
constant zero map takes every element to the same zero function. The
component bound in (EQ_C) therefore holds. The object \(X\) is generated
by the identity in its first sort and zero in its second. We have
\(U\in M_{\rm bfs}\subseteq H_{\rm fg}\), \(Y_\delta\in C\), and
\(\theta j_0=bj_0\), all in ZFC by the two-cut construction.

Suppose a proposed \(q:Y_\delta\to Q\), \(Q\in C\), satisfies its seed
condition. By currying, \(j_0\) factors through \(E(q)\). The image of
the identity generator in \(E(Q)_0\) is balanced, that is, it is an
equivariant function \(Q_0\to\omega\). Its composite with \(q_0\) is
\(u_0\). Consider the image of

\[
H(Q_0)\longrightarrow H((Y_\delta)_0)=[0,\delta],\qquad h\longmapsto hq_0 .
\]

This map is continuous for the pointwise topologies. Its domain is
compact because \(Q_0\) has finite support pointwise. Each character takes
each point into a finite support of that point, and the character equations
are closed in the product of those finite sets. The image is therefore
closed and contains zero. If it contains \(\xi\), extend the chosen
character uniquely across \(p_Q\). Its pullback along \(q_1\) must be
\(v_\xi\), by the unique-extension property of \(Y_\delta\). Pullback along
the other structural arrow gives \(u_{d(\xi)}\) in the first image, where
\(d\) takes successors and fixes the endpoint. Transfinite induction gives
the entire ordinal, including \(\delta\). In particular \(u_\delta\) is in
the image of \(E(q)_0\), contradicting \(\theta E(q)=bE(q)\).
This proof puts no surjectivity requirement on \(q\) and uses no cardinal
bound on \(Q\).

## 2. Arbitrary presheaf intermediates

In ZFC a map \(k:E(Q)\to E(Y_\delta)\) need not a priori be of the form
\(E(q)\). We prove that if \(j_0\) factors through such a \(k\), then
\(k\) is surjective in both sorts, for every \(Q\in C\).

For each point \(s\) of a target dual carrier, the scalar component
\(\ell_s(F)=k_i(F)(s)\) of the left-equivariant map is evaluation along
a countably complete ultrafilter on \(Q_i\). Indeed, finite operations
are preserved by coding tuples in \(\omega\). On indicators this yields
an ultrafilter, and the indicator of the fibre at \(\ell_s(F)\) has scalar
value one. This selects a cell of every countable partition and implies
countable completeness. If \(Q_i\) were empty there could be no such
scalar, since \(\omega\) has no point fixed by all relabelings.

Every such ultrafilter, on a set of **any** size, is closed under
intersections of at most \(\delta\) members. Indeed, its pushforward
along a map to a set of size at most \(\delta\) is principal.
For completeness, countably complete ultrafilters on a countable set
are principal. If the assertion holds up to \(\mu\), every countably
complete ultrafilter selects a cell in every partition of size at most
\(\mu\), by pushforward. Partitioning by the first failed condition shows
it is closed under \(\mu\) intersections. On a set of size at most
\(2^\mu\), intersecting the selected sides of \(\mu\) separating bits now
gives a singleton. Iterating covers \(\delta\le 2^{2^c}\).
The partition by the first failed condition applies once more to give
the claimed completeness on \(Q_i\).

For the general relation between the completeness of a nonprincipal
ultrafilter and measurable cardinals, see [D. A. Martin, *Determinacy of
Infinitely Long Games*, Lemma 3.1.3](https://www.math.ucla.edu/~dam/D.A._Martin_Determinacy_of_Infinitely_Long_Games.pdf).
The finite powerset argument above suffices here.

It follows that \(k_i\) commutes with every pointwise operation
\(o:\omega^J\to\omega\) for \(|J|\le\delta\). For a family
\((F_j)\), intersect the selected fibres of all \(F_j\) for the scalar
in question. The composite has the claimed constant value on this
ultrafilter-large intersection.

Now lift every \(u_\xi\) to a balanced \(a_\xi\in E(Q)_0\) by recursion.
The map from \(X\) gives \(a_0\). Given \(a_\xi\), its unique balanced
extension \(b_\xi\in E(Q)_1\) maps to \(v_\xi\), since \(k\) preserves
balanced elements and commutes with the first structural map. Pullback
along the second gives the successor lift whenever \(\xi<\delta\).
At a nonzero limit \(\lambda\le\delta\), choose an ultrafilter on
\(\lambda\) containing all final segments. At each point of \(Q_0\) the
previous lifts take values in a common finite set, namely a finite support
of that point. Their pointwise ultrafilter limit thus exists and is
equivariant, because each relabeling preserves limits of finite-range
families. This pointwise limit is the application of a single total
operation of arity \(|\lambda|\) (give it value zero on tuples with no
selected fibre). By the preceding paragraph its image under \(k_0\)
is \(u_\lambda\), since every continuous ordinal function is eventually
constant with value at \(\lambda\) along ordinals approaching \(\lambda\)
from below. Extend the last lift as well to obtain \(b_\delta\).

Finally every function \(G:(Y_\delta)_i\to\omega\) is a pointwise
operation of arity \(|[0,\delta]|=\delta\) applied to all the evaluations
of that sort. The evaluation tuple is the dual point itself, and one
can extend \(G\) arbitrarily off that set of tuples. Apply the operation
to their lifts. Its image is \(G\), proving both surjections.
If \(L\) belonged to \(H_{\rm fg}\), its map from the finitely generated
\(X\) would factor through some \(E(Q)\); composing with the inclusion of
\(L\) would contradict even the endpoint part of this proof.

## 3. The least closure really contains the equalizer

Let \(\mathcal A\) be the least full replete class containing \(D\) and
closed under small limits and directed unions. In the two-cut reduced
power \(U\), index subobjects by partitions of the row set into at most
\(c\) cells. For a partition, take the germs of tables constant on each
positive cell, allowing a change on a filter-small set. The union of
all nonpositive cells is small by \(c^+\)-completeness. The subobject
is a copy of \(E(\coprod T)\), one summand per positive cell. Positivity
makes the table on each such cell unique. These coproducts are in
\(C_{\rm bfs}\). Refinement enlarges the subobject, and two partitions
have a common refinement of size at most \(c\). Every single germ occurs
in one of these subobjects by partitioning by its row table, since the
carriers of \(T\) are countable. This exhibits \(U\) as an actual directed
union of \(D\)-subobjects. Taking the equalizer with domain \(E(Y_\delta)\)
now gives \(L\in\mathcal A\).

In particular no full class between \(D\) and \(H_{\rm fg}\) can satisfy
both closure requirements, even allowing a choice of which objects to
include. Reflectivity of \(\mathcal A\) is a separate question.

The arguments here are direct mathematical checks; they have not had
independent review or formal verification.
