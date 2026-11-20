# Problem 4：V を終域とする等化子は安全 — 根の成分圧縮と可算分離

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下は今回の直接証明を展開・自己点検した段階。独立査読・形式検証・新規性確認は未実施。一般の H_fg の等化子閉性、N⇒¬P4、P4 の反例完成は結論しない。**

**同日後続：一般の H_fg 等化子閉性は N+(NC) の下で否定された。** [filtered-colimit 閉性による障害](eqc_obstruction_sufficiently_filtered_colimits_2026-11-17.md) を参照。本稿の V を終域とする等化子定理と相対圧縮はその結論と両立する。V^(2) が具体的な失敗証人になるかは未同定である。

## 0. 今回の結論

前回の候補 V と E(Y_kappa) の間の二射を調べるという依頼を実行した。

1. **各 E(Y_kappa)→V は一意。** したがって、この始域・終域から非自明な二射の等化子は作れない。唯一の射を明示した。
2. さらに、**任意の Z∈H_fg と二射 a,b:Z⇉V の等化子は H_fg に属する**ことを示した。V は D に埋め込めないが、等化子の終域としては問題を起こさない。
3. 核心は、F→E(Y)（F は finitely generated）を E(Y_F) 経由に因子化し、Y_F の各 M_1-set の**連結成分数だけ**を continuum 以下にする圧縮。Y_F 自体の carrier は小さくしていない。
4. |S|≤continuum なら、任意の M_2-map Ω^S→colim_{alpha<omega_1} Ω^{T_alpha} は一つの stage に因子化する、という直接補題を証明した。可算分離族、Boolean 部分の可算交叉保存、各 stage の実際の点を使う。N は不要。
5. この因子化で得る stage maps は明示的に E の像の射なので、最後の等化子を C 内の余等化子から作れる。**今回の等化子定理自体は ZFC の直接証明であり、N も No.1 の非余反射性 (NC) も不要。** H_fg の非反射性を結論する既存の別の議論では、引き続き N と採用済み (NC) を使う。
6. 次の自然な検査対象として、Z_* を R_2=(Ω² --id,id--> Ω²) に置き換えた V^(2) を明示した。これは H_fg に属し、今回の根による分離性を満たさない。ただし、その等化子閉性の肯定・否定は今回確定していない。

この結果は H_fg を棄却する結果ではなく、反例探索に選んだ V という終域を除外する結果である。

## 1. 設定と依存関係

Ω=ω、M_1=M_2=End_Set(Ω) を別々のコピーとする。積 mn は m∘n。

    K=(M_1-Set)^J,      J=(0⇉1),
    P=(M_2-Set)^((M_1×J)^op).

P の各 sort には左 M_2-作用と右 M_1-作用があり、両者は可換。二つの構造射は sort 1→sort 0。

Y∈K に対し

    E(Y)_i=Ω^(Y_i)

とする。M_2 は後合成、M_1 は前合成で作用する。

    (m_2 f)(y)=m_2(f(y)),       (f·m_1)(y)=f(m_1 y).

E は K^op→P の忠実関手で、小余極限を小極限に送る。これらは ZFC。N の下での full faithfulness は Isbell の定理から従うが、今回の最後の等化子では full faithfulness を使わない。

C⊆K は

    Y_0 の全元が有限支持を持つ、かつ
    H_1(p_Y):H_1(Y_1)→H_1(Y_0) が全単射,
    H_1(A)=Hom_(M_1)(A,Ω)

というクラス。D は E(C^op) の replete image。

C の小余極限閉性は ZFC で直接確認できる。第0成分の colimit の元は元の段階の元から来るので有限支持を保つ。Hom_(M_1)(-,Ω) は colimit を limit に送り、p の Hom 写像は bijections の limit になる。

H_fg は P の次の full replete class：

    Z∈H_fg iff
    全 finitely generated F と全 f:F→Z が F→D→Z (D∈D) と因子化する。

中間 D の大きさや D→Z の mono 性は要求しない。

D⊆H_fg、および H_fg の directed-union 閉性は、この定義から ZFC で従う。以前の非反射性は今回の定理の入力ではない。

## 2. V の正確な形

alpha<omega_1 に対し

    T_alpha={t:alpha→ω : t は単射、ω\im(t) は無限}

とする。restriction maps r_{beta,alpha}:T_beta→T_alpha は全射。各 T_alpha は非空。

    Z_*=(Ω --id,id--> Ω),
    C_alpha=T_alpha・Z_*,
    V_alpha=E(C_alpha),
    V=colim_{alpha<omega_1} V_alpha.

C_alpha∈C、遷移 V_alpha→V_beta は mono（実際 split mono）。従って V∈H_fg。

M_2-set として

    Kappa=colim_{alpha<omega_1} Ω^(T_alpha)

と書く。Kappa は今回の補助対象であり、巨大基数の記号ではない。

V の両 sort は同じ

    L=colim_{alpha<omega_1} Ω^(T_alpha×Ω)

であり、p_V=q_V=id_L。ここで

    L ≅ Kappa^Ω                                             (2.1)

が成立する。可算個の Kappa の元は、一つの alpha<omega_1 に同時に現れるからである。逆向きの injectivity は stage injections の mono 性。

この表示で右 M_1-作用は

    (u·m)(n)=u(m(n)),    u:Ω→Kappa。

特に、右の定数変換 c_n は u の第 n 座標を定数列として取り出す。従って

    [∀n, u·c_n=v·c_n] ⇒ u=v。                            (2.2)

## 3. 最初の検査：E(Y_kappa)→V は一本しかない

M_1-set A の連結成分は、作用の向きを忘れた connected components とする。c_n∈M_1 は定数 n の写像。

同じ成分 C のどの a を選んでも

    rho_C(n)=c_n a

は同じである。実際 c_n m=c_n なので、作用に沿ってこの値は変わらない。逆に同じ根を持つ二元は共通の c_0 a を通じて連結する。

A が非空連結なら、全ての y∈A について c_n y=rho(n) であり、

    f·c_n = constant_(f(rho(n)))   (f∈Ω^A)。

任意の bimodule map h:Ω^A→L は M_2 の定数変換を保つので、(2.2) により一意に

    h(f)=[(t,n)↦f(rho(n))]                              (3.1)

と決まる。この式は stage 0（T_0 は一元集合）に入る。

No.1 の Y_kappa の両成分は非空連結である。第0成分 C([0,kappa]) も第1成分 Ω^[0,kappa] も、M_1 の定数変換ですべて定数関数に送られる。p,q はその根を保存する。

よって

    |Hom_P(E(Y_kappa),V)|=1。

唯一の射は、Z_*→Y_kappa の定数関数による射を E で反転し、V_0=E(Z_*)→V を合成したもの。

したがって E(Y_kappa)⇉V の等化子として X を得る方針は、この段階で除外される。これは『射が見つからなかった』ではなく一意性の証明である。

## 4. Scalar stage-factorization lemma（ZFC）

### 補題4.1

S は |S|≤c=2^aleph_0 の集合とする。任意の M_2-map

    phi:Ω^S→Kappa

は、ある alpha と集合写像 tau:T_alpha→S によって

    phi(f)=i_alpha(f∘tau)  for every f:S→Ω               (4.1)

と書ける。すなわち一つの stage に因子化する。

S=∅ の場合は Ω^S=1 に M_2 の共通固定点があり、Kappa にはないため、そもそも phi は存在しない。以下 S≠∅。

### 4.2 Boolean 部分と可算演算

Kappa の {0,1}-値元からなる部分 B(Kappa) は、2^(T_alpha) の increasing union と同一視できる。

任意の可算族の元は一つの stage に現れる。その stage で点ごとの union/intersection を取れば、B(Kappa) の可算 join/meet になる。後の stage への pullback はこれらを保存するので、計算は stage の選び方に依存しない。

phi は定数関数を保ち、Boolean 元を Boolean 元へ送る。さらに

    Phi:P(S)→B(Kappa),     Phi(A)=phi(chi_A)

は Boolean homomorphism。

有限 meet の説明：全単射 b:Ω²→Ω を選ぶ。任意の二関数 f,g に対する h=b(f,g) の像 phi(h) は、二つの射影を合成すると phi(f),phi(g) になる。Kappa でも二射影は jointly injective であり、同じ stage で tuple を符号化できる。従って phi は tuple 符号化を保つ。AND 等は符号化後の unary map として表せるので、Boolean 演算も保つ。

**Phi は可算 join/meet も保つ。** A_n の disjointification D_n=A_n\union_{k<n}A_k を取り、

    r(s)=n+1 if n is the first index with s∈A_n,
    r(s)=0 if no such index exists

とする。chi_(D_n) は r に unary selector を後合成したもの。従って Phi(D_n) は phi(r) の値 n+1 の fibre に等しい。phi(r) が現れる一つの stage で計算すれば、これらの可算 join は phi(r)≠0 の部分、すなわち Phi(union_n A_n) になる。有限 Boolean 演算と disjointification の整合性から一般の countable join を保つ。meet は complement から従う。

この議論は countable family 全体を Ω に単射符号化したものではない。first-hit map の値域が Ω になることを使う。

### 4.3 可算分離族から stage 上の評価点を復元

|S|≤c なので、可算族 d_n:S→Ω で点を分離できる。

phi(d_n) の全てを一つの alpha に取り、代表 d'_n:T_alpha→Ω を選ぶ。

任意の t∈T_alpha に対して、列 (d'_n(t))_n は、ある一意な s∈S の列 (d_n(s))_n に等しい。

存在の証明：そのような s がなければ、A_n={s∈S:d_n(s)=d'_n(t)} は交わりが空。可算 meet 保存により Phi(∩A_n)=0。一方、Phi(A_n) の stage-alpha 表示は t をすべて含むので、その meet は t を含み矛盾。

一意性は d_n の分離性。tau(t)=s と定める。

任意の s∈S に対し、singleton {s}=∩_n d_n^{-1}(d_n(s)) なので、Phi({s}) は stage alpha における tau^{-1}(s) の特性関数で表せる。

任意の f:S→Ω について phi(f) を beta≥alpha の代表で表す。u∈T_beta、s=tau(r_(beta,alpha)(u)) と置く。

    {s}⊆f^{-1}(f(s))

と Phi の単調性から、phi(f) の u での値は f(s) である。すべての u について成り立つので (4.1) が得られる。

**重要：すべての f を一つの stage に初めから集めたのではない。可算個の d_n だけを集め、singleton の像を使って任意の f を同じ stage の評価へ強制している。** □

## 5. 根の成分数が continuum 以下なら、E(Y)→V は stage に因子化する

### 補題5.1

Y∈K とし、各 i=0,1 について |pi_0(Y_i)|≤c とする。任意の theta:E(Y)→V は、ある alpha において

    E(Y) --theta_alpha--> V_alpha --i_alpha--> V

と因子化する。

さらに theta_alpha は、明示的な K-morphism k_alpha:C_alpha→Y の E による像である。ここにも N は不要。

**証明。** 一つの sort A=Y_i に注目し、I=pi_0(A)、pi:A→I とする。g:I→Ω に対して g∘pi は右 M_1-不変。その theta 像は Kappa^Ω の定数列なので、

    phi(g)=theta(g∘pi)(0)

で M_2-map phi:Ω^I→Kappa を得る。

任意の f:A→Ω と n∈Ω に対し

    theta(f)(n)=phi(g_(f,n)),
    g_(f,n)(C)=f(rho_C(n))。                            (5.1)

これは f·c_n=g_(f,n)∘pi から従う。

補題4.1により phi は tau_i:T_alpha→I を使う評価として表せる。従って

    theta_(alpha,i)(f)(t,n)=f(rho_(tau_i(t))(n))。       (5.2)

両 sort について共通の alpha を取る。V_alpha→V が mono なので、theta の自然性は theta_alpha の自然性へ反映される。

(5.2) は集合写像

    k_(alpha,i):T_alpha×Ω→Y_i,
    k_(alpha,i)(t,n)=rho_(tau_i(t))(n)

による前合成。これは M_1-equivariant。さらに、E は忠実なので theta_alpha の自然性から k_alpha の二本の構造射に関する自然性が従う。よって k_alpha:C_alpha→Y は K の射であり theta_alpha=E(k_alpha)。□

Y の carrier 全体にはサイズ制限がない。制限しているのは M_1-connected components の数だけ。

## 6. 有限生成 F に相対的な根の成分圧縮（ZFC）

### 6.1 双対 Hom と自然な転置

F∈P に対して

    Q(F)_i=Hom_(M_2)(F_i,Ω),
    (m h)(x)=h(x·m)

と定める。P の二射を前合成で反転すると Q(F)∈K。

自然な全単射

    Hom_P(F,E(Y)) ≅ Hom_K(Y,Q(F))                      (6.1)

がある。成分では f:F_i→Ω^(Y_i) を

    f^sharp(y)(x)=f(x)(y)

へ送る。これは普通の currying と作用の可換性だけであり、E の full faithfulness を必要としない。

### 6.2 F が finitely generated なら Q(F) の成分数は continuum 以下

F が P で finitely generated なら、各 sort F_i は有限集合 Gamma_i から左 M_2・右 M_1 の両作用で生成される。sort 0 には、元の sort-0 generators と sort-1 generators の二つの構造射による像を加えればよい。

h∈Q(F)_i に countable signature

    sig(h)=(h(g·c_n))_(g∈Gamma_i,n∈ω)

を対応させる。

この signature は M_1-action に沿って不変：

    sig(m h)_(g,n)=h(g·c_n m)=h(g·c_n)

だからである。

逆に sig(h)=sig(h') なら c_0 h=c_0 h'。実際、任意の生成表示 x=m_2 g·m_1 に対し

    (c_k h)(x)=m_2 h(g·c_(m_1(k)))

なので、すべての根 c_k h は signature から決まる。同じ c_0-root を持つ h,h' は同じ connected component。

従って

    pi_0(Q(F)_i) ↪ Ω^(Gamma_i×ω),
    |pi_0(Q(F)_i)|≤c。                                 (6.2)

F_i が空の場合も Gamma_i=∅ としてよい。Q(F)_i は一元集合で成分数は1。

### 6.3 自由な根だけを残す R

任意の M_1-set A に対して

    R(A)=Ω×pi_0(A),
    epsilon_A(n,C)=rho_C(n)

と置く。M_1 は Ω 座標に作用する。epsilon_A は自然な M_1-map。

K の図式には成分ごとに適用する。任意の Y∈K について R(Y)∈C：各成分は Ω の copower なので、Hom_(M_1)(R(Y)_i,Ω) は一元集合（空 copower の場合も同じ）。第0成分は有限支持。

### 補題6.4：相対圧縮

F は finitely generated、Y∈C、f:F→E(Y) とする。このとき Y_F∈C、q:Y→Y_F、f_F:F→E(Y_F) が存在し、

    E(q) f_F=f,
    |pi_0((Y_F)_i)|≤c  (i=0,1)。                       (6.3)

**構成。** (6.1) で f を f^sharp:Y→Q(F) に転置し、K の pushout

    R(Y) --epsilon_Y--> Y
      | R(f^sharp)        | q
      v                   v
    R(Q(F)) -----------> Y_F

を取る。

三つの入力 Y,R(Y),R(Q(F)) は C に属する。C は colimit-closed なので Y_F∈C。

f^sharp と epsilon_(Q(F)) は整合し、Y_F→Q(F) を与える。その転置を f_F とすれば E(q)f_F=f。

pi_0 は M_1-sets の connected-components functor で、trivial action functor の左随伴だから colimit を保存する。epsilon_Y は connected components 上で同型。従って各 sort で

    pi_0((Y_F)_i) ≅ pi_0(Q(F)_i)。

(6.2) から上界が従う。□

**制限の確認：Y_F の全要素数を continuum 以下にしたわけではない。q や E(q) の mono/epi 性も要求しない。この補題は No.1 の解集合の障害を回避して小さい反射を作るものではない。**

## 7. 主定理：V を終域とする等化子閉性

### 定理7.1（ZFC、今回の直接証明）

任意の Z∈H_fg と二射 a,b:Z⇉V に対して

    Eq(a,b)∈H_fg。

**証明。** e:W→Z を P の等化子とし、任意の finitely generated F と x:F→W を取る。

Z∈H_fg により

    ex = v f,
    F --f--> E(Y) --v--> Z,
    Y∈C

と因子化する。同型コピーは適宜選ぶ。

補題6.4で f を

    F --f_F--> E(Y_F) --E(q)--> E(Y)

と因子化する。Y_F∈C で connected components は各 sort とも continuum 以下。

補題5.1を二射

    a v E(q), b v E(q):E(Y_F)⇉V

に適用し、共通の alpha を取って

    a v E(q)=i_alpha a_alpha,
    b v E(q)=i_alpha b_alpha

とする。a_alpha,b_alpha:E(Y_F)⇉V_alpha は明示的に

    a_alpha=E(k_a), b_alpha=E(k_b),
    k_a,k_b:C_alpha⇉Y_F

の形である。

i_alpha は mono で、元の二射は f_F 上で一致するので

    a_alpha f_F=b_alpha f_F。

ここで K において

    C_alpha ⇉ Y_F --r--> R

を k_a,k_b の coequalizer とする。C_alpha,Y_F∈C と colimit 閉性から R∈C。

E はこの coequalizer を P の equalizer に送るので

    E(R) --E(r)--> E(Y_F)

は a_alpha,b_alpha の等化子。従って f_F は E(R) を経由する。

さらに v E(q) E(r):E(R)→Z は a,b を等化するため W を経由する。よって元の x は

    F→E(R)→W,       E(R)∈D

と因子化する。F,x は任意なので W∈H_fg。□

### N を使っていない箇所を再確認

最後に『D が全等化子で閉じる』を黒箱として使うと N が入る。しかし、今回の stage maps は (5.2) の明示的な前合成写像であり、K の射 k_a,k_b を直接得ている。C 内の coequalizer を E で移せばよく、fullness は不要。

したがって主定理の証明は、N、可測基数の不存在、No.1 の (NC) のいずれにも依存しない。ただし、この主定理と別に H_fg が非反射的だと結論する際は、前回どおり N と (NC) が必要。

### 系7.2

W→V が P の mono なら、任意の Z∈H_fg と二射 Z⇉W の等化子も H_fg に属する。mono を後合成して定理7.1を使えばよい。

これを『全 H_fg-object が V に埋め込める』という主張に読み替えてはいけない。

## 8. 一般化しなかった点と countable-directedness の役割

主定理は任意の W∈H_fg を終域とする場合まで証明したものではない。

特別な V の以下の二性質を使った：

(A) 各 sort が Kappa^Ω で、M_1 の定数変換が全座標を取り出すこと。
(B) Kappa が omega_1-directed union of full powers で、可算族が同じ atomic stage に入ること。

単なる directed union では (B) と (2.1) は自動でない。

例えば前回の可算鎖 U=colim_n E(2^n・Z_*) では、scalar part K_fin は Cantor 空間の有限座標依存関数である。列

    u_n(x)=x_n

は K_fin^Ω の元を与えるが、一つの有限 stage に一様には入らない。したがって

    colim_n Ω^(2^n×Ω) → (colim_n Ω^(2^n))^Ω

は全射でない。

ただし U 自体は E(2^ω・Z_*)∈D に埋め込めるので、以前の codomain-embedding lemma の範囲で既に安全である。U を新たな反例候補として提出するものではない。

## 9. 次に調べる具体的終域：根だけでは分離できない V^(2)

今回の証明の仮定 (A) を破り、同時に H_fg 所属性を確保する例は作れる。

    R_2=(Ω² --id,id--> Ω²)∈C,
    V^(2)=colim_{alpha<omega_1} E(T_alpha・R_2)。

R_2 の第0成分は有限支持、p=id なので R_2∈C。全 stage が D、遷移が mono なので V^(2)∈H_fg。

各 sort は

    colim_alpha Ω^(T_alpha×Ω²) ≅ Kappa^(Ω²)

で、M_1 は Ω² に対角作用する。

右定数変換による検査は、関数の対角 (n,n) の値しか見ない。例えば stage 内の

    u(t,a,b)=0,
    v(t,a,b)=0 if a=b, and 1 otherwise

は異なる元だが、全 n で u·c_n=v·c_n。したがって (2.2) は V^(2) で失敗する。

このため、V^(2) は V の任意の積にも mono で埋め込めない。右定数変換による分離性は products と subobjects に保存されるからである。

また N の下では、各 sort の Ω への Hom は

    lim_alpha(T_alpha×Ω²)=∅

となるので、前回と同じく V^(2) は D-object に埋め込めない。

**ここまでが今回確認した範囲。V^(2) を終域とする H_fg の等化子閉性、または反例は未確定。** この候補は、単に同じ V の濃度を増やすのでなく、今回の証明で使った根の分離性を実際に破る。

## 10. 監査項目

1. M_1 の左作用、P の右作用、M_2 の左作用を区別した。特に m c_n=c_(m(n))、c_n m=c_n の二式を取り違えない。
2. 有限生成 F の各 sort の有限 bimodule generators は、sort-1 generators の二つの構造射像を加えて得る。
3. §6.2 の sig(h) は可算長の値の列であり、Q(F) 自体の台集合の濃度ではなく connected components を数える。P の unary operations 全体の signature は濃度 continuum であり、可算とはしていない。
4. R(Y) は、固定点を持つ成分でも自由な Ω-root を置く。epsilon_Y が injective であるとは仮定しない。
5. pushout 後の C 所属性は C の既知の colimit 閉性を使う。Q(F) 自体が C に属するとは仮定しない。
6. Scalar lemma の可算 meet 保存を、Ω^ω の Ω への符号化で主張しない。可算 disjointification と first-hit map を用いる。
7. Stage alpha を選ぶのは可算分離族の像に対してのみ。任意の f の像の同一 stage 所属は、singleton の像と stage の実際の点から導く。
8. Scalar lemma の |S|≤c を外していない。一般の巨大な S に同じ主張をしていない。
9. 最後の equalizer は full faithfulness ではなく、明示的な K の二射の coequalizer を E で移して作る。これにより新しい閉性定理は ZFC の証明になる。
10. V が D に埋め込めないという性質を、等化子で H_fg を破る十分条件と取り違えない。今回の結果はその区別を具体的に示す。
11. V^(2) は次の具体候補にすぎず、反例完成を意味しない。

## 11. 文献と保存記録

このノートの補題4.1、5.1、6.4、定理7.1は今回の直接導出。公刊済みの定理や独立査読済みの新規結果として扱わない。

既存設定：

- `negative_isbell_transport_fg_factorizations_equalizer_obstruction_2026-11-17.md`：K,P,C,D,H_fg,V の定義、以前の二つの等化子範囲、No.1 からの非反射性入力。

外部一次資料の再確認：

- J. R. Isbell, *Adequate subcategories*, Illinois J. Math. 4 (1960), 541–552, Theorem 2.5, p.549。
  https://webhomes.maths.ed.ac.uk/~tl/docs/Isbell_Adequate_subcategories.pdf
- M. Shulman, *Set theory for category theory*, p.20。
  https://arxiv.org/pdf/0810.1279

両資料は本文と該当ページの screenshot を再確認した。参照目的は、旧設定の N 条件下の Set^op→M-Set の full embedding の照合。今回の新しい stage-factorization や等化子定理をこれらの資料に帰属させない。

今回は有限計算を無限・可算・omega_1 の証明の代替として使っていない。核となる検査は上記の直接証明と、仮定・射の向き・サイズ境界の自己点検である。
