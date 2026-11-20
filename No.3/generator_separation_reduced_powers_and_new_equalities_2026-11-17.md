# No.3: 生成対象からの二射の分離、reduced powers、反射で新たに生じる等式

2026-11-17。

**状態: PROOF_RECONSTRUCTED。前段階の二補題を主担当が再点検し、以下の直接証明と対照例を展開した。独立査読・形式検証・新規性確認は未実施。一般の P3 の肯定、反例、巨大基数による新しい一般上界は得ていない。**

依頼は、(i) pure inclusion の fixed-domain split-extension 表示と ultrafilter による整合化を監査し、(ii) retraction 全体ではなく生成対象からの二射の分離を、特に pure inclusion を反射した特殊図式で調べること。

## 0. 到達点

1. 前ノートの pure inclusion の分解と、FC(kappa,theta) による fixed-domain retraction 構成は、記載された仮定の下で維持できる。
2. ultrafilter の値域を X 自体から任意の局所対象 D に変えられる。十分小さい D への任意の射 X->D を colimit へ延長でき、D が二射を分離すればその二射は colimit でも分離される。
3. しかし『生成対象からの二射は常に一様に小さい局所対象への射で区別できる』は Grp でも偽。任意に大きい finitary alternating simple groups が反例を与える。生成対象は Z 一つでよい。
4. 個別の retractions を元の対象へ整合化せず、tail filter による reduced power に送れば、ZFC で整合的な cocone が作れる。これは古典的な pure/reduced-power の機構であり、Hébert (2004), Theorem 2.4(a) の証明との対応を確認した。新手法としての新規性は主張しない。
5. 特殊な pure inclusion i:A->EB では、この構成を反射前に行えて、EB->Red_F(A) と、反射後の B->L Red_F(A) を得る。従って i^#:LA->B による二射の消失は、L(delta_A):LA->L Red_F(A) での消失も引き起こす。ただし逆は成り立つと主張しない。
6. 元の union 保存と generatedness は、eventual-equality relation を局所対象にし、その relation に既に属する G-始域の二射を一つの filter 段階で検出するために実際に使える。
7. 残りは、その relation を K で coequalize した際に新たに生じる等式。特に constant families 上で新しい等式が生じないことが必要になる。
8. この最後の現象は実在する。任意の正則無限 kappa に対し、**二つの finitely generated strong generators を持ち、全 directed unions を保存する LP な反射部分圏**で、kappa-complete tail filter による reduced power の反射が二つの定数を同一視する例を作った。同じ例で RP は全基数で成立する。従って fixed-rank CS/reduced-power テストは、特殊な local-target purity の問題より強くなり得る。

今回は『二射だけに絞れば値域のサイズ問題が自動的に消える』という見込みを、そのまま証明にはできなかった。生成性で検出できる既存の等式と、反射が付け加える等式を明確に分離し、単純な一様化を二つの対照例で排除した。

---

## 1. 設定

K は No.3 の前提を満たす。集合 G は lambda-generated objects からなる strong generator。既存の還元により

    L : P = Set^(D^op) <-> K : E,    L ⊣ E

を固定する。E は fully faithful、small limits を保存し、lambda-directed mono diagrams の colimits を保存する。局所対象とは E の本質的像。

K は complete、cocomplete、well-powered。presheaf の大きさは全 sort の台集合の非交和の濃度で測る。

H は G の <lambda 個の余積からなる集合。既存の強商の上界判定

    K is LP iff each H∈H has a set of strong quotients

を入力として保持する。これを今回あらためて証明したとはしない。

monicity は G からの二射で検査できる。s:X->Y が非 monic なら、G∈G と u≠v:G->X で su=sv となるものがある。これは G が generator であることによる。

---

## 2. 二つの核心補題の監査

### 2.1 pure inclusion の分解

正則 kappa>|Mor D| と、ambient kappa-pure mono i:A⊂EB を取る。J=Sub_<kappa(EB) とし、C∈J に

    B_C=A∪C,    a_C:A->B_C

を対応させる。

C∩A と C は kappa-presentable。purity は、可換四角

    C∩A -> A
      |      |i
      C  ->  EB

に対して、C∩A 上で inclusion と一致する r_C:C->A を与える。pure lifting では i r_C が元の C->EB と一致する必要はないが、貼り合わせには C∩A 上の一致だけで十分。

presheaf の union は intersection に沿う pushout なので、r_C と id_A を貼り合わせて rho_C:B_C->A を得る。rho_C a_C=id_A。

J は kappa-directed、B_C の union は EB。反射すると s_C=L(a_C):LA->L(B_C) は split mono、colimit は B。

**維持する区別:** s_C は split mono だが、L(B_C)->L(B_C') は mono とは限らない。rho_C の整合性も保証されない。

### 2.2 ultrafilter の整合化

kappa-directed poset I 上の図式 Y_i、固定始域 X からの split monos s_i:X->Y_i、遷移 f_ij s_i=s_j を取る。各 retraction r_i を選ぶ。

I の tails が生成する filter は kappa-complete。FC(kappa,theta) と各 |EX(d)|<theta により theta-complete ultrafilter U に延長できる。

a∈EY_i(d) に対して j>=i 上の E(r_j f_ij)(a) の値域は theta 未満。U の完備性により一つの値を選べる。有限個の等式に対する U-large sets の交叉から自然性・整合性・t_i s_i=id_X が従う。

空 sort では EX(d)=empty なら retraction の存在から EY_i(d)=empty なので問題はない。tail の外の値は使用せず、または非空 sort で任意に補う。

**監査結果:** この証明のサイズ仮定は、U に沿う値を既存の X の中に選ぶために使われる。生成対象 G が小さいことから、この値域まで小さいとは結論できない。

標準的な pure morphism の定義・left-cancellation・split mono の directed-colimit 閉性は Positselski (2026), §3 と照合した。本稿2.1は presheaf の union を使った直接証明。

---

## 3. 局所対象 D を観測先にする正しい弱化

### 命題3.1

上の split-extension 図式と s:X->Y=colim_i Y_i を考える。D∈K と全 sort について |ED(d)|<theta を満たす theta を取る。

FC(kappa,theta) の下で、任意の h:X->D はある t:Y->D に延長できる:

    t s=h.

**証明。** 2.2の値を r_j f_ij ではなく h r_j f_ij に置き換える。値域は ED(d) なので同じ ultrafilter の選択ができる。得る t_i:Y_i->D は整合的で t_i s_i=h。colimit の普遍性から t を得る。□

従って hu≠hv となる h があれば su≠sv。必要なのは X 全体への retraction ではなく、その二射を分離する一つの適切な D への延長である。

### 3.2 一様に小さい D があるという仮定の強さ

各 G∈G に基数 b_G があり、全 X と u≠v:G->X を、||ED||<=b_G の局所対象 D への h:X->D で分離できると仮定する。

各 b_G 以下の局所対象の代表は集合個であり、その G 全体での和も集合。これらは K の cogenerating set となる。任意の異なる二射 f,g:Z->X を、まず G->Z により区別し、その後 h で区別すればよい。

この追加仮定を得られれば、実は巨大基数を使う前に、K の co-wellpoweredness が ZFC で従う。

固定 H と ordinary epi e:H->B に対し、各 cogenerator D への Hom(B,D) は Hom(H,D) に前合成で単射。従って、それらを部分集合 S_D⊂Hom(H,D) と見なせる。評価射

    B -> product_D D^(S_D)

は mono。可能な族 (S_D) は集合個であり、その各 product は K の対象。well-poweredness により、それぞれの subobjects は集合個。ゆえに B と e は同型を除いて集合個。

したがって『一様に小さい局所観測先』は有用な追加仮定ではあるが、生成性だけから当然に出るものではない。

### 3.3 Grp における反例

G=Z を取る。任意の基数 b に対して濃度 tau>b の無限集合 Omega を選び、X=Alt_fin(Omega) とする。|X|=tau で X は simple。

簡単な確認: 非自明な normal subgroup N の非単位元 g を一つ取る。g の support と任意の指定された有限集合を含む有限 T（|T|>=5）に対し、N∩Alt(T) は非自明 normal subgroup。有限 alternating group の simplicity により Alt(T)⊂N。全ての3-cyclesが N に入り、N=X。

u,v:Z->X を、生成元1をそれぞれ単位元と一つの非自明3-cycleに送る射とする。|D|<=b の群 D への h:X->D は trivial。非trivialなら simplicity により injective となり濃度に矛盾する。

従って hu=hv は全てのそのような D について成り立つ。

Grp は既知の LFP 圏で、Z は finitely presentable strong generator。それでも b を G だけから一様に取れない。『二つの値なので2値観測へ圧縮すればよい』も、2値関数が K の射である保証を欠く。

この例は、二射分離そのものが不可能という主張ではない。小さい局所対象への射による一様な分離という、特定の手法を否定する。

---

## 4. ZFC による整合的 cocone: reduced power に送る

この節では K が small products と small colimits を持つだけでよい。

### 4.1 categorical reduced power

I は非空集合、F は I 上の proper filter。F を reverse inclusion で順序付け、

    Q_F^K(X)=colim_(S∈F, reverse inclusion) X^S

と定める。遷移は restriction projections。constant families による diagonal

    delta_F^K:X->Q_F^K(X)

がある。F が kappa-complete ならこの添字 poset は kappa-directed。各 X->X^S は S の一点での評価で split する。

これは通常の categorical reduced-power construction であり、新しい定義ではない。

### 4.2 任意の fixed-domain split-extension からの射

kappa-directed I と s_i:X->Y_i、retractions r_i:Y_i->X を取る。tail I_i={j:j>=i}、F=tail filter とする。

    b_i:Y_i -> X^(I_i),
    (b_i)_j=r_j f_ij.

i<=k について、b_k f_ik と b_i の restriction to I_k は一致する。従って Q_F^K(X) への射は cocone となり、

    b:Y=colim_i Y_i -> Q_F^K(X)

が存在して

    b s=delta_F^K

を満たす。

**これは ZFC であり、ultrafilter の存在も値域の濃度上界も不要。** 元の X に値を戻す代わりに、尾部での値の族をそのまま残す。

従って delta_F^K が u,v:G->X を分離すれば s も分離する。

### 4.3 CS と reduced-power diagonal の関係

(Diag_kappa): 全 X と全 proper kappa-complete filters F に対し delta_F^K が mono。

すると

    CS_kappa iff Diag_kappa.

CS=>Diag は X->X^S の図式に適用するだけ。逆は4.2と monicity による。

この同値だけを一般肯定の前進とは数えない。利点は、任意の遷移を持つ図式の問題が、product projections だけからなる特定の図式に移ること。

Hébert (2004), Theorem 2.4(a) の証明には、pure/algebraically closed morphism を tail-filter reduced power への射に延長する同じ機構がある。同論文の LP 前提を K に無条件で適用せず、ここでは4.2を直接示した。

---

## 5. 特殊な pure inclusion では、反射前の A を使える

i:A⊂EB と B_C=A∪C、rho_C:B_C->A は2.1のものとする。

4.2の construction を ambient presheaf 圏 P 内で行う。J=Sub_<kappa(EB) の tail filter F を用いれば

    b:EB -> Red_F^P(A),
    b i=delta_A:A->Red_F^P(A)

を得る。

L を施すと

    r=i^#:LA->B,
    gamma=L(b):B->L Red_F^P(A),
    gamma r=L(delta_A).

従って、G∈G と u≠v:G->LA について r u=r v なら

    L(delta_A)u=L(delta_A)v.

**注意:** 逆向きは成り立つと主張しない。gamma 自身が二射を潰す可能性がある。L(delta_A) の monicity は r の monicity への十分条件にすぎない。

本構成では target reduced power を ELA ではなく A で作る。これにより、compactness で元の値域へ戻す場合も、||ELA|| でなく A の各 sort のサイズを超える完備性で足りる。しかし標準の kappa-pure hull のサイズは通常 kappa 以上で、FC(kappa,theta) に必要な |A(d)|<theta を自動で満たさない。

### 5.1 小さい pure hull を compactness cardinal 未満に取る近道も自動ではない

P を quiver presheaves、B を少なくとも kappa 個の頂点を持つ loopless complete directed graph とする。kappa は正則無限 limit cardinal（強コンパクト基数等の場合を含む）。

kappa-pure A⊂B は、各 cardinal alpha<kappa に対して alpha 頂点の loopless complete graph からの射を受ける。0->complete_graph(alpha) に purity を適用すればよい。始域・終域は kappa-presentable。

loopless な graph へのこの射は頂点上単射なので、|V(A)|>=alpha for all alpha<kappa、従って |V(A)|>=kappa。

これは既に LP な presheaf 圏の例であり、P3 の否定ではない。しかし『pure hull を必ず compactness cardinal 未満に取る』という一般的修復はできない。regular successor の場合に同じ >=kappa を無条件に主張してはいけない。

### 5.2 固定 H による強商の特殊性

q:H->B strong epi、Im(Eq)⊂A の場合 r は strong epi。したがって r が mono なら同型。

既存の非LP必要条件を用いると、非LPであれば同じ固定 H から、任意に高い purity rank の i と nonmonic r を得られる。今回の5節により、その nonmonicity は L(delta_A) の generator-pair failure を伴う。

G が集合なので、さらに一つの G_* を選び、任意に高い purity rank で G_* からの二射による failure を得られる。正確には、各 G の failure ranks が全て有界なら、集合個の上界をまとめて全failure ranksを抑えられてしまう。よって一つの G の failure ranks が unbounded。任意の指定 rank に対してそれ以上のrankの証人を取れる。

この最後の選び直しでは、A のサイズが元の指定rankだけの以前の明示式に収まるとは主張しない。高いrankの証人を使うからである。

---

## 6. generatedness が実際に効く箇所: eventual-equality relation

再び X∈K と、集合 I 上の proper kappa-complete filter F を取る。kappa>=lambda とする。

P_X=X^I、pi_S:P_X->X^S を restriction とし、

    R_S=P_X ×_(X^S) P_X -> P_X×P_X

を取る。全て K の limits なので局所対象であり、E で同じ kernel pair を計算できる。pi_S は、S の一点を選んで残りの座標を複製すれば split epi。

S を小さくすると R_S は大きくなる。F が kappa-complete なので、(R_S) は kappa-directed な subobject diagram。

### 補題6.1: R_F は局所対象

    R_F=union_(S∈F) E(R_S) ⊂ E(P_X×P_X)

は、元の local-union 閉性により E の像に属する。

各 sort d において、その元は f,g:I->EX(d) で

    {i:f(i)=g(i)}∈F

となる pair。これは equivalence relation であり、局所対象間の reflexivity/symmetry/transitivity maps は fullness と limit 保存により K の internal equivalence relation を与える。

### 補題6.2: G-始域の既存の等式は一段階で検出される

G∈G、a,b:G->P_X とする。ambient reduced-power quotient

    q_P:E(P_X)->Red_F^P(EX)

の後で E(a),E(b) が等しいと仮定する。

すると (Ea,Eb) は R_F に因子化する。R_F は局所なので fullness により G->R_F を得る。G の lambda-generatedness と kappa>=lambda により、これはある R_S を経由する。従って

    pi_S a=pi_S b

となる S∈F がある。

ここでは生成性を、実際に遷移が mono である relation diagram に適用している。反射された arbitrary-transition diagram に誤適用していない。

### 6.3 残るのは coequalizer が付け加える等式

ambient q_P は R_F の coequalizer。R_F と P_X は局所なので

    q_K:P_X->L(Red_F^P(EX))

は K 内で同じ二射 R_F⇉P_X の coequalizer。

    Sat(R_F)=kerpair_K(q_K)

と置く。R_F⊂Sat(R_F) だが、一般に等号は保証されない。

constant diagonal Delta:X->P_X について

    (Delta×Delta)^*(R_F)=Delta_X,

一方、

    (Delta×Delta)^*(Sat(R_F))=kerpair(delta_F^K).

従って必要な条件は正確に

    (Delta×Delta)^*(Sat(R_F))=Delta_X.

全ての relation が effective である必要はないし、R_F全体のeffectivityさえ要求しない。constant families 上で新しい等式が生じないことだけで十分。

**元の union 閉性から R_F の local 性までは導けた。しかし、その coequalizer の kernel pair が constants 上で拡大しないことは、まだ導けない。** 次節は fixed-rank で実際にこの拡大が起こる例。

---

## 7. 強い対照例: finitely generated strong generator でも fixed-rank CS は失敗する

この例は任意の正則無限 cardinal kappa ごとに作る。圏と signature は kappa に依存する。同じ一つの圏で全rankの失敗を得たという主張ではない。

### 7.1 presheaf 圏と反射部分圏

P_kappa は二sort V,W と unary maps

    a,b:V->W,     p_xi:V->W (xi<kappa)

を持つ構造の圏。これは小圏上の presheaf 圏。

K_kappa を、次の一つの infinitary Horn condition を満たす対象の full subcategory とする:

    for every v∈V,
       [ p_xi(v)=a(v) for every xi<kappa ] => a(v)=b(v).      (Horn_kappa)

### 7.2 reflector の直接構成

Z=(V,W,a,b,p_xi) に対して V は変更せず、W を最小の equivalence relation ~ で割る。この ~ は

    p_xi(v)~a(v) for all xi<kappa => a(v)~b(v)

を満たすものとする。

そのような equivalence relations は full relation を含み、任意の intersection で閉じるので最小のものが存在する。得る quotient は Horn_kappa を満たす。

任意の Z->Y（Y∈K_kappa）について、W成分のkernelはこの条件を満たす。従って上の quotient を一意に経由する。これが reflection。単位は (id_V, quotient_W) で成分ごとに全射。

### 7.3 全 directed unions を保存し、二つの finitely generated strong generators を持つ

K_kappa は ambient subobjects で閉じる。全 directed unions でも閉じる:

union 内の v を一つ選べば v は一段階にある。全ての p_xi(v)=a(v) が union で成り立つとき、同じ段階の injection が mono なので、その段階で全ての等式が成り立つ。Horn_kappa によりa(v)=b(v)。

二つの representables Q_V,Q_W は K_kappa に属する。Q_W は Vempty,Wsingleton。Q_V は Vsingleton,Wに形式的に相異なる a,b,p_xi の値を持つ。Horn の前件が Q_V では偽なのでlocal。

    Hom_K(Q_V,Z)=V_Z,   Hom_K(Q_W,Z)=W_Z.

これらは strong generator。E が全 directed mono-colimits を保存するため、Q_V,Q_W は K 内で finitely generated。

Q_V の ambient carrier size は kappa だが、generatednessはomegaである。この二つを混同しない。

### 7.4 K_kappa は LP、RP は全rankで成立

U を Vsingleton、W={c,d}、全 p_xi とaがc、bがdという構造とする。Tをc=dとした quotient とし、s:U->Tを取る。

    K_kappa={s}^perp

である。U,T は <kappa^+ 個の generators/relations によって表せるので kappa^+-presentable。

また、K_kappa の包含は kappa^+-filtered colimits を保存する。前件の kappa 個の等式が colimit で成り立つなら、kappa^+-filteredness によって一段階で同時に成立させられるからである。

reflection と小さい presentable strong generator により K_kappa は locally kappa^+-presentable。

さらに K_kappa は ambient subobjects に閉じるため、local objectへの任意の mono A->EB で A 自身がlocal。従って RP_rho は全ての正則rhoで成立する。

### 7.5 二つの定数を潰す kappa-complete reduced power

X∈K_kappa を

    V_X=kappa,   W_X={0,1},
    a(t)=0,      b(t)=1,
    p_xi(t)=0 if xi<t, 1 otherwise

で定める。各tで p_t(t)=1!=a(t) なので Horn の前件は偽。従ってXはlocal。

I=kappa を ordinal の順序で取り、Fを tail filter とする。kappa の正則性によりFはproper kappa-complete。

ambient reduced power Q=Red_F^P(EX) 内で、vを列t↦tの同値類とする。W-sortの定数列0,1の類を c_0,c_1 と書く。Fがproperなので c_0!=c_1。

しかし各xi<kappaについて

    p_xi(v)=c_0,     a(v)=c_0,     b(v)=c_1.

p_xi(t)=0 が xi より後の tail で成立するためである。

従って reflection LQ では Horn_kappa により c_0=c_1 となる。よって

    delta_F^K:X->LQ

はnonmonic。Q_Wから0,1を選ぶ二射が潰れる。

同時に delta_F^K は、全てsplitmonoである X->X^[alpha,kappa) のkappa-directed colimitなので、CS_kappaは失敗する。

### 7.6 この例の意味

- generatedness rank はomegaだが、任意に大きい指定kappaでCS_kappaの失敗を作れる。
- local unions の保存、二つの finitely generated strong generators、R_F のlocal性まであっても、fixed-rankでconstantsが潰れ得る。
- 全体はLPでありkappa^+ではCSが成立するので、No.3の反例ではない。
- **RPは全rankで成立するのにCS_kappaは失敗する。** 『あるrankのRP』と『あるrankのCS』の同値から、同じrankでの同値を推論してはいけない。
- local-target pure inclusion はこの例では単なるlocal subobjectで、反射後もmonoのまま。従って arbitrary reduced-power diagonal のmonicityを要求する方法は、特殊なpurity問題に不要なfailureまで検出し得る。
- signatureと圏がkappaに依存する。固定したP,Kについて、十分大きいrankを選べないことは示していない。

この例は前ノートのkappa-ary operationの例とは異なる。前ノートではRP_kappaが失敗した。今回はepireflectiveなHorn classでRPは常に成立し、generatednessもomegaなのにCS_kappaが失敗する。

---

## 8. 主な候補補題の検査結果

(A) 『生成対象からの二射なので、小さい局所targetに一様に圧縮できる』
    FALSE in Grp。§3.3。

(B) 『生成対象がlambda-generatedなら、lambda-directed fixed-domain split-extension colimitが二射を保つ』
    FALSE。§7でlambda=omega、kappa=omega。さらに任意kappaでも生成性rankはomegaのまま失敗を作れる（圏は変わる）。

(C) 『Eがlocal unionsを保存すれば、eventual-equality relationはlocal』
    TRUE for kappa>=lambda。§6.1。

(D) 『G-generatednessは、このrelationに既に属する二射の等式を一段階で検出する』
    TRUE。§6.2。

(E) 『このrelationがlocalであるだけで、反射された商はconstantsを区別する』
    FALSE at fixed rank。§7.5。

(F) 『反射された商がconstantsを区別するrankが、固定Kについてどこかに存在する』
    P3の前提下でLPと同値。今回その一般的存在は未証明。

(G) 『特殊なpure inclusionに対するL(delta_A)のmonicityを示せば、その反射rもmono』
    TRUE as a sufficient condition。§5。ただしrがmonoでもL(delta_A)はnonmonicになり得るので、逆や同rankの必要条件とはしない。

---

## 9. 未解決箇所と、今回の成果の評価

今回のdirect investigationは、二射分離に的を絞った際に、generatednessがどこまで使えるかを具体化した。

生成性を合法的に適用できたのは、kernel relations R_S のmono-union。そこで既存の等式は局所化できた。しかしquotientをKに戻すcoequalizerが新しい等式を付け加える可能性があり、その新しい等式の一様なrank上界は得られていない。

従って、現時点では次はいずれも未証明:

    ZFC => P3,
    ASC_infinity => P3,
    WVP => P3,
    N => not P3.

No.1/2の反例・独立性は今回の証明の入力にしていない。

今後は、arbitrary CSを元のgeneratedness rankそのもので示すことや、小さいlocal cogeneratorsの存在を目指すより、固定Hの強商から得られる特殊なr:LA->Bで、新たな等式の発生を小さいデータに局所化できるかを見る必要がある。今回のHorn例はfixed-rankの素朴な補題を否定するが、この固定H・高いpurityの構成の一般肯定を否定しない。

新しい同値条件の列挙だけを進捗として過大評価しない。具体的成果は、古典的reduced-power機構のこの設定への実装、generatednessを実際に使うrelation検出補題、二つの明示的な手法上の反例、およびRPとCSの同rankでの違いの確定である。

---

## 10. 監査・参照

ローカル入力:

- rp_equivalence_split_colimits_and_compactness_gap_2026-11-17.md: §§5,7の監査、RP/CSのexistential-rank同値、§8の固定Hの反例必要条件。
- positive_quotient_bounds_and_regular_towers_2026-11-17.md: 強商上界判定。
- positive_definability_and_local_submodels_2026-11-17.md: small-local-subobjectの強商判定。

一次資料:

1. I. Di Liberti and J. Rosicky, Enriched Locally Generated Categories, arXiv:2009.10980v2 / TAC 38 (2022).
   https://arxiv.org/pdf/2009.10980
   PDF p.3を画像でも再確認。generatednessとstrong quotient smallnessの役割。後者を落として標準定理を適用していない。

2. L. Positselski, On pure monomorphisms and pure epimorphisms in accessible categories, arXiv:2506.13374v4 / TAC 45 (2026).
   https://arxiv.org/pdf/2506.13374
   PDF p.11を画像でも再確認。§3のpure定義、Lemma3.1。

3. M. Hebert, Algebraically Closed and Existentially Closed Substructures in Categorical Context, TAC 12(9) (2004), 270–298.
   https://www.tac.mta.ca/tac/volumes/12/9/12-09.pdf
   本文取得に成功したmirror:
   https://citeseerx.ist.psu.edu/document?doi=d3ad24d2b27698cb3226a5bbc9fa9868665d8437&repid=rep1&type=pdf
   Theorem2.4(a)、proof pp.282–283のtail filterとreduced-powerへの延長を確認。本稿§4–5と古典的機構の対応を明記。mirrorのPDF screenshotは403で失敗し、当該ページの画像は未確認。今回の直接式と普遍性による証明は本文に展開した。

4. C. Pinnock, Finitary Permutation Groups, Combinatorics Study Group notes, §1.3, Theorem1.4.
   https://chrispinnock.com/assets/2015/01/fpg.pdf
   PDF p.4の画像を確認。finitary alternating groupのsimplicity。任意の無限濃度への適用の短い説明は§3.3に記した。

5. P. Bankston, Obstacles to duality between classes of relational structures, Algebra Universalis 17 (1983), 87–91.
   https://www.mscsnet.mu.edu/~paul/Paper/obstacles2.pdf
   p.90の画像を確認。categorical reduced powersとdiagonalのmonicityが古典的な問題であることの比較。本文の結果をP3へ適用したわけではない。

追加でAdamek–Rosicky(2015)のreflection論文の本文を取得したが、今回の主要証明には使っていない。PDF screenshotは取得失敗。最新文献の網羅的調査、新規性の確認、外部査読は行っていない。
