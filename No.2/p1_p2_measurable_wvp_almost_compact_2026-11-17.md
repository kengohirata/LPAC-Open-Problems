# P1・P2 の巨大基数上下界：rho への一般化、WVP、almost strong compactness

2026-11-17。状態：PROOF_RECONSTRUCTED。既存ノートを入力として、新しい還元・拡張を直接証明し再点検した段階。独立査読・形式検証・新規性確認は未実施。

入力として実際に確認したファイル：

- No.1/codex_sset_handoff/investigations/measurable_thresholds_and_strong_compactness_2026-11-17.md
- No.1/codex_sset_handoff/investigations/positive_tower_2026-11-16.md
- No.1/codex_sset_handoff/investigations/tower_bound_and_weak_vopenka_2026-11-16.md
- No.2/no2_direct_presheaf_kernel_proof_2026-11-17.md

## 0. 命題を区別する

P1：全ての locally presentable category において、集合個の射の ordinary coorthogonality class は coreflective。

P2a：全ての locally presentable category において、任意のクラスの射の ordinary coorthogonality class は coreflective。

P2：Open Problem 2(b)。同じ任意の coorthogonality class は二つの full replete coreflective subcategories の交わり。

P2set：P2 を集合個のテストで定まる coorthogonality class に制限したもの。

M_infty：可測基数が真クラス存在。
ASC_infty：almost strongly compact 基数が真クラス存在。定義は §3。

今回の追加導出：

    WVP ⇒ P2a ⇒ P2 ⇒ P2set ⇒ M_infty,
    P2a ⇒ P1 ⇒ P2set,
    ASC_infty ⇒ P1.

従って P2 には WVP ⇒ P2 ⇒ M_infty、P1 には ASC_infty ⇒ P1 ⇒ M_infty が得られる。旧ノートの WVP ⇒ P1 も保持される。

P1⇒P2、P2⇒P1、P1⇒ASC_infty、P2⇒WVP、ASC_infty⇒P2 は今回証明していない。WVP と ASC_infty/強コンパクト基数の真クラスの間の含意・同値・厳密な相対的一貫性比較もここでは主張しない。

クラスの扱いは、通常の ZFC の集合パラメータ付き定義可能クラスと原理のスキーマ、または対応するクラス理論とする。特に §2 は arbitrary class products や Global Choice を使わない。

## 1. P2 の下界も「可測基数が真クラス」へ強まる

### 1.1 基数を明示した局所仮定

無限基数 rho、|Omega|=rho、M=End(Omega) を固定し、

    N_rho：rho より大きい可測基数が存在しない

とする。No.1 の新ノート §§1–2 により、

    H(F(X)) ≅ {X 上の rho^+-complete ultrafilters},
    F(X)=Omega^X,
    H(L)=Hom_M(L,Omega).

従って N_rho の下で全ての X について H(F(X))≅X（座標評価）。逆にこの全サイズの評価表示があれば、rho より大きい可測基数はない。

有限支持 L の H(L) のコンパクト性、Stone 空間 X に対する C(X)=Cont(X,Omega_disc) と H(C(X))≅X は、Omega が非可算でも ZFC で成立する。

### 1.2 母圏の一般化

    K_fs,rho={Z=(Z_0⇉Z_1):Z_0 は有限支持},
    B_rho=(Omega⇉1),
    sigma_rho:(Omega² --pi_0,pi_1--> Omega)→B_rho,
    A_rho={Z∈K_fs,rho:H(p_Z) が全単射}.

sigma_rho=(pi_0,!) は regular epi、A_rho={}^perp{sigma_rho}、B_rho∉A_rho。

K_fs,rho は presheaf category である。非空有限部分集合 E⊆Omega ごとに

    P_E=(Omega^E --i_0,i_1--> Omega^E⊔Omega^E),
    Q=(empty⇉M)

を取る。Hom(P_E,Z) は E に支持される Z_0 の元の集合、Hom(Q,Z)=|Z_1|。E 上恒等で外側を E の一点に送る idempotent r_E∈M を用いると、前者は忘却関手の自然 retract なので全小余極限を保存する。全有限 E を使えば、非可算 Omega でも全ての有限支持元を検出する。この集合個の small projectives は jointly conservative。標準の nerve/coend 随伴から、その充満小圏上の presheaves と同値になる。

注意：Omega が非可算の場合、「全ての有限支持が自然数の初期区間 [n] に含まれる」とは言えない。全有限 E を添字にする上の表示ではその問題がない。有限 arity の代表 [n] だけを使う場合は、Omega の置換で支持を運ぶ議論を補う必要がある。

### 1.3 P2 直接証明の各段階を確認

既存の no2_direct_presheaf_kernel_proof の各段階は次のように一般化する。

(1) 成分と根 rho_a(n)=c_n a の議論は全ての無限 Omega に成立する。

(2) 非空連結 L に対する H(L×Omega)≅H(L)⊔1 は ZFC。M×Omega≅Omega^(Omega⊔1)≅M（左正則作用）を使うので、必要なのは |Omega⊔1|=|Omega| であり、可算性ではない。従って非同型の局所 coreflector 候補 r:T→B_rho では H(T_1)≠empty。

(3) pushout 補題 A は一般の M-set について同じ証明。W={e:H(e) bijective}、R=W^(perp_u) とすると、A_rho の対象 Z=(Z_0⇉F(S)) から T への射の第1成分 a_1:F(S)→T_1 は R に入る。

(4) N_rho の下で評価 L→F(H(L)) は W に入るので、W-local objects はちょうど冪 F(J)。従って R に属する a_1:F(S)→T_1 の核は、ある I⊆S に対する

    a_1(f)=a_1(g) ⇔ f|I=g|I

である。核対の local 性、添字写像 q:S⊔S↠J と対角 d:J→S、dq=fold の証明は変更不要。

(5) kappa>max(rho,|H(T_0)|,|T_1|,aleph_0) を無限初期順序数に取り、X=[0,kappa]、d=successor（kappa は固定）とする。Y=(C(X)⇉F(X)) は A_rho に属する。H(T_0) のコンパクト像 E⊆X に対する順序数の左平行移動と (R2) の議論により E⊆{0,kappa}。従って全 ell:T_1→Omega について ell a_1=ev_kappa。

(6) 各 beta<kappa に対する切れ目関数 f_beta^+, f_beta^- は二つの値0,1だけを使う。f_beta^+ は連続、f_beta^+d=f_beta^-、両者は beta だけで異なる。beta を核が忘れると p_Tz=q_Tz から z=rho_0(r_0z) が従い、ell_* による評価が0かつ1となり矛盾。ゆえに I=X、a_1 は単射。

(7) |T_1|≥rho^kappa≥2^kappa>kappa>|T_1| で矛盾。

従って次を得る。

**定理1（N_rho）。** A_rho を含む K_fs,rho の全ての full replete coreflective subcategory は B_rho を含む。特に A_rho は任意個の full replete coreflective subcategories の交わりでもない。

可測基数全体が集合なら、それらを上回る rho を一度選べる。この rho に定理1を適用すれば P2set、従って P2 が偽になる。結論：

    P2set ⇒ M_infty,
    P2 ⇒ M_infty.

これは P2⇒P1 を経由した帰結ではない。反例の具体的な証明を rho に一般化した帰結である。テストと標的は rho を選んだ時点で固定する。

## 2. WVP の下では任意の coorthogonality class 自体が coreflective

この節は旧 No.1 の WVP⇒P1 を、proper class 個のテストにも拡張する。新しい点は、全テストを一度に処理せず、各段階で最小ランクにある不合格テストの集合だけを処理すること。

### 2.1 商閉包と trace

まず K=Set^(C^op)、Sigma を射の任意の（定義可能）クラス、A={}^perp Sigma とする。A は小余極限閉で初対象を含む。

    Q(A)={Y:ある A_0∈A からの成分ごとの全射 A_0↠Y がある}

と置く。Q(A) は商と小余極限に閉じる。集合個の証人 A_j の選択には Collection と Choice を使う。クラス個の coproduct は取らない。

q_B:QB↪B を、B の Q(A)-部分対象の和として作る。B の部分対象は集合個なので Separation と通常の和で定義でき、Q(A) の余積・商閉性により QB∈Q(A)。これが Q(A) の monocoreflector。

A-equivalence u:X→Y とは全 A_0∈A について Hom(A_0,u) が全単射となること。

重要な相殺補題：A-equivalence u:X→Y に対し、Z∈Q(A) と v,w:Z→X が uv=uw を満たせば v=w。A_0∈A からの全射 A_0↠Z で前合成し、Hom(A_0,u) の単射性と全射性で相殺すればよい。特に Q(A) 対象間の A-equivalence は Q(A) 内の mono。

### 2.2 集合個のテストの一段階修復

集合 F={s_i:U_i→V_i}⊆Sigma と X∈K を固定する。各 h:X→V_i に一つの変数射 pi_(i,h):D_FX→U_i を用意し、

    s_i pi_(i,h)=h t_X,
    pi_(i,s_i g)=g t_X  (g:X→U_i)

を課した普遍対象 t_X:D_FX→X を、小さい積と pullback で作る。

正確には H_i=Hom(X,U_i)、K_i=Hom(X,V_i)、j_i:H_i→K_i として

    D_FX = X ×_(prod_i (V_i^K_i × U_i^H_i)) prod_i U_i^K_i.

右射は (s_i^K_i,j_i^*)、左射は評価である。

二つの性質：

(i) t_X は A-equivalence。A_0∈A から X への射に沿って、全ての h の唯一の lift を座標に取る。

(ii) t_X が section を持てば X⊥F。section は各 Hom(X,s_i) に左右両逆を与える。

F に X が不合格なテストが含まれていれば、t_X は section を持たない。

### 2.3 クラス個のテストに対する可変の修復列

標的 B を固定し、X_0=QB とする。X_alpha∉A なら、

    xi_alpha = min{xi:Sigma∩V_xi に X_alpha が不合格な射がある},
    F_alpha={s∈Sigma∩V_(xi_alpha):X_alpha not⊥s}

とする。F_alpha は非空の集合である。最小ランクの不合格テストを全て使うので、真クラスからの一様な代表選択は不要。

    X_(alpha+1)=Q(D_(F_alpha) X_alpha),
    e_alpha:X_(alpha+1)→X_alpha

と置く。e_alpha は A-equivalence。しかも section を持たない。section があれば Q(D_FX)↪D_FX と合成して t_X の section を得てしまう。

極限 lambda では

    X_lambda=Q(lim_(alpha<lambda) X_alpha)

とする。全ての遷移 p_(beta,alpha) は A-equivalence。極限段階は Hom(A_0,-) の極限保存と、Q の coreflection による Hom の保存で確かめられる。全ての X_alpha は Q(A) に属する。

同じ修復関手を各段階で反復しているわけではない。ここには co-well-pointed な固定 endofunctor は不要。使う不変量は A-equivalence、Q(A) 所属、一段階射が section を持たないことだけ。

### 2.4 非停止なら Ord^op が presheaf の slice に充満埋め込みされる

全ての段階が A の外にあると仮定する。b_alpha=p_(alpha,0):X_alpha→X_0 と置く。相殺補題から各 b_alpha は Q(A) 内で mono。

beta≥alpha のとき、K/X_0 では標準遷移 p_(beta,alpha) が存在し、他の射は相殺補題でこれに一致する。

alpha<beta のとき、もし u:X_alpha→X_beta が b_beta u=b_alpha を満たせば、

    b_alpha p_(beta,alpha)u=b_alpha

なので p_(beta,alpha)u=id_(X_alpha)。従って p_(beta,alpha+1)u は e_alpha の section となり矛盾。

従って

    Hom_(K/X_0)((X_beta,b_beta),(X_alpha,b_alpha))
      = singleton  if beta≥alpha,
        empty      if beta<alpha.

これは Ord^op→K/X_0 の充満忠実な関手である。K/X_0 は再び presheaf category、従って locally presentable。WVP の標準的定式化に矛盾する。

よってある集合順序数 alpha で X_alpha∈A。X_alpha→X_0→B は A-equivalence なので B の A-coreflection である。

### 2.5 任意の locally presentable category へ移す

L:K⇄D:J を D の full reflective presheaf 表示とする。D の任意のテストクラス Sigma に対し

    A={}^perp_D Sigma,
    C={}^perp_K J(Sigma)=L^(-1)(A).

C の JB-coreflection c:C_0→JB を取る。反射単位 eta:C_0→JLC_0 を介して c=Jd eta と因子化する。LC_0∈A なので JLC_0∈C。coreflection の普遍性から t:JLC_0→C_0 があり、t eta=id_(C_0)。反射の普遍性により eta t=id_(JLC_0)。従って C_0≅JLC_0 で、d:LC_0→B は A-coreflection。

**定理2。** WVP⇒P2a。従って WVP⇒P2、かつ WVP⇒P1。

任意の colimit-closed full subcategory に同じ証明を適用したとは主張しない。coorthogonality によるテスト表示を、一段階修復の構成と section の排除に本質的に用いる。この区別により、全ての colimit-closed 部分圏の coreflectivity が VP と同値である既知定理との混同を避ける。

文献の homotopy localization の定理を双対化して適用したのではない。引用するのは WVP が Ord^op の locally presentable category への充満埋め込みを禁止するという定式化だけ。

## 3. P1 の compactness 上界は almost strongly compact まで弱められる

### 3.1 二つの基数を分ける

theta を非可算正則基数とし、kappa≥theta が L_(theta,omega)-compact とは、任意の kappa-complete filter が theta-complete ultrafilter に延長できることとする。この性質は kappa を大きくしても保存されるので、必要な言語サイズを上回る正則 kappa を選べる。

ある lambda が almost strongly compact とは、全 theta<lambda について lambda が L_(theta,omega)-compact であること。この定義では lambda 自身の正則性は要求しない。証明で正則性が必要なのは、別に選ぶ kappa の方。

Brooke-Taylor–Rosicky, Accessible Images Revisited, Definition 2.3 と Proposition 2.4 により、

    ASC_infty ⇔ 全 theta について L_(theta,omega)-compact な kappa が存在。

必要なら正則 theta だけに量化しても、上の大きな正則 theta を取ることで同じ全体原理となる。

### 3.2 小さい標的の pure-injectivity

K=Set^(C^op)、|Mor C|<kappa、kappa は正則で L_(theta,omega)-compact、|D|<theta とする。

**補題3。** D は kappa-pure-injective。

証明。kappa-pure inclusion Y↪X と h:Y→D を取る。X の各 sort の各元の像を変数にし、presheaf の全構造写像を保存する方程式と h の値を固定する方程式からなる制約集合 E を取る。

各 s∈P_kappa(E) は、purity により D 内で解を持つ。具体的には、<kappa 個の変数・パラメータ・構造方程式は X で解けているので Y 内で解き直し、h を適用する。空 sort の問題も purity が処理する。X(c) が非空なら無パラメータの存在条件で Y(c) は非空になり、h により D(c) も非空。

P_kappa(E) 上の cone filter は kappa-complete（kappa が正則）。L_(theta,omega)-compactness により theta-complete ultrafilter U に延長する。

各局所解を選び、未使用変数には任意の値を補う。一変数の値の可能性は |D(c)|<theta 個だから、theta-completeness により U-almost everywhere の一意な値を選べる。

各方程式の成立集合は U に入り、その有限個の変数の選ばれた値の集合との交わりも U に入る。従って選んだ値は全方程式を満たす。h の延長 X→D を得る。□

ここで ultrafilter の kappa-completeness は不要だった。必要なのは値域のサイズを上回る theta-completeness だけである。

### 3.3 存在性と一意性の両方を処理する

テスト集合 Sigma={f_i:U_i→V_i} を固定し、

    |V_i|<theta,
    |U_i×_(V_i)U_i|<theta

となる theta を取る。集合個だから同じ theta を選べる。言語サイズより大きい正則 kappa≥theta で L_(theta,omega)-compact なものを選ぶ。

補題3により V_i と K_i=U_i×_(V_i)U_i は kappa-pure-injective。

A={}^perp Sigma、X∈A、kappa-pure Y↪X とする。

存在性：Y→V_i を X→V_i に延長し、X の直交性で持ち上げ、Y に制限する。

一意性：同じ V_i 成分をもつ二射 Y⇉U_i を Y→K_i にまとめ、X→K_i に延長する。その二射影 X⇉U_i は X∈A により等しく、元の二射も等しい。

従って A は kappa-pure subobjects に閉じる。

### 3.4 固定サイズの小さい pure subobjects と随伴

mu=2^kappa とすれば mu^(<kappa)=mu。任意の X∈A とサイズ≤mu の元集合は、同じサイズ以下の kappa-pure subpresheaf Y⊆X に含められる。長さ kappa の列で、各段階で<kappa 個の方程式系の解を全て一つずつ加える。系の数はmu以下、各追加もmu以下であり、kappaの正則性から最終合併はpureになる。

この Y は A に残る。サイズ≤mu のこうした部分対象は mu^+-directed に X を覆い、母圏でも A でも mu^+-presentable。同型類は集合個。A は全小余極限に閉じるため locally presentable で、包含 A→K は colimit-preserving、従って右随伴を持つ。

§2.5 と同じ反射移送により一般の locally presentable D にも coreflectivity が従う。

**定理4。** ASC_infty⇒P1。さらに各固定された presheaf/test データについて、その値域と kernel pairs のサイズを上回る theta に対する L_(theta,omega)-compact cardinal 一つで十分。

強コンパクト性の十分条件を弱めたという意味であり、ASC_infty と強コンパクト基数の真クラスの厳密な分離モデルや、P1との同値性を証明したという意味ではない。

## 4. P2 全体と集合テスト版の差

P1⇒P2set は自明：A 自体が coreflective なので A=A∩K と表せる。

P1 から任意のテストクラス Sigma について直ちに分かるのは、

    {}^perp Sigma=intersection_(f∈Sigma) {}^perp{f}

の各因子が coreflective ということだけ。クラス個の交わりを二因子に圧縮することは別の問題。

今回 P2 全体の肯定側を扱えたのは §2 の WVP による可変修復列であって、ASC_infty⇒P1 を形式的に移したためではない。

同様に P2 から P1 も形式的には従わない。二つの coreflective 部分圏の交わりが coreflective とは限らないことは、No.1/No.2の旧具体例が既に示している。ただしこのことだけでグローバルな原理 P2⇒P1 の非含意を証明したことにはならない。

## 5. P2 から P1 に持ち帰れるものと、残る研究目標

### 5.1 既に持ち帰れる構造的強化

定理1の A_rho は、明示的な presheaf category における一本の regular epi の coorthogonality class。

従って「その特殊なテストだけなら全て coreflective」という P1 の制限版ですら M_infty を含意する。可測基数の下界は、proper class 個のテストや二本のテストの複雑さに由来していない。

### 5.2 下界を compactness まで押すには fine 性が新たに必要

H(F(X)) の計算が与えるのは、ある集合 X 上の rho^+-complete ultrafilter。これから非主性を得ても可測性にしか到達しない。

L_(theta,omega)-compactness を狙うなら、同じkappaについて全てのlambda≥kappaに対し、P_kappa(lambda) 上のtheta-complete fine ultrafilterを出す必要がある。fineとは

    {u∈P_kappa(lambda):a∈u}∈U  (全a<lambda)

という条件。これは現在の Isbell 計算だけには含まれていない。

研究上の十分目標：thetaに依存する固定した圏・テスト集合・標的を作り、そのcoreflectorから一つのkappaを読み取り、全lambdaに対してfine ultrafilterを抽出する。P2のpushout→右直交性→核の制御は、この抽出を一意性と整合させる候補道具になる。ただしこの新しい実現補題は未証明。

また、P1⇒ASC_infty を予想する前に、既に得られている WVP⇒P1 と両立するかを集合論的に確認すべき。これを示すなら同時に WVP⇒ASC_infty を示すことになる。accessibility の既知の逆定理を、単なる coreflectivity にそのまま適用してはならない。

### 5.3 定義可能性を使う別の方向

WVP の各Lévy階層の強度は Bagaria–Wilson により解析されている。修復列から得る Ord^op 埋め込みの定義可能性を正確に見積もれば、P1や定義可能性を制限したP2の肯定側をWVPの断片へ弱められる可能性がある。

本稿では、Q(A) の trace、最小ランクの失敗集合、超限再帰による埋め込みの複雑性の見積もりを完了していない。従って特定の Sigma_n-WVP や「強基数の真クラス」で十分とは結論しない。strong cardinal と strongly compact cardinal は別の概念である。

## 6. 参考文献と今回の利用範囲

1. A. Brooke-Taylor and J. Rosicky, Accessible Images Revisited, Proc. AMS 145 (2017), 1317–1327, Definition 2.3 / Proposition 2.4.
   https://arxiv.org/pdf/1506.01986
   使用：L_(theta,omega)-compactnessのfilter-extension定義、上方単調性、ASC_inftyとの同値。強力像の定理からP1をそのまま引用したわけではない。

2. M. Cortes-Izurdiaga and J. Saroch, The cotorsion pair generated by the Gorenstein projective modules and lambda-pure-injective modules, arXiv:2104.08602v2, Proposition 5.3 / footnote 4 / Remark 5.4.
   https://arxiv.org/pdf/2104.08602
   使用：L_(theta,omega)-compactnessによる小さい加群のpure-injectivityという既知の類例の確認。presheaf版は§3で直接証明した。

3. C. Casacuberta and J. J. Gutierrez, Homotopy reflectivity is equivalent to the weak Vopenka principle, §1.1(b).
   https://www.ub.edu/topologia/casacuberta/articles/Semiweak.pdf
   使用：WVPの「Ord^opがどのlocally presentable categoryにも充満埋め込みされない」という定式化と、定義可能クラスの規約。同論文のホモトピー反射を本稿のcoorthogonalityへ転用していない。同論文§1.2は双対概念を扱わないと明記している。

4. J. Bagaria and T. M. Wilson, The Weak Vopenka Principle for definable classes of structures, JSL 88 (2023), 145–168, §1–2.
   https://doi.org/10.1017/jsl.2022.42
   使用：VP/WVPの区別と定義可能性階層の背景。本稿はWVPとASC_inftyとの比較を導いていない。

Web本文を確認した。PDFスクリーンショット取得はサービス側のCache missにより失敗しており、画像を目視確認したとは扱っていない。

## 7. 監査の優先箇所

(1) 任意rhoのpresheaf表示で、有限支持の検出を全有限Eまたは置換輸送で行うこと。
(2) P2直接証明のH(L×Omega)が正則作用で一般化できること。
(3) proper class Sigmaに対するQ(A)のtraceの定義とCollectionの使用。
(4) 最小ランクの不合格テスト集合 F_alpha の存在と、e_alpha がsectionを持たないこと。
(5) 固定修復関手なしでOrd^opのHom計算が成立すること。
(6) pure-injectivityで必要な完備性がthetaで、purityとcone filterには別の正則kappaを使うこと。

既存ファイルの内容・検証状態は変更していない。本稿の新規主張は引き続き独立検証前の直接証明として扱う。
