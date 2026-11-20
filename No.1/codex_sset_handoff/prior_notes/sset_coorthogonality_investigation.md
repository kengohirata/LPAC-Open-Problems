# sSet における small-coorthogonality の調査

2026-11-15

## 0. 問題と到達点

圏 K と射の集合 S に対して、

A_S = { X | Hom_K(X,f) がすべての f∈S について全単射 }

と置く。P_K は「すべてのそのような A_S が K で coreflective」という主張。
本ノートでは K = sSet = Set^(Δ^op) を調べる。Hom は通常の射の集合であり、ホモトピー類や derived mapping space ではない。

一般の P_sSet の ZFC 証明も、追加公理の下での反例も、本ノートでは得ていない。
以下は直接証明した還元・十分条件・例である。新規性は主張しない。

主要結果：

1. 非自明な場合、テスト射は頂点上全単射な一本の射にまとめられる。
2. 各テスト射の両端が 1-coskeletal なら ZFC で肯定。
3. 各テスト射の始域が degreewise finite なら、終域は任意でも ZFC で肯定。
4. テスト射が degreewise compact Hausdorff な simplicial objects の間の連続な射として与えられるなら、直交類は locally aleph_1-presentable。
5. P_sSet ⇒ P_Cat ⇒ P_Grp ⇒ P_Ab。反例は逆方向に移せる。
6. 2-coskeletal なテスト射で商閉性の失敗を実現できるが、その具体例も compactness によって肯定的に処理できる。

## 1. 頂点と一本の射への還元

### 命題 1.1

f:U→V について f_0 が全単射でないなら、{}^⊥{f}={∅}。

証明：非空な simplicial set X には頂点がある。その選択 j:Δ[0]→X と唯一の写像 r:X→Δ[0] は rj=id を満たす。
coorthogonality は retract に閉じるため、X⊥f なら Δ[0]⊥f。
Yoneda により Hom(Δ[0],f)=f_0。∎

すべての f_i が頂点上全単射なら、すべての離散 simplicial set は A_S に属する。
従って coreflection r:R(B)→B が存在するとき、その頂点写像は全単射。

### 命題 1.2

sSet の任意の small-coorthogonality class は一本の射で定義できる。
非自明な場合、その射は頂点上全単射に取れる。

証明：f_i の中に頂点上全単射でないものがあれば、命題1.1によりクラスは {∅}。これは ∅→Δ[0] で定義できる。
そうでなければ、空始域の射は ∅→∅ なので捨てる。残った U_i,V_i はすべて非空。
各 U_i の頂点を一つ選べば、任意の X から U_i,V_i への定数写像がある。
そこで f=∏_i f_i とする。自然な同一視の下で

Hom(X,f)=∏_i Hom(X,f_i)。

各因子の始域・終域が非空なので、積が全単射であることと全因子が全単射であることは同値。
空の族は Δ[0] の恒等射で表現する。∎

注意：この一本化は、有限性や compactness の証明に必要という意味ではない。必要に応じて元の族を使う。

## 2. Reflective full subcategory への移送

### 補題 2.1

L:K→D ⊣ J:D→K を adjunction とし、J は fully faithful とする。
D の射の集合 S に対して

A={}^⊥_D S,
C={}^⊥_K(JS)=L^(-1)(A)

と置く。任意の B∈D について、次は同値。

- B は D において A-coreflection を持つ。
- JB は K において C-coreflection を持つ。

証明：A-coreflection a:A_0→B があれば、任意の X∈C について

Hom_K(X,JA_0) ≅ Hom_D(LX,A_0)
              ≅ Hom_D(LX,B) ≅ Hom_K(X,JB)。

従って Ja が C-coreflection。

逆に c:C_0→JB を C-coreflection とする。
c の adjoint transpose を d:LC_0→B とすれば c=Jd・η_{C_0}。
LC_0∈A なので JLC_0∈C。coreflection の普遍性より

t:JLC_0→C_0,  ct=Jd

がある。c t η=c より、一意性から tη=id_{C_0}。
さらに対象 JLC_0 は反射部分圏内にあるため、η による前合成

Hom_K(JLC_0,JLC_0)→Hom_K(C_0,JLC_0)

は全単射。ηtη=η より ηt=id_{JLC_0}。
よって η は同型で、C_0≅JLC_0。これを通じて d が A-coreflection になる。∎

したがって、K,D が locally presentable なら P_K⇒P_D。
反例が D 内にあれば、同じ射を J で移したものが K 内の反例になる。

### 応用 2.2

nerve N:Cat→sSet は fully faithful な右随伴であり、その左随伴は categorification c。
[参考 R1, R2]

また、Grp→Cat は群を一対象圏と見る full embedding。この左随伴は、圏のすべての対象を一対象に潰した上で、各射を群の生成元、合成を関係式として課す universal group。
Ab→Grp も abelianization による reflective embedding。

従って

P_sSet ⇒ P_Cat ⇒ P_Grp ⇒ P_Ab。

重要：これは反例が現在存在するという主張ではない。存在すれば strict Hom と coreflection の不存在を保存して移せる、という還元。

### 応用 2.3：すべての presheaf 圏への還元

任意の locally presentable category は、ある presheaf category の full reflective subcategory として表せる（Adámek–Rosický, Theorem 1.46）。
従って

P がすべての locally presentable categories で成立
⇔ P がすべての小圏上の presheaf categories で成立。

これは「sSet 一つで十分」を意味しない。

## 3. Reflexive quivers は ZFC で肯定

RGraph を、頂点集合 X_0、辺集合 X_1 と

d_0,d_1:X_1→X_0,  s_0:X_0→X_1,
d_0s_0=d_1s_0=id

からなる圏とする。各頂点に指定された恒等ループがある。これは1-truncated simplicial sets の圏。

### 定理 3.1

RGraph の任意の small-coorthogonality class は、商に閉じ、monocoreflective である。

証明：非空な対象には一点 reflexive graph が retract として入る。
従って、テスト射の頂点写像が全単射でない場合、直交類は空対象のみ。
残る場合はすべてのテスト射の頂点写像が全単射である。

一本の f:U→V を固定する。X⊥f、q:X↠Y を各成分全射とし、h:Y→V を取る。
X⊥f から唯一の g:X→U があり fg=hq。
頂点については f_0 の単射性から、g_0 は q_0 の各 fibre 上で一定。

q_1(x)=q_1(x') である二辺を取る。g_1(x),g_1(x') の端点は一致し、f_1 による像も一致する。
x が指定された恒等辺でなければ、g_1(x) の値だけを g_1(x') に置き換えても reflexive-graph morphism で、fg=hq のまま。
一意性から g_1(x)=g_1(x')。
x が恒等辺でも x' が非恒等辺なら逆に置き換える。
両方恒等辺なら、頂点成分の一致からもともと同じ像を持つ。

よって g は q の fibre 上で一定で、k:Y→U に一意に降りる。fk=h。
従って Y⊥f。
この証明をすべての f_i について行えば、A_S は商に閉じる。

A_S は小余極限にも閉じる。固定 B の A_S-部分対象をすべて集め、その和集合（余積の像）を R(B)⊆B とする。
部分対象の同型類は集合個。余積と商への閉性から R(B)∈A_S。
任意の A_S-対象から B への射の像も A_S に属するので、R(B) を一意に経由する。∎

## 4. 1-coskeletal なテスト射は除外できる

r_n:sSet→sSet_{≤n} を次数nまでの制限とする。
右随伴 cosk_n は fully faithful。[R3]

両端が1-coskeletal な射 f は cosk_1(r_1f) と同一視できるので、

Hom_sSet(X,f) ≅ Hom_RGraph(r_1X,r_1f)。

定理3.1と、r_1 が各成分全射・余極限を保存することから、対応する A_S は sSet 内でも商と小余極限に閉じる。
従って同じ部分対象の和の構成で monocoreflective。

### 定理 4.1

各 f_i の両端が1-coskeletal なら、{}^⊥S は ZFC で coreflective。
サイズは任意。

注意：「1-coskeletal」は「1-skeletal」でも「ホモトピー的に1-truncated」でもない。

### 補足：一般の n-coskeletal テストの移送

T=sSet_{≤n}、S を T のテスト射、A={}^⊥_T S とする。
A が T で coreflective で、coreflector が R なら、sSet 内の

C={}^⊥(cosk_n S)=r_n^(-1)(A)

の coreflection は次の pullback で構成できる。

R_C(B)=B ×_{cosk_n(r_nB)} cosk_n(R(r_nB))。

r_n が極限を保存し r_n cosk_n≅id なので、r_nR_C(B)≅R(r_nB)∈A。
任意の X∈C から B への射について、次数nまでの射を R(r_nB) に一意に持ち上げ、adjunction と pullback の普遍性を使えば全体の一意な分解が得られる。

逆向きは補題2.1。したがって P_T は「cosk_n から来るすべてのテスト族の直交類が sSet で coreflective」と同値。

## 5. 小さい pure subobject と compact な標的

この節で compactness は補助的に使うだけであり、母圏は終始、通常の sSet。

### 補題 5.1：可算 pure 部分対象

任意の X とその可算個の simplices からなる部分集合 Z に対し、Z⊆Y⊆X となる、全 simplex の合計が可算な pure subsimplicial set Y が存在する。

ここで pure は、Y の元をパラメータに持つ有限連立方程式が X で解ければ Y でも解けるという意味。[R4, §2.2]

証明：simplicial identities を持つ、可算多ソート・可算 unary signature を使う。
Z の部分simplicial setとしての閉包を取り、現在の可算集合のパラメータを使うすべての有限連立方程式について、X 内の解を一つずつ加える。
これを可算回反復する。各段階は可算、合併も可算。有限パラメータはある段階で揃うため、最終合併は pure。
無パラメータの存在条件も含める。∎

### 補題 5.2：degreewise compact Hausdorff な標的への延長

D の各 D_n に compact Hausdorff topology があり、face/degeneracy maps が連続とする。
pure inclusion Y⊆X に対する任意の simplicial map h:Y→D は X→D に延長できる。

証明：各 x∈X_n の像を D_n に値を取る変数 z_x とする。
求める条件は、全face/degeneracyの保存と z_y=h(y) (y∈Y)。
これらは compact Hausdorff spaces の積内の閉条件。
有限部分の条件は、Y のパラメータを持つ有限方程式として X で解ける。purity により Y で解き、h を適用すれば D で解ける。
従って閉条件は有限交叉性を持ち、Tychonoff compactness により全条件を満たす解がある。
空なsortがある場合も、hの存在とpurityにより、Xにそのsortの元があるという矛盾は起きない。∎

### 定理 5.3：compact なテスト射

S={f_i:U_i→V_i} が、degreewise compact Hausdorff な simplicial spaces の間の連続な射の underlying simplicial maps であるとする。
このとき A_S は locally aleph_1-presentable、従って coreflective。

証明：W_i=U_i×_{V_i}U_i は各次数でcompact Hausdorff（閉部分空間）で、simplicial operators も連続。
X∈A_S の可算pure部分対象 Y を取る。

存在：h:Y→V_i を補題5.2で X→V_i に延長し、X⊥f_i により U_i へ持ち上げ、Yへ制限する。

一意性：g_0,g_1:Y→U_i で f_i g_0=f_i g_1 なら、(g_0,g_1):Y→W_i を X→W_i に延長する。
二つの射影 X→U_i は f_i との合成が等しいので X⊥f_i により等しい。Yに制限して g_0=g_1。

従って Y∈A_S。
各 X∈A_S は、可算な A_S-部分対象の aleph_1-directed union。
可算 simplicial sets は sSet で aleph_1-presentable（Δの射が可算個であることを使う；[R4, Convention 2.3 後]）。
A_S の小余極限は sSet で計算できるため、これらは A_S 内でも aleph_1-presentable。
可算 simplicial sets の同型類は集合個。よって A_S は locally aleph_1-presentable。
包含 A_S→sSet は余極限保存なので右随伴を持つ。∎

## 6. Degreewise finite な始域なら、終域は任意でよい

### 定理 6.1

各 f_i:U_i→V_i について、すべての n で (U_i)_n が有限なら、V_i に制約を課さなくても {}^⊥S は coreflective。

証明：各 f_i を e_i:U_i↠I_i と m_i:I_i↪V_i に像分解する。
m_i が mono なので

X⊥f_i ⇔ (X⊥e_i かつ X⊥m_i)。

U_i,I_i はdegreewise finite。有限離散位相を付ければ定理5.3が使え、

L={}^⊥{e_i}

は locally aleph_1-presentable で coreflective。包含 J:L→sSet の右随伴を R とする。
X∈L について Hom_L(X,Rm_i)≅Hom_sSet(JX,m_i)。Rm_i は L 内の mono。

残る条件は、locally presentable category L 内で、集合個の mono への coorthogonality。
このクラスは小余極限と strong quotients で閉じる：strong epi p:X↠Y と mono m に対し、X⊥m から strong epi/mono の持ち上げ性で Y⊥m が従う。
well-powerednessとstrong image factorizationにより、すべての当該部分対象の和の構成でcoreflectionを得る。
最後にLへのcoreflectionと合成する。∎

注意：始域だけdegreewise finiteの場合、この証明が直接示すのはcoreflectivityであって、最終クラスのaccessibilityではない。

## 7. 2次元の具体例：商閉性は失敗するが、それでも coreflective

T=R/Z を加法群（circle group）とし、BG=N(一対象圏G) と書く。

f=B(×2):BT→BT。

これは一頂点、2-coskeletal、各正次数で無限なテスト射。

X=BZ[1/2] は f に coorthogonal。
実際、群準同型 h:Z[1/2]→T の lift は g(a)=h(a/2) で与えられ、2g=h。
2g=h を満たす任意のgについて g(a)=2g(a/2)=h(a/2) なので一意。
nerveの充満忠実性から同じことがsimplicial Homに成立。

一方、C_{2∞}=Z[1/2]/Z とし Y=BC_{2∞} と置く。
商写像は各次数で全射な X↠Y を与える。
しかし、包含 h:C_{2∞}→T は ×2 に沿ってliftしない。
位数2の元 a=1/2+Z について、どんな準同型gでも2g(a)=g(2a)=0だが、h(a)≠0だから。
従って Y⊥f ではない。

つまり {}^⊥{f} は商に閉じない。

しかし、これは反例ではない。
(BT)_n=T^n にはcompact Hausdorff topologyがあり、face/degeneracy mapsと×2が連続。
定理5.3より {}^⊥{f} は locally aleph_1-presentable かつcoreflective。

さらに、この例でYのcoreflection r:R(Y)→Yはmonoではあり得ない。実際、A_fの対象Xからのepi X↠Yがrを経由するため、rがmonoなら同時にepiとなり、sSetでは同型になる。しかしYはA_fに属さない。

この例は「1-coskeletalの場合の商閉性証明は2次元では通らない」と「商閉性の失敗はcoreflectivityの失敗ではない」を同時に示す。

## 8. 2次元が既に Cat/Grp の難しさを含む

nerveは2-coskeletal。[R1,R2]
また、2-truncated nerve N_2:Cat→sSet_{≤2} もfully faithfulで左随伴を持つ。
左随伴は1-simplicesからfree categoryを作り、2-simplicesから合成関係を課すもの。
従って

P_{sSet_{≤2}} ⇒ P_Cat ⇒ P_Grp。

2-coskeletalなテスト射まで進むだけで、Grpで残った問題を含む。
したがって「無限次元だから難しい」という説明は正確でない。

切断を一段ずつ検査すれば十分、という逆向きも成立しない。
例：X=BC_3、U=BC_2、f:U→Δ[0]。
Hom_sSet(BC_3,BC_2)=Hom_Grp(C_3,C_2) は一点なので X⊥f。
しかし1-truncationではC_3の二つの非恒等辺をC_2の二辺へ独立に送れるため4通りの写像があり、r_1X⊥r_1fではない。
2-simplicesの合成条件が余分な割当を除いている。

## 9. Homotopy 版からの直接移植には二つの違いがある

Casacuberta–Gutiérrezの結果は、任意の射のクラスに関するhomotopy reflectivityをWVPと特徴づける。本文§1.2は今回の双対のcoorthogonalityを扱わないことを明記する。[R5]
Chornyはhomotopy coorthogonalityを扱うが、derived mapping spaceの弱同値が条件で、通常のHomの全単射性ではない。[R6]

明示例：f:Δ[1]→Δ[0] はweak equivalenceなので、すべてのXがhomotopy coorthogonal。
しかし非空のXからΔ[1]へは少なくとも二つの定数写像があるため、strict coorthogonality classは{∅}。

従って、この二条件を同一視したり、一般のhomotopy localization非存在を今回のsmall-coorthogonalityへ直接移したりしてはいけない。

## 10. 残った課題

一般のP_sSetは本ノートでは未判定。

次の明確な断片として、sSet_{≤2}の無限なデータを持つテスト射が残る。
反例を得るには、固定したfとBに対して、A_f={}^⊥{f}からBへの射にsolution setがないことを示す必要がある。

本ノートの結果により、少なくとも次を区別する。

- f_0が全単射でない：直交類は{∅}。
- 1-coskeletalな両端：商閉性から肯定。
- degreewise finiteな始域：pure/compactnessと像分解から肯定。
- degreewise compact Hausdorffで連続なテスト族：locally aleph_1-presentable。
- infinite 2-coskeletalな一般のテスト：上記の証明では決まらない。

sSetを反例候補から除外したわけでも、反例が存在すると示したわけでもない。

## 参考資料

R1. Riehl–Verityの内容に基づく infinity-cosmos blueprint, §1.2 Simplicial sets.
https://emilyriehl.github.io/infinity-cosmos/blueprint/sec-simplicial-sets.html
特にnerveの充満忠実性、2-coskeletality、categorification。

R2. Mathlib, AlgebraicTopology.SimplicialSet.NerveAdjunction.
https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicTopology/SimplicialSet/NerveAdjunction.html

R3. Stacks Project, Lemma 14.19.10 (Tag 018B), Coskeleton functors.
https://stacks.math.columbia.edu/tag/018B

R4. Cox–Feigert–Kamsma–Mazari-Armida–Rosický, Cofibrant generation of pure monomorphisms in presheaf categories.
https://arxiv.org/html/2506.20278v2
本ノートで使うのはpresheafの多ソートunary algebraとしての表示、purityの有限方程式による定義、presentabilityのサイズ基準。

R5. Casacuberta–Gutiérrez, Homotopy reflectivity is equivalent to the weak Vopěnka principle.
https://arxiv.org/html/2410.21244

R6. Chorny, Abstract cellularization as a cellularization with respect to a set of objects.
https://math.haifa.ac.il/chorny/publications/Chorny%20-%20Cellularization.pdf

R7. Adámek–Rosický, Locally Presentable and Accessible Categories (1994), Theorem 1.46 and Open Problems, Problem 1.
