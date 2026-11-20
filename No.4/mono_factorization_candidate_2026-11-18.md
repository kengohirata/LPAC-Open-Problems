# Problem 4 の埋込み因子化候補 M

2026-11-18。

**状態：PROOF_RECONSTRUCTED / 一般の equalizer 閉性と retract 閉性は未解決。** 以下は新候補の定義と基本性質。No.4 の反例完成は主張しない。非反射性は N と独立査読前の No.1 入力 (NC) に依存する。

## 1. 設定と変更点

[Isbell 構成](negative_isbell_transport_fg_factorizations_equalizer_obstruction_2026-11-17.md) の記号を使う。

    Ω=ω, M_1=M_2=End(Ω), J=(0⇉1),
    K=(M_1-Set)^J,
    P=(M_2-Set)^((M_1×J)^op),
    E(Y)_i=Ω^(Y_i).

C は、Y_0 が有限支持で H_1(p_Y):H_1(Y_1)→H_1(Y_0) が全単射となる Y∈K の full replete class。C は ZFC で全小 colimits に閉じ、E は colimits を limits に送る。

D は E(C^op) の replete image。N は「非可算可測基数が存在しない」という仮定。N の下で E は fully faithful なので、D は P の全小 limits に閉じる。積閉性だけは、積を E(∐Y_j) と明示できるため N なしでも成立する。

今回調べる full replete class は

    Z∈M ⇔ 任意の ambient finitely generated F と f:F→Z に対し
            f は F→D_0↪Z, D_0∈D と因子化する。

最後の射は **P の mono** とする。同値に、Z の任意の有限個の元（空集合も含む）が、一つの D-subobject に含まれる。有限個の元が生成する部分前層を取れば、この二つの定義が対応する。

旧 H_fg は最後の射を任意の射としていた。従って

    D ⊆ M ⊆ H_fg.

**同日後続：実際の Isbell 構成について M⊊H_fg を ZFC で証明した。**
[Y_ω の tail quotient と antichain 元](omega_template_tail_antichain_obstruction_2026-11-18.md)
は H_fg に属するが M に属さない。一般の equalizer/retract 閉性は未解決のまま。

## 2. 積と directed unions

**命題 2.1（ZFC）。** M は任意の小積に閉じる。

証明。Z_j∈M と fg f:F→∏_j Z_j を取る。各成分を F→D_j↪Z_j と因子化する。すると

    F → ∏_j D_j ↪ ∏_j Z_j

が求める因子化。D の積閉性を使った。空積も D に属する。□

**命題 2.2（ZFC）。** M は directed unions に閉じる。

証明。Z=⋃_j Z_j を M-objects の directed union とする。fg F→Z は一段階 Z_j を経由する。そこでの F→D_j↪Z_j を Z_j↪Z と合成すれば、最後の射は依然 mono である。□

**命題 2.3（ZFC）。** ambient fg Z に対し、Z∈M ⇔ Z∈D。

証明。順方向では id_Z を Z→D_0↪Z と因子化する。最後の mono は split epi でもあるので同型。逆方向は恒等射を使う。□

有限個の元をそれぞれ D-subobject で覆えることから、D-subobjects 全体が包含について directed であるとは従わない。大きい D-subobject 全体を、有限個の元で指定することはできない。そのため M を「D の directed-union closure」と同一視してはいけない。

## 3. 非反射性の障害は残る

B=(Ω⇉1)、X=E(B) とする。X は P で二元生成である。

(NC) は No.1 の [parallel-actions 証明](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md) の入力、すなわち N の下で C↓B が weakly terminal set を持たないという主張。この入力はまだ独立査読されていない。

N と (NC) の下で X↓D は weakly initial set を持たない。

**命題 3.1（N+(NC)）。** X↓M は weakly initial set を持たず、M は reflective でない。

証明。weakly initial set {f_j:X→Z_j}_j があると仮定する。X は fg なので、各 f_j を X→D_j↪Z_j と因子化できる。任意の X→D（D∈D⊆M）はある f_j の後合成だから、X→D_j の後合成でもある。従って {X→D_j}_j が X↓D の weakly initial set となり矛盾する。□

従って、**もし M の一般の equalizer 閉性を証明できれば**、積閉性と合わせて全小 limit 閉性が得られ、N+(NC) の下で P4 の反例が完成する。この「もし」は未解決である。

## 4. 旧候補を排除した議論との違い

P の signature は濃度 c=2^ℵ0。ambient fg F は c^+-presentable なので、十分大きい filtered colimit への F-map は一段階で表せる。

H_fg では、その段階で得た D_0→Z_j を colimit map と合成すれば定義を満たした。このため H_fg は全 c^+-filtered colimits に閉じ、N+(NC) の下で equalizer 閉性と両立しなかった。

M では、合成

    D_0 ↪ Z_j → colim Z_j

が mono である保証がない。旧証明をそのまま使えない理由はここにある。
その後、[明示的な tail quotient](omega_template_tail_antichain_obstruction_2026-11-18.md)
により、全ての無限正則 μ≤2^c に対する μ-filtered-colimit 閉性の失敗を ZFC で示した。
**2^c より大きい全ての正則基数で失敗するか、ある基数以降では閉じるかは未解決。**

固定した Y∈C の copowers を、その Y に依存する十分長い tail に沿って商にする場合は M 内に残る。[tail quotient の計算](mono_candidate_tail_quotients_2026-11-18.md) では、繰り返し現れる有限生成元の行パターンを使い、colimit 内に別の D-subobject を構成している。この基数条件は必須であり、Y_ω の c^+-tail には適用できない。

## 5. 現在証明できた equalizer の範囲

[mono を保つ圧縮と V-equalizer のノート](mono_local_compression_and_v_equalizers_2026-11-18.md) で次を直接証明した。

- fg F→E(Y) は、各 sort の連結成分数が ≤c の Y_t∈C を用いて F→E(Y_t)↪E(Y) と因子化する。成分数を減らす pushout の片側を全射にし、E(q) の mono 性を確保する。
- Z∈M、W↪V^I（I は任意の集合）なら、任意の Z⇉W の equalizer は M に属する。
- 可算な dual template R,S∈C から作る V^R⇉V^S の equalizer は M に属する。特に V^(2) の自己 equalizers と全 retracts は M に属する。
- 上の自己 equalizer の議論は、dual carrier ≤c の D-subobjects の directed union を始域とする場合にも適用できる。
- p_Y が同型なら、fg F→E(Y) は dual carrier 全体が ≤c の D-subobject を経由する。Y=(A --id,s--> A) と書き、転置 u_0 の可算個の観測 u_0s^n をまとめた像を取る。この場合は任意に大きい Y から V^(2)、さらに可算 dual template から作る V^R の積への equalizer も M に残る。

ここまでの特殊な閉性定理は ZFC の直接証明であり、N+(NC) を必要としない。成分数の上界は carrier の上界を与えないので、一般の W∈M への射の因子化にはまだ隔たりがある。

N の下で一般の equalizer 閉性は、同ノートの条件 (EQ_C^epi) と同値。旧条件からは、終域を H_fg から M に制限する一方、双対の q:Y→Y' に全射性を要求する点が変わる。旧 (EQ_C) の条件付き否定は、新条件の真偽をそのまま決めない。

## 6. 次に必要な判定

一般の M-retract 閉性も未解決である。これは equalizer 閉性の必要条件なので、idempotent e:Z→Z（Z∈M）の像が M に属するかは独立した検査点になる。

単に「D が limit-closed」という仮定だけから、この性質を導くことはできない。[別の presheaf ambient での具体例](mono_local_class_generic_retract_counterexample_2026-11-18.md) では、2-adic integers の増大和 Q_2 が局所的に良い部分対象で覆われる一方、その abstract additive retract Q は覆われない。同じ例で M⊊H_fg と、全ての無限正則 μ に対する μ-filtered-colimit 閉性の失敗も証明した。これは現在の Isbell D に対する結論ではない。

現段階で必要なのは、現在の C の有限支持条件と H_1(p) 条件を使い、(EQ_C^epi) を構成するか、その失敗を具体化すること。積・union・条件付き非反射性は保持できているが、反例として必須の limit 閉性はまだ揃っていない。

N と採用済みの No.1 因子化濃度下界の下では、κ>2^c の j_0:X→E(Y_κ) は、p_Y が同型のどの E(Y) も経由できない（[圧縮ノート §6.7](mono_local_compression_and_v_equalizers_2026-11-18.md)）。さらに、両 sort が有限支持の C-witness 全体も同じ小さい圧縮を持ち、この j_0 を覆えない。

ただし、その後の調査で E(Y_κ)→V^(2) の全写像を分類し、この等化子候補は除外した。[有限彩色の議論](ordinal_witness_maps_to_v2_finite_coloring_2026-11-18.md) は任意の diagonal M-target にも適用される。可算 mono D-chain の union を終域とする全等化子も N の下で安全である。

また、[座標の共通 stage 化](coordinate_stage_uniformization_by_pair_coloring_2026-11-18.md) と [飽和イデアルの議論](nonstage_scalar_maps_require_inner_measurable_2026-11-18.md) により、**measurable cardinal を持つ inner model が存在しない場合**、任意サイズの R∈C から作る元の ω_1-length V^R とその積の部分対象を終域とする等化子は M に属する。この仮定は N より強い。一般の M-target がこの範囲に入るとは主張しない。
