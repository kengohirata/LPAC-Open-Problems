# Problem 4：全ての coslice X/Ab での肯定定理

2026-11-18。状態：PROOF_RECONSTRUCTED。全て ZFC。
root が proof を提案し、mono_equalizer が独立に全段階を再構成した。外部査読・形式検証・新規性確認は未実施。

## 1. 主定理

X を任意の abelian group とする。A⊂X/Ab を full replete subcategory とし、次を仮定する。

1. X/Ab の全ての小極限で閉じる。
2. X/Ab の countable ascending unions of subgroups で閉じる。

**定理。** A は X/Ab で reflective である。
さらに、対象 (Y,y:X→Y) と μ=max(|Y|,ℵ₀) に対し、任意の射

    f:(Y,y)→(G,u),   (G,u)∈A

は、ある A-subobject (K,u_K)↪(G,u) を経由し、

    |K|≤μ^ℵ₀。

反射 R_A(Y,y) 自身も underlying group の濃度≤μ^ℵ₀ と取れる。

特に X=Z は distinguished element を持つ abelian groups の圏である。従って「巨大な E-rings の additive group を 1 で point する」という経路だけでは、No.4 の反例は得られない。

これは general locally presentable categories に関する No.4 の解決ではない。

## 2. Ab 定理の strengthened form

使用するのは
[Ab の limit/countable-union reflection theorem](abelian_groups_limit_countable_union_reflection_theorem_2026-11-18.md)
の proof に含まれている次の強化である。

**補題 1（kernel form）。** B⊂Ab が full replete で、全小極限と countable ascending unions で閉じるとする。
G∈B、S⊂G、μ=max(|S|,ℵ₀) とする。
このとき P∈B と準同型 θ:G→P が存在し、

    S⊂ker θ,
    |ker θ|≤μ^ℵ₀。

より強く、ある mono j:G↪P と、濃度≤μ^ℵ₀ の **retract subgroup** P₀≤P が存在し、j(S)⊂P₀ である。

### Ab proof から retract を得る箇所

元の proof が構成する embedding は二種類である。

- Q∉B の場合：j:G↪∏_p T_p(G)。各 T_p(G) は B に属する bounded primary group。
- Q∈B の場合：j:G↪E×∏_(p∈B₀)T_p(G)。E は B に属する divisible group、B₀ は B 全体で p-torsion の exponent が bounded な primes の集合。

いずれも右辺を P と書く。元の proof で行った次の選択は、実は small subgroup より強く small retract を与える。

各 bounded factor T_p(G) を finite cyclic groups の直和に分解する。j(S) の当該座標を含むように高々 μ 個の summands を選ぶと、濃度≤μ の direct summand H_p≤T_p(G) が得られる。

divisible factor E がある場合は、j(S) の E-coordinate を含む濃度≤μ の divisible subgroup E₀≤E を取る。これは、生成した部分群に各整数の roots を countably many stages で追加して構成できる。
元の proof により E₀ の divisible summands の種類は B に存在するものに限られ、従って E₀∈B である。
さらに E₀ は divisible、従って Ab の injective object なので、包含 E₀↪E が split する。

ここで injectivity を使っているのは **domain E₀** である。E が injective であることから任意の subgroup が split すると推論しているのではない。

以上により

    P₀=∏_p H_p

または

    P₀=E₀×∏_(p∈B₀)H_p

は P の retract subgroup である。prime は可算個しかないので、|P₀|≤μ^ℵ₀。
各 factor の retraction を積にして r:P→P₀ を取り、包含を i:P₀→P とする。e=ir と置けば e²=e、image(e)=P₀。

    θ=(id_P−e)j:G→P

と定義する。このとき

    ker θ=j⁻¹(P₀)。

j が mono なので、この kernel は P₀ に埋め込まれ、濃度≤μ^ℵ₀。
j(S)⊂P₀ より S⊂ker θ。これで補題 1 が示された。

Ab proof の classical inputs は bounded pure subgroup の splitting、bounded groups の cyclic decomposition、divisible groups の injectivity と分類、essential injective envelope の存在である。正確な一次文献へのリンクと、それらの使い方は元の Ab note §2 に記してある。

## 3. 各 (G,u) に付随する Ab の full class

(G,u:X→G)∈A を固定する。次の full replete subcategory を定義する。

    B_(G,u)={K∈Ab : (G⊕K,(u,0):X→G⊕K)∈A}。

この B_(G,u) は補題 1 の仮定を満たす。

### 小極限

まず 0∈B_(G,u) は (G,u)∈A から従う。

K_a∈B_(G,u) の任意の集合添字族について、A 内に pointed projections

    (G⊕K_a,(u,0))→(G,u)

がある。それらの fiber product over (G,u) は

    (G⊕∏_a K_a,(u,0))。

従って B_(G,u) は任意積で閉じる。空の場合は (G,u) 自身である。

f,g:K⇉L が B_(G,u) の二射なら、id_G⊕f と id_G⊕g は A 内の pointed maps であり、その equalizer は

    (G⊕Eq(f,g),(u,0))。

従って B_(G,u) は equalizers で閉じ、任意小極限で閉じる。

### Countable ascending unions

K₀≤K₁≤⋯ が B_(G,u) の chain なら、

    (G⊕K₀,(u,0))↪(G⊕K₁,(u,0))↪⋯

は A の mono chain である。その union は

    (G⊕⋃_n K_n,(u,0))。

従って B_(G,u) も countable ascending unions で閉じる。

### G 自身が B_(G,u) に属する

A は積で閉じるので (G⊕G,(u,u))∈A。
shear isomorphism

    G⊕G→G⊕G,   (g,h)↦(g,h−g)

は pointing (u,u) を (u,0) に送る。従って

    (G⊕G,(u,0))∈A,
    G∈B_(G,u)。

この shear が、指定された X→G を保存しつつ Ab の議論を使用するための要点である。

## 4. Seed を含む小さい pointed subobject

f:(Y,y)→(G,u) を A への任意の射とする。S=f(Y)⊂G と置く。
f y=u なので、S は u(X) を含む。
μ=max(|Y|,ℵ₀) とすれば |S|≤μ。

§3 で構成した B_(G,u) に補題 1 を適用する。P∈B_(G,u) と θ:G→P が得られ、

    θ(S)=0,
    |ker θ|≤μ^ℵ₀。

P∈B_(G,u) だから (G⊕P,(u,0))∈A。
次の二つの準同型を考える。

    a,b:(G,u)⇉(G⊕P,(u,0)),
    a(g)=(g,0),
    b(g)=(g,θ(g))。

θu=0 なので、両方とも X/Ab の射である。
その equalizer は

    (K,u_K)=(ker θ, u:X→ker θ)。

従って (K,u_K)∈A。S⊂K なので f はこの subobject を経由し、|K|≤μ^ℵ₀。
主定理の small-subobject conclusion が得られた。

注意：B_(G,u) において kernel を取るだけでは (K,u_K)∈A は出ない。B_(G,u) の membership は (G⊕K,(u,0))∈A を意味するにすぎない。上の **graph map と zero graph map の equalizer** が、必要な pointed subobject を取り出している。

## 5. Solution set と reflection

(Y,y) を固定し、ν=max(|Y|,ℵ₀)^ℵ₀ とする。
濃度≤ν の abelian groups K の同型代表、それらへの構造射 X→K、さらに (Y,y) からの射の全ては集合をなす。
このうち A に属するものを取れば、§4 によって ((Y,y)↓A) の weakly initial set になる。

A は complete で inclusion は limits を保存するので、solution-set form の adjoint functor theorem によって reflection が存在する。

反射自身の濃度評価も直接得られる。上の weakly initial set の積を取り、そこへの (Y,y) からの射の image を §4 により小さい A-subobject に入れる。これにより、濃度≤ν の weakly initial object W を comma category 内に得る。

W の全ての comma-endomorphisms と id_W の共通 equalizer e:I→W を取る。W の weak initiality から v:W→I があり、e の equalizing property と monicity により ve=id_I。
任意の comma-endomorphism t:I→I に対して etv は W の endomorphism なので、etve=e。従って t=id_I。

I から任意の comma-object への射は、I→W と W の weak initiality から存在する。二射の equalizer Q→I を取ると、weak initiality of W から Q への射を得て、それを I→W と合成することで Q→I の section を得る。I の endomorphism が id のみであることから equalizer は同型となる。従って I からの射は一意である。

よって I は initial、すなわち反射であり、|I|≤|W|≤ν。

## 6. E-ring 方向への帰結

E-ring R の additive group を unit 1 で point すると、(R,1) の pointed endomorphisms は id だけになる。この剛性や、大きい個別の localizations Z→R の存在は、主定理と矛盾しない。

主定理によると、(R,1) を含む full limit/countable-union closed class A の中には、1 を含む濃度≤𝔠 の pointed A-subgroup が必ず存在する。
従って |R|>𝔠 の場合、(R,1) はこの A における unit の最小 hull にはなれない。

この結論では multiplication-by-n を pointed endomorphism として使わず、bounded summand が unit を含むと仮定もしない。必要な Abelian-group の操作は B_(G,u) の中で実行し、最後の equalizer だけを元の coslice で取る。
