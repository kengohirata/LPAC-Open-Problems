# Coorthogonality と余反射：これまでの結果と証明の仕組み

## 2026-11-17 第20段階：WVP 側を有限階層へ弱めた上界

[制限版 Product Reflection と Π₂-strong 上界](investigations/restricted_product_reflection_pi2_strong_2026-11-17.md) を参照。今回の直接導出は **PROOF_RECONSTRUCTED**（独立監査前）。固定 A={}^⊥Σ と B に対する A-equivalence の slice 圏 E_B が Π₂-定義可能・極限閉であることを使い、**bold Π₂-PRP⇒P1** を得た。Bagaria–Wilson の出版版 Theorem 5.13 (n=3) により **Π₂-strong 基数が真クラス存在⇒P1** となる。

ASC∞ 側と共有する正確な条件は、E_B に限った PRP_test であり、これは P1 と同値。ただし全 Π₂-PRP と ASC∞ の比較や、純集合論的な最適 meet は未確立。新証明は修復列の trace・超限再帰に依存しない。外部モデルへの絶対性を使う素朴な outward-compactness 案には、一本の mono テストでも所属が forcing で変わる例を記録した。以下の第19段階以前の総覧は履歴として残す。

## 2026-11-17 更新：第19段階の最新結果（以下の旧総覧より優先）

[第19段階の証明・依存関係](investigations/p2_transfer_almost_strong_compactness_2026-11-17.md)。以前の第17・第18段階や以下の「2026年11月16日現在」の記述は、研究履歴として残す。新規部分は **PROOF_RECONSTRUCTED**（独立査読・形式検証・新規性確認なし）。

現在の P1 の上下界候補：
\[
\boxed{\text{almost strongly compact 基数が真クラス}
\ \Longrightarrow P1\Longrightarrow\
\text{可測基数が真クラス}},
\qquad \mathrm{WVP}\Longrightarrow P1.
\]
強コンパクト基数の真クラスによる以前の肯定側は、新しい almost strongly compact の十分条件に含まれる。

No.2 から得た P1 側の追加結果：任意の無限 \(\rho=|\Omega|\) に対する有限支持平行二射の母圏 \(\mathcal K_{\mathrm{fs},\rho}\) は、明示的な **presheaf category** として記述できる。この圏の一本の **regular epi** \(\sigma_\rho\) による coorthogonality class だけで、\(\rho\) より大きい可測基数が存在しないとき、非 coreflectivity が発生する。したがって P1 の制限版でも可測基数の真クラスを必要とする。No.2 のより強い「二つの full coreflective subcategories の交わりにもならない」は別の補題 A・B を使い、独立監査前である。

さらに No.1 の WVP⇒P1 の修復列は、No.2 側でクラス個のテストに対する可変修復列へ拡張し、\(\mathrm{WVP}\Rightarrow P2(a)\) まで主張する証明を記録した。P1⇒P2(b)、P2(b)⇒P1、P1⇒ASC、可測基数の真クラス⇒P1、WVP と ASC の比較は確立していない。

---

2026年11月16日現在。研究中に得た結果を、対象・仮定・証明機構・適用限界ごとに整理する。

**到達点は、非可算可測基数が存在しないという仮定の下で、固定した前層圏の二本の固定テストから、余反射を持たない coorthogonality class を構成したことである。** 途中では、ZFC で肯定できる範囲を広げ、多くの反例候補について「なぜその方法では必要な障害が出ないか」を特定した。それらも独立した成果として収める。

この総覧は、セッションで証明済みとして採用した結果を前提にした整理であり、新しい証明や再監査ではない。元の検証状態は [CLAIMS_LEDGER.md](CLAIMS_LEDGER.md) に保持する。最終反例は `PROOF_RECONSTRUCTED`、すなわち直接証明を書き下した段階で、独立査読・形式検証・文献上の新規性確認は未実施である。以前のノートの「未解決」は当時の記録として読む。

## 1. 問題と現在の見取り図

### 記号と問い

局所可呈示圏 \(\mathcal K\) と射の集合 \(\Sigma=\{f_i:U_i\to V_i\}\) に対し、

\[
\mathcal A_\Sigma={}^\perp\Sigma
=\{X\in\mathcal K:\operatorname{Hom}(X,U_i)\to\operatorname{Hom}(X,V_i)
\text{ が全単射、すべての }i\}
\]

と置く。ここで使うのは **ordinary Hom の全単射**であり、ホモトピー類や存在だけの持上げ条件ではない。

命題 \(P\) は「すべての局所可呈示圏とすべての射の集合に対し、\(\mathcal A_\Sigma\) が coreflective（余反射的）である」。具体的には、各 \(B\) に対し、\(\mathcal A_\Sigma\) の対象から \(B\) へのすべての射を一意に受ける普遍射 \(R(B)\to B\) が存在するか、を問う。

さらに次の記号を使う。

| 記号 | 意味 |
| --- | --- |
| \(N\) | 非可算可測基数が存在しない、という仮定 |
| \(\mathcal I_\Sigma\) | 各 \(\operatorname{Hom}(X,f_i)\) が単射となる、一意性だけのクラス |
| \(Q(\mathcal A)\) | \(\mathcal A\) の対象の通常の全射商からなるクラス |
| 内部 mono | 部分圏の対象からの射で相殺できる射。母圏で単射とは限らない |
| well-powered | 固定した対象への内部 mono が、同型を除いて集合個しかないこと |
| 解集合 | すべての合格対象から \(B\) への射を、少なくとも一通り受ける集合個の合格する射。\(\mathcal A\downarrow B\) の弱終集合 |
| OFS | orthogonal factorization system。ここでは一意持上げ性による直交因子分解系 |

### 全体の結論

| 調査領域 | 得られた結果 | 主な仕組み |
| --- | --- | --- |
| 有限性・コンパクト性 | 有限始域、コンパクトなテスト、線形テストなどで ZFC 肯定 | 小さい部分対象への縮約、コンパクト性、線形分裂 |
| Ab・Grp | 多くの定義域・核の条件で ZFC 肯定。巨大な内部単射も構成 | Hom–Ext、整数双対、slenderness、中央拡大 |
| 彩色・Quiver | 非 accessibility と非 coreflectivity を分離。集合テスト表示の条件を抽出 | 非彩色可能成分の選別、小さい商による検出 |
| 一般の ZFC 構成 | 修復列を構成し、余反射の存在をその停止・サイズ上界と同値化 | 積・pullback による修復と商閉包による正規化 |
| 因子分解 | \(P\) の同値な定式化と、終対象・mono・有限始域などの肯定定理 | 射の圏への翻訳、固定対象内の閉包 |
| 集合論的上界 | 既存の \(VP\Rightarrow P\)、本研究での supercompact の真のクラスによる肯定、および \(WVP\Rightarrow P\) | 定義可能性と既存定理の適用、非停止列からの \(\mathrm{Ord}^{op}\) の充満埋め込み |
| \(\mathrm{Set}^{op}\) | 単純な冪・対角図式は反例にならない範囲を特定 | Isbell の埋め込み、自由生成対象、小さい共通受け皿 |
| 最終構成 | \(N\Rightarrow\neg P\)、従って \(P\Rightarrow\) 非可算可測基数の存在 | 片側の有限支持、コンパクト双対、後続操作と閉包 |

最後の結果と既存の \(VP\Rightarrow P\) を合わせると、\(\operatorname{Con}(\mathrm{ZFC}+VP)\) を仮定した \(P\) の ZFC からの相対的独立性が得られる、というのが現在の結論である。\(P\Leftrightarrow VP\)、\(P\Leftrightarrow WVP\)、正確な無矛盾性強度は得ていない。

以下は、重なり合う補題をまとめた結果一覧である。詳細な個々の主張と検証状態は ledger、時系列は [RESEARCH_STATUS.md](RESEARCH_STATUS.md) を参照。

## 2. 共通の還元と、反例に必要な条件

| ID | 結果 | 仕組みと限界 | 証明 |
| --- | --- | --- | --- |
| R1 | sSet のテスト \(f\) が頂点で非全単射なら、合格対象は空対象だけ | 非空 simplicial set から \(\Delta[0]\) が retract として得られる。反例探索では頂点全単射のテストに絞れる | [基本還元 §§1–2](audits/basic_reductions.md) |
| R2 | sSet の集合個のテストは、空対象に関する自明な場合を処理すれば積で一本にまとめられる | 非空 Hom の確保に定値射を使う。任意の圏で無条件に使える積の議論ではない | [基本還元 §1](audits/basic_reductions.md) |
| R3 | \(P_{sSet}\Rightarrow P_{Cat}\Rightarrow P_{Grp}\Rightarrow P_{Ab}\) | nerve、群の圏、abelianization による充満反射埋め込みで移送。対象ごとの移送は埋め込みの像にある標的についての主張 | [基本還元 §2](audits/basic_reductions.md) |
| R4 | 一般の \(P\) は、すべての前層圏での \(P\) を示せば足りる | 局所可呈示圏の充満反射的な前層表示を使う。「sSet 一つで十分」という還元ではない | [集合論的上界 §§2–4](audits/set_theoretic_upper_bound.md) |
| R5 | \(\mathcal I_\Sigma\) は ZFC で monocoreflective。さらにこれが well-powered なら \(\mathcal A_\Sigma\) も coreflective | kernel pair の対角射で一意性を mono テストにする。存在性は、その部分圏内での mono 条件として残る。非 well-poweredness は必要な障害だが、それだけで反例にはならない | [一意性と内部 mono §2](investigations/list_colouring_independence_2026-11-15.md) |
| R6 | sSet の coorthogonality class で余反射が失敗するなら、固定標的への因子化に必要なサイズが、一つの固定次数で全基数を超える | 各次数に別々の一様因子化上界があれば、それらを組み合わせて解集合を得られる。単一テストの場合、障害次数では \(f_n\) が非全単射 | [サイズ判定 §§5–6](audits/linear_and_size_bounds.md) |
| R7 | supercompact cardinal が真のクラス存在すれば \(P\) が成り立つ | 前層圏の合格クラスが集合パラメータ付きで \(\Sigma_2\)・\(\Pi_2\) 定義可能と示し、Bagaria–Casacuberta–Mathias–Rosický の既存定理を適用。R4 で一般の局所可呈示圏へ移す。この十分条件の必要性・最適性は主張しない | [集合論的上界 §§2–4](audits/set_theoretic_upper_bound.md) |

R6 が、その後の方針を定めた。大きい合格対象を作るだけでは足りず、**どの合格する中間対象を経由させても大きさが残る**ことを、固定した標的上で示す必要がある。

## 3. 有限性・コンパクト性・線形性による ZFC 肯定結果

| ID | 対象と仮定 | 得られた結果と仕組み | 証明 |
| --- | --- | --- | --- |
| C1 | \(sSet_{\le1}\)、すなわち指定された反射的 loop を持つ quiver | 任意の集合テストで monocoreflective。辺の lift を独立に変更でき、一意性が通常の商へ降りる。標的内の合格部分対象の和を取る | [基本還元 §3](audits/basic_reductions.md) |
| C2 | full sSet の 1-coskeletal テスト | C1 と \(tr_1\dashv cosk_1\) から肯定。\(B\times_{\cosk_1tr_1B}\cosk_1R(tr_1B)\) が余反射を与える。通常の Quiv における全テストの肯定とは異なる | [基本還元 §4](audits/basic_reductions.md) |
| C3 | \(\mathrm{Set}^{C^{op}}\)。テストの全成分が compact Hausdorff、全構造射とテスト射が連続 | \(\kappa=\max(\aleph_0,\lvert\mathrm{Mor}\,C\rvert)\) として locally \(\kappa^+\)-presentable、従って coreflective。小さい pure 部分前層からコンパクト性で射を延長。一意性は kernel pair に二射を同時延長して確保 | [コンパクト性 §§2–5](audits/compactness_and_finite_tests.md) |
| C4 | 任意の小さい \(C\)。各テストの始域 \(U_i(c)\) が有限、終域は任意 | ZFC で coreflective。像分解の有限→有限部分に C3、残る mono 条件に trace を使う。この拡張では最終クラスの accessibility までは主張しない | [有限始域定理 §6](audits/compactness_and_finite_tests.md) |
| C5 | 有限 2-truncated テストとその \(cosk_2\) 拡張 | C3・C4 の適用範囲。拡張後に対象全体が無限でも肯定範囲に入る。有限探索で見つかった局所的異常から \(P\) の反例は導けない | [低次元への適用 §7](audits/compactness_and_finite_tests.md) |
| C6 | 同一の体 \(k\) 上の simplicial vector space の線形テストを ordinary sSet として見る | locally \(\aleph_1\)-presentable かつ \(\lvert R(B)\rvert\le(\lvert B\rvert+2)^{\aleph_0}\)。自由線形化、Dold–Kan、体上の複体の分裂で条件をホモロジーと境界写像へ翻訳し、有限支持の充填を反復。任意の環上への一般化ではない | [線形テスト §§1–4](audits/linear_and_size_bounds.md) |
| C7 | 有限の商 \((1,2,4)\to(1,1,2)\) | 始域は合格、終域は不合格という商閉性の反例を得た。しかしその商写像自身が終域の余反射。full sSet ではテストに \(cosk_2 f\)、商の証人に \(sk_2 f\) を使い分ける | [有限商の証人 §§1–4](audits/finite_quotient_witness.md) |

この段階で、**商に閉じないこと、有限な形で持上げが失敗すること、余反射が存在しないことは別の問題**だと分かった。C7 は、非単射の余反射が必要になることを示す具体例でもある。

## 4. Ab・Grp：肯定定理、巨大拡大、残された障害

ここでは

\[
\mathcal T=\{A\in\mathrm{Ab}:\operatorname{Hom}(A,\mathbb Z)=0\},\qquad
\mathcal F=\{K:\operatorname{Hom}(T,K)=0\text{ for every }T\in\mathcal T\}
\]

と置く。\(\mathcal F\) の対象は torsion-free だが、torsionless（\(\mathbb Z\) の直積に埋め込める群）と同じ意味ではない。以下のサイズ評価でも、この区別が効く。

### 4.1 肯定範囲と明示的な余反射

| ID | 対象・仮定 | 結果と仕組み | 証明 |
| --- | --- | --- | --- |
| A1 | Ab のテスト定義域がすべて torsionless、またはすべて divisible、またはすべて torsion | それぞれ ZFC 肯定。torsionless では非零核内の \(\mathbb Z\) が整数双対を消す。divisible では像の分裂と Hom–Ext、torsion では素数ごとの可除性を使う。三種類を任意に混合した族まで一括で主張しない | [Ab 再評価 §§1–2](audits/ab_grp_reassessment.md) |
| A2 | 任意のアーベル群 \(K\) に対する \(W_K=\{A:\operatorname{Hom}(A,K)=\operatorname{Ext}^1(A,K)=0\}\) | ZFC で coreflective。可除包への埋め込みで一つの商テストに表し、長完全列と \(\operatorname{Ext}^2_{\mathbb Z}=0\) を使う。特定の torsion 群のクラスまたは局所化環上の加群へ分類 | [Ab 再評価 §§1–2](audits/ab_grp_reassessment.md) |
| A3 | Grp の一般の \(f:U\to V\)、\(N_f=\ker f\) | \(C=C_U(N_f)\)、\(I=f(C)\) とすると、\(C\hookrightarrow U\)、\(C\twoheadrightarrow I\)、\(I\hookrightarrow V\) の三テストへ還元。共役による一意性から中心化を得る。中央拡大の核は \(Z(N_f)\)。これが有限なら ZFC 肯定 | [Grp 再評価 §§3–4](audits/ab_grp_reassessment.md) |
| A4 | \(\mathbb Z[1/p]\to C_{p^\infty}\)、および普通の Ab の \(\mathbb Z_p\to\mathbb Z_p/\mathbb Z\) | 前者は \(p\)-primary 部分を持たない torsion 群、後者は \(p\)-primary torsion 群を合格対象として持つ。Hom の可除性と reduced 群への評価で分類し、対応する torsion 部分を余反射とする | [代数候補 §1](investigations/algebraic_candidates_2026-11-15.md) |
| A5 | \(p\)-進数から構成した可算 rank-3 群 \(G_a,G_b\)、固定テスト \(\pi_a:G_a\to M\) | 相互 Hom の消失と自己準同型環 \(\mathbb Z\) を実現。\(G_b\) は不合格だが、\(P_0=G_a\times_MG_b\to G_b\) がその対象での余反射。\(G_a\) の小さい colimit 閉包より合格クラスの方が大きい。クラス全体の余反射性の証明ではない | [代数候補 §§2–5](investigations/algebraic_candidates_2026-11-15.md) |
| A6 | \(N\) の下、slender な固定標的、テスト両端も slender | 直積からの射は有限座標を経由し、合格条件は各直積成分で判定できる。固定した集合族の直積では、固定 slender 標的への射に小さい共通因子化先がある。A5 の余反射は任意の集合冪に延長できる。slender テストすべての一般肯定定理ではない | [有限座標試行 §§1–6](investigations/finite_coordinate_trial_2026-11-15.md) |
| A7 | \(\mathcal T\) 自体 | ZFC で coreflective。\(t(B)\) を \(B\) 内の全 \(\mathcal T\)-部分群の和として取る。\(N\) の下での非弱反射性・生成集合の不存在と両立する | [道具一覧 T10・§5](investigations/no_measurable_toolbox_2026-11-15.md) |
| A8 | Ab の全テスト定義域が \(\mathcal F\) に属する | ZFC で coreflective。A1 の torsionless 条件を拡張。非単射テストがあれば核中の \(\mathbb Z\) により合格対象は \(\mathcal T\) に入り、定義域への Hom が消えて Hom-null 条件へ還元。全テスト mono の場合は一般の mono 定理 | [因子分解への橋 §7](investigations/factorization_bridge_2026-11-16.md) |

### 4.2 巨大な内部部分対象を作る方法と、その限界

| ID | 得られた結果 | 使った仕組み・残る条件 | 証明 |
| --- | --- | --- | --- |
| A9 | \(E,B\in\mathcal T\) に対し、\(E\to B\) が内部 mono であることと核が \(\mathcal F\) に属することが同値 | 整数値準同型を持たない対象から核への射で判定。核がさらに torsionless なら、\(\mu=\max(\aleph_0,\lvert B\rvert)\) に対し \(\lvert E\rvert\le2^{2^\mu}\)。Hom–Ext の連結写像と整数双対への評価が上界を与える | [Z-null 内部部分対象 §§1–3](investigations/z_null_internal_subobjects_2026-11-15.md) |
| A10 | \(N\) の下、固定した可算 \(B=G_b\) への通常の全射かつ内部 mono \(E_\alpha\to B\) を全 \(0<\alpha<\omega_1\) で構成し、\(\lvert E_\alpha\rvert=\beth_{\alpha+1}\) | 後続段階は独立な Ext 類、可算共終数の極限は slenderness と逆極限。Baer–Specker 群の直和を埋め込み、次段の Ext を供給。全可算段階でも族は集合サイズであり、非 well-poweredness には届かない | [最初の巨大化 §§3–6](investigations/z_null_internal_subobjects_2026-11-15.md)・[超限塔 §§1–4](investigations/transfinite_z_null_towers_2026-11-16.md) |
| A11 | 整数 radical \(R_{\mathbb Z}(A)=\bigcap\ker(A\to\mathbb Z)\) の安定値は \(t(A)\)。固定標的の内部部分対象が集合個であることは、核の radical 長の一様順序数上界と同値 | 長さからサイズへの再帰上界を構成。A10 では可算順序数内の非有界性を得たが、全集合順序数を超える非有界性は得ていない | [Z-null §6](investigations/z_null_internal_subobjects_2026-11-15.md)・[超限塔 §4](investigations/transfinite_z_null_towers_2026-11-16.md) |
| A12 | \(V=L\) では、非零 torsion-free \(X\in\mathcal T\) に対し \(\lvert Y\rvert=2^{2^{\lvert X\rvert}}\) の内部全射単射 \(Y\to X\) を構成できる | 大きい \(\operatorname{Ext}(X,\mathbb Z)\) から拡大を選ぶ。固定標的 \(B\) 上では、\(2^{\lvert X\rvert}>2^{\max(\aleph_0,\lvert B\rvert)}\) なら核の整数双対を保存する選択も可能。ただし非可算極限で新しい整数双対が生じないことは別問題 | [超限塔 §5](investigations/transfinite_z_null_towers_2026-11-16.md)・[非可算極限 §2](investigations/uncountable_limit_and_dense_extensions_2026-11-16.md) |
| A13 | 非可算共終数の極限に非零 \(L\to\mathbb Z\) が生じる障害を、有限指数の調整後の \(L'=M\oplus\mathbb Z\) へ絞った | \(M\) は有限指数修正後の塔の全段階 \(E'_\alpha\) へ全射する。各段階では見えない整数直和因子を排除することが未解決。一般の逆系の反例や巨大 cellular-cover 核は、必要な連続性・\(\mathcal F\)-核の条件を満たさない | [非可算極限 §1](investigations/uncountable_limit_and_dense_extensions_2026-11-16.md)・[超限塔 §§6–7](investigations/transfinite_z_null_towers_2026-11-16.md) |
| A14 | \(\mathcal T\) well-powered \(\Leftrightarrow\mathcal F\) co-well-powered。可算標的の障害は、固定 \(S_0=\mathbb Z^{(\omega)}\) の \(\mathcal F\)-dense extensions のサイズ非有界性と同値 | 可除包への pushout と自由表示の pullback を使う。拡大は \(S_0\hookrightarrow K\)、\(K\in\mathcal F\)、\(K/S_0\in\mathcal T\)。標的を \((\mathbb Q/\mathbb Z)^{(\omega)}\) に固定できる。非有界性自体は未証明で、任意の非可算標的を可算へ還元した結果でもない | [dense extensions §§3–4](investigations/uncountable_limit_and_dense_extensions_2026-11-16.md) |
| A15 | 巨大拡大をそのまま因子分解の反例にする複数の方法を除外 | \(\mathbb Q\to\mathbb Q/\mathbb Z\) の OFS は ZFC で存在し、\(b:X\to Y\) は \(X\twoheadrightarrow X/t(\ker b)\to Y\) と分解。一つの逆塔では最初の適切な項が共通因子化先になる。dense extension の直接利用も、テスト核の条件や colimit 閉性に阻まれる | [dense extensions §5](investigations/uncountable_limit_and_dense_extensions_2026-11-16.md)・[因子分解への橋 §§3–7](investigations/factorization_bridge_2026-11-16.md) |

代数側で進んだのは、巨大化そのものに加えて、**どこまで巨大化してもまだ \(P\) の反例ではないかを正確にしたこと**である。最終的な前層圏の反例によって、Ab・Grp の一般問題や \(\mathcal T\) の well-poweredness が解けたわけではない。

## 5. Quiver・彩色・集合個のテストによる表示

| ID | 対象・結果 | 仕組みと境界 | 証明 |
| --- | --- | --- | --- |
| G1 | Quiv または Quiv/\(\Lambda\) の固定対象 \(D\) に対し、空対象と非 \(D\)-彩色可能対象のクラスは ZFC-coreflective | \(B\) が非彩色可能なら \(B\)、彩色可能なら空対象を返す。内部 mono は母圏の mono。この結果自体は \(D\) を小さく制限しない | [彩色 §§3–4](investigations/list_colouring_independence_2026-11-15.md) |
| G2 | 同じ母圏で、各非空連結成分が非 \(D\)-彩色可能であるクラスも coreflective かつ well-powered | 非彩色可能成分だけを選ぶ。内部部分対象 \(A\to B\) は \(\lvert A\rvert\le2^{\max(\aleph_0,\lvert B\rvert)}\)。内部 mono と母圏の mono は一致しない場合があるが、それでも上界がある | [彩色 §4](investigations/list_colouring_independence_2026-11-15.md) |
| G3 | 特別に構成したリスト彩色の例では、accessibility が \(\omega_1\)-strongly compact cardinal の存在と結び付く一方、余反射は ZFC で存在 | 非 accessibility をそのまま \(P\) の反例に使う方針を除外。この巨大基数との関係を任意の固定 \(D\) に一般化しない | [彩色 §§3–4](investigations/list_colouring_independence_2026-11-15.md)・[purity §§2–4](investigations/positive_purity_2026-11-16.md) |
| G4 | 部分彩色の「一意完成」を要求する具体案は肯定範囲に縮退。任意の局所可呈示圏で、集合個の固定証人 \(D_j\) への一意射と集合個の mono 条件の組合せも肯定 | 前者は各リストが一元で適正彩色済みという条件になる。後者は \(B\times\prod D_j\) 内の strong image でサイズを抑える。\(\operatorname{Hom}(e,D_j)\) 全単射という射のクラスにも解集合を構成 | [彩色 §§5–6](investigations/list_colouring_independence_2026-11-15.md) |
| G5 | 互いに非同型な非空 loopless グラフの定義可能な真のクラスで、任意の二対象間の Hom が高々一本なら、前層圏内に非 well-powered な monocoreflective 部分圏を構成できる | 終対象を加え、余積と全射商で閉じる。相互 Hom の乏しさから各 \(G\to1\) が内部 mono。¬VP の反鎖・上昇鎖、¬WVP の下降鎖はこの機構の異なる順序形。集合個の生成対象では評価により上界が戻る | [非 well-powered 部分圏 §§2–5](investigations/presheaf_non_wellpowered_2026-11-15.md) |
| G6 | Quiv の monocoreflective class がある集合 \(\Sigma\) に対する \(\mathcal I_\Sigma\) になる条件を、小さい商による不合格対象の検出に言い換えた | 一定基数以下の商で全不合格対象を検出できることが必要十分。kernel pair 内の像と counit の pushout-fold を使う。G5 の集合表示は未確立。十分大きい supercompact は反鎖型の表示を妨げる | [集合テスト表示 §§3–5](investigations/antichain_test_presentation_2026-11-15.md) |
| G7 | 「各頂点に loop がある」クラスは有限 mono テスト一本で定義され、ZFC-coreflective だが cofiltered limit に閉じない | 一頂点で loop 集合が \(\{n,n+1,\ldots\}\) の逆列は、極限で loop を失う。極限保存の失敗だけでは非余反射性や集合テスト表示の不存在を結論できない | [loop の逆極限例 §3](investigations/no_measurable_strategy_2026-11-15.md) |

この分野では、**部分圏を大きく複雑にすること**と、**それを集合個の固定テストで切り出すこと**が別の難しさだと分かった。G5 の非 well-poweredness は構成できても、G6 の表示問題を解かない限り、それだけでは今回の反例に使えなかった。

会話で挙がった「n-cycle を終域、可算グラフを始域にする案」や「単純群と巨大基数を使う案」については、独立した定理・証明として確定した記録が見つからないため、成果一覧には加えていない。G7 は loop に関する保存済みの結果であり、これらの cycle 案全体を否定する結果ではない。

## 6. 一般の修復列と直交因子分解

### 6.1 \(P\) の同値条件と、停止問題

| ID | 結果 | 使った仕組み・適用範囲 | 証明 |
| --- | --- | --- | --- |
| F1 | 一般の \(P\) は、任意の局所可呈示圏と射の集合 \(\Sigma\) について \(({}^{\perp_u}\Sigma,({}^{\perp_u}\Sigma)^{\perp_u})\) が OFS になることと同値 | \(s:U\to V\) を射の圏の \(\rho_s:(1_U)\to s\) へ移す。逆向きは \(0\to B\) を因子分解。Ab に限らず、すべての局所可呈示圏に量化した命題の同値。順方向では射の圏の \(P\) を使う | [因子分解への橋 §§1–2](investigations/factorization_bridge_2026-11-16.md) |
| F2 | 前層圏で一般のテストに対する修復関手 \(TB\to B\) を構成 | 全 \(B\to V_i\) の lift と既存の \(B\to U_i\) との整合性を積と pullback で課す。合格対象からの Hom を保存し、修復射が同型 ⇔ \(B\) が合格 ⇔ 修復射が section を持つ | [修復列 §§1–2](investigations/positive_tower_2026-11-16.md) |
| F3 | 前層圏の固定標的 \(B\) について、\(Q(\mathcal A)\) の trace で正規化した列を使うと、\(B\) の余反射の存在 ⇔ 列の停止 ⇔ 全段階のサイズに集合基数の上界 | 遷移を通常の全射かつ \(\mathcal A\)-同値にする。余反射があれば、その固定した台上の集合個の合同関係により停止する。正規化前の生の修復列に同じ必要十分性を主張しない | [修復列 §§3–5・定理7](investigations/positive_tower_2026-11-16.md) |
| F4 | 各入力 \(X\in\mathcal A\)、\(X\to B\) を、\(\mathcal A\) に残る最大の商へ圧縮できる | 合同関係を反復し、圧縮後の射 \(r\) を \(\mathcal A\) から見て monic、すなわち各 \(Z\in\mathcal A\) について \(\operatorname{Hom}(Z,r)\) が単射となるようにする。停止上界は \(X\) に依存し、母圏の mono とは限らないため、固定 \(B\) 上の一様サイズ上界は別問題 | [入力ごとの商圧縮 §§1–4](investigations/positive_solution_set_2026-11-16.md) |
| F5 | Ab のテスト \(p:\mathbb Q/\mathbb Z\to\mathbb Q/\mathbb Z\) では、Prüfer \(p\)-群からの正規化列が \(\omega\) で停止 | 合格クラスは \(\mathbb Z[1/p]\)-加群、商閉包は \(p\)-divisible 群。逆極限の座標 shift が逆写像を与える。極限から \(\mathbb Q/\mathbb Z\) への新しい射が出ても停止し得る | [修復列 §7](investigations/positive_tower_2026-11-16.md) |
| F6 | \(WVP\Rightarrow P\) | 正規化列が停止しなければ、slice に \(\mathrm{Ord}^{op}\) が充満埋め込みされる。内部 mono による相殺で逆方向の射を禁止する。WVP はこれを排除する。一般の \(\mathrm{Ord}^{op}\) 埋め込みを修復列にする逆方向は未証明 | [WVP との接続 §§2–4](investigations/tower_bound_and_weak_vopenka_2026-11-16.md) |

F3 により、「テストが集合個だからサイズもどこかで止まるはず」という期待を、具体的な必要十分条件へ変えられた。最終構成は、この上界を一般には ZFC で証明できないことを、\(N\) の下で直接示すものになった。

### 6.2 肯定できたテストと、失敗した一般化

| ID | 条件・試み | 結果と仕組み | 証明 |
| --- | --- | --- | --- |
| F7 | 終対象を終域とするテスト。より一般に一意性の余反射 \(R\) を通した \(RV_i\) が \(\mathcal I_\Sigma\) 内で subterminal | 任意の局所可呈示圏で ZFC 肯定。終対象なら \(\mathcal I_\Sigma\) 内で \(\prod RU_i\) と \(RB\) の積を取り、subterminal なら有効になるテスト添字を増やす操作が集合段階で停止。split epi テストも併用可能 | [終対象の肯定 §§2–5](investigations/terminal_positive_2026-11-16.md) |
| F8 | 前層圏で全 \(V_i\) と kernel pair \(U_i\times_{V_i}U_i\) が共通の無限正則基数 \(\lambda\) に対して \(\lambda\)-pure-injective | 合格クラスは \(\lambda\)-pure 部分対象に閉じ、accessible かつ coreflective。始域 \(U_i\) 自体の pure-injectivity を仮定する定理ではない | [purity §1](investigations/positive_purity_2026-11-16.md) |
| F9 | 「すべてのクラスで purity／accessibility を示す」一般証明案 | 彩色の一本の mono テストでも、\(\omega_1\)-strongly compact cardinal がなければすべての無限正則 \(\lambda\) で pure 部分対象閉性が失敗する。余反射自体は ZFC で存在するため、この追加要求は強すぎる | [purity §§2–4](investigations/positive_purity_2026-11-16.md) |
| F10 | 前層圏で、固定した集合個の対象 \(W_i\) に対する \(\operatorname{Hom}(-,W_i)\) の同値射を左クラスにする | ZFC で OFS を構成。評価積と pullback から固定した受け皿を作り、その部分対象内で閉包を反復する。右テストが \(W_i\to1\) の場合であり、任意の右テストの定理ではない | [対象で余生成される OFS §§1–5](investigations/object_cogenerated_factorization_2026-11-16.md) |
| F11 | 非終対象への全 \(B\to V\) を一度に slice で処理する案 | 右因子は大域的に合格するが、左因子は中間対象からの新しい \(C\to V\) に失敗し得る。Arr(Set) の有限例で確認。例の実際の余反射は存在し、この一回の組立ての反例に留まる | [slice の組立て §§1–4](investigations/nonterminal_slice_assembly_2026-11-16.md) |
| F12 | 全四角から作る pullback を、元の始域の像へ圧縮する案 | テスト両端が injective、テストが通常の全射でも左条件を失い得る有限例を得た。実際の左クラスは Iso で OFS は存在する。「既に合格した射」の像因子が合格する補題とは区別する | [像への圧縮 §§1–5](investigations/nonterminal_image_boundary_2026-11-16.md) |
| F13 | 前層圏で、終対象への射と mono を混合した集合右テスト。または一本の subterminal 終域テスト | ZFC で OFS。固定対象内の閉包と、mono による lift の像への下降・重なりでの貼合せを使う。任意の射を epi と mono に分けて同じ条件へ置換できるわけではない | [混合テスト §§1–6](investigations/mixed_mono_terminal_factorization_2026-11-16.md)・[slice §4](investigations/nonterminal_slice_assembly_2026-11-16.md) |
| F14 | 前層圏で、全右テストの始域が成分ごとに有限 | 終域が任意でも ZFC で OFS。F1 の \(\rho_s\) へ翻訳して C4 を適用。したがって一本の右テストで反例を探すなら、非 mono・非 subterminal 終域・少なくとも一成分で無限始域が必要 | [混合テスト §7](investigations/mixed_mono_terminal_factorization_2026-11-16.md) |

## 7. 可測基数の非存在と \(\mathrm{Set}^{op}\) の利用

### 7.1 採用した既存の道具

可測基数がない場合の道具一覧は [no_measurable_toolbox](investigations/no_measurable_toolbox_2026-11-15.md) にまとめた。これは既存結果を集めたもので、一覧の全項目を今回新しく証明したという意味ではない。実際に研究を動かした入力は次の通り。

| 道具 | この研究での役割 |
| --- | --- |
| 可算完備超フィルターが主的になること | Isbell の評価表示を導く。普通の非主的超フィルターまで存在しないという意味ではない |
| Isbell：\(\Omega=\omega\)、\(M=\operatorname{End}(\Omega)\)、\(F(X)=\Omega^X\) による \(\mathrm{Set}^{op}\) の充満反射埋め込み | 集合の点を \(M\)-同変な評価射で回収する。最終構成で \(N\) を使う核心 |
| Balcerzyk／Łoś–Eda 型の有限座標性 | 整数値準同型・slender 群への射を有限座標へ落とし、巨大直積の候補を評価する |
| 大きい \(\operatorname{Ext}\) を供給する群論的結果 | A10・A12 の後続拡大を反復する。Isbell を使う最終反例には依存関係がない |
| 非 accessible、非弱反射的、生成集合を持たないクラスの既存例 | どの種類の普遍性が失敗しているかを区別する比較材料。余反射の反例として直接使わない |

realcompactness、コンパクト空間の基本群なども候補として挙げたが、今回必要な Hom の保存を備えた翻訳や反例構成には進んでいない。

### 7.2 冪と図式の試行

ここから \(M\) は上の変換モノイド、\(H(A)=\operatorname{Hom}_M(A,\Omega)\) とする。

| ID | 結果 | 仕組み・限界 | 証明 |
| --- | --- | --- | --- |
| S1 | \(F\) の像内のテストは、\(\lvert H(A)\rvert\) が無制限・高々一・ちょうど一、の三種類に分類され、すべて coreflective | 集合写像による冪の前合成へ還元し、trace と \(\Omega\) との積で余反射を作る。分類したテストの肯定自体は ZFC、像内のすべての射をその形にする充満性に \(N\) を使う | [Setop §§1–2](investigations/setop_coorthogonality_2026-11-16.md) |
| S2 | 無限 \(X\) の \(F(X)\) が一つでも合格、または \(Q(\mathcal A)\) に属すると、全テストが同型になる | 自由射影生成対象 \(M=F(\Omega)\) が retract として得られる。裸の無限冪を非自明な修復列の段階に置く案は使えない | [Setop §§2–3](investigations/setop_coorthogonality_2026-11-16.md) |
| S3 | 有限冪だけが合格する mono テストは作れるが、それ自体は肯定範囲 | 有限像変換の包含 \(M_{fin}\hookrightarrow M\) を使う。一方、任意の標的への写像まで有限座標に依存するとは限らず、超フィルターを使う写像 \(\Omega^\kappa\to\beta\Omega\) がその期待を阻む | [Setop §§3–4](investigations/setop_coorthogonality_2026-11-16.md) |
| S4 | 小さい図式なら \(E:(\mathrm{Set}^{C^{op}})^{op}\to(M\text{-Set})^C\) を \(N\) の下で充満反射埋め込みできる | 元の orthogonality class が部分対象閉なら、像側では商閉性から余反射を構成できる。たとえば元のテストが epi の場合 | [Setop §5](investigations/setop_coorthogonality_2026-11-16.md) |
| S5 | \(E(G)\) は、一様に小さい商 \(Q\) の \(E(Q)\) による directed union として書けるが、合格性は各小部分へ自動では降りない | \(\lambda=\max(\omega,\lvert\mathrm{Mor}\,C\rvert)\) に対し各成分 \(2^\lambda\) 以下の商を使う。有限の矢印図式で不継承を確認。ただしその有限例のクラスは F10 により coreflective | [Setop §6](investigations/setop_coorthogonality_2026-11-16.md) |
| S6 | 対角図式 \(D_X=(\Omega\to\Omega^X)\) の族だけでは解集合条件を破れない | 一つの無限 \(D_X\) を含む合格クラスでは、全 \(D_X\to b\) を受ける固定した合格対象 \(Z_b\) を構成できる。根の射と定値作用に整合する元を集める。\(Z_b\) はこの族の共通受け皿であり、クラス全体の余反射とは限らない | [対角図式 §§3–5](investigations/setop_diagram_boundary_2026-11-16.md) |
| S7 | 抽象的な \(\mathrm{Ord}^{op}\) の埋め込みを図式へ運ぶことはできるが、固定テストの非停止修復列になるとは限らない | 反射埋め込みは Hom を運ぶが、「集合個のテストでちょうど切り出せる」という条件までは与えない。最終構成では、この一般実現問題を解かず具体的な図式を直接作った | [図式の境界 §6](investigations/setop_diagram_boundary_2026-11-16.md) |

裸の冪には自由生成対象が隠れており、単純な対角図式には小さい共通受け皿があった。そこで、**二つの成分の性質を変え、平行な二射に異なる役割を持たせる**ことが次の構成につながった。

## 8. 最終構成：有限支持と平行二射で、すべての因子化を大きくする

完全な定義・証明は [反例ノート](investigations/parallel_actions_counterexample_2026-11-16.md)、清書は [日本語 PDF](output/pdf/parallel_actions_proof_ja.pdf)・[LaTeX](output/pdf/parallel_actions_proof_ja.tex) にある。ここでは機構と各条件の役割をまとめる。

### 8.1 固定した圏・二本のテスト・標的

\[
\Omega=\omega,\qquad M=\operatorname{End}(\Omega),\qquad
\mathcal D=(M\text{-Set})^{(0\rightrightarrows1)}.
\]

これは小さい圏上の前層圏である。対象を \(Z=(Z_0\overset{p_Z,q_Z}{\rightrightarrows}Z_1)\) と書く。以下、\(H(A)\) には離散空間 \(\Omega\) の積 \(\Omega^A\) からの部分空間位相を入れる。

cofree \(M\)-set \(K=2^M\) に作用 \((n\chi)(m)=\chi(mn)\) を入れ、\(U\subseteq K\) を、ある有限 \(S\subseteq\Omega\) に対し \(\chi(m)\) が \(m|_S\) だけに依存する関数全体とする。包含を \(j:U\hookrightarrow K\) と書く。

二本のテストは次のもの。

\[
\tau:(U\rightrightarrows1)\longrightarrow(K\rightrightarrows1),
\qquad
\sigma:(\Omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\Omega)
\longrightarrow(\Omega\rightrightarrows1),
\]

ここで \(\sigma\) の成分は \((\pi_0,!)\)。標的も \(B=(\Omega\rightrightarrows1)\) に固定する。

このとき合格クラスは

\[
\boxed{\mathcal A={}^\perp\{\tau,\sigma\}
=\{Z:Z_0\text{ の全元が有限支持を持ち、 }H(p_Z):H(Z_1)\to H(Z_0)\text{ が全単射}\}.}
\]

有限支持とは、ある有限 \(S\subseteq\Omega\) があり、\(m|_S=n|_S\) なら \(ma=na\) となること。**有限支持を要求するのは \(Z_0\) だけ**であり、\(q_Z\) に追加の条件は課さない。

### 8.2 六つの部品がどう働くか

| ID | 部品・結論 | 証明機構と役割 |
| --- | --- | --- |
| P1 | 有限支持を一本の固定 mono \(j\) で指定 | 点 \(a\) を検出する \(A\to2^M\)、\(x\mapsto(m\mapsto\mathbf1_{\{a\}}(mx))\) と安定化部分モノイドの補題を使う。基数ごとにテストを増やす必要がない |
| P2 | 有限支持 \(A\) の \(H(A)\) はコンパクト | 同変射の値は各元の有限支持に拘束され、\(H(A)\) は有限集合の積の閉部分空間になる。合格する任意の中間対象にもコンパクト性を強制する |
| P3 | コンパクト零次元 Hausdorff 空間 \(X\) について \(C(X)=\operatorname{Cont}(X,\Omega)\) と置くと \(H(C(X))\cong X\) は同相 | clopen 集合と評価射で点を回収する ZFC の双対表示。一方 \(N\) の下で \(H(\Omega^X)\cong X\) は集合の全単射で、こちらの Hom 空間は離散。二つの位相を混同しない |
| P4 | 任意の集合写像 \(d:X\to X\) から合格対象 \(Y=(C(X)\rightrightarrows\Omega^X)\) を作れる | 第一射は包含、第二射は \(d\) に沿う前合成。値域を全関数にすることで \(d\) の連続性が不要になる。第一射の双対は全単射で、有限支持は第一成分が担う |
| P5 | 固定 \(B\) への評価射が合格対象 \(Z\) を経由すると、\(X\) 内に閉で \(d\)-不変な像が生じる | \(T=H(Z_0)\) のコンパクト性と \(H(p_Z)\) の逆写像から、連続な \(h:T\to X\) と集合写像 \(k:T\to T\) を得て \(hk=dh\)。像は閉、\(d\)-不変、かつ基点を含む。\(k\) の連続性は不要 |
| P6 | \(X_\kappa=[0,\kappa]\)、\(d(\alpha)=\alpha+1\)（\(\alpha<\kappa\)）、\(d(\kappa)=\kappa\)、基点 \(0\) なら、P5 の像は全体 | 後続段階は \(d\)-不変性、極限段階は閉性で回収。超限帰納法により任意の大きさの順序数区間が像に含まれ、あらゆる合格する因子化先にサイズ下界を強制する |

### 8.3 得られた結論

各基数 \(\kappa\) に対する合格対象と射 \(\psi_\kappa:Y_\kappa\to B\) について、

\[
Y_\kappa\longrightarrow Z\longrightarrow B,\qquad Z\in\mathcal A
\quad\Longrightarrow\quad
\kappa\le\lvert H(Z_0)\rvert\le\omega^{\lvert Z_0\rvert}.
\]

従って、集合個の合格する因子化先を先に用意しても、その全サイズ上界を超える \(\kappa\) を取れば受けられない。\(\mathcal A\downarrow B\) は弱終集合を持たず、\(B\) の余反射も存在しない。

ここで変えるのは \(Y_\kappa\) だけであり、**前層圏・二本のテスト・標的はすべて固定**されている。これにより \(N\Rightarrow\neg P\) を得る。

さらに、実際の一意性クラスは

\[
\mathcal I_\Sigma=\{Z:H(p_Z)\text{ が単射}\}
\]

であり、\(\tau\) は mono なので、この段階には有限支持条件が残らない。同じ \(\psi_\kappa\) がこの部分圏内で内部 mono となり、固定 \(B\) 上の非 well-poweredness も得られる。非余反射性はこの性質だけから推論せず、上の任意因子化に対する下界で示している。

### 8.4 条件を外した対照と、以前の試行との違い

有限支持テスト \(\tau\) を外すと、すべての \(\psi_\kappa\) が一つの固定した小さい図式 \((\Omega^\omega\rightrightarrows\Omega^\omega)\) を経由する。従って第二のテストだけでは、この族による解集合障害は出ない。一方、両成分に有限支持を要求すると、双対の全単射がコンパクト空間間の同相になり、必要な不連続の後続操作を自由に入れる仕組みが失われる。

代数の塔では非可算極限で性質を保存することが難所だった。今回は、順序数空間の**閉部分集合**を使い、極限段階を閉性で回収した。また、大きい対象が小さい対象へ潰れる問題には、任意の合格する因子化先の双対が \([0,\kappa]\) へ全射することを示して対処した。

この最終証明は、先行する巨大アーベル群の塔や新しい OFS 構成を前提としていない。直接の入力は Isbell の評価表示と、作用・有限支持・コンパクト性・順序数空間に関する補題である。

## 9. 有限計算で確認したこと

以下は保存済みの計算と証明書への索引であり、今回の総覧作成で計算を再実行したという意味ではない。有限検算は式や具体例の確認に使い、無限の余反射不存在や独立性の根拠とは分ける。

| 検算 | 確認した内容 | コード・証明書 |
| --- | --- | --- |
| GF(2) の線形式 | Dold–Kan による Hom 次元式の有限ランダム例。300例、seed 48291 | [コード](existing_checks/check_linear_formula.py) |
| 有限商の証人 | \((1,2,4)\to(1,1,2)\) と strict Hom の列挙 | [コード](checks/verify_quotient_witness.py)・[JSON](results/quotient_witness.json) |
| 彩色クラスの内部 mono | 3頂点6辺→1頂点2辺の例。内部 mono と母圏 mono の差 | [コード](checks/verify_colouring_internal_mono.py)・[JSON](results/colouring_internal_mono.json) |
| slice の組立て | 有限 Arr(Set) 例で、slice の左因子が大域的な左条件を失うこと | [コード](checks/verify_nonterminal_slice_obstruction.py)・[JSON](results/nonterminal_slice_obstruction.json) |
| 像への圧縮 | 全四角からの構成で、像へ縮めると lift が失われること | [コード](checks/verify_nonterminal_image_obstruction.py)・[JSON](results/nonterminal_image_obstruction.json) |
| 平行二射の式 | 3点の変換モノイドで作用式2,187件、有限冪の Hom、16サイズ対の因子化方程式 | [コード](checks/verify_parallel_actions_formulas.py)・[JSON](results/parallel_actions_formulas.json) |

汎用の有限 simplicial-set explorer を完成させたという成果ではなく、必要な例に絞った検算群である。

## 10. 何が残っているか

| 未解決・未実施の点 | 現在の位置 |
| --- | --- |
| 最終反例の独立した数学的検証 | 直接証明と清書はある。総覧作成では検証状態を上げていない |
| \(P\) と巨大基数原理の正確な関係 | \(WVP\Rightarrow P\Rightarrow\) 非可算可測基数の存在、という範囲。\(P\Rightarrow WVP\) や正確な無矛盾性強度は未証明 |
| 特定の圏だけに制限した \(P\) | Ab・Grp・通常の Quiv・sSet の一般問題を、今回の別の前層圏の反例から自動では結論できない。各肯定範囲は上記の通り |
| \(\mathcal T\) の well-poweredness | 全可算順序数で巨大な内部部分対象は作れたが、非可算極限と全基数非有界性が残る |
| \(\mathcal F\)-dense extensions の非有界性 | 固定可算自由群上の問題への還元はあるが、必要な非有界構成は未完成 |
| 反鎖型部分圏の集合テスト表示 | 非 well-powered な部分圏を作る方法と、小さい商による表示判定はある。両者を一般に結び付けてはいない |
| 任意の \(\mathrm{Ord}^{op}\) 埋め込みの修復列による実現 | 非停止列から埋め込みを得る方向は証明した。逆方向は最終構成でも解いていない |
| 可測基数が存在するが WVP を仮定しない状況 | 最終反例の \(N\) を外した判定や、肯定側との間を埋める分類は得ていない |

これまで繰り返し効いた肯定側の仕組みは、固定した標的の中、または固定した積・pullback の中に、合格する小さい受け皿を作ることだった。否定側では、その受け皿をどれほど工夫しても大きさを消せない構成が必要だった。最終構成では、有限支持によるコンパクト性と後続操作への不変性を組み合わせ、その要求を任意の因子化に対して実現した。
