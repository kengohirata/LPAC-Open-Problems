# Set の反対圏を使う経路の到達点

2026年11月16日。P は、局所可呈示圏の集合個の射への ordinary coorthogonality class が coreflective か、という命題である。N を「非可算の可測基数が存在しない」とする。

**結論。** N の下での Set^op の充満埋め込みは使える。しかし、裸の集合の像を巨大な候補対象として使う方法と、像の射だけをテストにする方法は、それぞれ以下の ZFC の除外定理に当たる。図式を加えた場合はなお候補が残るが、小さいテストと解集合条件の失敗を同時に実現していない。一般の P の肯定・反例・独立性はいずれも未証明。

以下の直接証明は主担当と別担当が照合した `INTERNAL_PROOF_CHECKED`。外部査読・形式検証・文献上の新規性を意味しない。既存の受け入れ済み証明は再監査していない。

## 1 埋め込みと向き

Ω を可算無限集合、M=End_Set(Ω)、D=M-Set=[M,Set] とする。M 自体の濃度は可算とは限らない。

\[
F:\mathbf{Set}^{op}\longrightarrow\mathcal D,
\qquad F(X)=\Omega^X,
\qquad u\cdot h=u\circ h.
\]

集合写像 f:Y→X は前合成 F(f):F(X)→F(Y) を与える。Isbell 2.5 の codensity により、ZFC+N では F が充満忠実である。Shulman p.20 に同じ M-Set への定式化がある。

H(A)=Hom_M(A,Ω) を Set^op の対象とみなせば

\[
\operatorname{Hom}_M(A,F(X))
\cong \operatorname{Set}(X,H(A))
=\operatorname{Set}^{op}(H(A),X),
\]

したがって H⊣F。この随伴同型自体は ZFC で成り立つ。F が充満忠実なら像は reflective である。

F は ambient coproduct を保存しない。Set^op での 1⊔1=1 に対し、比較射 Ω⊔Ω→Ω は同型でない。像自体を colimit-closed class として扱わない。

一次資料（2026年11月16日本文再確認）：

- Isbell, *Adequate subcategories*, 2.5, pp.549–550：[本文](https://conceptualmathematics.wordpress.com/wp-content/uploads/2013/05/adequatesubcategories.pdf)。
- Shulman, *Set theory for category theory*, p.20：[本文](https://arxiv.org/pdf/0810.1279)。

## 2 像の中のテストは三種類に分類できる

**仮定・圏。** D=M-Set。まずテストを F(f) の形に限る。この範囲の結論は ZFC。N の下では、像の二対象間の任意の射がこの形になる。

集合 S と f:Y→X に対し、Set(f,S):S^X→S^Y が全単射である条件は次のとおり。

| f の場合 | 合格する S |
|---|---|
| f が全単射 | 全て |
| f が非全単射かつ Y≠∅ | \(|S|\le1\) |
| Y=∅、X≠∅ | \(|S|=1\) |

**証明。** |S|≥2 なら、f が非全射であると S^X→S^Y は単射でなく、f が非単射であると全射でない。S=∅,1 の場合は空冪を含め直接計算する。Y→X があるため X=∅ なら Y=∅ である。∎

§1 の随伴同型から

\[
A\perp F(f)\iff\operatorname{Set}(f,H(A))\text{ is bijective}.
\]

従って、F(f) の形のテストからなる任意の集合が定めるクラスは

\[
\mathcal D,\qquad
\mathcal I=\{A:|H(A)|\le1\},\qquad
\mathcal E=\{A:|H(A)|=1\}
\]

の三つに限られる。

**明示的な coreflector。** I は coproduct と通常の全射商に閉じる。H が coproduct を集合の積に、全射商を単射に送るためである。従って

\[
r(B)=\bigcup\{C\subseteq B:C\text{ は M-部分対象かつ }C\in\mathcal I\}
\]

は I に属し、r(B)↪B が I-coreflection となる。実際、この和集合は集合個の I-対象の coproduct の全射像であり、I-対象からの射の像も I に属する。

E の coreflector は

\[
e(B)=r(\Omega\times B)\longrightarrow B
\]

である。第一射影が Ω への射を与えるので e(B)∈E。A∈E なら

\[
\operatorname{Hom}(A,e(B))
\cong\operatorname{Hom}(A,\Omega\times B)
\cong H(A)\times\operatorname{Hom}(A,B)
\cong\operatorname{Hom}(A,B).
\]

**境界点検。** 対角射 Ω→Ω² は I、終対象への射 Ω→1 は E を定める。Ω∈E だがその全射商 1 は E に属さないため、E を quotient-closed とする証明にはしていない。空テストの場合は D 全体。

## 3 任意のテストに対しても無限の像は使えない

**定理（ZFC）。** Σ を D の任意の射の集合、A={}^⊥Σ とする。一つでも無限集合 X について F(X)∈A なら、Σ の全ての射は同型であり、A=D である。

**証明。** F(Ω)=Ω^Ω=M は左正則作用であり、D の自由な一生成対象である。無限 X に対して選択公理により i:Ω→X と r:X→Ω を ri=id_Ω となるように取れる。従って

\[
F(X)\xrightarrow{F(i)}M\xrightarrow{F(r)}F(X),
\qquad F(i)F(r)=1_M.
\]

M は F(X) の retract。Coorthogonality class は retract に閉じるので M∈A となる。ところが Hom_M(M,s) は s の underlying function に同型である。従って全テストが全単射、すなわち M-Set の同型である。∎

**商閉包でも回避できない。** A の通常の全射商閉包を Q(A) とする。A∈A から無限 F(X) への全射があれば、F(X)↠M と合成して A↠M を得る。M は projective なのでこれが分裂し、再び全テストが同型になる。従って Σ に非同型があるなら

\[
F(X)\notin Q(A)\qquad(X\text{ infinite}).
\]

これは既存の正規化修復列にも適用できる。その段階は Q(A) に属するので、非自明なテストで無限 F(X) を段階として使うことはできない。

さらに、A の中の像の対象は F(0),F(1),F(2),… の中にしかない。これらと固定 B への全ての射を集めても集合個であり、この族だけでは解集合条件の失敗を作れない。

**上界が鋭い対照例。** M_fin⊂M を有限像の自己写像の M-部分集合とし、j:M_fin↪M を取る。全ての有限 n に対して F(n)⊥j だが、全ての無限 X で F(X)⊥̸j。

n>0 の場合、n 個の異なる値を持つ a∈Ω^n は F(n) を M-生成する。h:F(n)→M と m=h(a) を取る。a の値全てを固定する任意の u∈M は um=m を満たすため、m の像はその n 個の値に含まれる。従って h の全ての値は有限像であり、j を一意に経由する。n=0 では F(0)=1 から M や M_fin への射がなく、両 Hom は空。無限 X では上の F(X)↠M が id_Ω を像に含むため j を経由しない。この j は mono なので、その coorthogonality class は既存の ZFC 肯定定理により coreflective。

## 4 任意の標的への射を座標射に限ってはいけない

§3 は全テストに適用できるが、全ての固定標的への射が小さい座標集合に依存することを述べてはいない。

**対照例（ZFC）。** βΩ を Ω 上の全 ultrafilter の集合とし、M は pushforward で作用する。任意の X 上の ultrafilter U に対し

\[
h_U:\Omega^X\longrightarrow\beta\Omega,
\qquad f\longmapsto f_*U
\]

は M-equivariant である。無限基数 κ 上の uniform ultrafilter U を取ると、h_U はどの |Y|<κ の Y⊂κ への制限 Ω^κ→Ω^Y も経由しない。定数 0 と κ\Y の特性関数は Y 上で一致するが、pushforward はそれぞれ 0 と 1 の主 ultrafilter になるからである。Uniform ultrafilter は co-small filter の拡張として選択公理で取れる。

この U は可算完備とは限らないので N と矛盾しない。N が余分な射を消すのは §1 の特定の powers 間であり、任意の標的に同じ結論を拡張しない。

## 5 図式を加えた場合の正確な移送

C を小さい圏とし

\[
K=\mathbf{Set}^{C^{op}},\qquad D_C=(M\text{-Set})^C
\]

と置く。点ごとの F により E:K^op→D_C が得られ、ZFC+N で充満忠実な右随伴となる。左随伴の underlying K-object は H(A)(c)=Hom_M(A(c),Ω)。D_C も前層圏である。証明と境界例は [図式の別ノート](setop_diagram_boundary_2026-11-16.md)、§§1–2。

K のテスト集合 S に対し C_S=S^⊥ を通常の orthogonality class とすると

\[
{}^\perp E(S^{op})=\{A:H(A)\in C_S\}.
\]

**肯定できる範囲。** C_S が K の部分対象に閉じるなら、この逆像は ZFC で monocoreflective。H が D_C の全射商を K の mono に送るため逆像は全射商に閉じ、また Hom の定義から全ての小さい余極限に閉じる。従って §2 と同じ部分対象の trace が coreflector を与える。特に S が全て K の epi なら該当する。

最後の主張では、Z∈C_S、Z'↪Z、epi s:U→V と a:U→Z' に対し、Z での唯一の延長 V→Z の像が Z' に入ることを epi の成分ごとの全射性から確認する。したがって Z'∈C_S。

**一般には不足する点。** C_S は ZFC で reflective だが、それだけで逆像の coreflectivity は出ない。R:K→C_S を reflector とすると

\[
P_B=B\times_{E H(B)}E R H(B)
\]

への射 P_B→B は、全ての A∈{}^⊥E(S^op) からの Hom を全単射にする。実際 A→B の H 像は H(B)→H(A) であり、反射の単位 H(B)→R H(B) を一意に経由する。随伴により pullback への唯一の射が得られる。しかし P_B 自身が同じクラスに入ることは未証明。反射の存在とこの pullback の所属を区別する。

単純な図式 D_X=(Ω→Ω^X) については、[別ノート](setop_diagram_boundary_2026-11-16.md)、§§3–5 でさらに排除できる。無限 D_X を含む coorthogonality class は D_Ω を含み、根を指定した作用の明示的な colimit 表示から、全 D_X→b を受ける A 内の一つの対象 Z_b を構成できる。そのサイズは固定 b:B₀→B₁ のみに依存する。この対角族だけでも解集合条件は破れない。

## 6 一様に小さい商による表示と所属条件の不足

**定理（ZFC）。** §5 の K,D_C,E に対し λ=max(ℵ₀,|Mor C|)、κ=2^λ と置く。任意の G∈K について、E(G) は、|Q|≤κ の商 q:G↠Q に対応する部分対象 E(Q)↪E(G) の λ^+-directed union である。ここで |Q| は全成分の carrier の和。

**証明。** h:G(c)→Ω に対し、評価 ev_c の右随伴は

\[
(R_c\Omega)(d)=\Omega^{C(c,d)}.
\]

対応する自然変換 G→R_cΩ は x∈G(d) を (h(G(u)(x)))_{u:c→d} に送る。その像商 G↠Q は |Q|≤κ を満たし、h は q_c を経由する。従って E(G) の全ての元がいずれかの E(Q) に入る。

固定 G の商合同関係は集合個である。λ 個以下のこのような商の共通細分として G→∏_jQ_j の像を取れば、そのサイズは κ^λ=κ 以下。よって添字は λ^+-directed であり、その union は成分ごとに E(G) となる。各 E(Q) の carrier は 2^κ 以下である。C が空の場合も自明に成立する。∎

**所属の継承は偽。** この定理だけから、E(G)∈A のとき上の E(Q) も A に入るとはいえない。有限図式で既に反例がある。

C=[1]、K=Set^{C^op} の対象を G₁→G₀ と書く。

\[
G=(2\xrightarrow{1}2),\qquad Q=(2\twoheadrightarrow1),
\]

q:G↠Q を成分 (id₂,2→1) とする。D_C=Arr(M-Set) では

\[
E(G)=(\Omega^2\xrightarrow{1}\Omega^2),
\qquad E(Q)=(\Omega\xrightarrow{\Delta}\Omega^2).
\]

テストを

\[
\sigma:(\Omega\xrightarrow{1}\Omega)
\longrightarrow(\Omega\longrightarrow1)
\]

（成分 id_Ω と Ω→1）と取る。Hom(E(G),σ) は二つの座標射上の全単射 2→2 だが、Hom(E(Q),σ) は二つの座標射が対角上で一致する 2→1 であり非単射。従って E(G)∈{}^⊥{σ}、E(Q)∉{}^⊥{σ}。E(Q)↪E(G) は成分ごとには split mono ですらある。Hom_M(Ω²,Ω) が二つの座標射に限ることは、異なる二値の組を生成元とし、その二値を固定する M の作用で直接確認でき、N は不要。

この例は「全ての小さい商が所属を保つ」を否定するだけである。「十分な数の所属を保つ小さい商を選べる」を否定したことにはならない。この例自体では G が有限なので、自身を選べる。

さらに、この σ の coorthogonality class 自体は ZFC で coreflective である。[集合個の対象で測る同値射の因子分解](object_cogenerated_factorization_2026-11-16.md)で、任意の前層圏と集合個の対象 W_i について、全ての Hom(-,W_i) を保存する射を左クラスとする OFS を構成した。その左クラスは射の圏で coreflective であり、上の例は W=Ω の場合である。一般の右テストへの拡張は主張しない。

## 7 現在残る研究課題

裸の集合の像を巨大な候補として使う方法、裸の集合の埋め込み F の像内だけでテストを選ぶ方法、単純な対角図式は上記の理由で反例候補として除外された。より一般の図式への拡張は、反対向きのグラフや群の射を忠実に表す道具として残る。図式埋め込み E の像内のテスト全般を除外したわけではない。

必要なのは、固定したテスト集合 Σ と標的 B を先に決め、その coorthogonality class に属する構造付きの候補から B への射が、A 内の対象を通じてどのサイズ上界にも収まらないことを示す構成である。§6 の小さい商の表示だけでは、その所属条件が得られない。像の内部で反射・余反射があることも、ambient な解集合条件を自動では決めない。

[図式ノート §6](setop_diagram_boundary_2026-11-16.md) では、N の下で一般の図式なら Ord^op の充満埋め込みまで運べることも、文献結果と組み合わせて確認した。しかしそれが固定テストの正規化修復列であるという条件は得ていない。既存の WVP⇒P の逆向き、N⇒¬P、独立性はいずれも未証明である。
