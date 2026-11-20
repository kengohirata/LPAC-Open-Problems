# One colour can separate a function act with nonseparable spectrum

2026-11-18. Status: explicit ZFC construction. This records a boundary of separable-spectrum arguments, together with the later theorem that makes the example safe nevertheless. No counterexample to equalizer closure is claimed.

## 1. A one-colour observation lemma

Let X be nonempty and let S⊂ω^X be an M=End(ω)-subact under postcomposition. Suppose S has at most c binary-valued functions. There is a single function h:S→ω whose full M-orbit observations separate all points of S:

    [h(mf)=h(mg) for every m∈M] ⇒ f=g.               (1)

Choose a distinct code c_A∈2^ω for every binary function χ_A∈S. For each n choose a transformation m_n with

    m_n(0)=2n,    m_n(1)=2n+1.

Prescribe

    h(m_nχ_A)=c_A(n).

This is consistent. At fixed n the transformation is injective on {0,1}, so χ_A is recovered from m_nχ_A. At distinct indices the nonempty ranges lie in disjoint pairs {2n,2n+1}. The constant binary functions cause no exception: their translated constant values are distinct members of these disjoint pairs. Extend h arbitrarily, for example by zero, elsewhere in S.

If f≠g, choose one binary transformation m separating their values at a point where they differ. Then mf and mg are distinct binary functions in S. Their chosen codes differ at some n, so h(m_nmf)≠h(m_nmg). This proves (1). The colour h may itself be chosen binary.

## 2. A nonseparable finite-seed type quotient

Take X=[0,ω₁] with its compact ordinal topology and S=C(X)=Cont(X,ω). Every such function has finite image, so S is finite-support. A clopen subset of X is a finite union of ordinal intervals, and there are ω₁ such clopens; hence |S|=ω₁≤c.

Apply §1 to obtain h:S→ω satisfying (1). Let

    Y=(S --id,id--> S)∈C_bfs.

Use h as the only nonconstant sort-0 observation, with constant-zero observation in sort 1. The finite-observation type quotient is

    Q=(S⇉1).

Indeed (1) makes the sort-0 quotient the identity, whereas the sort-1 observation identifies all its points.

The compact evaluation lemma gives H₁(Q₀)≅[0,ω₁], while H₁(Q₁)=∅. This quotient thus fails H(p_Q)-surjectivity. Its first-sort spectrum is genuinely nonseparable: every isolated successor ordinal is an open singleton, so a dense subset must contain uncountably many points.

Thus finite seed data, even one binary observation function, do not force a separable character space. This is a density statement, not merely a claim that the character space has large cardinality. A cube 2^c, for example, can be separable and would not establish this boundary.

## 3. Why this is still a safe source

Neither sort of Y has an M-fixed point, and both have size at most c. Consequently the [packed-separator factorization theorem](packed_separators_force_monic_d_factorization_2026-11-18.md) applies: every pair E(Y)⇉Z with Z∈M has its equalizer in D_bfs.

The one-colour example therefore excludes only an attempted inference from finite seed data to separability of H(Q₀). It does not obstruct C-completion by the stronger argument, and it does not yield two distinct M-valued maps agreeing on a source that the packed-separator theorem makes rigid.

The [general both-finite-support theorem](both_finite_support_monic_local_class_is_reflective_2026-11-18.md) now handles this entire subclass, regardless of spectrum separability.
