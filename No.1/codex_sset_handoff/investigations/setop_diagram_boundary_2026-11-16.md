# Set^op の図式への拡張と対角射の除外

日付：2026年11月16日。新しい直接証明は主担当と別担当が照合した `INTERNAL_PROOF_CHECKED`。§6 の集合論的入力は文献結果として区別する。外部査読・形式検証・文献上の新規性、独立性・反例・一般の P の肯定を主張しない。

## 1 出発点と文献

N を「非可算の可測基数が存在しない」とし、Ω を可算無限集合、M=End_Set(Ω) とする。M-Set は左 M-作用の圏。

Isbell, *Adequate subcategories*, 2.5, pp.549–550 は、可算無限離散空間の right adequacy と可測基数の不存在を同値にしている。したがって ZFC+N では

\[
F:\mathrm{Set}^{op}\longrightarrow M\text{-}\mathrm{Set},\qquad F(X)=\Omega^X
\]

が充満忠実である。作用は後合成。Shulman, *Set theory for category theory*, p.20 に同じ M-Set への定式化がある。2026年11月16日に両本文を再確認。

- Isbell: <https://conceptualmathematics.wordpress.com/wp-content/uploads/2013/05/adequatesubcategories.pdf>
- Shulman: <https://arxiv.org/pdf/0810.1279>

\(L(A)=\operatorname{Hom}_M(A,\Omega)\) を Set^op の対象とすれば L⊣F。これは積の普遍性からの直接計算であり、像は reflective。

## 2 図式圏への拡張

**仮定・圏。** ZFC+N、C は任意の小さい圏、\(\mathcal K=\mathrm{Set}^{C^{op}}\)、\(\mathcal D=(M\text{-}\mathrm{Set})^C\)。D も前層圏。

**命題。** 点ごとの F は充満忠実な右随伴

\[
E:\mathcal K^{op}\cong(\mathrm{Set}^{op})^C\longrightarrow\mathcal D
\]

を与える。左随伴 H の underlying K-object は

\[
H(A)(c)=\operatorname{Hom}_M(A(c),\Omega),
\]

であり、C の射には前合成を使う。

**証明。** 点ごとの随伴同型は C の自然性条件と両立するので、自然変換集合にも随伴同型を与える。充満忠実性も点ごとに従う。∎

K の射 s:Y→X に対する E(s^op):E(X)→E(Y) は

\[
A\perp E(s^{op})\quad\Longleftrightarrow\quad
\operatorname{Hom}_{\mathcal K}(s,H(A))\text{ is bijective}
\]

を満たす。したがって像の射だけからなるテストは、K の通常の小さい orthogonality class の H による逆像に対応する。像内部での coreflectivity と、D 全体におけるその逆像の coreflectivity は別である。

**境界点検。** E は underlying componentwise な mono と epi を逆転する。集合写像 Y→X に沿う制限 Ω^X→Ω^Y は、それぞれ Y→X が単射なら全射、全射なら単射であり、逆も成立する。一方、任意の colimit は保存しない。C が一点の場合にも Ω⊔Ω→Ω が同型でない。Ab^op などの符号化には、Ab の通常の充満埋め込みの opposite とこの E を合成できるが、合成が右随伴であるとはこの議論ではいえない。

## 3 最小の図式候補：対角射

ここからは ZFC のみでよい。自然な M-作用を持つ Ω と M を使い、c_n∈M を値 n の定数関数とする。Arr(M-Set) に

\[
D_X=(\Omega\xrightarrow{\delta_X}\Omega^X),\qquad
\delta_X(n)=\text{constant function with value }n
\]

を取る。X=∅ の場合の終域は一元 M-集合。D_Ω=(Ω→M) の射は n↦c_n。

任意の無限 X に対し、D_Ω は D_X の retract である。実際、集合 Ω は X の retract であり、X→1 と Ω→1 の間の retract を反転して F を適用すればよい。この向きには N は不要。

ただし D_Ω は Arr(M-Set) の生成対象ではない。例えば、始域が非空な D_Ω から (∅→M) への射はないが、(∅→M) は恒等射と、M 上の定数写像との右合成が与える相異なる自己射を持つ。この二射を D_Ω で区別できない。従って裸の F(X) に対する「M が retract になる」という議論を、そのまま射の圏の生成性に置き換えることはできない。

## 4 根を指定した作用の明示的表示

**仮定・圏。** Arr(M-Set)。β:Ω→C が M-射で

\[
c_n a=\beta(n)\qquad(n\in\Omega,\ a\in C)\tag{*}
\]

を満たすものを考える。

**補題。** (Ω→C) は D_Ω の小さい colimit と retract を反復して得られる。従って D_Ω を含む任意の coorthogonality class に属する。

**証明。** B=(Ω=id Ω) は D_Ω の retract である。後向きの終域射 M→Ω は固定した n₀ での評価 u↦u(n₀)、前向きは定数写像の包含であり、これらは M-equivariant。

C の元 a ごとに D_Ω のコピーを取り、全てのコピーの B を同一視した pushout Q を作る。その始域は Ω、終域は M のコピーを定数関数部分で同一視したもの。コピー a の u∈M を u·a に送ることで Q→(Ω→C) ができる。終域上全射であり、Q の各元も (*) を満たす。

この全射の核関係の各対 (x,y) は、D_Ω から Q への二射として表せる。始域射はともに id_Ω、終域射はそれぞれ u↦u·x と u↦u·y。これら全てを coequalize すると (Ω→C) を得る。核関係は集合なので小さい colimit だけを使う。∎

**境界点検。** β が単射であることは不要。根が全て一つの M-固定点に潰れる場合も、核関係を終域でだけ同一視すればよい。β:Ω→C があるので C は非空。D_X は全て (*) を満たし、X=∅ も含めて補題が適用される。

従って任意の coorthogonality class A⊆Arr(M-Set) に対し、無限 X について

\[
D_X\in A\quad\Longleftrightarrow\quad D_\Omega\in A.
\]

右から左はこの補題、左から右は retract 閉性。

## 5 固定標的への普遍的な有界受け皿

**仮定。** A⊆Arr(M-Set) は coorthogonality class、D_Ω∈A。標的 b:B₀→B₁ を固定する。

R=Hom_M(Ω,B₀) とし、各 r∈R に対して β_r=b r および

\[
C_r=\{x\in B_1:\ c_n x=\beta_r(n)\text{ for every }n\in\Omega\}
\]

を取る。これは M-部分対象である。実際 c_nu=c_n より、x∈C_r なら ux∈C_r。また各 β_r(k) が C_r に属するので非空。β_r:Ω→C_r は (*) を満たす。

\[
Z_b=\left(\coprod_{r\in R}\Omega\longrightarrow\coprod_{r\in R}C_r\right)
\]

とし、z_b:Z_b→b は第 r 成分で r と包含 C_r↪B₁ により定める。

**命題。** Z_b∈A であり、全ての集合 X について

\[
\operatorname{Hom}(D_X,Z_b)\xrightarrow{(z_b)_*}\operatorname{Hom}(D_X,b)
\]

は全単射。特に D_X の族だけから、固定 b における A の解集合条件を破ることはできない。

**証明。** 各 (Ω→C_r) は §4 より A に属し、A は coproduct に閉じるので Z_b∈A。

(r,h):D_X→b に対し、任意の f∈Ω^X と n∈Ω について

\[
c_nh(f)=h(c_nf)=\beta_r(n).
\]

したがって h の像は C_r に入り、第 r 成分への因子化がある。X=∅ でも c_nf=f かつ h(f)=β_r(n) なので同じ式が成り立つ。

Ω は M-connected で End_M(Ω)={id} なので、Ω→∐_RΩ は一つの成分を選ぶしかない。b との合成を指定すると、その成分は r に決まる。Ω^X も非空かつ M-connected であり、定数操作と根の可換性から終域射は同じ成分 C_r に入る。C_r↪B₁ は単射だから、その射も一意。∎

**サイズと空の場合。** \(|R|\le |B_0|^{\aleph_0}\) なので、例えば

\[
|Z_b|\le \aleph_0+|B_0|^{\aleph_0}(\aleph_0+|B_1|)
\]

という標的だけに依存する上界がある。R=∅ なら Z_b は初対象であり、D_X→b 自体が存在しない。根が潰れている場合も証明は変わらない。

**範囲。** z_b が A 全体の coreflection であるとは主張しない。対角族 D_X および (*) を満たす根付き対象からの射に対して普遍である、という正確な除外結果。一般の図式 E(X)、構造付きグラフや群、任意の混合テストはこの証明の対象外。

## 6 Ord^op の図式としての実現と残る不足

裸の Set^op に Ord^op を充満埋め込みすることはできない。自己射が一つしかない集合は空集合と一元集合に限られるので、充満埋め込みの像に現れ得る同型類が二つしかない。

一方、図式を許すと事情は変わる。文献上、VP は Ord の Gra への充満埋め込みがないことと同値であり、VP⇒WVP、WVP⇒可測基数の真クラスの存在が知られている。したがって N の下では Ord→Gra の充満埋め込みがある。Gra を通常の二項関係と準同型の圏とすれば、辺集合を関係そのものとすることで Quiv に充満埋め込みできる。§2 を Quiv に適用して

\[
\mathrm{Ord}^{op}\longrightarrow\mathrm{Gra}^{op}
\longrightarrow\mathrm{Quiv}^{op}\longrightarrow\mathcal D
\]

という前層圏 D への充満埋め込みを得る。

この段落の集合論的入力は Bagaria–Wilson, *The Weak Vopěnka Principle for definable classes of structures*, Introduction および §2 を2026年11月16日に本文で確認したもの。新しい独立性結果ではない。

クラスの扱いは同文献 §2 に合わせる。任意クラス版なら NBG 等で解釈し、ZFC の schema 版なら §2.1 Definition 2.2 の集合パラメータを許す定義可能クラスを使う。特定の低い定義複雑度、パラメータなしの列、明示的な正規化修復列を得たという主張はしない。

**クラスの扱い。** 同論文は §2 末尾で任意のクラスへの量化には NBG などを用いると説明し、§2.1 Definition 2.2 では集合パラメータを許す定義可能な列に制限した schema を別に定義する。ここではその標準的な区別を維持し、N から得る列に特定の定義複雑度やパラメータ不要性を割り当てない。特定の固定テスト修復列の定義可能性を得たという意味でもない。

資料：<https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/weak-vopenka-principle-for-definable-classes-of-structures/B95D82A33C8D715E042F24CE73CF2361>

この実現は、固定した集合個のテストに対する修復列であること、商閉包 Q(A) に属すること、修復射の A-equivalence と Q-内部 mono 性を満たすことを保証しない。従って第14段階の必要条件を満たす抽象的な列は得られても、その必要条件を逆向きに使って P の反例を得たことにはならない。残る課題はこの「固定テストによる実現」であり、対角射だけでは §5 の有界受け皿により解決しない。
