# Mitchell order 2 の下界を試した結果と、今回の研究の停止点

2026-11-17。

**研究状態：PAUSED。下界は更新しない。** ユーザーの依頼は「Mitchell order の下界だけ試し、改善が難しければ今回の研究をここで止める」。今回はこの範囲だけを調べ、別の巨大基数候補・Boolean incidence・新しい貼合せ構成へは進まない。

**結論：P1⇒Mit2∞ は NOT_ESTABLISHED。否定も証明していない。** P1 の従来の下界「可測基数が真クラス存在」を維持する。本稿の標準的補題・計算の再構成は PROOF_RECONSTRUCTED、独立査読・形式検証なし。既存の P1/P2 の新規証明全体を今回再監査したものではない。

## 0. 目標と記号

P1 は、任意の locally presentable category の集合個の射による ordinary coorthogonality class が coreflective であるという命題。

    M∞     := ∀α ∃κ>α (κ は可測)
    Mit2∞  := ∀α ∃κ>α (κ は可測かつ o(κ)≥2)

ここで Mitchell 順序は、同じ κ 上の非主的正規測度 U,W について

    U ◁ W  ⇔  U∈M_W,
    M_W = Ult(V,W) の推移的崩壊

と定義する。o(U) はこの順序での測度のランク、o(κ)=sup{o(U)+1:U は κ 上の正規測度} とする。従って、κ が可測なら o(κ)≥1、測度 U の最小ランクは0である。測度のランク0と基数のorder1を混同しない。

今回の目的は P1⇒M∞ を P1⇒Mit2∞ に強められるか調べること。P2(b) 自体に対する新しい下界は今回主張しない。

入力として確認した No.1 の最新状態は第22段階で、下界は M∞、上界は proper class of Π₂-strong cardinals と ASC∞ の二系統（ともに新規適用の独立監査前）。これらは今回変更しない。

## 1. Order 2 に本当に必要な条件

κ を可測基数、D_κ={α<κ:α は可測} とする。標準的な特徴付けは

    o(κ)≥2
      ⇔ ∃ 正規測度 W on κ, M_W ⊨「κ は可測」
      ⇔ ∃ 正規測度 W on κ, D_κ∈W.                 (1)

概略の確認：W の正規性から [id]_W=κ。従って Łoś の定理は D_κ∈W と M_W 内での κ の可測性を同値にする。κ 未満の可測性は V_κ の範囲で判定できる。M_W は κ 列に閉じているため、M_W 内の κ 上の正規測度は V から見ても正規測度であり、Mitchell predecessor を与える。逆に U∈M_W が正規測度なら M_W は κ の可測性を認識する。

したがって、単なる測度の二個存在、非主性、高完備性、あるいは異なる基数上の測度の存在だけでは不十分。必要なのは同じ κ 上の測度が別の正規 ultrapower 内部に現れること、同値に (1) の正規性と集中条件の同時成立である。

一次資料：K. J. Williams, Math655 Lecture Notes, Part 1.1, §6, Definition 67、Corollary 70、その後の o(κ)=1 / o(κ)≥2 の説明、Lemma 71。

## 2. 既存の可測基数抽出を繰り返す案

### 補題 A：次の可測基数は order 1

任意の順序数 ρ に対して κ が ρ より大きい最初の可測基数なら、o(κ)=1。

証明。D_κ⊆ρ+1 なので D_κ は κ 内で有界。κ 上の非主的 κ-complete ultrafilter は κ 未満の濃度の集合を含まず、したがっていかなる正規測度 W についても D_κ∉W。(1) から o(κ)<2。一方 κ は可測なので o(κ)≥1。□

従って、M∞ の下で「各 ρ の上の最初の可測基数」を選ぶと、得られるのはむしろ真クラス個の order 1 の可測基数である。M∞ と Mit2∞ は異なる主張であり、存在証明を単純に反復するだけでは高い Mitchell order を強制しない。

### 既存の Isbell 型計算への影響

|Ω|=ρ、M=End(Ω)、H=Hom_M(-,Ω)、F(X)=Ω^X とする。No.1 の入力は

    H(F(X)) ≅ X 上の ρ^+-complete ultrafilters

である。κ>ρ が可測なら、その κ-complete 正規測度 U は H(Ω^κ) の非座標評価を与える。κ が order 1 でもこの射は存在する。

したがって、「ρ より大きい可測基数がない」という仮定を「ρ より大きい order≥2 の可測基数がない」に単に置き換えても、H∘F≅Id は回復しない。後者の仮定の下でも order1 の測度が非座標評価を供給し得る。

No.2 の local-object の冪表示・座標核分類は、この H∘F≅Id を入力としていた。それらを低 Mitchell order 仮定の下へそのまま移すことはできない。これは P1⇒Mit2∞ の反証ではなく、既存証明の仮定の置換が成立しない理由である。

## 3. 二段の Hom 評価／Fubini 積を試す

ρ<κ とし、κ 上の非主的正規測度 U を取る。ρ 個の値の分割を U が選択するので

    h_U:Ω^κ→Ω

が定まる。二段の評価

    Φ:Ω^(κ×κ)→Ω,
    Φ(f)=h_U(α↦h_U(β↦f(α,β)))                    (2)

を取る。各 h_U は End(Ω)-同変なので、Φ も同変である。

(2) に対応する超フィルターは Fubini 積

    A∈U⊗U
      ⇔ {α<κ:{β<κ:(α,β)∈A}∈U}∈U.

これは κ-complete である。η<κ 個の A_i∈U⊗U に対し、各外側の U-大集合の交叉を取り、その中の各 α で η 個の内側の U-大集合を交叉すればよい。各 singleton は小さいので非主的でもある。

しかし、この構成には o(κ)≥2 を使っていない。κ が最初の可測基数、あるいは任意の order1 の可測基数であっても同じ構成ができる。従って (2) の存在を order2 の証拠とすることはできない。

さらに第一射影 pr_1:κ×κ→κ による押出しは

    (pr_1)_*(U⊗U)=U

であり、少なくともこの自然な正常化方向は元の測度へ戻る。必要な U_0∈Ult(V,U_1) という同じ κ 上での内部所属は得られていない。

**判定：二段の評価を追加するだけの強化は失敗。** Ultrapower の反復可能性や超フィルターの積は、Mitchell predecessor の存在とは区別する。

## 4. Ultrapower 内で P1 を再適用する案

P1 の presheaf 版は、小圏・テスト集合・標的・射を集合コードで量化した一階の文として扱える。この版が V で成立すると仮定すれば、任意の正規 ultrapower j_U:V→M_U について、elementarity により M_U でも同じ版が成立する。

しかし、これは M_U⊨「κ は可測」を意味しない。

実際、κ 上の正規測度の Mitchell 順序は well-founded なので、rank0 の測度 U を選べる。そのとき

    M_U ⊨「κ は可測でない」

である。それでも、V⊨P1 なら elementarity による M_U⊨P1 とは両立する。既存の下界を M_U 内で適用して得られるのは M_U 内の可測基数の非有界性であり、特定の κ の可測性ではない。

同様に、j_U(U)∈M_U は自動的に成り立つが、j_U(U) は j_U(κ) 上の測度であって κ 上の測度ではない。これを U◁U や order2 の証人と読み替えてはいけない。

**判定：任意の ultrapower に P1 を反映して繰り返す方法だけでは不十分。** rank0 ではない正規測度を選べることを別途保証する必要があり、それがまさに現在欠けている部分である。

## 5. 文献による強度の確認

### 5.1 可測基数の真クラスから高 Mitchell order は自動的に出ない

Erin Carmody, Force to change large cardinal strength, arXiv:1506.03432v2, Theorem 31 は、V⊨ZFC+GCH と任意の ordinal α に対し、適切な class-forcing extension で

    o(κ)^(V[G])=min{α,o(κ)^V}   (κ>α)

とでき、α≥1 なら可測基数をすべて保存し新しい可測基数を作らない、と述べる。

α=1 とすれば、出発モデルの可測基数が真クラスなら、それを保ちながら全可測基数を order1 にできる。これは GCH を含む同定理の仮定の下での相対的モデル構成として引用する。

**重要：この forcing が P1、ASC∞、または P2 を保存するとは同定理から言えない。** 従って、この結果だけでは P1⇒Mit2∞ の非含意は示していない。示しているのは、現在の下界 M∞ だけから Mit2∞ に進めないこと。

### 5.2 Compactness と同じ基数での Mitchell rank を混同しない

Apter–Hamkins, Exactly Controlling the Non-Supercompact Strongly Compact Cardinals, arXiv:math/0301016, Proposition 6 は、supercompact κ から、κ が strongly compact のまま trivial Mitchell rank となる forcing extension を与える。本文の trivial Mitchell rank は、本稿の基数の記法では o(κ)=1 に対応する。

従って「ある strongly compact κ は必ず o(κ)≥2」という主張は正しくない。まして almost strongly compact κ 自体に高 Mitchell rank を自動的に付与できない。

ただし、指定した strongly compact の rank を1にできることは、他のすべての可測基数の rank も1にできることとは違う。今回、この結果から

    ASC∞ かつ ¬Mit2∞

のモデルを得たとは主張しない。proper-class レベルでの当該含意・非含意を決着する定理は、この限定的調査では確認していない。

### 5.3 測度の個数と Mitchell 比較は異なる

Gitik–Kaplan, On Restrictions of Ultrafilters from Generic Extensions to Ground Models, Theorem 4.17 は、明記された supercompactness・測度一意性・GCH・上方 inaccessible 非存在の仮定の下で、最初の可測基数が strongly compact で、指定した η 個の正規測度を持つモデルを構成する。

最初の可測基数は補題Aにより order1 である。従って、正規測度が複数あるだけでは order2 は保証されない。この定理を proper-class 版の分離定理として使用しない。

## 6. 何が新しく必要で、なぜ今回はここで止めるか

目標を実現するには、P1 の固定データに対する coreflection から、任意の下限 ρ の上のある κ と正規測度 W を得て

    {α<κ:α は可測}∈W

を強制する必要がある。単に高完備 ultrafilter を得ること、Fubini 積を作ること、外側の宇宙で測度を複数選ぶこと、j(U) を使うことではこの条件が出ない。

現在の Hom 計算や核の解析には、正規性と「可測基数集合への集中」を同じ抽出過程で保証する補題がない。そのような固定テストの実現は既存の一段階抽出の小修正ではなく、新しい還元を要する。

これは目標が偽だという証明でも、今後解けないという主張でもない。ただし今回ユーザーが指定した停止条件に従い、ここから別の符号化や新しい上界比較へは研究を広げない。

## 7. 停止時の記録

P1 の現時点の研究ノート上の境界（新規部分は独立監査前）:

    proper class of Π₂-strong cardinals ⇒ P1,
    proper class of almost strongly compact cardinals ⇒ P1,
    P1 ⇒ proper class of measurable cardinals.

P2(b) の以前の境界も変更しない:

    WVP ⇒ P2(b) ⇒ proper class of measurable cardinals.

今回試した追加下界:

    P1 ⇒ Mit2∞ : NOT_ESTABLISHED.

その否定・非含意:

    P1 ⇏ Mit2∞ : NOT_ESTABLISHED.

既存の bounds を確立済みの外部文献定理と同一視しない。今回それらの独立監査はしていない。

**今回の探索は停止。** 新規の数学探索をここから継続しない。研究ノートの保存と状態整理でこのセッションを閉じる。

## 8. 参考資料と実際の確認範囲

1. K. J. Williams, Math655 Lecture Notes, Part 1.1 Measurable cardinals, §6, Definition 67、Corollary 70、order1/order2 の説明、Lemma 71。
   https://juliakw.net/teaching/2019/math655/part1.1.pdf
   用途：Mitchell 順序の定義、正規測度の集中による特徴付け、rank0 の区別。

2. Erin Carmody, Force to change large cardinal strength, 2015, arXiv:1506.03432v2, Theorem 31（印刷ページ50、PDFページ58）。
   https://arxiv.org/abs/1506.03432
   https://arxiv.org/pdf/1506.03432
   用途：可測基数のクラスを保ちながら rank を指定 ordinal で切り詰める定理。P1やcompactnessの保存は引用しない。

3. Arthur W. Apter and Joel David Hamkins, Exactly Controlling the Non-Supercompact Strongly Compact Cardinals, arXiv:math/0301016, Proposition 6（PDFページ10）、Main Theorem 2。
   https://arxiv.org/abs/math/0301016
   https://arxiv.org/pdf/math/0301016
   用途：strong compactness と同じ基数での trivial Mitchell rank の両立。全可測基数のrankの制御とは区別。

4. Moti Gitik and Eyal Kaplan, On Restrictions of Ultrafilters from Generic Extensions to Ground Models, DOI 10.1017/jsl.2022.26, Theorem 4.17。
   https://doi.org/10.1017/jsl.2022.26
   用途：測度の個数と比較可能性の区別。出版社HTML本文で仮定と結論を確認した。

ローカル入力：
- No.1/codex_sset_handoff/RESEARCH_STATUS.md（第22段階まで）。
- No.1/codex_sset_handoff/investigations/measurable_thresholds_and_strong_compactness_2026-11-17.md（全内容を今回確認）。
- 会話で与えられている直前の No.2 の記録と、今回の停止条件。

PDFの本文抽出で該当定義・命題を確認。Web screenshot は Cache miss、コンテナからの取得はDNS障害で失敗したため、今回これらのページ画像の目視確認はできていない。画像・表の読解を証明の入力としていない。新しい独立査読や形式検証を行ったとは記録しない。
