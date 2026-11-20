# Compactness と有限テスト射の証明監査

監査日：2026-11-15

対象：`prior_notes/sset_coorthogonality_investigation.md` §§5–6。

**状態：内部証明監査。** 以下の仮定の下で、元ノートの compact Hausdorff テスト射および degreewise finite な始域に関する結論は成立すると判断した。本稿は検査可能な証明を書き直したものであり、形式検証・外部査読・文献上の新規性の確認は行っていない。元ノートの他の節まで監査したという意味ではない。

## 1. 設定と主張

集合論は選択公理を含む ZFC とする。小圏 \(C\) を固定し、通常の presheaf category

\[
\mathcal K=\mathbf{Set}^{C^{op}}
\]

で考える。射は通常の自然変換である。位相は一部の対象に付ける補助構造であり、母圏の射に連続性を課すわけではない。

presheaf の大きさは、sort を区別した台集合の非交和の濃度

\[
|X|=\left|\coprod_{c\in\operatorname{Ob}C}X(c)\right|
\]

とする。以後

\[
\kappa=\max(\aleph_0,|\operatorname{Mor}C|),\qquad
\lambda=\kappa^+
\]

と置く。\(S=\{f_i:U_i\to V_i\mid i\in I\}\) は集合で添字付けられた射の族とし、

\[
\mathcal A_S=
\{X\in\mathcal K\mid
\mathcal K(X,f_i):\mathcal K(X,U_i)\to\mathcal K(X,V_i)
\text{ がすべての }i\in I\text{ について全単射}\}
\]

を充満・同型閉部分圏として扱う。空の族も許す。この場合は \(\mathcal A_S=\mathcal K\) である。

本稿で証明するのは次の二つである。

1. 各 \(U_i,V_i\) の各 sort に compact Hausdorff 位相を入れ、すべての presheaf 構造写像および \(f_i\) の成分を連続にできるなら、\(\mathcal A_S\) は locally \(\lambda\)-presentable かつ coreflective である。
2. 各 \(U_i(c)\) が有限なら、\(V_i\) に制限を課さなくても \(\mathcal A_S\) は coreflective である。ここから最終クラスの accessibility までは主張しない。

sSet では \(C=\Delta\) の射は可算個なので、第一の結論は locally \(\aleph_1\)-presentable となる。第二の仮定は degreewise finite という意味であり、全次数を合わせた simplex の総数が有限である必要はない。

## 2. Pure 部分対象の定義と小さいものの構成

\(\mathcal K\) を、各 \(c\in C\) を sort とし、各 \(\alpha:c\to d\) に unary operation \(X(\alpha):X(d)\to X(c)\) を対応させる多ソート代数の圏として表す。関手の恒等射・合成に関する等式を課す。この signature の大きさは \(\kappa\) 以下である。

包含 \(Y\subseteq X\) を **pure** と呼ぶのは、\(Y\) の有限個の元をパラメータとする有限連立方程式が \(X\) で解を持てば、同じパラメータを固定して \(Y\) でも解を持つときである。式中の変数は有限個で、それぞれ sort を指定する。**自由変数・パラメータがない存在文も含める。** 例えば、sort \(c\) の \(\exists z\,(z=z)\) を含めるので、pure inclusion について \(X(c)\ne\varnothing\Rightarrow Y(c)\ne\varnothing\) が成り立つ。

これは、この代数的表示における positive primitive formula による purity の記述である。背景の定義と表示は [R1, §2.1, Definition 2.6] で確認できる。

**補題 2.1.** 任意の \(X\in\mathcal K\) と、その sort を区別した台集合の部分集合 \(Z\)（\(|Z|\le\kappa\)）について、

\[
Z\subseteq Y\subseteq X,\qquad |Y|\le\kappa
\]

となる pure subpresheaf \(Y\) が存在する。

**証明。** まず \(Z\) をすべての unary operation で閉じて \(Y_0\) とする。操作の数が \(\kappa\) 以下なので \(|Y_0|\le\kappa\) である。

\(Y_n\) を構成したとする。\(Y_n\) の有限個の元をパラメータに持つ有限方程式系は、すべて合わせても \(\kappa\) 個以下である。そのうち \(X\) 内で解ける各系について解を一組選び、現れる有限個の元を追加し、構造写像で閉じて \(Y_{n+1}\) を作る。無パラメータの方程式系もこの操作に含める。各段階で大きさは \(\kappa\) 以下に保たれる。

\(Y=\bigcup_{n<\omega}Y_n\) と置く。これは大きさ \(\kappa\) 以下の subpresheaf である。有限個のパラメータはある一段階 \(Y_n\) に揃うので、それらを使う \(X\) で可解な有限方程式系の解は \(Y_{n+1}\) に入る。従って \(Y\subseteq X\) は pure である。□

## 3. Compact Hausdorff な標的への延長

**補題 3.1.** \(D\in\mathcal K\) の各 \(D(c)\) に compact Hausdorff 位相があり、すべての \(D(\alpha)\) が連続であるとする。pure inclusion \(Y\subseteq X\) と任意の自然変換 \(h:Y\to D\) に対し、\(h\) を延長する自然変換 \(\widetilde h:X\to D\) が存在する。

ここで \(h\) は集合値 presheaf の射であり、その連続性は仮定していない。

**証明。** 各 \(x\in X(c)\) に対し \(D(c)\) に値を取る変数 \(z_x\) を用意し、積空間

\[
P=\prod_{c\in\operatorname{Ob}C}\prod_{x\in X(c)}D(c)
\]

を考える。必要な因子は非空である。実際、\(X(c)\ne\varnothing\) なら purity より \(Y(c)\ne\varnothing\) であり、\(h_c:Y(c)\to D(c)\) の存在から \(D(c)\ne\varnothing\) となる。選択公理により \(P\) は非空であり、Tychonoff の定理により compact である。

次の条件を \(P\) 上に課す。

\[
D(\alpha)(z_x)=z_{X(\alpha)(x)}
\quad(\alpha:c\to d,\ x\in X(d)),
\]

\[
z_y=h_c(y)
\quad(c\in C,\ y\in Y(c)).
\]

各条件が定める部分集合は閉である。前者は連続写像と Hausdorff 空間の対角の閉性、後者は点集合の閉性による。

これらから有限個の条件を選ぶ。現れる変数は有限個である。標的 \(D\) の演算を \(X\) の演算に置き換え、指定値 \(h(y)\) をパラメータ \(y\in Y\) に置き換えると、\(X\) において \(z_x=x\) を解に持つ有限方程式系が得られる。purity により、この系を \(Y\) 内で解ける。その解に \(h\) を適用すれば、元の有限個の条件を \(D\) 内で満たす値が得られる。残る変数には任意の値を選べるため、これらの条件の有限交叉は \(P\) 内で非空である。

compactness により全閉条件の交叉も非空である。その元が、すべての構造写像を保存し、\(Y\) 上で \(h\) と一致する写像 \(\widetilde h\) を与える。□

## 4. Compact なテスト射の coorthogonality

**定理 4.1.** §1 の第一の主張が成立する。

**証明。** まず \(\mathcal A_S\) が小余極限に閉じることを確認する。\(X_j\in\mathcal A_S\) からなる小図式について、

\[
\mathcal K(\operatorname{colim}_jX_j,f_i)
\cong\lim_j\mathcal K(X_j,f_i)
\]

であり、右辺は全単射からなる自然変換の極限なので全単射である。従って、この余極限は母圏で計算したものがそのまま \(\mathcal A_S\) の余極限になる。

次に、\(X\in\mathcal A_S\) と pure inclusion \(Y\subseteq X\) を取る。各 \(i\) について \(Y\perp f_i\) を示す。

持ち上げの存在について、\(h:Y\to V_i\) を補題 3.1 で \(\widetilde h:X\to V_i\) に延長する。\(X\perp f_i\) によって持ち上げ \(\widetilde g:X\to U_i\) が存在し、その \(Y\) への制限が \(h\) の持ち上げになる。

一意性について、\(g_0,g_1:Y\to U_i\) が \(f_i g_0=f_i g_1\) を満たすとする。kernel pair

\[
W_i=U_i\times_{V_i}U_i
\]

を取る。各 \(W_i(c)\) は \(U_i(c)\times U_i(c)\) の閉部分空間である。これは \(f_i(c)\) の連続性と \(V_i(c)\) の Hausdorff 性による。従って \(W_i\) は点ごとに compact Hausdorff で、構造写像も連続である。

二射をまとめた射 \((g_0,g_1):Y\to W_i\) を \(t:X\to W_i\) に延長する。二射影を \(p_0,p_1:W_i\to U_i\) とすると、\(f_i p_0t=f_i p_1t\) である。\(X\perp f_i\) の一意性より \(p_0t=p_1t\)。\(Y\) に制限して \(g_0=g_1\) を得る。従って \(Y\in\mathcal A_S\) である。

この一意性の証明には kernel pair を使って二射を同時に延長することが必要である。二射を別々に延長しただけでは、延長後も \(f_i\) との合成が等しいとは限らない。

固定した \(X\in\mathcal A_S\) に対し、

\[
P_X=\{Y\subseteq X: |Y|\le\kappa,\ Y\in\mathcal A_S\}
\]

を包含で順序付ける。これは集合であり、\(\lambda\)-directed である。実際、\(\lambda\) 未満、すなわち \(\kappa\) 個以下の \(P_X\) の元の合併は大きさ \(\kappa\) 以下である。補題 2.1 により、それを含む大きさ \(\kappa\) 以下の pure subpresheaf を取れ、今示したことからこれは \(P_X\) に属する。また各 \(X\) の元はそのような部分対象に入るので、\(\operatorname{colim}P_X=X\) である。

大きさ \(\kappa\) 以下の presheaf \(Y\) は母圏で \(\lambda\)-presentable である。直接には、\(Y\) から \(\lambda\)-filtered colimit への射を指定する値は \(\kappa\) 個以下であり、構造保存に必要な等式も \(\kappa\) 個以下なので、一つの段階で実現できる。二つの射の一致も同じく \(\kappa\) 個以下の等式で一段階に移せる。サイズによるこの presentability 判定は [R1, Convention 2.3 後] にも記されている。

\(\mathcal A_S\) の包含は小余極限を保存するので、これらの \(Y\in\mathcal A_S\) は同部分圏内でも \(\lambda\)-presentable である。固定 signature 上で大きさ \(\kappa\) 以下の対象の同型類は集合をなし、そのうち \(\mathcal A_S\) に属するものを代表に選べる。前段の表示から、これらは \(\lambda\)-filtered colimit によって \(\mathcal A_S\) の全対象を生成する。

従って \(\mathcal A_S\) は locally \(\lambda\)-presentable である。その包含 \(J:\mathcal A_S\hookrightarrow\mathcal K\) は locally presentable categories の間の余極限保存関手なので、随伴関手定理により右随伴を持つ。従って \(\mathcal A_S\) は coreflective である。□

この証明の \(\lambda\) は \(C\) によって決まり、射の族 \(S\) の濃度や各テスト対象の大きさの上界を必要としない。

## 5. Mono 条件の trace による coreflection

有限始域の証明に必要な補題を独立に記す。

**補題 5.1.** \(\mathcal L\) が locally presentable category、\(M\) がその mono の集合なら、\(\mathcal T={}^\perp_{\mathcal L}M\) は \(\mathcal L\) 内で monocoreflective である。

**証明。** coorthogonality class なので \(\mathcal T\) は小余極限に閉じる。また strong quotient に閉じる。実際、strong epi \(p:X\to Y\)、\(X\in\mathcal T\)、\(m:A\hookrightarrow D\in M\)、\(h:Y\to D\) を取る。\(X\perp m\) より \(mu=hp\) となる \(u:X\to A\) がある。strong epi と mono の持ち上げ性により、\(mv=h\) を満たす \(v:Y\to A\) が存在する。\(m\) が mono なので一意であり、\(Y\perp m\) となる。

\(B\in\mathcal L\) を固定する。locally presentable category は well-powered で strong-epi–mono factorization を持つ。従って、始域が \(\mathcal T\) に属する \(B\) の部分対象を、同型を除いて集合個の代表 \(j_a:T_a\hookrightarrow B\) として集められる。その余積からの射を strong-image 分解し、

\[
\coprod_a T_a\twoheadrightarrow T_B\xhookrightarrow{j_B}B
\]

を得る。余積閉性と strong-quotient 閉性から \(T_B\in\mathcal T\) である。

任意の \(t:T\to B\)、\(T\in\mathcal T\) を strong-image 分解すると、その像も \(\mathcal T\) に属する。従って像の包含は選んだ代表の一つと同型であり、\(t\) は \(j_B\) を経由する。その分解は \(j_B\) が mono であることから一意である。よって \(j_B\) は \(B\) の \(\mathcal T\)-coreflection である。空の余積にも同じ構成を使え、初対象の strong image も \(\mathcal T\) に属するので、退化した場合も処理される。□

## 6. 点ごとに有限な始域、任意の終域

**定理 6.1.** 各 \(U_i(c)\) が有限なら、\(V_i\) に制限を課さなくても \(\mathcal A_S\) は coreflective である。

**証明。** 各 \(f_i\) を presheaf category 内で成分ごとに像分解する。

\[
U_i\xrightarrow{e_i}I_i\xrightarrow{m_i}V_i,
\]

\(e_i\) は成分ごとに全射、\(m_i\) は mono である。任意の \(X\) について

\[
X\perp f_i\quad\Longleftrightarrow\quad
(X\perp e_i\text{ かつ }X\perp m_i).
\]

実際、\(\mathcal K(X,m_i)\) は単射である。集合写像 \(a:A\to B\)、\(b:B\to D\) について、\(b\) が単射で \(ba\) が全単射なら、\(ba\) の全射性から \(b\) も全射となり、\(b\) は全単射、従って \(a\) も全単射となる。この事実を Hom の合成に適用すればよい。

\(U_i,I_i\) は点ごとに有限である。すべての sort に有限離散位相を付けると、構造写像と \(e_i\) は連続である。定理 4.1 より

\[
\mathcal L={}^\perp\{e_i:i\in I\}
\]

は locally \(\lambda\)-presentable で coreflective である。包含と右随伴を \(J:\mathcal L\hookrightarrow\mathcal K\dashv R:\mathcal K\to\mathcal L\) と書く。

\(X\in\mathcal L\) について、随伴の自然な同型により

\[
\mathcal L(X,Rm_i)\cong\mathcal K(JX,m_i).
\]

さらに \(Rm_i\) は \(\mathcal L\) 内の mono である。例えば任意の \(X\in\mathcal L\) に対して右辺の写像が単射であることから直接従う。従って \(\mathcal L\) 内の

\[
\mathcal T={}^\perp_{\mathcal L}\{Rm_i:i\in I\}
\]

は補題 5.1 により coreflective である。

最初の Hom の同値性から、\(\mathcal T\) を \(\mathcal K\) の充満部分圏として見たものは \(\mathcal A_S\) と一致する。coreflective な二つの包含を合成すると、その右随伴も合成できるので、\(\mathcal A_S\hookrightarrow\mathcal K\) は右随伴を持つ。□

この証明は、locally presentable な中間圏 \(\mathcal L\) を作ってから、その内部の mono 条件を処理する。二つの任意の coreflective subcategory の交わりが coreflective だと仮定しているわけではない。また、最後の trace による部分圏 \(\mathcal T\) の accessibility は、この証明だけでは示していない。

## 7. 有限 2-truncated テストと cosk₂ に対する帰結

\(\mathcal K_2=\mathbf{Set}^{\Delta_{\le2}^{op}}\) を 2-truncated simplicial sets の圏とする。\(U_0,U_1,U_2\) が有限で、\(f:U\to V\) が任意の射なら、定理 6.1 により

\[
{}^\perp_{\mathcal K_2}\{f\}
\]

は coreflective である。これは、\(X\) も有限に制限した主張ではない。**すべての、無限なものも含む 2-truncated simplicial sets** に対する結論である。\(V\) も各次数で有限なら、定理 4.1 によりさらに locally \(\aleph_1\)-presentable と分かる。

有限な 2-truncated \(U\) から full simplicial set へ進む場合も、

\[
(\operatorname{cosk}_2 U)_n
\cong\operatorname{Hom}_{\mathcal K_2}
(\operatorname{tr}_2\Delta[n],U)
\]

は各 \(n\) で有限である。固定した \(n\) について \(\operatorname{tr}_2\Delta[n]\) の各 sort は有限であり、三つの有限集合間の写像の組は有限個しかないからである。この coskeleton の随伴・公式の標準的な背景は [R2] を参照。

従って \(\operatorname{cosk}_2 U\) は degreewise finite であり、定理 6.1 を sSet に適用すると

\[
{}^\perp_{\mathbf{sSet}}
\{\operatorname{cosk}_2f\}
\]

も coreflective である。\(U,V\) ともに有限な 2-truncated objects なら、こちらも locally \(\aleph_1\)-presentable である。

有限個の非退化 simplex を持つ full simplicial set を始域にする場合も、それは degreewise finite なので同じ除外結果が適用される。これと「各次数で有限」、および「2-truncated」は区別する。

したがって、テスト射 \(f\) 自体の有限サイズ上限を増やす探索から、非 coreflective な class を定義する個々の有限 \(f\) が見つかることはない。有限探索で扱える持ち上げの失敗や quotient-closure の失敗は、この肯定結果と両立する。有限探索範囲内に coreflection 候補がない場合も、探索範囲外の対象を排除したことにはならない。

本監査は探索器の実装や探索を実施したものではない。有限探索の数学的な対象範囲を確認したものである。

## 8. 監査結果と確認の範囲

元ノート §§5–6 の議論に、結論を壊す欠落は見つからなかった。特に次を明示して点検した。

- 無パラメータの存在条件と空の sort。
- 位相を付ける対象と、通常の presheaf を母圏にすることの区別。
- 一意性を降ろす際の kernel pair と、その compact Hausdorff 性に必要な連続性。
- \(\kappa\) サイズの pure 部分対象、\(\lambda\)-directed な表示、および母圏から部分圏への presentability の移送。
- 像分解後の二つの Hom 条件の同値性。
- locally presentable な中間圏で mono 条件を扱うことと、strong image による trace 構成。
- 有限 2-truncated テストと、その coskeleton 拡張が肯定結果の範囲に入ること。

これらは無限対象を含む証明の内部点検であり、有限計算を根拠とする判定ではない。本稿によって一般の \(P_{\mathbf{sSet}}\) や ZFC 独立性が解決したとは主張しない。

## 参考資料

[R1] S. Cox, J. Feigert, M. Kamsma, M. Mazari-Armida and J. Rosický, *Cofibrant generation of pure monomorphisms in presheaf categories*, arXiv:2506.20278v2. §2.1, Convention 2.3 後、Definition 2.6。

https://arxiv.org/html/2506.20278v2

2026-11-15 に本文を確認。本稿では unary-algebra 表示、purity の定義、およびサイズと presentability の背景として用いた。上記 coorthogonality 定理そのものを、この論文の定理として帰属させていない。

[R2] The Stacks Project, Equation 14.19.0.1 (Tag 0181), Section 14.19, *Coskeleton functors*。

https://stacks.math.columbia.edu/tag/0181

2026-11-15 に上記の随伴の式を確認。同資料の記号 `sk_n` は、ここでの切断関手 `tr_n` に対応する。本監査では、その随伴から有限性を直接計算した。参照先の各補題の証明全体を再監査したという意味ではない。
