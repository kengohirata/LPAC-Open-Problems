# Problem 3：N の下での否定方向 — 真クラス個の強商の構成と generatedness の障害

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下の新しい直接議論を主担当が再構成・再点検した。独立査読、形式検証、文献上の新規性確認は未実施。No.3 の反例・ZFC 独立性は得ていない。**

ユーザーの依頼は、N＝「非可算可測基数が存在しない」などの強い否定側仮定の下で、No.3 を否定できないか実際に試すこと。本稿は単なる調査計画ではなく、試した構成と、その成立部分・失敗部分の証明を記す。

## 0. 結論

No.2 の採用済み入力「N の下で A_sigma は大域的に coreflective」を使うと、次の圏 K_0 を構成できる。

- K_0 は locally small かつ cocomplete。
- K_0 は **二対象からなる strong generator** を持つ。
- K_0 の **一つの固定対象からの strong epi quotients が真クラス個**ある。従って weakly co-wellpowered でなく、locally presentable でもない。
- しかし K_0 には **generated objects からなる strong generator は存在しない**。集合サイズの問題ではなく、generated objects 全体でも非同型射を検出できない。

従って K_0 は No.3 の反例ではない。最後の条件は未確認なのではなく、すべての正則無限基数に対する明示的な図式によって否定できる。

さらに、次の二つの広い転用経路を排除した。

(A) 局所可呈示圏の全小余極限で閉じた充満部分圏は、小さい strong generator を持てば既に locally presentable。従って No.1/2 の非 coreflective coorthogonality class をそのまま No.3 の反例にすることはできない。

(B) 前層圏の充満部分圏 C が ambient な集合個の copowers で閉じ、非初対象を含むなら、C^op の generated objects は strong generator を形成できない。これは ZFC の一般補題であり、N を V=L に強めても同じ構成は修復されない。

本稿は「否定側の構成に必要なサイズの病理」を strong quotient の意味で実現したが、「generated strong generator」と両立させられなかった、という結果である。

---

## 1. 使用する入力と、今回の依存範囲

Omega=omega、M=End_Set(Omega)、作用は左作用とする。

    F(X)=Omega^X,
    H(A)=Hom_M(A,Omega).

F(X) への作用は後合成。H(A) には離散 Omega の積 Omega^A の部分空間位相を入れる。

以下の三点を既存ノートから用いる。

1. **N の下での Isbell 評価表示**：任意の集合 X について

       X -> H(F(X)), x |-> ev_x

   は自然な全単射。これは集合としての表示であり、後で X に入れる Stone 位相まで同一視しない。

2. **ZFC のコンパクト双対**：有限支持 M-set A に対して H(A) は compact Hausdorff。Stone 空間 X に対し

       C(X)=Cont(X,Omega_disc)

   は有限支持で、評価 X -> H(C(X)) は同相。

3. **N の下での大域的 coreflectivity**：D=(M-Set)^(0⇉1) の充満部分圏

       C = A_sigma = {Z=(Z_0 --p_Z,q_Z--> Z_1) : H(p_Z) is bijective}

   の包含 I:C->D は右随伴 R を持つ。

入力1–2の直接証明：
`../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md` §§1,4。

入力3の全標的に対する証明：
`../No.2/sigma_coreflectivity_under_no_measurables_2026-11-16.md`。

**入力3は今回独立に全面再証明したものではない。既存の PROOF_RECONSTRUCTED の証明を採用している。** 従って以下の K_0 の構成も、その入力に依存するものとして扱う。他方、§6 の copower 障害は入力1–3にも N にも依存しない。

C は一本の固定テスト sigma に対する coorthogonality class なので、D のすべての小余極限で閉じる。sigma は

    (Omega^2 --pi_0,pi_1--> Omega) -> B=(Omega⇉1),
    sigma=(pi_0,!).

No.1 の非 coreflective なクラス A は C にさらに「Z_0 が有限支持」を課したものである。**C と A を混同しない。** C では第0成分に有限支持を要求しない。

---

## 2. 元の coorthogonality class をそのまま使う経路の排除

### 命題2.1（ZFC）

P を locally presentable、A をその全小余極限で閉じた充満部分圏とする。A が集合サイズの strong generator G を持てば A は locally presentable。

**証明。** G は P の対象の集合である。十分大きな共通の正則基数 mu を取り、各 G∈G を P において mu-presentable にできる。A の mu-directed colimits は P で計算され、A は充満なので、これらの G は A でも mu-presentable である。A は cocomplete かつ mu-presentable objects からなる small strong generator を持つため、locally mu-presentable。□

この最後の標準的特徴付けは Positselski–Rosicky (2018) の導入 p.253 でも明記されている。

### No.1/2 の A への帰結

A は ambient presheaf 圏の全小余極限で閉じる。もし小さい strong generator を持てば命題2.1により LP となる。LP 圏から LP 圏への余極限保存包含は右随伴を持つので、A は coreflective となる。N の下での既存の非 coreflectivity に反する。

従って N の下では **A は小さい strong generator 自体を持たない**。generatedness を別に調べれば解けるという前回の候補は、この一般論で排除できる。

---

## 3. 固定した T_* の強部分対象となる順序数族

### 3.1 対象と射

任意の無限基数 kappa を初期順序数と見なし、

    X_kappa=[0,kappa]

に順序位相を入れる。これは Stone 空間である。自己写像

    d_kappa(alpha)=alpha+1  (alpha<kappa),
    d_kappa(kappa)=kappa

は集合写像として使う。連続とは要求しない。

    Y_kappa=(C(X_kappa) --i,d_kappa^*--> F(X_kappa)),
    d_kappa^*(f)=f∘d_kappa

と置く。入力1–2により H(i) は全単射なので Y_kappa∈C。

s:omega->omega を s(n)=n+1 とし、固定した対象

    T_*=(F(omega) --id,s^*--> F(omega))

を取る。これは H(id) が全単射なので C に属する。

両成分の omega への制限によって

    a_kappa:Y_kappa -> T_*

を定める。p との可換性は自明で、q との可換性は d_kappa|omega=s による。

また

    t:T_* -> B=(Omega⇉1),    t=(ev_0,!)

とすると、

    t a_kappa = psi_kappa=(ev_0,!) : Y_kappa -> B.

T_*、B、sigma は kappa に依存しない。

### 3.2 C 内の epi は成分ごとに全射

入力3により I:C->D は左随伴なので epimorphisms を保存する。D は前層圏なので、その epi は成分ごとの全射である。

逆に、成分ごとに全射な C の射は D で epi、従って充満部分圏 C でも epi。

ここでは **coreflectivity を使っている**。単なる充満部分圏について同じ主張をしているわけではない。

### 補題3.3（quotient rigidity、ZFC+N および入力3）

e:Y_kappa->Z が C 内の epi で、ある b:Z->B が b e=psi_kappa を満たすなら、e は同型である。

**証明。** §3.2より e_0,e_1 は全射。従って Z_0 は有限支持 M-set の商として有限支持である。

    T=H(Z_0), S=H(Z_1),
    u=H(p_Z):S->T, v=H(q_Z):S->T

と置く。u は全単射なので k=v u^(-1):T->T を定められる。

e を双対化し、入力1–2による同定を使うと

    h=H(e_0):T->X_kappa,
    ell=H(e_1):S->X_kappa

を得る。h は連続である。自然性から

    h u=ell,   h v=d_kappa ell,

従って h k=d_kappa h。

T は compact、X_kappa は Hausdorff なので h(T) は閉である。また d_kappa-不変で、b_0∈T は h(b_0)=0 を満たす。

0 を含む閉 d_kappa-不変部分集合は X_kappa 全体である。実際、後続段階で d_kappa、極限段階で閉性を使う超限帰納法による。従って h は全射。

すなわち C(X_kappa) のすべての点評価が e_0 を経由する。点評価は関数を分離するので e_0 は単射でもあり、全射と合わせて同型である。

次に

    H(e_0) H(p_Z)=H(i) H(e_1)

の左辺と H(i) は全単射であるから H(e_1) も全単射。従って F(X_kappa) のすべての座標評価が e_1 を経由する。座標評価は F(X_kappa) の元を分離するので e_1 も単射、従って同型。

よって e は図式圏で同型であり、C は充満なので C でも同型。□

注意：h の全射性を得るまでは No.1 の因子化下界と同じ機構である。今回は e が epi なので、全射性からさらに e の同型性まで導ける。

### 定理3.4（a_kappa は C 内の strong mono）

任意の C 内の epi e:U->V と可換四角

    U --u--> Y_kappa
    | e         | a_kappa
    v           v
    V --v-->   T_*

を取る。C の pushout P=Y_kappa ⊔_U V を作り、包含を j:Y_kappa->P、k:V->P とする。j は epi の pushout なので epi である。

四角から w:P->T_* が誘導され、w j=a_kappa、w k=v。従って (t w)j=psi_kappa となる。補題3.3により j は同型。

    d=j^(-1)k:V->Y_kappa

と置けば de=u、a_kappa d=v。一意性は e の epimorphicity による。

したがって a_kappa はすべての epi に対して一意右持上げ性を持ち、strong mono である。□

この証明では、a_kappa が母圏 D で mono だとは仮定しない。実際、一般には成分ごとの単射ではない。

### 3.5 従来の psi_kappa との違い

No.1 の uniqueness class I_sigma 内では psi_kappa:Y_kappa->B は内部 mono だが、成分ごとに全射でもあるため epi でもある。非同型なので strong mono ではない。従って psi_kappa の双対は ordinary epi しか与えず、strong quotient の病理を得られない。

今回使うのは **別の標的 T_* と、別の部分圏 C=A_sigma における a_kappa** である。pushout と quotient rigidity によって strong mono まで強化したことが本質。

---

## 4. K_0=C^op：余完備・有限 strong generator・真クラス個の強商

入力3により C は complete。極限は D の極限に R を施して得られる。また C は D の全小余極限で閉じるため cocomplete。

    K_0=C^op

は locally small、complete、cocomplete である。

### 4.1 固定始域の強商が真クラス個

定理3.4を双対化して

    a_kappa^op:T_*^op -> Y_kappa^op

は K_0 の strong epi である。

Y_kappa の第1成分の濃度は omega^(|X_kappa|) で、kappa とともに集合基数で一様に抑えられない。同型な C-対象は D でも同型なので、その成分濃度も等しい。

従って T_*^op の strong quotient classes は集合ではない。つまり K_0 は weakly co-wellpowered でなく、locally presentable ではない。

全 kappa の濃度が対ごとに異なるとは要求していない。族全体が一つの集合基数で抑えられないことだけで十分である。

### 4.2 二つの strong generators

W=2^M を cofree M-set とする。作用は (n chi)(m)=chi(mn)。D の対象

    Q_0=(W⇉1),
    Q_1=(W×W --pi_0,pi_1--> W)

について

    Hom_D(Z,Q_i) ≅ Set(|Z_i|,2),   i=0,1

が自然に成立する。

集合写像 f に対して Set(f,2) が全単射なら f は全単射。従って Q_0,Q_1 は D の jointly conservative な cogenerator の族である。

随伴から

    Hom_C(Z,RQ_i) ≅ Hom_D(IZ,Q_i)

なので RQ_0,RQ_1 は C の strong cogenerator を形成する。よって

    (RQ_0)^op, (RQ_1)^op

は K_0 の二対象からなる strong generator である。

**ここまでで No.3 に近いが、generatedness は得られていない。以下で、単に未証明なのではなく不可能であることを示す。**

---

## 5. 固定始域 T_*^op 自身も generated ではない

任意の正則無限基数 lambda を取る。集合 I の濃度を lambda とし、J=[I]^(<lambda) を包含で順序付ける。J は lambda-directed。

D=T_* として、次節の記号 D・S=∐_{s∈S}D を使う。C 内で

    D・2^T -> D・2^S    (S⊆T⊆I, |T|<lambda)

をラベルの座標制限によって定める。この逆系の極限は D・2^I である。すべての遷移と射影は、ゼロ延長により split epi になる。

T_* の相異なる二自己射

    f_0=id,
    f_1=(s^*,s^*)

を取れる。後者は p=id と q=s^* に可換であり、恒等射ではない。

D・2^I -> T_* の各コピー上の値を、全零ラベルなら f_0、それ以外なら f_1 と定める。これはどの S∈J の射影も経由しない。S の外の一点だけ1のラベルと全零ラベルは、S に制限すると一致するが、二つのコピー上の射は f_0,f_1 と異なるからである。

反対圏に移れば、lambda-directed split-mono colimit への T_*^op からの射が、どの段階も経由しない例である。従って T_*^op はどの正則無限 lambda についても lambda-generated ではない。

「固定した対象から強商が真クラス個ある」だけでは、その対象が generated であることを保証しない。

---

## 6. 一般補題：copowers を保った双対化では generated strong generator を作れない

### 定理6.1（ZFC）

P を任意の前層圏、C⊂P を充満部分圏とする。各 D∈C と各集合 S に対し、P で計算した copower

    D・S = ∐_{s∈S}D

が C に属すると仮定する。

G∈C について、G^op が C^op で lambda-generated となる正則無限基数 lambda が一つでも存在するなら、G は C 内で subterminal、すなわち

    |Hom_C(D,G)|≤1   for all D∈C

である。

C が P の非初対象を一つ含めば、C^op の generated objects 全体は strong generator にならない。

### 証明：第一部

f_0≠f_1:D->G が存在すると仮定する。|I|=lambda とし、J=[I]^(<lambda) を取る。

    A_S=D・2^S,    S∈J

と置き、S⊆T に対して A_T->A_S を座標制限により定める。各射はゼロ延長による section を持つ。

P の各 sort d では A_S(d)=D(d)×2^S。この逆系の極限は

    A=D・2^I

である。実際、S=empty の成分が D(d) 座標を固定し、残りの互換なラベルが一つの I->2 を定める。これは構造射について自然なので P の極限である。

仮定により A∈C。C は充満なので同じ A と射影 pi_S:A->A_S は C の極限でもある。各 pi_S もゼロ延長により split epi。

従って反対圏では

    A^op = colim_{S∈J} A_S^op

は lambda-directed な split monomorphisms の余極限である。余極限の各 injection 自身も split mono である。このため、mono 図式だけでなく union 型を要求する読み方でも本例は使える。

copower の普遍性により、h:A->G を、ラベル x:I->2 のコピー上で

    h|_x = f_0   if x is identically zero,
           f_1   otherwise

と定める。

S∈J を任意に取る。j∈I\S を選び、x_0 を全零、x_j を j だけ1とする。この二つのコピー D->A は pi_S の後では等しいが、h の後では f_0,f_1 となる。従って h は pi_S を経由しない。

これは Hom_{C^op}(G^op,-) が上の lambda-directed mono colimit を保存しないことを意味する。矛盾。よって Hom_C(D,G) は高々一元である。□

### 証明：strong generator の不存在

P の非初対象 D∈C を取る。fold

    nabla:D⊔D -> D

は P で非同型なので、C でも非同型。その section により split epi である。

任意の generated G^op に対し、第一部により Q=Hom_C(D,G) は空集合または一元集合。従って

    Hom_C(nabla,G):Q -> Q×Q

は全単射である。

つまり C^op の非同型の split mono nabla^op を、すべての generated objects が同型として観測する。従って、それら全体でも strong generator にはならない。□

### 6.2 適用範囲

- C=A_sigma は前層圏 D の全余極限で閉じるため、定理の仮定を満たす。従って K_0 の生成対象を取り替えるだけでは修復できない。
- 任意の presheaf coorthogonality class や、全小余極限で閉じた充満部分圏の反対圏にも同じ障害がある。
- 固定 B 上の slice C/B を使うだけでも回避できない。C/B は presheaf 圏 P/B の充満部分圏で、同じ対象の copowers は再び C/B に残る。非初対象がある限り同じ cube が作れる。
- 証明は ZFC。N を V=L に強めても、この特定の copower-preserving dual construction は反例にならない。

ここから、任意の双対化・gluing・completion が不可能だとは結論しない。仮定は **前層圏への充満埋め込みと ambient copowers の閉性**である。これらを変える構成まで排除していない。

---

## 7. Set^op の Isbell 反射表示も、全ての基数で union 閉性に失敗する

N の下では F:Set^op->M-Set は充満反射埋め込みである。その像を L とする。

任意の正則無限 lambda、|I|=lambda に対し、S∈[I]^(<lambda) の図式

    F(2^S) -> F(2^T),  S⊆T,

を、2^T->2^S に沿う前合成で定める。これらは split monos である。

ambient union U を F(2^I) の中で取ると、

    U={f:2^I->Omega : f depends on fewer than lambda coordinates}.

全零点では0、その他では1となる関数は U に入らないので、U は真の部分対象。

一方、H は余極限を集合の極限に送るため、N の評価表示から

    H(U) ≅ lim_S H(F(2^S)) ≅ lim_S 2^S ≅ 2^I.

U の反射単位 U->F(H(U)) は、この同定の下で真の包含 U↪F(2^I) である。従って U は L に属さない。

よって L は、どの正則無限 lambda に関しても、ambient lambda-directed unions で閉じていない。これは No.3 の同値な反射部分圏による定式化の、まさに必要な仮定が失敗する例である。

lambda を大きくするだけでは修復できない。§6 の一般障害の、よく知られた反射表示における具体化として見ることができる。

---

## 8. epireflective な反例候補を調べた結果

### 命題8.1（ZFC）

K が前層圏 P の full reflective subcategory であり、すべての反射単位が P の epi なら、K は weakly co-wellpowered。

**証明。** まず K は P の部分対象で閉じる。B∈K と P の mono m:A->B を取り、反射単位 eta_A:A->LA を経由させると m=bar(m) eta_A。m が mono なので eta_A も mono。仮定により epi でもあり、P は balanced なので eta_A は同型。従って A∈K（同型閉に取る）。

次に K 内の strong epi e:X->Y を P で image factorization

    X -> Im_P(e) -> Y

する。Im_P(e) は Y の P-subobject なので K に属する。最後の射は K でも mono であり、e が strong epi なので同型。従って e は P の epi、すなわち成分ごとに全射である。

P の固定 X からの epi quotient classes は集合個。K は充満なので K の strong quotient classes も集合個。□

従って、この範囲で generated objects からなる small strong generator まで得られれば、標準の locally-generated theorem により LP となる。**前層圏の epireflective subcategory は No.3 の反例には使えない。**

### 8.2 文献の rigid graph 反例との照合

Positselski–Rosicky (2018), Theorem 3.6 は、¬VP の下で proper rigid class の connected graphs G_i から、epireflective で nearly locally finitely presentable だが LP でない圏を作る。しかし nearly presentable は generated とは異なる。

本構成で一頂点・辺なしの graph V が、どの lambda でも lambda-generated でないことを直接確認できる。

lambda より大きい G_i を選び、その <lambda サイズの部分グラフ全体を取る。これらは proper subgraphs なので、どの G_j からも射を受けない。そうでなければ G_j->G_i を得て、rigidity により j=i かつ合成が恒等となり、proper subgraph への因子化に矛盾する。従って全部、文献の反射部分圏に属する。

この lambda-directed mono diagram の ambient union は G_i だが、部分圏内の colimit は G_i の反射、すなわち一頂点一ループの終対象1になる。

    colim Hom(V,G_small) ≅ Vertices(G_i),
    Hom(V,colim_K G_small)=Hom(V,1) ≅ 1.

比較射が単射でないので V は lambda-generated でない。ここでは図式の遷移は mono だが、反射後の余極限 injection が mono でなくなる点が障害である。§6 の split-mono cube は、この挙動とは異なり、余極限 injection 自体も split mono のままで generatedness が失敗する。

文献の反例を「generated」版の反例と読み替えてはならない。N の下で No.3 を否定するという今回の目標に、Theorem 3.6 を直接転用していない。

---

## 9. 今回の正確な到達点と、残っている問題

No.3 の反例には、余完備性、小さい strong generator、その生成対象の generatedness、非 LP 性を同時に満たす必要がある。

今回の K_0 は、最初の二条件と非 LP 性を満たし、非 LP 性は固定対象の **strong** quotients の無界性で証明できた。しかし generatedness については、任意の生成族への取り替えを含めて不可能と分かった。

したがって次のいずれも今回の結論ではない。

- N⇒¬P3。
- V=L⇒¬P3。
- P3⇒可測基数の存在。
- No.3 の ZFC 独立性。
- P3 の ZFC での肯定。

今回、反例構成の障害は「巨大な強商を作れない」ではなく、「それを generated strong generator と両立できない」に移った。

今後、No.1/2 のデータを使い続ける場合、同じ対象の任意集合個の余積が前層圏でそのまま計算される構造を残して単に双対化する方法は避ける必要がある。候補は、copower cube の任意のラベル依存射を制限しつつ、余完備性と順序数族の strong quotient 性を残すように、射または余極限の計算を変更する構成である。ただし、そのような構成は本稿では与えていない。

---

## 10. 監査項目

- No.2 の A_sigma の global coreflectivity を独立検証済みとはしていない。既存の記録を入力にしている。
- coreflective な C と、非 coreflective な A=C∩{Z_0 finite support} を区別した。
- epi の成分ごとの全射性には I⊣R を使った。
- 入力の巨大な内部 mono を単に双対化したのではなく、別の a_kappa の strong mono 性を pushout で証明した。
- quotient rigidity で Z_0 の有限支持は、e_0 の全射性から導いた。任意の C-対象が有限支持だとは仮定していない。
- h の全射性は任意の因子化先に対する閉像・不変性から導いた。大きな試験対象の存在だけでは strong mono を結論していない。
- C の一般の極限は母圏で計算されるとは仮定していない。copower cube の極限についてだけ、ambient limit が C に属することを示した。
- copower cube では遷移だけでなく余極限 injection の反対射も split epi。mono-colimit の読み方による弱い例になっていない。
- 任意の正則無限 lambda に対して構成した。一つの基数での非 generatedness を、すべての基数での失敗にすり替えていない。
- 生成対象の候補二つが失敗するだけではなく、すべての generated objects が非同型の fold の反対射を見落とすことを証明した。
- finite strong generator と generated strong generator を区別した。
- finite computational checks を無限の証明の代わりに使っていない。
- 結果の新規性、外部査読、形式検証を主張しない。

## 11. 参照

ローカル入力：

- `../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md`：Isbell 評価表示、有限支持・コンパクト性、順序数試験対象と閉像不変性、従来の内部 mono。
- `../No.2/sigma_coreflectivity_under_no_measurables_2026-11-16.md`：C=A_sigma の大域的 coreflectivity（N の下、独立検証前の入力）。
- `positive_quotient_bounds_and_regular_towers_2026-11-17.md`：P3 の strong quotient smallness への還元。
- `cross_problem_reconnaissance_2026-11-17.md`：今回の調査前の候補一覧。本稿はその直接転用・双対化案に具体的な判定を与える。

一次文献：

- L. Positselski and J. Rosicky, Nearly Locally Presentable Categories, TAC 33(10), 2018, pp.253–264. 導入の LP/generated の特徴付け、Theorem 3.6 の epireflective な nearly-presentable 反例を確認。PDF の該当ページを画像でも確認した。
  https://tac.mta.ca/tac/volumes/33/10/33-10.pdf
- I. Di Liberti and J. Rosicky, Enriched Locally Generated Categories, TAC 38, 2022; arXiv:2009.10980v2. Definitions 2.1–2.3, Examples 2.8, Remark 2.27 の仮定の区別を確認。
  https://arxiv.org/pdf/2009.10980

この文献確認は 2026 年現在までの解決状況を網羅した調査ではない。§3–7 の直接議論を、これらの論文の既存定理として引用しているわけではない。
