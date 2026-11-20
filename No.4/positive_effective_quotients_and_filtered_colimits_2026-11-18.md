# Problem 4：有効商を使う肯定証明と、その仮定の限界

2026-11-18。

**状態：PROOF_RECONSTRUCTED。追加の quotient 閉性の下での肯定証明、およびその閉性が P4 の仮定からは従わない具体例。一般 P4 は未解決。独立査読・形式検証・新規性確認は未実施。**

## 1. 追加条件

P=Set^(D^op)、A⊆P は full replete、全小極限と λ-directed unions に閉じるとする。

次の追加条件を置く。

    (AQ) B∈A および P 内の同値関係 R↪B×B について、
         R∈A なら P で計算した有効商 B/R も A に属する。

R の対象としての A-membership と、B/R の **ambient** 商であることが重要。A 内で商が存在するだけでは (AQ) とは言えない。

**定理 1.1。** (AQ) の下で A は全ての λ-filtered colimits に閉じる。従って A は反射的かつ局所可呈示。

## 2. 証明：eventual kernel を union として計算する

小さい λ-filtered diagram F:I→A と、その P 内の colimit

    c_i:A_i→Z

を取る。connecting maps は mono と仮定しない。

各 i∈I について、i から出る全ての射 u:i→j の kernel pairs

    K_u = A_i×_(A_j) A_i ↪ A_i×A_i

を考える。A は全小極限閉なので K_u∈A。

これらは inclusion に関して λ-directed な集合をなす。実際、i から出る <λ 個の射は、λ-filteredness により一つの共通の合成先に可換に写り、対応する kernel が元の kernel 全てを含む。

従って

    R_i = ⋃_{u:i→j} K_u

は A に属する。filtered colimits of sets における等式の判定から、これは c_i の P-kernel pair に一致する：同じ sort の二元は、colimit で等しいことと、どこか一つの後段で等しいことが同値。

(AQ) により

    Q_i = A_i/R_i ∈ A.

この Q_i は c_i の ambient image と同型なので、Q_i↪Z と見ることができる。

I の λ-filteredness により、これらの images は Sub_P(Z) の λ-directed family をなし、Z 全体を覆う。λ-directed-union 閉性から Z∈A。以上で全 λ-filtered-colimit 閉性を得た。

全小極限閉性と十分大きい filtered-colimit 閉性に対する Reflection Theorem により A は反射的。包含は λ-filtered colimits を保存するため、representables の反射は A の λ-presentable strong generator をなす。従って A は局所可呈示。必要なら最初に λ を大きい非可算正則基数に取り直してよい。□

**証明の要点。** union 閉性は、元の対象の像ではなく、まず固定 A_i×A_i 内の kernel relations に適用する。その後で (AQ) を使って像を A-object に変える。この最後の移送を省略してはいけない。

## 3. P4 の仮定から (AQ) は従わない

具体例を、simplicial sets 内の category nerves で与える。

P=sSet=Set^(Δ^op)、A を小圏の nerve の replete full image とする。

- N:Cat→sSet は fully faithful。
- N(C)_n=Cat([n],C) なので N は全小極限を保存する。
- 有限列 [n] からの functor は有限個の対象と射のデータで決まる。filtered colimits of categories ではこのデータと有限個の等式はある段階に現れるため、N は filtered colimits を保存する。

従って A は全小極限と全 filtered colimits、特に全 directed unions に閉じる。通常の categorification によって反射的でもある。

### 3.1 二つの辺を合成可能にする functor

C=[1]⊔[1] とし、二つの非恒等射を

    a0 --u--> a1,       b1 --v--> b2

と書く。D=[2] とし、F:C→D を

    a0↦0, a1↦1, b1↦1, b2↦2,
    u↦(0→1), v↦(1→2)

で定める。

I=im_sSet(NF)⊆ND を pointwise image とする。I は三つの頂点 0,1,2 と二つの辺 0→1、1→2 を含むが、辺 0→2 を含まない。

したがって I は category nerve ではない。実際、二つの合成可能な辺 (0→1,1→2) は存在するのに、それらの合成を表す 2-simplex がない。nerve の Segal map

    I_2 → I_1 ×_(I_0) I_1

は全射でない。

一方、NF の kernel pair は

    R = NC×_(ND) NC ≅ N(C×_D C)

であり、R∈A。P で計算した商 NC/R は I と同型なので A に属さない。

従ってこの A は P4 の全仮定を満たし、さらに局所可呈示かつ反射的なのに (AQ) を満たさない。

同時に、A の射 NF の ambient image が A に属さないので、別ノートの (IC) も P4 の仮定からは従わない。

### 3.2 Eventual kernel に限定しても自動ではない

上の例を eventually constant な filtered diagram

    NC --NF--> ND --id--> ND --id--> ···

の最初の stage に適用する。この colimit は ND∈A。しかし最初の stage の eventual kernel R の pointwise quotient は I∉A。

従って「eventual kernel なら、その pointwise quotient は自動的に A に入る」という修正でもギャップは埋まらない。全体の colimit が A に入る場合ですら、各 stage の像が A に入る必要はない。

## 4. この route で残ったこと

定理 1.1 は (AQ) の下での ZFC の肯定結果。一方、§3 は (AQ) を一般の P4 の補題として証明する方針を退ける。

今後この route を使うなら、個々の ambient images を A に入れることを要求せず、最終 colimit 自体を A に戻す方法が必要。これは全 filtered-colimit 閉性という、反射性より強い結論を目指す方法であることにも注意する。

反射性だけの正確な目標は [普遍近似の停止条件](positive_universal_approximants_and_stabilization_2026-11-18.md)。商のサイズを別に抑えられる場合は [small reflections と strong quotients](positive_small_reflections_and_strong_quotients_2026-11-18.md) の定理 4.1 が適用できる。

## 5. 標準入力

Adámek–Rosický, *On reflective subcategories of locally presentable categories*, TAC 30 (2015), 1306–1318, Introduction の Reflection Theorem。

https://arxiv.org/pdf/1504.03886

本文の filtered-colimit 閉性の直接証明、および nerves の反例計算は本ノートで記したもの。一般の directed unions と filtered colimits を入れ替えることはせず、その移送に (AQ) を明示的に使った。
