# Closing the mono-factorization candidate under retracts

2026-11-18. Status: elementary closure construction and conditional
nonreflection proof. This does not prove equalizer closure or produce a
Problem 4 counterexample.

Use the actual \(\mathcal D\subseteq\mathcal M\subseteq
\mathcal H_{\mathrm{fg}}\) of
[the mono-factorization candidate](mono_factorization_candidate_2026-11-18.md).
The statements about the closure operations hold for any presheaf category
and any product-closed full replete \(\mathcal D\). Statements using the
No.1 obstruction have the same N+(NC) dependencies as that candidate.

## 1. Why one need not discard the route after a retract failure

Let \(\operatorname{Retr}(\mathcal M)\) consist of all retracts of
\(\mathcal M\)-objects. Then

\[
\mathcal M\subseteq\operatorname{Retr}(\mathcal M)
\subseteq\mathcal H_{\mathrm{fg}}.
\]

The second inclusion uses retract closure of
\(\mathcal H_{\mathrm{fg}}\). Moreover,
\(\operatorname{Retr}(\mathcal M)\) is closed under arbitrary small
products: take the product of the section/retraction pairs, and use product
closure of \(\mathcal M\). It is also retract-closed, since retracts
compose.

**Directed-union closure of this one-step class has not been established.**
For a directed family \(A_i\hookrightarrow A_j\) of retracts of
\(M_i\in\mathcal M\), there is no automatic compatible system of
monomorphisms \(M_i\hookrightarrow M_j\). The evident maps

\[
M_i\xrightarrow{r_i}A_i\hookrightarrow A_j\xrightarrow{s_j}M_j
\]

usually fail to be monic. Conversely, attempts to enlarge witnesses by
products require extending a chosen section \(A_i\to M_i\) along
\(A_i\hookrightarrow A_j\), and such extensions have not been supplied.
Neither issue is resolved by the equation \(r_i s_i=1\).

## 2. Positive result for coherently split directed unions

There is a useful intermediate closure theorem. Suppose \(I\) is a small
directed poset and \((A_i,a_{ij})_{i\leq j}\) is a diagram in
\(\operatorname{Retr}(\mathcal M)\). Suppose also that its transition
monomorphisms have chosen retractions \(t_{ij}:A_j\to A_i\) satisfying

\[
t_{ij}a_{ij}=1_{A_i},\qquad
t_{ik}=t_{ij}t_{jk}\quad(i\leq j\leq k),\qquad t_{ii}=1.
\tag{2}
\]

Then \(\operatorname*{colim}_i A_i\in
\operatorname{Retr}(\mathcal M)\).

To prove this, choose retract presentations

\[
A_i\xrightarrow{s_i}M_i\xrightarrow{r_i}A_i,
\qquad r_i s_i=1,\quad M_i\in\mathcal M.
\]

Set \(N_i=\prod_{k\leq i}M_k\), which belongs to \(\mathcal M\). Define

\[
\sigma_i:A_i\to N_i,
\quad(\sigma_i)_k=s_k t_{ki},
\qquad
\rho_i:N_i\to A_i,
\quad\rho_i=r_i\operatorname{pr}_i.
\]

Then \(\rho_i\sigma_i=1\). For \(i\leq j\), define
\(u_{ij}:N_i\to N_j\) coordinatewise by

\[
\operatorname{pr}_k u_{ij}=
\begin{cases}
\operatorname{pr}_k,& k\leq i,\\
s_k t_{kj}a_{ij}\rho_i,& k\leq j\text{ and }k\not\leq i.
\end{cases}
\tag{3}
\]

The maps \(u_{ij}\) are split monomorphisms, with retractions given by
restriction to the coordinates \(k\leq i\). Equations (2) imply

\[
u_{jk}u_{ij}=u_{ik},\qquad
u_{ij}\sigma_i=\sigma_j a_{ij},\qquad
\rho_j u_{ij}=a_{ij}\rho_i.
\]

For example, a coordinate first added between \(i\) and \(j\) is
unchanged at later stages; its value in the direct map to a later stage
agrees because \(t_{k\ell}a_{j\ell}=t_{kj}\) for \(k\leq j\leq\ell\).
A coordinate first added after \(j\) agrees by the last displayed
compatibility of \(\rho_j\) with \(u_{ij}\). These two cases, together
with the old coordinates, check composition in (3).

Taking directed colimits therefore exhibits
\(\operatorname*{colim}_i A_i\) as a retract of
\(\operatorname*{colim}_i N_i\). The latter lies in \(\mathcal M\),
because the \(u_{ij}\) are monic and \(\mathcal M\) is closed under
directed unions. This proves the theorem.

In particular, \(\operatorname{Retr}(\mathcal M)\) is closed under
colimits of **countable chains of split monomorphisms**: choose retractions
for successive maps and compose them to get (2). The same applies to a
countable directed poset of split monomorphisms after passing to a cofinal
increasing sequence.

This theorem does not assert that arbitrary split directed systems admit
coherent choices (2), or that arbitrary monomorphisms split. Thus ordinary
directed-union closure remains open here.

## 3. A closure construction that does preserve all three operations

Let \(\mathcal A\) be the least full replete class containing
\(\mathcal M\) and closed under:

1. all small products;
2. retracts;
3. directed colimits of monomorphisms, computed in the ambient presheaf
   category.

One precise definition uses set-sized well-founded construction trees.
Leaves are labelled by \(\mathcal M\)-objects. An internal node is
labelled by the result of one of these operations on its children, together
with the witnessing diagram. An object belongs to \(\mathcal A\) when it
occurs at the root of such a tree, up to isomorphism. This is a definable
class: each construction tree and all its labels are sets. A small family
of such trees can be joined under one new root, so the class has all three
required closure properties. Equivalently, one can iterate the three
operations through the ordinals and take their union.

Because \(\mathcal H_{\mathrm{fg}}\) is closed under products, retracts,
and directed unions, induction on construction trees gives

\[
\mathcal D\subseteq\mathcal M\subseteq\mathcal A
\subseteq\mathcal H_{\mathrm{fg}}.
\tag{1}
\]

This proof does not identify \(\mathcal A\) with
\(\operatorname{Retr}(\mathcal M)\), nor does it identify it with
\(\mathcal H_{\mathrm{fg}}\).

## 4. The actual nonreflection obstruction survives

In the No.4 setting, \(X=E(B)\) is ambient finitely generated. Under
N+(NC), \(X\downarrow\mathcal D\) has no weakly initial set.

Suppose \(\{f_j:X\to A_j\}_{j\in J}\) were a weakly initial set in
\(X\downarrow\mathcal A\). By (1), each \(A_j\) lies in
\(\mathcal H_{\mathrm{fg}}\), so choose factorizations

\[
X\xrightarrow{g_j}D_j\xrightarrow{h_j}A_j,
\qquad D_j\in\mathcal D.
\]

For every map \(X\to D\) with \(D\in\mathcal D\subseteq\mathcal A\),
weak initiality supplies a factorization through some \(f_j\), and hence
through \(g_j\). This would make \(\{g_j\}_{j\in J}\) weakly initial in
\(X\downarrow\mathcal D\), a contradiction. Thus

\[
X\downarrow\mathcal A\text{ has no weakly initial set, and }
\mathcal A\text{ is not reflective}.
\]

Under N, the ambient finitely generated objects in \(\mathcal A\) are
exactly the finitely generated objects in \(\mathcal D\). Indeed,
\(\mathcal D\subseteq\mathcal A\), while a finitely generated member
of \(\mathcal H_{\mathrm{fg}}\) is a retract of a \(\mathcal D\)-object;
the actual \(\mathcal D\) is retract-closed under N.

## 5. What is still missing

To obtain a Problem 4 counterexample from \(\mathcal A\), one must still
prove that it is closed under equalizers. Products, directed unions, and
retracts are already built into its definition, and the conditional
nonreflection has been proved above.

This equalizer problem can be harder than the corresponding problem for
\(\mathcal M\), because the codomains now include new retracts and
subsequent closure stages. In particular, one must not transfer the special
equalizer theorems proved for maps between \(\mathcal M\)-objects to all
\(\mathcal A\)-objects without a new argument.

The old sufficiently-filtered-colimit obstruction does not automatically
apply to \(\mathcal A\): the defining operations do not include arbitrary
filtered colimits. Conversely, nothing here proves failure of such closure.
If one were to prove \(\mathcal A=\mathcal H_{\mathrm{fg}}\), the old
conditional obstruction would reject \(\mathcal A\) as a counterexample.

Thus an actual retract counterexample for \(\mathcal M\), if found, would
reject that particular class but would not by itself reject this larger
product/retract/union closure. No actual Isbell retract counterexample and
no general equalizer closure theorem are established in this note.
