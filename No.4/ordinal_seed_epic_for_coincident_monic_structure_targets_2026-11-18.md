# The ordinal seed is epic for coincident monic structure targets

2026-11-18. Status: PROOF_RECONSTRUCTED; no external or formal verification. This is a protected-target lemma for the new minimal-D-hull test. In particular, the tail object U that blocks V-template cogeneration cannot itself provide two distinct maps agreeing on the ordinal evaluation seed.

Let Y_kappa be the usual ordinal diagram, with A=Cont([0,kappa],omega) and B=omega^[0,kappa], p:A→B inclusion, and q(a)=a composed with d_kappa. Let

    j_0:X→E(Y_kappa)

be induced by evaluation at 0. No C-membership or N assumption is needed for the following statement.

**Theorem (ZFC).** Suppose Z∈H_fg and its two structure maps satisfy p_Z=q_Z:Z_1→Z_0, with this common map monic. If

    a,b:E(Y_kappa)→Z,
    a j_0=b j_0,

then a=b.

## Proof

Write sigma:B→B for sigma(f)=f composed with d_kappa. The undirected graph on B with edges {f,sigma(f)} whenever f≠sigma(f) has a proper coloring c:B→{0,1,2}. It is the graph of a function: every connected component is a tree or has a single cycle, so three colors suffice, with choice of colors for its components. Consequently

    c(p(a))=c(q(a))  iff  p(a)=q(a),    a∈A.

An ordinal-continuous function a with a composed with d_kappa=a is constant: successor induction and continuity at limits propagate its value at 0 to every ordinal point. Hence the last equality set is precisely the subset C⊂A of constant functions.

Take any theta:E(Y_kappa)→Z. Naturality and p_Z=q_Z give

    theta_0 E(p)=theta_0 E(q).

Applying this equality to the coloring c gives theta_0(c p)=theta_0(c q). The equality-set kernel-filter lemma for maps into H_fg therefore says that C belongs to the component kernel filter of theta_0. Thus theta_0 sends any two functions A→omega agreeing on C to the same element.

Let r:omega^A→omega^omega be restriction to the constant functions, indexed by their constant values. The sort-0 component j_(0,0):omega^omega→omega^A is precomposition with evaluation at 0, and r j_(0,0)=id. For every F:A→omega, the functions F and j_(0,0)r(F) agree on C. Hence

    theta_0=theta_0 j_(0,0) r.                         (*)

If a j_0=b j_0, equation (*) gives a_0=b_0. Naturality then yields

    p_Z a_1=a_0 E(p)=b_0 E(p)=p_Z b_1.

Since p_Z is monic, a_1=b_1, proving a=b. □

The [cogeneration counterexample U](monic_local_tail_object_not_cogenerated_by_v_templates_2026-11-18.md) has p_U=q_U=id. Thus this theorem protects U as a codomain for the specific ordinal-seed equalizer test. It does not establish all equalizer closure with codomain U.

To use the minimal-D-hull criterion to refute M-equalizer closure, one must therefore move beyond targets whose two structure arrows coincide and are monic, or use a different source/seed configuration.
