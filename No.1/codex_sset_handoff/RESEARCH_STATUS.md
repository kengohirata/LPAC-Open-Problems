# 研究状況 — 2026年11月17日

## 2026-11-17 第23段階：Mitchell order の下界を試行し、今回の研究を停止

**状態：PAUSED。巨大基数下界は更新しない。** ユーザーの「Mitchell order の下界だけ試し、改善が難しければ今回の研究はここまで」の指定に従う。[試行と停止点の全文](investigations/mitchell_order_trial_and_pause_2026-11-17.md)、[No.2 保存版](../../No.2/p1_mitchell_order_trial_and_pause_2026-11-17.md)。

- 目標は P1⇒Mit2∞、すなわち o(κ)≥2 の可測基数の真クラス存在。今回は **NOT_ESTABLISHED**。その非含意も証明していない。
- order2 の条件は、同じ κ 上の正規測度 W の ultrapower 内で κ が可測であること、同値に W が κ 未満の可測基数の集合に集中すること。単に二つの測度や二段の評価を得るだけでは足りない。
- 各ρより上の最初の可測基数は order1。従って、旧下界の可測基数抽出を反復するだけでは order2 を強制しない。また order1 の測度も H(Ω^X) の非座標評価を与えるため、No.2 の座標核分類の仮定を低 Mitchell order に単純置換できない。
- 二段の Hom 評価を実際に計算すると Fubini 積 U⊗U となり、order1 の可測基数だけでも構成できる。Mitchell predecessor の内部所属は得られない。
- Mitchell-minimal な正規測度 U を選ぶと、M_U 内で P1 を再適用できても κ は非可測のまま。内部の可測基数の非有界性と、特定の κ の可測性を混同しない。
- 文献確認：Carmody Theorem 31 は ZFC+GCH のモデルから、可測基数を保存して全ての Mitchell order を1へ落とす class forcing を与える。P1やASC∞の保存は結論しない。Apter–Hamkins Proposition 6 は指定した strongly compact の order1 との両立を与えるが、proper-class レベルの P1⇒Mit2∞ の非含意は得られない。

**停止時の境界（既存の新規含意は引き続き独立監査前）**：Π₂-strong∞⇒P1、ASC∞⇒P1、P1⇒可測基数が真クラス。P2(b) の WVP⇒P2(b)⇒可測基数が真クラスも変更しない。新しい符号化・別の下界候補へは進まず、今回の探索をここで区切った。以下は過去の研究履歴として保持する。

## 2026-11-17 追記：固定小界面つき reduced power の対称商（第22段階）

[No.1 要点](investigations/small_interface_orbit_compression_2026-11-17.md)、[No.2 の詳細証明](../../No.2/p1_small_interface_orbit_compression_2026-11-17.md)。新規直接証明は **PROOF_RECONSTRUCTED**（独立査読・形式検証前）。

- 前段階の局所評価を定数上で相対化し、proper κ-complete filter F の reduced power への対角 Ω→L_F が、κ>max(|M|,ρ) 正則なら κ-pure mono であることを示した。null な L_F では大域的 retraction はない。
- 正則 λ>ρ について、本質的値域 ess([f])={a:|f⁻¹(a)|=λ} が、L_λ から固定した null M-set P⁺(Ω) への全射を与える。定数を区別したまま圧縮するが、λ が十分大きければ逆向きの射は存在しない。
- **固定界面を保持した圧縮定理。** 固定 D→L_λ、μ≥max(ρ,|D|,ℵ₀)、正則 λ>ρ^μ に対し、界面を固定する添字置換群 Γ と、その軌道商 L_λ↠P⁺(Ω)^J を構成した。商は界面内の新しい同一視を作らず、サイズは 2^(ρ^μ) 以下。
- **適用範囲を限定した除外定理。** この Γ-商を保存する固定の貼合せ関手 G と、Γ 不変な固定標的への射を使う候補族は、集合個の合格対象を経由する。coorthogonality class の小余極限閉性で商の合格性を保証する。非対称な構造射・非不変な標的射・非有界な界面・商を保存しない構成までは排除しない。
- 一本の固定選択射 π:{(A,a):a∈A⊆Ω}↠P⁺(Ω) を試した。任意の reduced-power 商 q_F は π に一意左直交する。しかし二つの自然な標的では、一方は自ら合格し、もう一方は null q_F から射を受けないことを示した。
- 上界 Π₂-strong∞ と ASC∞ の含意・分離は今回の文献確認でも未判定。整合性を確認し終えたとは扱わない。次の候補は、固定 signature の中で可変の Boolean/partition incidence を保持し、今回の圧縮の仮定を破る構成。ただしその実現補題は未証明。

**下界は今回も更新していない。P1⇒可測基数が真クラスを維持する。** 固定した小さい null 商への因子化と、小さい null 証人が reduced power の内部にあることを明確に区別した。

## 2026-11-17 追記：必要条件強化のための reduced power と accessibility の境界（第21段階）

[No.1 要点](investigations/lower_bound_reduced_powers_accessibility_boundary_2026-11-17.md)、[No.2 の完全証明](../../No.2/p1_lower_bound_reduced_powers_accessibility_boundary_2026-11-17.md)。状態：**PROOF_RECONSTRUCTED**、独立監査前。

- 任意の proper filter F に対し、M=End(Omega), |Omega|=rho の reduced power L_F=Omega^I/~F から Omega への同変写像は、Fを延長するrho^+-complete ultrafilterと正確に対応する。co-small filterならuniform性、有限cone filterならfine性を表せる。
- 一本のmonoテストのnull class N_rho={empty}∪{X:Hom_M(X,Omega)=empty} はZFCでcoreflectiveかつwell-powered。しかし **N_rhoがaccessible ⇔ あるL_(rho^+,omega)-compact cardinalが存在** を直接証明した。全rhoについてのaccessibilityはASC∞と同値。
- この同値は、coreflectivityを小さい局所証人/accessibilityと取り違える逆証明を排除する。**P1⇒ASC∞の非含意を示したわけではない。**
- Usubaのuniform ultrafilterによる特徴付けから、必要側の具体的な十分目標は、固定rhoのcoreflectorから一つのkappaを得て、その上の全正則lambdaにrho^+-complete uniform ultrafilterを抽出すること。今回はこの実現補題は未証明。
- null reduced powerを第1成分へ単に積因子として追加する候補は、固定した有限像列の合格対象を経由するため、因子化サイズの無界性を与えないことを示した。

**巨大基数下界は今回更新していない。** 引き続き P1⇒可測基数が真クラス。第20段階の二つの十分条件も維持する。

## 2026-11-17 追記：制限版 Product Reflection と Π₂-strong 上界（第20段階）

[証明・依存関係](investigations/restricted_product_reflection_pi2_strong_2026-11-17.md)、[No.2 の完全な主ノート](../../No.2/p1_restricted_product_reflection_pi2_strong_2026-11-17.md)。新規適用は **PROOF_RECONSTRUCTED**（独立査読・形式検証・新規性確認前）。

- 固定した small coorthogonality class A と標的 B に対し、A-equivalence な射 X→B の圏 E_B は slice の全小極限に閉じた **Π₂-定義可能クラス**である。
- E_B に弱始集合があれば、完備性と自己射の等化子から初対象 r:R→B が得られる。pullback によって R の持上げ存在性を、equalizer によって一意性を証明でき、r は A-coreflection となる。
- 従って **集合パラメータ付き Π₂-Product Reflection ⇒ P1**。Bagaria–Wilson の出版版 Theorem 5.13 (n=3) により、これは **Π₂-strong 基数の真クラス存在 ⇒ P1** という新しい上界を与える。strongly compact と混同しない。
- 以前の ASC∞⇒P1 とも、E_B に対する制限版 PRP（PRP_test）で合流する。PRP_test⇔P1 は ZFC の同値である。ただし ASC∞ と全 Π₂-PRP の比較や、最適な純集合論的 meet は未確立。
- 修復列の超限再帰や Q(A) の定義可能性を追跡することは今回不要になった。outward compactness への直接適用に必要な外部充足性は残る。small coorthogonality が全 outer models で絶対的という補題には、完全グラフの collapse による反例を記録した。

現在の二つの上界：**Π₂-strong 基数が真クラス ⇒ P1**、**almost strongly compact 基数が真クラス ⇒ P1**。下界は引き続き **P1⇒可測基数が真クラス**。以下の段階は研究履歴として保持する。

## 2026-11-17 追記：No.2 から P1 への還元と上下界の改善（第19段階）

詳細： [P2 からの転用ノート](investigations/p2_transfer_almost_strong_compactness_2026-11-17.md)、原証明： [No.2 側](../../No.2/p1_p2_measurable_wvp_almost_compact_2026-11-17.md)。状態は **PROOF_RECONSTRUCTED**（独立査読・形式検証・新規性確認は未実施）。以下の第18段階以前は履歴として残す。

- **肯定側の改善。** 強コンパクト基数の真クラスという十分条件を、**almost strongly compact 基数の真クラス**へ弱める二基数の pure-injectivity 論法を記録した。各固定データより大きい \(\theta\) と正則 \(L_{\theta,\omega}\)-compact \(\kappa\) を取り、局所制約の解法には \(\kappa\)-purity を、値域の選択には \(\theta\)-complete ultrafilter を使う。kernel pair により一意性も処理する。結論：\(\mathrm{ASC}_\infty\Rightarrow P1\)。
- **否定側の構造的強化。** 第18段階の任意 \(\rho\) 版を、No.2 で明示した presheaf 圏 \(\mathcal K_{\mathrm{fs},\rho}\) へ移す。そこで、**一本の regular epi \(\sigma_\rho\)** の coorthogonality class だけで、\(\rho\) より大きい可測基数が存在しない場合に非 coreflectivity を得る。従って「全 presheaf 圏の一本の regular epi だけ」の制限版でも、可測基数が真クラス必要となる。巨大基数下界そのものは第18段階と同じ。
- **WVP の利用範囲の強化。** No.1 の集合テストに対する正規化修復列を、No.2 で各段階の最小ランクの不合格テスト集合だけを使う可変列へ拡張した。定義可能な任意のテストクラスについて、非停止なら presheaf の slice に \(\mathrm{Ord}^{op}\) の充満埋め込みを与える。したがって \(\mathrm{WVP}\Rightarrow P2(a)\Rightarrow P1\) を得るという証明候補を記録した（No.2 の主問題 P2(b) より強い肯定側の結論）。
- **現在の P1 上下界：**
\[
\boxed{\mathrm{ASC}_\infty\Longrightarrow P1\Longrightarrow\mathrm{M}_\infty},
\qquad
\mathrm{WVP}\Longrightarrow P1,
\]
  ここで \(\mathrm M_\infty\) は可測基数が真クラス存在すること。WVP と ASC の強さの比較をこの図式から推論しない。
- **未解決：** \(P1\Rightarrow\mathrm{ASC}_\infty\)、可測基数の真クラスから P1、WVP と P1 の同値、正確な無矛盾性強度。No.2 の P2(b) の否定側の直接証明は **独立監査前**であり、P1 の新しい構造的強化を利用するときも条件を明記する。


## 11月17日追記：第18段階・可測基数の下界と強コンパクト性の上界

[新しい直接証明](investigations/measurable_thresholds_and_strong_compactness_2026-11-17.md)。状態は `PROOF_RECONSTRUCTED`（本セッションによる証明の展開・点検。独立査読、外部査読、形式検証、新規性確認なし）。以下の第17段階以前の記述は履歴として保持する。

- Omega を可算集合から任意の無限濃度 rho の集合へ変更した。Hom_End(Omega)(Omega^X,Omega) は rho^+-complete ultrafilters に一致するので、rho より大きい可測基数がなければ座標評価だけになる。有限支持・コンパクト双対・固定標的の因子化下界もそのまま拡張できる。
- 従って、N⇒not P を **M⇒not P** へ強めた。M は可測基数全体が集合であるという仮定。結論は **P⇒可測基数が真クラス存在**。可測基数がちょうど一つの L[U] でも一般の P は偽になる。
- 肯定側では、固定した前層表示とテストデータを十分上回る強コンパクト基数から、標的と kernel pair の pure-injectivity を直接構成した。小さい pure 部分対象の生成と反射移送により、**強コンパクト基数が真クラス存在⇒P** を得た。
- 元の固定例については区別が必要。rho より大きい最初の可測基数 nu があれば、従来の順序数候補 Y_theta が合格するのは正確に theta<nu。これは coreflection の存在証明ではない。一方、rho より大きい強コンパクト基数があれば、その固定クラス A_rho は coreflective。
- 未解決：可測基数の真クラスが P に十分か、元の A_omega が可測基数一つで coreflective になるか、正確な無矛盾性強度。

---

分野別に結果・仮定・証明機構を比較する総覧は [RESEARCH_RESULTS_GUIDE.md](RESEARCH_RESULTS_GUIDE.md) を参照。以下は研究段階ごとの記録である。

研究対象は Adámek–Rosický Problem 1：局所可呈示圏の射の**集合**に対する、ordinary Hom による coorthogonality class は常に coreflective か。**第17段階で、非可算可測基数が存在しない場合の反例の直接証明を書き下した。状態は `PROOF_RECONSTRUCTED` であり、独立査読・外部査読・形式検証・文献上の新規性確認は未実施。** 既存の VP⇒P と合わせた相対的独立性の議論も記録した。

以下の第16段階以前は、その時点での到達点を保存した履歴である。「未解決」「未確立」は当該段階の判断として読む。最新の全体評価は第17段階と末尾の今後の課題に記す。

**Problem 2(b) への追記。** N の下では A_sigma 全体が coreflective であることの直接証明を得た。A_tau は ZFC で coreflective なので、No.1 の A=A_tau∩A_sigma は N の下で二つの full coreflective subcategory の交わりである。同例はその仮定の下で Problem 2(b) の反例にはならない。[証明](../../No.2/sigma_coreflectivity_under_no_measurables_2026-11-16.md)。状態は `PROOF_RECONSTRUCTED`、独立査読・形式検証は未実施。A_sigma の仮定なしの ZFC での判定と、Problem 2(b) 一般の判定は残る。

## 最新・第17段階：M作用付き平行二射による条件付き反例

N=「非可算可測基数が存在しない」の下で、**一つの固定した前層圏、二本の固定したテスト、固定した標的 B** に対し、A={}^⊥Σ の B における解集合条件が失敗する構成を得た。[全定義と直接証明](investigations/parallel_actions_counterexample_2026-11-16.md)。

ユーザーの依頼により、日本語10ページの独立した証明稿に清書した。[閲覧用 PDF](output/pdf/parallel_actions_proof_ja.pdf)・[編集用 LaTeX](output/pdf/parallel_actions_proof_ja.tex)。本文に主定理と相対的独立性を、付録に内部 mono と有限支持テストを外した対照を収めた。組版・相互参照・全ページの表示は確認済みであり、数学的な独立査読は未実施のままである。

- Ω=ω、M=End(Ω)、J=(0⇉1)、D=(M-Set)^J とする。有限支持を検出する固定 mono τ と、H(p_Z):Hom_M(Z_1,Ω)→Hom_M(Z_0,Ω) の全単射性を検出する固定 σ により、A は「Z_0 が有限支持、H(p_Z) が全単射」というクラスになる。
- 有限支持 M-set A では H(A) がコンパクトである。コンパクト零次元 Hausdorff 空間 X に対し C(X)=Cont(X,Ω) の双対 H(C(X)) は X と同相になる。一方、N の下で H(Ω^X) は集合として X に一致する。後者は Isbell の定理で、必要な向きは超フィルターを用いてノート内でも証明した。
- 任意の集合写像 d:X→X から Y=(C(X)⇉Ω^X) を作れる。二射は包含と d に沿う前合成であり、d の連続性を要求しない。これらの Y は A に属する。
- X=[0,κ]、d を後続操作、基点を 0 とする。固定 B=(Ω⇉1) への評価射 ψ_κ:Y_κ→B が任意の Z∈A を経由すると、H(Z_0) から X への連続全射が生じる。その像は閉かつ d-不変で 0 を含むため、超限帰納法で X 全体になる。従って κ≤|H(Z_0)|≤ω^{|Z_0|}。
- κ を任意に大きく取れるため、A↓B には弱終集合がない。これは大きな候補の存在だけでなく、**任意の合格する因子化先**への濃度下界である。N⇒¬P、従って P⇒非可算可測基数の存在を得る。
- 一意性だけのクラス I_Σ では、同じ ψ_κ が内部 mono となるので、固定 B における非 well-poweredness も示せる。ただし非 coreflectivity はこの性質だけから推論せず、上のコンパクト性と因子化下界で直接証明した。

有限支持テスト τ を外すと、全ての ψ_κ が一つの固定した小さい図式 (Ω^ω⇉Ω^ω) を経由する。従って τ の役割を具体的な対照で確認できている。有限モノイドの 2,187 件の作用式、有限冪の Hom、16 サイズ対の因子化方程式は補助検算であり、無限の結論の証明とは区別する。[コード](checks/verify_parallel_actions_formulas.py)・[結果](results/parallel_actions_formulas.json)。

今回の新規部分は主担当による再構成と再点検のみであり、追加担当を起動していない。既存の VP⇒P と組み合わせれば、Con(ZFC+VP) の下で P の ZFC からの相対的独立性が従う、という段階に達した。ただし P⇔VP、P⇔WVP、正確な無矛盾性強度は主張しない。次の優先課題はこの具体的な証明の独立した検証である。

## 第16段階：非終対象へのテストとスライスからの移送

一本の右テスト s:U→V について、終対象の場合の OFS 構成を一般化できるか調べた。**全ての元の B→V を処理しても、スライス OFS の左因子が元の圏で合格するとは限らない。実際の因子分解に対する有限反例を得た。** ただしこれは特定の構成の反例であり、P の反例ではない。

- 大域的な e:A→B の左条件は、全ての b:B→V に対するスライス Hom の全単射性である。一つの b だけを処理しても不十分。
- T=V^{Hom(B,V)} のスライスにおいて全ての元の射を同時に処理すると、右因子 r:C→B は必ず大域的な右クラスに入る。しかし C→V のうち B を経由しないものが左条件に残る。[正確な構成と有限反例](investigations/nonterminal_slice_assembly_2026-11-16.md)。
- Arr(Set) の有限な mono テストで、実際のスライス coreflection が C=(0→1) を返す一方、元の圏の coreflection は 0 となる例を得た。従って、全ての元の射を処理する一回の組立てそのものは否定された。
- 全ての f→s の四角から作る P=B×_{V^Q}U^Q も、A→P の像へ圧縮すると左条件を失い得る。U,V がともに injective、s が通常の全射である有限例でも失敗する。その例の実際の左クラスは Iso なので、OFS は自明に存在する。[像の反例と限界](investigations/nonterminal_image_boundary_2026-11-16.md)。
- 肯定範囲を拡大した：V が subterminal なら一本の s に対する OFS が存在する。また、任意の集合個の mono と終対象への射を混ぜたテストでも、固定した P の部分対象内の閉包で OFS を構成できる。[混合テストの証明](investigations/mixed_mono_terminal_factorization_2026-11-16.md)。
- 既存の有限始域定理を射の圏に適用すると、全テストの始域 U_i が各成分で有限なら、V_i が任意でも OFS が存在する。有限サイズの探索を P の反例探索とみなしてはいけない。

今回、一般化の不足を「元の B にある射だけでは、中間対象の新しい C→V と非 mono テストの lift の像への下降・貼合せを処理できない」と特定した。有限例はこの二つの手順の失敗を証明するが、サイズが真に非有界になることは証明しない。一般の P の肯定・否定・独立性は未解決。新規直接証明は内部で独立点検し、有限の Hom・四角・lift は保存した二つの検証コードと JSON 証明書で再検証した。

## 第15段階：Set の反対圏の埋め込みを使う経路

ユーザーの指示で、道具一覧 T2・T3 の経路を開始した。[主ノート](investigations/setop_coorthogonality_2026-11-16.md)。**直接の集合の像と単純な対角図式は反例候補から除外できたが、一般の構造付き図式は未決定である。**

- N=非可算可測基数の非存在の下で F(X)=Ω^X が Set^op を M-Set（M=End(Ω)）に充満反射埋め込みすることを一次資料で再確認した。N を使う箇所は全基数に対する充満性であり、以下の直接の除外証明自体は ZFC。
- F の像内のテストは、Hom(A,Ω) の濃度が無制限・高々一・ちょうど一の三条件に分類でき、全てに明示的な coreflector を構成した。
- 任意の ambient テストに対しても、無限 X の F(X) が一つ合格すれば、自由生成対象 M=F(Ω) が retract として合格し、全テストが同型になる。通常の商閉包 Q(A) に F(X) が属する場合も同じ。従って非自明な正規化修復列の段階に無限の F(X) を使えない。
- 対角図式 D_X=(Ω→Ω^X) についても、無限 D_X を含むクラス内で全 D_X→b を受ける有界な対象 Z_b を構成した。この族だけでは解集合条件を破れない。[図式ノート §§3–5](investigations/setop_diagram_boundary_2026-11-16.md)。
- 一般の小さい図式なら E:(Set^{C^op})^op→(M-Set)^C は充満反射埋め込みになる。E(G) は一様に小さい商 Q の像 E(Q) の directed union になるが、E(G) の合格が E(Q) に継承されるとは限らず、有限図式の明示例を得た。十分な数の合格する小さい商を選べるかは、この例だけでは決まらない。
- その有限例を詰める中で、前層圏において集合個の対象 W_i に対する Hom(-,W_i) の同値射を左クラスとする OFS を ZFC で構成した。固定した積と pullback の部分対象の中で閉包を反復するため停止する。従って右テストが W_i→1 の場合は肯定できる。[因子分解の証明](investigations/object_cogenerated_factorization_2026-11-16.md)。一般の右テストへの拡張は得ていない。

図式により Ord^op の抽象的な充満埋め込みを運ぶことはできるが、それを固定した集合個のテストの非停止修復列として実現する部分が残る。今回の新しい直接証明は INTERNAL_PROOF_CHECKED（内部の独立点検済み、外部査読・形式検証・新規性確認なし）。一般の P の肯定・否定・独立性は未証明。

## 第14段階：修復列の非停止と Weak Vopěnka principle

ユーザー指定のサイズ上界問題を詰め、集合論との具体的な接続を得た。[証明](investigations/tower_bound_and_weak_vopenka_2026-11-16.md)。**WVP⇒P を導いたが、ZFC 単独の P や独立性は未証明である。**

- 正規化列の B_α→B_0 は商閉包 Q 内で mono である。このため、α<β に対して B_0 上の射 B_α→B_β が一つでもあれば、B_(α+1)→B_α に section ができ、α 段階で停止する。
- したがって非停止なら、slice K/B_0 における Hom(B_β,B_α) は β≥α のとき一元、それ以外は空となり、Ord^op の充満埋め込みを得る。K/B_0 は再び presheaf 圏、従って局所可呈示圏である。
- Weak Vopěnka principle（WVP）はまさにこの形の充満埋め込みを禁止する。従って WVP の下ではすべての列が停止し、全段階のサイズに上界がある。既存の presheaf 還元から一般の P が従う。
- **逆向きは未証明。** ¬WVP が与える一般の充満埋め込みを、固定テスト集合によるこの特殊な修復列として実現できるとは示していない。P⇒WVP、¬WVP⇒¬P、ZFC 独立性は結論しない。

新しい直接証明は PROOF_RECONSTRUCTED（主担当による点検、独立査読・形式検証・新規性確認なし）。**集合論的問題が見えたら止まるというユーザー指示に従い、この接続を記録して停止した。** WVP との同値性、否定側モデル、定義可能性による仮定の弱化は今回ここから先を調べていない。

## 第13段階：ZFC 肯定構成と、その正確な停止条件

ユーザーの指示により、ZFC 肯定方向を優先した。**一般の P は未解決だが、肯定できるテストの範囲と、一般の場合に残る条件を証明した。**

- **終対象・subterminal 終域の肯定。** 任意の局所可呈示圏で、全テストの終域が終対象なら coreflection を明示できる。より一般に、一意性部分圏 I の coreflector R を通した各 RV_i が I で subterminal なら肯定。固定したテスト添字集合の部分集合を増大させ、θ=max(ℵ₀,|Σ|) として θ^+ より前に停止する構成を得た。Split epi のテストも併用できる。[証明](investigations/terminal_positive_2026-11-16.md)
- **一般の presheaf テストの修復関手。** 各 h:B→V_i の持上げと既存の U_i への射との整合性を、集合個の積と pullback で課す T B→B を構成した。A-対象からの Hom はすべて保存され、T B→B が同型であることと B∈A は同値。[構成](investigations/positive_tower_2026-11-16.md)
- **停止の必要十分条件。** A の通常の商閉包 Q(A) の trace を使って上の逆列を正規化すると、各遷移は通常の全射となる。この列について「標的 B の coreflection が存在する」「ある集合順序数で停止する」「全段階のサイズに集合基数の上界がある」は同値。一般の B,Σ に対する無条件の上界は未証明。Q(A) 自体は ZFC で存在するが、A から定義されたクラスであり、計算可能な小さい生成族を得たわけではない。[定理7](investigations/positive_tower_2026-11-16.md)
- **極限での新しい射は、それだけでは障害にならない。** Ab のテスト p:Q/Z→Q/Z に対する実際の正規化列を計算した。Prüfer p-群への p 倍写像を反復した列は ω で停止し、coreflection を与えるが、極限から Q/Z への射にはどの有限段階も経由しないものがある。これは Ab 内で直接構成した例であり、presheaf 表示への自動移送は主張しない。[具体例](investigations/positive_tower_2026-11-16.md), §7。
- **入力ごとの商圧縮。** X∈A と h:X→B に対し、A に残る最大の商を構成できる。停止段階の上界は X に依存する。圧縮後は A から見て monic だが、母圏で mono とは限らず、母圏の well-poweredness でサイズ問題を終えられない。[証明](investigations/positive_solution_set_2026-11-16.md)
- **Purity を経由する一般解法の排除。** テスト終域と kernel pair が共通の λ で pure injective なら肯定。しかし固定した彩色不能クラスの一つに λ-pure-subobject 閉性を与えるだけで、ω₁-strongly compact cardinal が必要になる。そのクラス自体は ZFC で coreflective。従って一般の肯定証明に全クラスの accessibility や pure 閉性を要求することはできない。[証明と一次資料](investigations/positive_purity_2026-11-16.md)

今回の本質的な未解決箇所は、**任意の終域に対して正規化した修復列のサイズ上界、または停止を ZFC で示すこと**である。一意性は全段階ですでに保たれている。極限で新しい射が現れること自体は非停止や非 coreflectivity を意味しない。肯定方向の限界を証明したのではなく、今回の構成で残る停止問題を特定した。新規補題は複数担当による内部点検を行い、外部査読・形式検証・新規性確認とは区別している。

## 第12段階：P を因子分解へ移す還元と直接符号化の排除

ユーザーの承認により、巨大拡大の存在から固定テストの非 coreflectivity へ移す部分を優先した。[第12段階の証明](investigations/factorization_bridge_2026-11-16.md)。**条件付きの「巨大拡大が非有界なら ¬P」という還元は、まだ得られていない。**

- P は、任意の局所可呈示圏と射の集合 Σ に対し、その集合に一意左持上げ性を持つ射を左クラスとする orthogonal factorization system が存在することと同値である。射 f:U→V を射の圏のテスト ρ_f:(1_U)→f に移すことで証明した。弱い持上げ性ではなく、一意持上げを使う。
- 自然なテスト q:Q→Q/Z については、その左クラスが「通常の全射で核が T」、右クラスが「核が F」であり、X→X/t(ker b)→Y が ZFC の因子分解を与える。T-内部単射の巨大化は、この因子分解の不存在を意味しない。
- F-dense extensions i:S₀↪K は、射の圏の I={e:coker e∈T} において、固定 b₀=(S₀→0) の内部部分対象になる。しかし i がテスト f に一意左持上げ性を持つには、Hom(K,ker f)→Hom(S₀,ker f) が同型でなければならない。
- ker f∈F が非零なら、この条件から i は同型となる。核に torsion があれば |K|≤2^ℵ₀、Q を含めば K は可算。既存の G_b を核または核の retract にしても、slender 性と End(G_b)=Z から i は同型となる。従来の T-内部単射をそのままテストに使う直接案は排除された。
- F 所属を始域・終域の条件としてそのまま加えた部分圏は coequalizer で閉じず、固定 S₀ の coslice でも自己 coproduct で閉じない。従ってそのまま small coorthogonality class にはできない。
- 固定 S₀ 上の値でテスト始域へのすべての射が決まる場合は、固定した積の部分群への像を取り、一様な因子化サイズ上界を得られる。特に Ab では、テスト始域がすべて F に属する coorthogonality class は ZFC で coreflective。

直接の射の圏への移し方で残るのは、上の排除条件を避ける新しい核 H と、Hom(K,H)→Hom(S₀,H) が同型になる無界な拡大族を作ること、さらに coreflection への因子化でサイズが消えないことを示すことである。既存の巨大化仮定だけからこの二条件は導けていない。異なる図式への符号化まで不可能と証明したわけではない。新しい直接証明は `PROOF_RECONSTRUCTED`、非 well-poweredness、P の否定、独立性はいずれも未確立である。

## 第11段階：非可算極限の障害と固定自由群の拡大への還元

既存の証明済み結果を前提に進めた。[第11段階の証明](investigations/uncountable_limit_and_dense_extensions_2026-11-16.md)。**ω₁ 極限の零整数双対はまだ証明できていないが、別の同値な構成目標を得た。**

- ZFC で **T well-powered ⇔ F co-well-powered** を証明した。F 内の epi は、通常の余核が T に属する射と同値である。固定した可除包への pushout と、自由表示に沿う pullback が両方向を与える。
- 可算標的での非 well-poweredness は、固定した S₀=Z^(ω) の拡大 S₀↪K で、K∈F、K/S₀∈T を満たすもののサイズが非有界か、という一問に統一できる。逆向きの標的は固定した B₀=(Q/Z)^(ω) にできる。有限 rank の S₀ ではこの非有界性は起こらない。
- V=L では、後続拡大の類を Ext(E,Z)→Ext(K,Z) の下でも独立に選び、巨大化しながら K の整数双対を変えないようにできる。全可算順序数でこの選択を保てるが、ω₁ 極限で新たに現れる双対はまだ排除できない。
- 非可算極限に非零 h:L→Z があれば、十分深い全射影核の像は同じ dZ≠0 に安定する。有限指数の修正後、極限は全段へ全射する稠密な直和因子 M を持つ M⊕Z になる。この可能性を今回の拡大で排除する補題が不足している。
- 巨大な内部部分対象の逆塔を、その項だけで P の反例へ移すことはできない。固定 A_S に入る最初の項一つが、塔中の全 A_S-項から B への共通因子化先になる。非 well-poweredness を得た後も、通常の因子化サイズを無界にする別の構成が必要である。

現在の方法は、**非可算極限での新双対の排除**または**固定 S₀ の F-dense extensions の非有界構成**のところで止まっている。どちらも未証明であり、T の非 well-poweredness、P の否定、ZFC 独立性は未確立である。新しい直接証明の状態は `PROOF_RECONSTRUCTED`。

## 第10段階：全可算順序数への延長と非可算極限の問題

[第10段階の証明](investigations/transfinite_z_null_towers_2026-11-16.md)で、N=可測基数の非存在の下で、固定 G_b への T-内部単射 E_α→G_b をすべての 0<α<ω₁ について構成した。|E_α|=beth_{α+1}、通常の群としては全射であり、すべて torsion-free である。

- 可算共終度の極限に、Baer–Specker 群の大きい直和を部分群として埋め込み、Ext の独立な類を供給できた。E_ω の後の拡大は可能である。
- 核の整数 radical 長は各々可算だが、族全体では可算順序数に一様に抑えられない。族は依然集合個なので、非 well-poweredness とは結論しない。
- 途中のすべての極限で full inverse limit を取る連続な全射塔では、任意の集合長の極限から各段への射影は全射になる。未解決なのはその極限の零整数双対である。
- V=L の下では、既知の Hiller–Huber–Shelah の Ext 定理により、任意の非零 torsion-free T-対象の後続段をさらに大きくできる。これにより後続段の Ext 供給を一般的に解決した。
- Bergman の構成を具体化すると、torsion-free T-対象の全射 ω₁-逆系で極限が Z になる例がある。ただしそれは連続な内部単射の塔ではなく、今回の特殊な極限問題を決定しない。

新しい構成は `PROOF_RECONSTRUCTED`。複数担当による内部点検を行ったが、外部査読・形式検証ではない。**固定 G_b の非 well-poweredness、P の否定・独立性は未証明。** V=L で構成を全順序数へ延ばすには、非可算共終度の極限で T 所属を保つ追加証明が必要である。

## 第9段階：固定した G_b の内部部分対象を拡大で増やす

T={A : Hom(A,Z)=0}=I_{Z→0} の内部部分対象を検査した。[構成・上界・残った条件](investigations/z_null_internal_subobjects_2026-11-15.md)。**T が非 well-powered であるとはまだ示していないが、同じ可算標的 G_b に入る巨大な内部単射を、有限段と可算逆極限まで構成できた。**

- 内部単射 E→B の条件は、核 K が全 T-対象から非零射を受けないこと。K が torsionless なら、ZFC で |E|≤2^{2^{max(ℵ₀,|B|)}}。固定 G_b では上界 2^{2^{ℵ₀}} を得た。
- N=「可測基数が存在しない」の下で、独立な p進群の拡大を G_b 上で fiber product にし、その上界に達する E₁→G_b を構成した。通常の直積ではない。
- Ext の独立な類を使って E_{n+1}→E_n を作り、すべて E_n∈T、|E_n|=beth_{n+1}（n≥1）となる、固定 G_b への内部単射を得た。E₂ の核は torsionless ではなく、最初の上界を実際に超える。
- 可算 inverse-limit slenderness により E_ω=lim E_n も T に属し、E_ω→G_b は内部単射かつ通常の全射。|E_ω|=beth_{ω+1}、核の整数 radical の長さは正確に ω。
- 固定 B の内部部分対象が集合個であることを、その核の整数 radical の長さに一様な ordinal 上界があることと同値にした。今回の族は集合個で、長さ ω の上界内にあるので、非 well-poweredness の証明ではない。

新しい直接証明は `PROOF_RECONSTRUCTED`。**固定 G_b でのサイズの無界性、T 全体の well-poweredness、P の否定・独立性は未決定。** 次に構成を延長するには、極限後の Ext の供給と、より長い逆極限での T 所属を別々に確保する必要がある。T の nondeconstructibility に関する既知結果を well-poweredness と混同していない。

## 第8段階：有限座標性を固定テストで試した結果

可測基数が存在しないという仮定 N の下で、積から slender 群への射の有限座標性を適用した。[証明・具体例・適用限界](investigations/finite_coordinate_trial_2026-11-15.md)。今回試した「小さい群のコピーを大量に並べてサイズ障害を作る」方法は、固定した slender 標的に対して肯定側に働いた。

- 始域・終域が slender なテストの集合 S について、積が A_S（または I_S）に属することは、すべての因子が属することと同値。両クラスの積閉性を得たが、一般の coreflectivity や well-poweredness は結論していない。
- B_κ=Z^κ/Z^{<κ} は任意の slender 群への Hom が零。従ってこれらはすべて上の A_S に属し、slender な標的への非零射を作れず、それ自体を標的にしても恒等射が coreflection になる。
- 固定した集合個の A_S-対象の積から slender な B への射は、サイズを一様に抑えた有限部分積を経由する。また、充満部分圏の内部単射であっても、無限個の非零因子の積から slender な B への射は内部単射になれない。
- 以前の p進群のテスト f=π_a では、任意の集合 J に対し (G_a×_M G_b)^J→G_b^J が A_f-coreflection になる。任意の A_f-対象からの射を対象とする普遍性を示した。全標的に対する結果ではない。

直接証明は `PROOF_RECONSTRUCTED`。因子自体が無界な族や、slender でない別の固定標的への射は上のサイズ上界の範囲外である。有限座標性全体を棄却したのではなく、今回の直接案の限界を確定した。**P の否定・独立性・非 well-powered な I_S は未確立。**

## 第7段階：可測基数の非存在から使える14項目

ユーザーの指示に従い、N=「可測基数が存在しない」から得られる道具を幅広く整理した。[結果・出典・用途・直接導出](investigations/no_measurable_toolbox_2026-11-15.md)。14項目には同じ原理の帰結を含み、独立した14定理という意味ではない。

- 最も具体的なのは、積から slender module への射が有限座標に依存する結果と、B_κ=Z^κ/Z^{<κ} への小さい群からの射を積へ持ち上げる結果の組合せ。N の下では Hom(B_κ,Z)=0 であり、固定した集合個の Z-null な対象から非零射を受けない大きい B_κ を選べる。
- codensity から Set^op を M-Set という前層圏へ充満忠実に埋め込める。随伴を明示した。ただしこの埋め込みは一般の余積を保存せず、small coorthogonality の移送を直ちには与えない。単位的環 Z^X による別の埋め込みも確認した。
- T={A∈Ab : Hom(A,Z)=0} について、N の下で積閉・非 weakly reflective・生成対象の集合なし、しかし一つのテストによる I_S であり ZFC で coreflective、と直接導出した。反射の向きと accessibility を取り違えないための対照例であり、P の反例ではない。
- 既知の Ab の非弱反射例、Grp の集合個の射で表示できない反射例、条件付きの coalgebra 表示、realcompactness、compact space の基本群による実現も比較した。位相の2項目は本文の取得・定理番号照合に制約があり、現時点では低優先度とした。

主な文献結果を確認し、直接の帰結は `PROOF_RECONSTRUCTED` とした。**P の否定、非 well-powered な I_S の確立、反鎖型の集合テスト表示は未解決。** この段階では reduced product による因子化障害と前層圏への符号化を候補とした。そのうち有限座標性の最初の適用結果は冒頭に記す。

## 第6段階の作業仮定：可測基数が存在しない場合

ユーザーの提案に従い、Q の最適な弱化を求めることより、扱いやすい否定側のモデルで反例を作ることを優先する。R=「可測基数が存在する」を選び、¬R を作業仮定に採用した。具体的な構成で必要なら V=L に限定する。必要なのは R⇒P ではなく、P⇒R、またはそのモデルでの ¬P である。[方針・文献・最初の検査](investigations/no_measurable_strategy_2026-11-15.md)

- 可測基数の非存在の下で、可算無限集合が Set の codense な一対象部分圏を与える結果と、Ab における weak reflectivity の否定例を一次資料で確認した。
- 反鎖型の coreflector は cofiltered limits を保存しないことを、ループ集合が減少する逆列で示した。従って、極限保存を仮定する coalgebra の小さい表示定理を直接適用する方法は使えない。
- この保存性の失敗は I_S 表示の不存在を意味しない。一つの有限単射テストで定義される「すべての頂点がループを持つ quiver」のクラスでも、同じ逆列が保存性の失敗を与える。

**P⇒R、¬R⇒¬P、V=L⇒¬P はすべて未証明。** 反鎖型の I_S 表示も未決定であり、以下の小さい商による判定を、今後は ¬R の下で検討する。

## 第5段階：反鎖型のテスト集合表示を調べた結果

反鎖型 C=Quot Coprod(G∪{1}) を I_S として表せるかは、**巨大基数が存在しない側では未決定**である。今回、表示の同値条件と、肯定側の巨大基数仮定による非表示を証明した。[証明と残った条件](investigations/antichain_test_presentation_2026-11-15.md)

- **表示の同値条件**：ある固定 κ 以下の全射商がすべて C に入るなら元の対象も C に入る、という判定が全対象で成り立つことと、C=I_S となるテスト集合 S の存在は同値。その κ が得られれば、小さい対象の counit の fold から S を具体的に作れる。
- **反鎖型の最小性**：各 G∈G の真の部分 quiver F は R_C(F)=0。積も、異なる G,H なら R_C(G×H)=0、同じ G なら R_C(G×G)=ΔG と計算できる。
- **表示の障害**：S のパラメータより上に supercompact cardinal が一つでもあれば、C=I_S は不可能。BCMR Theorem 5.2(a) によって大きい G に小さい非空 C-部分対象が生じ、上の最小性に反する。従って Q=「supercompact cardinal が真のクラス存在する」の下では、どのテスト集合でも表示できない。
- **ユーザーの指摘を受けた仮定の修正**：VP⇒Q⇒P なので、否定側では少なくとも ¬Q が必要。¬VP から例を得られたことだけを、独立性の反例候補として十分と扱わない。「WVP より弱い仮定から P」という結果は本研究では確認していない。

新しい直接証明は `PROOF_RECONSTRUCTED`。¬Q の下で上の κ が存在するか、その先で非 coreflective な A_S を得られるかは未証明である。Q の否定を P の否定と同一視しない。

## 第4段階：前層圏内の非 well-powered な例の比較

ユーザーの提案に従い、前層圏 Quiv の充満部分圏で非 well-poweredness が実際に起こる構成を調べた。[三つの型・証明・未解決部分](investigations/presheaf_non_wellpowered_2026-11-15.md)

- **条件付きの構成**：¬VP の下で反鎖型・上昇鎖型、¬WVP の下で下降鎖型の例を得た。射が高々一本のグラフの真のクラスに終対象を加え、集合個の余積と全射商で閉じる。得られる充満部分圏 C は monocoreflective だが、固定した終対象の内部部分対象が真のクラスになる。
- **共通点と対照**：三つとも「大きなグラフが C 内では subterminal になる」同じ機構を使う。出発点を集合個の生成対象にすると内部部分対象のサイズを一様に抑えられ、well-powered になることも証明した。
- **小さいテストへの接続は未解決**：C はクラス個の単射への coorthogonality で表せるが、テストを集合個に縮められるかは不明。前層圏では、集合個の単射テストによる表示と、あるテスト集合 S に対する I_S 表示は同値である。
- **必要条件を満たしても反例にはならない**：今回の C 自身は coreflective。さらに単射から作る fold テストだけを使うと A_S=I_S=C になり、非 coreflectivity は生じない。固定 S,B に対する解集合条件の失敗は別途必要である。

新しい直接証明の状態は `PROOF_RECONSTRUCTED`。**真正の非 well-powered な I_S の例、一般の P の反例、独立性の証明はまだ得られていない。** 反鎖型 C の表示についての続報は冒頭を参照。

## 第3段階：独立性に向けたリスト彩色の還元

ユーザーが独立性を主目的として明示したため、第3段階では、P から ω₁-strongly compact cardinal の存在を導けるかを調べた。この含意はまだ未証明である。[証明・符号化・未解決部分](investigations/list_colouring_independence_2026-11-15.md)

- **反例の新しい必要条件**：テスト集合 S の持ち上げの一意性だけを課した部分圏 I_S は ZFC で monocoreflective。その内部の単射が残る問題を表す。I_S が well-powered なら A_S は coreflective なので、否定例には I_S の非 well-poweredness が必要になる。
- **連結成分ごとの彩色不能性も除外**：このクラスは ω₁-strongly compact cardinal が存在しない場合に非 accessible になるが、内部の部分対象のサイズは、固定 B に対し 2^max(ℵ₀,|B|) 以下である。従って well-powered であり、これを I_S とする還元では反例にならない。
- **二つの具体的な符号化を除外**：全部分彩色の一意完成を要求するテストは、一元リストの適正なグラフだけを選ぶ。境界射の彩色の一意延長を arrow category の coorthogonality にした場合も、固定対象の部分対象による解集合条件が成り立つ。いずれも全サイズで ZFC の肯定結果となる。
- **内部単射の有限証明書**：元の quiver 圏では非単射だが、成分ごとの非二彩色可能クラスでは単射となる、3頂点6辺→1頂点2辺の例を構成した。kernel pair の2成分の全二彩色数は0と2で、内部の kernel pair は対角だけになることを検算した。

新しい直接証明は `PROOF_RECONSTRUCTED`。独立査読・形式検証は未実施。有限例の検算と一般のサイズ上界の証明は区別する。**非 well-powered な I_S を作る固定テスト、その障害を A_S↓B の解集合条件の失敗へ移す構成、否定側モデルは未確立である。**

## 第2段階：Ab / Grp の無限候補を調べた結果

第2段階では、旧 Ab / Grp ノートの主要証明を再点検し、具体的な無限テストを選んで計算した。主担当による証明の再構成であり、新しい結果の独立した再査読は未実施。

- **追加の除外条件**：Grp では `Z(ker f)` が有限なら coreflective。Ab では有限 kernel が十分。[証明と旧ノートの監査](audits/ab_grp_reassessment.md)
- **二つのクラスの分類**：`Z[1/p]→C_{p∞}` は prime-to-p torsion、`Z_p→Z_p/Z` は p-primary torsion を定義する。いずれも全標的で coreflector を明示できる。
- **固定 f,B の実計算**：p進数による二つの独立な cellular cover `π_a:G_a→M`, `π_b:G_b→M` を使い、`f=π_a`, `B=G_b` とした。`B∉A_f` だが、rank 4 の可算群 `P=G_a×_M G_b` が B の coreflection を与える。任意の大きさの A_f-対象から B への射がこの一つの P を経由する。
- **生成に関する注意**：この例では `A_f` は G_a の小余極限閉包より厳密に大きい。始域による cellular approximation だけで A_f 全体を処理したとは言えない。

具体的定義・全 Hom の計算・普遍性の証明は [無限候補の調査](investigations/algebraic_candidates_2026-11-15.md) に保存した。今回の固定対は反例から除外された。同じ f で全標的に coreflection が存在するかは未決定であり、反例候補を確保できたとはまだ言えない。

## 初回監査の範囲

引き継ぎ後の初回作業では、旧指示書の有限探索器を直ちに実装する前に、数学的な除外範囲と証明を点検した。以下は内部の独立監査と有限検算の結果であり、形式検証・外部査読・新規性確認とは区別する。

## 主要な結果

**肯定側の集合論的仮定。** 原著295頁と VP による肯定を確認した。さらに、固定したテスト集合に対する presheaf coorthogonality が Σ₂ 定義可能であることを示し、BCMR の既存定理と反射移送から、supercompact cardinal が真のクラス存在すれば一般の問題に肯定的に答えられることを記録した。この仮定の必要性や最適性は未確認。[証明・原著・文献の参照](audits/set_theoretic_upper_bound.md)

**有限探索の範囲。** Degreewise finite な始域を持つテスト射は、終域が任意でも ZFC で coreflective class を定義する、という引き継ぎノートの証明を点検した。従って有限2-truncatedテストとその cosk₂ 拡張は、無限の試験対象も含めて肯定結果の範囲にある。汎用有限探索器による直接の非 coreflectivity 探索は優先しない。[compactness と有限始域の証明](audits/compactness_and_finite_tests.md)

**商閉性が失敗する小例。** サイズ `(1,2,4)→(1,1,2)` の2-truncated商 `f:U→V` を構成した。`U⊥f` だが `V` は coorthogonal ではない。さらに `f` 自身が `V` の coreflection であり、商閉性失敗と非 coreflectivity が別であることを明示する。手計算と全1,076候補の列挙が一致した。[例と証明](audits/finite_quotient_witness.md)・[プログラム](checks/verify_quotient_witness.py)・[JSON 証明書](results/quotient_witness.json)

**今後使える還元。** 基本還元、共通の体上の線形テストの肯定結果、固定次数での因子分解サイズ障害を監査した。特に、固定 `B` に coreflection がなければ、ある一つの次数 `n` で因子分解先のサイズをどの基数でも一様に抑えられない。単一テスト `f` では、その次数の `f_n` は非全単射でなければならない。[基本還元](audits/basic_reductions.md)・[線形テストとサイズ障害](audits/linear_and_size_bounds.md)

## 検算と再現

Handoff ディレクトリから実行する。

```sh
python3 checks/verify_quotient_witness.py --output results/quotient_witness.json
python3 existing_checks/check_linear_formula.py
```

前者は標準ライブラリのみを使う。全 identities・自然性・合成を検査し、Hom 数 `(2,2,1,2)` と lift 数 `U:(1,1), V:(1,0)` を得た。別担当によるコードレビューと再実行でも一致した。

後者は NumPy を使う。固定 seed 48291、4次数のランダムな分裂複体と鎖写像について、300件の exact GF(2) checks が成功した。無限次元の証明は別に監査しており、この300件から推論していない。

第3段階で追加した内部単射の有限例は、次で再現できる。

```sh
python3 checks/verify_colouring_internal_mono.py --output results/colouring_internal_mono.json
```

標準ライブラリのみを使用する。一般の非 coreflectivity や独立性の検査ではない。

## 今後の課題

最優先は第17段階の直接証明の独立検証である。特に、有限支持の固定 mono による表示、H(C(X)) の位相を含む同定、任意の因子化先についての閉像・不変性、Isbell の集合論的仮定の四点を分けて検査する。これらに未記載の補題を仮定していないことと、κ に依存するテストを紛れ込ませていないことが主要な監査対象である。

この検証が通った後は、証明の簡約、既存文献との比較、必要な巨大基数仮定の強さを調べる。P⇔WVP や最適な強度は未証明であり、今回の N⇒¬P から推論しない。元の sSet や Quiver での具体的な二本のテストへの翻訳も、今回の D における直接構成とは別の作業である。

以前のアーベル群の未解決事項（固定 S₀ の F-dense extensions の無界構成、非可算極限の保存、p進群の固定 f に対する全標的での coreflectivity）は未解決のまま履歴として残す。今回の直接証明は、それらや第13–16段階の修復列・OFS の新規証明には依存していない。

個別の主張の状態は [CLAIMS_LEDGER.md](CLAIMS_LEDGER.md)、作業の記録は [PROGRESS.md](PROGRESS.md) を参照。`prior_notes/` と元の指示書は変更していない。
