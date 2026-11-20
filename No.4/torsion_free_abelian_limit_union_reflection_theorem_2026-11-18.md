# Problem 4：torsion-free Abelian groups の場合の肯定定理

2026-11-18。状態：PROOF_RECONSTRUCTED。全て ZFC。別 agent が有理化・有理線形空間の生成・濃度 bound の議論を監査し、問題を見出さなかった。外部査読・形式検証・新規性確認は未実施。

## 1. 結論

**定理。** A⊂Ab を full replete subcategory とし、次を仮定する。

1. A の全ての対象は torsion-free。
2. A は Ab の全ての小極限で閉じる。
3. A は countable ascending unions of subgroups で閉じる。

このとき A は Ab の reflective subcategory である。従って、torsion-free Abelian groups だけからなる部分圏では No.4 の反例を構成できない。全 directed unions より弱い、可算 ascending union 閉性だけで十分である。

証明の中心は次の補題である。

**中心補題。** A の全対象が torsion-free で、小極限で閉じ、Q∈A なら、A は reflective。この補題自体には union 閉性を要しない。

## 2. 可算 mono chain が Q を生成する

空極限の閉性から 0∈A。もし A の全対象が零群なら A={0} で、反射は X↦0 である。以下では非零 G∈A を一つ選ぶ。

G が torsion-free なので、自然射 G→Q⊗G は単射である。V=Q⊗G の中の部分群

    G_n=(1/n!)G  (n≥1)

は全て G と同型であり、G_n⊂G_(n+1)。その union は V 全体である。従って replete 性と可算 ascending union 閉性から V∈A。

これは抽象的な mono diagram

    G --×2--> G --×3--> G --×4--> ⋯

の colimit を、V 内の実際の部分群の union として表示したものである。よって「mono diagram の colimit」と「共通 ambient 内の subgroup union」の用語差には依存しない。

V は非零 Q-vector space なので Q を linear retract として持つ。小極限閉性は retract 閉性を含む（idempotent e の像は Eq(e,id)）ため、Q∈A。

## 3. 全ての Q-vector spaces と、小さい pure hulls

任意の Q-vector space W は、全ての linear functionals による単射

    W ↪ Q^(Hom_Q(W,Q))

を持つ。線形部分空間の補空間を選べばこの単射は split する。A は積・retract で閉じ、Q∈A なので、全ての Q-vector spaces が A に属する。

### 任意の射に対する濃度 bound

任意の Abelian group X と f:X→G、G∈A を取る。G を Q⊗G の部分群と同一視し、

    W=span_Q(f(X)),
    H=G∩W=ker(G→(Q⊗G)/W)

と置く。右辺の codomain は Q-vector space なので A に属する。従って kernel 閉性から H∈A。また f は H↪G を経由し、

    |H|≤max(|X|,ℵ₀)。

これは全ての f の codomain に共通する bound であり、各 X に対する solution set を与える。特に有限個の指定された G の元は、A に属する countable finite-rank pure subgroup に入る。

より一般に、G∈A の任意の pure subgroup H は A に属する。torsion-free 群の pure subgroup は

    H=G∩span_Q(H)

を満たすので、同じ kernel の表示が使える。

## 4. 反射の明示的な構成

solution set theorem を使わず、反射そのものを有理化の内部に構成できる。

X∈Ab とし、

    V_X=Q⊗X,
    X̄=im(X→V_X)≅X/t(X)

と置く。t(X) は torsion subgroup。

V_X の部分群 H で、X̄⊂H かつ H∈A を満たすもの全体を考える。この族は V_X の subgroups の部分集合なので集合であり、V_X 自身が A に属するので空でない。

    R_A(X)= ⋂ {H≤V_X : X̄⊂H and H∈A}

と定める。この intersection は A の対象 H と V_X を用いた小極限なので、R_A(X)∈A。自然な射を

    η_X:X→X̄↪R_A(X)

と書く。

### 存在

任意の f:X→G、G∈A は t(X) を消し、有理化した線形写像

    f_Q:V_X→Q⊗G

を与える。G↪Q⊗G との pullback

    P_f=V_X×_(Q⊗G)G=f_Q^(-1)(G)≤V_X

を取る。V_X,G,Q⊗G は全て A に属するので P_f∈A。また X̄⊂P_f。従って intersection の定義から R_A(X)⊂P_f であり、f_Q の制限は

    f̄:R_A(X)→G,  f̄η_X=f

を与える。

### 一意性

r∈R_A(X)⊂Q⊗X に対して、ある非零整数 n と x∈X が存在して nr=η_X(x) となる。従って a,b:R_A(X)→G が aη_X=bη_X を満たせば、

    n(a(r)−b(r))=0。

G は torsion-free なので a(r)=b(r)。よって分解は一意。

以上から η_X は X の A-reflection である。中心補題と §1 の定理が証明された。□

この構成はさらに

    X/t(X) ⊂ R_A(X) ⊂ Q⊗X,
    |R_A(X)|≤max(|X|,ℵ₀)

を与える。A={0} の場合は前述の零反射として別に扱う。

## 5. 既知の非反射的 torsion-free classes との整合性

Przeździecki, *An almost full embedding of the category of graphs into the category of abelian groups*, Adv. Math. 257 (2014), Proposition 6.8 は、¬WVP の下で Ab の非反射的 orthogonality class を構成する。その構成は torsion-free な graph images から生成される。[原論文、§6](https://arxiv.org/pdf/1104.5689)

この orthogonality class は torsion-free に取れる。実際、生成対象が torsion-free なら Z/n→0 は全生成対象に直交する。従って二重直交で得たクラスの任意の対象 G は Hom(Z/n,G)=0 を全 n>0 について満たす。

本ノートの定理は、そのような非反射的 limit-closed TF class A が **必ず可算 mono chain の union 閉性を失う**ことを示す。より具体的には、中心補題から Q∉A であり、任意の非零 G∈A に対して

    G --×2--> G --×3--> G --×4--> ⋯

の colimit Q⊗G は A に入らない。入るなら Q が retract として A に入ってしまうからである。

従って、既知の graph-to-Ab の非反射性をそのまま No.4 に持ち込むことはできない。この可算 union が既に必要条件を破る。

## 6. 混合群への境界

一般の Abelian groups を許す場合、G→Q⊗G は単射でなく、×n:G→G も mono とは限らない。従って §2 の有理化を union 閉性から導く部分は、そのまま移せない。

また G が torsion を持つ場合、§4 の一意性の証明も失敗する。このノートは Ab 全体に対する No.4 の肯定解を主張しない。混合群については、torsion subgroup の処理と、小さい hull を同じクラスの内部に構成する方法が別途必要である。
