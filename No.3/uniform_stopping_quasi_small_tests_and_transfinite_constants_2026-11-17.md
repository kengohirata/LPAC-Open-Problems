# No.3：一様停止の条件付き証明と、任意の集合順序数まで続く反射像の実例

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下の直接議論と既存定理への適用を主担当が展開・再点検した。独立査読・形式検証・文献上の新規性確認は未実施。一般の P3 の ZFC 証明、反例、独立性は得ていない。**

依頼：反射像の反復を使う肯定方向を進め、generatedness と射に関する整合性から、固定始域ごとの一様停止を証明することを試みる。

## 0. 今回の結論

(A) 次の追加条件の下では、**強商の一様停止まで ZFC で証明できる**。

    K = (S ∪ Q)^⊥ ⊂ P = Set^(D^op),
    S は射の集合、Q は P の epimorphisms の任意のクラス。

S^⊥ を A と置くと A は locally presentable。K は A の部分対象で閉じるため、K の strong epi は A でも strong epi となる。従って K は strong-epi co-wellpowered であり、元の generated strong generator の仮定と合わせて LP。さらに A が locally μ-presentable なら、K の全 strong epi の canonical regular decomposition は μ 以下で停止する。この bound は Q の濃度、始域、標的に依存しない。

(B) 一方、generatedness の基数だけから反射像の反復を短くする案には、**実際の反射圏の対照例**がある。

任意の非零集合順序数 Γ に対して、次を満たす圏 K_Γ を構成した。

- K_Γ は小さい前層圏 P_Γ の full reflective subcategory で、locally presentable。
- 包含は全 directed mono-colimits を保存する。
- finitely generated objects からなる集合サイズの strong generator を持つ。
- 初対象 H_Γ から終対象 T_Γ への strong epi の canonical regular decomposition は、正確に Γ 段で停止する。
- T_Γ の部分前層 A_S（S⊂Γ）上で、前稿の作用素は

      c_(T_Γ)(A_S) = A_(S ∪ {min(Γ\S)})   (S≠Γ)

  となる。以前の純粋に順序論的な「最初の欠落点を一つ加える」作用素を、反射から実際に実現した。

**Γ とともに圏・signature・生成族が変わる。** 一つの固定した K で停止段階が全順序数にわたり無界とは示していない。従って No.3 の反例ではない。

(C) 一般の反射の単位は epi–mono 分解できるので、P3 の一般肯定に向けた次の十分な橋は、非 epi の拡張条件を集合個に縮めること。今回その集合性は元の generatedness から導けなかった。

一様停止の条件付き証明と、一般の場合に残る集合性を区別する。同値条件の書換えだけを問題の解決と扱わない。

---

## 1. 前提と直前の補題の再点検

これまでの No.3 の presheaf reduction を使う。

    L:P=Set^(D^op) ⇄ K:E,    L ⊣ E,

E は fully faithful で、λ-directed mono-colimits を保存する。G は λ-generated objects の集合サイズの strong generator。K は complete、cocomplete、well-powered で strong epi–mono factorization を持つ。

H-family は G の <λ 個の coproducts の代表集合。空余積も含む。既存の還元により、H-family の各 H の strong quotients が集合個であることと K が LP であることは同値。

前稿の c_B(A)=Im_P(E(LA→B)) について、以下を再点検して維持した。

- A⊂c_B(A)、単調性、一段階の |c_B(A)|≤|ELA|。
- A→c_B(A) を反射した LA→L c_B(A) は kerpair(LA→B) の coequalizer。
- 固定 EB 内の増大列としての個別停止。
- 最終閉包 cl_B の λ-directed-union 保存。

これらから c_B 自体の λ-directed-union 保存や、全標的に共通の停止段階を導いてはいけない。

---

## 2. 集合個の非 epi 条件と、任意クラスの epi 条件による肯定

ここで右直交を用いる。対象 X が f:U→V に直交するとは、Hom(V,X)→Hom(U,X) が全単射であること。No.1 の coorthogonality とは向きが異なる。

### 定理2.1（ZFC、追加仮定付き）

上の P3 の設定に加えて、P の射の集合 S と、P の epimorphisms のクラス Q によって

    E(K) = (S ∪ Q)^⊥

と表示できるとする。このとき K は locally presentable。

Q は集合である必要がない。S の各射も mono である必要はない。重要なのは、epi でないテストを必要とする部分を集合で扱えることである。

### 2.2 中間の locally presentable category

    A=S^⊥⊂P

と置く。small-orthogonality theorem により A は locally presentable で、反射

    L_0:P⇄A:J_0

を持つ。

K⊂A であり、元の L を A に制限すると K への反射 R:A→K となる。随伴から

    K = { L_0(e) : e∈Q }^⊥   （A の内部）

が従う。

P は presheaf 圏なので e∈Q は regular epi。L_0 は coequalizers を保存するため、L_0(e) は A の regular epi、従って strong epi である。

注意：任意の圏の ordinary epi を無条件に strong epi としていない。ここでは presheaf の epi が regular であることと、左随伴の coequalizer 保存を使っている。

### 2.3 強 epi への右直交クラスは部分対象で閉じる

一般に A 内で、強 epi のクラス T に対する T^⊥ は全ての A-subobjects で閉じる。

**証明。** B∈T^⊥、mono m:C→B、e:U→V∈T と u:U→C を取る。B の直交性から、v:V→B、ve=mu が一意にある。

    U --u--> C
    | e       | m
    V --v--> B

を e の strong 性で埋めると w:V→C、we=u を得る。w の一意性は e の epimorphicity による。従って C∈T^⊥。□

これを L_0(Q) に適用して、K が A の部分対象で閉じることを得る。

### 2.4 強商を A に移す

q:H→B を K の strong epi とする。A で strong epi–mono factorization

    H --e--> I --m--> B

を取る。

B∈K と A-subobject 閉性から I∈K。K は full なのでこの分解は K 内の分解であり、m は K でも mono。

q の strong 性により m は同型。従って q は A でも strong epi である。

A は LP なので、固定 H の A-strong quotient classes は集合個。K は full であり、K 内の quotient arrows の同型関係も A と一致する。従って K も strong-epi co-wellpowered。

最後に、元の余完備性と generated strong generator と標準 locally-generated theorem を使い、K が LP と結論する。□

**この証明の途中で K の accessibility は仮定していない。** 既知の LP 性を使う対象は S から独立に作った A だけである。

### 2.5 用語と既存文献との関係

集合と epi のクラスの和であるテストクラスは、Adámek–Hébert–Sousa の用語で quasi-small。Freyd–Kelly 型の既存定理は、このようなクラスの orthogonality subcategory の reflectivity を扱う。

本稿では、その reflectivity だけを LP と取り違えない。A-subobject 閉性から強商を制御し、元の generatedness を最後に使った帰結として扱う。標準結果の組合せによる条件付き肯定であり、新規性は主張しない。

---

## 3. 上の追加条件なら、実際に一様停止まで得られる

### 定理3.1

定理2.1の A=S^⊥ が locally μ-presentable であるとする。このとき K の任意の strong epi q の canonical regular decomposition は μ 以下で停止する。

従って、始域 H を固定するより強く、全 strong epis に共通する集合順序数上界がある。

### 証明

§2.4から Jq は A の strong epi。

locally μ-presentable category では、strong epi は長さ≤μの regular-epi transfinite composition として分解できる。これは Gabriel–Ulmer の標準的分解結果で、Kawase–Nasu (2026), Corollaries 3.30–3.31 でも明記されている。

その A 内の分解に R:A→K を施す。R は全小余極限を保存するので、後続の regular epis は regular epis に、極限での連続な colimits は同じ colimits に送られる。始域・終域は K に属するので R はそれらを同型を除いて固定する。

従って q は K 内でも長さ≤μの regular-epi transfinite composition になる。

canonical kernel-pair tower は、任意の regular-epi decomposition より遅くは停止しない。次の直接比較で確認できる。

q の canonical tower を C_α、別の長さδの regular tower を D_α とする。D_0=C_0=H とし、帰納的に D_α→C_α を構成する。後続段階では D_α→D_(α+1) の kernel pair の像が C_α→B の kernel pair に入るため、canonical coequalizer C_α→C_(α+1) と合成するとその二射が等しくなる。regular epi の普遍性から D_(α+1)→C_(α+1) を得る。極限は colimit の普遍性。

D_δ=B となった時点で h:B→C_δ を得る。H→B と H→C_δ は epi であり、両三角形を H 上で比較して相殺すると h は C_δ→B の両側逆となる。従って canonical tower もδまでに停止する。

δ≤μなので結論を得る。□

この比較は Kawase–Nasu (2026), Theorem 2.34 および反射の随伴に対する Corollary 3.22(iv) とも一致する。使っているのは、既知の LP 圏 A からの分解の移送であって、未証明の K の LP 性ではない。

### 前稿の反射像反復との関係

前稿の A_0=Im_P(Eq) からの反射像反復は、初期の H→LA_0 を含めて同じ canonical regular tower を実装する。極限での添字の扱いと初期の一段を区別すれば、上のμから ambient-image 列にも集合長の共通停止上界が得られる。安全な上界としてμ+1を取ってよい。

---

## 4. 実際の圏での対照：任意の集合順序数 Γ の長さを実現する

generatedness の基数 λ だけを使って短い停止を導く案を検査する。

以下は任意の非零集合順序数 Γ ごとに作る。**Γ とともに母圏・圏・signature・生成族は変わる。** 一つの固定圏で真クラス長の failure を作るものではない。

発想の原型は Kawase–Nasu (2026), Example 3.32 にある可算列の partial constants の例。本稿では全ての集合順序数へ延ばすため、極限段階の前件を明示し、directed-union 保存を別に証明する。

### 4.1 母圏

P_Γ は、sorts

    V, B, C_α (α<Γ)

と unary structure maps

    B→V,   C_α→V

を持つ構造の圏。小圏上の presheaf category である。

K_Γ は次の条件を課した full subcategory。

1. B は一元集合。その V 内の値を b と書く。
2. 各 C_α は高々一元。C_α が非空の場合、その V 内の値を c_α と書き、c_α が定義されるという。
3. 各 α<Γ に対して

       [全ての β<α について c_β が定義され、c_β=b]
          ⇒ c_α が定義される。                         (D_α)

α=0 の空前件により c_0 は常に定義される。

c_α の値自体を b に等しいとする公理ではない。前件成立時に存在だけを要求し、値は自由でよい。また、ある c_α が b と異なる場合、後の定数が任意に定義されていることも許す。

### 4.2 小さい右直交表示と反射

B が一元という条件は 0→yB への直交で表せる。C_α が高々一元という条件は fold

    yC_α⊔yC_α→yC_α

への直交で表せる。

(D_α) には mono U_α→W_α を使う。

- U_α は B一元、V={b}、C_β一元（β<α）で出力は全てb、残りのCは空。
- W_α は U_α に一つの C_α-marker と、その出力となる新しい V-element z を付け加えたもの。

marker 条件の下で、U_α→Z が存在することは (D_α) の前件に等しい。W_α への一意延長は c_α の存在に等しい。値zの像はそのc_αによって決まる。

Γ は集合なので、以上のテストは集合個。従って K_Γ は reflective かつ LP。例えば μ=(max(aleph_0,|Γ|))^+ を取れば、全テストの始域・終域と presheaf 基底はμ未満で、包含はμ-filtered colimitsを保存する。

このLP性をNo.3の一般肯定の途中で仮定しているのではない。明示的な小さいテストを持つ対照例の性質として使っている。

### 4.3 全 directed mono-unions で閉じる

K_Γ-objects の directed mono diagram を P_Γ で union し、その対象を Z とする。Bは一元、各C_αは高々一元のまま。

Zで(D_α)の前件が成立すると仮定する。図式の段階iを任意に一つ固定する。β≤αについて超限帰納法を行い、C_βが既にこの同じ段階iで定義されることを示す。

- β=0：全局所対象でc_0は定義される。
- β>0：全ξ<βについて、帰納法によりc_ξが段階iにある。ξ<αであるため、Zではc_ξ=b。段階iからZへのV-componentが単射なので、段階iでもその等式が成り立つ。従って段階iの(D_β)からc_βが定義される。

β=αまで得られるので、Zで結論も成立する。

重要：α個の定数の出現段階をdirectednessで一度に揃えたのではない。**任意に選んだ一段階の内部で、規則と単射性を使って超限帰納した。** 従って通常のdirectednessで足りる。

E_Γは右随伴としてK_Γのmonosをpresheaf monosへ送るので、この検査は実際のK_Γ-mono diagramsに適用できる。

### 4.4 Finitely generated strong generator

presheaf のrepresentablesを反射した集合

    {L_Γ(y d): d=V,B,C_α (α<Γ)}

を取る。随伴から

    Hom_K(L_Γ(y d),Z)≅(E_Γ Z)(d).

これらはjointly conservative。§4.3により各evaluationはdirected mono-colimitsを保存するので、全てfinitely generated。従って生成性の基数はΓによらずλ=ωである。

生成族は集合だが、Γとともにその添字集合が変わる。有限個の生成対象で全てのΓを同時に扱えるとは主張しない。

---

## 5. 固定した初対象からの canonical tower は正確に Γ 段

### 5.1 対象

α<Γ に対して X_α を次で定める。

    V={b,x_α},  b≠x_α,
    c_β=b       (β<α),
    c_α=x_α,
    c_β undefined (α<β<Γ).

B-markerは一元。これらはK_Γの対象である。αより後の規則はc_α≠bのため前件が偽。

TはV={b}で全てのc_βが定義されbに等しい対象、すなわち終対象。

H=X_0は初対象でもある。任意の局所対象にはbとc_0が一意に指定されているので、Hからの射はそれらの値で一意に決まる。従ってHはfinitely presentableでもある。

q_α:X_α→Tを唯一の射とする。

### 5.2 後続段階

q_αのkernel pairはP_Γでも計算される。そのambient coequalizerは、Vを一元にし、C_βをβ≤αで定義済みとして残す対象である。

その反射は、α+1<Γなら、次の未定義定数c_(α+1)の値を自由に一つ付け加えるX_(α+1)。α+1=Γなら既にT。

この反射は直接普遍性でも確認できる。β≤αまでの定数が全てbに等しい射の標的では(D_(α+1))によって次の定数が存在し、その値への延長は一意。新しい値自体がbと異なる自由モデルを作れば、さらに先の定数を源側で定義する必要はない。

従って

    X_α→X_(α+1)

はK_Γ内のkerpair(q_α)のcoequalizerである。

### 5.3 極限段階

非零極限δ≤Γで、α<δのX_αのambient colimitを計算する。

各一時的な値x_αは次段でbへ送られるため、V-colimitは一元集合。定数c_βはβ<δについてちょうど定義され、値は全てbである。

これを反射すると、δ<Γでは新しくc_δの自由な値を一つ加えたX_δ、δ=ΓではTになる。

従ってX_δは前段階のK_Γ-colimitであり、列は連続。

### 5.4 強 epi 性と正確な停止

以上の列の合成q_0:H→Tは集合長のregular-epi transfinite compositionなのでstrong epi。

別の確認として、TのK_Γ-subobjectはT自身しかない。Bによりbを含み、(D_0)からc_0を含み、以後超限帰納法で全てのc_αを含むからである。q_0はepiでもあり、この部分対象の性質とpullbacksからstrong epi性も得られる。

全α<Γについてq_αは二つのV-elementsを同一視するのでmonoではない。Γ段でTに達し、residual mapは恒等射。

従って

    canonical stopping rank(q_0)=Γ.

Hは初対象でfinitely presentableであり、E_ΓHの全sort合計の元は有限個。にもかかわらず、圏を変えれば停止rankを任意の集合順序数にできる。

これは、source自体のpresentabilityだけから停止するという主張への対照でもある。既存の一様分解定理が使うのは、monicityを検査する強生成族全体の共通presentability rankであり、qの始域だけのrankではない。

---

## 6. 以前の順序論的作用素を、反射像そのものとして実現する

S⊂Γに対し、Tの部分前層A_Sを

    V={b}, B一元,
    C_α一元 if α∈S, empty otherwise,
    all defined constants have value b

で定める。

S≠Γとし、β=min(Γ\S)とする。L_Γ(A_S)は、A_SにC_β-markerと新しい値zを一つ付け加え、c_β=z≠bとした対象。

- βより前の定数は全てSにあり、規則がβの存在を要求する。
- βより後の規則はc_β≠bで止まる。
- 既にSにある後方の定数はそのままbとして残す。
- 任意のA_S→EZ（Z local）は、Zにc_βを要求するので、新しいzをその値に送る一意延長を持つ。

Tへの比較射はzをbへ送る。従ってambient imageはA_(S∪{β})。

    c_T(A_S)=A_(S∪{min(Γ\S)})  (S≠Γ),
    c_T(A_Γ)=A_Γ.

よって前稿のorder-theoretic d_Γを実際のpresheaf reflectionで再現した。

A_emptyからはα段でA_α（α≤Γ、αをその初期区間と同一視）が得られ、Γ段で停止する。強商q_0の初期imageはA_{ {0} }なので、canonical towerとの初期添字を区別する。canonical rankの正確な主張は§5で示した。例えばΓが非零無限極限なら、そのimage開始の反復もΓまで続く。

Tの局所部分対象はTだけなので、cl_T(A_S)=ETはSによらない。最終閉包は全ての非空directed unionsを保存する。

しかしδ<Γが非零極限なら

    c_T(union_(β<δ) A_β)=A_(δ+1),
    union_(β<δ) c_T(A_β)=A_δ.

したがって一段階c_Tはこのunionを保存しない。cf(δ)を大きく取れば、相応にdirectedな図式での失敗となる。

### この例から言えることと言えないこと

言えること：

- λ-generatednessのλ（ここではω）だけでは停止長を一様に抑えられない。
- 最終閉包のunion連続性、反射の普遍性、射に関する自然性があっても、c_B自体の同rankでの連続性は保証されない。
- 以前の「これは単なる順序論の例なので圏論的整合性で排除できるかもしれない」という期待は、そのままでは維持できない。実際の圏で同じ作用素が生じる。

言えないこと：

- 一つの固定Kで、全ての集合順序数の長さが必要になる。
- 固定K・固定presheaf基底・固定生成族に依存する上界が存在しない。
- No.3の反例または独立性。

ΓをOrdに取り替えるとsignatureが真クラスになり、今回のsmall presheaf表示ではなくなる。それをNo.3の反例として扱わない。

---

## 7. 元の反射に戻る：epi 部分は class のままでもよい

任意のfull reflectionに対して、局所対象は全単位への右直交で特徴付けられる。

    E(K)={η_X:X→ELX | X∈P}^⊥.

各単位をPで

    X --e_X--> I_X --m_X--> ELX

とepi–mono分解する。

### 補題7.1

eがepi、f=meなら

    {f}^⊥={e,m}^⊥.

**証明。** Z⊥fとし、u:I_X→Zを取る。ueをfに沿って一意に延長してv:ELX→Zを得る。vme=ueかつeがepiなのでvm=u。mに沿う一意性もfへの一意性から従う。よってZ⊥m。

次にa:X→Zをfに沿ってvへ延長すれば、vm:I_X→Zがeに沿う延長。一意性はeのepimorphicity。従ってZ⊥e。逆は直交射の合成閉性。□

したがって元のクラス全体を

    Q={e_X},  M={m_X},
    E(K)=(Q∪M)^⊥

と分けられる。

定理2.1によれば、epiクラスQは縮めなくてもよい。**M側の役割を集合個のテストSで代替できれば**、一般のKについてLP性と一様停止が従う。

ここで『mono側』を単純に『存在だけ』と同一視しない。右直交には一意性も含まれる。意味は、epiテストではない、拡張を要求する部分のsmallnessである。

### 未証明の橋

元のλ-generated strong generatorとlocal λ-directed-union閉性だけから、

    (Q∪M)^⊥=(Q∪S)^⊥   for some SET S

を導く証明は得ていない。

Mがclassであることを、集合Gがあるからという理由だけでsetと扱うことはできない。generatednessが局所対象間のmono-colimitsだけを扱うことと、Mの始域が非局所であることの差も残る。

一段階の反射像のsize boundや各標的での停止を、この集合性の代わりに用いると、始域ごとの強商の一様化を暗黙に仮定してしまう。

本稿は、元の問題を解決したものではなく、どの部分のsmallnessが得られれば、一様停止を実際に証明できるかを明示した条件付き結果である。

---

## 8. 監査・状態

- 前稿の個別停止とkernel-pair coequalizerの議論は、現在の仮定の範囲で維持する。
- K=(S∪Q)^⊥を元の仮定から導いたとはしていない。
- QはPのepis。PのregularityとL_0のcoequalizer保存によって、Aではstrong episになる。
- K-subobject閉性を用いる母圏はA=S^⊥。元のPでKがsubobject閉であるとは要求しない。
- strong epiの移送はimage factorizationとsubobject閉性から証明。一般の右随伴がstrong episを保存するとはしていない。
- 一様μは既知のLP圏Aのrankから取る。KのLP性を前提とする循環はない。
- 任意Γの例はset signatureであり、Γの各段階のテストを実際に書いた。
- directed-unionの証明で無限個の証人をdirectednessだけで一段階に集めていない。固定段階内の超限帰納法を使った。
- Γとともに生成族と母圏が変わることを明示した。
- H初対象のfinite presentabilityと、生成族全体のpresentabilityを区別する。
- canonical regular towerのrank Γと、ambient-image列の初期の一段のずれを区別する。
- 長い列の例をP3の反例や否定の証拠として過大評価しない。
- standard quasi-small reflectionやregular decompositionの結果の新規性は主張しない。任意Γへの直接構成にも新規性確認は行っていない。

**依然未確立：ZFC⇒P3、WVP⇒P3、ASC_infinity⇒P3、N⇒¬P3。**

---

## 9. 参照

ローカル入力：

- fixed_source_image_iteration_and_relative_equation_witnesses_2026-11-17.md：c_B、各標的の停止、最終閉包のunion保存、旧順序論的対照。
- positive_quotient_bounds_and_regular_towers_2026-11-17.md：強商集合性とLPの還元。
- generator_separation_reduced_powers_and_new_equalities_2026-11-17.md：fixed-rankの補題を反例で監査する方針。

一次資料（今回本文・関係ページのPDF画像を確認）：

1. I. Di Liberti and J. Rosický, Enriched Locally Generated Categories, TAC 38 (2022), 661–683; arXiv:2009.10980v2。
   https://arxiv.org/pdf/2009.10980
   §2冒頭、printed pp.3,9。generated strong generatorだけでなくstrong quotient smallnessを要する標準定理。一般P3を解いたものとして引用しない。

2. Y. Kawase and H. Nasu, On the decomposition of a strong epimorphism into regular epimorphisms, arXiv:2604.05744v1, 2026-04-07。
   https://arxiv.org/pdf/2604.05744
   Theorem2.34、Corollary3.22(iv)、Theorem3.27、Corollaries3.30–3.31、Example3.32。printed pp.24,27,28を画像で確認。Example3.32のω段の例を踏まえ、本稿§§4–6は全ての集合順序数Γについて直接証明を付した。原論文に任意Γの本稿の定理がそのまま記載されているとはしていない。

3. J. Adámek, M. Hébert and L. Sousa, The Orthogonal Subcategory Problem and the Small Object Argument, Coimbra preprint 07–40, 2007。
   https://www.mat.uc.pt/preprints/ps/p0740.pdf
   Introduction、printed p.2のquasi-smallの定義とFreyd–Kelly型のreflectivity定理を画像でも確認。reflectivityとLP性を区別する。

4. J. Adámek and M. Hébert, Quasi-equations in locally presentable categories, CTGDC 50 (2009)。
   https://cahierstgdc.com/wp-content/uploads/2016/05/ADAMEK-HEBERT.pdf
   Remark2.23、printed p.288を画像で確認。strong/regular episへのorthogonalityとsubobject閉性の関連。本稿§2.3には直接のlifting証明を記載した。

現在までの文献状況の網羅的調査や外部査読ではない。
