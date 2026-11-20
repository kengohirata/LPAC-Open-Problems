# Small coorthogonality の定義可能性と肯定側の十分条件

2026-11-15。通常の集合論 ZFC を基礎とする。ここでの証明は今回の内部監査で複数の担当が独立に点検したもの。形式検証・外部査読は未実施で、文献上の新規性や最小の集合論的強度は主張しない。

2026年11月16日の続報：[修復列と WVP](../investigations/tower_bound_and_weak_vopenka_2026-11-16.md) に、WVP⇒P の別の十分条件を記録した。以下の supercompact 仮定による証明は維持する。いずれの十分条件についても、P に必要であるとは主張しない。

## 1. 問題の確認

局所可呈示圏 \(\mathcal K\) と射の**集合** \(S=\{f_i:U_i\to V_i\mid i\in I\}\) に対して
\[
\mathcal A_S=\{X\in\mathcal K:\mathcal K(X,f_i)\text{ がすべての }i\in I\text{ について全単射}\}
\]
と置く。射集合は ordinary Hom であり、ホモトピー類ではない。全局所可呈示圏と全テスト集合について \(\mathcal A_S\) が coreflective になる主張を \(P\) と書く。

Adámek–Rosický の原著295頁、Problem 1 は次の問いである。

> Is each small-orthogonality class in the dual of a locally presentable category reflective?

これは上の \(P\) と一致する。同頁のコメントは、Vopěnka's principle の下では肯定的であることを、余極限閉性と Theorem 6.28 から説明している。原著の[章ページ](https://www.cambridge.org/core/books/abs/locally-presentable-and-accessible-categories/open-problems/2C96E4B704E77DA99C42BEDAB6482CCD)および[295頁の出版社画像](https://static.cambridge.org/content/id/urn:cambridge.org:id:book:9780511600579/resource/name/firstPage-9780511600579mem_p295-298_CBO.jpg)を確認した。

同頁 Problem 2 は small を外した別の問題である。テスト射が真のクラスである場合の否定的結果を、Problem 1 の反例として使用してはいけない。

## 2. Presheaf 圏での定義可能性

**命題。** 小圏 \(C\) を固定し、\(\mathcal K=\mathbf{Set}^{C^{op}}\) とする。射の集合 \(S\) を固定すると、\(\mathcal A_S\) の対象クラスは、\(C,S\) を集合パラメータとして \(\Sigma_2\) および \(\Pi_2\) の両方で定義できる。

**コードの約束。** Presheaf は、小さい対象集合で添字付けた carrier の族と、小さい射集合で添字付けた unary operation の族としてコードする。対象の妥当性、候補 \(g\) が自然変換 \(X\to U_i\) であるという述語 \(\operatorname{Map}(X,U_i,g)\)、および合成の一致は、与えられた carrier・operation・関数グラフ上の有界量化で表せる。したがってこれらは \(\Delta_0\) である。順序対や族の成分を取り出すための有限回の集合操作も、有界なグラフ検査として展開できる。任意の infinitary structure について同じことを無条件に主張しているわけではない。

**\(\Sigma_2\) 表現。** \(L\) を添字付き候補射 \((i,g)\) の集合とする。次を要求する。

1. \((i,g)\in L\) なら \(i\in I\) かつ \(g:X\to U_i\) は自然変換。
2. 任意の集合コード \(h\) と任意の \(i\in I\) について、\(h:X\to V_i\) が自然変換なら、\(f_i g=h\) となる \((i,g)\in L\) がある。
3. 任意の集合コード \(g,g'\) と任意の \(i\in I\) について、\(g,g':X\to U_i\) が自然変換で \(f_i g=f_i g'\) なら \(g=g'\)。

2 の持ち上げへの量化は \(L\) によって有界である。1 の検査も有界であるため、全体は
\[
\exists L\;\forall h\;\forall g\;\forall g'\;
\Theta(X,C,S,L,h,g,g')
\]
という形になる。\(\Theta\) は有界式で、\(X\) の対象としての妥当性も含む。

この式が成り立てば定義から \(X\in\mathcal A_S\)。逆に \(X\in\mathcal A_S\) なら、集合
\[
L=\coprod_{i\in I}\mathcal K(X,U_i)
\]
を採用すれば全条件を満たす。ここで \(L\) の存在を証明するのに集合としての Hom を使うことと、定義式の中でその集合をあらかじめパラメータとして与えることは異なる。

**\(\Pi_2\) 表現。** 各候補射 \(h:X\to V_i\) に対して持ち上げ \(g:X\to U_i\) が存在する、という直接の \(\forall h\exists g\) 表現に、普遍的な一意性条件を加える。\(i\in I\) は有界量化なので \(\Pi_2\) となる。∎

集合 \(S\) を固定することが本質的である。真のクラス全体のテスト射に同じ集合 \(L\) を使えるとは主張しない。

## 3. 文献定理からの帰結

Bagaria–Casacuberta–Mathias–Rosický, *Definable orthogonality classes in accessible categories are small*, [arXiv:1101.2792v4](https://arxiv.org/html/1101.2792v4), Definition 7.7(2) と Theorem 8.8 を確認した。両者を合わせると、supercompact cardinal が真のクラス存在する場合、局所可呈示な構造の圏の、\(\Sigma_2\) 定義可能で小余極限に閉じた充満部分圏は coreflective である。

Presheaf 圏は多ソート unary equational structures の圏としてこの定理の対象となる。また \(\mathcal A_S\) は小余極限に閉じる。実際、\(\mathcal K(-,U_i)\) と \(\mathcal K(-,V_i)\) は余極限を集合の極限に移し、全単射からなる自然変換の極限は全単射である。空図式も含む。

従って §2 を適用して、次を得る。

**系。** Supercompact cardinal が真のクラス存在すれば、すべての小圏 \(C\) に対して \(P_{\mathbf{Set}^{C^{op}}}\) が成り立つ。

これは既存定理と上の定義可能性計算の帰結である。Theorem 8.8 自体を無条件の ZFC 定理として用いてはいけない。

## 4. 一般の局所可呈示圏への移送

**補題。** \(L:\mathcal K\rightleftarrows\mathcal D:J\) を \(L\dashv J\)、\(J\) 充満忠実とする。\(\mathcal D\) 内のテスト集合 \(S\) に対し
\[
\mathcal A={}^\perp_{\mathcal D}S,\qquad
\mathcal C={}^\perp_{\mathcal K}(JS)=L^{-1}(\mathcal A)
\]
と置く。任意の \(B\in\mathcal D\) について、\(B\) に \(\mathcal A\)-coreflection が存在することと、\(JB\) に \(\mathcal C\)-coreflection が存在することは同値である。

**証明。** \(a:A_0\to B\) が coreflection なら、\(X\in\mathcal C\) に対して
\[
\mathcal K(X,JA_0)\cong\mathcal D(LX,A_0)
\cong\mathcal D(LX,B)\cong\mathcal K(X,JB)
\]
なので \(Ja\) が coreflection になる。

逆に \(c:C_0\to JB\) を coreflection とする。随伴による transpose を \(d:LC_0\to B\)、unit を \(\eta:C_0\to JLC_0\) とすれば \(c=Jd\,\eta\)。\(LC_0\in\mathcal A\) なので \(JLC_0\in\mathcal C\)。よって一意な \(t:JLC_0\to C_0\) があり \(ct=Jd\)。coreflection の一意性から \(t\eta=1\)。さらに \(JLC_0\) は反射部分圏の対象なので、\(\eta\) による前合成は
\(\mathcal K(JLC_0,JLC_0)\to\mathcal K(C_0,JLC_0)\)
上で全単射である。\(\eta t\eta=\eta\) から \(\eta t=1\)。従って \(C_0\cong JLC_0\) であり、\(d\) が所望の coreflection になる。∎

任意の局所可呈示圏は presheaf 圏の充満反射部分圏として表せる。Adámek–Rosický Theorem 1.46 のこの内容は [Raptis, *Notes on combinatorial model categories*, Theorem 2.5, p.5](https://www.graptismath.net/files/notes-comb-model-cat.pdf) でも確認した。§3 と補題をこの表示に適用する。

**結論。** Supercompact cardinal が真のクラス存在すれば、\(P\) は成り立つ。

この移送は **すべての** presheaf 圏での肯定を使う。\(\mathrm{sSet}\) 一つで肯定できれば全局所可呈示圏で肯定できる、という主張ではない。

## 5. 到達点と未解決部分

- 原著の問題と VP による肯定の向きを確認した。
- 肯定側の十分条件として、上記の supercompact cardinal 仮定を得た。
- この十分条件の必要性、最適性、文献上の新規性は確認していない。
- ZFC 単独での \(P\) の証明、\(\neg P\) のモデル、ZFC 独立性は、いずれも得ていない。
- 有限計算でこの集合論的結論を検証したとは主張しない。反射移送の unit の両側逆、空テスト族、真のクラスのテスト族との区別を証明上の境界条件として点検した。
