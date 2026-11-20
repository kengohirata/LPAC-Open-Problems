# P1 の必要条件の強化に向けて：reduced power・uniform ultrafilter・accessibility の正確な境界

2026-11-17。状態：PROOF_RECONSTRUCTED。以下の直接証明は主担当が点検した段階。独立査読・形式検証・新規性確認は未実施。

**重要：今回、P1 の巨大基数下界を「可測基数が真クラス」からさらに上げたとは主張しない。P1⇒ASC∞、P1⇒strong 基数の真クラス、P1⇒全 Π₂-PRP は依然未証明。** 得られたのは、強化に必要な ultrafilter 条件の具体的な Hom 符号化、ZFC-coreflective なクラスの accessibility と compactness の同値、および素直な図式への挿入方法を排除する固定受け皿である。

## 0. 結果の要約

無限基数 rho、|Omega|=rho、M=End_Set(Omega)、H(X)=Hom_M(X,Omega)、delta=rho^+ とする。

1. 任意の集合 I と proper filter F に対し、reduced power L_F=Omega^I/~F を M-set として作ると

       H(L_F) ≅ {F を延長する delta-complete ultrafilters on I}.

   これは No.1 の full-power/ultrafilter 計算を商へ拡張した、ZFC の直接計算。

2. lambda 上の co-small filter を用いれば、H(L_F) は delta-complete uniform ultrafilters。P_kappa(lambda) の有限coneで生成したfilterを用いれば、delta-complete fine ultrafiltersを正確に表す。全<kappa-coneで生成したfilterとの違いは§2.2で明記する。

3. 次の充満部分圏を取る。

       N_rho={empty} ∪ {X:H(X)=empty} = {}^perp{empty→Omega}.

   これは ZFC で coreflective、しかも内部 mono は母圏の mono で well-powered。

4. しかし以下は同値である。

   (a) N_rho が accessible。
   (b) ある集合基数 mu が存在し、任意の非空 X∈N_rho は濃度≤muの非空な N_rho-部分 M-set を含む。
   (c) ある kappa≥delta が L_(delta,omega)-compact。
   (d) ある kappa≥delta 以上のすべての正則 lambda に、delta-complete uniform ultrafilter が存在。

   (a)(b)(c) は下に直接証明する。(c)⇔(d) は Usuba, Theorem 1.2。

5. 従って、全 rho について N_rho が accessible と要求することは ASC∞ と同値。一方、それらの coreflectivity は全て ZFC で成立する。この結果は P1⇒ASC∞ の非含意を示さないが、個別の coreflectivity を accessibility と取り違える逆証明を明確に排除する。

6. null な reduced power を平行二射の第1成分へ単に積として足す方法について、全候補から固定した A-対象 P_rho=(finite-image sequences --id,shift--> finite-image sequences) への因子化を構成した。従って、その挿入だけでは No.1 型の解集合障害を作れない。

## 1. Reduced power の正確な Hom 計算

F を非空集合 I 上の proper filter とする。f,g:I→Omega に対し

    f~F g ⇔ {i∈I:f(i)=g(i)}∈F

と定義する。これは同値関係であり、Omega の自己写像 m による後合成を保つ。従って

    L_F=Omega^I/~F

は左 M-set である。q:Omega^I→L_F を商射とする。

No.1 の一般 rho 版の計算により、H(Omega^I) は I 上の delta-complete ultrafilters と自然に対応する。ここで delta=rho^+、delta-complete は rho 個以下の交叉を保存するという意味。

**補題1。** ultrafilter U の評価 h_U:Omega^I→Omega が q を経由することと F⊆U は同値。

証明。A∈F なら、0,1をOmegaの異なる点として χ_A~F c_1。h_U が商へ降りるなら h_U(χ_A)=1、すなわち A∈U。

逆に F⊆U、f~F g とする。E={i:f(i)=g(i)}∈U。また h_U(f)=a、h_U(g)=b とすると f^{-1}(a),g^{-1}(b)∈U。三集合の交叉は非空なので a=b。従って h_U は商へ降りる。q は全射なので降下は一意。□

よって

    H(L_F) ≅ {U : U は delta-complete ultrafilter、F⊆U}.       (1.1)

特に、「高完備 ultrafilter が存在する」に加えて「指定された filter を延長する」という条件を、対象の商関係だけで符号化できる。N（可測基数非存在）などの追加仮定は使わない。

## 2. Uniform と fine の特殊例

### 2.1 Uniform ultrafilter

無限基数 lambda に対して

    F_co<lambda={A⊆lambda:|lambda\A|<lambda}

と置く。U がこの filter を含むことと、U の全ての元が濃度lambdaを持つことは同値。従って

    H(Omega^lambda/~F_co<lambda)
      ≅ {delta-complete uniform ultrafilters on lambda}.      (2.1)

lambda が正則なら F_co<lambda は lambda-complete である。

Usuba の Theorem 1.2 によれば、delta≤kappa が非可算基数のとき、ある固定 kappa 以上の全正則 lambda について右辺が非空であることは、kappa が delta-strongly compact、すなわち L_(delta,omega)-compact であることと同値。

従って P1⇒ASC∞ を狙う十分目標は

    P1 ⇒ ∀rho ∃kappa≥rho^+ ∀lambda≥kappa regular,
              H(Omega^lambda/~F_co<lambda)≠empty.             (2.2)

これはまだ証明していない。既知定理によって「fine性を全lambdaで直接作る」代わりにuniform性を用いることもできる、という標的の具体化である。

### 2.2 Fine ultrafilter

正則 kappa≥delta、lambda≥kappa とし I=P_kappa(lambda) と置く。cone filter は

    F_cone={A⊆I:あるs∈P_kappa(lambda)に対し
                    {u∈I:s⊆u}⊆A}.

kappaの正則性からこれは proper kappa-complete filter。

(1.1) より H(Omega^I/~F_cone) の元は、全coneを含むdelta-complete ultrafilterと同値である。特にfineである。

逆に、delta-complete fine ultrafilterが必ず全<kappa-coneを含むとは限らない（delta<kappa の場合）。従ってこのcone filterで得るのは、一般のfine ultrafilterより強い「全<kappa-coneを含む」条件である点を区別する。

標準のfine ultrafilterそのものを正確に符号化したければ、singleton cones {u:a∈u} の有限交叉だけで生成したfilter F_finconeを用いる。この場合

    H(Omega^I/~F_fincone)
       ≅ {delta-complete fine ultrafilters on P_kappa(lambda)}. (2.3)

F_fincone が kappa-complete だとは主張しない。L_(delta,omega)-compactness の適用には F_cone を使い、Usuba/Bagaria–Magidor のfine性の特徴付けには (2.3) を使う。

## 3. Small subacts には座標評価が残る

**補題2（ZFC）。** kappa は無限基数で、|M|<kappa、F は proper kappa-complete filter。Y⊆L_F が |Y|<kappa を満たす部分 M-set なら、H(Y)≠empty。

証明。Y=empty なら自明。各 y∈Y に代表 f_y:I→Omega を選ぶ。全ての m∈M,y∈Y に対し

    E_(m,y)={i:f_(my)(i)=m(f_y(i))}

は F に属する。関係式の数は |M|·|Y|<kappa。kappa-completeness によってそれらの交叉は F に属し、proper性から非空。i_*を一つ選ぶと

    h(y)=f_y(i_*)

は全ての M-作用を保つ。従って h:Y→Omega。□

この補題は F の ultra 性を要求しない。全体 L_F に Ω 値写像が存在しなくても、その十分小さい部分 M-set には写像が存在する、という compactness の局所側を与える。

## 4. ZFC-coreflective な null class

    N_rho={empty}∪{X:H(X)=empty}
          ={}^perp{empty→Omega}

と置く。M-Set は一対象小圏上の presheaf category。empty→Omega は一本の mono。

### 4.1 明示的 coreflector

B∈N_rho なら R(B)=B。B≠empty かつ H(B)≠empty なら R(B)=empty とする。

後者の場合、非空 X∈N_rho から B への写像があれば、それと B→Omega を合成して H(X) の元を得てしまう。従ってそのような射はなく、empty→B はすべての N_rho-対象からの Hom を正しく表す。前者は恒等射の普遍性。よって N_rho は ZFC で coreflective。

coorthogonality により全小余極限は M-Set で計算される。また、非空 null act の全射像も null である。

### 4.2 Well-poweredness も ZFC

N_rho 内の mono m:A→B を取る。A=empty なら母圏でもmono。A≠emptyなら、任意の T と u,v:T→A に対し A⊔T∈N_rho（AからOmegaへの射がないため）。mu=mvなら [1_A,u] と [1_A,v] はmの後で一致するので内部mono性からu=v。従ってmはM-Setのmono。よってN_rhoはwell-powered。

したがって下記のaccessibility障害を、非coreflectivityや非well-powerednessに読み替えてはならない。

## 5. Null class の accessibility と L_(delta,omega)-compactness の同値

**定理3（ZFC内の同値）。** 固定した無限rhoとdelta=rho^+について、次は同値。

(A) N_rho は accessible。
(B) ある集合基数muが存在し、任意の非空null act Xは、濃度≤muの非空null subact Y⊆Xを含む。
(C) あるkappa≥deltaが L_(delta,omega)-compact。

### (A)⇒(B)

N_rhoのaccessible generatorsの集合Gを取り、その台集合のサイズをmuで一様に抑える。非空X∈N_rhoをGの対象のfiltered colimitとして表示する。包含N_rho→M-Setは余極限を保存するため、非空のG∈GからXへの射が存在する。その像Yは非空、サイズ≤mu、そしてGの商なのでnullである。□

### (B)⇒(C)

正則kappa>max(mu,|M|,rho)を固定する。任意の集合I上のproper kappa-complete filter Fを取る。

H(L_F)=emptyと仮定するとL_Fは非空null act（定数関数の類が存在する）。(B)から非空null subact Y⊆L_F、|Y|≤mu<kappaがある。しかし補題2によりH(Y)≠emptyで矛盾。

従ってH(L_F)≠empty。(1.1)によりFはdelta-complete ultrafilterへ延長される。FとIは任意なのでkappaはL_(delta,omega)-compact。□

### (C)⇒(B)：Hom の compactness

kappaを必要ならさらに大きい正則基数に取り替え、|M|<kappaを仮定する。この変更でL_(delta,omega)-compactnessは保たれる。

Xの全てのサイズ<kappaのsubactがOmegaへの射を持つと仮定する。I=P_kappa(|X|)とし、s∈Iから生成されるsubact X_s=M·sはサイズ<kappa。h_s:X_s→Omegaを選ぶ。emptyの場合も一意の空射を用いる。

I上のcone filterをdelta-complete ultrafilter Uへ延長する。h_sをX全体に固定値で補い、各x∈Xについて、rho<delta個の値のうちU-almost everywhereの唯一の値h(x)を取る。

m∈Mとx∈Xについて、x∈sのconeはUに属し、そこではh_s(mx)=m h_s(x)。h(x),h(mx)の値が定まる二つのU-大集合と交叉すればh(mx)=m h(x)を得る。従ってh:X→Omega。

対偶から、H(X)=emptyなら、あるサイズ<kappaの非空null subactがある。これが(B)。□

### (C)⇒(A)：小さい null subacts による生成

同じ正則kappaを使う。非空X∈N_rhoについてサイズ<kappaの非空null subact Y_0⊆Xを一つ固定する。

Y_0を含むサイズ<kappaのsubactのposetを取る。各対象はY_0から射を受けるのでnull。<kappa個のそのようなsubactの和集合はサイズ<kappaのsubactであり、posetはkappa-directedである。任意のx∈XにY_0∪M·xを加えれば全体を覆う。

|M|<kappaであるため、サイズ<kappaのM-setはkappa-presentable（生成元と作用関係式を<kappa個で書ける）。N_rhoのfiltered colimitsは母圏で計算されるので、これらはN_rho内でもkappa-presentable。小さいM-setの同型類は集合個。emptyを追加して全対象の生成族を得る。従ってN_rhoはkappa-accessible。□

(B)だけから(A)へ行く場合にも、上の小さいnull subactの生成をより大きな正則kappaで使える。

## 6. 全rhoに量化した意味とP1への境界

Brooke-Taylor–Rosický Proposition 2.4により

    ASC∞ ⇔ ∀theta ∃kappa : kappaはL_(theta,omega)-compact.

thetaをrho^+に制限しても、それらが全基数に共終なので同じ原理。従って定理3より

    ASC∞ ⇔ ∀rho N_rhoがaccessible.                             (6.1)

前段階の「ASC∞の下でpresheafの全small coorthogonality classはaccessible」という証明を採用すれば、さらに

    ASC∞ ⇔ 全presheaf圏の全small coorthogonality classがaccessible.

逆方向には、一本のmono empty→OmegaのクラスN_rhoだけで足りる。

ただしP1が要求するのはcoreflectivityである。全N_rhoのcoreflectivityとwell-powerednessは既にZFCの定理なので、P1をN_rho自身に適用しても(6.1)の右辺は得られない。

これはP1⇒ASC∞が偽という証明ではない。P1の全圏・全テストへの量化を別の図式に適用し、N_rhoの局所小証人を強制する可能性は残る。今回、その追加の還元は未構成。

## 7. 直接の「null reduced power を足す」候補の障害

reduced power L=L_F を第1成分の積因子として足す素直な候補を調べる。

Aを有限支持M-set、t:A→A、alpha,beta:A→LをM-射として

    Z=(A --p=(alpha,id_A), q=(beta,t)--> L×A)

とする。

このZが合格する場合も含めて、任意のb:Z→B_rho=(Omega⇉1)は、次の固定した合格対象を経由する。

    S_rho={f:omega→Omega : im(f)は有限},
    P_rho=(S_rho --id,shift--> S_rho),
    epsilon=(ev_0,!):P_rho→B_rho.

p_P=idなのでP_rho∈A_rho。bの第0成分をb_0:A→Omegaとし、

    a_0(x)(n)=b_0(t^n x),
    a_1(l,x)=a_0(x)

と定義する。

xの有限支持Sは、全t^n xの支持でもある。従ってb_0(t^n x)∈Sでありa_0(x)は有限像。各写像はM-同変で、

    a_1p=a_0,
    a_1q=shift a_0,
    ev_0 a_0=b_0.

よってa:Z→P_rho、epsilon a=b。この受け皿P_rhoはI,F,lambda,Aに依存しない。

従ってこの形の候補だけを増大させても、固定B_rhoへの因子化サイズを無界にはできない。観測のない積因子Lを消せてしまうことが原因である。これはreduced-power経路全体の不可能性ではなく、この具体的な挿入方法の排除。

## 8. 実際にP1の下界を強めるための残余補題

有望な十分目標は、rhoだけに依存する固定presheaf圏・固定テスト集合・固定標的を選び、そのcoreflector r:R→Bから一つのkappa=kappa(R)を取り出して、

    全てのregular lambda≥kappaに対し
    Omega^lambda/~F_co<lambda → Omega

を作ることである。Usubaの定理から、これが成立すればkappaはrho^+-strongly compact。全rhoで実現すればP1⇒ASC∞になる。

ここでは「同じkappaで、全てのlambda」が不可欠。lambdaごとにテストや標的を変え、lambdaごとに異なるcoreflectorを取るだけでは不十分。

別方向として、前稿のPRP_testから全bold Π₁-PRPへの還元ができれば、通常のstrong基数の真クラスという下界を狙える。しかし任意のΠ₁クラスをA-equivalenceの圏として実現する補題を得ておらず、この含意も未証明。全Π₂-PRPまで戻すことは、ASC∞からその原理を導くことにもなるため、上界の定理を逆向きに読むだけでは正当化できない。

本稿はP1の既存の下界（可測基数の真クラス）を変更しない。

## 9. 参照と確認範囲

ローカル入力：

- ../No.1/codex_sset_handoff/investigations/measurable_thresholds_and_strong_compactness_2026-11-17.md §1：H(Omega^I)とrho^+-complete ultrafilterの対応。
- ../No.1/codex_sset_handoff/investigations/positive_purity_2026-11-16.md：coreflectivityとaccessibilityの区別。本稿ではmonoid actによる別の正確な同値を直接証明した。
- p1_restricted_product_reflection_pi2_strong_2026-11-17.md：PRP_testの位置づけ。

外部一次資料：

1. Toshimichi Usuba, A note on delta-strongly compact cardinals, arXiv:2001.02124。Definition 1.1、Theorems 1.2、1.7。
   https://arxiv.org/abs/2001.02124
   今回はWebの全文HTML抽出で、uniform ultrafilterの特徴付けとfine ultrafilterの定義を確認した。
2. Andrew Brooke-Taylor and Jiri Rosicky, Accessible Images Revisited, arXiv:1506.01986v2。Definition 2.3、Proposition 2.4。
   https://arxiv.org/pdf/1506.01986
   本文抽出でfilter-extension定義、上方単調性、ASC∞との同値を確認。PDF screenshotはサービスのCache missで失敗したため、画像を目視したとは扱わない。

reduced-power計算、補題2、N_rhoの三条件の同値、固定受け皿は本稿で直接展開した議論であり、これらが新規の文献結果であると主張しない。P1の必要条件をさらに強化する実現補題は未証明。
