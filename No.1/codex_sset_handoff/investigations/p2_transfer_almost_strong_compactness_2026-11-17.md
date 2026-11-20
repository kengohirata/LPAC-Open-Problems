# P2 から No.1 への反映：almost strong compactness・regular epi 下界・WVP

2026-11-17。**状態：PROOF_RECONSTRUCTED。** 本ノートは No.2 の新しい議論を Problem 1 の研究記録へ移したものであり、独立査読、形式検証、文献上の新規性確認は未実施。No.1 の以前の第18段階および No.2 の原ノートの検証状態を上げるものではない。

## 0. 命題の区別と今回の進展

P1：任意の locally presentable category の任意の *集合個* の射による ordinary coorthogonality class は coreflective。
P2a：同じ主張を *任意の定義可能な射のクラス* に拡張したもの。
P2b：任意の（定義可能）coorthogonality class は二つの full replete coreflective subcategories の交わりとして表示できる。
P2set：P2b を集合個のテストで定まるクラスに限定した命題。

M∞：可測基数の真クラス存在。
ASC∞：almost strongly compact 基数の真クラス存在。
WVP：Weak Vopěnka principle。

No.1 第18段階に既にある

\[
\text{strongly compact cardinals form a proper class}
\Longrightarrow P1 \Longrightarrow M_\infty
\]

を肯定側で次のように改善する。

\[
\boxed{\mathrm{ASC}_\infty\Longrightarrow P1\Longrightarrow M_\infty.}
\]

また No.2 の直接証明の任意濃度 \(\rho\) 版を利用すれば、

\[
\boxed{P2b\Longrightarrow P2set\Longrightarrow M_\infty,}
\]

さらに下界の証人は、**明示的な presheaf 圏の一本の regular epi** による coorthogonality class として実現できる。

別の上界として、以前から No.1 で得た WVP⇒P1 を No.2 の可変修復列へ拡張したことにより

\[
\boxed{\mathrm{WVP}\Longrightarrow P2a\Longrightarrow P1,}
\qquad
\mathrm{WVP}\Longrightarrow P2b.
\]

全関係の見取り図：

\[
\begin{array}{ccccc}
\mathrm{WVP}&\Longrightarrow&P2a&\Longrightarrow&P2b\\
&&\Downarrow&&\Downarrow\\
\mathrm{ASC}_\infty&\Longrightarrow&P1&\Longrightarrow&P2set\\
&&\Downarrow&&\Downarrow\\
&&M_\infty&=&M_\infty
\end{array}
\]

この図は、特に ASC∞⇒P2b や P2b⇒P1 を主張しない。WVP と ASC∞ の含意関係もここでは主張しない。

## 1. P1 の肯定側：二基数に分けた pure-injectivity

### 1.1 Filter extension の弱化

\(\theta\) を無限（必要なら非可算正則）基数とし、\(\kappa\ge\theta\) が \(L_{\theta,\omega}\)-compact であるとは、任意の \(\kappa\)-complete filter が \(\theta\)-complete ultrafilter に延長されることをいう。正則性が必要なら \(\kappa\) をさらに大きい正則基数へ取る。

Brooke-Taylor–Rosický の Definition 2.3 / Proposition 2.4 により、ASC∞ は「任意の \(\theta\) に対し、ある \(\kappa\ge\theta\) が \(L_{\theta,\omega}\)-compact」というスキーマと同値。

### 1.2 小さい対象の \(\kappa\)-pure-injectivity

\(K=\mathbf{Set}^{C^{op}}\)、\(|\operatorname{Mor} C|<\kappa\)、\(|D|<\theta\) とする。正則 \(L_{\theta,\omega}\)-compact な \(\kappa\) の下で、\(D\) は \(\kappa\)-pure-injective となる（No.2 の原ノート §3）。

議論：\(\kappa\)-pure mono \(Y\hookrightarrow X\) と \(h:Y\to D\) に対し、\(X\) の全 sort の元を変数にする同変性・定数値の方程式系 \(E\) を組み立てる。どの \(<\kappa\) 個の制約も purity から解ける。\(\mathcal P_\kappa(E)\) 上の cone filter は \(\kappa\)-complete なので \(\theta\)-complete ultrafilter \(\mathscr U\) に延長できる。各変数が取る値は \(|D|<\theta\) 個であり、\(\theta\)-completeness により \(\mathscr U\)-ほとんど至るところ一つの値が決まる。これらの値は全方程式を満たし、\(h\) を \(X\to D\) に延長する。

**分離した役割：** 純性と cone filter に必要なのは正則 \(\kappa\)；値域が小さいため ultrafilter に必要な完備性は \(\theta\) で足りる。ここは No.1 の強コンパクト性による証明からの改善点。

### 1.3 small coorthogonality への適用

射の集合 \(\Sigma=\{f_i:U_i\to V_i\}\) に対して \(\theta\) を全 \(V_i\) と kernel pair \(U_i\times_{V_i}U_i\) の濃度より大きく選ぶ。同じ \(\kappa\) の pure-injectivity により、\(\mathcal A={}^\perp\Sigma\) は \(\kappa\)-pure subobjects に閉じる。

- 存在：\(Y\to V_i\) を \(X\to V_i\) に延長してから、\(X\) で一意持上げを行う。
- 一意：二射 \(Y\rightrightarrows U_i\) を \(Y\to U_i\times_{V_i}U_i\) に束ねて \(X\) に延長し、\(X\) の直交性を使う。

小さい pure subpresheaf を \(\mu=2^\kappa\) 以下で生成して \(\mu^+\)-directed union を得る。従って \(\mathcal A\) は accessible かつ全小余極限閉、よって locally presentable であり包含が右随伴を持つ。任意の locally presentable category へは充満反射的 presheaf 表示で移送する。

従って、**ASC∞⇒P1**（PROOF_RECONSTRUCTED）。この証明は一般の class-orthogonality まで主張しない。

## 2. 否定側：P1 の制限版にも可測基数の真クラスが必要

No.1 第18段階の無限濃度 \(\rho=|\Omega|\) について、No.2 の母圏

\[
\mathcal K_{\mathrm{fs},\rho}
=\{Z=(Z_0\rightrightarrows Z_1):Z_0\text{ が有限支持}\}
\]

は、明示的な小圏上の presheaf category と同値である。有限支持元を検出する small projective generators として、有限非空 \(E\subseteq\Omega\) それぞれの

\[
P_E=(\Omega^E\rightrightarrows\Omega^E\amalg\Omega^E),
\quad Q=(\varnothing\rightrightarrows M_\rho)
\]

を用いる。Hom(P_E,Z) は \(E\)-supported elements、Hom(Q,Z)=\(|Z_1|\) を与え、全小余極限を保存して jointly conservative である。**非可算 \(\Omega\) で \([n]\) だけを用いて全支持を検出したと誤認しないこと。**

この presheaf category の一本の regular epimorphism

\[
\sigma_\rho:
(\Omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\Omega)
\longrightarrow
(\Omega\rightrightarrows1)
\]

の coorthogonality class を \(\mathcal A_\rho\) とする。\(\rho\) より大きい可測基数が存在しない仮定 \(N_\rho\) の下で、No.1 の非 coreflectivity と No.2 の「任意の coreflective 拡大には固定標的 \(B_\rho\) が入る」という直接証明が両方成立する。

従って P1 の極端に狭い制限版

> 「すべての presheaf category で、一本の regular epi の coorthogonality class は coreflective」

だけでも \(M_\infty\) が必要。これは P1 の下界となる独立した構造的強化であり、定量的な巨大基数下界は既存の \(M_\infty\) と同じ。

なお P2b の反例性には No.2 のより強い「全 coreflective 拡大は \(B_\rho\) を含む」の証明を使う。P1 の非 coreflectivity 自体の証明とは区別する。

## 3. WVP からの肯定側を proper class テストまで拡張

既存の No.1 の正規化修復列（positive_tower および tower_bound_and_weak_vopenka）では固定したテスト集合を使っていた。No.2 では、定義可能な proper class \(\Sigma\) について、各段階 \(X_\alpha\notin\mathcal A\) で「最小ランクの不合格テストの全体」 \(S_\alpha\) だけを修復する可変列を構成した。

具体的には \(\mathcal Q\) を \(\mathcal A\) の regular epi 商閉包として、その trace monocoreflector \(Q\) を使い、
\[
X_0=QB,\qquad
X_{\alpha+1}=Q(T_{S_\alpha}X_\alpha),\qquad
X_\lambda=Q(\lim_{\alpha<\lambda}X_\alpha)
\]
とする。全遷移は \(\mathcal A\)-equivalence で、\(\mathcal Q\) の内部 mono。非合格の後続段階の遷移は section を持たない。

どの集合順序数でも非停止なら、slice \(\mathcal K/X_0\) に \(\mathrm{Ord}^{op}\) が充満埋め込みされ、WVP に反する。従ってある段階で止まり coreflection を与える。presheaf 表示から一般の locally presentable category に移送する。

結論：**WVP⇒P2a⇒P1**（同時に P2a⇒P2b）。proper class の一括積を作らず、最小ランクの不合格テスト集合だけを使う。ここは No.1 にあった WVP⇒P1 をさらに強めたものである。ただし arbitrary colimit-closed class に対する主張ではない。

## 4. 非含意・未解決の点

証明したと扱わないもの：

- P1⇒P2b、P2b⇒P1。
- P1⇒ASC∞、P1⇒WVP、可測基数の真クラス⇒P1。
- ASC∞⇒P2b、WVP と ASC∞ の厳密な含意・整合性強度の比較。
- P1 の正確な無矛盾性強度。
- 元の固定した \(\Omega=\omega\) の A の coreflectivity が「可測基数一つ」で保証されるという主張。
- No.2 の新しい直接証明が独立査読済みであるという主張。

P1 の下界をさらに compactness まで上げるには、単なる \(\rho^+\)-complete ultrafilter では足りない。\(P_\kappa(\lambda)\) 上の fine ultrafilter を、**同じ \(\kappa\) で全 \(\lambda\)** にわたって回収する新しい機構が必要。No.2 の pushout⇒右直交性⇒核の座標分類は、その整合性を引き出す候補だが、fine 性を導く定理は未証明。

## 5. 参照と検証状態

主たる原ノート：
- [No.1 第18段階](measurable_thresholds_and_strong_compactness_2026-11-17.md)。
- [No.1 修復列](positive_tower_2026-11-16.md)。
- [No.1 WVP](tower_bound_and_weak_vopenka_2026-11-16.md)。
- [No.2 P1/P2 転用の詳細](../../../No.2/p1_p2_measurable_wvp_almost_compact_2026-11-17.md)。
- [No.2 直接反例証明](../../../No.2/no2_direct_presheaf_kernel_proof_2026-11-17.md)。

外部参考文献：Brooke-Taylor–Rosický, *Accessible Images Revisited*, Definition 2.3 / Proposition 2.4 (arXiv:1506.01986); Cortés-Izurdiaga–Šaroch, arXiv:2104.08602, §5（小さい加群の pure-injectivity との類似）；Casacuberta–Gutiérrez, *Homotopy reflectivity is equivalent to the weak Vopěnka principle*（WVP の定式化）。これらを新規の P1/P2 定理そのものの出典と誤記しない。

新しい結果は **PROOF_RECONSTRUCTED**。独立査読・形式検証・文献上の新規性確認は未実施。