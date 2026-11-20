# Problem 4：mono を保つ成分圧縮と M の V-codomain equalizers

2026-11-18。

**状態：PROOF_RECONSTRUCTED。以下の直接証明は自己点検段階。一般の M の equalizer 閉性、一般の retract 閉性、No.4 の反例完成は結論しない。独立査読・形式検証・新規性確認は未実施。**

## 1. 設定

記号は [V-codomain の旧ノート](v_codomain_equalizers_root_compression_2026-11-17.md) と共通。

    Ω=ω, M_1=M_2=End(Ω), J=(0⇉1),
    K=(M_1-Set)^J,
    P=(M_2-Set)^((M_1×J)^op),
    E(Y)_i=Ω^(Y_i).

C は Y_0 が有限支持で H_1(p_Y):H_1(Y_1)→H_1(Y_0) が全単射となる Y のクラス。D=E(C^op) の replete image。

今回の新候補は

    Z∈M ⇔ 各 ambient finitely generated F と各 f:F→Z が
           F→D_0↪Z, D_0∈D と因子化する。

最後の射に ambient mono を要求する。従って M⊆H_fg。

C の colimit 閉性、E の colimit-to-limit 性、および以下の双対 Hom の currying は ZFC の直接議論。§3–§6.6 の定理には N も No.1 の非 coreflectivity 入力 (NC) も使わない。§6.7 は N と既存 No.1 定理8の因子化下界を条件として使う。§7 の必要十分条件のうち必要性だけは、E の full faithfulness のために N を使う。§6.7 は No.1 入力の独立査読を追加するものではない。

## 2. 旧圧縮の変更点

旧ノート §6 の圧縮では、fg F と t:F→E(Y), Y∈C に対し

    R(Y) → Y
      ↓     ↓q
    R(QF)→Y_F

という pushout を用いた。ただし QF のうち Y から来ない成分の根まで加えるため、q の surjectivity、従って E(q) の monicity は保証していなかった。

**変更点は、QF の全成分を使わず、Y から来る成分だけを使うこと。** これにより q を objectwise surjective にできる。

## 3. Epi にできる相対成分圧縮

### 3.1 双対 Hom と成分の像

F∈P に対し

    (QF)_i=Hom_(M_2)(F_i,Ω),
    (m h)(x)=h(x·m)

とする。自然な currying による全単射

    P(F,E(Y)) ≅ K(Y,QF)

で t を t^♯:Y→QF に対応させる。

π_0 は各 M_1-set の connected-components functor。各 sort について

    I_i = im(π_0(Y_i)→π_0((QF)_i))

と定める。自然性により p,q の component maps は I_0 を I_1 に送り、I は Set^J の図式をなす。

Set^J の図式 I に対し R_I を

    (R_I)_i=Ω×I_i,

で定め、M_1 は Ω 座標に作用させる。二つの構造射は I の対応する写像と id_Ω から作る。

R_I∈C。各成分は Ω の copower で、第0成分は有限支持。さらに、Ω→Ω の M_1-equivariant map は id のみなので、H_1(Ω×I_i) は I_i が空でも非空でも一元集合。従って H_1(p) は全単射。

### 3.2 Pushout

旧ノートの R(Y)_i=Ω×π_0(Y_i) と root map ε_Y:R(Y)→Y を使い、

    a:R(Y)→R_I,
    a_i(n,C)=(n,π_0(t^♯)_i(C))

を定める。I_i を像として取ったため、a は各 sort で全射。

K で pushout

    R(Y) --ε_Y--> Y
      |a           |q
      v            v
     R_I --------> Y_t

を取る。

Y,R(Y),R_I∈C と C の colimit 閉性から Y_t∈C。K の pushout は台集合上で計算され、a が各 sort で全射なので **q:Y→Y_t も各 sort で全射**。

### 3.3 元の t の保存

I⊆π_0(QF) の各成分 C に対し、その root を使う射

    ε_I:R_I→QF,
    ε_I(n,C)=ρ_C(n)

がある。根の自然性により

    t^♯ ε_Y = ε_I a.

従って pushout から h:Y_t→QF が得られ、h q=t^♯。h を転置した t_t:F→E(Y_t) は

    E(q)t_t=t

を満たす。

### 3.4 成分数の上界

π_0 は colimits を保存し、π_0(ε_Y) は同型なので、各 sort で

    π_0((Y_t)_i) ≅ I_i.

旧ノート §6.2 の countable-signature lemma から、F が finitely generated なら

    |π_0((QF)_i)|≤𝔠,  𝔠=2^ℵ0.

従って |π_0((Y_t)_i)|≤𝔠。

**補題 3.1（ZFC）。** 任意の fg t:F→E(Y), Y∈C は

    F --t_t--> E(Y_t) --E(q)↪ E(Y)

と因子化し、Y_t∈C、各 sort の component 数≤𝔠。ここで **E(q) は ambient mono**。

最後の monicity は、surjective q_i:Y_i→(Y_t)_i に沿う前合成 Ω^((Y_t)_i)→Ω^(Y_i) が injective であることによる。

**上界の限界。** 抑えたのは component 数だけ。Y_t の carrier の大きさは抑えていない。従って中間 D-object のサイズの一様上界や、十分大きい filtered-colimit 閉性はここからは従わない。

## 4. V を値域とする M の equalizer 閉性

旧ノートの

    T_α={coinfinite injections α→ω}, α<ω_1,
    Z_*=(Ω --id,id--> Ω),
    V_α=E(T_α・Z_*),
    V=colim_(α<ω_1) V_α

を使う。各 V_α∈D、transition maps と colimit injections は mono。

fg F→V は一段階 V_α を経由するから、**V∈M**。

旧ノート §5 の stage-factorization lemma を入力とする：各 sort の component 数が≤𝔠 の Y について、任意の E(Y)→V は一段階 V_α を経由し、その stage map は明示的な K-map T_α・Z_*→Y の E 像である。この補題は ZFC で証明されている。

**定理 4.1（ZFC）。** Z∈M と a,b:Z⇉V に対し、Eq(a,b)∈M。

### 証明

j:W↪Z を equalizer とし、fg F と x:F→W を固定する。

Z∈M より

    jx=v t,
    F --t--> E(Y) --v↪ Z,
    Y∈C

と因子化できる。

補題 3.1 を使い

    t=E(q)t_t,
    E(q):E(Y_t)↪E(Y),
    |π_0((Y_t)_i)|≤𝔠

とする。特に **v E(q) は mono**。

二射 avE(q), bvE(q):E(Y_t)⇉V に stage-factorization lemma を適用する。共通の α を取り、

    avE(q)=i_α E(k_a),
    bvE(q)=i_α E(k_b),
    k_a,k_b:T_α・Z_*⇉Y_t

と書ける。i_α は mono、かつ元の a,b は jx 上で一致するので

    E(k_a)t_t=E(k_b)t_t.

C 内の coequalizer

    T_α・Z_* ⇉ Y_t --r--> R

を取ると R∈C で、E(r):E(R)↪E(Y_t) は E(k_a),E(k_b) の equalizer。従って t_t は E(R) を経由する。

合成

    E(R) --E(r)↪ E(Y_t) --E(q)↪ E(Y) --v↪ Z

は mono で a,b を equalize する。従って W への因子化 E(R)→W も mono。この D-subobject を x が経由するので W∈M。□

ここで E の full faithfulness は使っていない。stage maps k_a,k_b が明示的に得られるため、最後の equalizer を C の coequalizer から直接作れた。

## 5. 系：V に埋め込める codomain と V の retracts

**系 5.1。** W↪V が P の mono、Z∈M、a,b:Z⇉W なら Eq(a,b)∈M。W 自身の M-membership はこの主張には不要。

証明。W↪V を後合成しても equalizer は変わらないので、定理 4.1 を適用する。□

**系 5.2。** V の全 retracts は M に属する。

証明。R --s→V --r→R, rs=id_R とする。s は id_V と sr の equalizer。V∈M と定理 4.1 より R∈M。□

より一般に、Z∈M が V に埋め込めるなら Z の全 retracts は M に属する。id_Z と retract に対応する idempotent の equalizer に系 5.1 を使えばよい。

これは任意の M-object の retract 閉性の証明ではない。

**系 5.3。** 任意の集合 I、mono W↪V^I、Z∈M、および a,b:Z⇉W について Eq(a,b)∈M。従って V の積に埋め込める M-object の全 retracts も M に属する。

証明。a,b を V^I に後合成し、その各座標を a_s,b_s:Z⇉V (s∈I) とする。定理 4.1 と同様に、fg x:F→Eq(a,b) の Z への像を、一つの mono v:E(Y_t)↪Z（各 sort の component 数≤𝔠）を経由させる。各 s について別々の α_s と

    k_(a,s),k_(b,s):T_(α_s)・Z_*⇉Y_t

を取り、a_s v=i_(α_s)E(k_(a,s)), b_s v=i_(α_s)E(k_(b,s)) と表す。全 s の α_s に共通の上界を取る必要はない。C の中で

    coproduct_(s∈I) (T_(α_s)・Z_*) ⇉ Y_t → Q

を coequalizer とすれば、E(Q)↪E(Y_t) は全 E(k_(a,s)),E(k_(b,s)) を同時に等化する。元の fg map は E(Q) を経由し、v が mono なので E(Q)↪Eq(a,b) が得られる。I が空の場合も同じ構成（または Eq(a,b)=Z）でよい。□

## 6. V^(2) の自己等化子：carrier が小さい始域の場合

V^(2) を値域とする一般の M-equalizer は未解決だが、始域も V^(2) の場合は処理できる。より一般の形で述べる。

R∈C の各 sort R_i が可算（有限・空も許す）とし、

    C^R_α=T_α・R,
    V^R_α=E(C^R_α),
    V^R=colim_(α<ω_1) V^R_α

と置く。遷移は mono なので V^R∈M。各 sort は

    (V^R)_i ≅ Kappa^(R_i)

である。右から左への全射性には、R_i が可算なので各座標の stage を一つの α<ω_1 に集められることを使う。

**補題 6.1（ZFC）。** |Y_i|≤𝔠 の Y∈K と θ:E(Y)→V^R に対し、θ は一段階 V^R_α を経由する。その stage map は明示的な K-map k:C^R_α→Y の E 像である。

### 証明

各 i と r∈R_i について、座標射を合成した

    φ_(i,r):Ω^(Y_i)→Kappa

は M_2-equivariant。旧ノートの scalar stage-factorization lemma を使うと、ある α_(i,r) と τ_(i,r):T_(α_(i,r))→Y_i により評価写像として表せる。これらは可算個なので、共通の α<ω_1 を取り、restriction による前合成で全 τ_(i,r) の始域を T_α に揃える。

    k_i(t,r)=τ_(i,r)(t)

と置くと、集合写像による前合成 θ_(α,i)=Ω^(k_i) が得られ、stage injection i_α と合成すると θ_i になる。i_α が mono なので、θ の両作用との可換性と二本の構造射に関する自然性は θ_α に反映される。Ω 値関数が点を分離することから、k_i は M_1-equivariant で、二本の構造射とも可換。従って k:C^R_α→Y は K の射で θ_α=E(k)。

R_i=∅ なら k_i は空写像であり、その sort では座標射を使わない。R_i≠∅ かつ Y_i=∅ の場合は Ω^(Y_i)=1 の M_2-固定点を Kappa に送れないので、そもそも θ は存在しない。□

**定理 6.2（ZFC）。** R,S∈C が各 sort で可算なら、任意の a,b:V^R⇉V^S に対して Eq(a,b)∈M。

### 証明

j:W↪V^R を equalizer とし、fg x:F→W を取る。jx は一段階 V^R_β を経由する：

    jx=i^R_β t.

|T_β|≤𝔠 と R_i の可算性により、C^R_β の各 sort の carrier は≤𝔠。従って補題 6.1 を a i^R_β,b i^R_β に適用し、共通の α で

    a i^R_β=i^S_α E(k_a),
    b i^R_β=i^S_α E(k_b),
    k_a,k_b:C^S_α⇉C^R_β

と書く。C 内でこれらの coequalizer r:C^R_β→Q を取り、E(r):E(Q)↪V^R_β を得る。stage injection i^S_α が mono なので、t は E(Q) を経由する。合成 i^R_β E(r):E(Q)↪V^R は a,b を equalize し、W への mono を与える。これが x の D-subobject による因子化。□

特に R=S=R_2=(Ω² --id,id--> Ω²) とすれば、**任意の二射 V^(2)⇉V^(2) の equalizer は M に属する**。また各 V^R の全 retracts は M に属する。retract を id と対応する idempotent の equalizer として表せばよい。

**系 6.3。** Z が、各 sort |Y_(j,i)|≤𝔠 である D-subobjects E(Y_j)↪Z の directed union として表されるとする。S∈C が各 sort で可算なら、任意の a,b:Z⇉V^S の equalizer は M に属する。より強く、その equalizer 自体が D-subobjects の directed union である。

証明。各 stage への a,b の制限に補題 6.1 を使うと、その equalizer W_j↪E(Y_j) は C 内の coequalizer の E 像として得られ、従って W_j∈D。W_j は Eq(a,b) と E(Y_j) の交わりなので directed family をなし、その union は Eq(a,b)。□

この議論で得た有界性は、各 source stage V^R_β の上で射が一つの target stage を経由するという意味である。V^R→V^S 自体が一つの target stage を経由すると主張していない。

**適用範囲の境界。** 補題 6.1 は |Y_i|≤𝔠 という carrier の上界を要する。補題 3.1 の component 数の上界では代用できない。従って一般の Z∈M と a,b:Z⇉V^(2) に対する結論はまだない。

### 6.4 双対 Hom の有限支持部分には carrier の上界がある

**補題 6.4（ZFC）。** fg F∈P に対し、(QF)_i の有限支持元全体からなる M_1-subset (QF)_(i,fs) の cardinality は≤𝔠。

証明。n≥1 に対し、e_n:ω→ω を

    e_n(k)=k  (k<n),
    e_n(k)=0  (k≥n)

とする。各 sort F_i の左 M_2・右 M_1 に関する有限生成集合 Γ_i を取る。h∈QF_i が e_n h=h を満たせば、x=m_2 g·m という生成表示について

    h(m_2 g·m)=h((m_2 g·m)·e_n)=m_2 h(g·m e_n)。

m e_n は m(0),…,m(n−1) だけで決まるので、その候補は可算個。従って h は可算個の値 h(g·m e_n) で決まり、

    |Fix(e_n;QF_i)|≤ω^ω=𝔠。

有限支持 S の元 h は S⊆{0,…,n−1} となる n に対し e_n h=h を満たす。逆に e_n h=h なら {0,…,n−1} が h の支持になる。よって

    (QF)_(i,fs)=union_(n≥1) Fix(e_n;QF_i)

であり、その cardinality は≤𝔠。有限支持性が作用で保たれるので、この集合は M_1-subset でもある。Γ_i が空の場合も QF_i は一元集合で、同じ結論になる。□

### 6.5 p が同型なら carrier 全体を mono 圧縮できる

Y∈C の p_Y が同型なら、第1 sort を p_Y で第0 sort と同一視することにより、Y は

    Y=(A --id,s--> A)

という形にできる。ここで A は有限支持 M_1-set、s は M_1-equivariant endomorphism。A の cardinality には制限を置かない。s=id の場合は対角図式 ΔA である。

**補題 6.5（ZFC）。** p_Y が同型である Y∈C と任意の fg t:F→E(Y) に対し、

    F --t'--> E(Y') --E(q)↪ E(Y)

という因子化が存在する。ここで Y'∈C、p_(Y') も同型、各 sort |Y'_i|≤𝔠、q:Y↠Y' は objectwise-surjective な K-map。

証明。Y=(A --id,s--> A) としてよい。転置 u=t^♯:Y→QF の sort maps を u_0,u_1 とし、QF の構造射を P,Q:QF_0⇉QF_1 と書く。自然性より

    u_1=P u_0,
    Q u_0=u_1 s=P u_0 s。

M_1-equivariant map

    q_0:A→(QF_0)^ω,
    q_0(a)=(u_0(s^n a))_(n<ω)

を取り、その像を A' とする。各座標は有限支持元なので、補題 6.4 により

    A'⊆((QF)_(0,fs))^ω,
    |A'|≤𝔠^ℵ0=𝔠。

さらに q_0 が equivariant であるため、元 a の有限支持は列 q_0(a) 全体の共通の有限支持となる。従って A' は有限支持 M_1-set である。

列の左 shift は q_0(a) を q_0(s a) に送るから、A' 上の equivariant endomorphism s' を定める。Y'=(A' --id,s'--> A') と置くと Y'∈C で、q=(q_0,q_0):Y↠Y' は K-map。

h_0:A'→QF_0 を第0座標への射影、h_1=P h_0 とする。任意の a∈A に対し

    Q h_0 q_0(a)=Q u_0(a)=P u_0(s a)=h_1 s' q_0(a)

なので、q_0 の全射性により Qh_0=h_1s'。従って h=(h_0,h_1):Y'→QF は K-map で、u=hq。転置すれば求める因子化を得る。q が objectwise-surjective なので E(q) は mono。□

s=id の場合は、単に A'=im(u_0) と取ればよい。この補題は rank-2 の固定点だけでなく carrier 全体を小さくする。p_Y が同型であり、残る s の挙動を可算列に記録できる点を使っている。

### 6.6 p が同型の大きい図式から V^(2) への equalizer も安全

**定理 6.6（ZFC）。** Y∈C の p_Y が同型とする。各 s∈I に対して R_s∈C が各 sort で可算であり、W↪prod_(s∈I)V^(R_s) が mono なら、任意の a,b:E(Y)⇉W の equalizer は M に属する。

証明。fg x:F→Eq(a,b) の E(Y) への合成に補題 6.5 を使い、carrier≤𝔠 の Y' を経由する mono 因子化を取る。各 s 座標への二射 E(Y')⇉V^(R_s) に補題 6.1 を適用し、適当な α_s と明示的な

    k_(a,s),k_(b,s):T_(α_s)・R_s⇉Y'

を得る。系 5.3 と同様に、これらを coproduct にまとめた C 内の coequalizer Y'→B を取り、E(B)↪E(Y')↪E(Y) を作る。この mono は a,b を equalize し、x は E(B) を経由する。従って Eq(a,b)∈M。□

特に **任意に大きい有限支持 A に対し、Eq(E(ΔA)⇉V^(2))∈M**。A=Cont([0,κ],Ω_discrete) のように、一成分で rank-2-supported elements が任意に多い例も、この対角形なら安全である。

また、Z が p_(Y_j) の同型な D-subobjects E(Y_j) の directed union なら、同じ W への任意の a,b:Z⇉W の equalizer も M に属する。各 stage との交わりが定理 6.6 により M に属し、それらの directed union が全 equalizer になるためである。さらに一般に、Z の各 fg map がそのような D-subobject を経由すれば、定理 6.6 の局所的な証明を同様に適用できる。

**一般の Y∈C との区別。** 補題 6.4 から、t^♯:Y→QF の第0成分の像は常に≤𝔠 と分かる。しかし Y_1 に有限支持性は仮定されておらず、両 sort の像を取った図式が C に属する保証もない。補題 6.5 を p_Y が同型でない一般の Y に適用したとは主張しない。

### 6.7 p が同型の証人だけでは実際の候補全体を覆えない

この小節だけは、N に加え、[No.1 の既存ノート §6・定理8](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md) の因子化下界を採用する。これは非 coreflectivity という結論だけでなく、次の具体的な入力である：

> 無限基数 κ、Y_κ=(Cont([0,κ],Ω_discrete) --inclusion,d_κ^*--> Ω^[0,κ])、および第0成分が 0 での評価である ψ_κ:Y_κ→B に対し、Y_κ→Z→B という任意の C 内の因子化は κ≤|H_1(Z_0)| を満たす。

ここで d_κ は κ 未満で後続点へ送り、κ を固定する写像、B=(Ω⇉1)。N の下で Y_κ∈C であることも既存の構成による。X=E(B) は二元生成であり、特に ambient fg。j_0=E(ψ_κ):X→E(Y_κ) と置く。

**系 6.7（N と上記の既存因子化下界を条件とする）。** κ>2^𝔠 なら、j_0 は p_Y が同型であるどの Y∈C に対しても

    X→E(Y)→E(Y_κ)

と因子化しない。最後の射には mono 性を要求していない。

証明。そのような因子化があれば、X の有限生成性と補題 6.5 により、さらに

    X→E(Y')→E(Y)→E(Y_κ),
    Y'∈C,  |Y'_i|≤𝔠

と因子化する。N の下での E の fullness と faithfulness により、これは

    Y_κ→Y'→B

という ψ_κ の因子化へ双対化できる。採用した下界から

    κ≤|H_1(Y'_0)|≤ω^(|Y'_0|)≤ω^𝔠=2^𝔠

となり、κ の選び方に反する。□

従って、p_Y が同型の D-subobjects だけを局所証人に用いるクラスは、これらの条件の下で実際の M より真に小さい。E(Y_κ)∈D⊆M 自身が反例になる。§6.5–§6.6 が一般の M の問題を解いていないことを、具体的な fg map によって区別できる。

## 7. 一般の M-equalizer 閉性に対する正確な epi 条件

この節では N を「非可算 measurable cardinal が存在しない」とする。N の下では E:K^op→P が fully faithful。以下の同値定理の必要性に、この fullness を使う。十分性と成分数の制限への帰着は ZFC の議論である。

次の条件を (EQ_C^epi) と呼ぶ。

> Y∈C、W∈M、a,b:E(Y)⇉W、および fg F と t:F→E(Y) が at=bt を満たすとする。このとき、Y'∈C と objectwise-surjective な K-map q:Y→Y'、および h:Y'→QF が存在し、
>
>     t^♯=h q,
>     a E(q)=b E(q)
>
> を満たす。

第一式は、h の転置 t':F→E(Y') を用いた t=E(q)t' と同値。q が objectwise-surjective なので、E(q):E(Y')↪E(Y) は mono である。

**定理 7.1（N の下での同値）。** 次の三条件は同値。

1. 任意の Z,W∈M と a,b:Z⇉W について Eq(a,b)∈M。
2. (EQ_C^epi) が成り立つ。
3. (EQ_C^epi) が、各 sort |π_0(Y_i)|≤𝔠 を満たす Y に対して成り立つ。

### 1 ⇒ 2：ここだけ N を使う

E(Y)∈D⊆M なので、L=Eq(a,b) は仮定により M に属する。at=bt より t は x:F→L を経由する。M の定義から、ある Y'∈C と

    F --t'--> E(Y') --d↪ L --j↪ E(Y)

を取り、j d t'=t とできる。

N の下での fullness により j d=E(q) となる K-map q:Y→Y' が存在する。j d が mono なので各 E(q)_i:Ω^(Y'_i)→Ω^(Y_i) は injective。q_i が全射でなければ、像の外の一点でだけ値の異なる二つの Ω 値関数が同じ前合成を与えるため矛盾する。従って q は objectwise-surjective。

t=E(q)t' を転置すると t^♯=(t')^♯ q。j d が equalizer を経由するため aE(q)=bE(q) も成り立つ。□

### 2 ⇒ 3

適用する Y を制限するだけなので直ちに従う。

### 3 ⇒ 2：mono 圧縮による帰着、ZFC

任意のデータ Y,W,a,b,F,t に補題 3.1 を適用し、

    q_0:Y↠Y_t,
    t=E(q_0)t_t,
    |π_0((Y_t)_i)|≤𝔠

を取る。条件 3 を Y_t、aE(q_0),bE(q_0)、t_t に適用し、q_1:Y_t↠Y' と h:Y'→QF を得る。q=q_1q_0 は objectwise-surjective で、

    t^♯=h q_1q_0=h q,
    aE(q)=aE(q_0)E(q_1)=bE(q_0)E(q_1)=bE(q)

となる。□

### 2 ⇒ 1：ZFC

j:L↪Z を a,b:Z⇉W の equalizer とし、fg x:F→L を取る。Z∈M より jx=v t となる mono v:E(Y)↪Z, Y∈C を取れる。(EQ_C^epi) を av,bv:E(Y)⇉W と t に適用し、q:Y↠Y' と t':F→E(Y') を得る。

    v E(q):E(Y')↪Z

は mono で a,b を equalize するため、L への mono を誘導する。x はこの D-subobject を経由するので L∈M。□

条件 3 では、得られる Y' の component 数も自動的に≤𝔠 となる。objectwise-surjective q:Y→Y' は π_0(Y_i)→π_0(Y'_i) を全射にするためである。

**旧 (EQ_C) との差。** 新条件は中間射 E(Y')→E(Y) の mono 性、同値に q の objectwise-surjectivity を明記している。また対象 W の範囲は H_fg 全体ではなく M。旧 H_fg の一般等化子閉性の失敗だけから、この新条件の成否は決まらない。この節は必要十分条件への帰着であり、条件自体の証明・反証ではない。

## 8. 残る問題

今回の改善によって、旧 V-codomain の証明で mono 性を失っていた箇所は修復できた。V と、その部分対象を codomain とする equalizer については、新候補 M でも閉性を証明できる。

V^(2) や任意の W∈M への、component 数だけを仮定する stage-factorization は依然として未証明。component 圧縮は rank-2-supported elements の個数を抑えず、その個数には既に無界性の例がある。§6 では、carrier が小さい場合に加え、p_Y が同型で carrier を小さく圧縮できる場合を処理した。§6.7 の条件付き境界は、その範囲が実際の M 全体を覆わないことを示す。

一般の M の equalizer 閉性は、N の下で §7 の (EQ_C^epi) に正確に帰着したが、その成否は未解決。一般の retract 閉性、M と H_fg の一致・不一致、十分大きい filtered-colimit 閉性について、本ノートは結論を追加しない。
