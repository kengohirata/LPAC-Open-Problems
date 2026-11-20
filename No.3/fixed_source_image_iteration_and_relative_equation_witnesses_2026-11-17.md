# No.3：固定始域の強商、反射像の反復、等式の相対的な証人

2026-11-17。

**状態：PROOF_RECONSTRUCTED。以下の直接証明を主担当が展開・再点検した段階。独立査読・形式検証・文献上の新規性確認は未実施。一般の P3 の肯定・否定・独立性、新しい一般的巨大基数上界はいずれも得ていない。**

依頼：前段階の方針を維持し、固定した H の強商と pure hull から生じる r:LA→B の「新しい等式」を局所化する。一般の reduced-power diagonal の monicity には戻らない。

## 0. 今回の結論

1. **一段階の等式局所化は完了した。** A⊂EB に対し、c_B(A)=Im_P(E(LA→B)) と置くと A⊂c_B(A)。その包含を反射した LA→L c_B(A) は、r_A:LA→B の kernel pair の coequalizer である。従って r_A が同一視する二射を全てこの一段階で同一視し、それ以外の二射は同一視しない。しかも |c_B(A)|≤|ELA|。標的 B に依存しない一段階の濃度上界が、A を固定すれば得られる。
2. **purity は、新しく追加される元の個数に使える。** κ>|Mor D| を正則とする。i:A⊂EB が κ-pure で、c_B(A)\A の全 sort 合計の濃度が κ 未満なら、r_A は mono。固定 H の強商を因子化している場合は同型。従って失敗例には、一段階で少なくとも κ 個の新しい ambient 元が必要になる。A 自体が κ 未満とは要求しない。
3. **各標的に対する反復停止は ZFC で証明できる。** A_(α+1)=c_B(A_α)、極限で ambient union を取る。固定 EB の部分前層の増大列なので、μ=max(aleph_0,|EB|) に対して μ^+ より前に停止する。停止対象は A_0 を含む最小の K-subobject of B。
4. A_0 が固定 strong epi q:H→B の ambient image を含むなら、その停止対象は EB 全体。特に A_0=Im_P(Eq) から出発すれば、反射した列（初期の H→LA_0 を含む）は canonical な regular-epi quotient tower を与え、各 q は集合長で実際に停止する。
5. **残るのは始域ごとの一様な停止上界。** μ^+ は B に依存する。固定 H の全強商に共通の集合順序数上界は未証明。既存の (Q) と同値であるが、以前未確立だった「各 q ごとの停止」は本稿で確保した。
6. 元の local-union 保存から、最終的な local-subobject closure は λ-directed unions を保存すると示せる。しかし一段階の c_B が同じ union を保存するとは導けない。最終閉包の連続性と、一段階の濃度上界だけでは、一様な反復長は一般の順序論では従わない。明示的な対照作用素を示した。

No.1/2 の反例、N、ultrafilter、巨大基数は今回の新証明に不要。

---

## 1. 設定と表記

No.3 の既存の還元を採用する：

    L : P=Set^(D^op) <-> K : E,    L ⊣ E,

E は full faithful。D は小圏で、K の replete image を P の中で局所対象と呼ぶ。式では counit LE≅Id_K と Lη≅Id_L による標準同型を省略する。

No.3 の元の仮定により、ある正則無限 λ と集合 G があり、G は λ-generated strong generator。E は K 内の λ-directed mono diagrams の colimits を保存する。

K は complete、cocomplete、well-powered。完備性と局所対象の ambient limit 閉性は reflection の通常の性質。E は limits を保存し、P の monos は sortwise injections。

|A| は全 sorts の台集合の非交和の濃度。A⊂EB は ambient subpresheaf であって、A が局所対象とは仮定しない。

H は G の <λ 個の余積からなる集合。既存の還元

    K is locally presentable
    iff every H∈H has a set of strong quotients
    iff their E-carriers have a uniform set-cardinal bound for each H

を維持する。以下の §§2–5 の多くは generatedness を使わず、任意の full reflection into a presheaf category で成立する。どこで No.3 の追加仮定を使うかを分ける。

---

## 2. 反射像による一段階作用素

B∈K、i_A:A↪EB を固定し、その adjoint transpose を

    r_A:LA→B,    E(r_A)η_A=i_A

とする。P における image factorization を

    ELA --p_A--> c_B(A) --m_A--> EB

と書く。p_A は sortwise surjection、m_A は inclusion。

### 補題2.1：基本性質

(a) A⊂c_B(A)。この inclusion k_A:A→c_B(A) は

    k_A=p_Aη_A

である。

(b) A⊂A'⊂EB なら c_B(A)⊂c_B(A')。

(c) |c_B(A)|≤|ELA|。

(d) B→B' が K の射 f なら、ambient image に関して

    Im_P(Ef(c_B(A))) ⊂ c_(B')(Im_P(Ef(A))).

**証明。** (a) は m_Ap_Aη_A=i_A が inclusion であること。(b) は r_A=r_(A') L(A→A') により像が含まれること。(c) は p_A の全射性。(d) は A→Im(Ef(A)) の反射と、f r_A の factorization に対し同じ像の包含を使う。□

c_B は extensive かつ monotone だが、一般に idempotent ではない。ここでは final closure と区別する。

### 定理2.2：Lk_A は kernel-pair coequalizer

K 内で

    e_A=L(k_A):LA→L c_B(A)

は r_A の kernel pair の coequalizer である。特に regular epi。

**証明。** R=LA×_B LA とする。E は kernel pairs を保存するので

    ER=ELA×_(EB)ELA=kerpair_P(p_A).

P の image quotient p_A はこの kernel pair の coequalizer。L は coequalizers を保存し、ER と ELA は局所対象なので、L p_A は K 内で R⇉LA の coequalizer。

一方 k_A=p_Aη_A であり、Lη_A は canonical isomorphism。従って Lk_A は、上の Lp_A と同一視できる。□

ここでは E が epis や coequalizers を保存すると仮定していない。むしろ E がそれらを保存しない可能性が、次段階での新しい値・等式の原因となる。

### 系2.3：等式は正確に一段階で局所化される

任意の Z∈K と u,v:Z→LA について

    r_A u=r_A v  iff  e_A u=e_A v.

従って

    kerpair_K(e_A)=kerpair_K(r_A).

**証明。** 右から左は r_A=r_(c_B(A)) e_A。左から右は、p_A が E(r_A) と同じ kernel pair を持つこと、または定理2.2から従う。□

これは generator からの二射だけに限らない。A を固定すれば、標的 B の大きさと無関係な |ELA| 以下の ambient extension c_B(A) に、r_A の全等式を一度に移せる。

ただし、これから r_(c_B(A)):L c_B(A)→B が mono とは言えない。次の反射には、LA から lift できない新しい元・新しい射があり得る。kerpair(e_A)=kerpair(r_A) から残りの factor の monicity を導くのは、一般には誤りである。§8の Cat の例を参照。

---

## 3. Pure inclusion と「追加される元」の下界

正則無限 κ>|Mor D| を固定する。i:A⊂EB が categorical κ-pure であるとする。

### 補題3.1：小さい相対拡張は split する

A⊂C⊂EB とし、

    sum_d |C(d)\A(d)| < κ

と仮定する。このとき k:A→C は P 内の split mono。

**証明。** C\A の全元を構造写像で閉じて得られる subpresheaf D_0⊂C を取る。|Mor D|<κ と κ の正則性により |D_0|<κ。また C=A∪D_0。

D_0∩A と D_0 は κ-presentable。i の purity を

    D_0∩A ---> A
       |         |i
       v         v
      D_0 -----> EB

に適用すると、D_0∩A 上で inclusion に一致する t:D_0→A を得る。presheaf の union は intersection に沿う pushout なので、t と id_A を貼って C→A を作れる。これは k の retraction。□

A 自体のサイズに制限はない。必要なのは新しく追加された元の集合が κ 未満であること。

### 定理3.2：少ない新元しか生じない場合は RP を局所的に証明できる

上の pure inclusion に対して

    sum_d |c_B(A)(d)\A(d)| < κ

なら r_A:LA→B は mono。

**証明。** 補題3.1により k_A は split mono。従って Lk_A は split mono。一方定理2.2により Lk_A は regular epi。よって同型。

系2.3から kerpair(r_A) は diagonal。従って r_A は mono。□

### 固定 H の強商に対する帰結

q:H→B が strong epi、Im_P(Eq)⊂A なら、随伴により q=r_A a と書ける。q の strong 性により、r_A が mono なら r_A は同型。

従って上の相対的サイズ条件だけで

    B≅LA

が従う。強商の証明で必要なのはこの結論。

対偶として、今回扱う特殊な失敗例には必ず

    r_A nonmonic  =>  sum_d |c_B(A)(d)\A(d)|≥κ

が成立する。以前の「A の pure hull は κ 以上になり得る」という話より強い。ここで数えるのは A の古い元ではなく、**A の反射像が B 内で新たに生む元**である。

より一般に、r_A が潰す相異なる u,v:Z→LA を L(A→C) も潰すなら、C\A は κ 未満ではあり得ない。小さい相対拡張は反射後も split mono になるため。

この下界自体は、生成性から新元の数が κ 未満になることを証明したものではない。一般の RP や P3 はまだ得られない。

---

## 4. 反復は固定標的ごとには必ず停止する

任意の A_0⊂EB から出発し、集合順序数について

    A_(α+1)=c_B(A_α),
    A_δ=union_(α<δ) A_α   (δ a nonzero limit)

と定める。

### 補題4.1：fixed points は局所部分対象に一致する

c_B(A)=A iff A は局所対象（EB の K-subobject）である。

**証明。** A が局所なら r_A は元の inclusion と同型なので c_B(A)=A。

逆に c_B(A)=A とする。p_A:ELA→A は p_Aη_A=id_A を満たす。局所対象 ELA への二射 η_Ap_A と id_(ELA) は η_A の後で一致する。反射の普遍性による一意性から η_Ap_A=id_(ELA)。従って η_A は同型で A は局所。□

### 定理4.2：標的依存の停止上界

μ_B=max(aleph_0,|EB|) とすると、ある τ<μ_B^+ で

    A_τ=A_(τ+1)

となり、その後は一定。A_τ は A_0 を含む最小の K-subobject of B。

**証明。** 全ての A_α は固定した EB の subpresheaves。もし μ_B^+ 個の successor steps で strict に増加すれば、各差集合 A_(α+1)\A_α から一元を選ぶことで μ_B^+ から EB の全 sort の非交和へ injection ができ、矛盾。これは集合長 μ_B^+ の再帰だけを使う。

一度等号が起きれば c_B の fixed point なので、その後は一定。補題4.1より局所。A_0 を含む任意の局所部分対象 D⊂EB は c_B(D)=D を満たすため、monotonicity と超限帰納法により全 A_α を含む。従って停止対象は最小。□

重要：数えているのは **既に与えられた EB の元**であり、未証明の「H の強商の集合」ではない。その代わり、上界は B に依存している。

### 系4.3：固定 strong epi の場合、停止対象は EB

q:H→B strong epi とし、Im_P(Eq)⊂A_0 とする。停止対象 A_τ は局所で、q はその包含 A_τ→EB に対応する K-mono を経由する。strong 性からこの mono は同型。従って

    A_τ=EB.

つまり、各個別の q と A_0 について、この構成は必ず B 全体まで到達する。

---

## 5. これは canonical regular-epi tower の具体的な実装になる

strong epi q:H→B に対し

    A_0=Im_P(Eq),   X_α=L A_α,
    r_α:X_α→B

とする。

初期射 H→X_0 は、P の image quotient EH→A_0 を反射したもので、K 内の kerpair(q) の coequalizer。

各 successor の

    X_α→X_(α+1)

は定理2.2により kerpair(r_α) の coequalizer、従って regular epi。

極限 δ では、L が colimits を保存するので

    X_δ=L(union_(α<δ) A_α)≅colim_(α<δ) X_α.

よって、初期の H→X_0 を含めた列は canonical な regular-epi decomposition の列である。各 H→X_α は strong epi（regular epi の集合長の超限合成）であり、r_α も q=r_α(H→X_α) の右消去により strong epi。

§4により、この列は集合長で B に到達する。r_α が既に mono ならその時点で同型であり、ambient-image 列は遅くとも次段で EB に等しくなる。従って停止段階を一つずらしても、μ_B^+ 未満という上界は維持される。

### 更新される以前の未解決箇所

`positive_quotient_bounds_and_regular_towers_2026-11-17.md` §7.4 は、一般の strong epi の個別停止も当時未証明としていた。

**今回の presheaf reflection の設定では、個別停止は本稿で証明した。残るのは H ごとの一様停止である。**

この結論は No.3 の generatedness を使わず、任意の full reflective subcategory of a presheaf category に適用できる。局所可呈示性を前提として使っていない。

regular decomposition 自体は古典的な機構であり、本稿は新規性を主張しない。MacDonald–Stone (1982) §1 および Kawase–Nasu (2026) §§2–3 の canonical construction と比較した。本稿の個別停止は、既知の LP 性を使った停止上界を引用しているのではなく、ambient images の増大を固定 EB 内で数える直接証明である。

---

## 6. 始域ごとの一様化に残る正確な量化

反復の最終閉包を cl_B(A) と書く。

固定 H について、A_0=Im_P(Eq) からの到達段階を τ(q) とする。§4により全 q について τ(q) は集合順序数である。

しかし必要なのは

    exists θ_H, for every strong epi q:H→B,  τ(q)≤θ_H.

標的 B に依存する μ_B^+ は、この量化を満たす上界ではない。

### 6.1 一段階のサイズ上界は一様に定義できる

無限基数 μ に対し、サイズ ≤μ の presheaves の小さい skeleton S_μ を取り、

    Φ(μ)=max(μ,aleph_0,|Mor D|, sup{|ELS|:S∈S_μ})

とする。必要なら単調増大に選び直す。これは集合の上限である。よって全ての B と A⊂EB について

    |A|≤μ  =>  |c_B(A)|≤Φ(μ).

特に、一段階の濃度制御には「強商が集合個」という未証明の仮定は入っていない。

### 6.2 一様な反復長があれば Q が従う

μ_0≥max(aleph_0,|EH|,|Mor D|) を固定し、

    μ_(α+1)=Φ(μ_α),
    μ_δ=max(aleph_0,|δ|,sup_(α<δ)μ_α)

とする。帰納的に |A_α|≤μ_α。

もし τ(q)≤θ_H が全強商で成立すれば、A_(θ_H)=EB より |EB|≤μ_(θ_H)。これが既存の (Q)。

逆に (Q) で |EB|≤b_H と分かれば、§4の停止論法により θ_H=max(aleph_0,b_H)^+ を共通上界にできる。

従ってこの新しい ambient-image rank の一様有界性も、元の前提下で LP と同値である。この同値自体を一般肯定の証明として扱わない。今回新しく埋まったのは、rank が各 q について実際に定義できることと、その具体的な計算方法。

### 6.3 pure hull から開始する場合

A_0 を指定した κ-pure hull としても§4は動く。途中の A_α⊂EB は pure とは限らないが、単に B に到達する構成には purity を維持する必要はない。

反対に、全段階で pure hull を取り直してから c_B を適用すれば、各 nonmonic stage で少なくとも κ 個の新元が必要となる。ただしその pure-hull enlargement は canonical regular-epi step と同一ではなく、反射後の transition が regular epi とも限らない。二つの反復を混同しない。

---

## 7. Generatedness が保証するのは最終閉包の連続性

No.3 の local λ-directed-union 保存をここで用いる。

### 命題7.1

任意の局所 B と、λ-directed な ambient subobjects A_i⊂EB に対して

    cl_B(union_i A_i)=union_i cl_B(A_i).

**証明。** cl_B(A_i) は局所部分対象で、monotonicity により λ-directed diagram。元の仮定からその ambient union U は局所となる。U は全 A_i を含むので左辺を含む。逆の包含は閉包の monotonicity より従う。□

ここから c_B 自体が λ-directed unions を保存すると推論してはいけない。c_B は一回の反射像であり、cl_B はその transfinite iteration の停止値である。

### 7.2 抽象的な閉包計算だけでは一様長は出ない

この差を検査するための純粋な順序論的対照例。

任意の順序数 γ に対し P(γ) 上で

    d_γ(S)=S∪{min(γ\S)}  if S≠γ,
           γ             if S=γ

と置く。d_γ は extensive かつ monotone。|d_γ(S)|≤|S|+1 という、γ に依存しない一段階のサイズ上界がある。

しかし、空集合からの continuous transfinite iteration は γ 段まで strict に増大し、d_γ^α(empty)=α (α≤γ)。最終閉包は全ての S を γ に送る定数作用素で、任意の非空 directed union を保存する。

従って、「一段階のサイズ上界」と「最終閉包の directed-union 保存」だけから、全 γ に一様な反復長を導くことはできない。

**これは No.3 の反例ではない。** これら d_γ を、一つの固定された reflection と局所対象間の全射に関する自然性から実現したわけではない。§2.1(d) のような圏論的整合性も別途必要。本例が排除するのは、この二つの抽象的性質だけを用いた停止上界の証明である。

---

## 8. Cat による実際の二段階の検算

c:sSet→Cat と nerve N:Cat→sSet の標準反射を使う。N は fully faithful。

H=[1]、B=BC_n (n≥2)、q:[1]→BC_n は両対象を唯一の対象に送り、非恒等射を巡回群の生成元 g に送る functor とする。以前のノートで直接確認したとおり strong epi。

A_0=Im_sSet(Nq) は、両端を同一視した一つの1-simplexとそのdegeneraciesからなる simplicial set。次元 m では、全て恒等の列と、ちょうど一箇所だけgで他が恒等の列からなる。

その反射は

    c(A_0)=Bℕ,

自由な一つの自己射を持つ一対象圏である。r_0:Bℕ→BC_n は m↦g^m。

r_0 は対象・各Homで全射なので、Nr_0 は全ての simplicial degrees で全射。従って

    c_B(A_0)=N(BC_n)=EB.

A_0→EB を反射した射は Bℕ→BC_n で、g^n=1 などを課す regular epi。初期の [1]→Bℕ と合わせて二段階の regular decomposition を得る。

ここでは一段目で元のkernel pairを全て潰しても、反射により新たに合成できるようになった自己射の間の等式が二段目に現れる。定理2.2が「一回でBに到達する」とは言っていないことの具体的な確認である。

Cat の global regular length 2 は既知で、Kawase–Nasu (2026) の導入にも説明がある。本稿は上の既存の q を新しい c_B 作用素で再計算した。

---

## 9. 非 LP の場合に必要になる失敗形の強化

既存の (Q) 還元により、K が P3 の仮定を満たしつつ非LPなら、一つの H∈H からの強商の E-carrier が無界。

本稿で追加された条件は次の通り。

- その各強商 q は個別には canonical regular decomposition を持ち、集合長で停止する。
- しかし固定 H の τ(q) は集合順序数で一様に抑えられない。抑えられれば§6で(Q)になるため。
- 以前の必要条件から取れる κ-pure A⊂EB と nonmonic r_A に対しては、c_B(A)\A の濃度が少なくとも κ。
- r_A のその段階での全等式は、一回の regular epi LA→L c_B(A) で正確に検出される。従って failure は「その等式の証人が全く見つからない」ことではなく、新しい段階・新しい元が生じ続け、その深さが H ごとに有界か分からないことにある。

これらは反例の構成でも、反例の存在証明でもない。

**未確立：ZFC⇒P3、ASC_infinity⇒P3、WVP⇒P3、N⇒¬P3。**

---

## 10. 依存関係と監査点

- 本稿の主要な直接証明は、No.3 の既知の full reflective presheaf presentation に依存する。No.1/2 の非coreflectivityやNを用いない。
- c_B(A) はPのimage。K内のimage（最小の局所部分対象）はcl_B(A)であり、同一視しない。
- Lが全monoを保存するとは仮定しない。特定の包含 A→c_B(A) は、反射するとむしろregular epiになる。
- Eがcoequalizersを保存するとは仮定しない。保存するのはkernel pairsで、coequalizerを保存するのはL。
- Lk_Aがkernel-pair coequalizerであることを、Pのimage quotientから直接証明した。
- kerpair(Lk_A)=kerpair(r_A)から、残りのfactorのmono性を推論しない。
- pure lemmaではAがκ未満とは仮定しない。新元の集合を構造射で閉じたD_0だけをκ未満とする。
- c_Bのfixed pointがlocalであることを、split reflection unitの一意性から示した。単なるmono unitをlocalと扱わない。
- 反復の極限はambient subpresheaf union。反射後の極限段階のcolimitはLの左随伴性で確保する。
- 個別停止のHartogs argumentが数える集合はEBの全sortの元。強商全体の集合性を先取りしていない。
- 個別停止の上界はBに依存する。Hごとの一様停止と混同しない。
- 一段階のΦ(μ)は小さいpresheavesの集合の反射値の上限。class reflector全体を集合パラメータにしたわけではない。
- generatednessから得る最終閉包の連続性を、一段階c_Bの連続性にすり替えない。
- 順序論的対照例は圏論的反例として提示しない。
- 既存のregular-decomposition理論と今回の具体化の新規性は別問題。新規性の主張はしない。

---

## 11. 参照と確認範囲

ローカル入力：

- generator_separation_reduced_powers_and_new_equalities_2026-11-17.md：固定Hの特殊なr、旧relation局所化、一般reduced-power手法の過剰さ。
- rp_equivalence_split_colimits_and_compactness_gap_2026-11-17.md：purityの分解、非LPなら固定Hから任意に高いpurityでfailureを取れること。
- positive_quotient_bounds_and_regular_towers_2026-11-17.md：強商上界QとLPの同値、当時未確立だった個別停止。

一次資料（2026-11-17に本文と必要ページ画像を確認）：

1. I. Di Liberti and J. Rosický, Enriched Locally Generated Categories, TAC 38 (2022), arXiv:2009.10980v2.
   https://arxiv.org/pdf/2009.10980
   PDF p.3を画像で確認。generatednessとstrong quotient smallnessを含む定義・標準定理。Remark2.27の問題との関係は本文も確認。

2. J. L. MacDonald and A. Stone, The tower and regular decomposition, CTGDC 23(2) (1982), pp.197–213.
   https://www.numdam.org/item/CTGDC_1982__23_2_197_0.pdf
   印刷p.200（PDF p.5）の画像でProposition1.4、Definition1.5、Proposition1.7の仮定を確認。possibly large chainsを持つという仮定を、本稿のsmall cocompletenessから無断で導かない。本稿では固定EB内の増大による別の停止証明を展開した。

3. Y. Kawase and H. Nasu, On the decomposition of a strong epimorphism into regular epimorphisms, arXiv:2604.05744v1 (2026-04-07).
   https://arxiv.org/pdf/2604.05744
   導入、§3のadjunction比較、Theorem3.27とCorollaries3.30–3.31の本文を照合。印刷p.23の画像を確認。LP性から得る一様上界を、P3の一般肯定の途中で仮定していない。

4. L. Sousa, On boundedness and small-orthogonality classes, CTGDC 50(1) (2009), pp.67–79.
   https://www.numdam.org/item/CTGDC_2009__50_1_67_0.pdf
   導入の画像と本文で、mono-preserving reflector、cowellpowerednessを課す議論との違いを確認。本稿の停止を同論文の未確認な定理として引用していない。

文献調査は網羅的な解決状況・新規性調査ではない。本稿の主要な主張には直接証明を付した。
