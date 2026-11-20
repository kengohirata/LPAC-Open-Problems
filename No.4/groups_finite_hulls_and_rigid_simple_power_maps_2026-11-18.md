# Problem 4：群の有限 hull と巨大な rigid simple groups の積からの射

2026-11-18。状態：PROOF_RECONSTRUCTED / RESEARCH_REDUCTION。root が §§1–7 の議論と出版版の仮定を独立に再構成し、現時点で穴を見出していない。
Göbel–Shelah の存在定理を使用し、その帰結をここで証明する。No.4 の反例や Grp 全体での肯定解はまだ得ていない。外部査読・形式検証・新規性確認は未実施。

## 1. 設定と可換な seed の処理

A⊂Grp は full replete で、小極限と countable ascending unions で閉じるとする。
Ab の積・equalizer・union は Grp のそれと一致するので、A_ab=A∩Ab は
[Ab の反射性定理](abelian_groups_limit_countable_union_reflection_theorem_2026-11-18.md)
の仮定を満たす。

G∈A と集合 S⊂G に対し、C_G(S) は id_G と各 inner automorphism c_s の共通 equalizer である。従って C_G(S)∈A。同様に Z(C_G(S))∈A。

**命題 1。** S の元が互いに可換なら、S を含む A-subgroup K≤G が存在し、

    |K|≤max(|S|,ℵ₀)^ℵ₀。

実際、この場合 S⊂Z(C_G(S))。後者は A_ab の対象なので、Ab 定理の small-subobject conclusion を適用すればよい。

特に各一元は濃度≤𝔠 の A-subgroup に入る。ただし、非可換な二元を一つの小さい A-subgroup に入れる結論は、この議論から出ない。

## 2. 最小 A-subgroup が満たす相対的な剛性

小極限閉性だけでも、G∈A と任意の S⊂G について

    H_A^G(S)=⋂{K≤G : K∈A, S⊂K}

が A に属する。この交叉の添字は G の部分集合の集合であり、候補には G 自身がある。

**命題 2。** H=H_A^G(S) とする。任意の W∈A と f,g:H→W について、f|S=g|S なら f=g。

証明：Eq(f,g) は S を含む A-subgroup of G である。H の最小性から Eq(f,g)=H。

従って S を各点固定する H の自己準同型は id_H のみである。特に

    C_H(S)=Z(H)。

一方の包含は自明。逆包含は、x∈C_H(S) による共役が S を各点固定するため、命題 2 から H 全体を固定することによる。

従って有限 seed の small-hull 定理を証明するには、この相対的な剛性を持つ H の大きさを、union 閉性を使って制御する必要がある。End(H) の相対的剛性だけでは、以下の存在定理により一様な濃度制御はできない。

## 3. 使用する巨大な単純群の存在定理

一次文献は Göbel–Shelah, *Constructing Simple Groups for Localizations*, Communications in Algebra **30** (2002), 809–837, Main Theorem 1.3, p.812。
[出版版 PDF](https://shelah.logic.at/files/95471/739.pdf)

固定群 H=A₅ を取る。任意の無限基数 μ で μ^ℵ₀=μ を満たすものに対し、|G|=μ⁺ で H を部分群に持つ群 G があり、次を満たす。

1. G は simple。g≠1 を固定すると、G の各元は高々 4 個の g の conjugates の積。
2. 任意の mono H→G は、指定された H≤G の包含と G の inner automorphism の合成。
3. H と同型な全ての部分群 H'≤G に対して C_G(H')=1。
4. 任意の nonzero endomorphism G→G は inner automorphism。

最後の形は、論文の monomorphism に対する主張と G の simplicity を合わせたもの。
任意に大きい μ=ν^ℵ₀ を選べるため、これらの G は ZFC で任意に大きい濃度に存在する。

**版の注意。** [初期 arXiv 版](https://arxiv.org/pdf/math/0009089) の主定理の表示には μ^ℵ₀=μ が抜けている。ここでは出版版の正確な仮定を採用する。

包含 η:H→G は Hom(G,G)→Hom(H,G) を全単射にする。非自明な H→G は simple H により mono なので上の 2 で延長でき、延長の一意性は 3 と 4 による。自明な射の延長も自明な endomorphism に限られる。

η-local objects の full subcategory

    L_η={W : Hom(G,W)→Hom(H,W) is bijective}

は小極限で閉じ、G を含む。L_η 内の部分群 K≤G が H を含むなら、H→K を延長する r:G→K があり、合成 G→K→G は H 上で id と一致する。従ってこの合成は id_G となり、K=G。

すなわち、**小極限閉類における有限 seed の最小 hull は任意に大きくなり得る**。
ここでは L_η の directed-union 閉性は主張していない。

## 4. 固定された A₅ が全ての積を一様に normal-generate する

以下 G_i はそれぞれ §3 の条件を満たし、指定した H=A₅ の包含を持つとする。
H 内の involution h=(12)(34) を固定する。

H の Klein four subgroup の三つの非自明元は H 内で互いに共役で、積は 1 である。従って 1 は h の conjugates の積として、長さ 2 と長さ 3 の表示を持つ。

各 G_i の任意の元 x_i は長さ n≤4 の h の conjugates の積である。6−n は 2 と 3 の非負整数結合なので、上の identity words を付け加えると、長さをちょうど 6 にそろえられる。x_i=1 でも長さ 6 の表示を選べる。

従って任意の非空な添字集合 J について、P_J=∏_(i∈J)G_i の全ての元は、diagonal h の conjugates **ちょうど 6 個**の積である。
特に diagonal H は P_J を normal-generate する。

この長さの一様性が、個々の G_i の normal generation から無限積の normal generation へ移る際に必要である。

## 5. Mixed product からの非自明な射は一つの ultraproduct を経由する

**定理 3（ZFC）。** T も §3 の条件を満たす群とする。任意の非自明な射

    f:∏_(i∈I)G_i→T

について、一意な ultrafilter U on I があり、f は

    ∏G_i → (∏G_i)/U ↪ T

と分解する。最後の射は monomorphism である。

**証明。** J⊂I に対し、P_J は残りの座標を 1 にして全積に入れる。
f|P_J が非自明なら、§4 によってその diagonal H 上で非自明であり、H は simple なので像は H と同型である。

P_J と P_(I\J) は可換なので、もし f|P_J が非自明なら f(P_(I\J)) はその H-copy を centralize する。§3 の条件 3 より f(P_(I\J))=1。
全体の f が非自明であるため、二つの complementary subproducts のうちちょうど一方が非自明に写る。

よって

    U={J⊂I : f(P_(I\J))=1}

は ultrafilter である。上方閉性と有限交叉閉性は、それぞれ kernel の下方閉性と P_(K∪L)=P_K P_L から従う。complement の二択と f≠0 によって proper ultrafilter となる。
U 上で一致する二つの tuple の差は kernel に入るので、f は ultraproduct を経由する。

この ultraproduct Q は simple である。a=[a_i]≠1 と b=[b_i] を取る。U 上で a_i≠1 であり、各 b_i は高々 4 個の a_i の conjugates の積。表示の長さには有限個の候補しかないので、一つの長さ n が U-large な集合上で共通になる。そこで conjugators を座標ごとに選ぶと、b は Q 内で a の conjugates の積になる。従って a の normal closure は Q 全体である。
誘導された非自明射 Q→T は、simple Q により mono。

最後に、f が別の ultrafilter V を経由するなら、J∈V の全てに対し f(P_(I\J))=1、従って V⊂U。ultrafilter の maximality により V=U。□

一般の simple target に対する「surjective map は一つの ultraproduct を経由する」という標準的な議論と違い、ここでは **f の全射性を仮定していない**。その代わり、固定された H の normal generation と T 内の H-copy の trivial centralizer を使っている。

## 6. Self-power の完全な分類

**定理 4（ZFC）。** G が §3 の群、λ=|G| とする。任意の非自明射 f:G^I→G は

    G^I → G^I/U ≅ G → G

と分解する。U は λ⁺-complete ultrafilter、中央の同型は diagonal G の逆、最後の射は inner automorphism である。

**証明。** 定理 3 から Q=G^I/U と mono ρ:Q↪G を得る。diagonal map δ:G→Q は mono。
合成 ρδ:G→G は非自明なので inner automorphism、特に全射である。ρ の injectivity から Q=δ(G) となる。

したがって、任意の関数 a:I→G は U 上で定数である。λ 個以下の部分集合による I の partition を G の元で label すれば、一つの cell が U に属することが分かる。この partition property は λ⁺-completeness と同値である。
逆に U が λ⁺-complete なら各 a:I→G は U 上で定数なので、ultralimit G^I→G は群準同型となり、任意の inner automorphism と合成できる。□

**系 5（N の下）。** N を「非可算可測基数が存在しない」とする。このとき任意の非自明射 G^I→G は、ただ一つの座標射影 G^I→G と inner automorphism の合成。

実際、非 principal な countably complete ultrafilter が集合上に存在すれば、非可算可測基数が存在する。定理 4 の U は countably complete なので、N の下では principal。

I=∅ のとき非自明射は存在しない。

## 7. Mixed product についてさらに従う濃度制限

**系 6（ZFC）。** 定理 3 の状況で κ=|T| とすると

    {i∈I : |G_i|≤κ}∈U。

そうでなければ U-large な集合上で |G_i|≥κ⁺。各その座標で κ⁺→G_i の injection を選べば、κ⁺ 個の tuple が座標ごとに相異なるので、ultraproduct 内でも相異なる。これは Q↪T に反する。

特に全ての |G_i|>|T| なら Hom(∏G_i,T) は自明な射だけである。

ただし、|G_i|≤|T| の座標に U が集中するという結論は、U が principal であるという結論ではない。異なる G_i の mixed products には §6 の diagonal G が存在せず、その箇所で self-power の証明が止まる。

## 8. Bergman の一般定理との関係と、使えない近道

一次文献：Bergman, *Homomorphisms on infinite direct products of groups, rings and monoids*, Pacific J. Math. **274** (2015), 451–495。
[著者版 PDF](https://math.berkeley.edu/~gbergman/papers/prod_gp.pdf)
特に Lemma 10, Lemma 12, Theorem 13 を確認した。

同論文では、非 countably-complete な ultraproduct の homomorphic image にある各元は、非 principal な countable ultrapower of Z の像、従って cotorsion abelian subgroup の中に入る。
適切な元がこの条件を満たさない target について、ultrafilter を principal にできる。しかし、これを §3 の G に機械的には適用できない。

Göbel–Shelah の実際の construction は全ての infinite-order elements を互いに共役にしている（Construction 3.4 の S₂-step と Lemma 3.6(c) の証明）。従って infinite-order element g と n≥1 に対して g^n と g は共役であり、g の n-th root が存在する。
順に x₁=g、x_(n+1)^(n+1)=x_n と選ぶと、増大する infinite cyclic subgroups の union は Q と同型であり、g を含む。
finite-order elements は finite cyclic subgroup に入る。

よってこの G の **全ての元が cotorsion abelian subgroup に入る**。cotorsion-free abelian groups が construction に使われていることから、Bergman の obstruction が働くと推論することはできない。

これは mixed product からの nonprincipal-ultraproduct map が存在するという主張でもない。その存在・非存在は、このノートでは未決着。

## 9. No.4 に向けた未解決の条件

以上で得たのは、巨大な有限 relative hull の実在、mixed products の一つの ultraproduct への分解、self-powers の座標分類である。
No.4 の反例には、さらに一つの full class A について次を同時に確保する必要がある。

1. 全ての小極限への閉性。
2. directed unions への閉性。
3. 固定された有限群 H から A への射に solution set がないこと。

任意に大きい個別の localizations H→G があるだけでは、3 は出ない。小さい固定 G₀ が全ての大きい G に写り、H→G を factor する可能性が残るためである。
また、individual G の endomorphism rigidity は、異なる G_i と G_j の間の Hom を制御しない。

従って次の具体的な課題は、適切な proper class の G_i について cross-Hom と mixed-ultraproduct embeddings を制御し、さらに limit/union closure が有限 relative hull を壊さないかを調べることである。

## 10. Coslice H/Grp では powers の小極限閉性が正確に得られる

以下 N を仮定する。固定された H=A₅ と §3 の G に対し、ambient category を H/Grp に変更する。この coslice は locally presentable である。

各集合 I に、diagonal inclusion を持つ pointed power

    D_I=(H→G^I)

を対応させる。I=∅ の場合は H→1 とする。

**命題 7。** D_I 全体の full replete subcategory D⊂H/Grp は Set^op と同値であり、小極限で閉じる。さらに D は reflective である。

まず I,J が非空とする。射 D_I→D_J の各座標 G^I→G は H 上で指定された包含に一致するので非自明。系 5 によって coordinate projection と inner automorphism の合成である。その inner automorphism は H の各元を固定するから、C_G(H)=1 により id である。

従って射 D_I→D_J はちょうど関数 J→I に対応する。I=∅ または J=∅ の場合にも同じ記述が成り立つ：H→1 から非自明な D_J への pointed map は存在せず、逆向きは一意である。

積は D_(⊔I_a)。二つの射 D_I⇉D_J が u,v:J→I に対応すると、その equalizer は

    {(x_i)∈G^I : x_(u(j))=x_(v(j)) for all j∈J}

であり、I に u(j)∼v(j) を課した quotient set Q に対する D_Q と同型である。これで全小極限への閉性が従う。

反射は明示できる。対象 X=(H→K) に対して

    S_X=Hom_(H/Grp)(X,D_1),
    R(X)=D_(S_X)

とし、各 pointed homomorphism を座標とする evaluation map X→R(X) を取る。任意の集合 I について

    Hom_(H/Grp)(X,D_I) ≅ Set(I,S_X)
                              ≅ Hom_(H/Grp)(D_(S_X),D_I)

が evaluation によって与えられるので、これが反射である。

この ambient の変更は、unpointed Grp で inner automorphism の equalizer が centralizer を生む問題を除く。しかし **D 自体の directed-union 閉性を意味しない**。D を directed unions で拡大した後の equalizer 閉性と反射性は別の問題として残る。

## 11. Powers の union は増えるが、可算 mono chain は equalizer の安全な target

引き続き N を仮定する。

**命題 8。** D は countable ascending unions で閉じない。

T_n=2^n と truncation T_(n+1)↠T_n を取り、それらの dual である mono chain

    D_(T₀) ↪ D_(T₁) ↪ D_(T₂) ↪ ⋯

を考える。その union U は、Cantor space 2^ω から discrete G への locally constant functions の群であり、pointing は H の constant functions である。

有限 powers の射の分類から、Hom_(H/Grp)(D_(T_n),G)=T_n。従って

    Hom_(H/Grp)(U,G)=lim_n T_n=2^ω。

これらの射は各点での評価そのものである。もし U∈D なら §10 の reflection unit

    U→G^{Hom(U,G)}=G^{2^ω}

は同型でなければならない。しかしこの evaluation map の像は locally constant functions に限られ、例えば一点集合の characteristic function（相異なる二元 1,h∈G を値に使う）は含まれない。従って U∉D。

**定理 9。** U が D の countable mono chain の union なら、任意の射 D_S→U は一つの stage を経由する。特に D_S⇉U の equalizer は D に属する。

**証明。** 非自明な場合、chain は非空な集合の inverse sequence

    T₀ ← T₁ ← T₂ ← ⋯

の dual であり、各 transition は全射である。L=lim_n T_n とすると、各 π_n:L↠T_n も全射である。よって U は G^L に injective に評価される。

θ:D_S→U を評価点 l∈L と合成すると、§10 の分類から S の一つの座標に対応する。これを τ(l)∈S と書く。従って U↪G^L と θ の合成は

    G^S→G^L,  F↦F∘τ

である。各 F:S→G について θ(F)∈U なので、F∘τ はある有限 stage π_n を経由する。

τ 自身がどの π_n も経由しないと仮定する。各 n に対し、π_n(l_n)=π_n(l'_n) かつ τ(l_n)≠τ(l'_n) となる二点を選ぶ。
相異なる元の対の可算列には、それらの対の無限個を分離する二色塗り c:S→{0,1} がある。これは、対応する graph に infinite matching がある場合と、finite vertex cover の一頂点が無限個の edges に接する場合に分ければ分かる（同じ edge が無限回現れる場合はその両端を分ければよい）。

この二色を G の相異なる元に置き換えた F を取る。F∘τ が π_m を経由するなら、全ての n≥m について π_n(l_n)=π_n(l'_n) から Fτ(l_n)=Fτ(l'_n)。これは無限個の対を分離したことに反する。

従って τ=τ_nπ_n となる n と τ_n:T_n→S が存在する。G^S→G^(T_n) を τ_n の precomposition とすれば、その U への合成は θ と一致する。これは U↪G^L の injectivity から従う。

二つの射には共通の stage を選べるので、equalizer は D 内の二射の equalizer と一致し、§10 により D に属する。□

この proof は、以前の Isbell power の可算 mono chain の場合と同じ inverse-limit / pair-coloring argument である。ここでは必要な full-power 射の分類が §6 の群論的定理から得られた。

**系 10。** Z が D-subobjects の arbitrary directed union、U が D の countable mono chain の union なら、Eq(Z⇉U) も D-subobjects の directed union。

各 stage D_S≤Z に定理 9 を適用すると、その stage 上の equalizer は D に属する。これらが ambient equalizer を directed union で覆うためである。

従って、この powers-in-coslice の具体的な経路でも、可算 chain を target にするだけでは equalizer 破綻を作れない。

## 12. 有限 H-hull を実際に壊すための partial-homomorphism criterion

以下は構成条件であり、この条件を満たす family の存在はまだ証明していない。

G=⋃_(j∈J)K_j を H を含む部分群の directed union とする。各 j に非空集合

    T_j⊂Hom_H(K_j,G)

があり、j≤k に対する restriction T_k→T_j が well-defined かつ全射であると仮定する。
さらにある j、x∈K_j、t∈T_j について t(x)≠x とする。

このとき pointed powers の mono diagram とその union

    U=colim_j D_(T_j)

を作れる。x∈K_j を evaluation function (t↦t(x))∈G^(T_j) に送る定義は restrictions と両立し、射 f:G→U を与える。群演算に必要な有限個の元を一つの K_j に入れることで、f が homomorphism であることが分かる。
各 t は H 上で包含に一致するので、f は pointed map である。

他方、constant functions からなる canonical map c:G→U がある。仮定 t(x)≠x と stage maps の injectivity により f(x)≠c(x)。従って

    H≤Eq(f,c)<G。

この equalizer は D-subobject を一つも含まない。実際、pointed mono D_I→G は、§6 の分類から一座標射影に等しい。これが mono であるためには I が singleton でなければならず、その像は G 全体となる。I=∅ からの pointed map は存在しない。

したがって、この条件が実現すれば、D の limit/union closure は original localization H→G の「proper subobject が H を含まない」という性質を壊す。
また、D-subobjects の directed unions からなる full class は equalizer で閉じない。

**重要な未解決点：** 全ての Hom_H(K_j,G) を無条件に T_j に取ることはできない。部分準同型がより大きい K_k へ延長できる保証がなく、restriction maps が全射とは限らないからである。この全射条件を落とすと、powers 間の transition maps が mono でなくなり、ここで必要な directed-union 構成ではなくなる。

## 13. 実際の初期段階における extension failure

§12 の条件は単なる technicality ではない。次の三点は、marker の最終 centralizer に関する主張を用いずに証明できる。

**補題 11。** G が simple、1≠H≤G、G=⋃K_j とする。§12 のように restriction maps が全射である系 T_j が存在するなら、その全ての member は injective である。

証明：t∈T_j が 1≠x∈K_j を潰すとする。1≠h∈H を固定する。G が simple なので、h は有限個の x または x⁻¹ の conjugates の積である。その conjugators を全て含む後の K_k を選ぶ。t を延長する t'∈T_k は x を潰すため h も潰すが、H 上では包含に一致するので矛盾する。□

**実例 12（full Hom の制限系は全射でない）。** Göbel–Shelah の Construction 3.4(i) の初期段階は Aut(H)*F_μ である。Aut(H) を固定し、free generators を全て 1 に送る retraction を G に合成したものは、H を固定する部分準同型である。
任意の free generator x≠1 を潰すので、補題 11 の証明で使った有限個の conjugators が現れる後の stage には延長できない。
従って、実際の stage subgroups K_α に対して T_α=Hom_H(K_α,G) と置く素朴な案は成立しない。

**実例 13（partial embeddings に絞っても自動的には直らない）。** 同じ初期段階で、H の上に自由な相異なる generators x,y と、H 内の involution a を選び、b=y⁻¹ay と置く。
free-product normal form により

    ⟨H,b⟩≅H*C₂,
    K=⟨H,H^x⟩≅H*H,
    K'=⟨H,H^b⟩≅H*H。

従って、H を固定して各 x⁻¹hx を b⁻¹hb に送る同型 t:K→K'≤G がある。
しかしこれを L=⟨H,x⟩ まで延長する準同型 φ があれば、全ての h∈H について

    φ(x)⁻¹hφ(x)=b⁻¹hb。

C_G(H)=1 より φ(x)=b。したがって φ(x²)=1 となり、φ は injective でない。
さらに補題 11 の有限 normal-generation witness を付け加えた段階には、homomorphism としても延長できない。

ここで K と L は実際の初期段階の有限生成部分群である。この例は、全ての pointed partial embeddings を採用しても、restriction maps の全射性が得られないことを具体的に示す。

### 構成本文を使う際の未解決の注意

出版版 p.824 では κ=ℵ₀ でもよいと記した直後、Theorem 3.2 に濃度 κ の ℵ₁-free abelian rigid family を掲げている。しかし countable ℵ₁-free abelian group は free abelian なので、この二つの記述を文字通り同時に適用することはできない。
また Def.2.3 の κ-malnormality の定義をそのまま使うと、L の上に非自明な U×L を amalgamate した後、u∈U\{1} は L を centralize するため L は κ-malnormal ではない。従って Cor.2.7(i) / Lemma3.8(a) の表示を、そのまま最終 centralizer の計算に使うことはできない。

これらは publication の主定理を否定したという意味ではない。κ の取り方や normalizer を含む適切な補題を別に確認する必要がある、という construction-level の監査記録である。本ノートの §§4–7 の証明は Main Theorem 1.3 の明示された性質だけを使い、これらの中間補題は使わない。
