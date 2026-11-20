# Problem 3：RP の同値性、固定始域の split-colimit、コンパクト性の量化の差

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下の議論を本セッションで展開し再点検した。独立査読・形式検証・新規性確認は未実施。一般の P3 の肯定・反例・独立性は未確立。**

依頼：前回の計画（RP を既知の肯定例で検査し、必要部分へ弱め、元の仮定から導けるか試す）を実行する。

## 0. 結論

1. 前回の計画を修正する必要がある。**局所可呈示な reflective subcategory では、十分大きいある κ について RP_κ は必ず成立する。** 従って全ての κ で RP が失敗する LP の例は存在しない。P3 の前提下では「ある κ の RP」は LP と同値。
2. 強商ごとに小さい部分対象を選ぶ弱化 W も LP と同値。W の定式化には purity 自体は不要。量化の見た目を弱めただけでは、独立な進展にならない。
3. 一方、**固定した κ の RP_κ は LP 圏でも失敗する。** 任意の正則無限 κ に対し、κ-ary operation を持つ代数の hypergraph 表示で、κ-pure inclusion を反射すると非単射になる例を明示した。同じ例では RP_(κ^+) は成立する。これは P3 の反例ではない。
4. RP の証明に必要なものを、K 内の「固定始域の split monos の directed colimit が mono のままである」という条件 CS_κ に移した。pure inclusion は、presheaf 内で fixed-domain split extensions の directed union として具体的に表示できる。
5. No.1 型の filter-extension 議論で、**始域 X を固定すれば**、十分大きい almost strong compactness からこの colimit map が split mono になることを証明した。しかし得られる κ は X に依存する。P3 の一般肯定に使うには一様化が必要で、この点は未証明。
6. 非 LP であると仮定した場合、同じ一つの H から、任意に強い purity を持つ unit と、反射後の非 monic strong epi を作れる、という必要な反例形を得た。

N や No.1/2 の条件付き反例の主定理は使用していない。巨大基数を使用するのは §7 だけ。

---

## 1. 設定

K は P3 の仮定を満たす。すなわち locally small、cocomplete で、集合 G が λ-generated objects からなる strong generator。原著の還元を採用し、

    L : P = Set^(D^op) <-> K : E,   L ⊣ E

を固定する。E は fully faithful、λ-directed colimits of monomorphisms を保存する。局所対象とは E の本質的像の対象。T=EL、反射単位 η:Id_P→T。

H は G の <λ 個の余積の代表からなる集合。既存ノートの (Q) を使う：

    (Q) 各 H∈H について、全ての strong epi q:H→B の ||EB|| に集合基数の上界がある。

P3 の前提下で K が LP であることと (Q) は同値。この還元の直接証明は positive_quotient_bounds_and_regular_towers_2026-11-17.md §§2–4。最後の locally-generated theorem は標準定理である。

pure は ambient presheaf category P の categorical κ-purity を意味する。具体的には、κ-presentable U,V の間の s:U→V と可換四角

    U --u--> A
    |s       |i
    V --v--> B

に対して、ws=u を満たす w:V→A が存在すること。i w=v までは要求しない。

    (RP_κ) 全 B∈K と全 κ-pure mono i:A→EB に対し、i^#:LA→B が mono。

κ を大きくすれば purity の条件が強くなるため、RP_κ は上方に維持される。

---

## 2. LP なら十分大きい κ の RP が必ず成立する

### 定理2.1

P の full reflective subcategory K が LP なら、ある正則 κ について、E(K) は κ-pure subobjects で閉じる。従って RP_κ が成立する。

この方向には P3 の generatedness は不要。

### 証明：E の accessibility

各 representable y(d) に対する L(y(d)) は K の対象の集合をなす。K が LP であると仮定しているので、それら全てが共通の正則 μ について presentable となるよう μ を選べる。

    (EX)(d) ≅ K(L(y(d)),X)

なので E は μ-filtered colimits を保存する。L は左随伴として全余極限を保存するため、T=EL も μ-filtered colimits を保存する。μ は必要に応じて大きくし、P が locally μ-presentable であるとする。

### 証明：集合個の単位による表示

P の μ-presentable objects の小さい skeleton P_μ を取り、

    S={η_C:C→TC | C∈P_μ}

とする。

E(K)=S^⊥ が成り立つ。局所対象は全ての単位に直交するから一方向は明らか。逆方向では、任意の X を P_μ-objects の μ-filtered colimit に表示する。T の保存性と単位の自然性により η_X はこれらの η_C の arrow-category colimit になる。Hom(-,Z) は colimits を limits に送るので、Z⊥S なら全ての η_X に直交する。

特に id_Z を η_Z に沿って延長すると r:TZ→Z、rη_Z=id_Z を得る。η_Zr と id_(TZ) は η_Z の後で一致し、TZ は局所対象なので反射の一意性から一致する。従って η_Z は同型であり Z は局所対象。

### 証明：十分大きい purity で閉じる

S の全始域・終域が κ-presentable になるよう正則 κ を選ぶ。これは S が集合なので可能。κ=μ と主張する必要はない。

i:A→EB が κ-pure とし、s:U→V∈S、u:U→A を取る。EB の直交性から v:V→EB、vs=iu がある。purity により w:V→A、ws=u を得る。

二つの候補 w,w' は EB に入れた後に s 上で一致するため、EB の直交性により i w=i w'、i の mono 性から w=w'。

よって A⊥S で A は局所。i^# は i と同型なので mono。□

### 系2.2：P3 の前提下での同値

既存ノートの RP⇒Q と合わせて

    K is LP
    ⇔ ∃κ RP_κ
    ⇔ ∃κ [E(K) is closed under κ-pure subobjects].

**従って、前回提案した「LP な例でも全 κ で RP が失敗するか」の探索は不要。固定した κ の失敗と、全 κ での失敗を区別する。**

この証明は standard small-orthogonality / purity arguments の再構成であり、新規な公刊定理とは主張しない。

---

## 3. 強商ごとの選択版：purity は条件から外せるが、やはり同値

### 条件 W

各 H∈H に基数 μ_H があり、全ての strong epi q:H→B について、部分前層 i:A↪EB を次のように選べる。

    Im_P(Eq)⊆A,   ||A||≤μ_H,   i^#:LA→B is mono.

A が pure であることは要求しない。μ_H は q,B に依存してはいけない。

### 命題3.1

P3 の前提下で W⇔Q⇔K is LP。

**W⇒Q。** Eq が A を経由するので、随伴で q は H→LA→B と因子化する。最後の射は mono だから、q の strong 性により LA→B は同型。

大きさ ≤μ_H の presheaves は同型を除いて集合個であり、それらの反射 LA も集合個。従って ELA のサイズに共通上界があり、B の上界となる。

**Q⇒W。** ||EB|| の上界を μ_H とし、A=EB、i=id を選べばよい。□

A をある固定 κ の pure subobject と要求しても同値のままである。逆方向で選ぶ identity は全ての κ について pure だから。

RP から W への条件の見かけ上の弱化は、元の問題の前提下では論理的には同値なまま。ただし、実際の構成では「任意の A」ではなく「よい A の選択」を狙えるという技術的な利点は残る。

---

## 4. 固定した κ の RP は LP な反射でも失敗する：明示例

任意の正則無限基数 κ を固定する。

### 4.1 母圏と局所対象

P_κ は二つの sorts V（頂点）, R（operation records）と unary maps

    p_j:R→V  (j<κ),    o:R→V

を持つ構造の圏。これは小圏上の presheaf category。

K_κ は、

    (p_j)_j : R→V^κ

が全単射となる対象の full subcategory。この全単射を用いて R=V^κ と正規化すると、o は一つの κ-ary operation t:V^κ→V となる。従って K_κ は一つの κ-ary operation を持つ代数の圏。

U を κ 個の入力頂点だけを持ち records が空の presheaf、W を一つの record とその κ 個の入力頂点および出力頂点を持つ presheaf とする。s:U→W は入力頂点の包含。

    Hom(W,Z)≅R_Z,
    Hom(U,Z)≅V_Z^κ,
    Hom(s,Z)=(p_j)_j.

従って K_κ={s}^⊥。U は κ 個の頂点-representables の余積、W は record-representable なので、両者は κ^+-presentable。small orthogonality theorem により K_κ は reflective かつ LP。包含は κ^+-filtered colimits を保存する。

反射は、頂点の free κ-ary algebra を作り、各 record r に

    t((p_j(r))_(j<κ))=o(r)

という関係を課すことで具体化できる。

### 4.2 κ-pure inclusion

B は二元集合 {0,1} 上の定数零 operation、

    t_B(x)=0 for every x∈2^κ

とする。従って EB の頂点は2、records は2^κ。

A は同じ頂点2を持ち、records を

    R_A={x∈2^κ : |supp(x)|<κ}

に制限する。出力 o は全て0。i:A↪EB は明らかに mono。

**補題。i は κ-pure。**

この unary signature で κ-purity を調べるには、<κ 個の variables/equations と A の parameters からなる、EB で解ける正の方程式系を A で解けばよい。presheaf の κ-presentable objects は <κ 個の generators/relations による対象の retract として取れるため、この方程式判定は categorical purity の lifting condition を与える。

与えられた系で、等号によって同一視される record variables をまとめる。record parameter に固定された変数は、その A-record のままにする。それらの support の合併は κ の正則性により <κ。

残る record variables については、系に明示的に現れる入力 index j の集合 J だけで、元の EB の解の値を保ち、その他の入力を0にする。|J|<κ。頂点変数の値は元の二元集合内の解の値のまま。出力は EB でも A でも0。

この変更は全ての equations を保ち、各 record の support は <κ になる。record variable の等号は最初にまとめており、record parameter に固定される場合も変更しない。従って A で解ける。□

ここでは |signature|=κ であることを隠していない。κ-presentability を「台集合のサイズ <κ」と同一視せず、<κ 個の generators/relations を使っている。

### 4.3 反射後に二元が同一視される

LA の頂点として、生成元の像を a_0,a_1 と書く。次の二元を考える：

    a_0,
    z=t_(LA)(a_1,a_1,...).

比較射 r:LA→B は z と a_0 をともに0へ送る。

一方、別の二元代数 D を

    t_D(x)=0  if |supp(x)|<κ,
           1  otherwise

で定める。頂点で identity、records はそのまま送る A→ED が存在する。A の全 record の出力条件は t_D=0 により満たされるためである。

反射の普遍性により LA→D があり、a_0 を0、z を1に送る。従って z≠a_0。よって r は mono でない。

以上、**RP_κ は失敗**する。しかし K_κ={s}^⊥ の両端は κ^+-presentable なので、§2 の最後の purity argument を s に直接使えば **RP_(κ^+) は成立**する。

これは「固定 κ では不足し得る」例であり、一つの固定圏で全 κ の RP が失敗する例ではない。K_κ も母圏も κ に応じて変わる。No.3 の反例ではない。

---

## 5. pure inclusion を fixed-domain split extensions の union にする

以後は一般の P=Set^(D^op) に戻る。κ を正則無限で |Mor D|<κ となるよう取る。

### 補題5.1（具体的な分解）

κ-pure inclusion i:A↪B に対し、B のサイズ <κ の部分前層 C 全体を包含で順序付けた poset J を取る。

    B_C=A∪C⊂B,
    a_C:A↪B_C.

このとき：

- J は小さい κ-directed poset。
- 各 a_C は split mono。
- C⊂C' の B_C→B_C' は ambient mono。
- B=colim_C B_C であり、i は fixed-domain split monos a_C の colimit。

**証明。** D の射が κ 未満なので、<κ 個の部分前層の union は再びサイズ <κ。全ての元を覆う。

C∩A→C は両端がサイズ <κ、従って κ-presentable な presheaves の間の射。i の purity を

    C∩A -> A
      |      |i
      C  ->  B

に適用して、C∩A 上で inclusion に一致する r_C:C→A を得る。presheaf では union は交わりに沿う pushout なので、r_C と id_A を貼り合わせて B_C→A を得る。これは a_C の retraction。

これらの retractions が C について compatible であるとは主張していない。□

### 局所終域に反射する

B=EB_0 が局所の場合、L を施すと

    LA --s_C--> L(B_C),
    s_C=L(a_C)

は全て split mono であり、

    B_0 ≅ colim_C L(B_C),
    i^#=colim_C s_C.

ここで **段階間の L(B_C)→L(B_C') は mono と判定できない**。元の generatedness が扱うのは段階間の射が mono である図式であり、s_C がそれぞれ split mono であるだけでは適用できない。

これは一般の「pure mono は split monos の directed colimit」という定理より、この問題の形に合わせて具体化した表示。一般定理は Positselski (2026), Theorem 3.4 / Corollary 3.5 とも整合する。

---

## 6. K 内の colimit 条件へ移した ZFC 判定

### 条件 CS_κ

任意の X∈K と、κ-directed poset I 上の図式 Y_i、および自然な射

    s_i:X→Y_i,
    f_ij s_i=s_j

で、全ての s_i が split mono であるものに対し、誘導される射

    s:X→colim_i Y_i

は mono。

f_ij 自体が mono であることは要求しない。retractions の整合性も要求しない。結論は mono であって split mono とは限らない。

### 定理6.1

P3 の前提下で、ある正則 κ の CS_κ が成り立てば K は LP。

**証明。** κ を |Mor D| より大きくしてよい。大きな基数の directed diagram は元の基数でも directed なので CS は維持される。補題5.1を反射した図式に CS を適用すると i^# が mono。従って RP_κ が成立し、既存の RP⇒Q⇒LP を使う。□

### 逆方向

K が LP なら、§2のように E が μ-filtered colimits を保存する μ を選べる。固定始域の split monos の μ-directed colimit を E で計算すれば、presheaf の各成分で、単射の自然変換の filtered colimit なので単射。E は mono を反映するため CS_μ。

従って P3 の前提下で

    K is LP ⇔ ∃κ CS_κ ⇔ ∃κ RP_κ.

CS の証明に独立に使える十分条件は、ある κ について、K の arrow category における κ-directed colimits が monomorphisms を保つことである。ただしこれは元の「mono を遷移とする図式の union 保存」より強く、仮定なしに使わない。

### Generatedness が直ちに使えない正確な箇所

s_i:X→Y_i が全て split なら、各 i では X 内の二射は区別される。求めているのは、K の colimit が新しくその二射を同一視しないこと。

元の λ-generated strong generator が直接保証するのは、**遷移が monos の** colimit における因子化と等式検出。今回の f_ij は mono とは限らない。その仮定を CS の証明の中で暗黙に追加してはいけない。

全ての r_i:Y_i→X を f_ij と整合的に選べれば colimit から X への retraction ができるが、split 性だけではその coherent choice は得られない。

---

## 7. Almost strong compactness で実際に得られた局所的肯定

ここでは元の generatedness は不要。K は presheaf 圏 P へ full faithful に埋め込まれ、小さい colimits を持つとする。

### フィルター拡張仮定 FC(κ,θ)

κ は正則、θ は無限基数で、全ての κ-complete filters が θ-complete ultrafilters に延長できるとする。θ-complete は <θ 個の交叉で閉じる、という約束。

regular almost strongly compact κ なら全 θ<κ についてこの条件が成立。ASC が singular の場合でも、κ をその上の正則基数に上げれば filter-extension 条件は維持される。

### 定理7.1（固定した始域）

X∈K を固定し、全 d∈D について |EX(d)|<θ とする。FC(κ,θ) の下では、CS_κ の形の任意の X 始域の図式について、

    s:X→colim_i Y_i

は **split mono** になる。

### 証明

各 s_i の retraction r_i:Y_i→X を選ぶ。I 上で tails

    I_i={j∈I:j≥i}

の生成する filter は κ-complete。κ-directedness により <κ 個の tails の交わりは別の tail を含むからである。θ-complete ultrafilter U に延長する。

a∈EY_i(d) に対し、j≥i で

    E(r_j f_ij)(a)∈EX(d)

を考える。値域の濃度が <θ なので、U-completeness により U-almost everywhere 一意な値を取る。その値を t_(i,d)(a) とする。tail の外は任意に補ってよい。EX(d)=empty なら r_i があるため EY_i(d)=empty で、この sort では値の選択自体が不要。

有限個の等式は U-large な集合の交わりで同時に成立する。従って：

- t_(i,d) は d について自然であり、自然変換 EY_i→EX を与える。
- E の fullness により t_i:Y_i→X が得られる。
- t_j f_ij=t_i。
- t_i s_i=id_X。

colimit の普遍性から t:colim Y_i→X があり、ts=id_X。□

**ここでは ultraproduct が K に属するという仮定を一切使わない。** U による値の選択で既存の固定対象 X への自然変換を作り、fullness で K の射に戻す。θ>|EX(d)| が全ての値を X 内に保つ要点。

### 7.2 得た量化と、必要な量化

ASC が真クラス存在するなら、この定理から

    ∀X∈K ∃正則κ_X:
       X 始域の全 κ_X-directed split-extension colimits は split mono

が従う。

一方、§6で P3 を肯定するための十分条件は

    ∃正則κ ∀X∈K:
       X 始域の全 κ-directed split-extension colimits は mono。

**∀X∃κ_X を ∃κ∀X に交換してはいけない。** split という結論を mono に弱めても、自動的な一様化は示せていない。

RP への適用では X=LA。小さい κ-pure hull A の通常のサイズ上界 μ は、μ^(<κ)=μ を満たすよう κ 以上に取る。反射 LA のサイズはさらに大きい可能性がある。

「κ を ||ELA|| より大きく取り直す」だけでは、新しい κ-pure hull を作り直すことになり、始域 LA 自体が変わる。従ってこの繰り返しの停止や一様上界を仮定してはならない。

本節は **ASC_infinity⇒P3 を証明していない**。No.1 と同型の compactness 技法がここでも実際に働く局所的範囲と、その先の不足を明示した結果である。

---

## 8. 非 LP の場合に必ず現れる、より具体的な反例の形

### 命題8.1

P3 の前提を満たす K が LP でないと仮定する。このとき H∈H を一つ固定でき、任意の正則 κ>|Mor D| に対して、次が存在する。

    κ-pure mono i:A↪EB,
    Im(Eq)⊆A for a strong epi q:H→B,
    r=i^#:LA→B is a nonmonic strong epi,
    η_A:A→ELA is κ-pure and not an isomorphism.

A のサイズは κ と EH だけから選んだ μ=2^ν 以下にできる。

### 証明

Q が失敗するので、一つの H の strong quotients の E-carrier は無界。κ を固定し、ν≥κ,||EH||,aleph_0、μ=2^ν とする。サイズ ≤μ の presheaves の skeleton S_μ を取り、

    b=sup{||ELC||:C∈S_μ}

を取る。これは集合の上限。

||EB||>b となる strong quotient q:H→B を選ぶ。Im(Eq) を含むサイズ ≤μ の κ-pure A↪EB を標準の方程式閉包で作る。

随伴によって q=r a、a:H→LA、r:LA→B。q が strong epi なので r も strong epi。この右消去は直接確認できる：r と mono m の square を a で前合成し q の対角を取る。得た対角の r 側の等式は m の monicity で確認できる。r の epi 性も q=r a から従う。

||ELA||≤b<||EB|| なので r は同型でない。strong epi かつ mono は同型だから r は mono でない。

    i=E(r)η_A

が κ-pure であることから、pure morphisms の left-cancellation により η_A は κ-pure。具体的にも η_A に対する lifting square を E(r) で後合成して i の purity を適用すればよい。

η_A が同型なら r は i と同型な mono になるので矛盾。従って非同型。□

この命題は新しい反例を構成したものではない。「P3 の反例があるなら、一つの固定 H に対してこの形が全 κ で現れる」という条件付きの必要条件。

---

## 9. 現時点の判定と次の焦点

今回の実行結果は：

- RP が最終結論より不必要に強すぎるという懸念を、**ある κ が存在するという形では**解消した。
- 固定 κ では失敗する LP の対照例を与え、基数の拡大を明示的に扱う必要を確認した。
- 弱い選択版 W の purity を除けたが、W が Q と同値であることも確認した。条件を言い換えただけで「一般肯定に近づいた」と過大評価しない。
- pure inclusion の具体的な split-extension union を反射し、元の generatedness が直接適用できない箇所を、**段階間の射**と**固定始域からの射**の違いに局所化した。
- almost strong compactness を使った新しい局所的 split-colimit 定理を得た。ただし objectwise な κ と一様な κ の差は残る。

最も具体的な未解決点は、元の generated strong generator と union 保存から、必要な fixed-domain split-extension colimits の monicity を、ある一つの基数で一様に示せるか。

全面的な CS を示す必要があるとは限らず、§5の「pure subobject を反射して得た図式」に限定してもよい。しかし、その限定だけから一様化を得たわけではない。

**未証明のまま：ZFC⇒P3、WVP⇒P3、ASC_infinity⇒P3、N⇒not P3。**

---

## 10. 監査事項

- §2の LP 仮定は必要条件の検査にだけ使う。一般肯定の証明で accessibility を先取りしない。
- RP_κ の固定 κ と ∃κ RP_κ を区別する。
- §4は圏が κ に依存する。固定圏に全 κ の失敗を与えたとはしない。
- §4の purity は <κ generators/relations による判定。signature の濃度が κ であることから、台集合 <κ という誤った判定を使わない。
- §4で t_D は同じ二元集合上の別の operation。A→ED が存在することを全 records について検証した。
- §5の小部分前層 C∩A は κ-presentable。このサイズ判定には |Mor D|<κ を使う。
- §5の retractions は個別に存在するだけで、互換とはしない。
- §6は反射後の transition maps が mono であると仮定しない。s_i が split mono なのとは別。
- §7は値域 EX(d) が θ 未満であることを全ての coordinates で使う。無界な値域から U-limit の値を X に選べるとはしない。
- §7は K の ultraproduct 閉性を仮定していない。fullness で自然変換を射へ戻す。
- §7で得た ∀X∃κ_X と欲しい ∃κ∀X を区別する。
- §8で b は小さい presheaves の **集合**の反射値から取る。未証明の強商の集合を数えていない。
- 既存の標準定理と今回の直接再構成を区別し、新規性・独立査読・形式検証を主張しない。

## 11. 参照と今回確認した範囲

ローカル：

- positive_definability_and_local_submodels_2026-11-17.md §6：RP の元の十分条件。
- positive_quotient_bounds_and_regular_towers_2026-11-17.md §§2–4：Q⇔LP の還元。
- reflection_first_stone_dynamics_and_ambient_union_boundary_2026-11-17.md §6：local unions と ambient preservation の区別。

一次資料：

1. I. Di Liberti and J. Rosicky, Enriched Locally Generated Categories, TAC 38 (2022), 661–683; arXiv:2009.10980v2.
   https://arxiv.org/pdf/2009.10980
   §2冒頭（PDF p.3）、Theorems 2.18, 2.24 と Remark 2.27（PDF p.9）を本文と screenshot で確認。強商の集合性を落として標準定理を使っていない。Remark 2.27 の monad 記法を、元の仮定から全 ambient diagram の保存を得る証明として採用していない。

2. Leonid Positselski, On pure monomorphisms and pure epimorphisms in accessible categories, TAC 45 (2026), no.7, pp.246–288; arXiv:2506.13374v4.
   https://www.tac.mta.ca/tac/volumes/45/7/45-07abs.html
   https://arxiv.org/pdf/2506.13374
   公刊ページの日付は2026-01-30。§3の定義、Lemma 3.1（pure left-cancellation 等）を PDF p.11 の screenshot と照合し、Theorem 3.4 / Corollary 3.5 の本文も確認。
   §5の fixed-domain union 表示は本稿で直接示しており、同論文が P3 の橋を証明しているとは主張しない。

3. W. Boney and P. Zambrano, Around the set-theoretical consistency of d-tameness of Metric Abstract Elementary Classes, preprint (2015).
   https://people.math.harvard.edu/~wboney/papers/BZMAECsLC.pdf
   Definition 3.1 の filter-extension による almost strong compactness の定義を本文と PDF p.4 の screenshot で確認。本稿§7の colimit 定理を同論文から引用しているのではなく、使う集合論的仮定の出典。

4. J. Adamek and J. Rosicky, On reflective subcategories of locally presentable categories, TAC 30 (2015), no.41, pp.1306–1318.
   https://www.tac.mta.ca/tac/volumes/30/41/30-41abs.html
   公刊ページの reflection theorem の位置づけを確認。今回本文 PDF の取得はエラーとなったため、本文の特定の補題を読めたとはしない。§2は本文の未確認な定理番号に依存せず直接記した。

全ての最新文献を網羅的に監査したという意味ではない。

5. J. Bagaria, C. Casacuberta, A. R. D. Mathias, J. Rosicky, Definable orthogonality classes in accessible categories are small, JEMS 17 (2015), 549–589.
   https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content
   §8の定義と Lemma 8.1（arrow colimit から orthogonality を移す議論）を本文と印刷 p.575 の screenshot で確認。今回§2の単位集合による表示に用いる一般的な Hom-colimit の機構の参照。全ての反射部分圏が無条件に small-orthogonality class だと引用していない。
