# Atomic regular power maps into chain unions factor at one stage

2026-11-18. Status: PROOF_RECONSTRUCTED. The proof was proposed by mono_equalizer and its mechanism checked by root; no external review or formal verification. Everything below is ZFC. This supplies a precise safe case for the larger injection unions, and a necessary ghost condition for any remaining non-stage scalar map.

## 1. General chain theorem

Let λ be an infinite regular cardinal, allowing λ=ω. Let

    (B_α)_(α<λ)

be an increasing chain of complete atomic Boolean algebras, with **complete Boolean embeddings** as transition maps. Put B=⋃_(α<λ)B_α. Completeness of the embeddings means that a stage's joins remain its joins at every later stage. In particular the atoms of any stage have supremum 1 also in B.

Let ψ:P(S)→B be a Boolean homomorphism. Put e_s=ψ({s}), and assume

    sup_B {e_s:s∈S}=1.                                      (1)

Zero e_s are allowed. Condition (1) says equivalently that every nonzero element of B meets at least one e_s. It is an ambient join-density assumption, stronger than the assertion that the image of ψ is an abstract complete atomic Boolean algebra.

**Theorem.** There is α<λ such that ψ(P(S))⊂B_α. At that stage there is a function from its set of atoms to S whose inverse-image Boolean homomorphism is ψ.

### Stage atoms and overlapping image atoms

For an atom t of B_α define

    I_(α,t)={s∈S:t∧e_s≠0}.

By (1), I_(α,t) is nonempty.

Suppose that for some α every I_(α,t) is a singleton, say {s(t)}. Then t≤e_(s(t)): otherwise t\e_(s(t)) is a nonzero element disjoint from every e_s, contradicting (1).

For A⊂S put

    b_A=∨_(t atom of B_α, s(t)∈A) t,

with this join taken in B_α. Each atom t of B_α lies below ψ(A) or its complement according as s(t) belongs to A or its complement. The atoms of B_α still have supremum 1 in B, so this determines ψ(A) uniquely and gives ψ(A)=b_A. Thus the theorem follows once such a stage is found.

### Cofinal extraction of distinct pairs

Suppose, for a contradiction, that every stage has an atom meeting two distinct e_s. At each stage choose such an unordered pair {s,r}.

Any fixed pair {s,r}, s≠r, can occur only boundedly often. Indeed, choose a stage containing both e_s and e_r. At that and every later stage they are disjoint elements of the stage algebra, and a stage atom cannot meet both.

We can therefore recursively choose a cofinal increasing sequence (α_β)_(β<λ), stage atoms t_β, and **distinct** pairs {s_β,r_β} such that

    t_β∧e_(s_β)≠0,       t_β∧e_(r_β)≠0.

At step β, fewer than λ previously selected pairs have bounded occurrence sets. Regularity gives a common bound for them and for the previously selected stages. Choose α_β above that bound; its pair is new. For λ=ω, only finitely many previous bounds are involved at each step.

### Cardinal graph two-coloring

A graph with λ distinct edges has a two-coloring cutting λ of its edges.

If a vertex has degree λ, color that vertex 0 and λ of its neighbors 1. Otherwise every degree is smaller than λ. Construct a matching of size λ recursively: fewer than λ already chosen vertices meet fewer than λ edges, by regularity, so an unused edge exists at each step. Color the two endpoints of every matching edge differently and extend the coloring arbitrarily.

Apply this lemma to the pairs {s_β,r_β}, and let A⊂S be one color class. There are λ, hence cofinally many, selected stages whose pair is split by A.

Choose γ with ψ(A)∈B_γ. At a split stage α_β≥γ, its atom t_β must lie wholly below ψ(A) or wholly below its complement. But it meets both an e_s with s∈A and an e_r with r∉A. This is impossible. The contradiction proves the theorem.

## 2. Why the hypotheses matter

The complete-embedding condition is used to ensure that the atoms of a stage remain join-dense in the union. Completeness of each algebra considered separately does not imply this condition for an arbitrary Boolean embedding.

The **chain** condition is also essential. For an infinite S, P(S) is the directed union of its finite Boolean subalgebras. All transitions in that diagram are complete embeddings and the identity P(S)→P(S) satisfies (1), but its image lies in no finite stage. The poset of finite subalgebras is directed, not a cofinal chain of the type used above.

Nor does injectivity of ψ imply (1). For example let S be uncountable, let I be the ideal of countable subsets, and let q:P(S)→P(S)/I be the quotient. The map

    ψ=(id,q):P(S)→P(S)×(P(S)/I)

is an injective countably complete Boolean homomorphism. Its singleton images have supremum (1,0), strictly below the unit (1,1). Its second component is a nonzero ghost invisible to every singleton image. This example distinguishes the missing hypothesis; it is not asserted to be a chain-union target of the present theorem.

## 3. Scalar consequences for injection unions

For the [large injection system](large_injection_union_generic_inverse_boolean_obstruction_2026-11-18.md), the embeddings P(T_α)→P(T_β) are precomposition along surjections, hence complete. The theorem therefore applies to its Boolean skeleton B_κ.

Let φ:ω^S→V_κ be an M_2-map, and write ψ for its induced Boolean map. Suppose the singleton images ψ({s}) have supremum 1 in B_κ. At the stage supplied by the theorem, each atom t∈T_α lies below a unique ψ({s}); define τ(t)=s.

For every f:S→ω, its unary fiber indicators have images ψ(f^−1{n}), which are exactly the fibers of fτ at this stage. The left unary fiber indicators jointly separate elements of V_κ, so

    φ(f)=[fτ].

Thus φ factors through ω^(T_α) by the explicit coordinate map τ:T_α→S. Neither N nor an Isbell full-faithfulness theorem is needed.

**Necessary ghost condition.** If φ does not factor through any stage, there exists a nonzero b∈B_κ such that

    b∧ψ({s})=0       for every s∈S.

Indeed, otherwise every nonzero element meets a singleton image, which is precisely condition (1). The theorem would then force a stage factorization.

Consequently, after restricting ψ to the nonzero interval B_κ|b, every genuinely non-stage scalar map has a Boolean component killing all singleton sets. Restriction here is A↦b∧ψ(A), with the interval's unit b. This is a necessary reduction, not a construction of such a component.

The conclusion applies to arbitrary scalar maps, including injective ones. Injectivity alone does not remove the possible ghost component, as Section 2 shows.
