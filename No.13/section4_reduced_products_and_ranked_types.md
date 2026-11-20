# No.13 草稿 §4 の補題：フィルターによる被約積とランク付き往復型

2026-11-20。[証明草稿](no13_reduced_products_proof_draft.md) の §4 は、対象によらない一つの完備度 \(\kappa\) で被約積が閉じることを示す。その中心にある「被約積は、座標ごとのランク付き往復型の一致を保存する」という Feferman–Vaught 型の補題は、本文では略述されているだけだった。AI による検証でこの補題を独立に述べるよう指摘されたので、主張と証明をここに書き下す。この文書は Claude (Opus 5.5) が作成した。人間による検証はまだ行っていない。

## 0. 設定

- \(\Sigma\) は多ソート署名で、記号は単項関数だけとする（草稿 §2 の前層署名）。ソートは空でもよい。項は、変数に単項関数を合成したものである。原子式は、同じソートの項 \(u,v\) について \(u(x)=v(y)\) の形をしている。
- \(\chi\) は無限正則基数とする。式は \(L_{\chi,\chi}\) で考える。すなわち、否定、\(<\chi\) 個の式の連言・選言、\(<\chi\) 個の変数の存在量化（ブロック量化）を使う。
- 量化ランク \(\mathrm{qr}\) を次で定める。原子式は \(0\)、\(\mathrm{qr}(\neg\varphi)=\mathrm{qr}\varphi\)、\(\mathrm{qr}(\bigwedge\Phi)=\mathrm{qr}(\bigvee\Phi)=\sup_{\varphi\in\Phi}\mathrm{qr}\varphi\)、\(\mathrm{qr}(\exists\bar y\,\varphi)=\mathrm{qr}\varphi+1\)。
- **組**は、長さ \(<\chi\) の順序数で添字付けた元の列で、各位置のソートを指定したものとする。指定したソートの列を \(\bar s\) と書く。
- **フィルターによる被約積** \(\prod^F A_i\) は草稿 §4 と同じものとする。\(F\) は \(I\) 上の固有フィルターである。ソート \(s\) の元は、ある \(X\in F\) 上で定義された部分切断 \(f\)（各 \(i\in X\) で \(f(i)\in(A_i)_s\)）の同値類である。二つの部分切断は、\(F\) に属する集合上で一致するとき同値とする。単項関数は座標ごとに作用させる。全ソートが非空なら、通常の被約積と一致する。

## 1. ランク付き往復型

構造 \(A\) と、ソート列 \(\bar s\) の組 \(\bar a\) に対し、\(\mathrm{tp}_\beta(A,\bar a)\) を \(\beta\) に関する再帰で定める。

- \(\mathrm{tp}_0(A,\bar a)\) は、\(A\models\varphi[\bar a]\) となる原子式 \(\varphi(\bar x)\)（\(\bar x\) はソート \(\bar s\)）全体の集合である。
- \(\mathrm{tp}_{\beta+1}(A,\bar a)\) は次の対である。第一成分は \(\mathrm{tp}_\beta(A,\bar a)\)。第二成分は、長さ \(<\chi\) の各ソート列 \(\bar s'\) に集合 \(\{\mathrm{tp}_\beta(A,\bar a^\frown\bar c):\bar c\in A^{\bar s'}\}\) を対応させる関数である。
- 極限 \(\beta\) では \(\mathrm{tp}_\beta(A,\bar a)=(\mathrm{tp}_\gamma(A,\bar a))_{\gamma<\beta}\) とする。

**補題 0（集合性）。** \(\bar s\) と \(\beta\) を固定すると、全ての \((A,\bar a)\) にわたる \(\mathrm{tp}_\beta(A,\bar a)\) の値は、\(\Sigma,\chi,\bar s,\beta\) だけで決まる一つの集合 \(T_\beta(\bar s)\) に収まる。

*証明。* \(\beta\) に関する帰納法による。\(T_0(\bar s)\) は原子式全体の冪集合に含まれる。後続段階では
\[
T_{\beta+1}(\bar s)\subseteq T_\beta(\bar s)\times\prod_{\bar s'}\mathcal P\bigl(T_\beta(\bar s^\frown\bar s')\bigr)
\]
が成り立つ。長さ \(<\chi\) のソート列全体は集合である。極限段階は直積で抑えられる。∎

定義から直ちに次の二つが従う。

- (a) \(\gamma\le\beta\) のとき、\(\mathrm{tp}_\beta\) が等しければ \(\mathrm{tp}_\gamma\) も等しい。
- (b)（往復性）\(\mathrm{tp}_{\gamma+1}(A,\bar a)=\mathrm{tp}_{\gamma+1}(B,\bar b)\) とする。このとき任意の \(\bar s'\) と \(\bar c\in A^{\bar s'}\) に対し、\(\mathrm{tp}_\gamma(A,\bar a^\frown\bar c)=\mathrm{tp}_\gamma(B,\bar b^\frown\bar d)\) となる \(\bar d\in B^{\bar s'}\) が存在する。\(A,B\) を入れ替えても同じである。特に、\(A\) のあるソート列の組が存在すれば、\(B\) にも同じソート列の組が存在する。

## 2. 補題 A（Feferman–Vaught 型）

**補題 A。** \(F\) を \(I\) 上の固有な \(\chi\)-完備フィルターとし、\((A_i)_{i\in I}\) と \((B_i)_{i\in I}\) を \(\Sigma\)-構造の族とする。\(\bar a=([f_k])_{k<\ell}\in\prod^F A_i\) と \(\bar b=([g_k])_{k<\ell}\in\prod^F B_i\) は同じソート列 \(\bar s\) の組で、\(\ell<\chi\) とする。ある \(X\in F\) と順序数 \(\beta\) について、次の二つが成り立つと仮定する。

- \(X\subseteq\bigcap_k(\mathrm{dom}f_k\cap\mathrm{dom}g_k)\)
- 各 \(i\in X\) で \(\mathrm{tp}_\beta(A_i,(f_k(i))_k)=\mathrm{tp}_\beta(B_i,(g_k(i))_k)\)

このとき、\(\mathrm{qr}\varphi\le\beta\) を満たす全ての \(L_{\chi,\chi}\) 式 \(\varphi(\bar x)\) について、
\[
\textstyle\prod^F A_i\models\varphi[\bar a]\iff\prod^F B_i\models\varphi[\bar b].
\]

仮定は代表の選び方によらない。代表を取り替えても、変わるのは \(<\chi\) 個の \(F\) の元の補集合の上だけである。それらの共通部分は \(\chi\)-完備性により \(F\) に属するので、\(X\) をそれで縮めればよい。

*証明。* 式の構成に関する帰納法で示す。帰納法の主張は、全ての \(\beta\ge\mathrm{qr}\varphi\)、全ての族と組について同時に成り立つ、という形にしておく。

**(i) 原子式。** \(\varphi\) を \(u(x_k)=v(x_l)\) とする。演算は座標ごとに定義されているので、\(u([f_k])=[i\mapsto u(f_k(i))]\) である。二つの類が等しいのは、代表が \(F\) の元の上で一致するときである。従って \(\prod^F A_i\models\varphi[\bar a]\) は
\[
Z_A=\{\,i\in\mathrm{dom}f_k\cap\mathrm{dom}f_l: A_i\models u(f_k(i))=v(f_l(i))\,\}\in F
\]
と同値である。\(Z_B\) も同様に定める。(a) により \(X\) 上では \(\mathrm{tp}_0\) が一致するので、\(Z_A\cap X=Z_B\cap X\) となる。\(X\in F\) だから
\[
Z_A\in F\iff Z_A\cap X\in F\iff Z_B\cap X\in F\iff Z_B\in F.
\]

**(ii) 否定・連言・選言。** 部分式の量化ランクは \(\le\mathrm{qr}\varphi\le\beta\) である。同じ \(\bar a,\bar b,X\) で各部分式に帰納法の仮定を適用し、被約積の水準でブール結合を取る。ここで、真になる座標集合が座標ごとに計算できるとは主張していない（§4 の注意を参照）。

**(iii) 存在量化。** \(\varphi=\exists\bar y\,\psi(\bar x,\bar y)\) とし、\(\bar y\) のソート列を \(\bar s'\)（長さ \(<\chi\)）、\(\gamma=\mathrm{qr}\psi\) とする。このとき \(\gamma+1\le\beta\) なので、(a) により \(X\) 上で \(\mathrm{tp}_{\gamma+1}\) が座標ごとに一致する。

\(\prod^F A_i\models\varphi[\bar a]\) と仮定し、\(\prod^F A_i\models\psi[\bar a,\bar c]\) となる組 \(\bar c=([h_m])_m\)（ソート列 \(\bar s'\)）を取る。\(Y=X\cap\bigcap_m\mathrm{dom}h_m\) と置くと、\(\chi\)-完備性により \(Y\in F\) である。

各 \(i\in Y\) で \((h_m(i))_m\in A_i^{\bar s'}\) である。往復性 (b) と選択公理により、次を満たす \(\bar d(i)\in B_i^{\bar s'}\) を選ぶ。
\[
\mathrm{tp}_\gamma\bigl(A_i,\bar a(i)^\frown\bar c(i)\bigr)=\mathrm{tp}_\gamma\bigl(B_i,\bar b(i)^\frown\bar d(i)\bigr)
\]
\(Y\) 上の部分切断を \(e_m(i)=\bar d(i)_m\) で定めると、\(\bar d=([e_m])_m\) は \(\prod^F B_i\) のソート列 \(\bar s'\) の組である。組 \(\bar a^\frown\bar c\) と \(\bar b^\frown\bar d\) は、\(Y\) とランク \(\gamma\ge\mathrm{qr}\psi\) について補題の仮定を満たす。長さ \(\ell+\mathrm{len}(\bar y)\) は \(\chi\) が無限基数なので \(<\chi\) である。帰納法の仮定から \(\prod^F B_i\models\psi[\bar b,\bar d]\) となり、従って \(\prod^F B_i\models\varphi[\bar b]\) である。逆向きも対称に示せる。∎

この証明は超フィルターも Łoś の定理も使わない。\(F\) に要るのは固有性と \(\chi\)-完備性だけである。

## 3. 補題 B（セルへの分解）

**補題 B。** \(F\) を \(I\) 上の固有な \(\kappa\)-完備フィルターとし、\(I=\bigsqcup_{t\in T}I_t\) を \(|T|<\kappa\) 個のセルへの分割とする。

- **零集合**とは、補集合が \(F\) に属する集合のことである。零でないセルを**非零セル**と呼ぶ。
- 非零セル \(I_t\) 上の**跡フィルター**を \(F_t=\{Y\subseteq I_t: Y\cup(I\setminus I_t)\in F\}\) と定める。

このとき、各 \(F_t\) は \(I_t\) 上の固有な \(\kappa\)-完備フィルターである。さらに、制限による写像
\[
\textstyle r:\prod^F_{i\in I}A_i\longrightarrow\prod_{t\ \text{非零}}\ \prod^{F_t}_{i\in I_t}A_i,\qquad [f]\mapsto\bigl([f|_{\mathrm{dom}f\cap I_t}]\bigr)_t
\]
は \(\Sigma\)-構造の同型である。

*証明。*

- **\(F_t\) の性質。** \(\emptyset\in F_t\) は \(I\setminus I_t\in F\)、すなわち \(I_t\) が零であることと同値である。従って非零セルでは \(F_t\) は固有である。\(\kappa\)-完備性は \(\bigcap_j(Y_j\cup(I\setminus I_t))=(\bigcap_jY_j)\cup(I\setminus I_t)\) から従う。
- **well-defined。** \(\mathrm{dom}f\in F\) なら \((\mathrm{dom}f\cap I_t)\cup(I\setminus I_t)\supseteq\mathrm{dom}f\) なので、\(\mathrm{dom}f\cap I_t\in F_t\) である。一致集合についても同様である。
- **鍵となる計算。** 各非零 \(t\) で \(Y_t\in F_t\) とすると、\(\bigcup_tY_t\) の補集合は
\[
\textstyle\bigcup_{t\ \text{非零}}(I_t\setminus Y_t)\ \cup\ \bigcup_{t\ \text{零}}I_t
\]
に含まれる。これは \(<\kappa\) 個の零集合の和集合である。零集合全体は \(\kappa\)-完備イデアルをなすので、この和集合も零である。従って \(\bigcup_tY_t\in F\) となる。
- **単射性。** \(r[f]=r[g]\) なら、各非零 \(t\) で、ある \(Y_t\in F_t\) 上で \(f=g\) である。上の計算より \(f\) と \(g\) は \(F\) の元の上で一致する。
- **全射性。** 各非零 \(t\) について \(Y_t\in F_t\) 上の部分切断 \(f_t\) が与えられたとする。それらを貼り合わせた \(f=\bigcup_tf_t\) は、上の計算により \(F\) に属する定義域を持ち、\(r[f]=([f_t])_t\) を満たす。
- **準同型性。** 単項関数はどちらの側でも座標ごとに作用するので、\(r\) はそれと可換である。

あるソートで、ある非零セルの因子が空なら、両辺ともそのソートは空になる。これは全単射性に含まれている。∎

## 4. 系（草稿 §4 の補題）

**系。** ある無限正則基数 \(\kappa\) が存在して、\(\mathcal D\) の対象の任意の族 \((A_i)_{i\in I}\) と、\(I\) 上の任意の固有な \(\kappa\)-完備フィルター \(F\) について、\(\prod^F A_i\in\mathcal D\) となる。

*証明。* \(\mathcal D\) は草稿 §2 の本質像で、前層署名の \(L_{\chi,\chi}\) 文の集合 \(S\) で公理化される。\(\mathcal D\) は前層圏の小極限、特に積で閉じる（草稿 §2）。

\(\alpha=\sup\{\mathrm{qr}\sigma:\sigma\in S\}\) と置く。補題 0 により \(T_\alpha(\emptyset)\) は集合である。\(\mathcal D\) の対象で実現される各 \(t\in T_\alpha(\emptyset)\) について、\(\mathrm{tp}_\alpha(A(t),\emptyset)=t\) となる \(A(t)\in\mathcal D\) を一つ選ぶ。\(\kappa\) は次を満たす正則基数とする。
\[
\kappa>\chi,\qquad \kappa>|T_\alpha(\emptyset)|,\qquad \kappa\ge\kappa(A(t))\ \text{（全ての }t\text{ について。草稿 §3 の補題の基数）}
\]
この \(\kappa\) は入力の族によらない。

族と \(F\) が与えられたら、\(I_t=\{i:\mathrm{tp}_\alpha(A_i,\emptyset)=t\}\) と置く。セルの数は \(<\kappa\) なので、補題 B により \(\prod^F A_i\cong\prod_{t\ \text{非零}}\prod^{F_t}_{i\in I_t}A_i\) となる。

非零 \(t\) を固定する。\(F_t\) は固有で \(\kappa\)-完備、従って \(\chi\)-完備である。補題 A を二つの族 \((A_i)_{i\in I_t}\) と \((A(t))_{i\in I_t}\) に、空の組と \(X=I_t\in F_t\) で適用する。すると全ての \(\sigma\in S\) について次が成り立つ。
\[
\textstyle\prod^{F_t}A_i\models\sigma\iff A(t)^{I_t}/F_t\models\sigma
\]
\(I_t\) は空でなく \(\kappa\ge\kappa(A(t))\) なので、草稿 §3 により \(A(t)^{I_t}/F_t\in\mathcal D\) であり、\(S\) を満たす。草稿 §4 冒頭の注意により、§3 の被約冪はここでの部分切断による定義と一致する。従って \(\prod^{F_t}A_i\models S\)、すなわち \(\prod^{F_t}A_i\in\mathcal D\) である。

最後に、\(\mathcal D\) は積で閉じるので \(\prod^F A_i\in\mathcal D\) である。∎

**注意（否定の扱い）。** 補題 A は、二つの被約積を比べる主張である。真になる座標集合を座標ごとに計算できるとは言っていない。草稿 §4.1 の例がこの区別を示している。\(I=\{0,1\}\)、\(F=\{I\}\)、因子は二元集合とする。直積では \(p=(0,0)\)、\(q=(1,1)\) に対して \(\exists x\,(x\ne p\wedge x\ne q)\) が真になる。ところが各座標では偽である。否定を被約積の水準で取る (ii) は、この例と整合する。

## 5. この文書で扱っていない点

検証報告では次の点も指摘されている。いずれもここでは扱っていない。

- 草稿 §2 の公理化を、公理の一覧として形式的に書き下すこと。
- §3.1 で \(\chi\le\delta\) を、§3.2 で \(\mu\) が \(A^+\) の演算の個数を上回ることを、それぞれ明記すること。
- §5 に、原著の命題 2.31 の注意と Adámek–Rosický (1996) を引用すること。
- 未解決問題の決着を主張しているので、外部の専門家に査読を依頼すること。
