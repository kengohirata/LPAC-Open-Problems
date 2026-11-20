# A generic retract counterexample for the monic finite-local construction

Date: 2026-11-18. Status: explicit ZFC construction with a self-contained proof;
independent agent checks found no gap. External review and formal verification
have not been performed.

## 1. What this establishes

For a presheaf category \(\mathcal P\) and a full replete limit-closed
subcategory \(\mathcal D\), put

\[
\mathcal M(\mathcal D)=\{Z\in\mathcal P:\text{ every map }F\to Z
\text{ with }F\text{ ambient finitely generated factors as }
F\to D\lhook\joinrel\longrightarrow Z,\quad D\in\mathcal D\}.
\]

There exist such \(\mathcal P,\mathcal D\) and a split idempotent
\(e:V\to V\) for which

\[
V\in\mathcal M(\mathcal D),\qquad
\operatorname{Eq}(e,1_V)\notin\mathcal M(\mathcal D).
\]

In particular, the monic finite-local construction is **not automatically
retract-closed**, even when its defining \(\mathcal D\) is closed under all
small limits. In this example \(V\) is already a countable increasing union
of \(\mathcal D\)-subobjects.

This is a diagnostic example for the new No.4 construction. Its
\(\mathcal D\) is different from the specific Isbell image
\(E(\mathcal C^{op})\) in the No.4 candidate. It does **not** disprove
retract closure for that particular candidate, and does not solve Problem 4.
Neither the no-measurable-cardinal assumption (N) nor the adopted No.1 input
(NC) is used here.

## 2. A limit-closed class of abelian groups

For an abelian group \(A\), define

\[
\delta_A:A^{\mathbb N}\longrightarrow A^{\mathbb N},\qquad
\delta_A((x_n)_{n\geq0})=(x_n-2x_{n+1})_{n\geq0}.
\]

Let \(\mathcal D_{\mathrm{Ab}}\) be the full replete subcategory consisting
of groups for which \(\delta_A\) is bijective. Thus every sequence
\((a_n)\) must admit a unique solution of

\[
x_n-2x_{n+1}=a_n\qquad(n\geq0).
\tag{1}
\]

This class is closed under all small limits in \(\mathrm{Ab}\). Indeed, put
\(L=\bigoplus_{n\geq0}\mathbb Z e_n\), and let

\[
s:L\longrightarrow L,\qquad s(e_n)=e_n-2e_{n+1}.
\]

Then \(\delta_A\) is precisely
\(\mathrm{Ab}(s,A):\mathrm{Ab}(L,A)\to\mathrm{Ab}(L,A)\).
Consequently \(\mathcal D_{\mathrm{Ab}}=\{s\}^{\perp}\).
Representable functors preserve limits, and a limit of a diagram of
bijections is a bijection. This proves the asserted limit closure directly.

The condition is the usual recurrence description of a
\(2\)-contramodule abelian group. For the terminology and its broader
context, see Leonid Positselski,
[Contraadjusted modules, contramodules, and reduced cotorsion modules](https://arxiv.org/abs/1605.03934)
and his [recurrence description in Semi-Infinite Algebraic Geometry](https://users.math.cas.cz/~positselski/semi-inf-nopause.pdf), slide 41.
The argument below uses only the explicit definition above.

### Lemma 2.1. \(\mathbb Z_2\in\mathcal D_{\mathrm{Ab}}\)

Here \(\mathbb Z_2\) denotes the ring of \(2\)-adic integers, regarded as
an abelian group. Given \((a_n)\in\mathbb Z_2^{\mathbb N}\), set

\[
x_n=\sum_{k\geq0}2^k a_{n+k}.
\]

The series converges in \(\mathbb Z_2\) and satisfies (1). If
\((y_n)\) is a solution of the homogeneous recurrence, then
\(y_n=2^k y_{n+k}\) for every \(k\), so

\[
y_n\in\bigcap_{k\geq0}2^k\mathbb Z_2=0.
\]

The solution is therefore unique.

### Lemma 2.2. No nonzero subgroup of \(\mathbb Q\) belongs to \(\mathcal D_{\mathrm{Ab}}\)

Suppose \(0\ne H\leq\mathbb Q\). Rescaling by a nonzero element of
\(H\) replaces \(H\) by an isomorphic subgroup containing \(1\), so assume
\(1\in H\). There are two cases.

**Unbounded powers of \(2\) in denominators.** Suppose the \(2\)-adic
valuations of nonzero elements of \(H\) are unbounded below. For any
\(n\), choose

\[
\frac{a}{2^k b}\in H,\qquad a,b\text{ odd},\quad k\geq n.
\]

Multiplication by \(b\) shows \(a/2^k\in H\). As
\(\gcd(a,2^k)=1\), integers \(u,v\) satisfy \(ua+v2^k=1\), whence

\[
u\frac{a}{2^k}+v=\frac1{2^k}\in H.
\]

It follows that \(2^{-n}\in H\) for every \(n\). Thus
\((x_n)=(2^{-n})\) is a nonzero element of \(\ker\delta_H\), so
\(H\notin\mathcal D_{\mathrm{Ab}}\).

**Bounded powers of \(2\) in denominators.** Otherwise, there is
\(N\geq0\) such that

\[
v_2(h)\geq-N\quad\text{for all }0\ne h\in H.
\]

Choose \(\alpha\in\mathbb Z_2\setminus\mathbb Q\), and write its binary
expansion

\[
\alpha=\sum_{n\geq0}2^n a_n,\qquad a_n\in\{0,1\}\subseteq H.
\]

If \(\delta_H\) were surjective, a solution of (1) in \(H\) would give
for every \(m\)

\[
x_0=\sum_{n=0}^{m}2^n a_n+2^{m+1}x_{m+1}.
\]

The final term has valuation at least \(m+1-N\), and therefore tends to
zero in \(\mathbb Q_2\). Taking the \(2\)-adic limit yields
\(x_0=\alpha\), impossible because \(x_0\in H\subseteq\mathbb Q\).
Hence \(\delta_H\) is not surjective in this case.

Both cases rule out \(H\in\mathcal D_{\mathrm{Ab}}\).

## 3. A local union with a bad retract

The additive group of the \(2\)-adic field satisfies

\[
\mathbb Q_2=\bigcup_{n\geq0}2^{-n}\mathbb Z_2.
\tag{2}
\]

Each subgroup \(2^{-n}\mathbb Z_2\) is isomorphic to \(\mathbb Z_2\),
and thus belongs to \(\mathcal D_{\mathrm{Ab}}\). Every finite subset of
\(\mathbb Q_2\) lies in one such subgroup.

Since \(\mathbb Q_2\) is a vector space over \(\mathbb Q\), the standard
inclusion \(j:\mathbb Q\hookrightarrow\mathbb Q_2\) has a
\(\mathbb Q\)-linear retraction \(r:\mathbb Q_2\to\mathbb Q\): extend
\(1\) to a vector-space basis and project onto its coordinate. This uses
the usual axiom of choice in ZFC. Let \(e=jr\). Then

\[
e^2=e,\qquad\operatorname{Eq}(e,1_{\mathbb Q_2})=j(\mathbb Q).
\tag{3}
\]

These are morphisms of abstract abelian groups; no continuity condition is
imposed. Lemma 2.2 shows that the retract \(\mathbb Q\) contains no
nonzero \(\mathcal D_{\mathrm{Ab}}\)-subgroup at all.

## 4. Transfer to an actual presheaf category

Let \(\mathcal A\) be the small category whose objects are
\(\mathbb Z^n\), \(n\geq0\), and whose morphisms are all homomorphisms
between them. Both its object set and its total morphism set are countable.
Put

\[
\mathcal P=[\mathcal A^{op},\mathrm{Set}],\qquad
E(A)=\mathrm{Ab}(-,A)|_{\mathcal A}.
\]

The functor \(E:\mathrm{Ab}\to\mathcal P\) has the following properties.

1. It is fully faithful. A natural transformation is determined by its
   component at \(\mathbb Z\). Naturality with the coordinate maps and
   the homomorphism \(\mathbb Z\to\mathbb Z^2\), \(1\mapsto(1,1)\),
   forces that component to preserve addition; naturality with
   \(\mathbb Z\to0\) forces it to preserve zero. Conversely, every group
   homomorphism induces such a natural transformation.
2. It preserves all small limits, since each component is a representable
   functor on \(\mathrm{Ab}\).
3. It preserves filtered colimits, since every \(\mathbb Z^n\) is finitely
   presented in \(\mathrm{Ab}\).
4. It preserves and reflects monomorphisms. Preservation follows
   componentwise; reflection is already detected by evaluation at
   \(\mathbb Z\), which is the underlying-set functor.

Let \(\mathcal D\) be the replete image of
\(\mathcal D_{\mathrm{Ab}}\) under \(E\). Full faithfulness and limit
preservation, together with Section 2, show that \(\mathcal D\) is a full
replete subcategory closed under all small limits in \(\mathcal P\).

By (2) and filtered-colimit preservation,

\[
V:=E(\mathbb Q_2)
 =\operatorname*{colim}_{n<\omega}E(2^{-n}\mathbb Z_2)
\]

is an increasing union of \(\mathcal D\)-subobjects. Thus
\(V\in\mathcal M(\mathcal D)\): any map from an ambient finitely
generated presheaf into this directed union factors through a stage, by
the defining property of finite generation.

On the other hand, \(W:=E(\mathbb Q)\notin\mathcal M(\mathcal D)\).
Indeed, the representable presheaf

\[
y(\mathbb Z)=\mathcal A(-,\mathbb Z)=E(\mathbb Z)
\]

is finitely presentable, hence finitely generated. Consider its map
\(f:y(\mathbb Z)\to E(\mathbb Q)\) induced by \(\mathbb Z\hookrightarrow
\mathbb Q\). A hypothetical factorization

\[
y(\mathbb Z)\longrightarrow D\lhook\joinrel\longrightarrow E(\mathbb Q),
\qquad D\in\mathcal D,
\]

would, after replacing \(D\) by an isomorphic \(E(A)\), give a group
monomorphism \(A\hookrightarrow\mathbb Q\) with
\(A\in\mathcal D_{\mathrm{Ab}}\). The factorization of \(f\) ensures
that its image contains \(1\). Its image would therefore be a nonzero
\(\mathcal D_{\mathrm{Ab}}\)-subgroup of \(\mathbb Q\), contradicting
Lemma 2.2.

Finally, applying \(E\) to (3) gives

\[
W\cong\operatorname{Eq}(E(e),1_V),\qquad
V\in\mathcal M(\mathcal D),\quad W\notin\mathcal M(\mathcal D).
\]

This is the promised presheaf counterexample to both retract closure and
equalizer closure of the generic monic finite-local construction.

## 5. Strictness and failure of every sufficiently filtered closure

For this generic \(\mathcal D\), let \(\mathcal H_{\mathrm{fg}}(\mathcal D)\)
be the corresponding class obtained by dropping the monomorphism requirement
from the final map \(D\to Z\). Then

\[
\mathcal M(\mathcal D)\subsetneq\mathcal H_{\mathrm{fg}}(\mathcal D).
\]

Indeed, the inclusion is immediate from the definitions, and the witness to
strictness is \(W=E(\mathbb Q)\). The class
\(\mathcal H_{\mathrm{fg}}(\mathcal D)\) is always retract-closed: compose
a map \(F\to W\) with a section \(W\to V\), factor through a
\(\mathcal D\)-object using \(V\in\mathcal H_{\mathrm{fg}}(\mathcal D)\),
then compose the final map with the retraction \(V\to W\). Thus
\(V\in\mathcal M(\mathcal D)\) and the retraction above imply
\(W\in\mathcal H_{\mathrm{fg}}(\mathcal D)\), whereas Section 4 proves
\(W\notin\mathcal M(\mathcal D)\).

Furthermore, for **every infinite regular cardinal** \(\mu\),
\(\mathcal M(\mathcal D)\) fails closure under \(\mu\)-filtered colimits.
Choose an infinite regular cardinal \(\lambda\geq\mu\), regarded as its
ordinal poset. It is a \(\mu\)-filtered category. Form the diagram with
object \(V\) at every \(\alpha<\lambda\), identity maps on identity
arrows, and transition map \(E(e):V\to V\) for every strict inequality
\(\alpha<\beta\). The equation \(E(e)^2=E(e)\) makes this a functor.

Its colimit in \(\mathcal P\) is \(W\), with cocone map \(E(r):V\to W\)
at every stage. To verify the universal property, any cocone
\((f_\alpha:V\to T)\) satisfies

\[
f_\alpha=f_\beta E(e)\qquad(\alpha<\beta).
\]

For \(\alpha<\beta<\gamma\), idempotence gives
\(f_\alpha=f_\gamma E(e)^2=f_\gamma E(e)=f_\beta\). As \(\lambda\) has
no greatest element, all cocone maps are equal to a common \(f\), with
\(fE(e)=f\). There is a unique factorization

\[
f=(fE(j))E(r)
\]

through \(W\), because \(E(r)E(j)=1_W\). This proves the claimed
colimit description. All diagram objects lie in \(\mathcal M(\mathcal D)\)
and their colimit does not.

Thus the monomorphism requirement can genuinely prevent the automatic
sufficiently-filtered-colimit closure of the old construction. In this
generic example it also destroys retract and equalizer closure. These
statements do not settle any of those properties for the actual Isbell
candidate.

## 6. Consequence for the current No.4 search

A proposed proof that \(\mathcal M(E(\mathcal C^{op}))\) is retract-closed
must use a special feature of the actual Isbell image. Limit closure of
\(\mathcal D\), local coverage by \(\mathcal D\)-subobjects, and the
idempotence equation alone are insufficient.

The mechanism is concrete: a retraction can send one large good subobject
onto a small bad subgroup, while its finitely many selected elements still
lie in large good subobjects of the ambient object. Taking the finite
idempotent orbit of the selected elements does not produce an invariant
good subobject.

More specifically, \(e\) cannot send the stage \(\mathbb Z_2\) into any
later stage \(2^{-N}\mathbb Z_2\). If it did, \(r(\mathbb Z_2)\subseteq
\mathbb Q\) would have valuations bounded below by \(-N\). For
\(\alpha\in\mathbb Z_2\setminus\mathbb Q\), its binary partial sums
give

\[
\alpha=\sum_{i=0}^{m-1}2^i a_i+2^m y_m,\qquad y_m\in\mathbb Z_2.
\]

Since \(r\) fixes all rational numbers, applying \(r\) gives

\[
r(\alpha)=\sum_{i=0}^{m-1}2^i a_i+2^m r(y_m).
\]

The bounded-valuation assumption would make the remainder tend to zero,
forcing \(r(\alpha)=\alpha\), a contradiction. Thus the endomorphism
fails stage factorization even on its first good stage.

In the actual candidate, the already proved equalizer results with
codomain \(V\) and with the countable-carrier variants \(V^R\) remain
unaffected; see
[the separate compression and equalizer note](mono_local_compression_and_v_equalizers_2026-11-18.md).
The present example supplies a failure pattern to search for beyond those
protected cases, rather than a counterexample inside them.
