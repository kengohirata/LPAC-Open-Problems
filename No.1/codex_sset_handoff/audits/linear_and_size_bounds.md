# 線形テストと固定次数のサイズ障害の監査

監査日：2026-11-15
対象：[`sset_higher_dimensional_followup.md`](../prior_notes/sset_higher_dimensional_followup.md)、主に §§1–7。
状態：`INTERNAL_PROOF_CHECKED`（独立の手計算による内部監査）。形式検証・外部査読は行っていない。標準的な背景結果の出典確認と、このノート固有の証明の確認を区別する。

主要な線形判定式、可算部分対象の構成、coreflector の濃度上界、固定次数のサイズ障害について、記載された仮定の下で数学的な破綻は見つからなかった。本稿では省略されていた理由を補い、量化と適用範囲を明示する。元ノートは変更していない。本担当の証明監査はコードの実行結果に依存しない。root 担当は別途、既存の GF(2) 検算を seed 48291 で再実行し、300件の成功を確認した。

## 1. 仮定と記法

ZFC で議論する。母圏は通常の simplicial sets の圏 `sSet`。体 $k$ 上の simplicial vector spaces の射の集合

\[
f_i:U_i\longrightarrow V_i\qquad(i\in I)
\]

を構造を忘れて `sSet` のテスト射とする。充満部分圏

\[
\mathcal A=\{X\mid\operatorname{sSet}(X,f_i)
\text{ がすべての }i\text{ について全単射}\}
\]

を考える。Hom は通常の射集合であり、鎖ホモトピー類や導来写像空間ではない。

$C_*(X;k)$ は非退化 simplex を基底とする正規化鎖複体、$N(U)$ は simplicial vector space の正規化複体とする。すべての複体は非負次数にあり、$d_0:C_0\to0$。

\[
Z_nC=\ker d_n,\qquad B_nC=\operatorname{im}d_{n+1},\qquad
H_nC=Z_nC/B_nC.
\]

以下で可算とは有限を含む。simplicial set の全体のサイズは

\[
|X|=\left|\coprod_{n\ge0}X_n\right|
\]

と定める。

## 2. 線形判定式

元ノート §§1–3（22–114行）に対応する。

自由 simplicial vector space と忘却関手の随伴、および Dold–Kan 同値から、自然な全単射

\[
\operatorname{sSet}(X,\operatorname{und}U)
\cong\operatorname{sVect}_k(k[X],U)
\cong\operatorname{Ch}_{\ge0}(k)(C_*(X;k),N(U))
\]

を得る。Dold–Kan は通常の圏の同値なので、ここでは Hom 集合そのものを比較している。[S1, S2]

任意の非負次数 $k$-複体 $C$ について、体上の短完全列を分裂させると、複体として

\[
C\cong
\bigoplus_{n\ge0}S^n(H_nC)
\oplus\bigoplus_{n\ge1}D^n(B_{n-1}C)
\]

と書ける。ここで $S^n(W)$ は次数 $n$ のみに $W$ を置く複体、$D^n(W)$ は次数 $n,n-1$ に $W$ を置き、その間の境界を恒等写像とする複体である。$n=0$ では $B_{-1}C=0$ とする。

この分裂を始域 $C$ について固定すると、標的 $E$ について自然な全単射

\[
\operatorname{Ch}(C,E)\cong
\prod_{n\ge0}\operatorname{Hom}_k(H_nC,Z_nE)
\times\prod_{n\ge1}\operatorname{Hom}_k(B_{n-1}C,E_n)
\tag{1}
\]

が得られる。sphere からの鎖写像は cycle を選ぶことに等しく、disk からの鎖写像は上側の次数 $n$ の像を選べば決まる。分裂が標準的である必要はなく、固定した分裂に対する標的方向の自然性で足りる。

非零 vector space $W$ に対し、$\operatorname{Hom}_k(W,g)$ が全単射であることは $g$ が同型であることと同値である。基底を選べばこの写像は $g$ の非空個のコピーの積になる。すべての Hom 集合には零写像があるため、積の全単射性から各因子の全単射性を取り出せる。$W=0$ の因子は一元集合であり条件を課さない。

$\phi_i=N(f_i)$ と置き、

\[
J=\{n\ge0\mid\exists i:\ Z_n\phi_i\text{ が同型でない}\},\qquad
K=\{n\ge1\mid\exists i:\ (\phi_i)_n\text{ が同型でない}\}
\]

と定める。(1) より

\[
X\in\mathcal A\iff
\begin{cases}
H_n(X;k)=0 &(n\in J),\\
d_n:C_n(X;k)\to C_{n-1}(X;k)\text{ が零} &(n\in K).
\end{cases}
\tag{2}
\]

第二条件には $B_{n-1}C=0\iff d_n=0$ を使った。これは元ノートの命題3.1の証明を補足したものである。

**確認した境界・失敗例。** 空のテスト族または恒等射では $J=K=\varnothing$ となる。$0\in J$ なら、非空な $X$ は $H_0(X;k)\ne0$ なのでクラスは $\{\varnothing\}$。また acyclic な disk の射 $D^n(k)\to0$ は homology 上同型だが、$C=D^n(k)$ に対する Hom 写像は $k\to\{0\}$ で全単射ではない。したがって $Z_n\phi$ を $H_n\phi$ に置き換えることはできない。これらは手計算による確認であり、計算探索ではない。

**判定：** 共通の体 $k$ と strict Hom という仮定の下で成立。体上の分裂を使うため、この証明をそのまま一般のアーベル群や任意の環上の加群に適用することはできない。

## 3. 可算部分対象と局所可呈示性

元ノート §4（118–165行）に対応する。

**主張。** $X\in\mathcal A$ と、全 simplices の可算部分集合 $Z$ に対して、$Z\subseteq Y\subseteq X$、$Y\in\mathcal A$、$|Y|\le\aleph_0$ を満たす subsimplicial set が存在する。

**証明。** $k_0\subseteq k$ を素体とする。$k_0$ は可算であり、

\[
C_*(X;k)\cong C_*(X;k_0)\otimes_{k_0}k.
\]

体拡大は忠実かつ完全なので、固定した $J,K$ に対する (2) の条件は $X$ の係数を $k_0$ に変えても同値である。ここでテスト射 $f_i$ 自体が素体上定義されるとは主張していない。

$Z$ を face と degeneracy で閉じて $Y^{(0)}$ を作る。simplex category の射は可算個なので、この閉包は可算。可算な $Y^{(r)}$ ができたら、すべての $n\in J$ と $C_n(Y^{(r)};k_0)$ のすべての cycle $z$ に対し、$X$ 内の有限支持の鎖 $b_z$ で $d b_z=z$ となるものを選ぶ。存在は $H_n(X;k_0)=0$ による。それらの台を加え、再び simplicial operators で閉じて $Y^{(r+1)}$ を得る。扱う cycle 全体が可算なので可算性が保たれる。

$Y=\bigcup_{r<\omega}Y^{(r)}$ とする。$Y$ の cycle は有限支持であるためある段階に現れ、次の段階で boundary になる。よって $n\in J$ に対し $H_n(Y;k_0)=0$。

また、subsimplicial inclusion は非退化性を保存する。実際、$y\in Y$ が $X$ 内で $y=s_i x$ と退化していれば、$x=d_i y\in Y$ なので $Y$ 内でも退化している。したがって

\[
C_*(Y;k_0)\longrightarrow C_*(X;k_0)
\]

は次数ごとに単射である。$n\in K$ の境界が零という条件も $Y$ に引き継がれ、(2) より $Y\in\mathcal A$。∎

任意の coorthogonality class は小余極限に閉じる。実際、

\[
\operatorname{sSet}(\operatorname{colim}_a X_a,f_i)
\cong\lim_a\operatorname{sSet}(X_a,f_i)
\]

であり、全単射の極限は全単射である。従って $\mathcal A$ の余極限は `sSet` 内で計算される。

上の構成より、各 $X\in\mathcal A$ は可算な $\mathcal A$-部分対象の $\aleph_1$-directed union である。可算個のそのような部分対象の合併を再び上の構成で拡張すれば、共通の上界が得られる。各 simplex を含む部分対象も得られるので合併は $X$。

可算な simplicial set は `sSet` で $\aleph_1$-presentable である。射を指定する可算個の値と可換性の等式は、$\aleph_1$-filtered colimit の一段階で実現でき、二射の等しさも可算個の等式で確認できる。包含がこれらの余極限を保存するため、可算な $\mathcal A$-対象は $\mathcal A$ 内でも $\aleph_1$-presentable。可算 sSet の同型類は集合個なので、$\mathcal A$ は locally $\aleph_1$-presentable である。

**判定：** 可算閉包の議論は成立する。非退化性の保存と、素体に移すのは $X$ 側の条件であることを明記した。

## 4. Coreflector の構成と濃度上界

元ノート §5（169–191行）に対応する。

$B\in\mathrm{sSet}$ を固定する。可算な $\mathcal A$-対象の skeleton から $B$ への任意の射 $c:C\to B$ を対象とし、$B$ 上の可換三角形を射とする小圏を $J_B$ とする。

可算図式の余極限は可算であり、$\mathcal A$ に属し、$B$ への誘導射を持つ。その代表を skeleton から取れば $J_B$ 内の cocone が得られる。空図式についても $\varnothing\to B$ がある。従って $J_B$ は $\aleph_1$-filtered。

\[
R(B)=\operatorname{colim}_{(C\xrightarrow{c}B)\in J_B}C
\]

とし、標準射を $r_B:R(B)\to B$、各構成射を $\iota_c:C\to R(B)$ と書く。余極限閉性から $R(B)\in\mathcal A$。

$a:X\to B$、$X\in\mathcal A$ を取る。$X$ の可算な $\mathcal A$-部分対象 $C$ ごとの標準射 $\iota_{a|_C}$ は包含に関して整合し、$u:X\to R(B)$ に貼り合わさる。これにより $r_Bu=a$ を得る。skeleton の代表への置換は同型を通して行い、異なる置換は colimit の関係式により同じ標準射を与える。

一意性には filteredness を使う。可算 $C\in\mathcal A$ と任意の $h:C\to R(B)$ は、presentability により

\[
h=\iota_d t,
\qquad t:C\to D,
\qquad d:D\to B
\]

と因子分解する。$c=r_Bh$ と置けば $dt=c$ なので $t:(C,c)\to(D,d)$ は $J_B$ の射。従って $h=\iota_dt=\iota_c$。一般の $X$ でも可算な $\mathcal A$-部分対象への制限で一意性が従う。よって $r_B$ は coreflection。

可算な simplicial sets の同型類は高々 $2^{\aleph_0}$ 個である。各可算 $C$ から $B$ への射は高々 $(|B|+2)^{\aleph_0}$ 個。従って $J_B$ の対象数もこの基数以下であり、各対象は可算なので、その余積と商として得られる余極限について

\[
|R(B)|\le (|B|+2)^{\aleph_0}
\tag{3}
\]

を得る。上界にテスト射のサイズは現れない。

**判定：** 存在・一意性と (3) は成立する。ここで $J_B$ が filtered である理由は、可算な $\mathcal A$-対象が可算余極限に閉じることにある。

## 5. 固定次数の因子分解サイズ定理

元ノート §7、定理7.1・系7.2（241–292行）に対応する。この節では線形構造を仮定しない。

**仮定。** $\mathcal A\subseteq\mathrm{sSet}$ は充満・同型閉で、空図式を含むすべての小余極限に閉じる。$B\in\mathrm{sSet}$ を固定する。

**定理。** 次は同値である。

1. $B$ の $\mathcal A$-coreflection が存在する。
2. 次の量化を満たす。

\[
\begin{aligned}
\forall n\in\mathbb N\ \exists\text{基数 }\kappa_n\ 
\forall(X\in\mathcal A)\ \forall(a:X\to B)\ 
\exists(Y\in\mathcal A)\ \exists(u:X\to Y)\ \exists(v:Y\to B):\\
vu=a\quad\text{かつ}\quad |Y_n|\le\kappa_n.
\end{aligned}
\tag{4}
\]

$Y,u,v$ は $n,X,a$ に依存してよい。同じ $Y$ がすべての次数の上界を同時に満たすとは仮定しない。

**証明。** 1 から 2 は coreflection の始域を $Y$ とすればよい。逆向きでは

\[
\kappa=\max(\aleph_0,\sup_{n<\omega}\kappa_n)
\]

と置く。任意の $a_0:X^{(0)}\to B$、$X^{(0)}\in\mathcal A$ から出発し、段階 $n$ で (4) を次数 $n$ と射 $a_n:X^{(n)}\to B$ に適用する。これにより $B$ 上の列

\[
X^{(0)}\longrightarrow X^{(1)}\longrightarrow X^{(2)}\longrightarrow\cdots
\]

で、各 $X^{(n)}\in\mathcal A$、$|(X^{(n+1)})_n|\le\kappa$ を得る。

$Y=\operatorname{colim}_{n<\omega}X^{(n)}\in\mathcal A$ とする。各固定 $m$ と $n\ge m$ について、退化写像の合成が split mono

\[
(X^{(n+1)})_m\hookrightarrow (X^{(n+1)})_n
\]

を与える。従って $m$ 次成分の列の十分後ろはすべて濃度 $\kappa$ 以下である。余極限は次数ごとに計算され、列の末尾は cofinal なので $|Y_m|\le\aleph_0\kappa=\kappa$。さらに次数は可算個なので $|Y|\le\kappa$。$a_0$ は $Y\to B$ を経由する。

サイズ $\kappa$ 以下の simplicial sets の同型類、およびそれらから $B$ への射は集合個である。その中で $\mathcal A$ に属するものの代表を集めると、$\mathcal A\downarrow B$ の weakly terminal set になる。ここまでは $\kappa$ の正則性や $\kappa^{\aleph_0}=\kappa$ を仮定していない。

最後に、weakly terminal set から終対象を作る。以下の全操作は $\mathcal C=\mathcal A\downarrow B$ 内で行う。$\mathcal C$ は余完備かつ局所小である。weakly terminal set の余積 $W$ は weakly terminal object。局所小性により $\operatorname{End}_{\mathcal C}(W)$ は集合なので、すべての自己射 $\sigma$ を恒等射と同時に coequalize した

\[
q:W\longrightarrow Q,
\qquad q\sigma=q\quad(\sigma\in\operatorname{End}_{\mathcal C}(W))
\]

が存在する。

任意の二射 $u,v:X\rightrightarrows Q$ に対し、その coequalizer を $c:Q\to T$ とする。$W$ の弱終性から $h:T\to W$ がある。$\sigma=hcq$ は $W$ の自己射なので $qhcq=q$。$q$ は epi であり、

\[
qhc=1_Q
\]

を得る。従って $c$ は split mono であると同時に coequalizer、従って epi であり、同型になる。ゆえに $u=v$。任意の $X$ から $Q$ への射の存在は $X\to W\xrightarrow qQ$ による。従って $Q$ は終対象であり、対応する $Q\to B$ が coreflection となる。∎

**否定形。** coreflection が存在しなければ、

\[
\exists n\in\mathbb N\ \forall\text{基数 }\kappa\ 
\exists(X\in\mathcal A)\ \exists(a:X\to B)\ 
\forall(Y\in\mathcal A,u:X\to Y,v:Y\to B):
\quad vu=a\Rightarrow |Y_n|>\kappa.
\tag{5}
\]

つまり固定した一つの次数が、任意の基数に対する障害を担う。次数 $n$ 自体は $B,\mathcal A$ に依存してよいが、$\kappa$ には依存しない。

**判定：** 対角構成と weakly-terminal-to-terminal の証明は成立する。(5) は全 simplicial sets の $\mathcal A$-対象に量化しており、有限探索範囲の障害でも、有限切断圏への反例移送定理でもない。

## 6. 障害次数をさらに限定する

元ノートの系7.3（294–302行）を、証明を補って記す。

**仮定。** $\mathcal A={}^\perp\{f}$、$f:U\to V$ は通常の simplicial map。ある次数 $n$ の成分 $f_n:U_n\to V_n$ が全単射とする。

Yoneda の全単射 $\operatorname{sSet}(\Delta[n],f)\cong f_n$ により $\Delta[n]\in\mathcal A$。任意の $a:X\to B$、$X\in\mathcal A$ に対し、集合

\[
P=\{(x,x')\in X_n\times X_n\mid a_n(x)=a_n(x')\}
\]

を取る。各対に対応する二射 $\Delta[n]\rightrightarrows X$ をまとめた

\[
\coprod_{(x,x')\in P}\Delta[n]\rightrightarrows X
\xrightarrow qY
\]

の coequalizer を作る。余積の始域と $X$ は $\mathcal A$ に属するので、余極限閉性から $Y\in\mathcal A$。$a$ は二射を等化するため $a=vq$ と因子分解する。

$q_n$ は全射であり、$a_n$ が同一視する全対を同一視する。一方、$a_n=v_nq_n$ なので異なる $a_n$-像を持つ元は同一視しない。従って

\[
Y_n\cong X_n/\ker(a_n)\cong\operatorname{im}(a_n),
\qquad |Y_n|\le |B_n|.
\tag{6}
\]

よって (5) の障害次数は $f_n$ が全単射でない次数でなければならない。特に $f_0$ が全単射なら頂点次数は排除され、$n\ge1$ とできる。

テスト族 $S=\{f_i\}$ の場合も、当該次数のすべての $(f_i)_n$ が全単射なら同じ証明が使える。必要なのは $\Delta[n]\in{}^\perp S$ である。

**判定：** 成立。任意の商への閉性は使っていない。使用した商は、始域・終域の両方が $\mathcal A$ に属する特定の二射の coequalizer である。

## 7. 元ノートの例と記録に関する補足

元ノート §6 の $\bigoplus_{m\ge1}D^{2m+1}(\mathbb Q)\to\bigoplus_{m\ge1}S^{2m+1}(\mathbb Q)$ について、cycle 写像を次数ごとに計算すると、記載された $J=\{2,3,\ldots\}$、$K=\{2,4,\ldots\}$ を得る。始域は acyclic、終域は任意に高い奇数次数に非零 homology を持つ。対応する underlying simplicial sets の section があれば、これらの homotopy groups 上にも section が生じるため矛盾する。[S3, S4]

この例の判定条件は上の線形定理に含まれ、非分裂性・無限次元性があっても coreflective である。これは一般の `sSet` の問題の解決を意味しない。

元ノート330行にある検算スクリプトの記載先 `sset_followup_checks/check_linear_formula.py` と、同梱先 [`existing_checks/check_linear_formula.py`](../existing_checks/check_linear_formula.py) は異なる。今回の監査はスクリプト実行結果に依存していない。

今後の検討候補として、固定次数の議論を一般の小さい presheaf 圏の「固定 sort」の障害に拡張すること、異なる体上の線形テストの混合を素体ごとに整理することがある。本稿ではこれらを追加定理として採用せず、上で証明した範囲と区別する。

## 標準的背景の出典

以下のウェブ本文を2026-11-15に確認した。これらは線形化・正規化・homotopy 計算の背景を支持する。今回の coorthogonality の定理や固定次数定理そのものの既存出典としては引用していない。

- **[S1]** The Stacks Project, [Theorem 14.24.3, Tag 019G](https://stacks.math.columbia.edu/tag/019G)。アーベル圏の simplicial objects と非負次数鎖複体の通常の圏としての同値。
- **[S2]** Kerodon, [Construction 2.5.5.9, Tag 00QH](https://kerodon.net/tag/00QH)。simplicial set の正規化鎖複体を非退化 simplex と交代 face 境界で記述する。
- **[S3]** Kerodon, [Construction 2.5.6.3, Tag 00QT](https://kerodon.net/tag/00QT)。正規化標準 simplex からの鎖写像による Eilenberg–Mac Lane 関手。
- **[S4]** Kerodon, [Exercise 3.2.2.22, Tag 00W2](https://kerodon.net/tag/00W2)。正次数における Eilenberg–Mac Lane 空間の homotopy groups と鎖複体の homology の対応。

**残る限界。** 一般の $P_{\mathrm{sSet}}$ の ZFC 証明、反例、独立性モデルは本監査では得ていない。主張の状態は内部の証明確認であり、形式検証・外部査読・文献上の新規性確認を済ませたものではない。
