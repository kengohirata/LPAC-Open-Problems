# For M_bfs targets the endpoint test reduces to one map

Let λ=(2^aleph₀)^+ and use the ordinal object Y=Y_λ. Write u_α and v_α for evaluation on its first and second carriers. Let C_∞ consist of continuous ω-valued functions on [0,λ] that are constant on [ω,λ]. Such functions are eventually constant on the initial ω with that same value. Put Y_∞=(C_∞,C_∞; id,d^*) with its usual inclusion into Y. Write r:E(Y)→E(Y_∞) for restriction. Both carriers of Y_∞ are countable. The [finite-support ordinal calculation](countable_actions_and_ordinal_bfs_coreflection_2026-11-18.md) describes this diagram.

**Proposition (ZFC).** Suppose θ:E(Y)→Z with Z∈M. It suffices that θ₀(u₀) lies in a monic cover j:E(T)↪Z with T∈C and both carriers of T finite-support. Then there exists a unique map θ_std:E(Y)→Z factoring through r and agreeing with θ at u₀. It satisfies

    (θ_std)₀(u_λ)=θ₀(u_ω).

In particular, for Z∈M_bfs a pair splitting the endpoint while agreeing at u₀ exists **if and only if** a single map θ:E(Y)→Z satisfies θ₀(u_λ)≠θ₀(u_ω). The cover condition concerns just one element. The construction does not assume θ itself factors through r.

## Constructing the comparison

Lift θ₀(u₀) along j to h₀:T₀→ω. It is equivariant: the balance equations hold for its image, and j is monic. For h∈H(T₀), let s_h∈H(T₁) be its unique extension along p_T and put D(h)=s_h q_T. Define h_(n+1)=D(h_n).

By induction j₀(h_n)=θ₀(u_n) and j₁(s_(h_n))=θ₁(v_n). The second identity at each step follows because the two balanced elements in Z have the same p_Z-image and Z has unique balanced extensions. Applying q_Z gives the first identity at n+1.

For each t∈T₀ the values h_n(t) are eventually constant. Here both the existence and the value of this limit can be checked using countable Boolean operations. The indicator of eventual constancy of a sequence f_n is

    ⋃_(l∈ω) ⋃_(k∈ω) ⋂_(n≥k) [f_n=l].

This indicator is 1 for the u_n on Y₀ by continuity at ω. Both θ₀ and j₀ preserve the indicated countable joins and meets in Z (the countable preliminary in [the Boolean continuity theorem](continuum_boolean_continuity_and_orbit_separator_factorization_2026-11-18.md)). Since their images agree term by term and j₀ is monic, the indicator is also 1 for the h_n on T₀. The same formula with l fixed shows that their eventual-value function h_ω satisfies j₀(h_ω)=θ₀(u_ω). Pointwise eventual limits preserve equivariance here, so h_ω is a character.

Both H(T₀) and H(T₁) are compact Hausdorff in the pointwise topology, because both carriers are finite-support. Thus the continuous bijection H(p_T) is a homeomorphism. In particular h↦s_h and D are continuous. Now h_n→h_ω, hence s_(h_n)→s_(h_ω) pointwise and D(h_ω)=h_ω by the convergence of the shifted sequence.

Define τ:T→Y_∞ as follows. At t∈T₀ its coordinates below ω are h_n(t), and on [ω,λ] its value is h_ω(t). At z∈T₁ use s_(h_n)(z) below ω and s_(h_ω)(z) on [ω,λ]. Both functions lie in C_∞ by their pointwise convergence into discrete ω. Both assignments are equivariant. The p-square follows from the extension equations, and the q-square follows from D(h_n)=h_(n+1) below ω and D(h_ω)=h_ω thereafter. Thus

    θ_std = j E(τ) r

is a P-map. It has the asserted values at 0 and λ.

## Uniqueness and the one-map criterion

Two maps E(Y_∞)⇉Z agreeing at evaluation at 0 agree at every finite evaluation in both sorts by the same unique-extension induction. These countably many evaluations separate C_∞, since the endpoint value is determined by the initial sequence. Each singleton is a countable intersection of their fibers and every subset of the countable carrier is a countable union of singletons. Countable Boolean continuity followed by joint separation by value indicators gives equality of the two maps on both full powers. This proves uniqueness of θ_std and its independence of the chosen cover.

For any pair a,b agreeing at u₀, the countable limit calculation on the original source yields a₀(u_ω)=b₀(u_ω). If their endpoint images differ, at least one of them therefore distinguishes u_λ from u_ω. Conversely, for any such θ with the cover stipulated above, the constructed θ_std supplies the second member of an endpoint-splitting pair. Every Z∈M_bfs supplies this cover, completing the equivalence.

The proposition does not decide whether this one map exists. For a general C-cover with non-finite-support second carrier, H(p_T) need not have continuous inverse, so the construction of τ into Y_∞ does not follow from that cover.
