# Mono と終対象への右テストを併用する因子分解

2026年11月16日。主担当の構成を別担当が直接点検した証明。状態は `INTERNAL_PROOF_CHECKED`。外部査読・形式検証・文献上の新規性は主張しない。既存の [対象で測る同値射の因子分解](object_cogenerated_factorization_2026-11-16.md) の構成を使い、mono の右テストを同時に課せることを示す。

## 1 仮定と結論

K=Set^{C^op} を前層圏とする。集合個の対象 (W_i) と、集合個の mono (m_j:U_j↪V_j) を固定し、右テストの集合を

\[
\Sigma=\{W_i\to1:i\in I\}\cup\{m_j:U_j\hookrightarrow V_j:j\in J\}
\]

とする。直交は全て一意対角持上げの意味であり、

\[
\mathcal L={} ^{\perp_u}\Sigma,
\qquad\mathcal R=\mathcal L^{\perp_u},
\qquad
\mathcal E=\{e:\operatorname{Hom}(e,W_i)\text{ is bijective for all }i\}
\]

と置く。

**定理（ZFC）。** (L,R) は orthogonal factorization system である。両種類のテストを同時に課した結論であり、別々の OFS の存在だけを述べているのではない。

## 2 固定した受け皿と初期像

f:A→B を固定する。既存の構成と同じく

\[
T_A=\prod_i W_i^{\operatorname{Hom}(A,W_i)},\quad
T_B=\prod_i W_i^{\operatorname{Hom}(B,W_i)},\quad
P=B\times_{T_B}T_A
\]

を作る。T_A→T_B は f に沿う前合成で決まり、A→P は f と評価射から定まる。

この p:P→B は E^{⊥_u} に属し、L⊆E なので R にも属する。また全ての A→W_i は P 上への座標延長を持つ。

初期像を J₀=im(A→P) とする。A↠J₀ は、上記の座標延長により E に属する。一方、前層圏の通常の全射は全ての mono に一意左直交する。従って A→J₀∈L。

## 3 L の持上げで生成する部分対象の閉包

A→J∈L と J↪P が得られているとする。e∈L を用いた全ての可換四角

\[
\begin{array}{ccc}
X&\xrightarrow{u}&J\\
e\downarrow&&\downarrow\\
Y&\xrightarrow{v}&P
\end{array}
\]

に現れる v の像の和集合を C(J)⊆P と定義する。これは P の各成分に対する Separation で定義できる部分前層である。L 所属は集合パラメータを持つ条件なので、クラス個の coproduct や証人選択は必要ない。e=id_J を含めることで J⊆C(J)。

**補題。** 包含 J→C(J) は L に属する。

まず E 所属は既存の座標延長の証明と同じである。任意の χ:J→W_i は A 上の制限の座標を使って P に延長できる。二つの C(J)→W_i が J 上で一致すれば、各生成射 v:Y→P と合成した二射は e の後で一致する。e∈L⊆E の一意性により Y 上でも一致し、像が C(J) を覆うので全体で一致する。

次に任意の mono m_j:U_j↪V_j と、J→C(J) から m_j への正方形

\[
a:J\to U_j,\qquad b:C(J)\to V_j,
\qquad m_j a=b|_J
\]

を取る。定義に現れる e,u,v に対して v を C(J) に値を持つ射とみなすと、

\[
m_j a u=bv e
\]

である。e∈L より、Y→U_j の一意の lift がある。その m_j との合成は bv なので、b は im(v) を U_j の像の中に送る。m_j が mono であるため、この lift は Y↠im(v) に沿って降りる。異なる生成像の重なりでも、m_j との合成が b に一致することから降りた射は一致する。

従ってこれらは C(J)→U_j に貼り合わさり、所望の lift となる。一意性は m_j が mono であることから従う。これで全ての m_j への直交も得た。∎

## 4 停止と OFS

後続段階は C(J)、極限段階は和集合として J₀ から反復する。L は合成と超限合成に閉じるため、全ての A→J_α は L に属する。κ=max(ℵ₀,Σ_c|P(c)|) と置けば、固定した P の部分対象の増大列は κ^+ より前に停止する。

固定点 J=C(J) では、L と J↪P の任意の正方形の下辺 Y→P は J に像を持つので lift が存在する。包含が mono なので lift は一意。従って J↪P∈R。p:P→B も R に属するので

\[
A\xrightarrow{\mathcal L}J\xrightarrow{\mathcal R}B
\]

を得る。Σ⊆R より {}^{⊥_u}R=L であり、定義通り R=L^{⊥_u} だから OFS となる。∎

## 5 Mono だけの場合の短い証明

I=∅ の場合、最初から P=B であり、中間対象は B の部分対象に収まる。この場合は交わりによっても直接構成できる。

全ての epi が L に属するので、R の射は mono である。固定 f:A→B に対し、f を経由させる R-部分対象 C↪B 全ての交わりを取る。B 自身が候補であり、部分対象は集合個、R は極限に閉じるので、最小の候補 c:C↪B が得られる。

f=cℓ と書く。ℓ と任意の m_j の正方形に対し、下辺 C→V_j に沿って m_j を引き戻して d:D↪C を作る。m_j∈R なので d と cd は R に属し、ℓ は D を経由する。最小性から D=C となり、ℓ に対する lift が得られる。一意性は m_j が mono であることによる。従って ℓ∈L。

## 6 境界点検と残る範囲

- Mono テストが空なら、既存の対象で測る同値射の因子分解に一致する。終対象へのテストが空なら、§5 の mono のみの場合を含む。
- 両方空なら L は全ての射、R は同型射であり、閉包は B まで到達する。
- 各 m_j の終域 V_j は任意であり、injective であることも終対象であることも仮定していない。従って「非終対象の終域」だけが障害ではない。
- 貼合せの段階では mono 性を本質的に使った。非 mono のテストに対する lift は、像への降下や異なる生成像の重なりで一致するとは限らない。この証明はその場合を処理していない。
- この定理は、任意の右テストを epi–mono に分解して二つのテストに置き換えてよい、という主張ではない。合成への一意左直交と各因子への一意左直交が同値であるとは仮定しない。
- 通常の Hom と一意持上げだけを扱う。弱い持上げ性への置換、巨大基数、Global Choice、一般の P の肯定・否定は用いていない。

## 7 始域が各成分で有限な場合の別の肯定結果

**系（ZFC）。** K=Set^{C^op}、Σ={s_i:U_i→V_i} を射の集合とする。全ての i,c に対し U_i(c) が有限なら、({}^⊥_uΣ,({}^⊥_uΣ)^⊥_u) は OFS。V_i は任意でよく、有限濃度の一様な有限上界も不要。

**証明。** Arr(K) も前層圏であり、テスト

\[
\rho_{s_i}:(1_{U_i})\longrightarrow s_i
\]

の始域は二つの位置とも U_i(c) である。従って [既存の有限始域定理6.1](../audits/compactness_and_finite_tests.md) を Arr(K) に適用でき、その ordinary coorthogonality class L は coreflective。これは一意左持上げのクラス {}^⊥_uΣ に一致する。[既存の橋渡し §2.1](factorization_bridge_2026-11-16.md) により L の coreflection が求める OFS を与える。∎

これは既存定理からの帰結であり、有限探索からの一般化ではない。主担当と別担当で適用する圏と始域の有限性を照合した。

従って、前層圏で一本の s:U→V による OFS の反例を探すなら、今回までの十分条件から少なくとも次が必要になる：s が非 mono、V が非 subterminal、U の少なくとも一成分が無限。これらは必要条件にすぎず、満たせば反例になるという主張ではない。
