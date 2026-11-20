# A single object of the least closure factors all ordinal seeds

Put \(c=2^{\aleph_0}\), \(\delta=(2^c)^+\), and \(S=[0,\delta]\).
Write \(Y=Y_\delta\). Its carriers are \(Y_0=C(S,\omega)\) and
\(Y_1=\omega^S\), with postcomposition by \(\mathrm{End}(\omega)\).
The two arrows are inclusion and pullback by successor with fixed endpoint.
In the presheaf category the corresponding arrows run from sort one to
sort zero. A balanced element of \(E(Y)_i\) is an equivariant function
on \(Y_i\).

Let \(\mathcal A\) be the least full replete class containing \(D=E(C^{op})\)
up to isomorphism and closed under small limits and directed unions.
Let \(H_\delta\subseteq E(Y)\) be the least \(\mathcal A\)-subobject
containing the ordinal seed \(j_0:X\to E(Y)\). It exists by taking
the set-indexed intersection inside \(E(Y)\in D\).

**Theorem (ZFC).** Every \(F\in(H_\delta)_1\) satisfies

\[
 F(r)=F(r[\delta\gets a])\qquad
 (r:S\to\omega\text{ of finite range},\ a\in\omega).
 \tag{*}
\]

Consequently \(H_\delta\) is a common factor in \(\mathcal A\) for all
the ambient seed maps \(X\to E(Y_\kappa)\). For every \(\kappa\ge\delta\)
with \(E(Y_\kappa)\in\mathcal A\), the least seed hull in \(E(Y_\kappa)\)
is isomorphic over \(X\) to \(H_\delta\). The proof uses the two-cut
equalizer twice, with a new comparison target at the second step.

## 1. The consequence of the first equalizer used below

Use the [two-cut construction, §§2–4](two_cuts_give_an_actual_m_equalizer_failure.md)
and its [membership in the least closure](two_cuts_refute_eq_c_and_escape_nonmonic_factorization.md).
Write \(L=\operatorname{Eq}(\theta,b)\in\mathcal A\). Its seed inclusion
gives \(H_\delta\subseteq L\). Let \(\mathcal F\) be the proper
\(c^+\)-complete filter on pairs \(t<s<\delta\) from that construction.
Denote by \(g_t(x,y)\) the ordinal function equal to \(x\) through \(t\)
and \(y\) thereafter, including at \(\delta\). For each \(F\in L_1\),
on an \(\mathcal F\)-large set of rows one has simultaneously

\[
 F(g_t(x,y))=F(\mathrm{const}_x)\quad\text{for all }x,y\in\omega .
 \tag{1}
\]

Indeed, intersect the good rows for descent of \(F\) with the rows on
which the full tables \(\theta_1(F)\) and \(b_1(F)\) agree. Evaluate at
the tuple \((x,x,y,y,y)\). The large set can depend on \(F\).

## 2. Extending the dual template by one countable orbit

Fix a finite-range \(r\in Y_1\). Write \(r(\xi)=b_{i(\xi)}\), with
\(b_1,\ldots,b_n\) the distinct values and \(i:S\to\{1,\ldots,n\}\).
Write \(j=i(\delta)\) and \(r_{\mathbf x}(\xi)=x_{i(\xi)}\).
Take \(Q_0=Y_0\). Form \(Q_1\) from the disjoint union of \(Y_1\) and
the act of tuples \((\mathbf x,\mathbf y,z)\in\omega^{2n+1}\), subject
to the following identifications. Write \(\bar x=(x,\ldots,x)\).

* Glue \((\mathbf x,\mathbf x,x_j)\) to the old point \(r_{\mathbf x}\).
* Identify \((\bar x,\bar y,y)\) with \((\bar x,\bar x,x)\) for all \(x,y\).

The relations are stable under simultaneous relabeling. They leave the
old carrier embedded. The first gluing is injective on its specified
tuples because \(i\) is onto. In the second relation the left tuple
is already a gluing tuple only for \(x=y\), and otherwise is attached
only to the constant old point with value \(x\). The two arrows into
\(Q_1\) are the old arrows into \(Y_1\) followed by this inclusion.

We check \(Q\in C\). Its first carrier is unchanged and finite-support.
Any character on the tuple act is one of its coordinate projections:
the tuple of distinct integers generates the act and its image must be
one of those integers. The second relation forbids each \(y_k\) and
\(z\), leaving exactly the \(x_k\). On \(Y_1\) every character is
evaluation at some \(\xi\in S\), by the bounded-cardinal calculation for
\(Y_\delta\) in the two-cut note. By the first relation, its unique
compatible projection is \(x_{i(\xi)}\). Conversely that projection
supplies a character on the quotient. Thus restriction gives a bijection
\(H(Q_1)\to H(Y_1)\), and restriction along \(p_Q\) is a bijection
because it already was for \(Y\).

## 3. A target in \(\mathcal A\) with a fixed old carrier

In the componentwise reduced power \(E(Q)^I/\mathcal F\), take the
subpresheaf \(V\) of germs whose restrictions to the old \(Y\) are
constant across rows on a large set. Constancy here is equality of entire
old tables. The actions and structural maps preserve this condition.
There is no bound on the number of different old tables across different
elements of \(V\).

For a partition of \(I\) into at most \(c\) cells, glue copies of \(Q\)
over the common \(Y\), one per positive cell (a cell is positive when
its complement is not large). At least one is positive. The union of
all the other cells is filter-small by \(c^+\)-completeness. The glued
dual belongs to \(C\): its first carrier is \(Y_0\) and a character on
its second is a character on \(Y_1\) uniquely extended to each copy by
§2. Its power embeds in \(V\) by using each copy's table on its cell.
The old parts agree, and every difference on a positive cell survives
in the germ. The images enlarge under refinement. Any two of the
partitions have a common refinement with at most \(c\) cells.

These images cover \(V\). Choose a representative with its old table
fixed on all rows, modifying the small exceptional set if necessary.
Only the entries on the countable added orbit can vary, so there are
at most \(c\) different row tables. Partition by these tables.
This gives a directed union of \(D\)-subobjects, hence \(V\in\mathcal A\).
Using the whole reduced power would not justify this step for the large
old carrier.

## 4. Two comparisons on \(L\)

Define two maps \(\alpha,\beta:L\rightrightarrows V\). In sort zero
send \(G\) to its constant row \(G\) on \(Q_0=Y_0\). In sort one both
maps assign \(F\) itself on the old \(Y_1\) in every row. On the added
tuple use \(F\) applied to the following histories:

| position \(\xi\) | history for \(\alpha\) | history for \(\beta\) |
| --- | --- | --- |
| \(\xi\le t\) | \(x_{i(\xi)}\) | \(x_{i(\xi)}\) |
| \(t<\xi<\delta\) | \(y_{i(\xi)}\) | \(y_{i(\xi)}\) |
| \(\xi=\delta\) | \(z\) | \(y_j\) |

The gluing tuple gives \(r_{\mathbf x}\) in both columns on every row.
The second relation compares \(g_t(x,y)\) with the constant \(x\)
in both columns. Thus (1) makes both tables descend to \(Q_1\) on a
large set for each \(F\). On the other rows extend the old table by any
values on the new points. These choices do not affect the germs.

The two assignments are presheaf maps. For a left action, intersect
the good sets of \(F\) and its transform and use postcomposition of the
table entries. For a right action use the same intersection and the
fact that both history formulas commute with simultaneous relabeling.
For the structural arrows all arguments are old points and both maps
use the unchanged old table. The two maps agree on the seed: they are
identical throughout sort zero, and on constant second-sort observations
both history formulas give the same constant.

Their equalizer inside \(L\) is therefore an \(\mathcal A\)-subobject
of \(E(Y)\) containing the seed. It contains \(H_\delta\). For any
\(F\in(H_\delta)_1\) intersect its good set with the large set of equality
of the two full tables. At the tuple \((\mathbf b,\mathbf b,a)\), on
every such row the first history is \(r[\delta\gets a]\) and the second
is \(r\). Properness gives (*). A separate target for each finite-range
\(r\) suffices, since each equalizer contains the same least hull.

## 5. Factorization and stabilization

For \(\kappa>\delta\) precompose each observation of \(H_\delta\) with
ordinary restriction of its argument to \([0,\delta]\).
The two actions and the first structural arrow commute with restriction.
For a continuous \(g:[0,\kappa]\to\omega\), shifting before or after
restriction yields histories that agree below \(\delta\) and may differ
at \(\delta\). Both have finite range by compactness of the interval
and discreteness of \(\omega\). Equation (*) gives precisely the second
structural square. This produces a map \(s_\kappa:H_\delta\to E(Y_\kappa)\)
over \(X\). Both restrictions on arguments are surjective (extend
constantly after \(\delta\)), so \(s_\kappa\) is monic. At \(\kappa=\delta\)
use the inclusion. For \(\kappa<\delta\) use the usual dual extension
of functions constantly after \(\kappa\), which commutes with the
endpoint-fixed successors. These are maps over \(X\) for every ordinal,
regardless of membership of the ambient target in \(\mathcal A\).

If \(E(Y_\kappa)\in\mathcal A\) and \(\kappa\ge\delta\), the image of
\(s_\kappa\) is an \(\mathcal A\)-subobject containing the seed, hence
contains its least hull \(H_\kappa\). Pulling \(H_\kappa\) back along
\(s_\kappa\) gives an \(\mathcal A\)-subobject of \(H_\delta\) containing
the seed, hence all of \(H_\delta\). Thus \(s_\kappa(H_\delta)=H_\kappa\).

This settles the [canonical endpoint question](ordinal_seed_common_factor_and_the_endpoint_condition.md).
In particular the singleton indicator of the endpoint spike exhibited
there lies in \(L_1\) and outside \((H_\delta)_1\).
The family handled here consists of the initial ordinal evaluations.
A solution set for all arrows \(X\to A\), \(A\in\mathcal A\), and
reflectivity of \(\mathcal A\) remain open in this investigation.
