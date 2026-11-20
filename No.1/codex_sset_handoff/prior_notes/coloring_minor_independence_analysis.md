# 無限彩色・無限 minor から small-coorthogonality 問題の独立性へ

作成日：2026-11-15

## 0. 対象と到達点

今回の命題は

\[
P:\quad \text{任意の locally presentable category }\mathcal K
\text{ と射の集合 }S\text{ について }{}^\perp S\text{ は coreflective}
\]

である。ここで

\[
{}^\perp S=\{X:\mathcal K(X,U)\xrightarrow{\mathcal K(X,f)}
\mathcal K(X,V)\text{ が全単射 }(f:U\to V\in S)\}.
\]

**このノートは P の ZFC 独立性の証明ではない。** 以下を確立する。

1. 可算パレットの list colouring を固定対象への射として表現する presheaf category を明示する。
2. そこで「彩色不可能」クラスは一本の射に対する coorthogonality class であり、ZFC で coreflective。一方、その accessibility は、ある ω₁-strongly compact cardinal の存在と同値になる。
3. 任意の locally presentable category において、「固定対象 D への射がちょうど一本」というクラスは ZFC で coreflective。
4. VP の相対的無矛盾性の下では、P と「すべての無限基数で κ-Hadwiger 予想が失敗する」が両立する。Suslin tree による、より特殊な minor 反例も P と両立する。
5. 固定グラフ H の minor の存在には、H の大きさだけで抑えられる部分グラフ内の証人がある。

文献の定理は末尾の [FH], [U], [BT], [KS], [BCMR] に帰属させる。それらから導く圏論的命題は、以下で直接証明する。独立性の新しい既知定理が発見されたという意味ではない。

## 1. 既知の彩色コンパクト性定理

色の集合を ω に固定する。各頂点 v に許される色の集合 L(v)⊆ω を指定し、c(v)∈L(v) かつ隣接頂点の色が異なる写像 c を L-colouring と呼ぶ。

C_κ を次の主張とする。

> 任意のグラフ G とリスト L について、頂点数が κ 未満のすべての部分グラフが制限されたリストに関して彩色可能なら、G 全体も L-colourable である。

[FH, Theorem 7] の δ=ω の場合から、非可算 κ に対して

\[
C_\kappa\quad\Longleftrightarrow\quad
\kappa\text{ is }\omega_1\text{-strongly compact}.
\]

これは通常の可算彩色ではなく、**リストを指定した彩色**についての同値性である。

## 2. List colouring の固定 presheaf category への符号化

### 2.1 母圏と固定対象

Λ を次の quiver とする。

- 頂点は P(ω) の元、つまり色のリスト。
- 各順序対 (L,M) について、L→M の辺をちょうど一本持つ。L=M も許す。

したがって、任意の quiver G へのリスト割当 L:G_v→P(ω) は、一意に quiver morphism G→Λ を決める。

\[
\mathcal K=\mathbf{Quiv}/\Lambda
\]

と置く。これは presheaf category の slice なので、再び presheaf category であり、locally finitely presentable である。射は quiver morphism であって、頂点のリストラベルを厳密に保存するもの。

E を次の quiver とする。

- 頂点は (L,n)、ただし n∈L⊆ω。
- (L,n)→(M,m) の辺は n≠m のときちょうど一本、n=m のとき零本。

射 p:E→Λ を (L,n)↦L で定め、slice の対象 D=(p:E→Λ) とする。

すると、X=(G,L) に対して

\[
\mathcal K(X,D)\cong \operatorname{Col}_L(G).
\]

辺の像は頂点の像で一意に決まる。平行辺の数は彩色に影響せず、ループがあれば彩色は存在しない。通常の単純無向グラフは各無向辺を両方向の辺に置き換えて含められる。したがって、ここでの彩色コンパクト性は通常の list colouring のものと同値である。

### 2.2 彩色不可能な対象

空 quiver の slice 対象を 0 とし、

\[
\mathcal N=\{0\}\cup\{X:\mathcal K(X,D)=\varnothing\}
\]

と置く。このとき

\[
\boxed{\mathcal N={}^\perp\{0\to D\}.}
\]

非空 X では Hom(X,0)=∅ なので、Hom(X,0)→Hom(X,D) が全単射である条件は Hom(X,D)=∅。X=0 では両者が一元集合である。

さらに、次で coreflector が与えられる。

\[
R(B)=
\begin{cases}
B,&\mathcal K(B,D)=\varnothing,\\
0,&\mathcal K(B,D)\neq\varnothing.
\end{cases}
\]

第一の場合 B 自身が N に属する。第二の場合、非空 A∈N から B への射は存在しない。もし存在すれば B→D と合成して A→D が得られるからである。従って 0→B が coreflection である。

**この coreflection は ZFC だけで存在する。**

## 3. 同じクラスの accessibility は大きな基数と同値になる

### 命題

上で定義した、一本の射への coorthogonality class N について、

\[
\boxed{
\mathcal N\text{ is accessible}
\quad\Longleftrightarrow\quad
\exists\kappa\ C_\kappa
\quad\Longleftrightarrow\quad
\exists\kappa\ (\kappa\text{ is }\omega_1\text{-strongly compact}).
}
\]

最後の同値性は [FH, Theorem 7]、最初は以下の直接証明による。

### 3.1 Accessibility から小さい obstruction へ

N が accessible と仮定し、その accessible generation に用いる対象の集合を G とする。N は coorthogonality class なので K のすべての小余極限で閉じており、包含 N→K はそれらを保存する。

G に含まれる全対象の頂点数・辺数を上から抑える非可算正則基数 κ を選ぶ。

非空な彩色不可能対象 X∈N は、G の対象からなる filtered diagram の余極限である。従って、ある非空 A∈G と射 a:A→X がある。全図式が空対象だけなら、その余極限も空対象になってしまうためである。

X 内で a(A) の頂点が張る誘導部分グラフ H は、頂点数が κ 未満である。H にリスト彩色があれば A に引き戻せるが、A∈N なので不可能。

従って、任意の彩色不可能 X は κ 未満の彩色不可能部分グラフを持つ。対偶を取ると C_κ が成立する。

### 3.2 小さい obstruction から accessibility へ

C_κ を仮定する。十分大きい非可算正則 λ>κ を固定する。

任意の非空 X∈N は、頂点数 κ 未満の彩色不可能部分グラフを持つ。必要な各隣接関係に対して X の辺を一本ずつ選べば、頂点数と辺数の和が λ 未満の彩色不可能部分 quiver Z⊆X を得る。

Z を含み、頂点数と辺数の和が λ 未満である部分 quiver Y⊆X 全体を考える。

- 各 Y は Z を含むため彩色不可能。
- これらは λ-directed な半順序をなす。λ 未満個の合併は、λ の正則性により再び大きさ λ 未満。
- その合併は X。

λ 未満の大きさの quiver は、slice K でも λ-presentable である。N の包含は λ-filtered colimits を保存するので、これらの Y は N の中でも λ-presentable。

ラベル Λ は固定された集合なので、大きさ λ 未満のラベル付き quiver の同型類は集合個。これらと空対象を合わせると N の accessible generating set が得られる。

### 帰結

ω₁-strongly compact cardinal が存在しないモデルでは、N は accessible でない。しかし 2.2 の coreflector はそのモデル内でも存在する。

従って、

\[
\text{無限 list colouring のコンパクト性の失敗}
\]

をそのまま N に移すことはできるが、得られるのは **nonaccessibility** であって、P の反例である **noncoreflectivity** ではない。

ここでは、同じ一本の射 0→D を使って、その区別が具体的に現れる。

## 4. 「解がちょうど一つ」への変換も coreflectivity を破らない

### 一般命題

K を locally presentable、D∈K とする。

\[
\mathcal U_D=\{X:|\mathcal K(X,D)|=1\}.
\]

すると、

\[
\mathcal U_D={}^\perp\{D\to1\}
\]

であり、U_D は ZFC で coreflective。

### 証明

任意の B∈K を固定する。A∈U_D と a:A→B に対し、唯一の射を c_A:A→D と書く。

\[
\langle a,c_A\rangle:A\to B\times D
\]

を strong epi–mono 分解する。

\[
A\twoheadrightarrow Q\hookrightarrow B\times D.
\]

Q→D は射影から存在する。二つの射 u,v:Q→D があれば、A 上への制限は唯一性から等しい。A↠Q が epi なので u=v。従って Q∈U_D。

K は well-powered なので、B×D の subobject で domain が U_D に属するものは、同型を除いて集合個である。その代表を Q_j↪B×D とする。

C=⊔_j Q_j と置く。Hom(C,D) は一元集合の積なので一元集合。射 C→B×D の strong image を R_B↪B×D とすると、同じ epi の議論により R_B∈U_D。

r_B:R_B→B を第一射影との合成とする。

任意の A∈U_D と a:A→B は、その組み合わせ <a,c_A> の像 Q_j を通じて R_B→B を経由する。従って存在は成立。

u,v:A→R_B が r_Bu=r_Bv を満たすなら、D への成分も A∈U_D によって等しい。R_B↪B×D は mono なので u=v。従って分解は一意。

よって r_B が coreflection。□

### 彩色への適用

K=Quiv/Λ、D=(E→Λ) とすれば、U_D は「指定されたリストについて彩色がちょうど一つ」のクラスである。したがって、この条件にしても P の反例は得られない。

この場合、R_B は slice の積 B×_Λ E の部分対象として構成できる。つまり一意な彩色を対象に付け加えて記録すると、候補を固定した一つの集合サイズの対象の中に集められる。

### 重要な区別：固定された一つの彩色と、すべての彩色

一般の f:U→V に対して K/V を考えると、対象 (X,h:X→V) が f への射をちょうど一つ持つ条件は、h の f に沿った持ち上げがちょうど一つという条件である。

この **slice 内のクラス** は上の一般命題で coreflective。

しかし元の問題は

\[
X\perp f\iff
\text{すべての }h:X\to V\text{ が一意に持ち上がる}
\]

である。slice の coreflector は h に依存するので、ここから元の K 内の {}^⊥{f} の coreflector は得られない。

従ってこの一般命題は P を解いていない。一方、**一つの list-colouring 問題を唯一解問題に変えるだけの還元は、十分ではない**ことを示す。

## 5. Minor 側：Hadwiger 型反例は P と両立する

κ-Hadwiger 命題を

\[
H_\kappa:\quad
\forall G\ (|V(G)|=\chi(G)=\kappa\Rightarrow K_\kappa\preccurlyeq_m G)
\]

と定義する。

[U, Theorem 1.1] が引用する Komjáth の定理によれば、任意の無限 μ に対して、頂点数 2^μ、彩色数 μ^+、K_{μ^+} minor を持たないグラフが存在する。

GCH の下では 2^μ=μ^+ なので、すべての無限後続基数 κ で H_κ が失敗する。

無限極限基数 κ では ZFC だけで反例がある。例えば κ 未満の濃度の完全グラフを、濃度が κ に共終になるように非交和する。全体のサイズも彩色数も κ だが、連結な K_κ の minor model は一つの連結成分に入らねばならず、その成分のサイズは κ 未満なので不可能。κ=ω には有限完全グラフの非交和を使う。

従って

\[
\mathrm{ZFC}\vdash\mathrm{GCH}\Rightarrow
\forall\kappa\geq\aleph_0\ \neg H_\kappa.
\]

この帰結は [U, §6] にも明記されている。

一方 [BT, Corollary 26] は

\[
\operatorname{Con}(\mathrm{ZFC}+\mathrm{VP})
\Rightarrow
\operatorname{Con}(\mathrm{ZFC}+\mathrm{VP}+\mathrm{GCH})
\]

を示す。既知の VP⇒P と組み合わせると、

\[
\boxed{
\operatorname{Con}(\mathrm{ZFC}+\mathrm{VP})
\Rightarrow
\operatorname{Con}\bigl(\mathrm{ZFC}+P+
\forall\kappa\geq\aleph_0\ \neg H_\kappa\bigr).
}
\]

**すべての無限基数に Hadwiger 型反例が存在しても、P は真であり得る。**

したがって「Hadwiger 型反例が任意に大きく存在する」という仮定だけから ¬P を導く一般的還元は、VP の相対的無矛盾性を認める限り成立しない。

## 6. Suslin tree に由来する特殊な反例も P と両立する

[U, Theorem 4.2] の κ=ω₁ の場合は、Suslin tree の存在と、次のグラフの存在を同値にする。

- 頂点数 ω₁。
- 濃度 ω₁ の independent set を持たない。
- K_{ω₁} minor を持たない。

[BT, Theorem 24] によると、VP は任意の set forcing で保存される。

一方、Suslin tree を付加する set forcing がある。例えば Jech の countably closed forcing は free Suslin tree を付加する。[KS, Introduction] にも説明されている。

従って、VP のモデルからその forcing を行うと、VP と Suslin tree が両立し、従って P と上の特殊な minor 反例が両立する。

\[
\operatorname{Con}(\mathrm{ZFC}+\mathrm{VP})
\Rightarrow
\operatorname{Con}(\mathrm{ZFC}+P+\text{Suslin tree exists}).
\]

これは、Suslin tree を用いるあらゆる構成を否定するものではない。しかし、**Suslin tree の存在だけを仮定して P の反例を必ず作る**という方針は成立しない。

同様に、V=L の下で研究を継続することは排除されていないが、その証明で GCH または Suslin tree の存在しか使わないなら、この障害にぶつかる。

## 7. 固定した minor には大きさの有界な証人がある

### 補題

H を固定グラフ、μ=max(aleph₀, |V(H)|) とする。

\[
H\preccurlyeq_m G
\Rightarrow
\exists G_0\subseteq G\quad
|V(G_0)|\leq\mu,\quad H\preccurlyeq_m G_0.
\]

有限 H の場合には G₀ も有限にできる。

### 証明

H の各頂点 h に対応する、互いに素な非空連結 branch set B_h を取る。

各 h に根 r_h∈B_h を一つ選ぶ。H の各辺 hh' に対し、B_h と B_{h'} を結ぶ G の辺を一本選ぶ。

各 B_h の内部で、今選んだ接続辺の端点と r_h を有限パスで結ぶ。H が単純グラフなので |E(H)|≤μ。根、接続辺、有限パスの合併に含まれる頂点数は μ 以下。

縮小された branch sets は依然として連結で互いに素であり、必要なすべての接続辺を保つ。これらの合併が求める G₀。□

従って、固定した H の minor の存在そのものは、任意に高いサイズまで「証人が見つからない」現象を生まない。この点で、大きな基数のないモデルにおける固定可算パレットの list-colouring 非コンパクト性とは異なる。

ただし、この補題は H-minor-free なクラスの colimit 閉性や coreflectivity を主張するものではなく、minor を使ったあらゆる高度な符号化を排除するものでもない。

## 8. Minor を Hom に表現する素朴な方法の限界

G に対し M(G) を、非空連結頂点集合を頂点とし、二つの頂点集合が互いに素で、その間に G の辺が存在するとき隣接するグラフとする。

このとき完全グラフについては

\[
K_\kappa\preccurlyeq_m G
\iff
\operatorname{Hom}(K_\kappa,M(G))\neq\varnothing.
\]

完全グラフを使うため、すべての branch sets の二つずつの非交差が辺保存条件で要求される。

しかし、通常のグラフ準同型 h:G→G' は、互いに素な連結集合を重なる集合に写し得る。このため S↦h[S] は一般に M(G)→M(G') の準同型を与えず、M はこの方法では通常の Graph 上の関手にならない。

例として P₄=a-b-c-d を K₂ へ交互に二彩色する。互いに素で接続している連結集合 {a,b} と {c,d} は、両方とも K₂ の全頂点集合に写る。その二つの像は交差するので、M(G') 内の隣接する二頂点にはならない。

さらにこの表示は固定始域 K_κ から可変標的 M(G) への射の存在であり、今回必要な Hom(X,U)→Hom(X,V) の全単射性とは向きと役割が異なる。従って、この表示だけでは coorthogonality や coreflection を移送できない。

## 9. なお必要なもの

反例を示すには、固定した K、集合 S、標的 B に対して A={}^⊥S と置き、A↓B に終対象がないことを示さなければならない。

A は小余極限閉なので、A↓B は余完備である。従って次は同値。

1. B の A-coreflection が存在する。
2. A↓B に weakly terminal な集合が存在する。
3. 標準的な構造としての表示を固定すると、ある基数 μ があり、任意の a:A→B（A∈A）が、大きさ μ 未満の A の対象を経由する。

3⇒2 は、有界サイズの対象と B への射が同型を除いて集合個であるため。2⇒1 は完備圏の初対象補題の双対。1⇒3 は coreflector の大きさより大きい μ を選ぶ。

従って否定側の目標は、同じ K,S,B を固定したまま

\[
\forall\mu\ \exists a:A\to B,\quad A\in{}^\perp S,
\]

であって、大きさ μ 未満の {}^⊥S 対象を一つも経由しないものを作ること。

彩色側で上の N が nonaccessible になることは、「小さい対象で全体を生成できない」ことを表す。しかし固定した B の coreflector は B または 0 で済み、そのような因子分解障害を生まない。

minor 側では、Hadwiger 型反例が全サイズで存在しても P と両立する。従って反例そのものの存在以上の、Hom の構造または特定の追加仮定が必要。

**現時点で、この因子分解障害を無限彩色または無限 minor の独立性から構成する還元は得られていない。**

## 文献

[FH] Roman Feller and Peter Holy, *Large cardinal characterizations via compactness for list colourings*, arXiv:2608.20883v1 (2026), Definitions 5–6, Theorem 7.

[U] Dávid Uhrik, *The Uncountable Hadwiger Conjecture and Characterizations of Trees Using Graphs*, arXiv:2212.02169; Acta Mathematica Hungarica (2024), Theorem 1.1, Proposition 2.2, Theorem 4.2, Section 6. DOI: 10.1007/s10474-024-01399-x.

[BT] Andrew D. Brooke-Taylor, *Indestructibility of Vopěnka's Principle*, arXiv:1003.4707; Archive for Mathematical Logic 50 (2011), 515–529. Theorem 24 and Corollary 26 in the inspected arXiv version.

[KS] John Krueger and Šárka Stejskalová, *Forcing Over a Free Suslin Tree*, arXiv:2402.00226v3 (2026), Introduction, discussion of Jech's forcing.

[BCMR] Joan Bagaria, Carles Casacuberta, A. R. D. Mathias and Jiří Rosický, *Definable orthogonality classes in accessible categories are small*, arXiv:1101.2792v4, Definition 7.7 and Theorem 8.8. This supplies the large-cardinal coreflectivity background, in particular the use of VP⇒P.
