# No.2: 現在の母圏そのものの presheaf 表示

2026-11-17。状態：PROOF_RECONSTRUCTED。以下の二成分図式圏の同値について直接証明を記録する。独立査読・形式検証は未実施。No.1 の主結果は入力として採用する。本稿作成時点では Problem 2(b) は未解決。

**同日追記。** この presheaf 表示を用いた後続ノート `no2_direct_presheaf_kernel_proof_2026-11-17.md` で、N（非可算可測基数の非存在）の下で予想 F を導く直接証明を書き下した。pushout による右直交性、冪から出る射の座標核、順序数の切れ目を組み合わせる。これにより、N の下で A が任意個の full replete coreflective subcategories の交わりでないという結論に至る。状態は引き続き PROOF_RECONSTRUCTED（独立査読・形式検証前）。本稿末尾の「今後の方針」等はこの追記前の記録として読む。

## 定理

\(M=\operatorname{End}_{\mathbf{Set}}(\omega)\) とし、\(\mathcal K_{\mathrm{fs}}\) を左 \(M\)-set の平行二射 \(Z=(Z_0\rightrightarrows Z_1)\) のうち、第0成分 \(Z_0\) の全元が有限支持であるものの充満部分圏とする。第1成分には有限支持を課さない。

ある明示的な小圏 \(\mathcal E\) に対して

\[
\boxed{\mathcal K_{\mathrm{fs}}\simeq\mathbf{Set}^{\mathcal E^{\mathrm{op}}}.}
\]

これは単に元の大きな母圏 \(\mathcal D=(M\text{-}\mathbf{Set})^{(0\rightrightarrows1)}\) に戻すことではない。圏同値なので、No.2 の coreflectivity と intersection 問題をそのまま保存する。

## 1. 有限支持 \(M\)-set の representable な arity

\(n\ge1\)、\([n]=\{0,\ldots,n-1\}\) とし、\(\omega^n\) に座標ごとの \(M\)-作用を入れる。

任意の左 \(M\)-set \(X\) に対して

\[
\operatorname{Hom}_M(\omega^n,X)
\cong X_{[n]}=
\{x\in X:[n]\text{ supports }x\}.
\]

射 \(f:\omega^n\to X\) は \(x=f(0,\ldots,n-1)\) で決まる。逆に \([n]\) が \(x\) を支持すれば、任意の \(m\in M\) で \(m(i)=a_i\) となるものを選び \(f(a_0,\ldots,a_{n-1})=m x\) と定める。支持性により選択に依存しない。

\(\rho_n:\omega\to\omega\) を \([n]\) 上恒等、その他を0に送る冪等写像とすると

\[
X_{[n]}=\operatorname{Fix}(\rho_n:X\to X)=\operatorname{im}(\rho_n:X\to X).
\]

前向きは支持性から、逆向きは \(u,v\) が \([n]\) 上一致すれば \(u\rho_n=v\rho_n\) となることから従う。\(X\mapsto X_{[n]}\) は、忘却関手 \(X\mapsto|X|\) の自然 retract である。

有限支持 \(M\)-sets の余極限は underlying sets の余極限で計算されるので、忘却関手もその自然 retract も全小余極限を保存する。有限支持の全元は \([n]\)（n>=1）のどれかに含まれる支持を持つ。これにより有限支持 \(M\)-set 圏自体は非空有限集合と全ての写像の圏 \(\mathbf{FinSet}_{+}\) 上の共変集合値関手の圏と同値になる。この既知結果は Staton §6.4 の nominal substitutions の表示とも一致する。

## 2. 二成分図式圏の small projective generators

\[
P_n=(\omega^n\overset{\iota_0,\iota_1}{\rightrightarrows}\omega^n\amalg\omega^n)
\quad(n\ge1),\qquad
Q=(\varnothing\rightrightarrows M).
\]

\(\iota_0,\iota_1\) は余積包含。これらはすべて \(\mathcal K_{\mathrm{fs}}\) に属する。

任意の \(Z\) について

\[
\operatorname{Hom}(P_n,Z)\cong(Z_0)_{[n]},
\qquad
\operatorname{Hom}(Q,Z)\cong |Z_1|.
\]

なぜなら \(P_n\to Z\) は第0成分 \(\omega^n\to Z_0\) を指定すると、第1成分が p,q との可換性で一意に定まるからである。また \(Q\to Z\) は第1成分 \(M\to Z_1\)、つまりその元一個で決まる。

\(\mathcal K_{\mathrm{fs}}\) の全小余極限は元の二成分図式圏で計算される。上の Hom 関手は第0成分の自然 retract と第1成分の忘却関手なので、どちらも全小余極限を保存する。

この関手族は jointly conservative。\(f:Z\to Z'\) がすべての \(P_n,Q\) に関する Hom 上で全単射なら、\(f_1\) は全単射で、\(f_0\) も両対象の全元が何らかの \([n]\) に支持されることから全単射である。従って \(f\) は同型。

\(\mathcal E\) を \(\mathcal K_{\mathrm{fs}}\) の \(P_n\ (n\ge1),Q\) 上の充満小部分圏とする。nerve

\[
N:\mathcal K_{\mathrm{fs}}\to\mathbf{Set}^{\mathcal E^{op}},
\qquad N(Z)(e)=\operatorname{Hom}(e,Z)
\]

は全小余極限を保存し、同型を反映する。標準 coend による左随伴
\[
L(F)=\int^{e\in\mathcal E}F(e)\cdot e
\]
を取る。\(L(ye)=e\), \(N(e)=ye\) であり、\(NL\) は全小余極限を保存するので、representables の全小余極限表示から \(NL\cong1\)。随伴 counit \(LN(Z)\to Z\) に \(N\) を適用すると同型であり、\(N\) は同型を反映するため counit も同型。従って圏同値。

## 3. 添字圏の具体的な Hom

\(n,m\ge1\) に対し

\[
\mathcal E(P_n,P_m)\cong[n]^m,
\qquad
\mathcal E(P_n,Q)=\varnothing,
\]
\[
\mathcal E(Q,P_n)\cong\omega^n\amalg\omega^n,
\qquad
\mathcal E(Q,Q)\cong M^{op}.
\]

合成は元の図式圏から受け継ぐ。有限 arity に対応する可算個の sort \(P_n\) と、有限支持を要求しない第1成分用 sort \(Q\) がある。

## 4. No.1 と No.2 への意味

従来の正則 epi
\[
\sigma:
(\omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\omega)
\longrightarrow
(\omega\rightrightarrows1)
\]
に対する
\[
\mathcal A={}^\perp_{\mathcal K_{\mathrm{fs}}}\{\sigma\}
\]
は、仮定 N（非可算可測基数が存在しない）の下で、No.1 の結果により非 coreflective。上の同値を通して、明示的な presheaf category の一本の regular epi に関する結果となる。

ただし Problem 2(b) の反例を得るには、\(\mathcal A\) が二つの full coreflective subcategories の交わりにならないことが別に必要。元の大きい presheaf \(\mathcal D\) では同じ \(\mathcal A\) が \(\mathcal A_\tau\cap\mathcal A_\sigma\) と表せてしまうため、単純にその母圏へ戻す方法では目的を達成しない。

今後の方針として、\(\mathcal E\) 上の presheaf の成分、projective generators、商と部分対象の言葉で予想 F の普遍性障害を再検討する。

## 5. 文献・関連ノート

- Sam Staton, Relating coalgebraic notions of bisimulation with applications to name-passing process calculi, §6.4: nominal substitutions と非空有限集合上の presheaves の同値。 https://www.cs.ox.ac.uk/people/samuel.staton/papers/calco09.pdf
- Andrew M. Pitts, Locally Nameless Sets, POPL 2023, Remark 3.6: 全変換モノイド上の有限支持作用と renaming sets の同値。 https://www.cl.cam.ac.uk/~amp12/papers/locns/locns-popl-updated.pdf
- No.2/positive_route_and_regular_epi_obstruction_2026-11-16.md: \(\mathcal K_{\mathrm{fs}}\) の local presentability と \(\sigma\) の正則 epi 性。
- No.2/no2_negative_F_endpoint_collapse_2026-11-16.md: 予想 F。
- No.2/no2_coreflector_retracts_one_sided_groups_2026-11-17.md: 最近の増大・retract 証明。
