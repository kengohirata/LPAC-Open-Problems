# 平行二射の単独テスト sigma に対する coreflectivity

2026年11月16日。対象は No.1 の二本のテストのうち sigma だけが定める部分圏である。**追記：可測基数の非存在 N の下で、部分圏全体の coreflectivity の直接証明を得た。** [任意の標的を扱う証明と Problem 2(b) への帰結](sigma_coreflectivity_under_no_measurables_2026-11-16.md)。仮定なしの ZFC での判定は未了である。

以下は初期段階の局所計算を保存した記録であり、元の反例の標的、および sigma の始域における coreflection を ZFC で明示する。新しい直接証明の状態は `PROOF_RECONSTRUCTED`。独立査読・形式検証・新規性の確認はしていない。

## 1 設定と判定対象

\(\Omega=\omega\)、\(M=\operatorname{End}_{\mathbf{Set}}(\Omega)\) とし、左作用を用いる。\(J=(0\rightrightarrows1)\)、\(\mathcal D=(M\text{-}\mathbf{Set})^J\) と置き、対象を \(Z=(Z_0\overset{p_Z,q_Z}{\rightrightarrows}Z_1)\) と書く。

\[
H(A)=\operatorname{Hom}_M(A,\Omega),\qquad
\mathcal A_\sigma=\{Z\in\mathcal D:H(p_Z)\text{ が全単射}\}.
\]

テストは
\[
\sigma:U=(\Omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\Omega)
\longrightarrow
B=(\Omega\rightrightarrows1),
\qquad \sigma=(\pi_0,!).
\]
実際、\(\mathcal D(Z,U)\cong H(Z_1)\)、\(\mathcal D(Z,B)\cong H(Z_0)\) の下で \(\mathcal D(Z,\sigma)\) は \(H(p_Z)\) になる。\(q_Z\) に所属条件は課さないが、\(\mathcal D\) の射は二本の構造射の双方と可換である。

元の定義は [No.1 の証明ノート §3](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md)。有限支持条件を課す別のテスト tau は、今回の所属条件に含めない。

## 2 元の標的 B における coreflection

\(F=\Omega^{\mathbb N}\) に後合成による左 \(M\)-作用を入れる。シフトを
\[
t:F\longrightarrow F,\qquad t(f)(n)=f(n+1)
\]
とし、
\[
C=(F\overset{1_F,t}{\rightrightarrows}F),\qquad
\varepsilon=(\operatorname{ev}_0,!):C\longrightarrow B
\]
と置く。\(t\) は \(M\)-射であり、\(\varepsilon\) は図式の射である。\(p_C=1_F\) なので \(C\in\mathcal A_\sigma\)。

**命題 1（ZFC）。** \(\varepsilon:C\to B\) は \(B\) の \(\mathcal A_\sigma\)-coreflection である。

**証明。** \(Z\in\mathcal A_\sigma\) と任意の射 \(b:Z\to B\) を取る。第1成分は一意なので、\(b\) は \(h_0=b_0\in H(Z_0)\) で指定される。

\(H(p_Z)\) の全単射性を使って、次の列を一意に定める。
\[
\ell_n\in H(Z_1),\qquad
\ell_n p_Z=h_n,\qquad
h_{n+1}=\ell_n q_Z
\quad(n\in\mathbb N).
\]
この再帰は通常の集合上の可算再帰であり、可測基数の非存在を使わない。

\[
a_0(z)(n)=h_n(z),\qquad
a_1(w)(n)=\ell_n(w)
\]
と定義すると、各座標が \(M\)-射なので \(a_0:Z_0\to F\)、\(a_1:Z_1\to F\) は \(M\)-射である。各 \(n\) において
\[
(a_1p_Z)(z)(n)=\ell_n(p_Zz)=h_n(z)=a_0(z)(n),
\]
\[
(a_1q_Z)(z)(n)=\ell_n(q_Zz)=h_{n+1}(z)=(ta_0)(z)(n).
\]
従って \(a=(a_0,a_1):Z\to C\) は図式の射であり、\(\operatorname{ev}_0a_0=h_0=b_0\) から \(\varepsilon a=b\) となる。

一意性を示す。\(a':Z\to C\) が \(\varepsilon a'=b\) を満たすとし、その座標を \(h'_n=\operatorname{ev}_n a'_0\)、\(\ell'_n=\operatorname{ev}_n a'_1\) と書く。構造射との可換性と \(B\) 上の条件から
\[
h'_0=h_0,\qquad \ell'_np_Z=h'_n,\qquad h'_{n+1}=\ell'_nq_Z.
\]
\(H(p_Z)\) の単射性と帰納法により全ての \(h'_n=h_n\)、\(\ell'_n=\ell_n\) が従う。従って \(a'=a\)。

以上より、全ての \(Z\in\mathcal A_\sigma\) に対して
\[
\mathcal D(Z,C)\xrightarrow{\mathcal D(Z,\varepsilon)}\mathcal D(Z,B)
\]
は全単射である。右辺が空なら、左辺の射を \(\varepsilon\) と合成できるので左辺も空である。空 Hom の場合も含む。□

No.1 の [§9.1](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md) の \(Z_*\) はこの \(C\) である。そこに記録されていた順序数試験族からの因子化を、任意の \(\mathcal A_\sigma\)-対象からの射についての普遍性へ強めた。

## 3 sigma の始域でも同じ対象が coreflection を与える

\[
\delta:C\longrightarrow U,
\qquad
\delta_0=(\operatorname{ev}_0,\operatorname{ev}_1),
\quad \delta_1=\operatorname{ev}_0
\]
と置く。\(\pi_0\delta_0=\delta_1p_C\)、\(\pi_1\delta_0=\delta_1q_C\) なので図式の射であり、\(\sigma\delta=\varepsilon\) である。

**系 2（ZFC）。** \(\delta:C\to U\) は \(U\) の \(\mathcal A_\sigma\)-coreflection である。

**証明。** \(Z\in\mathcal A_\sigma\) に対して、\(\mathcal D(Z,\sigma)\) は定義により全単射、\(\mathcal D(Z,\varepsilon)\) は命題1により全単射である。\(\sigma\delta=\varepsilon\) から \(\mathcal D(Z,\delta)\) も全単射となる。□

## 4 射の圏の肯定定理からは全体の結論が出ない

既存の [対象で測る同値射の因子分解](../No.1/codex_sset_handoff/investigations/object_cogenerated_factorization_2026-11-16.md) は、
\[
\mathcal E=\{p\in\operatorname{Arr}(M\text{-}\mathbf{Set}):H(p)\text{ が全単射}\}
\]
が射の圏で coreflective であることを示す。今回はさらに \(q\) を保持する必要があるので、忘却関手 \(\mathcal D\to\operatorname{Arr}(M\text{-}\mathbf{Set})\) による逆像の coreflectivity は、その結論から直ちには従わない。

元の標的 \(B\) ですら、この相違を具体的に確認できる。\(p_B:\Omega\to1\) の \(\mathcal E\)-coreflection は \(1_\Omega:\Omega\to\Omega\) であり、\(q_B\) を \(1_\Omega\) に持ち上げて
\[
T=(\Omega\overset{1,1}{\rightrightarrows}\Omega),\qquad
\gamma=(1_\Omega,!):T\longrightarrow B
\]
を作れる。しかし \(\gamma\) は \(\mathcal A_\sigma\)-coreflection ではない。

実際、もし命題1の \(\varepsilon:C\to B\) が \(C\xrightarrow{a}T\xrightarrow{\gamma}B\) と因子化すれば、\(B\) 上の条件から \(a_0=\operatorname{ev}_0\)、\(p\) との可換性から \(a_1=a_0\) となる。\(q\) との可換性は \(\operatorname{ev}_0t=\operatorname{ev}_0\) を要求するが、左辺は \(\operatorname{ev}_1\) であり、両者は相異なる。従ってその因子化は存在しない。

ここで用いた射の圏の局所計算も直接確認できる。\(e:X\to Y\in\mathcal E\) から \(\Omega\to1\) への四角は \(h:X\to\Omega\) で指定され、\(H(e)\) の全単射性により \(h\) は \(Y\to\Omega\) に一意に延長する。これが \(1_\Omega\) への唯一の因子化である。

## 5 初期段階の到達点と後続の判定

| 主張 | 状態 | 範囲 |
|---|---|---|
| 元の標的 \(B=(\Omega\rightrightarrows1)\) に coreflection がある | `PROOF_RECONSTRUCTED` | ZFC、全ての \(\mathcal A_\sigma\)-対象からの射に対する普遍性 |
| sigma の始域 \(U\) に coreflection がある | `PROOF_RECONSTRUCTED` | ZFC、同じ \(C\) を使用 |
| 一本の射の coreflection に \(q\) を付ければ平行二射の coreflection になる | `FALSE_COUNTEREXAMPLE` | §4 の \(T\to B\) は実際に普遍性を満たさない |
| N の下で \(\mathcal A_\sigma\hookrightarrow\mathcal D\) に右随伴がある | `PROOF_RECONSTRUCTED` | [後続の証明](sigma_coreflectivity_under_no_measurables_2026-11-16.md) §7：任意の標的に対する普遍性 |
| 仮定なしの ZFC で同じ右随伴がある | `NOT_ESTABLISHED` | 後続の証明 §9：可算完備 ultrafilter による基礎計算の障害を明示 |

この局所計算だけでは Problem 2(b) に対する結論は出なかった。後続の大域的証明により、N の下では No.1 の例 A=A_tau∩A_sigma が二つの full coreflective subcategory の交わりであり、同例は Problem 2(b) の反例にはならないことを得た。特定の二対象の計算からこの結論を推論したわけではない。
