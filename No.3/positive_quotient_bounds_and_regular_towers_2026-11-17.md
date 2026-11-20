# Problem 3：肯定方向 — 小さい始域の強商、regular quotient の塔、一様な停止上界

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下の還元・条件付き肯定結果・反例計算を主担当が書き下して点検した。独立査読・形式検証・新規性確認は未実施。Problem 3 一般の ZFC 証明、反例、独立性はいずれも得ていない。**

## 0. 今回の結論

肯定証明を試した結果、残る箇所を次に局所化した。

> λ-generated な strong generator G の <λ 個の余積 H を固定する。H からの strong epi quotient H→B の大きさを、B によらず集合基数で抑えられるか。

これは単なる十分条件ではない。以下の設定では、この局所的上界条件は K が locally presentable であることと同値である。さらに、核対の coequalizer を反復する標準列について、始域 H ごとに全ての strong quotient に共通する集合順序数の停止上界が存在することとも同値である。

ZFC で肯定できる追加条件を二つ証明した。

1. 上の H を始域に持つ strong epi が全て regular epi である。
2. presheaf 表示の reflector が monomorphism を保存する。

一般の場合には、核対を数えるだけでは不足する。Cat の同じ有限対象 [1] から、全く同じ核対を持つ非同型の strong quotients を構成できる。核対の余等化を反復しても、元の H 上の核対は最初の一段で既に安定するため、元の部分対象の個数では残りの列を止められない。

**ここで確認したのは集合サイズ・一様停止の問題への到達であり、その問題が ZFC では解消不可能だという証明ではない。VP の必要性や独立性を主張しない。**

---

## 1. 前提と採用する既知の還元

K は locally small、cocomplete で、集合 G が strong generator をなし、その各対象が共通の正則無限基数 λ に対して λ-generated であるとする。

原著 pp.295–296 の presheaf 還元を使い、以降は

    L : P = Set^(D^op)  ⊣  E : K → P

という full reflective presentation のもとで議論する。D は小圏、E は fully faithful で、λ-directed colimits of monomorphisms を保存する。必要なら λ を大きくしてよい。この還元自体を今回新しく証明したとはしない。

重要な区別：

- λ-generated は mono の λ-directed colimit だけを扱う。
- λ-presentable は全ての λ-directed colimit を扱う。
- 最終目標は「ある μ に対して locally μ-presentable」であって、元の λ のまま locally λ-presentable とは限らない。

標準定理として、cocomplete・weakly co-wellpowered で generated objects からなる strong generator を持つ圏は locally presentable であることを使う。weakly co-wellpowered は、ここでは strong epi quotients が各始域について集合個であることを意味する。全ての epi quotients を最初から仮定する必要はない。

この標準定理と Problem 3 の関係は Positselski–Rosický (2018) の導入、および Di Liberti–Rosický (2022) の Theorems 2.18, 2.24 と Remark 2.27 で確認した。

---

## 2. この段階で ZFC により確保できる構造

### 2.1 完備性と well-poweredness

full reflective subcategory K は P の small limits で閉じ、E はそれらを保存する。従って K は complete。

K の mono m:Y→X は E により P の mono EY→EX に送られる。E が fully faithful なので、P で同じ部分対象となる K の二つの部分対象は K でも同じ部分対象である。P は well-powered だから、Sub_K(X) は集合である。

ここで得たのは **well-poweredness** であって **co-wellpoweredness** ではない。二つを取り違えない。

### 2.2 strong epi–mono factorization

任意の f:A→B について、f が経由する B の K-subobjects 全体を交わらせる。その集合性は 2.1、交わりの存在は完備性による。得られる最小の部分対象を m:I→B とし、f=me と書く。

e は strong epi である。実際、mono n:C→D に対する e の lifting square から pullback mono P→I を作ると、e がこれを経由する。m に続けた部分対象 P→B は f を含むので、I の最小性から P→I は同型。これが対角射を与える。一意性は n の monicity による。

従って K には (strong epi, mono)-factorizations がある。以下 Im_K(f) はこの像を指す。

### 2.3 mono の directed colimit の安定性

λ-directed な mono 図式の colimit は E によって P の対応する colimit になる。P では pointwise な集合の union なので、colimit injections は mono。また、図式全体が一つの対象 X の部分対象図式なら、その union から X への比較射も mono である。

以下の像による分解に必要なのは、この比較射まで mono になる点である。

---

## 3. 全ての対象を、小さい始域からの像の union に分解する

H を、G の <λ 個の対象の余積を一つずつ選んだ集合とする。重複を許し、空余積も含める。正則性により H は <λ 個の余積について再び H に入る、という意味で閉じている。

### 補題 3.1：H の対象は λ-generated

Hom(∐_{j∈J}G_j,-) は |J|<λ 個の Hom(G_j,-) の積である。Set において λ-directed colimits と <λ 個の積は交換するので、各 H∈H は λ-generated。

### 補題 3.2：λ-generated objects は strong quotients で閉じる

strong epi e:H→B と mono の λ-directed colimit X=colim_i X_i を取り、f:B→X とする。

H の generatedness により fe はある i で H→X_i→X と因子化する。X_i→X は mono なので、e の strong lifting property により f は B→X_i→X と因子化する。colimit injection が mono であることから、Hom の比較射の単射性も従う。

従って B も λ-generated。

### 補題 3.3：任意の X は H からの像の λ-directed union

各 H∈H と各 f:H→X に対して Im_K(f)↪X を取る。これらは集合個である。H が集合で、各 Hom(H,X) が集合だからである。同じ部分対象を同一視して得た部分対象 poset を I_X とする。

<λ 個のそのような像に対し、対応する H_i の余積から X への射の像が共通上界となる。正則性からこの余積は再び H の対象である。従って I_X は λ-directed。

    U = colim_{I∈I_X} I

と置く。比較射 m:U→X は 2.3 により mono。任意の G∈G から X への射は、その射自身の像を経由するので m を経由する。G が strong generator であることから m は同型。

よって

    X ≅ colim_{I∈I_X} I

は λ-directed union で、各 I は H の対象の strong quotient、従って λ-generated である。

### 系 3.4：λ-generated objects の正確な表示

B が λ-generated なら、3.3 の B の union に対して id_B が一つの段階 I↪B を経由する。この mono は split epi でもあるので同型。従って B はある H∈H の strong quotient である。

逆向きは 3.2 で示した。すなわち

    {λ-generated objects}/≅
      = {strong quotients of members of H}/≅.

この等式は、右辺が集合であることを主張していない。

---

## 4. 必要なサイズ上界の必要十分性

presheaf F の大きさを

    ||F|| = Σ_{d∈Ob D} |F(d)|

とする。以下を条件 (Q) と呼ぶ。

> 各 H∈H について基数 b_H があり、全ての strong epi e:H→B に対し ||EB||≤b_H。

H 自体が集合なので、(Q) が成り立てば必要に応じて b_H の共通上界 b を取れる。

### 4.1 (Q) と局所的な商集合性

大きさ ≤b_H の D-presheaves は同型を除いて集合個である。E は fully faithful なので、(Q) があれば B は同型を除いて集合個、さらに Hom(H,B) の集合性から quotient arrows も H 上の同型を除いて集合個である。

逆に strong quotients が集合個なら、その codomain の ||EB|| の上限を取れば (Q) を得る。

### 4.2 小さい始域での商集合性から、任意の始域での商集合性

(Q) を仮定する。3.4 により λ-generated objects の skeleton A は小さい。

任意の X を固定し、3.3 の分解

    X = colim_i X_i

を一つ固定する。I は小さい λ-directed poset、X_i は A の対象と同型である。

strong epi e:X→Y に対し、e|_{X_i} の像を Y_i↪Y とする。X_i は H の strong quotient、X_i→Y_i も strong epi なので、Y_i も H の strong quotient、従って A の対象と同型である。

像の間の射は mono で、Y_i は同じ I 上の部分対象図式となる。U=colim_i Y_i→Y は mono。e は U→Y を経由するため、e の strong 性から U→Y は同型である。

従って e は、固定した X_i 図式から小圏 A 内の I-図式への自然変換の colimit として表せる。小圏 A と固定した小さい I に対し、そのような図式と自然変換は集合個しかない。従って X からの strong quotients は集合個である。

よって (Q) は K の weak co-wellpoweredness を与える。

### 定理 4.3：局所的上界判定

今回の前提のもとで、次は同値である。

1. K は locally presentable。
2. K は weakly co-wellpowered。
3. 条件 (Q)。
4. λ-generated objects は同型を除いて集合個。

(1)⇒(2) は locally presentable categories の標準的な co-wellpoweredness、(2)⇒(3) は上限、(3)⇒(2) は 4.2、(3)⇔(4) は 3.4 と Hom の集合性である。(2)⇒(1) に 1 節で明記した標準定理を使う。

つまり現在の残りは、任意の対象の全商を一度に扱うことではない。**集合 H の各対象の strong quotients だけを一様に抑えればよい。**

### 4.4 同値な「小さい像」の形

(Q) は次とも同値である。

> 各 H∈H について b_H があり、任意の f:H→X に対し、f が経由する K-subobject Y↪X を ||EY||≤b_H となるように取れる。

(Q)⇒この条件：Y=Im_K(f) とする。

逆向き：f 自体を strong epi H→B とすると、この Y↪B は strong 性により同型でなければならない。

従って必要なのは、標的によらない small-image / Löwenheim–Skolem 型の上界である。各固定 X の内部で像が集合個であること（3.3）と、全ての X に共通する上界があることを混同しない。

---

## 5. 二つの ZFC 肯定定理

### 定理 5.1：小さい始域の strong epi が regular epi なら肯定

全ての H∈H について、H を始域に持つ strong epi が regular epi だと仮定する。このとき K は locally presentable。

**証明。** 固定 H の regular quotient e:H→B は、その kernel pair R↪H×H の coequalizer である。K は well-powered なので可能な R は集合個。各 R の coequalizer は quotient arrow として同型を除いて一意である。従って H の strong quotients は集合個で、4.3 を適用できる。□

特に strong epi = regular epi が全体で成り立つ場合は肯定となる。regular epi–mono factorization がある場合や abelian の場合はこの範囲に入る。

これは必要条件ではない。例えば Cat は locally finitely presentable だが、次節の strong epi は regular ではない。

### 定理 5.2：reflector が mono を保存すれば肯定

1 節の reflector L:P→K が mono を保存すると仮定する。このとき K は locally presentable。

**証明。** strong epi e:H→B を固定する。P において

    EH --p--> Q --m--> EB

を通常の regular epi–mono image factorization とする。L を施し、LE≅Id_K を使うと

    H --Lp--> LQ --Lm--> B

を得る。Lm は仮定により mono。e は strong epi だから Lm は同型である。

Q は固定 EH の P における regular quotient である。そのような Q と quotient map は集合個しかない。従って B≅LQ および e≅Lp も集合個であり、4.3 を適用する。□

注意：これは L の accessibility を仮定した証明ではない。使ったのは L の mono 保存と、presheaf 圏の quotient smallness である。

### 5.3 reflector の mono 保存は自動ではない

P=Quiv、K=Set を、S を constant quiver (S --id,id--> S) に送る full embedding E により埋め込む。左随伴 L は graph の connected-component set、すなわち s,t の coequalizer である。E は全ての colimits を保存する。

頂点が {0,1} で辺がない quiver X と、同じ頂点に一本の辺 0→1 を加えた Y を取る。X→Y は componentwise mono。しかし

    L(X)={0,1} → L(Y)={*}

は mono でない。

この例では K=Set はもちろん locally presentable である。反例は Problem 3 ではなく、「この reflector は mono を保存するはず」という推論に対するもの。

---

## 6. 核対を数えるだけでは足りない：Cat での直接計算

J=[1] を 0 --a--> 1 という一つの非恒等射を持つ圏とする。n≥2 に対し、BC_n を巡回群 C_n の一対象圏、g_n を標準生成元とし、

    q_n:J→BC_n

を二つの対象を同一視し a↦g_n とする functor とする。

### 6.1 q_n は strong epi

mono functor m:C→D に対する lifting square

    J --u--> C
    |q_n     |m
    v        v
    BC_n--v->D

を考える。Cat の mono は対象上単射かつ faithful である。

m(u0)=m(u1) なので u0=u1=c。h=u(a):c→c と置く。可換性から

    m(h^n)=v(g_n^n)=id_(mc)

であり、faithfulness により h^n=id_c。従って g_n↦h は functor d:BC_n→C を定め、要求される対角射となる。一意性は m の monicity による。

よって q_n は strong epi。

### 6.2 全ての n≥2 で kernel pair は同じ

J×_{BC_n}J の対象は (0,0),(0,1),(1,0),(1,1) の四つ。非恒等射は

    (a,a):(0,0)→(1,1)

だけである。g_n≠1 なので (a,id) や (id,a) は入らない。この圏と J への二つの射影は n に依存しない。

この共通 kernel pair の coequalizer は、J の二つの対象を同一視して a を自由な自己射にする functor

    J→Bℕ

である。BC_n ではない。従って q_n は regular epi ではない。

異なる n の BC_n は非同型なので、同じ kernel pair が quotient を決定するという主張は strong epi には成立しない。

この例が否定するのは一段階の核対カウントである。族は可算集合であり、非 co-wellpoweredness も Problem 3 の反例も与えない。

この種の strong/regular の差と Cat での二段階分解は、1999 年の Bednarczyk–Borzyszkowski–Pawłowski、および Kawase–Nasu (2026) の導入とも整合する。上の特定の q_n と kernel pair の計算は本稿で直接示した。

---

## 7. 次に試した方法：regular quotient の超限反復

strong epi e:H→B を固定する。

    A_0=H,   f_0=e.

後続段階では

    R_α = A_α ×_B A_α,
    q_α:A_α→A_(α+1) = coeq(R_α ⇉ A_α),
    f_α = f_(α+1) q_α.

集合順序数の極限 δ では

    A_δ=colim_(α<δ) A_α

とし、f_δ:A_δ→B を誘導する。真のクラス長の colimit は取らない。各集合長での構成だけを用いる。

### 7.1 停止すれば完成する

各 q_α は regular epi、H→A_α は strong epi である。strong epi が合成と集合長の超限合成で閉じることによる。

また e=f_α(H→A_α) から f_α も strong epi である。ある段階で f_α が mono になれば、strong epi かつ mono なので同型。そこで B に到達し、e の regular-epi decomposition を得る。

q_α が同型であることと f_α が mono であることは同値である。coequalizer が同型なら kernel pair の二射影が等しく、f_α は mono だからである。

### 7.2 元の H 上の kernel pair は最初から安定してしまう

r_α:H→A_α とし、R=kerpair(e) とする。α≥1 について

    kerpair(r_α)=R.

実際、q_0 が R を coequalize するので R⊆kerpair(r_α)。一方 e=f_αr_α から kerpair(r_α)⊆R。

従って「H×H の部分対象が集合個だから kernel pair の増加が止まり、そのとき quotient tower も止まる」という論法は使えない。元の kernel pair は一段で既に安定しており、その後にも新しい対象 A_α の内部で新しい同一視が必要となり得る。6 節の Cat の例がその二段階版である。

### 7.3 generatedness を適用しようとして失敗する箇所

μ を正則基数として A_μ=colim_(α<μ) A_α を考える。通常の presentability を使う証明なら、G→A_μ を一つの A_α に持ち上げ、次段階で必要な同一視が行われることから f_μ の monicity を示す。

しかしここでの transition maps は regular epi であり、mono ではない。

    G が λ-generated

という仮定だけでは

    G→colim_α A_α がどこかの A_α を経由する

とは結論できない。この推論を入れると generatedness を presentability と取り違えることになる。

Kawase–Nasu (2026), Theorem 3.27 の証明では、まさに μ-presentability によってこの因子化を行っている。Corollaries 3.30–3.31 は locally κ-presentable 圏で κ という上界を与えるが、今回は locally presentable であることをこれから証明したいので、そのまま適用すれば循環する。

### 7.4 一様停止と局所的な quotient smallness の同値

条件 (T) を次とする。

> 各 H∈H に集合順序数 θ_H があり、任意の strong epi e:H→B について、上の canonical tower が θ_H 以下で停止する。

このとき

    (Q) ⇔ (T).

**(Q)⇒(T)。** H 上の strong quotient arrows の同型類は集合である。tower が停止していなければ、H→A_α は相異なる quotient classes を与える。

なぜなら α<β で H→A_α と H→A_β が H 上同型なら、H→A_α の epimorphicity により A_α→A_β はその同型そのものになる。ところが A_α→A_β が同型なら、最初の regular epi q_α は split mono でもあり、従って同型。これは停止していないことに反する。

quotient set の濃度より大きい Hartogs ordinal を θ_H に取れば、全ての e に共通する停止上界を得る。

**(T)⇒(Q)。** 任意の固定対象 A の regular quotient arrows は集合個である。2.1 と kernel-pair count による。

従って、固定した集合順序数 θ_H までの全ての regular-quotient chains は、H 上の同型を除いて集合個にまとめられる。後続段階では各既存対象の regular quotients の集合を取り、極限では既に得られた集合個の coherent chains の small colimits を取る。固定した集合長の再帰なので、全体も集合である。停止後は identity maps で延長してよい。

(T) により任意の B はこの候補集合の対象と同型となる。Hom(H,B) の集合性も使うと、strong quotient arrows が集合個となり (Q) を得る。□

注意：「各 e がどこかで止まる」と「始域 H ごとに全ての e を一様に抑える θ_H がある」は別である。今回は後者が必要である。前者さえ一般には今回証明していない。

---

## 8. VP が上界を与える場所

原著と 2018 年の論文は VP のもとで Problem 3 が肯定となることを述べている。今回の還元に沿うと、その作用点は (Q) である。

標準的なクラス圏の記法でその機構を説明する。固定 H の strong quotients e:H→B を、presheaf EB に EH の各元を定数として加えた、小さい signature の構造として符号化する。signature は D の sorts と structure maps、および EH の各元に対応する定数からなり、集合サイズである。

同型でない quotient structures の真のクラスがあれば、VP の構造埋め込みの形により、その二つの間に elementary embedding を得る。特にそれは pointwise injective な自然変換

    m:EB→EB',   m(Ee)=Ee'

を与える。E の fullness により m は K の mono B→B' に対応する。

しかし e'=me は strong epi なので m は同型でなければならない。quotients を互いに非同型に取ったことに矛盾する。これは VP の既知の bounded-category / co-wellpoweredness の帰結が今回のサイズ問題を解く仕組みである。

この説明では、通常の大きい圏と VP のクラス定式化を使っている。ZFC で VP を証明したり、任意の真のクラスの colimit を使ったりしているわけではない。厳密な集合論的定式化に関する既知の入力は原著 Corollary 6.8 に戻す。

**逆向きは未証明。** (Q) がなければ VP が失敗することは VP⇒(Q) の対偶だが、¬VP から (Q) の反例を構成したことにはならない。Problem 3⇒VP、Problem 3⇒可測基数の存在、ZFC 独立性などは今回一切結論しない。

---

## 9. 今回の証明の監査ポイント

- full reflective presentation と union 保存は原著の還元を入力としている。これを今回独立に再証明したとは言わない。
- E は右随伴として mono を保存する。一方 L は一般には mono を保存しない。定理5.2では明示的な追加仮定とした。
- Im_K(f) と presheaf image Im_P(Ef) を区別した。後者が K に属するとは仮定していない。
- 3.3 で「各固定 X に対する像の集合」は得たが、それを標的によらない集合にすり替えていない。
- strong quotient は λ-generated である。そこから λ-generated objects 全体の集合性を推論していない。
- regular epi は kernel pair で決まるが strong epi は一般には決まらない。具体的な反例を計算した。
- tower の kernel pairs は各 A_α×A_α の内部にあり、全段階の部分対象を一つの固定集合の部分集合とは扱っていない。
- 元の H 上の kernel pair の安定は tower の停止を意味しない。
- generatedness を epi の列に適用していない。
- (T)⇒(Q) では集合順序数の一様上界があることを明示的に使っている。
- 最後の locally presentable への移行には、既知の locally-generated theorem を明示して使った。未証明の一般命題を隠れた補題として使っていない。
- No.1、No.2 の主定理や条件付き反例には依存しない。
- ここにある標準的な還元や条件付き定理について、新規性を主張しない。

---

## 10. 次に解くべき肯定側の補題

最も直接の目標は、4.4 の small-image bound を、reflector の mono 保存を仮定せずに導くことである。

同値な別の目標は、7.4 の θ_H を、presentability や quotient smallness を仮定せずに構成すること。

証明を試す際の判定基準は具体的である。

- 「generated だから極限段階への射が前段階を経由する」と言ったなら、その図式が本当に mono 図式か確認する。
- 「kernel pair が同じだから同じ quotient」と言ったなら、その quotient が regular epi か確認する。
- 「像を取れば小さい」と言ったなら、K の像か P の像か、どちらの意味か確認する。
- 「Hartogs で止まる」と言ったなら、どの既に存在する集合を数えているか明示する。未証明の strong quotient set を数えてはならない。

このいずれかを新しい議論で補えれば肯定証明は進む。現時点でそれらを ZFC で補えないと証明したわけではない。

---

## 11. 確認した一次資料

### A. 問題と標準定理

J. Adámek and J. Rosický, *Locally Presentable and Accessible Categories* (1994), Open Problems 3, pp.295–296。原文と equivalent formulation は既存の `open-problems.pdf` および README に対応する。書籍の関連参照は Remark 1.72、Corollary 6.8。

DOI: https://doi.org/10.1017/CBO9780511600579.011

### B. 2018 年の位置づけ

L. Positselski and J. Rosický, *Nearly Locally Presentable Categories*, TAC 33 (2018), 253–264。導入 pp.253–254 が、weak co-wellpoweredness の削除と Open Problem 3 に言及する。

https://tac.mta.ca/tac/volumes/33/10/33-10.pdf

注意：nearly presentable と generated は異なる。同論文 Theorem 3.6 の VP 同値性を元の Problem 3 に転用していない。

### C. 2022 年の標準証明の確認

I. Di Liberti and J. Rosický, *Enriched Locally Generated Categories*, TAC 38 (2022), 661–683。arXiv:2009.10980v2。

https://arxiv.org/pdf/2009.10980

Definition 2.3、Lemmas 2.12–2.13、Theorems 2.18, 2.24、Remark 2.27 を確認。特に Theorem 2.18 の証明では、small orthogonality presentation の集合性および E-quotients の cointersection にサイズ条件が入る。Remark 2.27 は Problem 3 との関係と VP の必要性が不明であることを明記する。

### D. 2026 年の regular-decomposition の上界

Y. Kawase and H. Nasu, *On the decomposition of a strong epimorphism into regular epimorphisms*, arXiv:2604.05744v1 (2026-04)。

https://arxiv.org/pdf/2604.05744

導入、Corollaries 3.22–3.24、Theorem 3.27、Corollaries 3.30–3.31 を確認。Theorem 3.27 の証明、印刷 p.27 は μ-presentability により極限への射を前段階に持ち上げている。したがってこの上界を今回の前提にそのまま適用しない。

### E. historical tower reference

J. MacDonald and A. Stone, *The tower and regular decomposition*, Cahiers de topologie et géométrie différentielle catégoriques 23(2) (1982), 197–213。

https://www.numdam.org/item/CTGDC_1982__23_2_197_0.pdf

Proposition 1.7 の chain-colimit 仮定には possibly large chains が含まれる。small cocompleteness だけからそのまま使わない。

これらの確認は現在までの全論文の網羅的調査ではない。2022 年に関連問題が明記され、2026 年の関連する分解論文が上記の強い仮定を使うことを確認した、という範囲である。
