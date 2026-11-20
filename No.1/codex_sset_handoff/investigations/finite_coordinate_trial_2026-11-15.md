# 有限座標性を固定テストとサイズ障害に適用する

2026-11-15、第8段階。母圏は Ab、Hom は通常の代数的準同型全体。以下で N は「可測基数が存在しない」。断りのない新しい結論は ZFC+N の下で述べる。

**今回の結論。** 有限座標性から固定テストの積に対する振る舞いを計算できる。ただし、今回試した「固定した小さい群の積を大きくして、slender な固定標的への因子化を妨げる」案には、逆に一様な因子化上界が得られた。大きな reduced product も、slender なテスト・標的からは見えない。以前の非自明な p進群のテストでは、標的を任意の積へ広げても coreflection を明示できる。

これは有限座標性を使う全構成の否定ではない。一般の P、slender な端点を持つ全テストの coreflectivity、I_S の well-poweredness は示していない。

状態：文献定理は `STANDARD`、直接の導出は `PROOF_RECONSTRUCTED`。主担当が証明と仮定・境界例を点検した。独立査読・形式検証・文献上の新規性確認は未実施。無限の主張を有限計算で認定していない。

## 1. 使用する有限座標性

アーベル群 H が slender とは、任意の準同型 Z^ω→H が有限個の座標を経由することをいう。可算積の各因子を任意のアーベル群にしても同じ性質が成り立つ。

一般の集合 I に対しては、Łoś–Eda theorem が、積から slender 群への射を有限個の可算完備超フィルターによる ultraproduct に因子化する。N の下ではこれらの超フィルターがすべて principal なので、任意の群族 (X_i) について自然な同型

$$
\Gamma_H:\bigoplus_{i\in I}\operatorname{Hom}(X_i,H)
\xrightarrow{\ \cong\ }
\operatorname{Hom}\!\left(\prod_{i\in I}X_i,H\right),
\qquad (h_i)\longmapsto\sum_i h_i\pi_i
\tag{1}
$$

を得る。全射性が上の定理であり、単射性は各座標の包含 X_i→∏X_i への制限で従う。有限和なので右辺は代数的準同型として定義できる。

出典：[Bergman, *Families of ultrafilters, and homomorphisms on infinite direct product algebras*, §4.1, (25)](https://math.berkeley.edu/~gbergman/papers/cap_ultra.pdf)。可測基数と可算完備超フィルターの関係は同論文 §1。可算 I なら (1) に N は不要である。射ごとに有限な台を得るのであって、全射に共通する有限個数の上界を主張していない。

## 2. 固定した slender なテストは積を因子ごとに判定する

S を Ab の射の集合とし、

$$
\mathcal A_S={}^\perp S,
\qquad
\mathcal I_S=\{X:\operatorname{Hom}(X,f)\text{ が単射 }(f\in S)\}
$$

と置く。各 f:U→V の **始域と終域がともに slender** だとする。(1) の自然性から

$$
\operatorname{Hom}\!\left(\prod_iX_i,f\right)
\cong\bigoplus_i\operatorname{Hom}(X_i,f).
\tag{2}
$$

直和で得られる射が全単射であることは各成分が全単射であることと同値。単射についても同様である。従って

$$
\boxed{\prod_iX_i\in\mathcal A_S\iff(\forall i)\ X_i\in\mathcal A_S,}
\qquad
\prod_iX_i\in\mathcal I_S\iff(\forall i)\ X_i\in\mathcal I_S.
\tag{3}
$$

特に両クラスは集合添字の積に閉じる。非空の冪 X^I を取っても所属は変わらない。空積は零群であり、両クラスに属する。始域 X_i 自身には slender 性を仮定していない。

積閉性だけから coreflectivity や well-poweredness は結論していない。

## 3. Reduced product を大きな試験対象にする場合

無限基数 κ について

$$
Z^{<\kappa}=\{x\in\mathbb Z^\kappa:|\operatorname{supp}(x)|<\kappa\},
\qquad B_\kappa=\mathbb Z^\kappa/Z^{<\kappa}
$$

と置く。ここでは κ の正則性は不要である。

**補題。** 任意の slender 群 H に対し Hom(B_κ,H)=0。

**証明。** h:B_κ→H と商射 q:Z^κ→B_κ を取る。(1) により hq は有限座標に依存するが、各座標の Z は ker q に含まれるので、すべての座標成分は零。(1) の単射性から hq=0、q の全射性から h=0。∎

B_κ は零ではない。定数列 1 の台は κ である。また κ を κ 個の互いに素な、各サイズ κ の集合に分割し、各部分集合の和集合の特性関数を取れば、B_κ に 2^κ 個の異なる元を得る。従って |B_κ|=2^κ であり、大きさは無界である。

しかし §2 のテスト集合に対しては、両 Hom が零なので **すべての B_κ が A_S に属する**。従って次の二つの直接案は障害を与えない。

- 始域 B_κ から固定した slender な B への射は零であり、零群を経由する。
- B_κ 自身を標的にすると、既に A_S に属するので、その coreflection は恒等射になる。

この計算は有限座標性だけの適用である。小さい群から B_κ への射を持ち上げる別の定理は、今回の証明には使用していない。

## 4. 固定した小さい因子の積による増大を排除する

### 4.1 因子化先の一様なサイズ上界

ここでは S の端点の slender 性は不要である。H を A_S の対象からなる **集合** とし、γ=max(ℵ₀,sup_{A∈H}|A|) と置く。B は固定した slender 群とする。

任意の族 X_i∈H と任意の h:∏_iX_i→B は、ある有限 F⊂I に対して

$$
\prod_iX_i\xrightarrow{\pi_F}\prod_{i\in F}X_i\xrightarrow{h_F}B
\tag{4}
$$

と因子化する。有限積は Ab の有限直和なので、中央の対象は A_S に属し、そのサイズは γ 以下である。A_S の直和閉性は Hom(⊕X_i,f)=∏Hom(X_i,f) から従う。

したがって、この型の始域のうち A_S に属するものに限れば、一様な A_S-因子化上界 γ がある。有限積とその B への射の同型を除いた選択肢も集合個しかない。この型の始域だけでは、A_S↓B の解集合条件の失敗を証明できない。

**限定。** 因子をサイズが無界な真のクラスから選ぶ場合は、残る一個の因子が既に大きい可能性がある。「有限座標」を「一様に小さい対象」と同一視してはいけない。

### 4.2 内部単射を作る場合にも制約がある

C⊂Ab を充満部分圏とし、各 X_i、積 X=∏X_i、slender な標的 B が C に属するとする。C の内部単射 m:X→B が存在するなら、**非零の X_i は有限個しかない**。

実際、m が有限 F を経由するとき、i∉F に対して mι_i=0。ι_i:X_i→X と零射は C の射なので、内部単射性から ι_i=0。座標射影との合成が 1_{X_i} だから X_i=0 となる。∎

これは ambient な単射と内部単射を同一視した議論ではない。特に積閉な I_S においても、slender な固定 B の内部部分対象を、非零の小さい因子を無限個並べるだけで作ることはできない。一般の内部部分対象のサイズ上界は得ていない。

## 5. 以前の固定した p進群のテストへの適用

### 5.1 固定したデータと slender 性

[以前の構成と全 Hom の計算](algebraic_candidates_2026-11-15.md)を使う。p=2、w,a,b∈Z_p は Q 上代数的に独立な固定元、R₀=Z[1/p] とし、

$$
M=(R_0+R_0w)\cap\mathbb Z_p,\qquad
G_t=\bigl(R_0(1,0)+R_0(0,1)+R_0(wt,w)\bigr)\cap\mathbb Z_p^2
\quad(t=a,b).
$$

第2座標への全射を π_t:G_t→M とし、**f=π_a を固定**する。前のノートの pullback P を、一般命題 P と区別するためここでは P₀ と書く。

$$
P_0=G_a\times_MG_b,\qquad p_b:P_0\to G_b,\qquad\rho:P_0\to M.
$$

G_a,G_b,M,P₀ はいずれも可算、torsion-free、reduced である。最後の性質は、Z_p の有限冪の部分群として ∩_n p^nX=0 であり、非零可除部分群を持てないことから従う。可算 reduced torsion-free 群は slender なので、(1)–(3) が適用できる。出典：[Lady, *Slender rings and modules*, Theorem 1, Example 1, p.399](https://msp.org/pjm/1973/49-2/pjm-v49-n2-p12-p.pdf)。

既に ZFC で確認した事実は、

$$
G_a,P_0\in\mathcal A_f,\quad G_b\notin\mathcal A_f,\quad
\operatorname{Hom}(G_a,G_b)=0,\quad
\operatorname{Hom}(P_0,M)=\mathbb Z\rho,\quad
\operatorname{Hom}(P_0,\mathbb Z)=0,
$$

および p_b:P₀→G_b が A_f-coreflection であること。

### 5.2 始域を大きな積にした計算

任意の集合 I に対して

$$
\operatorname{Hom}(G_a^I,G_b)=0.
\tag{5}
$$

従って f の始域のコピーを増やしても、G_b に向かう非零射は得られない。

一方、Hom(P₀,G_b)=Zp_b である。実際、h:P₀→G_b に対し π_bh=nρ となり、h−np_b は ker π_b≅Z に値を取るので零である。よって

$$
\operatorname{Hom}(P_0^I,G_b)\cong\mathbb Z^{(I)},\qquad
h=\sum_{i\in F}n_i p_b\pi_i
=p_b\left(\sum_{i\in F}n_i\pi_i\right).
\tag{6}
$$

この場合は有限部分積に留まらず、元の **一つの可算群 P₀** を経由する。

### 5.3 標的を任意の積にしても coreflection がある

**補題。** 充満部分圏 A⊂Ab が積閉であり、各 r_j:C_j→B_j が A-coreflection なら、∏r_j:∏C_j→∏B_j も A-coreflection である。

**証明。** ∏C_j∈A。任意の X∈A について Hom(X,∏r_j)=∏Hom(X,r_j) は全単射。これは X のサイズや積表示を仮定しない。∎

(3) により A_f は積閉なので、任意の集合 J について

$$
\boxed{p_b^J:P_0^J\longrightarrow G_b^J
\quad\text{は }\mathcal A_f\text{-coreflection。}}
\tag{7}
$$

非空 J では G_b^J∉A_f なので、これは対象が既にクラスに入る自明な場合ではない。空 J なら零群の恒等射になる。G_b^J 自身が slender だとは仮定しておらず、その標的への射全体に有限座標性を適用したのでもない。各成分の普遍性と A_f の積閉性を使っている。

この特定の f について、G_b の任意の積まで肯定範囲が広がった。全標的 B に対する coreflectivity は依然未決定である。

## 6. 適用範囲の境界

### 6.1 Z の積をテストの始域にする案は既存の肯定範囲

f:U→V の U が torsionless、すなわちある Z^D に埋め込める場合は、既に ZFC で coreflective と確認している。単射 f なら単射テストの一般結果による。ker f≠0 なら ker f は Z を含み、X⊥f の一意性が Hom(X,Z)=0 を強制する。U↪Z^D より Hom(X,U)=0 となり、

$$
{}^\perp f=\{X:\operatorname{Hom}(X,\mathbb Z)=0=\operatorname{Hom}(X,V)\}.
$$

逆包含も同じ埋め込みから従う。このクラスは商と直和に閉じ、各 B におけるクラス所属の部分群の和を取れば coreflector になる。

従って Z^I→V、特に Z^ω→Z^ω/Z^(ω) をテストにする直接案は反例にならない。ここには N を使わない。[既存監査](../audits/ab_grp_reassessment.md)の再確認であり、今回の新しい発見とは数えない。slender と torsionless は異なり、§5 の G_a は Hom(G_a,Z)=0 だが非零なので torsionless ではない。

### 6.2 小さい標的なら有限座標、とは言えない

ZFC で ω 上の nonprincipal ultrafilter U を取り、各座標を mod p に落としてから有限群 Z/p 内で U-limit を取ると、準同型

$$h:\mathbb Z^\omega\longrightarrow\mathbb Z/p$$

を得る。有限群の加法は U-limit と可換する。各標準基底 e_i は 0 に送るが、定数列 1 は 1 に送るので、h は有限座標を経由しない。これは通常の nonprincipal ultrafilter であり、可算完備性を要求しないから N と矛盾しない。

従って標的の有限性・可算性だけでは (1) を使えない。ただし §5 のテストでは torsion 標的はすべて A_f に属し、その coreflection は恒等射になる。nonslender な標的を選ぶことだけで反例が得られるわけでもない。

## 7. 今回どこまで進んだか

有限座標性は、固定テストに対する積の所属判定、大きな reduced product の零 Hom、因子化サイズの上界、内部単射の障害に使えた。しかし、いずれも今回の直接案では肯定側または反例候補の除外に働いた。

この方法をなお否定側に使うなら、(4) の一様上界を逃れる必要がある。例えば、因子自体が無界な族で有限座標の一個に大きさを残すか、slender でない固定標的への射を制御する構成が必要になる。§3 の B_κ についても、slender な標的への射と B_κ 自身を標的にする二案は処理されたが、別の固定標的への射全体は調べていない。

有限座標性の一般的な無効性、非 well-powered な I_S の構成、P の否定・ZFC 独立性は、いずれも主張しない。今回は有限座標性の検査に留め、別の道具による次の構成は開始していない。

第9段階の続報：[T=I_{Z→0} の内部部分対象](z_null_internal_subobjects_2026-11-15.md)では、拡大の核 Z^J の双対を有限座標性で計算する別の使い方が得られた。固定 G_b 上で拡大を反復し、可算逆極限まで大きな内部単射を構成した。§4 の「固定した小さい T-対象の通常の積」を始域にする構成ではないため、そこでの除外と矛盾しない。非 well-poweredness は依然未確立。
