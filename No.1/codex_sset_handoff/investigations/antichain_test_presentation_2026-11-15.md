# 反鎖型のテスト集合表示と商による判定

2026年11月15日。Quiv の rigid な真のクラス G から作った C=Quot Coprod(G∪{1}) が、射の集合 S に対する I_S になるかを調べる。直接証明の状態は `PROOF_RECONSTRUCTED`。独立査読・形式検証・新規性確認は未実施。

**結論は部分的である。** 表示可能性を、ある固定サイズ以下の商だけで C への所属を判定できることと同値にした。また、supercompact cardinal が真のクラス存在する場合、非 well-powered なこの C はいかなる I_S にもならない。これらの巨大基数が存在しない側での表示の存在・不存在は、まだ決定できていない。

## 1 否定側の集合論的仮定を修正する

Q を「supercompact cardinal が真のクラス存在する」とする。確認済みの含意は

\[
\mathrm{VP}\Longrightarrow Q\Longrightarrow P,
\qquad
\neg P\Longrightarrow\neg Q\Longrightarrow\neg\mathrm{VP}.
\]

Q⇒P の証明は [肯定側の監査 §2–4](../audits/set_theoretic_upper_bound.md)。VP⇒Q および Q の定義可能性階層での位置は BCMR, Corollary 5.4 による。[一次資料](https://arxiv.org/html/1101.2792v4)

従って、¬VP を使って非 well-powered な部分圏を得たことだけを、¬P の証明へ進める根拠にはできない。少なくとも ¬Q、すなわち supercompact cardinal がある順序数より上には存在しない側を扱う必要がある。これは supercompact cardinal が一つもないという仮定より弱い。

ユーザーから、この否定条件の強さについて指摘があった。以後、反鎖型の存在に使う ¬VP と、I_S 表示を狙う際に必要な ¬Q を分けて扱う。¬Q から ¬P、あるいは ¬Q から今回の表示の存在を結論したわけではない。

この図には WVP を入れていない。「WVP より弱い仮定から P が従う」という結果は、本研究では確認していない。Bagaria–Wilson は WVP の整合性強度が一つの supercompact cardinal の存在より低いことを説明しており、Q と WVP の比較を逆向きに扱うことはできない。また、整合性強度と同じ宇宙内の論理的含意は区別する。[一次資料 §1](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/weak-vopenka-principle-for-definable-classes-of-structures/B95D82A33C8D715E042F24CE73CF2361)

## 2 反鎖型に固有の性質

前段階と同じく、G は非空・ループなしの関係グラフの真のクラスであり、異なる二対象間には射がなく、各自己射は恒等射だけとする。関係グラフを Quiv に充満埋め込みし、商と余積は Quiv で計算する。クラスは定義可能なものとして扱い、集合を添字とする余積だけを取る。

C の coreflector を R、counit を c_B:R(B)↪B と書く。[構成と証明](presheaf_non_wellpowered_2026-11-15.md)

### 2.1 真の部分グラフはすべて排除される

**補題。** G∈G と真の部分 quiver F⊊G に対して、R(F)=0 である。特に G の非空の C-部分 quiver は G 自身だけである。

**証明。** 1→F はループがないため存在しない。H∈G から F への射があれば、包含との合成 H→G が得られる。rigid 性により H=G で合成は id_G でなければならないが、真の部分 quiver への因子化は不可能である。従って、どの生成対象からも F に射がない。

非空 A∈C から F への射があれば、A の表示 ∐H_j↠A に前合成して、ある非空生成対象 H_j から F への射が得られて矛盾する。従って F の非空 C-部分対象は存在せず、R(F)=0。∎

これは母圏 Quiv の部分対象についての主張である。G→1 が内部単射になるという、前段階の主張とは区別する。

### 2.2 積の coreflection も明示できる

**補題。** G,H∈G に対し

\[
R(G\times H)=
\begin{cases}
0 & G\ne H,\\
\Delta G\subseteq G\times G & G=H.
\end{cases}
\]

**証明。** 各生成対象から積への射を二つの射影で調べる。G≠H の場合、両方へ写る生成対象はない。G=H の場合、写る生成対象は G だけで、その射は (id_G,id_G) である。1 からはループがないため写らない。生成対象の像の和が R の値になるので、式を得る。∎

## 3 小さいテストでの不合格は小さい商に残る

ここではまず S={f_i:U_i→V_i} を Quiv の射の任意の集合とする。無限基数 κ を、すべての |U_i|=|V(U_i)|+|E(U_i)| が κ 以下になるように選ぶ。終域 V_i のサイズ上界は不要である。

**補題。**

\[
X\notin\mathcal I_S
\Longrightarrow
\exists(q:X\twoheadrightarrow Z)\;
\bigl(|Z|\le\kappa\ \land\ Z\notin\mathcal I_S\bigr).
\]

**証明。** 不合格を証言する i と異なる二射 g,h:X→U_i を取り、f_i g=f_i h とする。kernel pair P_i=U_i×_{V_i}U_i への射 (g,h) の像を取って

\[
X\overset{q}{\twoheadrightarrow}Z\hookrightarrow P_i
\]

と分解する。Quiv では像と kernel pair を各集合で計算できるため |Z|≤|P_i|≤κ。二つの射影 Z→U_i は異なる。等しければ g=h となるからである。その f_i との合成は等しいので Z∉I_S。∎

逆に、I_S は頂点・辺ごとの全射商に閉じる。従って

\[
\boxed{X\in\mathcal I_S
\quad\Longleftrightarrow\quad
\text{X のサイズ }\le\kappa\text{ の全射商がすべて }\mathcal I_S\text{ に属する}.}
\]

対象 X の小さい**部分グラフ**による判定ではなく、小さい**商**による判定である。この違いが §2.1 の最小性から直ちに非表示を結論できない理由でもある。

## 4 逆向きも成り立つ

この節では C を Quiv の任意の monocoreflective な充満・同型閉部分圏とし、R をその coreflector とする。

C は全射商に閉じる。実際、A∈C からの全射 A↠Z は counit c_Z を経由するため、c_Z 自身が全射かつ単射となり、Z∈C である。

κ を無限基数とし、サイズ ≤κ の quiver の同型類の代表集合 K_κ を選ぶ。その各 Z について単射 c_Z:R(Z)↪Z と fold

\[
d_Z:Z\amalg_{R(Z)}Z\longrightarrow Z
\]

を取り、S_κ={d_Z:Z∈K_κ} と置く。これは集合であり、各始域のサイズも ≤κ である。

\[
\mathcal C_\kappa:={}^\perp\{c_Z:Z\in K_\kappa\}
=\mathcal I_{S_\kappa}.
\]

最後の等式は [単射と fold の同値性 §5.2](presheaf_non_wellpowered_2026-11-15.md) による。

**補題。** C_κ は、サイズ ≤κ の全射商がすべて C に属する対象のクラスである。

**証明。** X∈C_κ なら、全射商 q:X↠Z、|Z|≤κ は c_Z を経由する。全射性から c_Z も全射なので同型であり、Z∈C。

逆にその商条件を仮定し、h:X→Z、|Z|≤κ を取る。h の像 W は X のサイズ ≤κ の全射商だから C に属する。W→Z は coreflection c_Z を経由するので、h も経由する。c_Z は単射だから因子化は一意であり、X∈C_κ。∎

§3 と合わせて次を得る。

**定理。** Quiv の monocoreflective な充満部分圏 C について、次は同値である。

1. ある射の集合 S に対して C=I_S。
2. ある無限基数 κ に対して C=C_κ。
3. ある無限基数 κ に対して、C に属さない任意の X は、サイズ ≤κ の C に属さない全射商を持つ。

常に C⊆C_κ であり、κ≤λ なら C_λ⊆C_κ。また、すべての κ にわたる共通部分は C になる。X∉C なら |X|≤κ となる κ を選ぶと、恒等商 X↠X が不合格を検出するためである。さらに |X|≤κ の対象については、C_κ と C の所属は一致する。

従って、反鎖型の非表示を証明するには、**すべての κ に対して**

\[
X_\kappa\notin\mathcal C,
\qquad
\text{サイズ }\le\kappa\text{ のすべての商 }Z\text{ は }\mathcal C\text{ に属する}
\]

という例を作れば十分であり、必要でもある。反対に一つの κ でこの種の例が存在しないと証明できれば、上の S_κ が所望のテスト集合を具体的に与える。

## 5 Supercompact cardinal による表示の障害

### 5.1 テストのパラメータより上に一つあれば排除される

**命題。** 反鎖型の C が C=I_S と表示されると仮定する。Quiv の署名と S のランクより上に supercompact cardinal があってはならない。

**証明。** そのような supercompact cardinal λ を仮定する。I_S は、Quiv の構造と S をパラメータとする Π₁、従って Σ₂ の充満部分圏である。

G∈G を |G|≥λ となるように選ぶ。互いに非同型なグラフの真のクラスなので、この選択が可能である。G は辺を持つ。辺なしで二頂点以上なら非恒等自己射があり、一頂点・辺なしのグラフなら他の非空グラフへの射があるため、rigid な真のクラスには属せないからである。二頂点・一辺の quiver P_e から G へ、その辺を指定する射 a:P_e→G を取る。

BCMR, Theorem 5.2(a) を I_S に適用すると、a は、ある Y∈I_S∩V_λ と elementary embedding e:Y→G を通る。特に Y は非空で、e は頂点・辺の両方で単射である。[一次資料 Theorem 5.2](https://arxiv.org/html/1101.2792v4)

C=I_S なので、その像 e[Y] は G の非空 C-部分 quiver である。§2.1 により e[Y]=G となり、e は同型である。しかし |Y|<λ≤|G| に矛盾する。∎

### 5.2 Q の下での非表示

**系。** Q が成り立ち、反鎖型 C が与えられているなら、どの集合 S に対しても C≠I_S。従ってすべての κ に対し C⊊C_κ である。

任意の S のパラメータより上に supercompact cardinal を取れるので、前命題から従う。これは前段階で示した「Q の下ではすべての I_S が well-powered」と C の非 well-poweredness からも従う。

この系は Q と反鎖型 C の存在を仮定した条件付きの主張である。ここでは、それらを同時に満たすモデルの新しい構成や整合性証明は行っていない。

Q の下では C_κ は well-powered なので、すべての G∈G が C_κ 内で subterminal のままでいることはできない。従って、ある G に対して

\[
R_{\mathcal C_\kappa}(G\times G)\supsetneqq\Delta G
\]

となる。左辺を Z とすると Z∈C_κ だが Z∉C である。後者は §2.2 の R_C(G×G)=ΔG から従う。これにより、Q の下で生じる余分な対象の場所を、ある G の二乗の部分 quiver にまで絞れる。

## 6 C_κ の coreflector を構成する手順

固定 B に対し B_0=B とし、次を繰り返す。

\[
B_{\alpha+1}=
\bigcap_{Z\in K_\kappa}\ \bigcap_{h:B_\alpha\to Z}
h^{-1}(R(Z)),
\qquad
B_\delta=\bigcap_{\alpha<\delta}B_\alpha
\quad(\delta\text{ は極限}).
\]

各段階の添字は集合であり、部分 quiver の交わりを取っている。一度等号 B_{α+1}=B_α が起これば、その後は変わらない。真に減る段階では頂点または辺が少なくとも一つ失われるので、μ=max(ℵ₀,|B|) とすれば μ⁺ より前に安定する。

安定値は C_κ に属する。一方、B の任意の C_κ-部分 quiver は、超限帰納法によって全段階 B_α に含まれる。従って安定値は R_{C_κ}(B) である。

これは集合論内の構成であり、無限グラフに対する有限時間のアルゴリズムを与えたものではない。また一段階だけの交わりを coreflection と同一視してはいけない。

## 7 現在の判定と残った作業

今回確定したのは、テスト集合表示と小さい商による一様判定の同値性、および Q の下での反鎖型の非表示である。¬Q の下で C=C_κ となる κ が存在するかは未決定である。

独立性に向けては、以後少なくとも ¬Q を明示した上で、次の二方向を区別して調べる。

- 表示を作る方向：固定した κ について、任意の X∉C からサイズ ≤κ の C 外の商を取り出す。成功すれば S_κ を得る。
- 表示を否定する方向：各 κ に対して C_κ\C の対象を作る。§2.2 の積や §6 の G×G の coreflection が候補になるが、¬Q の下で常に対角より大きくなるという証明はまだない。

表示が得られても、C 自身は coreflective である。S_κ の fold は split epi なので A_{S_κ}=I_{S_κ}=C となる。従って、ここから ¬P を得るには、同じ一意性部分圏の内部で、別の固定テストと標的による解集合条件の失敗を示す必要がある。

境界条件として、空テスト集合、空 quiver、全射の頂点・辺両方の条件、恒等商、商と部分対象の区別、超限反復の安定性を点検した。C=Quiv ではすべての κ で C=C_κ、C={0} では無限 κ に対して一頂点の商で非空対象を検出でき、同じ特徴付けと整合する。有限計算から真のクラスについての結論を推論していない。
