# An explicit antichain element in the c^+-tail quotient of Y_omega

2026-11-18. Status: PROOF_RECONSTRUCTED; independently checked by a second research agent, not externally reviewed or formally verified. This gives an explicit ZFC object W in H_fg but outside the actual mono-factorization class. In particular, the actual mono-factorization class fails closure under c^+-filtered colimits. This does not decide its equalizer closure or solve Problem 4.

Write c=2^aleph_0, lambda=c^+, and M=End(omega). In this note M denotes the monoid; the mono-factorization class is written as mathcal M in prose when needed.

## 1. The actual ordinal template and its tail quotient

Use the No.1 ordinal template at omega:

    R_0=Cont([0,omega],omega_discrete),
    R_1=omega^[0,omega],
    p:R_0→R_1 the inclusion,
    q(f)=f composed with d,

where d(n)=n+1 for n<omega and d(omega)=omega. Both actions are postcomposition by M. Then R_0 is countable and finite-support, while R_1 has cardinality c and contains elements with infinite support.

The fact R∈C holds in ZFC. The equivariant maps R_0→omega are exactly the evaluations at points of [0,omega]: this is the finite/cofinite Stone-space instance of the No.1 evaluation argument. The same holds for R_1 because its coordinate index set is countable. Restriction along p is therefore bijective. Choose a bijection [0,omega]≅omega and identify R_1 with the left regular M-set M. Under this identification every element in p(R_0) and q(R_0) is a finite-image map omega→omega.

For beta<lambda put T_beta=[beta,lambda), and form

    Z_beta=E(T_beta·R)∈D,
    W=colim_(beta<lambda) Z_beta,

with transition maps induced by inclusions of tails. Componentwise W consists of germs of functions on T_beta×R_i, where equality means equality on some later tail.

Since lambda=c^+ and every ambient finitely generated presheaf is lambda-presentable, the existing sufficiently-filtered-colimit lemma gives W∈H_fg. No N or No.1 non-coreflectivity input is needed for this membership statement.

## 2. A right-translation antichain of row functions

Let Sym(omega)⊂M be the permutations. There are 2^c nonempty subsets of Sym(omega), and each orbit under right translation by Sym(omega) has size at most c. Choose lambda nonempty subsets

    A_alpha⊂Sym(omega),    alpha<lambda,

from distinct right-translation orbits. Define x_alpha:M→{0,1} by x_alpha=chi_(A_alpha), extending by zero outside the permutations.

**Antichain lemma.** If

    x_alpha(m)=x_gamma(m a) for every m∈M

for some a∈M, then alpha=gamma and a is a permutation.

Proof. If a is not injective, every m a is noninjective, so the right-hand side is identically zero, while x_alpha is not. If a is injective but not surjective, choose pi∈A_gamma. Define m on im(a) by m(a(n))=pi(n), and define it arbitrarily on the nonempty complement. The restriction to im(a) already maps onto omega, so m is noninjective. Thus x_alpha(m)=0, whereas x_gamma(m a)=x_gamma(pi)=1, again impossible. Finally, if a is a permutation, the displayed identity says A_alpha=A_gamma a^(-1), forcing alpha=gamma by the choice of orbit representatives. □

Let x∈W_1 be the germ represented by

    x(t,r)=x_t(r),    t<lambda, r∈R_1=M.

This germ is nonzero, since every row x_t is nonzero. Here zero means the germ of the constant-zero function.

## 3. No monic full-power image can contain x

**Theorem (ZFC).** For every K-object Y, there is no monomorphism j:E(Y)↪W whose sort-1 image contains x. No stage-lifting assumption is made.

### Proof

Suppose j_1(h)=x for some h:Y_1→omega. The maps E(Y)→W preserve every finitary pointwise omega operation: encode any finite tuple using a bijection omega^n≅omega, use the inherited unique tuple coding in W∈H_fg, and then apply a unary selfmap of omega. This is the finite-operation argument used in the kernel-filter lemma.

Let b:omega→omega fix 0,1 and send all other values to 0. Since b(x)=x and j is monic, b(h)=h. Thus h is {0,1}-valued. Since x≠0 and j preserves constant zero, h≠0. Choose y∈Y_1 with h(y)=1, and put

    v=j_1(chi_{y})∈W_1.

Then v≠0 by monicity and v is {0,1}-valued in the sense that b(v)=v. Choose a binary representative v(t,r)∈{0,1} on some tail, by applying b to any representative. Write

    B_t={r∈M:v(t,r)=1}.

Nonzero v means that B_t is nonempty for unboundedly many t<lambda.

For every m∈M we have the pointwise inequality in E(Y)_1

    chi_{y} <= [h·m = h(m y)],

where brackets denote the {0,1}-valued equality test and the right M-action is precomposition: (h·m)(z)=h(m z). This inequality is an equation between finitary pointwise operations. More explicitly, for a∈omega use the binary operation k_a(b,z), equal to b when z=a and equal to 0 otherwise; then

    k_(h(m y))(chi_{y},h·m)=chi_{y}.

Applying j and using naturality gives

    v <= [x·m = h(m y)]                        (m∈M).       (*)

There are c many equations (*). Each germ equality holds pointwise on some tail. Since lambda=c^+ is regular, choose one beta<lambda beyond all these exceptional initial segments, as well as beyond the starting tail for v. Thus, for every t>=beta, r∈B_t, and m∈M,

    x_t(m r)=h(m y).                                      (**)

Taking m=id gives x_t(r)=h(y)=1. Hence every r∈B_t lies in A_t and is therefore a permutation.

Choose distinct s,t>=beta with B_s and B_t nonempty, and choose r_s∈B_s and r_t∈B_t. Equation (**) says

    x_t(m r_t)=h(m y)=x_s(m r_s)    for every m∈M.

Substituting m=n r_t^(-1) gives

    x_t(n)=x_s(n r_t^(-1)r_s)     for every n∈M.

This contradicts the right-translation antichain lemma, since s≠t. Therefore no such monomorphism j exists. □

The singleton indicator chi_{y} is the decisive tool. Its nonzero image supplies actual nonempty rows, and only c equations are needed to recover all observations of the orbit M y on those rows. Consequently all relevant equations stabilize on one tail even when the whole map E(Y)→W does not lift to a stage.

## 4. An explicit strict inclusion and filtered-colimit failure

Let F⊂W be the ambient subpresheaf generated by x. It is finitely generated. If W belonged to the mono-factorization class mathcal M, the inclusion F→W would factor through a monomorphism E(Y)↪W with Y∈C. Its image would contain x, contradicting Section 3.

We have proved

    W∈H_fg and W∉mathcal M.

Thus mathcal M is strictly smaller than H_fg for the actual Isbell construction, in ZFC. Moreover, W is the colimit of the lambda-filtered tail diagram (Z_beta)_(beta<lambda), and every Z_beta lies in D⊆mathcal M. Therefore mathcal M is not closed under all c^+-filtered colimits.

No use is made of N, the No.1 non-coreflectivity input, or the comparison between c^+ and 2^c beyond the ZFC inequality c^+<=2^c, which supplies enough row orbits.

This is not a counterexample to equalizer or retract closure of mathcal M. Its failure of sufficiently filtered colimit closure at this cardinal is compatible with its intended role as a Problem 4 counterexample candidate. It removes the earlier proposed fatal shortcut mathcal M=H_fg, rather than rejecting mathcal M.

## 5. A useful simpler diagnostic and the cardinal boundary

The chosen element also satisfies

    x·e_n=0 for all n>=1,    while x≠0,

where e_n fixes 0,...,n-1 and sends all larger integers to 0. Indeed e_n r always has finite image and so never lies in A_t⊂Sym(omega).

This alone excludes every monic E(Y)↪W containing x when Y_1 is finite-support. If h maps to x, monicity gives h·e_n=0 for every n; every y∈Y_1 is fixed by some e_n, so h(y)=0, a contradiction. The antichain argument of Section 3 additionally excludes all non-finite-support Y_1.

The earlier bounded-template tail theorem guarantees membership in mathcal M for regular tails strictly larger than 2^c when R=Y_omega. There is no contradiction: at those cardinals there are fewer possible rows than the tail regularity, and the recurrent-pattern monic witness exists. The present construction uses c^+ many distinct row orbits; its pointwise equations synchronize because |M|=c, while the row-pattern stabilization bound is not met.

This one example proves failure at c^+. It does not prove failure at every sufficiently large regular cardinal, nor does it prove that some larger uniform filtered-colimit closure cardinal exists for mathcal M.

More generally, exactly the same proof works for every regular lambda with

    c < lambda <= 2^c.

There are enough right-translation orbits for the row family, and the c many equations in the singleton-indicator proof still stabilize on one tail. Hence mathcal M fails closure under mu-filtered colimits for every regular infinite mu<=2^c: choose lambda=max(c^+,mu), and the displayed lambda-filtered counterexample diagram is also mu-filtered. Any possible uniform filtered-colimit closure cardinal for mathcal M must therefore be strictly larger than 2^c. No failure above that threshold is established here.

## Local dependencies

- [Kernel-filter reduction](mono_factorization_kernel_filters_2026-11-18.md).
- [Bounded-template tail theorem](mono_candidate_tail_quotients_2026-11-18.md).
- [Both-finite-support epi compression](both_finite_support_accessibility_and_epi_compression_2026-11-18.md).
- [Sufficiently-filtered-colimit closure of H_fg](eqc_obstruction_sufficiently_filtered_colimits_2026-11-17.md).
