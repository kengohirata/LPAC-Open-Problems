# ZFC 肯定方向：pure 部分対象による構成の到達点と障害

2026年11月16日。`INTERNAL_PROOF_CHECKED`。通常の集合論 ZFC と ordinary Hom を使う。既存の証明済み結果は前提として採用し、再監査しない。本稿の証明は内部点検までで、形式検証・外部査読・新規性確認はない。一般の P の証明・反例ではない。

## 1. Compact Hausdorff 条件を置き換える十分条件

K = Set^(C^op)、C は小圏、S = {s_i:U_i→V_i} は射の集合とする。λ は無限正則基数。λ-pure inclusion は、λ 個未満の変数・方程式と λ 個未満の始域のパラメータを使う正の原始的な方程式系について、終域での可解性が始域へ反映する包含とする。これは presheaf の多ソート unary algebra 表示における λ-purity である。

対象 D が λ-pure injective とは、λ-pure inclusion Y→X に沿ってすべての射 Y→D が X→D に延長できることをいう。

**定理 1.** すべての i について V_i と W_i = U_i×_(V_i)U_i が λ-pure injective なら、A = {}^⊥S は λ-pure 部分対象に閉じ、accessible、従って locally presentable かつ coreflective である。

**証明（閉性）。** X∈A と λ-pure inclusion Y⊆X を取る。h:Y→V_i を X→V_i に延長し、X∈A による一意 lift を Y に制限すれば存在性を得る。g_0,g_1:Y→U_i が s_i g_0=s_i g_1 を満たすなら、(g_0,g_1):Y→W_i を X→W_i に延長する。二射影との合成は s_i 後に一致するので X∈A によって等しく、Y に制限すれば g_0=g_1。∎

以下に accessibility のサイズ部分を明記する。κ=max(ℵ₀,|Mor C|) とし、μ≥max(κ,λ) かつ μ^(<λ)=μ となる基数を選ぶ。このような μ は、ν≥max(κ,λ) に対して μ=2^ν とすれば取れる。X の大きさ ≤μ の任意の元集合 Z は、大きさ ≤μ の λ-pure subpresheaf Y⊆X に含まれる。実際、長さ λ の連続増大列を作り、各後続段でそれまでの元をパラメータに持つ λ 個未満の方程式系のうち X で解けるものすべての証人を加え、構造演算で閉じる。各段の系の総数は μ^(<λ)=μ 以下。λ の正則性により、最終段の λ 個未満のパラメータはある段に揃うので、その系の解は次段に加わっている。

従って X∈A の大きさ ≤μ の部分集合は、大きさ ≤μ の A-部分対象に入る。これらの A-部分対象の poset は μ^+-directed で X を覆う。大きさ ≤μ の presheaf は μ^+-presentable。A は小余極限に閉じ、その包含は余極限を保存するので、これらは A 内でも μ^+-presentable である。同型類は集合個だから A は accessible。小余極限も持つので locally presentable であり、余極限保存包含 A→K は右随伴を持つ。∎

この定理は `audits/compactness_and_finite_tests.md` の位相的証明を、実際に必要な延長性へ一般化したもの。U_i 自身の pure injectivity は仮定していない。一意性のためには二つの射の個別延長ではなく W_i への同時延長が必要である。

**境界点検。** 空テスト集合なら K 全体。空 sort も purity の無パラメータ存在条件に含める。λ=ℵ₀ なら通常の pure-injective 版。compact Hausdorff 構造がある V_i,W_i は既存補題によりこの通常版の仮定を満たす。

## 2. 一般のテストに pure 閉性を期待する案は強すぎる

既存のリスト彩色用 presheaf 圏 K=Quiv/Λ と固定対象 D を用いる。Λ の頂点は P(ω)、任意の順序対に辺が一本。D の頂点は (L,n), n∈L、辺は異なる色を持つ頂点間に一本。K(X,D) はリスト彩色の集合である。

固定した一本の mono s:0→D に対して

    N = {}^⊥{0→D} = {0} ∪ {X : K(X,D)=∅}.

N の coreflector は、B が彩色不能なら B、彩色可能なら 0 であり、ZFC で存在する（既存ノート `list_colouring_independence_2026-11-15.md`, §3）。従って以下の障害は coreflectivity の障害ではない。

**定理 2.** N がある無限正則 λ について λ-pure 部分対象に閉じるなら、ω₁-strongly compact cardinal が存在する。

**証明。** §1 の μ を、K を表す小 presheaf signature に対して選ぶ。任意の非空なリスト彩色不能グラフ X を K の対象と見なす。頂点を一つ含む大きさ ≤μ の λ-pure subpresheaf Y⊆X を取る。仮定から Y∈N、しかも非空なので Y は彩色不能。Y の頂点を持つ X の誘導部分グラフも彩色不能であり、その頂点数は ≤μ。従って、任意の彩色不能グラフには頂点数 <μ^+ の彩色不能部分グラフがある。これは μ^+-compactness for ω-list-colouring。Feller–Holy, Theorem 7 により μ^+ は ω₁-strongly compact。∎

**帰結。** ω₁-strongly compact cardinal が存在しないモデルでは、この一つの固定したテスト 0→D に対し、どの無限正則 λ についても、X∈N と λ-pure inclusion Y⊆X で Y∉N となる例が存在する。つまり **一意持上げという条件を保ったまま、任意に強い purity による閉性が失敗し得る**。

この結果は単なる「非 accessibility の可能性」より具体的に、pure-subobject 降下による一般証明が詰まる箇所を示す。なお s は mono なので一意性は自動であり、ここでは存在性の降下が失敗する。一般の一意持上げ条件から存在性の局所化まで導くことはできない。

**定理 3.** 同じ巨大基数非存在の仮定の下では、D はどの無限正則 λ に対しても λ-pure injective でない。

**証明。** 定理 2 の帰結の Y⊆X を取る。Y∉N は K(Y,D)≠∅ を意味するが、X∈N かつ非空なので K(X,D)=∅。Y→D は延長できない。∎

従って、任意のテスト対象に対し十分大きい λ を選んで定理 1 を使う、という ZFC 一般証明もこの例で阻まれる。P の肯定証明は、accessible にならないクラスをも扱える、標的 B ごとの解集合条件などを使う必要がある。

**Nonaccessibility の直接確認。** 同じ巨大基数非存在の仮定の下で N が accessible だとすると、小さい生成対象の集合があり、それらの carrier サイズはある μ で抑えられる。非空 X∈N の filtered-colimit 表示には非空な生成対象から X への射がある。その像は N の商閉性によって彩色不能であり、サイズは ≤μ。従って全彩色不能グラフに一様に小さい彩色不能部分グラフがあり、再びリスト彩色の compactness と巨大基数を得て矛盾する。ここでは accessibility から pure 部分対象閉性を直接推論していない。

## 3. 最近の pure mono 論文は何を供給するか

Cox–Feigert–Kamsma–Mazari-Armida–Rosický, *Cofibrant generation of pure monomorphisms in presheaf categories*, arXiv:2506.20278v2 の Theorem 1.2 は、Set^C の pure monomorphism が cofibrantly generated であることと、C が locally linearly preordered であることを同値にする。Corollary 1.3 はこの条件下で enough pure injectives を与える。

これは任意の D が pure injective、あるいはある λ で λ-pure injective であるという主張ではない。D を pure-injective 対象 E に埋め込んでも、Hom(X,D) を Hom(X,E) で置き換えた coorthogonality 条件は一般に同じにならない。従って、今回の一般のテスト集合に対する定理 1 の仮定を供給するものではない。

また「すべての presheaf 圏で pure monos は cofibrantly generated」とする案は論文の分類定理自体に反する。例えば multiplicative monoid of natural numbers の acts が反例として挙げられる。

## 4. 次に必要なもの

一般の P を ZFC で証明する際に、全 coorthogonality class の accessibility、全テスト対象のある λ における pure injectivity、あるいは全 coorthogonality class の λ-pure-subobject 閉性を補題にすることはできない。これらは P より強く、上の ZFC-coreflective な例ですでに巨大基数を要求する。

残る肯定案は、各固定標的 B について A↓B の解集合を構成することである。この構成は、A 自体の小さい生成族を要求しないものでなければならない。本稿はその解集合を構成していない。

## Sources checked on 2026-11-16

- S. Cox et al., Theorems 1.2 and 5.1, Corollary 1.3: https://arxiv.org/html/2506.20278v2
- R. Feller and P. Holy, Definitions 5–6 and Theorem 7: https://arxiv.org/html/2608.20883v1
- S. Cox and J. Rosický, *Fibrantly generated weak factorization systems*, Theorem 3.1, Example 3.2, Lemma 3.3: https://ems.press/content/serial-article-files/48316 . This paper concerns weak lifting and is background only; no negative conclusion about P is attributed to it.
