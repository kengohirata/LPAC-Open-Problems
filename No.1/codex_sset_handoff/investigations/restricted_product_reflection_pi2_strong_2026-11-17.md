# 第20段階：P1 の Product Reflection 表示と Π₂-strong 基数による上界

2026-11-17。状態：PROOF_RECONSTRUCTED。直接導出を主担当が点検した段階。独立査読・形式検証・新規性確認は未実施。

完全な証明・符号化の詳細は [No.2 の主ノート](../../../No.2/p1_restricted_product_reflection_pi2_strong_2026-11-17.md)。本稿は No.1 側に要点と依存関係を反映する。

## 0. 新しい結論

\[
\boxed{\text{Π₂-strong 基数が真クラス存在}\Longrightarrow P1.}
\]

集合パラメータを許す boldface 原理について、Bagaria–Wilson の出版版 Theorem 5.13 (n=3) は

\[
\boldsymbol\Pi_2\text{-PRP}\iff\boldsymbol\Sigma_3\text{-WVP}
\iff\text{Π₂-strong 基数が真クラス存在}
\]

を与える。今回の追加の導出は \(\boldsymbol\Pi_2\text{-PRP}\Rightarrow P1\) である。Π₂-strong は同論文 Definition 5.1 の用語であり、strongly compact や almost strongly compact とは異なる。

修復列のグラフの定義可能性を算定する代わりに、A-equivalence な固定標的への射のクラスを用いる。これにより、Q(A) の trace、超限再帰、修復列の選択は新しい証明に不要になった。

## 1. 固定標的上の同値射の圏

小圏 C、K=Set^(C^op)、射の集合 Σ、A={}^⊥Σ、B∈K を固定する。

    E={p:X→Y : 全 Z∈A について K(Z,p) は全単射},
    E_B={p:X→B : p∈E} ⊆ K/B.

E_B は充満部分圏。id_B∈E_B。E は pullback・合成で閉じ、E_B の全小極限は slice で計算される。

後者の確認：Z∈A と a:Z→B は、図式の各 p_j:X_j→B に唯一に持ち上がる。一意性により持上げは整合するので、slice 極限への唯一の持上げがある。

## 2. 初対象から coreflection へ（ZFC）

r:R→B が E_B の初対象なら、R∈A が従う。

テスト s:U→V∈Σ と h:R→V を取る。s∈E なので pullback t:R×_V U→R は E に入る。r t は E_B の対象であり、初対象性により a:R→R×_V U がある。t a は E_B の r の自己射なので恒等射。これにより h を s に沿って持ち上げられる。

二つの持上げ g,h:R→U の等化子 e:D→R は、K(Z,s) の単射性を全 Z∈A に適用することで E に入る。r e∈E_B への初対象射から e は section を持つ。従って g=h。

よって R⊥Σ。r∈E_B は全 Z∈A に対する所要の Hom 全単射を既に与えるので、r は A-coreflection。

逆に、A-coreflection r:R→B は E_B の初対象である。R∈A と p∈E_B により K(R,p) が全単射だからである。

局所小完備圏に弱始集合があれば初対象がある。証明は、まずその集合の積 P を取り、End(P) の全自己射を id_P と同時等化する i:R→P を取る。P→R の射を使って R の全自己射が恒等と示し、任意の二射 R⇉X の等化子を使って一意性を得る。クラス個の等化子を取ってはいない。

従って次は同値：

- B の A-coreflection が存在。
- E_B に初対象がある。
- E_B に弱始集合がある。
- E_B のある非空の集合 S について、slice 積 ∏_B S から E_B の全対象へ射がある。

最後の条件を、全 C,Σ,B について要求する制限版 PRP_test は P1 と同値である。PRP_test は本研究内の略称で、既知の巨大基数原理の正式名称ではない。

## 3. E_B の Π₂ 定義

No.1 の既存ノート [定義可能性監査](../audits/set_theoretic_upper_bound.md) §2 により、A(Z) は Σ₂ で定義できる。具体的に、全 U_i 値候補射を集めた集合 L を存在量化し、全 V_i 値射の lift が L 内にあり一意であることを普遍量化で述べればよい：

    A(Z) ⇔ ∃L∀w θ(Z,L,w;C,Σ),   θ は有界。

Bij(Z,p)＝K(Z,p) が全単射、は存在性 ∀h∃g と普遍的な一意性から Π₂。

    p∈E_B ⇔ Map(p:X→B) ∧ ∀Z(¬A(Z) ∨ Bij(Z,p)).

¬A は Π₂、Bij も Π₂。従って全体も Π₂。ここは A の Π₂ 表示ではなく **Σ₂ 表示を antecedent に使う**ことが重要。

K/B は再び小圏上の presheaf 圏なので、固定された多ソート関係言語で符号化できる。空ソートや通常の関係積と slice 積の違いは No.2 主ノート §5 で処理した。各 fibre を unary predicate で指定し、関係積のその predicate に入る部分へ homomorphism を制限すれば slice の射を得る。

bold Π₂-PRP により、E_B の集合個の対象の積から全対象への射を得る。§2 により coreflection が存在する。任意の locally presentable category への移送は既存の full reflective presheaf 表示で行う。

## 4. ASC 側との合流

No.2 の二基数純性の証明により、ASC∞ の下では A が小さい A-対象の集合 G で directed-colimit 生成される。

このとき p が A-equivalence であることは、全 G∈G に対し K(G,p) が全単射であることと同値。従って E_B は slice 内の集合個の射

    (0→B) → (G,a),  G∈G, a:G→B

への通常の右 orthogonality class である。small-orthogonality の反射定理から E_B に初対象が得られる。

従って二つの経路は、同じ E_B の初対象／Product Reflection に合流する：

    WVP ⇒ bold Π₂-PRP ⇒ PRP_test ⇔ P1,
    ASC∞ ⇒ E_B の small-orthogonality 表示 ⇒ PRP_test ⇔ P1.

既存の下界を加えると

    proper class of Π₂-strong cardinals ⇒ P1 ⇒ proper class of measurables,
    ASC∞ ⇒ P1.

## 5. 何を解決していないか

全 Π₂-PRP と ASC∞ の比較、P1⇒全 Π₂-PRP、通常の strong 基数の真クラスだけで P1、既知の純粋な ultrafilter 原理と P1 の同値、最強の共通弱化という意味の meet は未確立。

PRP_test と P1 が同値であることは、共通原理が P1 の特徴付けであることを明示している。この制限を隠して新しい巨大基数原理を発見したとは言わない。一方、既知の PRP の Π₂ インスタンスと同定したことから、新しい有限階層の上界を実際に引き出せた。

outward compactness に直結させるには、外部モデルでも小部分理論が充足可能という仮定の検証が必要。small coorthogonality が一般に上向き絶対であるという期待は偽：Quiv の s:0→K_ω と ground model の K_(ω₁) について、ground では Hom(K_(ω₁),K_ω)=∅、ω₁を可算にcollapseしたextensionでは新しい単射が graph morphism を与える。従って同じ対象・同じ一本のmonoテストでも所属が変わる。この比較例は任意の closeness predicate を破る例という主張ではない。

## 6. 出典と監査

詳細な新しい証明： [No.2 の主ノート](../../../No.2/p1_restricted_product_reflection_pi2_strong_2026-11-17.md)。

文献：Bagaria–Wilson, The Weak Vopěnka Principle for Definable Classes of Structures, JSL 88 (2023), §2.1, Definition 3.1, Theorem 5.13 (n=3), DOI 10.1017/jsl.2022.42。ASC∞ の filter-extension 定式化は Brooke-Taylor–Rosický, Accessible Images Revisited, Definition 2.3 / Proposition 2.4。Outward compactness の外部充足性要件は Holy–Lücke–Müller, Definition 1.3 / 3.3。

監査の優先箇所：E_B の Π₂ 計算、slice 積の符号化、初対象からの存在と一意性の別々の証明、boldface の添字対応。新規適用は独立査読・形式検証前。
