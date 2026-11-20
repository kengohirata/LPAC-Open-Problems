# P1 の共通構造：テストに制限した Product Reflection と Π₂-strong 上界

2026-11-17。状態：PROOF_RECONSTRUCTED。今回の直接導出を主担当が点検した段階。独立査読・形式検証・新規性確認は未実施。既知の Product Reflection Principle (PRP) とその強度の定理を、以下の新しい適用・同値化と区別する。

## 0. 到達点

P1 は「任意の locally presentable category の集合個の射による ordinary coorthogonality class は coreflective」。ASC∞ は almost strongly compact 基数の真クラス存在。

今回、次を導いた。

(1) 固定した small coorthogonality class A と標的 B に対し、A-equivalence な射 p:X→B の圏 E_B を考えると、E_B は slice の小極限に閉じた Π₂-定義可能な充満部分圏である。

(2) E_B に対する PRP（集合個の対象の slice 積から E_B の全対象への射が存在すること）は、B の A-coreflection の存在と同値。

(3) この限定された PRP を全 presheaf/test/target データについて要求する原理 PRP_test は P1 と同値。PRP_test は本ノート内の略称であり、既知の正式名称を主張しない。

(4) Bagaria–Wilson の既知の強度計算と (1)(2) により

    Π₂-strong 基数が真クラス存在 ⇒ P1.

より精確には、集合パラメータを許す boldface 原理について

    bold Π₂-PRP ⇔ bold Σ₃-WVP
      ⇔ Π₂-strong 基数が真クラス存在,

であり、そのいずれからも P1 が従う。strongly compact ではなく、同論文 Definition 5.1 の Π₂-strong である。

(5) ASC∞ 側では、従来の pure-injectivity 議論から A の小さい生成族を得て、同じ E_B を small-orthogonality class として反射できる。従って二つの十分条件は、E_B の初対象／制限版 Product Reflection という一つの構造で合流する。

(6) 全 Π₂-PRP が ASC∞ から従うことや、P1 が全 Π₂-PRP を含意することは証明していない。従って新しい上界そのものを二原理の最適な meet と呼ばない。純粋な ultrafilter 原理による必要十分な特徴付けも未完成。

(7) outward compactness を素朴に適用するための「small coorthogonality が外部モデルで絶対的」という補題は偽。最後に固定 mono テストに対する forcing 反例を示す。

本証明は正規化修復列の定義可能性を追跡しない。Q(A) の trace、超限再帰、proper class の選択、群の増大構成も不要である。

## 1. 設定と同値射のクラス

C を小圏、K=Set^(C^op)、Σ を K の射の集合とし、

    A = {}^⊥Σ = {Z : K(Z,s) は全単射、すべての s∈Σ}

とする。B∈K を固定する。

射 p:X→Y が A-equivalence であるとは、全 Z∈A に対し K(Z,p) が全単射であること。この射の全体を E=A^⊥ と書く。

    E_B = {p:X→B : p∈E} ⊆ K/B

を充満部分圏として取る。射は B 上の可換三角である。id_B∈E_B なので E_B は空でない。

E は合成、pullback、小極限（射の圏での極限）に閉じる。これは K(Z,-) の極限保存から従う。

### 補題1：E_B の全小極限は slice で計算できる

E_B 内の小図式 (p_j:X_j→B) と Z∈A、a:Z→B を取る。各 j に唯一の持上げ a_j:Z→X_j がある。図式の各射に沿う合成は B 上で同じ a を与えるので、一意性からこれらは整合する。従って slice の極限へ唯一の射を得る。

空図式の極限は id_B であり、これも E_B に属する。従って E_B は完備で、包含 E_B→K/B は全小極限を作る。□

## 2. 初対象補題を省略せずに確認する

### 補題2

局所小な完備圏 D が弱始対象 P を持てば、初対象を持つ。

証明。End_D(P) は集合なので、id_P と全自己射を同時に等化する小極限

    i:R→P,
    u i=i  (u∈End(P))

を取る。P が弱始なので f:P→R が存在する。u=i f に対する等式 i f i=i と i の mono 性から f i=id_R。

任意の v:R→R に対し i v f は P の自己射なので i v f i=i。f i=id_R から i v=i、従って v=id_R。

R は弱始でもある。任意の D∈D への P→D と i を合成すればよい。二射 g,h:R→D の等化子 j:E→R を取り、弱始性で k:R→E を取ると、j k は R の自己射なので恒等射。ゆえに g=g j k=h j k=h。従って R は初対象。□

弱始集合がある場合は、その積 P が弱始対象になる。非空性は明記しておく。

## 3. 核心：E_B の初対象は A-coreflection を与える

### 補題3

r:R→B が E_B の初対象なら、R∈A であり、r は B の A-coreflection である。

証明。任意のテスト s:U→V∈Σ を取る。定義から s∈E である。

存在性：h:R→V に対し pullback

    P=R×_V U,
    t:P→R,
    k:P→U

を取る。s∈E と pullback 閉性により t∈E、従って r t:P→B は E_B の対象。初対象性から a:R→P があり r t a=r。t a は E_B における r の自己射なので t a=id_R。従って s k a=h。

一意性：g,h:R→U、s g=s h とする。等化子 e:D→R を取る。Z∈A と任意の z:Z→R に対し、K(Z,s) の単射性から g z=h z。従って z は e を一意に経由し、e∈E。r e:D→B∈E_B なので初対象性から b:R→D、r e b=r を得る。再び e b=id_R となり、g=g e b=h e b=h。

よって K(R,s) は全単射。s は任意なので R∈A。r∈E_B 自体が全 Z∈A に対する Hom(Z,r) の全単射性を与えるため、r は coreflection。□

この証明は修復関手 TΣ を作らない。持上げの存在を pullback で、一意性を equalizer で処理する。

逆向きも成立する。r:R→B が A-coreflection なら R∈A、r∈E_B。任意の p:X→B∈E_B に対して K(R,p) は全単射なので、r の p に沿う持上げは唯一。すなわち r は E_B の初対象。

### 定理4（ZFC、固定データに関する同値）

次は同値。

(a) B の A-coreflection が存在。
(b) E_B が初対象を持つ。
(c) E_B が弱始集合を持つ。
(d) 非空の集合 S⊆Ob(E_B) があり、slice 積 P=∏_B S から E_B の任意の対象への射がある。

(b)⇒(d) は初対象一つを S とすればよい。(d)⇒(c) は P が E_B に属することによる。(c)⇒(b) は補題2。(a)⇔(b) は補題3とその逆。□

## 4. Lévy 複雑性：E_B は Π₂

パラメータは C、Σ、B の集合コード。presheaf と自然変換をソート集合、単項操作、関数グラフで符号化する。対象・射としての妥当性と射の合成の検査は Δ₀ で書ける（同等の標準的 Δ₁ コードを用いても以下のレベルは変わらない）。

### 4.1 A(Z) の Σ₂ 表示

Σ={s_i:U_i→V_i : i∈I} とする。L を添字付き U_i 値写像の集合とし、以下を要求する。

- L の各元 (i,g) は Z→U_i という自然変換を表す。
- 全候補 h:Z→V_i に対し、s_i g=h となる (i,g)∈L がある。
- g,g':Z→U_i で s_i g=s_i g' なら g=g'。

持上げ g の量化は L に有界化される。従って全体は

    A(Z) ⇔ ∃L ∀w θ(Z,L,w;C,Σ)

と書け、θ は有界式。逆向きの証人として L=∐_i K(Z,U_i) を取れる。Σ が集合であることが本質。

直接の ∀h∃g 表示もあるので A は Δ₂ であるが、以下で必要なのは Σ₂ 側。

### 4.2 Hom(Z,p) が全単射であることの Π₂ 表示

p:X→B に対し、存在性は

    ∀h [Map(Z,B,h) ⇒ ∃g (Map(Z,X,g) ∧ p g=h)]

であり Π₂。一意性は二候補 g,g' に対する普遍条件で Π₁。従って Bij(Z,p) は Π₂。

### 4.3 相対同値射のクラス

    p∈E_B ⇔ [p:X→B は射] ∧ ∀Z (A(Z)⇒Bij(Z,p)).

A が Σ₂ なので ¬A は Π₂。Bij も Π₂ なので、括弧内は Π₂ の論理和であり、Π₂ に書き直せる。外側の ∀Z を加えても Π₂。

明示的には A(Z)=∃L∀wθ、Bij(Z,p)=∀h∃gψ と書くと、含意は

    ∀L∀h [ (∃w ¬θ) ∨ (∃g ψ) ]

となるので、全体を ∀Z∀L∀h∃v χ の形にまとめられる。候補の妥当性と一意性もこの形に吸収する。

**補題5。** E_B は集合パラメータ付き Π₂-定義可能クラスである。□

この計算は Q(A)、最大 trace、再帰列のグラフの定義可能性に依存しない。Σ₂-WVP（通常の strong 基数の真クラス）だけで十分と結論するには、さらに一段階を下げる論証が必要。ここでは Π₁ 表示や Σ₂ 表示は得ていない。

## 5. 既知の Product Reflection Principle の適用

Bagaria–Wilson, JSL 88 (2023), Definition 3.1 の PRP は、同じ関係言語の構造のクラス C に対し、非空の集合 S⊆C があり、∏S から全 X∈C へ homomorphism が存在すること。

同論文 §2.1 と Definition 3.1 直後により、集合パラメータを許す boldface 原理では、graphs を任意の固定された集合サイズの多ソート関係言語に取り替えてよい。

K/B≃Set^((∫_C B)^op) は再び小圏上の presheaf 圏であり、多ソートの単項演算をそのグラフ関係で表せる。E_B はこの固定言語の Π₂ クラスに対応する。PRP を適用して得た積からの homomorphism は B 上の自然変換を与える。

### 空ソート・通常の積と slice 積の技術的処理

空ソートの規約に依存したくなければ、次の一ソートの関係符号化を使える。

- p:X→B の符号化の台を、一つの dummy 点とタグ付き全ソートの元の非交和にする。
- 各 (c,b), b∈B(c) に unary predicate P_(c,b) を置き、p_c の fibre を指定する。
- 各 C の射に binary graph relation を置き、構造写像を表す。
- dummy 点を識別する unary predicate を置く。台は常に非空。

妥当な符号化の条件は、各実元が唯一の fibre predicate に入り、graph relations が全域一価で presheaf 方程式を満たすこと。これは与えられた台と言語上の有界検査である。正準的な decoding は Δ₁ なので E_B の Π₂ 表示を維持できる。

符号化の集合 S の通常の関係積には異なる fibre を混ぜた tuple も入る。しかし各 P_(c,b) の解釈は「全座標が同じ fibre (c,b) にある tuple」なので、その部分を取り出すと元の K/B の積になる。PRP で得た homomorphism をこれらの fibre に制限すれば、B 上の自然変換 P→X が得られる。full embedding が積を保存すると無条件に仮定してはいない。

このように bold Π₂-PRP から定理4(d) が得られ、B の A-coreflection が存在する。

### 定理6（今回の新しい適用）

    bold Π₂-PRP ⇒ P1.

presheaf 圏での結論は上記。一般の locally presentable category D には full reflective presentation L:K⇄D:J を使う。D のテスト Σ に対して、K のクラス C={}^⊥JΣ は L^(-1)({}^⊥Σ)。JB の C-coreflection の domain は反射の単位を介して J の像と同型になり、D の coreflection が得られる。この移送は No.1 の既存の unit の両側逆の証明と同じ。

Bagaria–Wilson の出版版 Theorem 5.13 を n=3 で使うと

    bold Π₂-PRP ⇔ bold Σ₃-WVP
      ⇔ Π₂-strong 基数が真クラス存在。

従って

    Π₂-strong 基数が真クラス存在 ⇒ P1.

パラメータなしの原理と boldface 原理を混同しない。ここでは C、Σ、B の任意の集合パラメータが必要。

Π₂-strong は同論文 Definition 5.1 の用語であり、2-strongly compact、almost strongly compact、通常の強コンパクト基数ではない。

## 6. 両側の証明が共有する制限版 PRP

PRP_test を、全ての集合コード C、Σ、B について §1 の E_B が定理4(d) を満たす、という原理と定める。

    PRP_test ⇔ P1.

この同値は ZFC の定理であり、独立の巨大基数仮定を使わない。

WVP 側は

    WVP ⇒ bold Π₂-PRP ⇒ PRP_test

と進む。今回、全 WVP の代わりに一つの有限階層の原理で足りることが分かった。

ASC∞ 側を、P1 を黒箱にせず同じ E_B の構造へ接続するには次のようにする。

1. No.2 の二基数 pure-injectivity の証明により、A はある κ に対して小さい A-対象の directed colimits で生成される。小さい代表の集合を G とする。
2. p:X→B が A-equivalence であることは、全 G∈G について K(G,p) が全単射であることと同値。Hom(-,X)、Hom(-,B) が colimit を limit に送ることによる。
3. slice K/B で、全 G∈G と a:G→B に対する射 (0→B)→(G,a) の集合を取る。E_B はこれらに対する通常の右 orthogonality class である。
4. locally presentable な slice の small-orthogonality class は ZFC で reflective。初対象 (0→B) の反射が E_B の初対象を与える。
5. その一対象からなる集合が PRP_test の証人となる。

従って両側は E_B の初対象、あるいはその一つ前の「集合個の積から全対象へ射がある」条件で合流する。

これは名前を RCP から変更しただけではない。既存の PRP の明示的な Π₂ インスタンスとして特定したことで、有限階層の巨大基数上界（定理6）を引き出せた。ただし、P1 と同値な特殊な原理であることは明記し、独立した自然な巨大基数名称による最適 meet を得たとは主張しない。

## 7. なぜ通常の fine ultrafilter 延長をそのまま meet にできないか

前ノートの ASC∞ は

    ∀θ ∃κ≥θ：任意の κ-complete filter が θ-complete ultrafilter に延長される

という原理と同値である。Brooke-Taylor–Rosický, Accessible Images Revisited, Definition 2.3 / Proposition 2.4 による。

従って、停止を証明するために全ての制約系でこの標準の filter extension を要求すれば、ASC∞ 自体を再要求することになる。WVP⇒ASC∞ が未確立のまま、それを両側に共通の弱い仮定として採用することはできない。

今回取り出せた共通性は、任意の fine ultrafilter ではなく、特別な Π₂ クラス E_B に関する product-reflection witness の存在である。任意の P→X という自然変換が、超フィルター評価に必要な全自己写像との可換性や Boolean 演算の保存を備えるわけではない。そこから ultrafilter を抽出する追加符号化は未構成。

## 8. Outward compactness の適用に残る条件と、素朴な絶対性の反例

Holy–Lücke–Müller の outward compactness は、単に V において全ての小さい制約集合が解けるという仮定ではない。指定された outer models でも小部分理論の充足可能性が成り立つことを要求する。出版前著者版の Definition 1.3、Definition 3.3 を確認した。

従って、No.1 の purity から得る V 内の局所解を、そのまま outward compactness の仮定に用いることはできない。

### 補題7：small coorthogonality 所属は outer model に対し一般には上向き絶対でない

Quiv を quiver の presheaf 圏とする。D を頂点集合 ω のループなし完全有向グラフ（異なる二頂点の順序対に辺一つ）、s:0→D とする。X を頂点集合 ω₁^V の同じ型の完全有向グラフとする。

V では X→D の quiver morphism は存在しない。頂点写像が単射でなければ、異なる二頂点間の辺が D のループに写ってしまうためである。また X→0 も存在しない。従って

    V ⊨ X∈{}^⊥{s}.

ω₁^V を可算に collapse する forcing extension V[G] では、新しい単射 ω₁^V→ω が存在する。それは X→D の quiver morphism を与える。一方 X→0 は依然存在しない。よって

    V[G] ⊨ X∉{}^⊥{s}.

圏の小さい添字、一本の mono テスト s、X,D の関係集合を全て同じ ground-model パラメータとして保持しても、Hom に新しい写像が加わるため所属が変わる。□

これは outward compactness による解法全体を否定しない。またこの forcing が任意の closeness predicate Ψ の許す outer model だとは主張しない。否定したのは「ordinary coorthogonality は全 outer models で自動的に正しい」という素朴な補題。適用を進めるには、制約系と Ψ の選び方によって必要な外部充足性を別に証明する必要がある。

## 9. 正確な含意図と残された問題

今回の上界を入れると、研究で採用済みの下界と合わせて

    WVP ⇒ bold Σ₃-WVP ⇔ proper class of Π₂-strong cardinals
        ⇒ PRP_test ⇔ P1 ⇒ proper class of measurable cardinals,

    ASC∞ ⇒ PRP_test ⇔ P1.

ここで P1⇒可測基数の真クラスは No.1 の既存の反例証明を入力とする。今回それを再証明していない。

未証明：

- ASC∞⇒全 bold Π₂-PRP、またはその逆。
- P1⇒全 bold Π₂-PRP。
- 通常の strong 基数の真クラス（bold Σ₂-WVP）だけで P1。
- P1 と同値な、圏論的テストを使わない既知の ultrafilter／extender 原理。
- PRP_test が WVP と ASC∞ の論理的に最強の共通弱化であること。
- outward compactness に対する必要な外部充足性。

次の具体的な目標は、任意の Π₂ クラスを E_B の形に実現することではなく、E_B に特有の閉性・Hom 全単射性から得られる product-reflection witness を、必要最小限の ultrafilter 条件として符号化すること。任意の Π₂-PRP への逆還元は、ASC∞ から全 Π₂-PRP を導くことにもなるため、集合論的な強度を確認せず進めてはいけない。

## 10. 依存関係と文献

採用済みのローカル入力：

- ../No.1/codex_sset_handoff/audits/set_theoretic_upper_bound.md §2：small coorthogonality の Δ₂ 表示。
- p1_p2_measurable_wvp_almost_compact_2026-11-17.md §3：ASC∞ による小さい pure subobjects の生成。
- ../No.1/codex_sset_handoff/investigations/positive_tower_2026-11-16.md：比較対象となる以前の停止原理。本稿の補題1–6は同ノートの超限列を使わない。

外部一次資料：

1. Joan Bagaria and Trevor M. Wilson, The Weak Vopěnka Principle for Definable Classes of Structures, Journal of Symbolic Logic 88 (2023), 145–168. 出版版 §2.1、Definition 3.1、Theorem 5.13 (n=3)。
   https://doi.org/10.1017/jsl.2022.42
   https://diposit.ub.edu/server/api/core/bitstreams/5ac83f7a-9752-4a28-bf65-31c2d878692a/content
   arXiv v1 では章・定理番号が異なるため、5.13 は出版版を指す。

2. Andrew Brooke-Taylor and Jiří Rosický, Accessible Images Revisited, Proceedings AMS 145 (2017), 1317–1327. Definition 2.3、Proposition 2.4。
   https://arxiv.org/pdf/1506.01986

3. Peter Holy, Philipp Lücke, Sandra Müller, Outward compactness, 著者公開版。Definition 1.3、Definition 3.3。利用は外部モデルでの局所充足性の要件の確認に限定する。
   https://www.math.uni-hamburg.de/home/luecke/publications/outward.pdf

4. Bagaria–Casacuberta–Mathias–Rosický, Definable orthogonality classes in accessible categories are small。通常の small-orthogonality class の反射性と背景。
   https://arxiv.org/abs/1101.2792

今回 Web の本文抽出で定義・定理を確認した。PDF screenshot はサービスの Cache miss で失敗し、画像による組版確認はできていない。本文から読んだ boldface／パラメータの扱いは出版版の定理直前の説明と照合した。

## 11. 監査箇所

最優先：

(A) E_B の Π₂ 表示：A の Σ₂ 表示を antecedent に使う点。
(B) 初対象 r:R→B から R∈A を示す pullback と equalizer の二段階。
(C) PRP の通常の関係積から slice 積への制限、空ソートの扱い。
(D) 完備＋弱始集合から初対象を構成する際、自己射集合だけで十分な点。
(E) Bagaria–Wilson の bold Π₂-PRP と proper class of Π₂-strong の添字対応（n=3）。

本文の新しい結論は PROOF_RECONSTRUCTED。独立検証済みとは記録しない。
