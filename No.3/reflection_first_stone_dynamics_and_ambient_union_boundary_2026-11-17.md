# Problem 3：反射・union 保存を先に確保する構成の検査

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下は本セッションで直接展開し、主担当が再点検した議論である。独立査読・形式検証・文献上の新規性確認は未実施。No.3 の反例、ZFC 独立性、一般の肯定証明は得ていない。**

ユーザーが承認した方針：generatedness を後から付け足さず、まず presheaf 圏への full reflection と、ある固定 λ での mono の λ-directed colimit 保存を確保し、その中に既存の商の巨大化を移す。

## 0. 今回の結論

三つの具体的な修復を定義し、次を得た。

| 候補 | 反射 | 固定 λ の union 保存 / generatedness | 判定 |
|---|---|---|---|
| 両成分を Stone 双対にし、自己写像を連続にする R_cont | ZFC で明示 | 包含は全 filtered colimits を保存 | Boolean 代数と自己準同型の圏。局所有限表示可能 |
| 第0成分だけ Stone 双対、第1成分は任意の冪とする R_mix | N の下で明示 | 全ての λ で union 閉性が失敗。さらに generated objects 全体でも strong generator にならない | 反例から除外 |
| R_mix で一方の双対構造射を全単射にし、任意の不連続自己写像を残す R_disc | 不可能 | 可算積すら存在しない | 完備圏の反射部分圏にはなれない |

ここで N は非可算可測基数が存在しないこと。最後の二つの構造的障害は、それぞれの抽象的な Stone 空間の圏では ZFC の証明である。N はそれらを今回の M-set の full image と同定するために用いる。

加えて、次の一般的な判定補題を証明した。

> **前層圏上の自己関手 T が、ある κ に関して、任意の ambient な κ-directed mono diagram の colimit を保存するなら、T はある μ で accessible である。**

したがって、P3 の反例となる反射 L ⊣ E、T=EL では、

- 局所対象間の mono の λ-directed colimits は E が保存する一方、
- **任意の非局所な入力まで含む** mono の κ-directed colimits は、どの κ でも T がすべて保存することはできない。

この二条件は異なる。後者を証明してしまう構成は、反例ではなく肯定例になる。

---

## 1. 前回の排除補題の再点検

### 1.1 全余極限閉部分圏の直接転用

P が locally presentable、A⊂P が充満かつ全小余極限で閉じ、小さい strong generator G を持つとする。集合 G の全対象が P で共通の μ に関して presentable になるよう μ を取る。A の directed colimits は P で計算されるので、同じ対象は A でも μ-presentable である。cocomplete category の presentable strong generator による特徴付けから A は LP。

この議論では「全小余極限で閉じる」を使っており、単に余完備な充満部分圏や reflective subcategory に同じ結論を適用しない。

### 1.2 ambient copowers を保った反対圏

C⊂P が presheaf 圏の充満部分圏で、D∈C と集合 S に対し ambient copower D·S が C に残るとする。任意の正則無限 λ、|I|=λ に対する D·2^S、S∈[I]^{<λ} の逆系は、C 内でも D·2^I を極限に持つ。射影は split epi。

二射 f_0≠f_1:D→G を、全零ラベルでは f_0、それ以外では f_1 として貼ると、どの <λ 座標への射影も経由しない。従って G^op が generated なら G は C で subterminal。非初対象 D の fold D⊔D→D は全てのその G で検出できないため、generated objects 全体でも C^op を strong generate しない。

極限が C に存在すること、各射影まで split epi であること、全ての λ に量化していることを再確認した。この範囲で前回の補題は維持される。

今回の候補では、この copower 仮定を外すために Stone 空間の連続性を導入する。ただし、それだけで反射や generatedness が成立するとは扱わない。

---

## 2. 記号と有限支持の基本反射

Ω=ω、M=End_Set(Ω)、作用は左作用とする。

    F(E)=Ω^E,
    H(A)=Hom_M(A,Ω).

H(A) には離散 Ω の積 Ω^A の部分空間位相を入れる。有限支持 M-set の圏を S とする。

既存の No.2 ノートから、

    S ≃ Set^{FinSet_+}

を採用する。具体的には Ω^n (n≥1) が small projective generators で、

    Hom_M(Ω^n,A) ≅ A_[n]

は [n]={0,...,n-1} に支持される元の集合。全小余極限は underlying M-set で計算される。この presheaf 表示の直接証明は
`../No.2/no2_presheaf_presentation_Kfs_2026-11-17.md` にある。

Stone 空間 X に対し

    C(X)=Cont(X,Ω_disc)

とする。空空間も認める。C(X) は有限支持。既存のコンパクト双対補題により、A∈S なら H(A) は Stone 空間で、

    X → H(C(X)), x↦ev_x

は同相である。この部分は ZFC であり N を使わない。

### 補題2.1：Stone 双対像への反射（ZFC）

B⊂S を C(X) 全体の充満同型閉部分圏とする。B は reflective で、

    L_0(A)=C(H(A)),
    η_A(a)(h)=h(a)

が反射である。

**証明。** A∈S と Stone 空間 X に対し

    Hom_M(A,C(X)) ≅ Cont(X,H(A))

が自然に成立する。左辺の射 f は、x↦[a↦f(a)(x)] に送る。この写像は各 a 座標で連続なので連続。逆は評価による。

A=C(Y) の場合には H(C(Y))≅Y を使って

    Hom_M(C(Y),C(X)) ≅ Cont(X,Y)

となる。従って C は Stone^op を充満忠実に埋め込み、上の Hom 表示が反射の普遍性そのものである。η_A(a) は H(A) 上で連続で、a の有限支持によって有限個の値しか取らない。□

Stone 双対により B≃Bool。trivial Boolean algebra も含める。

### 補題2.2：B→S は全 filtered colimits を保存する（ZFC）

S の n 番目の nerve 成分で、

    C(X)_[n] = Cont(X,[n])
              ≅ Hom_Bool(P([n]),Clop(X)).

P([n]) は有限 Boolean algebra なので finitely presentable。従って各成分で filtered colimits を保存し、presheaf 表示から包含 B→S も保存する。□

ここで使ったのは有限対象 P([n]) の presentability であり、任意の M-set の generatedness を presentability と取り違えていない。

---

## 3. 第一候補：連続な Stone dynamics の反対圏

J=(0⇉1) とし、

    P_fin=S^J

を取る。これは **両成分に有限支持を課した** presheaf 圏で、以前の「第0成分だけ有限支持」の K_fs とは異なる。

R_cont を、同型を除いて

    (C(X) --id,d^*--> C(X))

の形を持つ対象の充満部分圏とする。X は Stone、d:X→X は連続で、d^*(f)=f∘d。

不変な定義では、両成分が B に属し、一方の構造射 p が同型であることを要求する。p を同型として正規化すると上の形になる。

### 3.1 反射の明示

まず L_0 を成分ごとに施し、Bool 内の平行二射

    p,q:A⇉B

に移す。

Bool で

    T(B)=∐_{n<ω}B_n

を取り、shift endomorphism t を i_n(b)↦i_(n+1)(b) で定める。これは B 上の free Boolean algebra with endomorphism である。

次の関係を含む最小の t-invariant Boolean congruence で割る：

    i_(n+1)(p(a)) = i_n(q(a)),    a∈A, n<ω.

得られた Boolean algebra を D、誘導された自己準同型を t と書く。反射先は

    (D --id,t--> D).

単位の第1成分は B→D の第0コピーへの写像、第0成分はその p との合成。

**普遍性。** (E --id,u--> E) への元の図式射は、f_1:B→E で

    u f_1 p = f_1 q

を満たすものと同値である。これを i_n(b)↦u^n f_1(b) によって T(B) から一意に延長でき、上の全ての関係を満たす。逆も同様。従って反射が存在する。□

### 3.2 fixed λ での union 保存を確保した

R_cont≃BoolEnd、すなわち Boolean algebra と Boolean endomorphism の圏。

BoolEnd→Bool は filtered colimits を作る。補題2.2より Bool≃B→S は filtered colimits を保存する。従って

    R_cont→P_fin

は **全 filtered colimits** を保存する。特に λ=ω を一度固定して mono の directed colimits を保存する。

presheaf の representables を反射すると finitely presentable objects からなる small strong generator を得る。

### 3.3 しかし R_cont は locally finitely presentable

BoolEnd は finitary operations

    ∧,∨,¬,0,1,t

と、Boolean identities および t が Boolean homomorphism であることを表す finitary equations の variety である。従って LFP。

これは「反射を作れなかった」例ではない。反射と union 保存の両方を通した候補が、具体的な finitary algebra の圏に同定された肯定例である。

### 3.4 epireflection / mono-preserving reflection による自明な除外ではない

この表示は前回の二つの十分条件に自動的に入るわけではない。

**単位が epi でない例。** A=Ω²⊔Ω²∈S とすると H(A)=2×2。L_0A=Ω^(2×2)。単位の像は、第一座標だけに依存する関数と第二座標だけに依存する関数の和である。XOR の関数は像に入らないので単位は epi でない。二つのコピーの定数関数は同一視されるので mono でもない。

**L_0 が mono を保存しない例。** Y={00,01,10} とし B=Ω^Y≅Ω³。A⊂B を、Y の第一座標だけ、または第二座標だけに依存する関数全体とする。二つの Ω² の交わりは定数関数 Ω だから

    A=Ω²⊔_ΩΩ²,
    H(A)=2×_1 2=4,
    H(B)=Y=3.

包含 A↪B に対する H の写像は Y↪2×2 であり、点11を欠く。従って

    L_0(A↪B):Ω⁴→Ω³

は座標制限であって mono でない。

A↦(A --id,id--> A) という対角図式にすれば、R_cont の反射でも同じ二つの現象が起こる。その反射は (L_0A --id,id--> L_0A) である。

### 3.5 旧順序数機構が失われる具体的な理由

連続な d:X→X と点 x に対し

    C_x=cl{d^n(x):n<ω}

は閉かつ d-invariant である。連続性より d(cl S)⊂cl d(S)⊂cl S。

C_x は countable dense subset を持つ Stone 空間。clopen 集合はその dense subset 上の値で決まるので |Clop(C_x)|≤2^aleph_0。clopen による点分離から

    |C_x|≤2^(2^aleph_0).

従って「一点を含む閉 d-invariant 部分集合は X 全体」という条件を使って、任意の κ の大きさを強制する旧構成は維持できない。種が集合 τ 個の場合にも、同じ議論で 2^(2^max(τ,aleph_0)) という集合上界がある。

これは連続性を持つ全ての圏が P3 の反例にならないという一般論ではない。今回の閉像・単一自己写像の機構への制限である。

---

## 4. 第二候補：Stone 頂点と集合としての辺

今度は以前の presheaf 圏

    P_mix=K_fs={Z_0⇉Z_1 : Z_0∈S, Z_1∈M-Set}

を使う。

N を仮定する。R_mix を次の対象の full replete image とする：

    (C(X) --s^*,t^*--> F(E)),

X は Stone、E は集合、s,t:E→|X| は任意の集合写像で、s^*(f)=f∘s 等。

Isbell の評価表示

    E≅H(F(E))

により、R_mix^op は次の圏 TGraph と同値になる。

- 対象：Stone 空間 X、集合 E、s,t:E→|X|。
- 射：連続な頂点写像と集合としての辺写像で、s,t と可換なもの。

辺には位相を課さない。従って端点写像 s,t の連続性も要求しない。

### 4.1 反射は明示できる（N）

Z=(Z_0⇉Z_1) に対し

    RZ=(C(H(Z_0)) ⇉ F(H(Z_1)))

とする。H(Z_0) には Stone 位相を使い、H(Z_1) は集合として使う。構造射は

    p_R(f)(h)=f(h∘p_Z),
    q_R(f)(h)=f(h∘q_Z).

単位は各成分の評価射。第0成分が C(H(Z_0)) に入るのは有限支持による。

**普遍性。** Z→(C(X)⇉F(E)) の第0成分は連続写像 u:X→H(Z_0)、第1成分は集合写像 v:E→H(Z_1) と同値。自然性は

    H(p_Z)v=us,
    H(q_Z)v=ut

である。C と F の充満忠実性によって、u,v は RZ からの一意な図式射を与える。ここで F の充満忠実性に N を使う。□

### 4.2 全ての λ で ambient union 閉性が失敗する

正則無限 λ、|I|=λ とし、S∈[I]^{<λ} に対して

    Z_S=(Ω --Δ,Δ--> F(2^S))

を取る。これは X が一頂点、E=2^S の R_mix-対象。

S⊂T の構造射は id_Ω と、2^T→2^S に沿う前合成。split mono であり、ambient union は

    Z=(Ω⇉U),
    U={f:2^I→Ω : f は <λ 個の座標のみに依存する}.

全零ラベルで0、それ以外で1という関数は U に入らず、U⊊F(2^I)。

H は colimits を limits に送るので、N の下で

    H(U)=lim_S H(F(2^S))≅lim_S 2^S≅2^I.

従って反射単位の第1成分は真の包含 U↪F(2^I)。Z は R_mix に属さない。

λ は任意なので、λ を大きくする修復では足りない。

### 4.3 別の生成族への取り替えも不可能：平行辺の cube

以下は TGraph についての ZFC の主張。

**補題4.3。** G=(X,E,s,t) に対し G^op が TGraph^op である λ について generated なら、各 x,y∈X に対し

    E_(x,y)={e:s(e)=x,t(e)=y}

は高々一元である。

**証明。** 同じ端点を持つ相異なる e_0,e_1 があるとする。D_S を、頂点が離散二点 {0,1}、辺集合が 2^S で、全辺が0から1へ向かう graph とする。辺ラベルの制限による逆系の極限は D_I。各遷移・極限射影は、頂点を固定し辺ラベルをゼロ延長することで split epi。

D_I→G を頂点では0↦x、1↦y、辺では全零ラベルを e_0、それ以外を e_1 に送って作る。頂点写像は離散有限空間からの写像なので連続。この射はどの <λ 座標の射影も経由しない。

従って G^op は λ-generated でない。λ は任意である。□

B_1 を二頂点と一本の0→1辺、B_2 を同じ頂点と二本の平行辺からなる graph とし、c:B_2→B_1 を辺を潰す射とする。これは非同型な split epi。

上の必要条件を満たす全ての G について

    Hom_TGraph(c,G):Hom(B_1,G)→Hom(B_2,G)

は全単射。二本の辺の像は同じ端点を持つため、一致しなければならないからである。

従って generated objects 全体でも c^op の非同型性を検出できず、TGraph^op の strong generator にはならない。

**これは R_mix の特定の反射表示で union が失敗するだけでなく、圏自身が No.3 の仮定を満たさないことの証明である。** ambient copowers の閉性は仮定していない。

なお、R_mix は旧 Y_kappa を含むが、以前の固定標的 T_* の第0成分 F(ω) は有限支持でないため、この R_mix に以前の strong quotient の定理がそのまま残るとは主張しない。

---

## 5. 第三候補：不連続 dynamics をそのまま残すと、可算積が存在しない

R_mix で s:E→|X| が全単射という条件を加え、E=|X|、s=id と正規化する。対象は

    (C(X) --i,d^*--> F(|X|)),

ただし d:X→X は任意の集合写像である。この full image を R_disc と書く。

N の下で

    R_disc≃Dyn_Stone^op,

ここで Dyn_Stone の対象は Stone 空間と任意の集合自己写像、射は連続な equivariant map。

実際、第一成分の射は連続写像 f:X'→X、第二成分の射は集合写像 g:X'→X に対応し、i との自然性が g=f を要求する。もう一つの自然性が自己写像との可換性になる。

Dyn_Stone は全小極限を持つ。Stone で極限を取り、その underlying set に座標ごとの自己写像を入れればよい。従って R_disc は余完備である。しかし次が成り立つ。

### 定理5.1（ZFC）：Dyn_Stone には、一点固定系の可算余積が存在しない

E=(1,id) とし、仮に E の可算個の余積 Q があるとする。余積射で選ばれる点 q_n∈Q は自己写像の固定点である。

|Q| より大きい無限初期順序数 κ>ω を取り、X_κ=[0,κ] に順序位相を入れる。次の自己写像を使う：

    d_κ(n)=n                    (n<ω),
    d_κ(α)=α+1                  (ω≤α<κ),
    d_κ(κ)=κ.

**以前の順序数例とは異なり、有限点は固定している。** これによって各 n への射 E→X_κ が dynamics の射になる。

余積の普遍性から、それらを一度に延長する連続 equivariant map

    f:Q→X_κ,   f(q_n)=n

がある。

f(Q) はコンパクトから Hausdorff への連続像なので閉であり、equivariance により d_κ-invariant。全ての自然数を含むので閉性から ω を含む。そこから、後続段では d_κ、極限段では閉性を使う超限帰納法により、全ての [ω,κ] を含む。従って f は全射。

これは |Q|≥κ を意味し、κ の選択に反する。□

同じ証明は「可算個の E に対する cocone の弱初集合」の不存在まで与える。候補の集合の台集合濃度を一つの κ で上回ればよい。

### 帰結

R_disc は可算積を持たない。従って、今回の P_mix に限らず、**いかなる完備圏の full reflective subcategory とも同値にはなれない**。

これにより、parallel-edge cube を s の全単射性で排除する修復は、反射の段階で失敗する。

この不可能性の証明は Dyn_Stone において ZFC であり、N を V=L に強めても同じ圏は修復されない。ただし、射や対象を別の方法で制限する全ての構成まで排除しているわけではない。

---

## 6. 一般補題：ambient な mono-colimit 保存は accessibility を強制する

前の三候補と独立の ZFC の議論である。ここでの仮定は、局所対象だけでなく **前層圏の全対象** の mono diagram に量化する。

### 定理6.1

P=Set^{D^op} とし、D は小圏。F:P→Set が、ある正則無限 κ に対して、κ-directed な monomorphisms の図式の colimit を保存するとする。

正則 μ≥κ かつ |Mor D|<μ を取れば、F は μ-directed colimits を保存する。さらに同じ証明で μ-filtered colimits を保存する。特に F は accessible。

**F 自身が monos を保存するとは仮定しない。** 一方、単に「各元は小さい部分対象から来る」とする boundedness よりは強い保存仮定を用いる。

### 6.2 小さい部分前層

前層 X の大きさを全成分の台集合の非交和の濃度とする。サイズ <μ の部分前層の poset Sub_<μ(X) は μ-directed で、その union は X である。

任意の <μ 個の元を構造射で閉じても、μ の正則性と |Mor D|<μ によりサイズ <μ。したがって、上の union が X 全体になる。

サイズ <μ の前層 A は μ-presentable。射 A→colim X_i を指定・照合するための元と自然性等式は <μ 個であり、μ-filtered 性によって一つの段階に揃えられる。

μ-directed なら κ-directed でもあるので、F の仮定をこの部分対象表示に適用できる：

    F(X)≅colim_(A∈Sub_<μ(X)) F(A).

ここで得るのは元の小さい支持だけでなく、**F(A) の元の等式も、より大きい小部分対象で既に成立する**という事実である。

### 6.3 任意の μ-directed colimit についての全射性

X=colim_i X_i を任意の μ-directed diagram とする。遷移は mono と仮定しない。

x∈F(X) を取る。上の表示から小さい A⊂X と a∈F(A) があり、a の像が x である。A は μ-presentable なので、A→X はある X_i を経由する。従って x は F(X_i) から来る。

### 6.4 任意の μ-directed colimit についての単射性

x_i∈F(X_i)、y_j∈F(X_j) が F(X) で同じ元に送られるとする。

小部分前層 A_i⊂X_i、A_j⊂X_j と、その上の代表元 a,b を取る。A_i,A_j の X における像はサイズ <μ。両方を含む小部分前層 B⊂X を取る。

a,b を F(B) に送ると、その二つの像は F(X) で一致する。6.2 の **等式の検出** により、ある小部分前層 C⊂X、B⊂C において既に一致する。

C は μ-presentable なので C→X はある X_k を経由する。A_i→X は、X_i 経由の射と C→X_k 経由の射で同じである。A_i の μ-presentability によって、十分後の段階でこの二つの射は一致する。A_j についても同様。共通の後続段階 X_l を取ると、F(C) 内の等式が F(X_l) に移り、x_i と y_j の像は一致する。

従って colim_i F(X_i)→F(X) は単射でもあり、全単射となる。μ-filtered な一般の添字圏でも、有限個の添字・射を共通 cocone に揃える同じ議論でよい。□

### 系6.5：前層圏上の自己関手

T:P→P が仮定を満たすなら、各評価関手 ev_d と合成して定理6.1を適用する。μ は D と κ だけから選べるので、全ての成分で同じ μ を使え、T は μ-accessible。

### 系6.6：反射モナドについて

L:P⇄K:E、L⊣E、E fully faithful とし T=EL。もし T がある κ の ambient mono-directed colimits を保存すれば、K は LP。

**証明。** 系6.5により T はある μ の filtered colimits を保存する。局所対象の μ-filtered diagram を P で余極限すると、その単位は各段階の同型な単位の colimit になり、再び同型。従って余極限は局所対象であり、E はその余極限を保存する。

P の representables を L で反射した集合は K の strong generator である。E が μ-filtered colimits を保存するので、各 L(y d) は μ-presentable。K は反射によって cocomplete だから、presentable strong generator の特徴付けにより LP。□

### 6.7 P3 に対する意味と、未証明の橋

P3 の反例に必要なのは

    (Local unions)
    E は、K の対象からなる mono の λ-directed diagram の colimit を保存する

である。これに対し、系6.6 が排除するのは

    (Ambient unions)
    T=EL は、P の任意の対象からなる mono の κ-directed diagram の colimit を保存する

という強い条件である。

後者を前者から推論してはいけない。ambient mono A→B を L で反射した LA→LB は一般には mono でない。そのため、ambient mono diagram を反射しても Local unions の仮定を適用できない。

従って、反例があるとすれば、Local unions は一つの固定 λ で成り立ちながら、Ambient unions は全ての κ で失敗しなければならない。

逆に、この二つを結ぶ追加の原理を P3 の仮定だけから導ければ、肯定証明になる。しかし本稿ではその橋は得ていない。

---

## 7. 成果の範囲と次の未解決点

今回実際に構成した「反射＋fixed union 保存」の候補 R_cont は LFP であり、反例ではなかった。ただし、反射が epi でも mono-preserving でもない例まで具体的に通した。

不連続性を残した R_mix は反射を持つが、すべての λ の cube が残り、generated objects 全体でも強生成できない。さらに一方の構造写像を全単射にして cube を除く R_disc は、今度は可算積を失う。

したがって、旧 No.1 の機構の次の二つの直接修復は排除された：

- 両成分の compact duality により連続化して反射と union を得るが、無界性を失う。
- 任意の不連続 dynamics を残すが、それらを全て含む連続 equivariant map の圏では、可算個の固定点からさえ無界な閉不変像が生じ、必要な積が存在しない。

新しい候補は、単に「有限支持を増やす」または「p を可逆にする」だけでは足りない。また反射モナド全体を directed unions で連続にすると、系6.6で LP に戻る。

**No.3 の否定、P3 から巨大基数を導く含意、一般の ZFC 肯定はすべて未確立。** No.1/2 の独立性からこれらを推論しない。

---

## 8. 仮定と監査ポイント

- §§2–3、Dyn_Stone の可算余積の不存在、TGraph の generatedness 障害、§6 は ZFC の直接議論。
- N は §§4–5 で F(E) の充満忠実性、H(F(E))=E、M-set 内の full image の同定に用いる。
- No.2 の A_sigma の大域的 coreflectivity は今回の新証明の入力にしていない。前回の K_0 の成立を再査読したとは主張しない。
- S の presheaf 表示、有限支持の H のコンパクト性、Stone の評価同相は既存の明示的補題を採用した。新しい反射の Hom 計算は本文で展開した。
- R_cont の ambient P_fin は両成分有限支持、R_mix の ambient P_mix は第0成分だけ有限支持。混同していない。
- R_cont の p は実際の同型、R_disc の p=i は通常の M-set の同型でなく H(p) が全単射。ここを同一視しない。
- continuous d と任意の集合写像 d を区別した。可算余積の不存在の d_κ は有限点を固定するため、旧 d_κ と同じ記号でも式は異なる。
- 「具体的な union が局所でない」と「圏自身が generated strong generator を持たない」は異なる。R_mix では後者を平行辺の fold で別途証明した。
- R_disc の obstruction は intrinsic な countable product の不存在。単なる ambient product 閉性の失敗ではない。
- §6 の accessible functor 判定には **元の支持と等式の検出の両方**を使う。元の小さい支持だけから injectivity を推論していない。
- §6 の μ は presheaf 基底の全射の数を上回る。λ=ω のままを無条件に主張していない。
- 有限モデルの実験から無限の結果を推論していない。新規性、第三者査読、形式証明は主張しない。

## 9. 参照と文献との関係

ローカル入力：

- `negative_trials_strong_quotients_and_copower_obstruction_2026-11-17.md`：前回の二つの排除補題と巨大強商。
- `positive_quotient_bounds_and_regular_towers_2026-11-17.md`：P3 の presheaf 反射表示と strong quotient bounds への還元。
- `../No.2/no2_presheaf_presentation_Kfs_2026-11-17.md`：有限支持作用の presheaf 表示と第0成分だけ有限支持の図式圏。
- `../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md`：H(C(X))、有限支持のコンパクト性、N の評価表示。

一次資料：

1. L. Positselski and J. Rosický, *Nearly Locally Presentable Categories*, TAC 33 (2018), 253–264.
   https://tac.mta.ca/tac/volumes/33/10/33-10.pdf
   presentable strong generator の特徴付け、generated / nearly presentable の区別、Problem 3 の位置づけを参照。今回 PDF screenshot はタイムアウトし、本文抽出を使用した。以前のセッションでの確認と今回の画像取得成功を混同しない。

2. I. Di Liberti and J. Rosický, *Enriched Locally Generated Categories*, TAC 38 (2022), 661–683; arXiv:2009.10980v2.
   https://arxiv.org/pdf/2009.10980
   Theorem 2.24、Theorem 2.26、Remark 2.27 の周辺を本文と当該 PDF ページ画像で確認。小ささと factorization system の仮定を落として P3 を結論する使い方はしていない。

3. J. Adámek, S. Milius, L. Sousa, T. Wißmann, *On Finitary Functors*, TAC 34 (2019), 1134–1164.
   https://tac.mta.ca/tac/volumes/34/35/34-35.pdf
   https://tac.mta.ca/tac/volumes/34/35/34-35abs.html
   boundedness と finitarity / accessibility の関係、mono 保存の役割を確認。Theorem 3.4 周辺を PDF ページ画像でも確認。
   **本稿§6は、単なる boundedness でなく mono-directed colimits の実際の保存を仮定する。従って同論文の一般定理から mono 保存仮定を勝手に削除したものではない。** 本稿の直接証明には filtered colimit での等式の検出が含まれる。

文献調査は 2026 年現在までの P3 の解決状況を網羅するものではない。新しい直接議論の妥当性と、その文献上の新規性は区別する。
