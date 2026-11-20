# Problem 4：肯定方向の第1段階 — 定義可能性、局所 hull、巨大基数の上界

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下の適用・直接補題を書き下して自己点検した段階。独立査読・形式検証・文献上の新規性確認は未実施。一般の P4 に対する WVP より弱い一様十分条件、ZFC 解、最適な巨大基数強度は今回未確立。**

**2026-11-18 続編：** [小さい反射と strong quotients](positive_small_reflections_and_strong_quotients_2026-11-18.md) で、(SH) と A の局所可呈示性との同値、小さい自由 source の反射からの大域化、Σ1 の ZFC における局所可呈示性、および Σ2＋regularity の下での単一 strong cardinal の十分性を整理した。反射性だけに必要な弱い条件は [普遍近似の停止](positive_universal_approximants_and_stabilization_2026-11-18.md) に分離している。一般 P4 は引き続き未解決。

## 0. 要点と区別

P4：局所可呈示圏 K の full replete subcategory A が K の全小極限と directed unions に閉じていれば、A は K に反射的か。

今回の肯定結果は次の二系統。

1. **Product Reflection の適用。** 標準的な前層／構造表示で A の対象クラスが集合パラメータ付き Lévy Σ1 なら ZFC で反射的。Σ2 なら strong 基数の真クラスから反射的。Σ_n (n>=2) なら Σ_n-strong 基数の真クラス（同値な一様原理として Π_(n-1)-strong 基数の真クラス）から反射的。この系統は directed-union 閉性を使わず、全小極限閉性だけでよい。
2. **Union を使う局所から大域への構成。** A が Σ2 であれば、固定した signature・パラメータ・union rank より大きい **一つの supercompact** から、全ての X の反射が存在する。小さい seed の A-hull を一様に抑え、任意の seed の hull をその directed union として作る。さらに strong-quotient smallness を示し、A 自身の局所可呈示性まで得る。

重要な限定：

- Σ1/Σ2 は集合論の Lévy hierarchy。構造内部の一階／無限論理の量化複雑性ではない。
- 一般の P4 の仮定から A が Σ2 と導いたわけではない。従って「strong 基数の真クラス ⇒ unrestricted P4」は未証明。
- strong、strongly compact、almost strongly compact、supercompact は別物。単一 supercompact の結果を WVP より弱い巨大基数上界と呼ばない。
- 一つの strong κ は、定義パラメータと source X のコードが V_κ に入る場合の X の反射を与える。全 X に同じ κ を使う結論は、この PRP の証明からは得ていない。
- No.1/2 の反例・独立性、および No.3 の反例候補を入力にしていない。No.3 で問題となった『generated strong generator から full reflective presheaf presentation』も使用しない。

## 1. 安全な母圏の還元

局所可呈示な母圏 K には、小圏 D に対する標準的な full reflective presentation

    K --E--> P = Set^(D^op)

があり、E は全小極限と、ある正則 λ0 に対する λ0-filtered colimits を保存する。これは K の局所可呈示性を既知の仮定として使うもので、No.3 の問題のある還元とは違う。

λ>=λ0 を正則に取り、必要なら |Mor D|<λ とする。A が K 内で directed unions に閉じていれば、E(A) は P 内で λ-directed unions に閉じる。実際、E(A) のそのような mono diagram は fullness により K の図式であり、K の colimit は A に入り、E がその colimit を保存する。

従って以下では P の full replete subcategory A を扱う。P の全小極限と λ-directed unions に閉じると仮定する。対象の大きさ ||A|| は全 sort の台集合の非交和の濃度。

定義可能性の仮定は **この構造表示での対象クラス**について課す。任意の抽象的な表示変更が同じ複雑性を保つと無条件には主張しない。

## 2. 完備 comma category と Product Reflection

### 2.1 反射を求める正しい comma category

X∈P を固定し、

    D_X = (X ↓ A)

とする。A は全小極限閉なので D_X は完備かつ局所小。終対象 1∈A があるため非空でもある。

D_X の初対象が、まさに X の A-reflection である。

### 2.2 弱始集合から初対象

完備な局所小圏 D が弱始集合 S を持てば、P=∏S は弱始対象。End(P) は集合なので、id_P と全自己射を同時に等化する

    i:R → P,    u i = i for all u:P→P

を取れる。弱始性から f:P→R が存在し、u=if を用いると ifi=i、従って fi=id_R。

任意の v:R→R に対し ivf は P の自己射なので ivfi=i、従って iv=i、v=id_R。R は弱始でもある。二射 g,h:R→Z の等化子 j:Q→R に対して弱始性から k:R→Q があり、jk=id_R。よって g=h。従って R は初対象。

この証明は外部の proper-class choice や accessibility を仮定しない。

### 2.3 D_X の構造としての符号化

P は D の対象を sorts、D の射を unary operations とする小さい多ソート言語で表せる。f:X→A を表すため、各 d と x∈X(d) に定数 c_(d,x) を加え、これを f_d(x) と解釈する。定数が X の構造写像と整合する条件を課す。

この拡大言語の homomorphisms は、ちょうど X 上の可換三角である。射・関手法則・定数整合性の検査は標準的な有界／Δ1 符号化で行えるため、A が Σ_n(p) なら D_X も Σ_n(p,D,X)。Σ1 の場合も保存する。

PRP は関係構造の言語で述べられる。単項演算を graph relations に置き換え、空 sort がある場合には dummy 点と sort predicates を使う。通常の一ソートの関係積には異なる sorts の混合 tuple も含まれるが、同じ sort の tuple の部分に制限すると P における積を得る。PRP の homomorphism をその部分に制限すれば、D_X における積からの射になる。『符号化が通常の積をそのまま保存する』とは仮定しない。

### 2.4 PRP の適用

PRP により集合 S⊆Ob(D_X) が得られ、∏S から D_X の全対象への射があれば、この積は D_X 内の弱始対象。2.2 から初対象、従って X の反射が得られる。D_X が essentially small の場合はその代表集合を直接使えばよい。

使用する既知の結果は Bagaria–Wilson (2023)：

- Proposition 3.2：bold Σ1-PRP は ZFC の定理。
- Proposition 3.3：strong κ から Σ2(V_κ)-PRP。
- Corollary 3.4：strong 基数が真クラスなら bold Σ2-PRP。
- Proposition 5.10：Σ_n-strong κ から Σ_n(V_κ)-PRP (n>=2)。
- Theorem 5.13：パラメータを許す bold Σ_n-PRP は、Σ_n-strong 基数の真クラス、または Π_(n-1)-strong 基数の真クラスと同値 (n>=2)。

従って今回の直接適用として：

**定理 A。** 全小極限閉な A⊆P について、A が Σ1 なら ZFC で反射的。A が Σ2 なら strong 基数の真クラスの下で反射的。一般の Σ_n (n>=2) には上記の階層が十分。

さらに、固定 X と D,p のコードが V_κ に入り κ が strong なら、Σ2 の A に対するその X の反射は存在する。

これは定義可能性を限定した十分条件であり、P4 の converse や最適性は主張しない。BW の一般 PRP の強度計算が、union-closed なクラスに限った P4 の必要条件になるとも主張しない。

## 3. Directed unions を使う ZFC の局所 hull 補題

### 3.1 Hull の存在

B∈A、S⊆UB（sort-tagged underlying carrier）とする。P の B の部分対象で、S を含み、かつその domain が A に属するものを全て交わらせる：

    cl_B(S) = ⋂ {C⊆B : C∈A and S⊆UC}.

P は well-powered で、この族は B 自身を含む集合。A の全小極限閉性により cl_B(S)∈A。ここで反射の存在は使用しない。

### 3.2 Union continuity

A が λ-directed unions に閉じるなら、

    cl_B(S) = ⋃_{T∈[S]^{<λ}} cl_B(T).                 (H)

実際、右辺の図式は λ-directed（λ の正則性）。各項は A に入り、右辺は A-object で S を含むから cl_B(S) を含む。逆の包含は各 T⊆S についての最小性から従う。

### 3.3 小さい seed の一様な上界から解集合

次の条件を仮定する：

    ある集合基数 ν があり、全 B∈A と全 |T|<λ に対し
    ||cl_B(T)|| ≤ ν.                                  (SH)

μ=max(λ,||X||) とする。任意の f:X→B、B∈A は

    X → cl_B(im f) ↪ B

と因子化し、(H) により

    ||cl_B(im f)|| ≤ max(ν, μ^{<λ}).                    (B)

この大きさ以下の presheaves の同型類は集合個。A に属するものの代表と、それらへの X からの全ての射を集めれば D_X の弱始集合を得る（全射・epimorphism だけに限定しない）。

**定理 B（ZFC）。** 全小極限閉性、λ-directed-union 閉性、(SH) から A の反射性が従う。

重要：**(SH) を反射性と同値とはしていない。** 一般に反射 R が存在しても、R(P) の A-strong quotients が自動的に集合個とは限らない。ここを逆向きに推論すると No.3 の未解決な reflective-formulation のサイズ問題を紛れ込ませる。

## 4. Σ2 の場合：一つの supercompact で全対象の反射

A の対象クラスを Σ2(p) とし、D,p,λ の固定データを上回る supercompact κ を一つ仮定する。

使用する既知の入力は Bagaria–Casacuberta–Mathias–Rosický (2015), Theorem 5.2(a)：小さい始域 Q∈V_κ から A-object B への射は、A∩V_κ の対象と elementary embedding を経由する。

任意の B∈A と |T|<λ を取る。T が生成する部分前層 Q⊆B は ||Q||<κ。実際、|Mor D|<κ と κ の正則性から従う。Q の実際の元は高い rank を持ち得るので、**小さい同型コピー Q0∈V_κ** を選び、Q0→B に外部定理を適用する：

    Q0 → C0 --e--> B,
    C0∈A∩V_κ,   e elementary.

e の像 C は A の部分対象で、T を含み ||C||<κ。A は replete としている。従って

    ||cl_B(T)|| < κ

が全 B,T に一様に成り立つ。(SH) に ν=κ を入れればよい。

**定理 C。** Σ2 の A が全小極限と λ-directed unions に閉じていれば、固定データより上の一つの supercompact κ から A の反射性が従う。source X は κ より大きくてもよく、κ を X ごとに選び直さない。

明示的な解集合の carrier bound は

    b_X = max(κ, (max(λ,||X||))^{<λ}).

特に前層表示で全 directed unions に閉じる場合は λ=ω として、b_X=max(κ,||X||,ℵ0) とできる。|Mor D|<ω は不要であり、固定 signature の大きさが κ 未満なら小さい seed の生成部分前層は κ 未満になる。

### 4.1 局所可呈示性までの強化

上記の (B) は任意サイズの seed を含む小さい A-subobject を与える。A 内の strong epi q:C→B に適用すると、

    C → cl_B(im q) ↪ B

の mono factor は strong 性によって同型。従って、固定 C の全 strong quotients の carrier に b_C という上界がある。A は strong epis に関して co-wellpowered。

既に得た反射により A は cocomplete。P の representables の反射 R(yd) は small strong generator をなし、包含 A→P が λ-directed mono-colimits を保存するため λ-generated である。ここで標準の、**co-wellpoweredness を含む** locally-generated characterization を適用して A は locally presentable。

この段階は『generated strong generator だけで bounded』とは推論せず、必要な strong quotient smallness を先に証明している。

### 4.2 大きさと強さの区別

定理 C は『一つの supercompact が十分』という fixed-instance の改善である。『supercompact が WVP より弱い』という強度比較ではない。また、Σ2 の仮定を外した arbitrary A に一つの supercompact が十分ともしていない。

より高い定義可能性には BCMR Corollary 6.6(a) の C^(n)-extendible を使って同じ hull の証明を適用できるが、今回の弱い上界の主眼は定理 A の strong/Π_n-strong 側である。

## 5. コンパクト性の素朴な近道を検査する対照例

以下は **P4 の反例ではない**。ZFC で反射的なクラスを使い、『union 閉性が指定した rank の purity/reduced-power 閉性を直ちに与える』という主張だけを否定する。

正則無限 θ を固定する。3 sorts R,V,W、演算

    a:R→V,  r:W→R,  p_i:W→V (i<θ)

を持つ unary presheaf category P_θ を取る。

A_θ を次の条件を満たす対象の full subcategory とする：

    ∀x∈R, ∃!w∈W : r(w)=x and ∀i<θ, p_i(w)=a(x).      (*)

U は root x と a(x) のみを持つ構造、V_test はさらに w を加えて r(w)=x と全 p_i(w)=a(x) を課した構造とする。s:U→V_test に対して A_θ={s}^⊥。

従って A_θ は小さい orthogonality class で ZFC で反射的、全小極限閉。U,V_test は finitely generated なので全 directed unions にも閉じる。直接にも、root と witness は一つの stage に現れ、mono によって全 p_i の等式が stage に反映されるので (*) が保存される。

### 5.1 θ-pure subobject が外れる

B の R={x}, V={0,1}, a(x)=0 とし、

    W_B={*} ⊔ {w_T : T⊆θ, |T|<θ},
    r(w)=x,
    p_i(*)=0,
    p_i(w_T)=0 if i∈T, and 1 otherwise.

とする。B は (*) を満たす。唯一の good witness は *。

A0⊆B を * だけを除いた部分前層とする。A0 は A_θ に属さない。しかし A0→B は θ-pure。

証明：前層圏の θ-presentable objects は、<θ 個の生成元と <θ 個の関係による表示の retract として扱える。pure lifting square の上側三角を解くための方程式系を、このような表示で書く。B 内の解で * に送られる W-sort の未知数を全て、一つの w_T に置き換える。系に現れる p_i の添字は <θ 個なので、それらを含む |T|<θ を選べる。既存のパラメータは固定する。r と a の条件は変わらず、記載された p_i の値は 0 のまま、* 同士の等式も維持される。* と既存 w_S を同一視する等式は元の B の解で成立しないため問題にならない。従って上側三角を A0 内で解ける。retract を取る場合も purity は保たれる。

従って

    limits + all directed unions

だけから、あらかじめ指定した θ における θ-pure-subobject 閉性を推論できない。

### 5.2 θ-complete reduced powers にも閉じない

I=[θ]^{<θ} 上の fine filter F を、基本集合

    ↑S={T∈I : S⊆T},  |S|<θ

で生成する。θ の正則性から F は proper θ-complete。

B^I/F において u(T)=w_T と定数関数 *(T)=* は異なる同値類を持つ。しかし全 i<θ について p_i([u])=[0]、かつ r([u])=[x]。従って [u] と [*] は同じ root の二つの good witnesses になり、A_θ の一意性条件が壊れる。

F を延長する θ-complete ultrafilter が存在する場合にも同じ計算が成立する。これは strong compactness そのものの反証ではなく、『この閉性から ultraproduct/reduced-power 閉性は自動』という推論の反証である。

### 5.3 この対照例の正確な限界

- signature とクラスは θ に依存する。一つの固定 A で全 rank の pure 閉性が失敗する例ではない。
- 特に『十分大きい κ を signature より上に選べばよい』という可能性を、この例だけで否定していない。
- A_θ はそもそも小さい orthogonality class。P4 の反例でも、巨大基数下界でもない。
- 指定した小さい purity rank をそのまま使うこと、または reduced product を A に属すると無検査で扱うことだけを排除する。

## 6. 今回未確立のものと残る核心

以下はいずれも今回証明していない：

    ZFC ⇒ unrestricted P4,
    proper class of strong cardinals ⇒ unrestricted P4,
    proper class of strongly compact cardinals ⇒ unrestricted P4,
    proper class of almost strongly compact cardinals ⇒ unrestricted P4,
    proper class of measurable cardinals ⇒ unrestricted P4.

この研究段階での一般形の十分条件は、既知の WVP のままである。新しく明確にしたのは、低い定義可能性を持つ instances の弱い十分条件と、union 閉性を実際に使う hull の一様化である。

今後の十分目標は二つを区別する必要がある。

(A) **直接の解集合。** D_X=(X↓A) に対する Product Reflection を、A の任意の定義複雑性に依存しない弱い原理で得る。これは P4 の結論に近く、無条件の PRP を再要求すれば WVP に戻ってしまう。

(B) **より強い small-hull route。** 全 B の <λ-seed の A-hull を一様に抑える。この場合は反射性だけでなく、上記の議論で局所可呈示性も得られる。従って必要以上に強い結論を要求している可能性を意識する。単なる反射性と同値だとはしていない。

strong/almost-strong compactness の標準的な powerful-image theorem は、入力となる accessible functor や set-sized theory を先に必要とする。一般の A をそのような powerful image として既に表示できる、と置くのは今回の不足を仮定に隠すことになる。

## 7. 参照資料と確認範囲

1. J. Adámek and J. Rosický, Locally Presentable and Accessible Categories (1994), Open Problems, p.296, Problem 4。原文はこのチャットの前段で Library の user-provided PDF とページ画像で確認済み。今回 web では出版社の章情報まで確認した。
2. J. Bagaria and T. M. Wilson, The Weak Vopěnka Principle for Definable Classes of Structures, JSL 88 (2023), 145–168, DOI 10.1017/jsl.2022.42。
   https://diposit.ub.edu/server/api/core/bitstreams/5ac83f7a-9752-4a28-bf65-31c2d878692a/content
   Proposition 3.3 と Theorem 5.13 を本文および pp.151,167 の screenshot で確認。定理 A はその直接適用として本稿で証明し、新規性は主張しない。
3. J. Bagaria, C. Casacuberta, A. R. D. Mathias, J. Rosický, Definable orthogonality classes in accessible categories are small, JEMS 17 (2015), 549–589, DOI 10.4171/JEMS/511。
   https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content
   Theorems 5.1(a),5.2(a), Corollary 6.6(a)。pp.562–563 の screenshot で確認。定理 C は 5.2(a) と本稿の hull 補題の組合せ。
4. J. Adámek and J. Rosický, On reflective subcategories of locally presentable categories, TAC 30 (2015), 1306–1318。
   https://www.tac.mta.ca/tac/volumes/30/41/30-41abs.html
   λ-filtered colimits の一般反射定理と directed unions の区別の背景。今回この論文の新しい詳細定理は入力にしていない。
5. A. Brooke-Taylor and J. Rosický, Accessible images revisited, arXiv:1506.01986v2; Proc. AMS 145 (2017), 1317–1327。
   https://arxiv.org/abs/1506.01986
   accessible functor の powerful image に対する compactness theorem の適用範囲のみ確認。本稿ではこの定理を一般 A に適用していない。

## 8. 優先監査箇所

- D_X の符号化と Product Reflection から comma の弱始対象への移送。空 sort と通常の関係積の混合 tuple を区別する。
- 全小極限閉性から hull の交わりが A に属すること。ambient well-poweredness を用い、A の未知の co-wellpoweredness は仮定しない。
- (H) に用いる directedness が λ-directed であること。
- 小さい carrier と V_κ 所属を混同せず、Theorem 5.2 には小さい同型コピーを入力すること。
- 単一 supercompact を X に依存させていないこと。
- 定理 C の locally-presentable 強化で、strong quotient smallness を先に証明したこと。
- 対照例の θ-purity が <θ 個の関係による表示に基づくこと、signature が θ に依存するという限界。

以上の新しい導出は自己点検段階であり、外部検証済みの新定理とは扱わない。

## 9. 最終照合（同日）

定理 C の局所可呈示性への最後の標準入力を、Positselski–Rosický, *Nearly Locally Presentable Categories*, TAC 33(10) (2018), p.253 の Introduction と照合した。同論文は、余完備性・λ-generated strong generator・各対象の strong quotients が集合個という三条件から、局所可呈示性を明記している。

https://www.tac.mta.ca/tac/volumes/33/10/33-10.pdf

利用したのは p.253 の **strong quotient smallness を仮定する**標準定理のみ。次ページの、これを VP の下で省略するという Problem 3 に関する記述は、今回の証明の入力にしていない。本文抽出は成功したが、このURLの今回の screenshot は timeout だった。

Bagaria–Wilson の出版版 Proposition 3.3/Corollary 3.4 (p.151) と Theorem 5.13 (p.167)、BCMR Theorem 5.2 (p.563) は再度ページ画像で照合した。仮定の階層・boldface（集合パラメータ）・単一κと真クラスの区別は上記のままである。
