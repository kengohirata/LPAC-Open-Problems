# Problem 4：Ab では小極限と可算 ascending union 閉性から反射性が従う

2026-11-18。状態：PROOF_RECONSTRUCTED。全て ZFC。root と別 agent が主要な代数的議論・濃度評価を独立に確認し、現時点で問題を見出していない。外部査読・形式検証・新規性確認は未実施。

## 1. 主定理

**定理。** A⊂Ab が full replete subcategory で、次を満たすとする。

1. Ab の全ての小極限で閉じる。
2. Ab の countable ascending unions of subgroups で閉じる。

このとき A は reflective である。特に No.4 の ambient category が Ab の場合、答えは肯定である。

より具体的に、X∈Ab、μ=max(|X|,ℵ₀) とすると、任意の射 f:X→G、G∈A は、ある A-subobject H↪G を経由し、

    |H|≤μ^ℵ₀。

従って X から A への射に solution set が存在する。A-reflection R_A(X) 自身も |R_A(X)|≤μ^ℵ₀ と取れる。

これは一般の locally presentable ambient category に対する No.4 の解決を主張するものではない。

## 2. 使用する古典的な Abelian-group の事実

以下を使う。

**(B1)** Bounded abelian group は有限 cyclic groups の直和に分解する。

**(B2)** Abelian group の bounded pure subgroup は direct summand である。

正確な参照は Milne, *Addendum to: Values of zeta functions of varieties over finite fields*, Lemma 1(a),(b)。同所はそれぞれ Fuchs (1970), 17.2 と 27.5、および Kaplansky (1954), Theorem 7 を挙げている。[著者版 PDF](https://www.jmilne.org/math/articles/2015b.pdf)

**(D)** Divisible abelian groups は injective であり、Q と Prüfer groups C_(p∞) の直和に分解する。逆にこれらの直和は divisible。例えば Goldsmith–Kelly–Wallutis の論文冒頭にこの構造が明記されている。[原論文、pp.25–26](https://www.maths.tcd.ie/pub/ims/bull54/R5401.pdf)

**(E)** 任意の Abelian group M は essential injective extension M↪E を持つ。[Stacks Project, Lemma 47.5.2](https://stacks.math.columbia.edu/tag/08Y1)

特に、M に p-torsion がなければ、その injective envelope E にも p-torsion はない。実際、E 内の位数 p の cyclic subgroup があれば、essential 性から M と非自明に交わる。

注意：bounded groups を Ab の injective objects として扱ってはいない。(B2) は **pure subgroup の splitting** にのみ使う。injectivity を使うのは divisible groups の場合である。

## 3. A で利用できる基本操作

空極限から 0∈A。従って空の A は仮定を満たさず、A={0} なら X↦0 が反射である。

小極限閉性から、A は積・kernel・pullback・retract で閉じる。最後の主張は、idempotent e の像を Eq(e,id) として表せることによる。

### 3.1 非零 torsion-free object があれば Q が入る

非零 torsion-free K∈A があるとする。Q⊗K 内の実際の部分群

    K⊂(1/2!)K⊂(1/3!)K⊂⋯

は各々 K と同型で、union は Q⊗K。従って Q⊗K∈A。非零 Q-vector space は Q を linear retract として持つので、Q∈A。

従って

    Q∉A ⇒ A 内の torsion-free object は 0 だけ。

### 3.2 利用可能な divisible groups の任意直和

Divisible groups D_i∈A の任意の集合族に対して、直和 ⊕_i D_i も A に属する。

実際、その直和は divisible、従って injective。自然な包含 ⊕_i D_i↪∏_i D_i は、domain の injectivity により split する。右辺は A に属するので、retract 閉性を使える。

この操作には directed union 閉性を使わない。これにより、主定理で可算 ascending unions だけを仮定すればよい。

## 4. 素数ごとの許容 torsion exponent

素数全体を二つに分ける。

    U={p : A の対象の p-primary torsion exponent に有限の共通上界がない},
    B={p : p∉U}。

p∈B について、全ての G∈A の p-primary torsion subgroup T_p(G) が p^(n_p) で消えるような有限 n_p≥0 を一つ固定する。n_p=0 はその prime の torsion が全対象で零の場合を表す。

### 4.1 p∈U なら C_(p∞)∈A

任意の n≥1 を取る。U の定義から、ある G∈A は位数が p^n 以上の p-power である元を持つ。従って bounded kernel G[p^n]=ker(p^n:G→G) は位数 p^n の元を持つ。(B1) による cyclic decomposition に、位数 p^n の summand が現れるので C_(p^n)∈A。

Prüfer group C_(p∞) はその finite cyclic subgroups C_(p^n) の ascending ω-union である。従って C_(p∞)∈A。

### 4.2 U≠∅ なら Q∈A

p∈U を一つ選ぶ。D=∏_(n≥1) C_(p∞) は divisible で A に属する。第 n 座標に位数 p^n の元を取れば、D 内に無限位数の元が得られる。

(D) の分解定理により、D は Q の非零直和因子を持つ。したがって Q が retract として A に入る。

特に、Q∉A の場合には U=∅、すなわち全ての prime が B に属する。

## 5. bounded primary parts の splitting

G∈A と p∈B に対して

    T_p(G)=G[p^(n_p)]∈A。

T_p(G) は G の pure subgroup である。実際、m y∈T_p(G) なら y は torsion であり、y の primary decomposition の p 成分 y_p を取れば m y_p=m y。従って T_p(G)∩mG=mT_p(G)。

(B2) により retraction

    r_p:G→T_p(G)

を選べる。q≠p の primary torsion subgroup は r_p により零に送られる。従って r_p の族は ⊕_(p∈B) T_p(G) 上で元を分離する。

## 6. G を、A に属する制御可能な対象へ埋め込む

### Case I: Q∉A

§4.2 から B は素数全体である。写像

    j:G→∏_p T_p(G),  j=(r_p)_p

の kernel K は A に属する。

K は torsion-free。非零 torsion element g の primary decomposition の非零成分 g_p を取れば、r_p(g)=g_p≠0 だからである。§3.1 と Q∉A により K=0。従って j は単射である。

### Case II: Q∈A

    T_B=⊕_(p∈B)T_p(G)≤G,
    M=G/T_B

と置く。ここで T_B や M が A に属するとは仮定しないし、証明にも不要である。

M は B-primary torsion を持たない。より正確には

    t(M)=t(G)/T_B=⊕_(p∈U)T_p(G)。

実際、ng∈T_B⊂t(G) なら g∈t(G) なので、商の torsion は t(G) の像に限られる。

M の essential injective envelope M↪E を取る。§2(E) により E も B-primary torsion を持たない。従って分解 (D) の summands は Q と C_(p∞)、p∈U だけである。これらは全て A に属し、§3.2 により任意直和も A に属するので、E∈A。

商写像と envelope を合成した q:G→E を使い、

    j:G→E×∏_(p∈B)T_p(G),  j=(q,(r_p)_p)

と置く。q の kernel は T_B であり、r_p は T_B 上で元を分離するので、j は単射である。source と target の全対象は A に属する。

## 7. 指定された元を含む小さい A-subobject

G∈A と S⊂G を取り、μ=max(|S|,ℵ₀) とする。

各 p∈B について、(B1) により T_p(G) を有限 cyclic groups の直和に分解する。r_p(S) の元の supports を全て集めると、必要な summands は高々 μ 個である。それらの直和を H_p とすれば、

    r_p(S)⊂H_p≤T_p(G),
    |H_p|≤μ,
    H_p は T_p(G) の direct summand。

従って H_p∈A。

Case II では、q(S) を含む divisible subgroup E_0≤E を |E_0|≤μ となるように取れる。具体的には q(S) の生成する subgroup から始め、各段階で全ての元の全ての正整数 n に対する n-th roots を E の中から選んで加え、これを可算回繰り返す。各段階と union の濃度は μ 以下で、union は divisible になる。

E_0 は E の部分群なので B-primary torsion を持たない。従って、その divisible decomposition は Q と U-primes の Prüfer groups だけからなり、§3.2 により E_0∈A。この membership の主張は、構成の途中の subgroups が A に属することを必要としない。

Case I では E の因子を省く。Case II では

    P_0=E_0×∏_(p∈B)H_p

と置く。両場合とも P_0∈A であり、素数は可算個しかないので

    |P_0|≤μ^ℵ₀。

§6 の monomorphism j:G→P の下での inverse image

    H=G×_P P_0=j^(-1)(P_0)

を取る。pullback 閉性から H∈A。j が mono なので H→P_0 も mono であり、|H|≤μ^ℵ₀。構成から S⊂H。

これが主定理の一様な local bound である。

## 8. solution set から反射を得る

X∈Ab を固定し、ν=(max(|X|,ℵ₀))^ℵ₀ とする。|H|≤ν の A-objects の isomorphism types は集合をなす。それらへの全ての射 X→H を集めれば、§7 により X から A への射の solution set になる。

A は full で小極限で閉じるので、comma category (X↓A) は complete かつ locally small。solution set の全対象の積を取ると、weakly initial object (η:X→P) が得られる。

§7 を η(X)⊂P に適用して、η が |W|≤ν の A-subobject W↪P を経由するようにできる。この X→W も weakly initial である。実際、任意の X→G が P→G を使って分解されるので、その射を W に制限すればよい。

以下の標準的な complete-category の議論を明記して、一意性も得る。

1. (X↓A) における W の全 endomorphisms と id_W の共通 equalizer e:I→W を取る。endomorphisms は集合なので小極限で足りる。
2. W の weak initiality により v:W→I を取れる。ev は W の endomorphism なので、equalizer の定義から eve=e。e は mono だから ve=id_I。
3. 任意の endomorphism t:I→I に対し etv は W の endomorphism。よって etve=e、すなわち et=e、従って t=id_I。
4. 任意の平行二射 a,b:I⇉G の equalizer J→I を取り、W→J と e:I→W を合成すれば I→J が得られる。その後 J→I と合成した endomorphism は id_I。従って J→I は split epi かつ mono、すなわち同型であり、a=b。

I から全対象への射は W の weak initiality と e から存在し、上で一意性も示した。従って I は (X↓A) の initial object、つまり X の A-reflection である。さらに I↪W より |I|≤ν。主定理が証明された。□

## 9. 仮定と結論の境界

Union 閉性を使った場所は二つだけである。

* 非零 torsion-free K の factorial chain から Q⊗K を作る。
* 有限 cyclic p-groups の chain から Prüfer p-group を作る。

どちらも可算 ascending unions である。その他の大きな対象は積・retract・kernel・pullback と、Ab における外部の構造定理を用いて扱った。特に quotient G/T_B や、E_0 の root-closure の途中の群が A に属するという未証明の仮定は使っていない。

この結果は、Specker 群や graph-to-Ab の torsion-free 構成に限らず、**Ab 内の full subcategory を No.4 の反例にする経路全体**を除外する。一般の locally presentable category、一般の module category、nonabelian groups について同じ証明が使えるとは主張しない。
