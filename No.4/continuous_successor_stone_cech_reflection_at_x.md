# 後続操作が連続な場合の \(X\) の反射

**定理（ZFC）。** \(Y\in C\) のうち、指標空間上の後続操作が連続なものを
\(C_{\mathrm{cont}}\) とする。\(E(Y)\), \(Y\in C_{\mathrm{cont}}\), を含み、
周囲の前層圏 \(\mathcal P\) での全小極限と有向合併に閉じた最小の充満・
同型閉部分圏を \(\mathcal A_{\mathrm{cont}}\) とする。
固定した \(X=E(\omega\rightrightarrows 1)\) の
\(\mathcal A_{\mathrm{cont}}\)-反射が存在する。以下で反射射を構成する。

## 1. 指標空間と連続性の仮定

\(M=\mathrm{End}(\omega)\) とし、\(\omega\) には離散位相を入れる。
\(H(A)=\mathrm{Hom}_M(A,\omega)\) に各点収束位相を入れる。
\(Y=(Y_0\overset{p_Y,q_Y}{\rightrightarrows}Y_1)\) が \(C\) に属するとは、
\(Y_0\) の各点が有限支持を持ち、\(H(p_Y):H(Y_1)\to H(Y_0)\) が全単射で
あることをいう。\(S_Y=H(Y_0)\) と書く。\(h\in S_Y\) について
\(\widetilde h\,p_Y=h\) を満たす唯一の指標を \(\widetilde h\) と書き、
\[
 d_Y(h)=\widetilde h\,q_Y
\]
と定める。定理の仮定はこの \(d_Y:S_Y\to S_Y\) の連続性である。

\(S_Y\) はコンパクトな零次元 Hausdorff 空間である。各 \(y\in Y_0\) に
空でない有限支持 \(F_y\) を選ぶ。\(h(y)\notin F_y\) なら、\(F_y\) を
各点で固定して \(h(y)\) を動かす付け替えが同変性と矛盾する。従って
\(S_Y\) は \(\prod_y F_y\) の中で同変性の閉じた等式を課した部分空間である。

\(E(Y)_i=\omega^{Y_i}\) には出力への左作用と入力への右作用がある。
二本の構造射は \(p_Y,q_Y\) との前合成でソート 1 からソート 0 へ向かう。
\(X\to E(Y)\) は正確に \(h\in S_Y\) の選択である。実際、ソート 0
では \(X_0=M\) の恒等写像の像が \(h\) で、右作用との可換性がその
同変性を与える。ソート 1 では \(X_1=\omega\) の \(n\) の像は定数
\(n\) である。逆にこれらの指定から射が定まる。\(X\) はソート 0
の恒等写像とソート 1 の 0 で生成される。

## 2. \(\beta\mathbb N\) から作る一つの対象

\(K=\beta\mathbb N\) を \(\mathbb N\) 上の全超フィルターの Stone 空間、
\(s:K\to K\) を \(n\mapsto n+1\) による押し出しとする。主超フィルター
を自然数と同一視する。集合 \(A\subseteq\mathbb N\) に属するかを検査する
clopen 集合 \(\{U:A\in U\}\) が基底をなし、主超フィルターは稠密である。
次を用いる。
\[
 T=\left(C(K,\omega)
        \overset{\mathrm{incl},\,s^*}{\rightrightarrows}\omega^K\right),
 \qquad s^*g=g\circ s .
\]
第1の台 \(C(K,\omega)\) は、\(\mathbb N\) への制限で有限値の列全体と
同一視できる。任意の有限値の列は有限離散空間への写像として一意に
延長され、コンパクト性により連続な離散値関数は有限値である。
第2の台 \(\omega^K\) には \(K\) 上のすべての関数を入れる。

\(T\in C_{\mathrm{cont}}\) を確認する。任意の空でない Stone 空間 \(J\)
について \(H(C(J,\omega))\cong J\) が点評価で成り立つ。同変な汎関数は、
任意の正の有限項数の演算を保存する。実際、連続関数の有限組を
\(\omega^k\cong\omega\) で一つの連続関数に符号化すると、座標の復号も
任意の \(k\) 項演算の適用も \(M\) の単項写像で実現できる。
従って clopen 集合の指示関数上で超フィルターを定める。コンパクト性と
clopen 分離によりその超フィルターは一つの点を定め、各関数の有限な
ファイバー分割から元の汎関数はその点での評価となる。評価写像は
コンパクト空間から Hausdorff 空間への連続全単射なので同相である。

第2の台では濃度を確認する。同変な \(\ell:\omega^I\to\omega\) は
指示関数上で超フィルターを定め、各 \(f:I\to\omega\) の
\(\ell(f)\)-ファイバーを選ぶ。これは可算分割ごとに一つのセルを選ぶ
ことを意味し、最初に外れる条件で分割することから可算完備性が従う。
\(\beth_0=\aleph_0,\ \beth_{n+1}=2^{\beth_n}\) とすると、有限な \(n\)
について \(|I|\le\beth_n\) 上の可算完備超フィルターはすべて主である。
実際、可算集合では明らかであり、\(\beth_n\) までの主性を仮定すると、
押し出しによって \(\beth_n\) 個以下のセルを持つ任意の分割で一つの
セルが選ばれる。従って \(\beth_n\) 個以下の大きな集合の共通部分も
大きい。\(\beth_{n+1}\) 個以下の点なら \(\beth_n\) 個以下の二値座標
で分離でき、それぞれ選ばれた側の共通部分が一点になる。

\(|K|\le\beth_2\) より \(H(\omega^K)\) も正確に \(K\) の点評価である。
よって \(H(p_T)\) は点の上で恒等写像、\(d_T\) は連続な \(s\) である。
第1の台の各元はその有限像を支持に持つ。これで \(T\in C_{\mathrm{cont}}\)
が示された。\(X\to E(T)\) の初期写像 \(j\) には \(0\in K\) の評価を取る。

## 3. 任意の初期指標を通す射

\(Y\in C\) と \(h\in S_Y\) を取り、\(h_n=d_Y^n(h)\) と書く。
\(n\mapsto h_n\) は一意な連続写像 \(t_h:K\to S_Y\) に延長される。
具体的には \(t_h(U)(y)=\lim_U h_n(y)\) であり、各 \(y\) で値は共通の
有限支持に入る。ここで使う位相的普遍性は
[Stacks Project, §5.25](https://stacks.math.columbia.edu/tag/0908) にある。

\(d_Y\) が連続なら、次の二つの連続写像は自然数上で一致し、
稠密性と Hausdorff 性から \(K\) の全点で一致する。
\[
 d_Y t_h=t_h s.                                                     \tag{1}
\]
そこで \(Y\to T\) の二成分を
\[
 k_0(y)(U)=t_h(U)(y),\qquad
 k_1(z)(U)=\widetilde{t_h(U)}(z)
\]
と定める。\(k_0(y)\) は連続な座標評価との合成であり、\(k_1(z)\)
は \(K\) 上の関数でよい。特に \((H(p_Y))^{-1}\) の連続性を要さない。
両成分は各 \(U\) で指標を用いるため \(M\)-同変である。また
\[
 \begin{aligned}
 k_1(p_Y y)(U)&=t_h(U)(y)=k_0(y)(U),\\
 k_1(q_Y y)(U)&=d_Y(t_h(U))(y)=k_0(y)(sU).
 \end{aligned}
\]
これが二本の構造射の可換性である。\(k_0(y)(0)=h(y)\) なので、
双対を取れば所要の因子化 \(X\xrightarrow j E(T)\xrightarrow{E(k)}E(Y)\)
が得られる。

任意の初期指標を保つ \(k:Y\to T\) からは、同じ逆向きの計算で
\(U\mapsto(y\mapsto k_0(y)(U))\) が (1) を満たす連続写像になる。
自然数上で \(h_n\) に等しいため、これは \(t_h\) に等しい。\(k_1\)
も指標の一意延長によって決まる。さらに、\(\mathcal P\) の任意の射
\(E(T)\to E(Y)\) はこの向きの双対射に由来する。各出力座標で
\(\omega^{T_i}\to\omega\) を取り、\(|T_i|\le\beth_3\) と §2 を使えば、
それは一つの \(T_i\) の点での評価である。得られた点写像の同変性と
二つの構造等式は、\(T_i\) 上の全関数で検査できる。特に生成対象
\(E(Y)\), \(Y\in C_{\mathrm{cont}}\), への因子化はこの段階で一意である。

## 4. 小極限と有向合併で閉じた後の反射

次の一般的な議論を用いる。前層圏で \(\mathcal B\) が生成族 \(\mathcal G\)
を小極限と有向合併で閉じた最小の充満・同型閉部分圏であるとする。
有限生成な \(X\) からの射 \(X\to W\), \(W\in\mathcal B\), があり、
任意の \(G\in\mathcal G\) への任意の \(X\to G\) がこれを通ると仮定する。

1. \(W\) 内で初期写像の像を含み、台が \(\mathcal B\) に属するすべての
   部分前層を交わらせ、その交わりを \(H\) とする。部分前層は集合個で、
   \(W\) 自身が候補である。交わりは \(\mathcal B\) 内の小極限なので
   \(H\in\mathcal B\)。誘導射を \(\eta:X\to H\) と書く。
2. 任意の \(Z\in\mathcal B\) について、\(\eta\) 上で一致する二射
   \(H\rightrightarrows Z\) の等化子は、\(W\) 内の上記の候補になる。
   \(H\) の最小性から等化子は \(H\) 全体であり、延長は高々一つである。
3. \(\mathcal B\) の中で、すべての \(X\to Z\) が \(\eta\) に沿って
   延長できる対象を取る。これは \(W\) からの射を \(H\) に制限する
   ことで \(\mathcal G\) を含む。小極限では、各射影先への延長が
   手順 2 の一意性で両立する。有向合併では \(X\) の有限生成性により
   初期写像が一段階を通る。その段階で延長して合併への単射と合成する。
   この部分クラスは両演算に閉じるので \(\mathcal B\) 全体である。

ここで \(\mathcal B=\mathcal A_{\mathrm{cont}},\ W=E(T)\) とする。
§3 がすべての生成対象について仮定を満たすので、
\[
 H_{\mathrm{cont}}=
 \bigcap_{\substack{V\subseteq E(T),\ V\in\mathcal A_{\mathrm{cont}}\\
                    \operatorname{im}j\subseteq V}} V,\qquad
 \mathcal P(H_{\mathrm{cont}},Z)\ \xrightarrow[\ \circ\eta\ ]{\ \cong\ }\
 \mathcal P(X,Z)
 \quad(Z\in\mathcal A_{\mathrm{cont}}).
\]
全台の濃度は \(\beth_4\) 以下である。有向合併を通す箇所で有限生成性を
用いたのは \(X\) である。

## 5. 過去の二例と連続性の正確な境界

二周期では \(t_h(U)\) は偶数集合と奇数集合のどちらが \(U\) に
属するかで二点の一方を選ぶ。[二極限の標的](identity_trace_has_no_scalar_extension_and_two_limit_target.md)
では、自然数 \(n\) の像は \(n\)、自由超フィルターの像はその選ぶ
偶奇に応じて \(\infty_0\) または \(\infty_1\) である。従って前稿の
観測 \(r(n)=n,\ r(\infty_0)=0,\ r(\infty_1)=1\) に対する \(k_1(r)\)
は、自然数上で恒等列を保ち、自由超フィルター上で 0 と 1 を
区別する。これが第2の台として \(\omega^K\) を使った効果である。

一般の \(Y\in C\) と初期指標 \(h\) についても、以下は同値である。

* \(H_{\mathrm{cont}}\to E(Y)\) で \(\eta\) を \(h\) に送る射がある。
* 式 (1) が成立する。
* 軌道閉包 \(L_h=\overline{\{d_Y^n h:n<\omega\}}\) が前向き不変で、
  \(d_Y|_{L_h}\) が連続である。

後二条件の同値は \(t_h:K\to L_h\) がコンパクト空間から Hausdorff 空間
への商写像であることと、自然数上での (1) による。(1) から第1条件は
§3 の構成を \(H_{\mathrm{cont}}\) に制限して従う。

逆向きには [初期写像に付随する軌道列演算の補題、§§2–3](identity_trace_has_no_scalar_extension_and_two_limit_target.md)
を用いる。この補題から実は \((H_{\mathrm{cont}})_0=E(T)_0\) と分かる。
\(g\in C(K,\omega)\) の軌道列は \((g(n))_{n<\omega}\) であり、稠密性により
\(g\) を決定する。従って \(C(K,\omega)\) 上の任意の自然数値関数は、
この軌道列にある \(\Phi:\omega^\omega\to\omega\) を適用して得られる。
補題を \(H_{\mathrm{cont}}\) の初期写像に適用し、包含射による自然性を使えばよい。

各 \(U\in K\) に対し、有限値の軌道列の \(U\)-極限を取る
第0ソートの元 \(a_U\) が初期写像から自然に定まる。補題は全体の
\(\mathcal A\) で成立し、\(\mathcal A_{\mathrm{cont}}\subseteq\mathcal A\)
である。\(H_{\mathrm{cont}}\hookrightarrow E(T)\) の中で \(a_U\) は
\(U\) の点評価である。従って balanced で、初期写像の第1ソートの
定数と併せて新しい \(X\)-射をなす。
[両端が有限生成な指標延長テスト](general_equalizers_finite_orthogonality_and_quotient_reduction_2026-11-17.md)
\(E(\sigma)\) への直交性により、この元は \(H_{\mathrm{cont}}\) 内に
一意な balanced 延長 \(b_U\) を持つ。\(E(T)\) 内でこれは第1ソート
の \(U\) の評価であり、\(q^* b_U=a_{sU}\) が成立する。所与の
\(H_{\mathrm{cont}}\to E(Y)\) は \(a_U\) を \(t_h(U)\) に、\(b_U\)
をその一意延長に送る。この等式の像が (1) である。

例えば \(Y_{\omega+1}\) の 0 の評価では自由 \(U\) について
\(t_h(U)=t_h(sU)=\omega\) だが \(d_Y(\omega)=\omega+1\) である。
従ってこの初期写像は \(H_{\mathrm{cont}}\) を通らず、
\(E(Y_{\omega+1})\notin\mathcal A_{\mathrm{cont}}\) である。
この不連続な例まで含めた肯定結果は
[不連続点および順序数軌道への拡張](continuous_reflection_extension_to_discontinuous_orbits.md)
に示す。
