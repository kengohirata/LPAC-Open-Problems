# Ab / Grp における small coorthogonality：還元と除外結果

2026-11-15

## 状態

このノートは Problem 1 の反例や ZFC 独立性の証明ではない。以下の還元・肯定的結果は、その場で確認した直接証明を記すものであり、新規性は主張しない。文献で確認した事実は末尾に区別して挙げる。

圏 K と射の集合 S に対し、A_S は Hom_K(X,f) がすべての f in S について全単射となる X の充満・同型閉部分圏とする。P_K は、すべての集合 S について A_S が coreflective であるという主張。

## 1. 一本のテスト射への還元

K を Ab または Grp とし、S={f_i:U_i -> V_i | i in I} とする。積の射

f = product_i f_i : product_i U_i -> product_i V_i

について A_S=A_{f} である。

証明：Hom(X,f)=product_i Hom(X,f_i)。各 Hom 集合には零写像／自明準同型がある。成分写像がすべて全単射なら積も全単射。逆に積が全単射なら、一成分以外を零写像にして、各成分の全射性・単射性を回復できる。空集合の場合も f=id_0（Grp では id_1）として成り立つ。

注意：これは今回の pointed な圏についての還元。空 Hom 集合のあり得る任意の圏に、理由なく一般化してはいけない。

## 2. 商閉性による肯定結果

Ab または Grp の充満・同型閉部分圏 T が小余積と商対象に閉じていれば、T は coreflective である。

証明：B の T に属する部分群全体は集合。その和（Grp では生成する部分群）t(B) を取る。これはそれらの余積の商なので T に属する。任意の T-object A から B への射は、その像が T に属するため t(B) を一意に経由する。

各テスト射が mono または split epi であるとき、A_S は商閉である。mono の場合は、A ->> Q と Q -> V を取り、A 上での持ち上げが quotient の kernel を殺すことを mono 性から確認する。split epi の場合には section が存在を保証し、一意性は A ->> Q に沿って下降する。

また任意の f:U -> V を U ->> im(f) -> V と分解すると、A_f は二つの因子への coorthogonality class の共通部分である。Hom(X, im(f) -> V) が単射だからである。

注意：この事実だけで mono 側を捨ててよいわけではない。二つの coreflective な部分圏の共通部分が一般に coreflective であるとは、この議論では示していない。

## 3. Ab：torsionless な始域は除外できる

torsionless とは、U がある整数群の直積 Z^J に埋め込めることとする。torsion-free より強い条件である。

**命題。** U が torsionless なら、任意の f:U -> V について A_f は coreflective。

f が mono なら第2節による。そうでないとき K=ker(f) は非零 torsion-free 群なので Z を部分群として含む。A in A_f なら Hom(A,K)=0、従って Hom(A,Z)=0。埋め込み U -> Z^J より Hom(A,U)=0。従って

A_f = { A | Hom(A,Z)=0 かつ Hom(A,V)=0 }.

右辺は直和と商に閉じるので第2節が適用できる。

特に任意の自由アーベル群、整数群の任意の直積、その任意の部分群を始域とするテスト射は反例を与えない。torsionless 群の積は torsionless なので、そのような始域の射の集合も一本化によって除外できる。

## 4. Ab：Hom と Ext の同時消滅類の分類

任意のアーベル群 K に対して

W_K = { A | Hom(A,K)=0, Ext^1(A,K)=0 }

と置く。

### 4.1 閉性

K を可除群 I に埋め込み q:I -> I/K を取る。I は injective なので、長完全列から W_K=A_q。従って W_K はすべての小余極限と retract に閉じる。

W_K は拡大にも閉じる。これは Hom と Ext の長完全列による。

さらに W_K は、その内部の射の kernel に閉じる。a:A -> B を W_K 内の射とし、L=ker(a), J=im(a), D=coker(a) と置く。余極限閉性より D in W_K。短完全列 0 -> J -> B -> D -> 0 と Ext^2(-,K)=0 から J in W_K。次いで 0 -> L -> A -> J -> 0 から L in W_K。

ここで Ext^2_Z=0 は、自由アーベル群の部分群が自由であることから従う。

### 4.2 必要な初等分類補題

**補題。** Ab の非空な充満・同型閉部分圏 W が、すべての小余極限、内部の射の kernel、拡大に閉じるとする。すると W は次のいずれか。

(a) ある素数集合 J に対する J-primary torsion groups 全体。

(b) ある素数集合 T に対する R=Z[T^{-1}] の加群全体（Ab の充満部分圏として）。

証明：J={p prime | Z/p in W} と置く。W は retract に閉じる。

W に非 torsion 群 A があれば、rationalization A tensor Q は W に属する。これは A に整数倍射を繰り返して作る filtered colimit だからである。非零 Q-vector space の直和因子として Q in W。

まず Q notin W の場合、W の対象はすべて torsion。A に p-torsion があれば、kernel(A --p--> A)=A[p] が W に属し、その直和因子 Z/p も W に属する。従って A は J-primary torsion。一方、Z/p から拡大で有限 p-groups、filtered colimit で全 p-groups、直和で全 J-primary torsion groups を作れる。これで (a)。

次に Q in W の場合、p notin J なら各 A in W における p:A -> A の kernel と cokernel は零でなければならない。そうでなければ非零 F_p-vector space から Z/p を retract として得るためである。従って W は R=Z[p^{-1} | p notin J] の加群の中に含まれる。

p in J に対し Prüfer p-group Z(p^infinity) は W に属する。よって短完全列

0 -> R -> Q -> direct_sum_{p in J} Z(p^infinity) -> 0

の右二項は W に属する。その kernel として R in W。任意の R-module は R の直和間の射の cokernel であるから W に属する。これで (b)。証明終わり。

(a) の coreflector は J-primary torsion subgroup。
(b) の coreflector は Hom_Z(R,B) で、R-action は (r phi)(x)=phi(rx)、counit は phi -> phi(1)。

**帰結。** W_K はすべて ZFC で coreflective。したがって Hom(-,K) と Ext^1(-,K) を両方零にする形だけでは Ab の反例にならない。

## 5. Ab：可除な始域も除外できる

**命題。** U が可除なら、任意の f:U -> V について A_f は coreflective。

I=im(f), K=ker(f) とする。I は可除であるため injective で、包含 I -> V は分裂する。C=V/I とすれば V は I direct_sum C と同型である。

e:U ->> I について、U が injective なので

A_e = W_K.

従って

A_f = W_K intersection { A | Hom(A,C)=0 }.

第4節により W_K は J-primary torsion groups または R-modules。

前者なら A_f は Ab 内で直和と商に閉じるため coreflective。

後者なら A_f は R-Mod 内で直和と商に閉じるため R-Mod 内で coreflective。R-Mod -> Ab 自体も右随伴 Hom_Z(R,-) を持つため、包含の合成も右随伴を持つ。

可除群の積は可除なので、可除な始域を持つ任意の集合個のテスト射にも成り立つ。

さらに、各射の始域が「torsionless または可除」のどちらかである集合 S も除外できる。torsionless 側の条件は商閉・直和閉な部分圏を与え、可除側は W_K と商閉・直和閉な条件の共通部分にまとめられる。第4節の二つの場合に分け、同じ内部 trace の議論を適用すればよい。

### 5.1 任意の torsion な始域も除外できる

**命題。** U が torsion 群なら、任意の f:U -> V について A_f は coreflective。

K=ker(f) とし、P={p prime | K[p] != 0} と置く。U の p-primary component を U_p、その最大可除部分群を D_p とする。

A in A_f なら Hom(A,K)=0。p in P について K は Z/p を含むため Hom(A,Z/p)=0、従って A=pA である。

A がこれらすべての p について p-divisible なら、A -> U_p の像も p-divisible であり、p-primary 群の p-divisible 部分群は可除なので、像は D_p に含まれる。従って A -> U のすべての射は

U' = D direct_sum U_0,
D = direct_sum_{p in P} D_p,
U_0 = direct_sum_{q notin P} U_q

を一意に経由する。

I=f(D) は可除で、torsion の素数は P に属する。I は injective なので V=I direct_sum V' と分解できる。U_0 の素数は P の外にあるため、任意の射 U_0 -> I は零。従って f(U_0) は V' に含まれる。また K に P 以外の torsion はないので m=f|_{U_0}:U_0 -> V' は mono。

e=f|_D:D ->> I とすれば、f|_{U'} は e direct_sum m であり、D は可除。従って

A_f = W_{ker(e)} intersection {A | A=pA for all p in P} intersection A_m.

第二・第三の条件は直和と商に閉じる。第4節の W の分類を使い、torsion class の場合は Ab 内の trace、R-Mod の場合は R-Mod 内の trace とその右随伴を合成すれば、coreflection が得られる。

この議論は各 torsion-source test を「可除群を始域とする全射への coorthogonality」と「商・直和に閉じる条件」に変換する。可除群始域の射は集合個でも積で一本化できるので、torsion-source tests の集合にも適用できる。

より一般に、各テスト射の始域が torsionless・可除・torsion のいずれかである集合 S はすべて除外できる。これは三種の群の任意の直和を始域としてよいという主張ではない。各射の始域ごとに三条件のいずれかを満たす、という意味である。

## 6. Whitehead 群の候補の訂正

f:Q -> Q/Z について

A_f = { A | Hom(A,Z)=0, Ext^1(A,Z)=0 }.

非零 Whitehead 群は separable で、Hom(A,Z) は非零である。この事実は Eklof–Shelah の論文 [1] p.200 に明記されている。

従って A_f={0} は V=L を仮定せず ZFC で成り立つ。

なお Grp で同じ射を使うと、Hom(G,Q) と Hom(G,Q/Z) は G_ab だけに依存するから、A_f は perfect groups 全体になる。こちらも coreflective。coreflector は transfinite derived series の安定値：

D^0(G)=G,
D^{alpha+1}(G)=[D^alpha(G),D^alpha(G)],
D^lambda(G)=intersection_{alpha<lambda} D^alpha(G).

部分群の全体は集合なので列は停止する。安定値は perfect であり、任意の perfect group から G への射は全段階の部分群を経由する。

## 7. Ab の反例は同じ射で Grp に移る

S をアーベル群間の射の集合とし、

A = A_S in Ab,
C = A_S in Grp

と置く。

C={ G | G_ab in A }.

**命題。** 任意のアーベル群 B について、B の A-coreflection が Ab に存在することと、B の C-coreflection が Grp に存在することは同値。

Ab -> Grp の方向：r:R -> B が A-coreflection なら、任意の G in C について

Hom_Grp(G,R)=Hom_Ab(G_ab,R) -> Hom_Ab(G_ab,B)=Hom_Grp(G,B)

が全単射。よって同じ r が C-coreflection。

Grp -> Ab の方向：r:R -> B が C-coreflection とする。任意の x in R の内部自己同型 c_x に対し、B が abelian なので r c_x=r。R in C と universal uniqueness より c_x=id。よって R は abelian。従って R in A であり、r は Ab における A-coreflection。

**帰結。** P_Grp implies P_Ab。同値性の逆方向は主張しない。Ab の非 coreflective な small coorthogonality class の証人 (S,B) は、そのまま Grp の証人になる。

## 8. Grp：中心拡大への正確な還元

任意の f:U -> V に対して

N=ker(f),
C=C_U(N),
I=f(C)

と置く。自然な射を

j:C -> U,
e:C ->> I,
m:I -> V

とする。j,m は mono であり、ker(e)=Z(N) は C の中心に含まれる。従って e は中心拡大。

**命題。** A_f=A_{j,e,m}。

証明：A in A_f とする。任意の u:A -> U と n in N について f c_n u=f u。持ち上げの一意性から c_n u=u。従って u(A) は C に含まれ、Hom(A,j) は全単射。

f j=m e なので Hom(A,m e) も全単射。m が mono であるため Hom(A,e), Hom(A,m) がそれぞれ全単射。

逆に j,e,m すべてへの coorthogonality があれば、f j=m e と Hom(A,j) の全単射性から Hom(A,f) も全単射。

**帰結1。** Z(ker(f))=1 なら e は同型で、A_f は二つの mono への coorthogonality class。従って商閉で coreflective。

この主張は集合個の f のそれぞれに適用できる。

**帰結2。** 一般の Grp の探索では、中心拡大に還元したとき非分裂となる場合が残る。mono 条件 j,m を勝手に捨ててはいけない。

中心拡大 1 -> K -> E -> V -> 1 に対し、任意の A -> V が持ち上がるなら、その持ち上げの集合は Hom(A,K) による torsor である。従って unique lifting は、全 pullback extension が分裂することと Hom(A,K)=1 の組合せである。

## 9. Grp：自由群を始域とするテストも除外

U を自由群とし f:U -> V を取る。mono の場合は第2節。

非 mono の場合、N=ker(f) は非零の torsion-free 群なので無限巡回群 Z を含む。A in A_f なら Hom(A,Z)=1。

任意の非自明な準同型 A -> U があれば、その像 H は Nielsen–Schreier により非自明な自由群。H ->> Z が存在し、合成 A -> Z が非自明となる。矛盾。

従って

A_f={ A | Hom(A,Z)=1, Hom(A,V)=1 }.

右辺は自由積と商に閉じ、coreflective。

同じ議論は、U が自由群の直積に埋め込める場合にも成立する。各座標への射がすべて自明になるためである。

## 10. 残る Ab の障害：特定の拡大類だけを消す条件

e:U ->> V, K=ker(e) とし、短完全列の拡大類を xi in Ext^1(V,K) とする。長完全列より

A in A_e
iff Hom(A,K)=0 かつ、すべての h:A -> V に対して h^*xi=0.

第二条件は Ext^1(A,K) の全体の消滅ではない。

従って、U が injective でない場合に Ext^1(A,K)=0 へ置き換えてはいけない。第4節によって、後者に強めてしまうと反例候補がすべて coreflective なクラスへ移ってしまう。

正確には

W_K subseteq A_e subseteq { A | Hom(A,K)=0 }.

両端は coreflective だが、中間の A_e に対してはこの議論だけでは結論できない。

一般の f にはさらに im(f) -> V への mono 条件を残す。

Ab の A_f は自動的に直和・cokernel に閉じる。従って [2], Corollary 7.2 により、coreflectivity は precovering 性と同値。否定側には、固定した f と B に対して、任意の a:A -> B (A in A_f) を経由しない a':A' -> B (A' in A_f) を構成する必要がある。

## 11. 大きな cellular covers：使える事実と残る問題

[3], Theorem 2.11 は、固定したアーベル群 M に対して任意に大きい核を持つ cellular covers c:G ->> M が存在する例を ZFC で与える。

ここで cellular cover は Hom(G,c):End(G) -> Hom(G,M) が全単射という意味。これは一つの G によるテストであり、固定した f による A_f 全体に対する coreflection とは異なる。

大きな cellular covers の存在だけから P_Ab の否定は導けない。すべての c:G -> M は Ab 全体の恒等 coreflection id_M を経由するという単純な例からも、大きさだけでは障害にならないと分かる。

さらに、f 自体が cellular cover c:G -> M なら、G in A_f であり、定義により c は M の A_f-coreflection である。従って cellular cover 自体をテスト射に選び、その同じ終域 M を非存在の証人にすることはできない。

この文献を使うには、固定した別のテスト射 f のもとで、A_f 内に属する射たちの非因子分解性を証明する追加の構成が必要。

## 12. 到達点

反例または独立性モデルは構成できていない。

一方、次を得た。

- Ab と Grp では集合個のテストを一本にまとめられる。
- Ab の反例は、同じテストとアーベルな標的を用いて Grp に移る。
- Ab では torsionless な始域、可除な始域、torsion な始域、およびこれらのテスト射を混ぜた集合を除外できる。
- Ab の Hom(-,K)=Ext^1(-,K)=0 型はすべて coreflective。
- Whitehead の Q -> Q/Z 案は ZFC で零群（Grp では perfect groups）に退化。
- Grp の一般の射は中心拡大と二つの mono へ還元でき、centerless kernel や自由群始域は除外できる。
- 残る代数的課題は、非可除・非 torsionless・非 torsion な始域の非分裂拡大において、特定の拡大類の pullback 消滅条件と Hom 消滅条件を組み合わせたクラスの precovering 性。

## 文献

[1] P. C. Eklof, S. Shelah, A non-reflexive Whitehead group, Journal of Pure and Applied Algebra 156 (2001), 199–214. p.200.
https://shelah.logic.at/files/95759/621.pdf

[2] M. Cortés-Izurdiaga, S. Crivei, M. Saorín, Reflective and coreflective subcategories. Corollary 7.2.
https://arxiv.org/abs/2109.05111

[3] E. D. Farjoun, R. Göbel, Y. Segev, S. Shelah, On kernels of cellular covers, Groups, Geometry, and Dynamics 1 (2007), 409–419. Theorem 2.11.
https://arxiv.org/abs/math/0702294

[4] S. Estrada, J. L. Rodríguez, Envelopes and covers for groups, Groups, Geometry, and Dynamics 12 (2018), 107–120. Theorem 3.1 における conjugation argument も関連する。
https://ems.press/content/serial-article-files/29859

[5] The Stacks Project, Injective abelian groups, Tag 01D6.
https://stacks.math.columbia.edu/tag/01D6

[6] The Stacks Project, Ext groups, Tag 00LO.
https://stacks.math.columbia.edu/tag/00LO

[7] A. J. Przeździecki, An almost full embedding of the category of graphs into the category of abelian groups.
https://arxiv.org/abs/1104.5689
同論文の通常の orthogonality に関する移送を、このノートでは small coorthogonality の非 coreflectivity に転用していない。

[8] mathlib, Nielsen–Schreier theorem (formal proof).
https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FreeGroup/NielsenSchreier.html
