# Quiv / Graph における small coorthogonality：還元と除外結果

## 状態

本ノートは会話中に組み立てた直接証明をまとめた研究用の作業ノートである。以下の個別定理を同じ形で文献から発見した、という主張ではない。Quiv 全体における Problem 1 の肯定・否定、また ZFC 独立性は、ここでは結論していない。

射の集合 S に対し A_S = {}^⊥S は、各 f:U→V∈S に対して Hom(X,U)→Hom(X,V) が全単射である対象 X の充満部分圏を表す。

使用する母圏：

- Quiv：頂点集合 X_v、辺集合 X_e、source/target X_e⇉X_v。ループ・平行辺を許す。
- Dig：集合に二項関係を与えた有向グラフ。平行辺なし、ループは許す。
- UGraph：対称二項関係を与えた無向グラフ。ループは許す。

これらは locally finitely presentable。ループを禁止したグラフの圏そのものは終対象を持たず、locally presentable ではない。ループなし対象を使う場合も、上記の母圏で問題を考える。

## 0. 一般補題

### 補題 0.1：単射への coorthogonality

locally presentable category K の単射の集合 M に対し、{}^⊥M は monocoreflective である。

証明：coorthogonality class は小余極限に閉じる。また C∈{}^⊥M と strong epi C↠D に対し、任意の単射 m:U↪V∈M と射 D→V を考える。C での一意な持ち上げと strong-epi/mono の lifting により、D でも持ち上がり、一意性は m が mono であることから従う。したがって strong quotient に閉じる。固定した B に対し、domain が {}^⊥M に属する B の subobject を集合個集め、その余積の B への strong image を取る。これが coreflection となる。

### 補題 0.2：局所可呈示な中間部分圏と単射条件

L⊂K が locally presentable な余極限閉充満部分圏で、包含 J の右随伴を R とする。単射の集合 M に対し L∩{}^⊥_K M は K において coreflective。

実際、L 内では {}^⊥_L{Rm:m∈M} であり、右随伴は単射を保存する。補題 0.1 を L 内で適用し、二つの coreflection を合成する。

### 補題 0.3：像分解

f = m e、m が mono なら、

    {}^⊥{f} = {}^⊥{e,m}.

Hom(X,m) が単射なので、Hom(X,m)Hom(X,e) の全単射性から両因子の全単射性が従う。

## 1. 頂点側が単射なら、平行辺の複雑さは反例を生まない

### 定理 1

Quiv の f:U→V で f_v が単射なら、{}^⊥{f} はある mono j:V_good↪V の coorthogonality class と一致する。

V_good の頂点は f_v[U_v]。辺は、f_e による逆像がちょうど一本である V の辺とする。

頂点の持ち上げは存在すれば一意である。したがって h:X→V の持ち上げがちょうど一つ存在することは、各頂点が f_v[U_v] に入り、各辺の逆像がちょうど一本であることと同値。辺ごとの選択は独立なので、これは h が V_good を経由することと同値である。

従って {}^⊥{f}={}^⊥{j}。集合個の vertex-injective な射にも同時に適用でき、coreflective となる。

## 2. 辺側が単射な射の集合にも、ZFC の肯定結果がある

### 定理 2

Quiv、Dig、UGraph のいずれでも、各 f_i∈S が辺側で単射なら {}^⊥S は coreflective。

UGraph の「辺」は対称二項関係の順序付き組として数える。特に、ループへ潰す写像について、通常の無向辺の集合への単射性と混同しないこと。

### 証明

C を「孤立頂点のない対象」の充満部分圏とする。零対象ではなく初対象である空グラフも C に含める。

C は小余極限に閉じる。各対象は有限な孤立点なし部分グラフの directed union であり、有限対象は母圏で finitely presentable なので、C は locally finitely presentable である。包含の右随伴 N は孤立頂点を除く操作。

C 内では、辺側が単射な射は mono である。実際、C の対象からの二射は、辺上で等しければ、その端点であるすべての頂点でも等しい。

従って

    A_0 = C ∩ {}^⊥S = {}^⊥_C {Nf_i}

は C で monocoreflective である。

固定した B に対し二つの場合に分ける。

**場合 I**：A={}^⊥S の対象から B への射に、孤立頂点を持つ domain のものが存在しない。

この場合 A↓B と A_0↓B は同じなので、N(B) の A_0-coreflection を B に合成すればよい。

**場合 II**：孤立頂点を持つ A∈A と a:A→B が存在する。

S_good を頂点側が全単射な f_i の族、S_bad をそれ以外とする。S_good の射は頂点・辺の双方で単射なので母圏の mono である。

各 i∈S_bad に対して Hom(A,V_i)=∅ でなければならない。もし非空なら、A の孤立頂点を一つ分離して A=1_disc⊔A' と書くと、Hom(A,f_i) は二つの集合写像の積であり、その終域は非空である。その積が全単射なので、第一因子

    Hom(1_disc,f_i) = (f_i)_v

も全単射となって矛盾する。

D={}^⊥S_good は補題 0.1 により coreflective。B の D-coreflection を d:D_B→B とする。A∈D なので a は D_B を経由する。従って D_B→V_i（i∈S_bad）が存在すれば A→V_i が存在して矛盾する。

よって Hom(D_B,V_i)=Hom(D_B,U_i)=∅。D_B は bad な条件も満たし、D_B∈A である。D の普遍性はそのまま A の普遍性となる。∎

### 系 2.1：どちらか一方の sort が単射ならよい

Quiv の各 f_i について、頂点側か辺側の少なくとも一方が単射なら {}^⊥S は coreflective。頂点側単射の射を定理 1 で mono に置き換えれば、すべて辺側単射にできる。

従って、反例の射の集合には、頂点と辺の両方を同一視する射が少なくとも一本必要である。

### サイズについて

定理 2 の場合 I の counit は C 内の mono なので辺上で単射。coreflection の辺数は |B_e| 以下、頂点数は 2|B_e| 以下である。場合 II では母圏の subobject である。したがって、この結果は単なる存在以上のサイズ制御を与える。

## 3. 始域の頂点数が有限なら、終域は無限でもよい

### 定理 3

Quiv の各 f_i:U_i→V_i の U_i の頂点数が有限なら、{}^⊥S は coreflective。U_i の辺数、V_i の頂点数・辺数には制限しない。

### 3.1 有限個の頂点を持つ二つの quiver 間の射の圧縮

まず e:U→I で U_v、I_v が有限とする。

I の辺 d:v→w に対して、U_v×U_v 上の行列

    p_d(a,b) = min(2, #{c∈U_e : s(c)=a, t(c)=b, e(c)=d})

を取る。成分は 0,1,2 の三種類で、2 は「二本以上」を表す。始点・終点 (v,w) とこの行列の組は有限種類しかない。

I の各辺をこの有限種類に置き換えた有限 quiver I_bar を作る。U_bar は U と同じ頂点を持ち、各行列・各対 (a,b) に対して 0,1,2 本の辺を作る。これにより有限 quiver 間の射 e_bar:U_bar→I_bar が得られる。

固定した h:X→I の持ち上げについて、まず頂点の像を選び、その後、各辺の逆像を選ぶ。持ち上げが「存在しない／ちょうど一つ／二つ以上」のどれであるかは、各逆像の濃度そのものではなく、0,1,2+ の区別だけで決まる。

また、X→I_bar の各辺型は、I 内の代表辺を選んで実現できる。従って、任意の X に対して

    X⊥e  iff  X⊥e_bar.

ここで主張するのは coorthogonality class の一致であり、Hom 集合そのものの同型ではない。

### 3.2 有限テストの直交類は locally presentable

有限 quiver 間の射の集合 T に対する {}^⊥T は locally aleph_1-presentable。

任意の可算部分集合を含む可算 pure subquiver Y⊂X が取れる。有限 quiver D への Y からの射は、有限離散集合の積の compactness により X へ延長できる。T の各終域 V と kernel pair U×_V U が有限なので、X∈{}^⊥T なら Y も属する。存在は V への延長、一意性は kernel pair への延長から従う。

従って各 X は可算な同類の部分対象の aleph_1-directed union である。可算 quiver は aleph_1-presentable であり、この部分圏はすべての小余極限に閉じるため、主張が従う。

### 3.3 一般の終域へ戻す

各 f_i を strong-image 分解

    U_i --e_i↠ I_i --m_i↪ V_i

する。I_i の頂点数も有限。3.1 により e_i を有限テスト e_bar_i に置き換えられる。

L={}^⊥{e_i} は 3.2 により locally presentable かつ余極限閉。残る m_i は mono なので、補題 0.2 により

    {}^⊥S = L ∩ {}^⊥{m_i}

は coreflective。∎

Dig と UGraph では、有限頂点の対象は既に有限グラフなので、行列圧縮なしで同じ結論が得られる。

## 4. 局所有限なテスト対象も除外できる

ここで「局所有限」とは、各頂点に接する辺が有限個という意味。Quiv では入辺・出辺・平行辺をすべて含めて有限とする。

### 定理 4

S の各 f_i:U_i→V_i の U_i,V_i が局所有限なら、{}^⊥S は locally presentable、従って coreflective。

### 4.1 一点を固定した compactness

D を局所有限とし、C を連結グラフ、c∈C_v、d∈D_v とする。c↦d という条件の下で、各有限部分グラフが D に写るなら、C 全体が D に写る。

c から距離 n の頂点の像は、d から距離 n 以下の有限球に入る。辺の像の候補も有限である。各有限条件を確認する際には、関係する頂点と c を結ぶ有限な道も加える。従って有限離散集合の積の compactness が適用できる。

### 4.2 写らないことの小さい証人

X→D が存在しないなら、X のある連結成分 C は D に写らない。根 c∈C を固定する。各 d∈D_v に対して 4.1 の対偶により、c↦d の写像を禁止する有限部分グラフ F_d⊂C がある。

それらを合併すると、大きさ max(aleph_0,|D|) 以下の Z⊂X で Hom(Z,D)=∅ となる。D が空なら一頂点で十分。

### 4.3 小さい延長部分対象

局所有限な標的の集合 T を固定し、その総サイズを抑える無限基数 κ を取る。

X の κ 以下の部分集合を与える。各 D∈T で Hom(X,D)=∅ となる場合の小さい証人を加え、その後、有限 positive-existential 条件の解を繰り返し加えて、κ 以下の pure subquiver Y⊂X を取る。

任意の h:Y→D は X に延長する。

- Y と交わる X の連結成分について：purity により Y のその交わりは連結である。根を Y に固定する。任意の有限な延長条件は purity により Y 内で解け、h を適用できる。4.1 と同じ有限球 compactness で延長する。
- Y と交わらない成分について：h が存在する以上、4.2 の証人を入れた構成により X→D が存在する。その射をこれらの成分で使う。

従って Hom(X,D)→Hom(Y,D) は全射。

T={V_i, U_i×_{V_i}U_i} と置く。kernel pair も局所有限である。X∈{}^⊥S なら、V_i への延長により持ち上げの存在、kernel pair への延長により一意性が Y に降りる。

各 X は κ 以下の同類の部分対象の κ^+-directed union となり、これらは母圏で κ^+-presentable。余極限閉性と合わせて locally presentable となる。∎

有限次数の無限経路・無限木・格子・それらの任意の余積を、始域と終域の双方に使う構成も、これで除外できる。

## 5. 無向グラフ：二部グラフを始域にしても反例にならない

### 定理 5

UGraph の射の集合 S で、各 U_i がループなし二部グラフなら {}^⊥S は coreflective。終域 V_i のサイズや次数には制約しない。

証明：一本の f:U→V を考える。

f が辺側で単射なら定理 2 の対象。

辺側で単射でないなら、K_2⊥f は成立しない。ここで Hom(K_2,G) は G の順序付き隣接組の集合である。また f_v も単射でないので、ループなし一頂点グラフ K_1 も f に coorthogonal でない。

X∈{}^⊥{f} かつ X→V が存在すると仮定する。持ち上げによって X→U が存在するから、X はループなし二部グラフ。

X が非空・辺なしなら K_1 が retract。X が辺を持つなら、二彩色と一本の辺の選択により K_2 が retract。coorthogonality は retract に閉じるので、どちらも矛盾する。

従って

    {}^⊥{f} = {∅} ∪ {X : Hom(X,V)=∅}
               = {}^⊥{∅→V}.

つまり、この場合も mono に置き換えられる。各 f_i を処理すれば辺側単射の族になり、定理 2 から結論する。∎

木、森、完全二部グラフなどは、大きさ・分岐数にかかわらず、この無向グラフ版の反例の始域としては使えない。

注意：有向グラフの underlying undirected graph が二部である、というだけでは同じ議論にならない。K_2 への向き付き retraction が必要になるため、無向版の結果を一般の有向 Quiv に拡張してはいけない。

## 6. グラフ彩色の非コンパクト性だけでは足りない

任意の V に対し

    N_V = {∅} ∪ {X : X↛V}

は、mono ∅→V の coorthogonality class。coreflector は

    R(B)=B  if B↛V,
    R(B)=∅  if B→V.

後者では、非空な N_V の対象から B への射があると合成して V へ写り、矛盾する。

従って、V=K_κ を使って「κ 彩色不可能」を表し、その小部分グラフへの反映が集合論的に複雑であっても、このクラス自体は常に coreflective である。accessibility の失敗と coreflectivity の失敗を区別する必要がある。

### 持ち上げを動かす対称性

f:U→V に、fσ=f を満たす自己準同型 σ:U→U があり、σ が頂点を一つも固定しないなら、{}^⊥{f}=N_V。

実際、非空 X の持ち上げ g:X→U が一意なら σg=g となり、固定頂点が必要となる。

特に、非自明な自由な deck transformation を持つ通常の被覆、二重被覆、対称な blow-up は、この形で否定候補から外れる。

## 7. 一般の射を fiberwise-rigid な全射へ還元する

### 定理 7

Quiv / Dig / UGraph の一本の射 f:U→V に対し、

    i:U_*↪U,
    e:U_*↠I,
    m:I↪V

が存在して、

    {}^⊥{f} = {}^⊥{i,e,m},
    End_I(U_*)={id}.

### 構成

U_0=U とする。U_α→V の上のすべての自己準同型を取り、

    U_{α+1} = ⋂_{σ:U_α→U_α, f_ασ=f_α} Eq(σ,id)

と置く。極限段階では交わりを取る。

これは固定された U の subobject の下降列であり、集合個の段階で停止する。例えば U の頂点・辺を合わせたサイズを κ とすれば、κ^+ 段階まで真に減少し続けることはできない。

安定値を U_* とする。安定値の V 上の自己準同型はすべて恒等写像である。

X⊥f なら、任意の X→U は各段階のすべての自己準同型で固定される。一意な持ち上げ同士だからである。従って X→U は一意に U_* を経由する。これで

    {}^⊥{f} = {}^⊥{i,f|_{U_*}}

が得られる。最後に f|_{U_*} を strong epi e と mono m に像分解し、補題 0.3 を使う。m が mono なので、e 上の自己準同型と V 上の自己準同型は一致する。∎

これは U_* が絶対的に rigid という意味ではない。e を保つ自己準同型だけが恒等である。

e が split epi なら section s による se は e 上の自己準同型なので se=id。従って e は同型。よって、残る非自明な e は自動的に非分裂である。

この還元の後、e の始域の頂点数が有限なら定理 3 の証明を適用できる。e の両端が局所有限なら、定理 4 と補題 0.2 を適用できる。e が辺側で単射なら、i,e,m 全部に定理 2 を適用できる。

従って、一本の射について残る核心は、無限頂点の始域を持つ、辺も頂点も同一視する、非分裂・fiberwise-rigid な全射である。さらに、その両端がともに局所有限であってはならない。

## 8. Quiv と単純グラフの間で反例を移せる

L:Quiv→Dig を平行辺を潰す関手、J:Dig→Quiv を包含とする。L⊣J。

Dig のテスト S に対し A={}^⊥_Dig S と置くと、

    {}^⊥_Quiv(JS)=L^{-1}(A).

A が Dig で coreflective なら、任意の quiver B の coreflection は

    B ×_{JLB} J R_A(LB) → B

で与えられる。この pullback を簡約すると R_A(LB) が得られるため、domain は L^{-1}(A) に属する。普遍性は adjunction と pullback の普遍性から従う。

逆に L^{-1}(A) が Quiv で coreflective なら、単純グラフ B の coreflection T→JB を考える。T→JLT を経由した後も domain は L^{-1}(A) に属する。coreflection の一意性から、この unit は同型であり、T 自身が単純グラフとなる。従って A の coreflection が得られる。

UGraph に対しても、さらに対称化する reflector を使って同じ議論が成立する。pullback を簡約・対称化すると R_A(LB) が回復するためである。

従って、単純有向／無向グラフのテストによる非 coreflective な例は、そのまま Quiv の非 coreflective な例に移せる。ただし、任意の Quiv のテストを単純グラフのテストに置き換えられたわけではない。

ループなし B に向かう射の domain はループなしなので、ループなしグラフの slice で普遍射の非存在を証明できれば、ループを許す母圏でも同じ反例になる。

## 9. 次の具体的な残余問題

無向グラフで、三角形のない 3-chromatic graph U と三彩色

    e:U→K_3

を考える。e は頂点・辺で全射であり、三角形がないので非分裂である。

反例候補として残すには、少なくとも U の頂点数が無限、どこかの頂点の次数が無限、End_{K_3}(U)={id} という条件が必要となる。最後の条件は定理 7 の還元後の条件である。

この e に対する A_e の条件は、

    X の各 3-彩色 h:X→K_3 が、U への準同型として一意に持ち上がる

こと。

- X が 3-彩色不可能なら、Hom(X,K_3)=Hom(X,U)=∅ なので自動的に A_e に入る。
- 非空二部グラフ X は入らない。K_1 または K_2 が retract であり、無限の 3-chromatic U から K_3 への e はその Hom を全単射にしない。
- 3-彩色可能な X が A_e に属するなら X→U があるので X は三角形を持たない。

coreflection を失敗させる標的 B も χ(B)=3 に絞れる。χ(B)>3（またはループあり）なら B 自身が A_e に属し、B の coreflection は恒等。B が二部なら、B に向かう非空 A_e 対象はなく、coreflection は空グラフ。

これは反例の構成ではなく、次に取り組む具体的な残余問題の定式化である。S を一本の射に限定してよいという、一般の Quiv についての還元も主張していない。

## 10. 有限検算

有限 quiver の 70 個のランダムなテスト射と、頂点数 2 以下・辺数 2 以下などの 25 個の試験始域、計 1,750 組について、次を直接 Hom 集合を列挙して照合した。

- 辺の逆像の濃度を 0/1/2+ に圧縮した射との coorthogonality の一致。
- 定理 7 の fixed-point reduction と、包含を残した coorthogonality の一致。
- 頂点側が単射の場合の、定理 1 の V_good への置換。

全件で一致した。この有限検算は一般証明の代替ではない。

## 背景文献

1. J. Adámek et al., “Terminal Coalgebras for Finitary Functors”, CALCO 2025, Example 2.2 / Remark 2.4：グラフの局所有限可呈示性、strong-epi/mono 分解などの背景。
   https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CALCO.2025.3
2. S. Cox and J. Rosický, “Fibrantly generated weak factorization systems”, Rend. Sem. Mat. Univ. Padova 152 (2024), 133–144, arXiv:2201.06782：projectivity、pure-injectivity、accessibility と大きな基数の関係。ここでの具体的な graph coorthogonality の定理と混同しない。
   https://arxiv.org/abs/2201.06782
3. S. Cox, J. Feigert, M. Kamsma, M. Mazari-Armida, J. Rosický, “Cofibrant generation of pure monomorphisms in presheaf categories”, arXiv:2506.20278：presheaf の purity と有限方程式、compactness の背景。
   https://arxiv.org/abs/2506.20278

## 結論

得られたのは ZFC 内の肯定的な除外定理と、一般のテスト射の還元である。Quiv / Graph における非 coreflective な small-coorthogonality class や、その存在を導く追加集合論的仮定は、まだ得られていない。
