# Z-null クラスの内部部分対象：サイズ上界と拡大による増大

2026-11-15、第9段階。母圏は Ab、Hom と Ext は通常の代数的 Hom と Ext¹_Z。N は「可測基数が存在しない」。各結果について N が必要かを区別する。

2026-11-16 の[続報](transfinite_z_null_towers_2026-11-16.md)：可算共終度の極限後の Ext 供給を解決し、構成を全可算順序数へ延長した。連続な全射塔の極限射影の全射性も解消した。V=L では後続段を任意の非零 torsion-free T-対象で作れる。非可算共終度の極限の T 所属と非 well-poweredness は依然未証明。以下は第9段階時点の証明・到達点である。

**到達点。** 固定した可算群 B=G_b の T-内部部分対象を調べた。torsionless な核には ZFC で |E|≤2^{2^{ℵ₀}} という上界があり、N の下でその上界を実現した。さらに拡大を反復し、同じ B に入る内部単射 E_n→B（n≥1、|E_n|=beth_{n+1}）と E_ω→B（|E_ω|=beth_{ω+1}）を構成した。E_ω→B の核の整数 radical の長さは正確に ω である。

**非 well-poweredness はまだ示していない。** この族は集合個であり、すべてのサイズは beth_{ω+1} 以下である。一般の P の否定・独立性も未証明。従来の「小さい対象の積」では得られなかった、固定標的の内部部分対象を拡大で増やす方法を得た段階である。

状態：直接の構成・導出は `PROOF_RECONSTRUCTED`。主担当による点検までで、独立査読・形式検証・新規性確認は未実施。文献定理の採用は下記の確認範囲に限定した。有限近似による検証は行っていない。

## 1. 固定したクラスと内部単射の正確な条件

$$
\mathcal T=\{A:\operatorname{Hom}(A,\mathbb Z)=0\}
=I_{\{\mathbb Z\to0\}},\qquad
\mathcal F=\{K:\operatorname{Hom}(T,K)=0\text{ for all }T\in\mathcal T\}.
$$

T は全射商・直和・拡大に閉じる。各 A の T-部分群の和 t(A) も T に属し、T の coreflector を与える。F は部分群・積・拡大に閉じ、T∩F={0}。また A/t(A)∈F：そこに非零の T-部分群があれば、その逆像は t(A) の T-対象による拡大となり、t(A) の最大性に反する。これらは ZFC の事実である。

**内部単射の判定。** E,B∈T に対し、m:E→B が T 内の単射であることと ker m∈F は同値。

実際、Hom(T,m) の核は Hom(T,ker m)。加法性により、全 T∈T についてこの核が零であることが内部単射性に等しい。F の核は通常の torsion-free 群である。非零 torsion 部分群は T に属してしまうためである。

一般の内部単射では A=im m≤B と置く。A は E の全射商なので T に属し、

$$0\longrightarrow K\longrightarrow E\longrightarrow A\longrightarrow0,
\qquad K\in\mathcal F,\quad A\in\mathcal T,\quad |A|\le|B|.\tag{1}$$

を調べればよい。以下の構成はさらに A=B、すなわち通常の群として全射でもある内部単射を与える。

以前の p_b:P₀=G_a×_M G_b→G_b はこの最初の例である。P₀,G_b∈T、ker p_b≅Z∈F なので、p_b は T 内の単射だが Ab 内の単射ではない。

## 2. Torsionless な核には一様な上界がある（ZFC）

**命題。** E∈T、0→K→E→A→0 が完全で K が torsionless、すなわち Z の積に埋め込めるとする。κ=max(ℵ₀,|A|) と置けば

$$|E|\le 2^{2^\kappa}.\tag{2}$$

**証明。** 長完全列の一部は

$$0=\operatorname{Hom}(E,\mathbb Z)\longrightarrow
K^*\xrightarrow{\delta}\operatorname{Ext}(A,\mathbb Z),
\qquad K^*=\operatorname{Hom}(K,\mathbb Z).
$$

従って δ は単射。A の κ 以下の階数の自由分解から |Ext(A,Z)|≤2^κ となる。一方、torsionless 性は評価射 K→Z^{K*} の単射性を意味するので、|K|≤ℵ₀^{2^κ}=2^{2^κ}。完全列から同じ上界が E にも成り立つ。∎

これは核についての条件であり、以前に扱った「テストの始域が torsionless」という除外とは異なる。B=G_b は可算なので、その内部部分対象のうち核が torsionless なものは、すべてサイズ 2^c 以下（c=2^{ℵ₀}）となる。

**境界。** K∈F を torsionless と同一視してはいけない。後述の E₂→B の核は F に属するが torsionless ではなく、|E₂|>2^c となる。

## 3. 上界に達する内部部分対象を、同じ G_b 上で作る

この節以降の構成には N を仮定する。用いる有限座標性は Hom(Z^J,Z)=Z^(J) である。[前段階の定理と出典](finite_coordinate_trial_2026-11-15.md)を参照。

### 3.1 独立な拡大類を c 個用意する

[既存の p進群](algebraic_candidates_2026-11-15.md)と同じ p=2、固定した w,b∈Z_p、R₀=Z[1/p] を用いる。I は |I|=c の集合とし、w,b と合わせて Q 上代数的に独立となる (a_i)_{i∈I}⊂Z_p を選ぶ。元の a をこの族に含めてよい。Z_p の Q 上の超越次数が c なので、この選択が可能である。

$$
M=(R_0+R_0w)\cap\mathbb Z_p,\qquad
G_t=\bigl(R_0(1,0)+R_0(0,1)+R_0(wt,w)\bigr)\cap\mathbb Z_p^2,
\quad B=G_b.
$$

第2座標射影 π_t:G_t→M の核は Z。各 i について P_i=G_{a_i}×_M B とし、拡大

$$0\longrightarrow\mathbb Z\longrightarrow P_i\longrightarrow B\longrightarrow0$$

の類を e_i∈Ext(B,Z) とする。B は以後ずっとこの同じ可算群である。

**独立性の確認。** 有限 F⊂I に対する B 上の fiber product P_F は、座標表示では

$$
P_F=\left(R_0^{F\sqcup\{b,y\}}+
R_0\bigl((wa_i)_{i\in F},wb,w\bigr)\right)
\cap\mathbb Z_p^{F\sqcup\{b,y\}}.
$$

P_F は標準整数格子を含み、p進 filtration に関して pure である。その completion は表示された Z_p の有限冪。h:P_F→Z は p進 completion に延長し、標準基底上の値が整数だから、その延長の係数は整数である。上の特別なベクトルの像が整数であることと w,b,(a_i) の代数的独立性から、すべての係数は零。従って Hom(P_F,Z)=0。

0→Z^F→P_F→B→0 の connecting map は

$$\mathbb Z^F\longrightarrow\operatorname{Ext}(B,\mathbb Z),
\quad(n_i)\longmapsto\sum_{i\in F}n_i e_i$$

であり、前の零 Hom により単射。従って (e_i)_{i∈I} は Z-線形独立である。

### 3.2 Fiber product 全体を取る

E₁=∏_B(P_i)_{i∈I} と置く。これは各 P_i→B に対する同じ B 上の fiber product であり、単なる群の直積ではない。選択公理により各 fiber に同時に元を選べるので、

$$0\longrightarrow\mathbb Z^I\longrightarrow E_1
\xrightarrow{m_1}B\longrightarrow0\tag{3}$$

は完全。N による Hom(Z^I,Z)=Z^(I) と e_i の独立性から、connecting map が単射になり、Hom(E₁,Z)=0 となる。核 Z^I∈F なので m₁ は T-内部単射である。

$$\boxed{|E_1|=2^{|I|}=2^{\mathfrak c}.}\tag{4}$$

従って (2) の可算標的に対する上界に達した。有限 fiber product は以前の可算の計算に含まれ、可算添字なら有限座標性の部分に N は不要である。

## 4. 拡大を重ねて torsionless な核の上界を超える

### 4.1 一回の増大に必要な補題

**拡大補題（N）。** X∈T とし、Ext(X,Z) に J 個の Z-線形独立な元 (e_j) があるとする。それぞれを表す Z による拡大の X 上の fiber product を Y とすると、

$$0\longrightarrow\mathbb Z^J\longrightarrow Y\longrightarrow X\longrightarrow0\tag{5}$$

で Y∈T、Y→X は T-内部単射である。

証明は §3.2 と同じで、Hom(X,Z)=0 と connecting map Z^(J)→Ext(X,Z) の単射性を使う。有限座標性は Y そのものへの仮定ではなく、**核 Z^J の整数双対の計算**に使っている。この点が、前段階の「小さい群の積を始域にする」方法との違いである。

### 4.2 次の拡大類が十分に存在する

**補題（ZFC）。** 無限基数 μ に対し

$$\operatorname{rank}_{\mathbb Q}\operatorname{Ext}(\mathbb Z^\mu,\mathbb Z)
\ge 2^\mu.\tag{6}$$

ここで rank_Q A は dim_Q(Q⊗A) を表す。

文献入力は Ext(Z^ω,Z) に無限位数の元があること。より強い rank_Q Ext(Z^ω,Z)=2^c が [Keef–Koşan–Žemlička, *On virtually regular modules and rings*, Lemma 4.18](https://www.karlin.mff.cuni.cz/~zemlicka/pdf/VirtuallyRegular.pdf) に示されている。

**(6) の導出。** μ を μ 個の可算ブロックに分ければ、D=⊕_μ Z^ω が Z^μ の部分群になる。Ab の Ext²=0 から

$$\operatorname{Ext}(\mathbb Z^\mu,\mathbb Z)
\twoheadrightarrow\operatorname{Ext}(D,\mathbb Z)
\cong\prod_\mu\operatorname{Ext}(\mathbb Z^\omega,\mathbb Z).
$$

各成分の無限位数の元により、右辺は Z^μ を部分群として含む。その torsion-free rank は 2^μ。Q⊗− の完全性から (6) が従う。∎

0→Z^μ→X→X₀→0 が完全なら、同じ Ext²=0 により Ext(X,Z)→Ext(Z^μ,Z) も全射。従って (6) の独立な元を X 上へ持ち上げ、(5) を繰り返せる。

### 4.3 有限段の tower

beth₀=ℵ₀、beth_{α+1}=2^{beth_α}、極限では上限、とする。E₀=B、μ_n=beth_n（n≥1）と置き、§3 の E₁（μ₁=c）から出発する。

帰納的に

$$0\longrightarrow\mathbb Z^{\mu_n}\longrightarrow E_n
\xrightarrow{q_n}E_{n-1}\longrightarrow0\qquad(n\ge1)\tag{7}$$

を作る。次段では Ext(E_n,Z)→Ext(Z^{μ_n},Z) の像で μ_{n+1}=2^{μ_n} 個の独立な元を選んで持ち上げ、拡大補題を適用する。これにより

$$E_n\in\mathcal T,\qquad
m_n=q_1\cdots q_n:E_n\to B\text{ は内部単射かつ全射},
\qquad |E_n|=\beth_{n+1}.\tag{8}$$

核 K_n=ker m_n は、K₁=Z^c から出発する torsionless 群の有限回の拡大なので F に属する。

特に |E₂|=beth₃>beth₂=2^c。(2) によって K₂ は torsionless ではない。さらに選んだ拡大類の Z^{μ₁} への制限も独立だから、Hom(K₂,Z)→Hom(Z^{μ₂},Z) は零で、Hom(K₂,Z)≅Hom(Z^{μ₁},Z)。従って

$$R_{\mathbb Z}(K_2)=\mathbb Z^{\mu_2}\ne0,
\qquad R_{\mathbb Z}^2(K_2)=0.\tag{9}$$

ここで R_Z(A)=∩_{h:A→Z}ker h。K₂∈F と R_Z(K₂)≠0 は両立する。内部単射の核に課すべき条件を、torsionless 性へ強めてはならない。

## 5. 可算逆極限まで進められる

E_ω=lim_n E_n とする。(7) は全射の逆列なので、各射影 E_ω→E_n と m_ω:E_ω→B は全射である。

Z は inverse-limit slender：全射 bonding map を持つ可算逆列の極限から Z への任意の射は、ある段への射影を経由する。この ZFC の事実は [Conner–Herfort–Kent–Pavešić, *Inverse limit slender groups*, Definition in §1, Theorem 3.6, Corollary 3.11](https://arxiv.org/pdf/2106.06032) で確認した。各 E_n の双対が零なので、

$$\operatorname{Hom}(E_\omega,\mathbb Z)=0.$$

K_ω=ker m_ω は lim_n K_n であり、∏_n K_n の部分群。F の積・部分群閉性から K_ω∈F。従って

$$\boxed{m_\omega:E_\omega\longrightarrow B
\text{ は }\mathcal T\text{-内部単射かつ全射。}}\tag{10}$$

集合としての sections を各 q_n に選ぶと、E_ω の元は E₀ の元と各段の核の元によって一意にパラメータ化できる。これは集合の全単射であって、群の直積分解ではない。従って

$$
|E_\omega|=|B|\prod_{n\ge1}|\mathbb Z^{\mu_n}|
=2^{\sum_{n\ge1}\mu_n}
=2^{\beth_\omega}=\beth_{\omega+1}.
\tag{11}
$$

ここでも固定標的は同じ可算群 G_b のままである。

**限定。** 参照した inverse-limit slenderness は可算逆列についての定理である。任意の非可算 ordinal に添字付けられた tower へ無条件に拡張してはいけない。

## 6. 一般の内部部分対象を radical の長さで整理する

この節は ZFC。R(A)=R_Z(A) とし、

$$R^0A=A,\quad R^{\alpha+1}A=R(R^\alpha A),\quad
R^\lambda A=\bigcap_{\alpha<\lambda}R^\alpha A$$

と定める。各 A では部分群の下降列がいずれ安定し、その安定値は t(A) である。実際、安定値は整数双対が零であり、任意の T-部分群は自然性によりすべての段に含まれる。従って

$$K\in\mathcal F\iff(\exists\alpha)\ R^\alpha K=0.\tag{12}$$

この transfinite iteration は標準的な idempotent radical の構成であり、[Dugas–Fay–Shelah, *Singly cogenerated annihilator classes*, §I, p.128](https://shelah.logic.at/files/95421/265.pdf) に記述されている。Keef–Koşan–Žemlička の上記論文では、torsion-free な場合の右辺を free-reduced と呼ぶ。t(A) と一段目の R(A) は区別する。

### 6.1 長さを固定すれば、すべての内部部分対象に上界が出る

固定した B∈T に対し κ₀=max(ℵ₀,|B|) とし、集合 ordinal の範囲で

$$\kappa_{\alpha+1}=2^{2^{\kappa_\alpha}},\qquad
\kappa_\lambda=2^{\sum_{\alpha<\lambda}\kappa_\alpha}
\quad(\lambda>0\text{ は極限})\tag{13}$$

を定める。内部単射 m:E→B の核を K とすると、

$$R^\theta K=0\quad\Longrightarrow\quad |E|\le\kappa_\theta.\tag{14}$$

**証明。** A=im m とし、X_α=E/R^αK と置く。X₀=A、すべての X_α は E の商なので T に属する。

後続段では

$$0\longrightarrow R^\alpha K/R^{\alpha+1}K
\longrightarrow X_{\alpha+1}\longrightarrow X_\alpha\longrightarrow0.$$

左端は torsionless なので (2) を適用できる。極限 λ では X_λ→∏_{α<λ}X_α が単射であり、積のサイズは (13) 以下。R^θK=0 なら X_θ=E である。∎

**同値な判定。** 固定 B の T-内部部分対象が集合個であることは、その核の R-長さに一様な ordinal 上界があることと同値。

一方向は (14) と、有界サイズの群および B への射が同型を除いて集合個であることによる。逆に、内部部分対象が集合個ならその始域のサイズには一様な無限基数上界 μ がある。R の下降列は |K|⁺ 以下では安定し、(12) より安定値は零なので、μ⁺ を共通の ordinal 上界にできる。

これは、固定 B の核に対する判定である。F 全体で長さが無界な群を見つけただけでは、固定 B の非 well-poweredness は得られない。

### 6.2 今回の可算極限の核の長さは正確に ω

(7) から 0→Z^{μ_n}→K_n→K_{n-1}→0。R の自然性と左端の torsionless 性から、帰納的に R^nK_n=0 となる。

射影 K_ω→K_n に自然性を適用すると、R^ωK_ω はすべての射影の核に含まれる。従って R^ωK_ω=0。

一方、ある有限 n で R^nK_ω=0 なら、B の可算性と (13)–(14) から |E_ω|≤beth_{2n} となり、(11) に反する。よって

$$\boxed{R^nK_\omega\ne0\ (n<\omega),\qquad R^\omega K_\omega=0.}\tag{15}$$

有限の長さを固定する方法はすべて超えたが、一つの ordinal 上界 ω の範囲に留まっている。

## 7. 文献の位置付けと残った問題

Cox–Poveda–Trlifaj, [*Approximation properties of torsion classes*, Theorem 2](https://arxiv.org/pdf/2406.02829) は、T の deconstructibility と ω₁-strongly compact cardinal の存在の同値を示している。これは T の内部部分対象のサイズを直接判定する結果ではない。T の covering / coreflective 性と、今回の well-poweredness の問題も区別する。

Keef–Koşan–Žemlička, Example 4.21 / Remark 4.22 は、free-reduced 群の R-長さが任意に長くなる構成を与える。しかし、それらが固定 G_b の内部部分対象の核になるとは示していない。固定した B 上の T-拡大には K*↪Ext(B,Z) という追加制約があり、任意の F-群を核に取り替えることはできない。

今回得た family は (8) と (10) であり、任意の基数を超える family ではない。次に必要なのは、(14) の一様な ordinal 上界を破るか、逆にその上界を証明することである。構成を続けるなら、少なくとも次の点を処理する必要がある。

1. 極限後の E にも、サイズを増やすだけの独立な Ext(E,Z) の類を供給できるか。有限段の証明は、直前の核が Z の積であることを使っており、そのままでは E_ω に適用できない。
2. より長い逆極限で T 所属と固定標的への全射性を保てるか。可算 inverse-limit slenderness だけで非可算極限を処理したことにはならない。

**今回未確立：** G_b の内部部分対象が集合個か真のクラスか、T 全体の well-poweredness、非 well-powered な小さい I_S の確立、P の否定と独立性。これらを (15) や巨大な始域の存在だけから結論しない。

## 8. 境界・自己点検

- 標的 B=G_b とクラス T=I_{Z→0} は全構成で固定した。拡大に用いる補助射・独立な拡大類は変わるが、対象クラスを定義するテストは変えていない。
- E_n→B は T の内部単射であり、Ab の単射ではない。通常の全射との両立は T が abelian category ではないことと矛盾しない。
- E_n が以前の A_{π_a} に属するとは主張しない。P₀→G_b の A_{π_a}-coreflection と今回の大きい T-内部部分対象は矛盾しない。
- 上界 (2)、radical による判定 (12)–(14)、Ext の下界 (6) は ZFC。大きな Z の積の双対を使う拡大構成は N の下で記述した。可算逆列に対する slenderness 自体には N は不要。
- R(K)=0 と R^∞(K)=0 を区別した。(9) はその相違が今回の固定標的で実際に現れる例である。
- E_ω の集合としてのパラメータ化を、群としての直積分解と取り違えていない。もし T-対象の単なる積であれば、前段階の有限座標性の除外が適用される。
- 零の核・零の標的では恒等射／零対象が通常どおり含まれる。空の fiber product は基準 B であり、独立な拡大類を選ばない場合も整合する。
