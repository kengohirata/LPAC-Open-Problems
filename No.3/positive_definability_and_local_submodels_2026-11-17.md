# Problem 3：肯定側の条件付き定理 — 定義可能性・小さい局所部分対象・pure mono

2026-11-17。

**状態：PROOF_RECONSTRUCTED。既存の structural-reflection 定理を適用した帰結と、以下の直接証明を主担当が展開・再点検した。独立査読・形式検証・文献上の新規性確認は未実施。一般の P3 の ZFC 証明、反例、独立性は得ていない。**

ユーザーの依頼：肯定側を、できるだけ弱い仮定で示すことを実際に試す。

## 0. 今回の結論と、仮定の種類の区別

P3 の元の仮定を維持したうえで、次の条件付き肯定結果を得た。

| 追加する条件 | 集合論的追加公理 | 結論 |
|---|---|---|
| presheaf 表示で局所対象のクラスが集合パラメータ付き Lévy Σ1 | 不要：ZFC | K は locally presentable |
| 同じクラスが Lévy Σ2 | 固定データを上回る一つの supercompact cardinal | K は locally presentable |
| 同じクラスが Lévy Σ_(n+2), n>=1 | 固定データを上回る一つの C(n)-extendible cardinal | K は locally presentable |
| K が集合個の L_(chi,chi) 公理の全モデルと全準同型の圏に同値 | 不要：ZFC | K は locally presentable |
| ある kappa について、局所対象を終域に持つ kappa-pure mono を L が mono に送る | 不要：ZFC | K は locally presentable |

二番目の基数は **supercompact（超コンパクト）** であり、No.1 の strongly compact（強コンパクト）とは異なる。

**一般の P3 への集合論的十分条件そのものを、VP から強コンパクト基数の真クラス等へ弱めたわけではない。** 上の定義可能性・公理化・pure-mono 条件は、元の仮定から導いたものではない。十分条件の最適性も主張しない。

中心となる点は、巨大な商を直接数えず、「小さい始域の像を含む、小さい局所部分対象」を作ること。その部分対象の包含は、strong epi の性質によって同型になる。

---

## 1. 設定と既存の還元

K は locally small、cocomplete、G は集合サイズの strong generator とする。各 G∈G は共通の正則無限基数 lambda に関して generated。

原著の還元を入力として

    L : P = Set^(D^op) <-> K : E,     L ⊣ E

を取る。D は小圏、E は full faithful、mono の lambda-directed colimits を保存する。K の同型閉な像を P 内で K とも書く。

H は G の <lambda 個の余積の代表からなる集合。既存ノート

    positive_quotient_bounds_and_regular_towers_2026-11-17.md

の §§2–4 により、次の (Q) が得られれば P3 のこの instance は肯定される。

(Q) 各 H∈H に基数 b_H があり、全ての K-strong epi q:H→B について

    ||EB|| <= b_H.

ここで ||X|| は presheaf の全 sort の台集合の非交和の濃度。

要点を再掲する。strong quotient は generatedness を保ち、全対象は H からの K-内部の像の lambda-directed union になる。従って lambda-generated objects は H の strong quotients に一致する。(Q) によってそれらが本質的に小さくなり、任意の X の強商も固定した union 図式とこの小さい圏で記述できる。これにより weak co-wellpoweredness が得られる。

最後の「余完備＋generated strong generator＋strong quotient smallness ⇒ LP」は標準定理を使う。Di Liberti–Rosicky (2022), §2 の冒頭、Theorems 2.18, 2.24 を参照。本文は今回あらためて画像と照合した。

以下の補題2.1やモデル論的 small-submodel 議論自体には、generatedness は不要。generatedness は smallness から LP へ進む部分に使う。

---

## 2. 核心：strong quotient は適切な小さい部分対象を許さない

### 補題2.1（ZFC）

J:K→Str(Sigma) を full faithful な関手とする。H∈K を固定する。

ある基数 b_H があり、任意の K-strong epi q:H→B が構造の圏で

    JH --f--> X --m--> JB

と因子化し、次が成り立つとする。

- X は J の本質的像に属する。
- m は underlying sets 上で単射な homomorphism。
- ||X|| <= b_H。

このとき、q の終域 B は同型を除いて集合個しかない。

**証明。** X≅JX_0 と選び直す。fullness により f,m は K の射に戻り、faithfulness により同じ因子化 q=m_0 f_0 が成り立つ。underlying sets 上で単射な m は Str(Sigma) で mono なので、faithfulness から m_0 も K で mono。

可換四角

    H --f_0--> X_0
    | q          | m_0
    v            v
    B ----id---->B

を q の strong 性で埋めると d:B→X_0、m_0 d=id_B を得る。m_0 は mono なので d m_0=id_(X_0)。従って m_0 は同型であり、JB≅X。

固定した set signature におけるサイズ <=b_H の構造の同型類は集合個。J の full faithfulness から B の同型類も集合個である。各 Hom(H,B) も集合なので、quotient arrows の H 上の同型類も集合個。□

重要なのは **X 自身が局所対象であること**。単に JB の小さい elementary substructure を取るだけでは、任意の部分圏 K に関してこの条件は保証されない。

---

## 3. Lévy Σ1 定義可能な局所対象：ZFC で肯定

### 3.1 ここでいう定義可能性

presheaf は、Ob(D) を sorts、D の射を unary operation symbols とする set-sized finitary signature Sigma_D の構造として扱える。関手法則はこの signature の式で課せる。P は Str(Sigma_D) の full subcategory。

仮定は、E(K) の同型閉な対象クラスが、集合論の言語で

    X∈E(K) iff phi(X,p)

と書け、p は一つの集合パラメータ、phi は Lévy Σ1 であること。

これは「構造の中の一階存在式で定義可能」という意味ではない。集合論の Σ1 は、存在量化の後の量化が全て bounded である形式を指す。class parameter や reflector 全体を一つの集合パラメータとして符号化したとは仮定しない。

### 3.2 使用する外部定理

Bagaria–Casacuberta–Mathias–Rosicky (2015), Theorem 5.1(a)：Σ1(p) の full class of structures に対し、十分大きい regular kappa と小さい始域 A∈H(kappa) からの homomorphism A→Y は、同じクラスに属する X∈H(kappa) と elementary embedding X→Y を経由する。

原定理には signature の arity に応じた nu^(<arity)<kappa の条件がある。今回は signature が finitary なので、regular uncountable kappa を取れば必要な算術条件を満たす。p, Sigma_D, および全ての EH（H∈H）が H(kappa) に入るように kappa を一度選べる。これらは集合個のデータだからであり、巨大基数は不要。

### 定理3.3（ZFC、条件付き）

P3 の仮定に加え、上の presheaf image が Σ1(p) であるなら K は locally presentable。

**証明。** 一つの kappa を3.2のように固定する。任意の H∈H と strong epi q:H→B に5.1(a)を適用すると

    EH --f--> X --m--> EB,
    X∈E(K)∩H(kappa),
    m elementary embedding

となる。m は sortwise injective。補題2.1より m は K 内で同型であり、||EB||=||X||<kappa。

同じ kappa が全ての H に使えるため (Q) が成立し、§1から K は LP。□

Σ1 に対する upward absoluteness が、小さい構造が「同じクラス」に残る保証である。この保証を任意の定義可能クラスに無条件で適用してはいけない。

この結果は既存の structural-reflection theorem と既存の P3 還元からの帰結であり、Theorem 5.1 自体を今回証明したという意味ではない。文献上の新規性は未調査。

---

## 4. Lévy Σ2：一つの超コンパクト基数で肯定

### 定理4.1（条件付き）

P3 の仮定に加え、E(K) が Σ2(p) とする。

    p, Sigma_D, {EH:H∈H}

を全て V_kappa に含む supercompact cardinal kappa が一つ存在すれば、K は locally presentable。

**証明。** BCMR Theorem 5.2(a) を、任意の Eq:EH→EB に適用する。

    EH --f--> X --m--> EB,
    X∈E(K)∩V_kappa,
    m elementary embedding

を得る。kappa は strongly inaccessible なので、V_kappa=H(kappa) であり ||X||<kappa。補題2.1により m は同型となる。

従って全 H∈H の strong quotient の大きさを同じ kappa で抑えられる。(Q) と§1を適用する。□

### 4.2 「一つ」で足りる範囲

kappa を要求するのは **固定されたこの K とこの表示のデータより上**である。標的 B に応じて kappa を選び直していない。B は任意に大きくてよい。

一方、全ての Σ2 instances を同時に肯定するなら、それぞれのパラメータを上回る基数が必要であり、supercompact の真クラスが自然な一様十分条件になる。

これは任意の P3 instance が Σ2 だという主張ではない。したがって、一般の P3 について「超コンパクト基数が真クラスあれば十分」と結論したわけでもない。

### 4.3 より高い定義の複雑さ

BCMR Corollary 6.6(a) は、Σ_(n+2)(p) の full class に対して、パラメータ・signature より大きい一つの C(n)-extendible cardinal（n>=1）があれば同じ因子化を与える。

この kappa を全ての EH の上にも選べば、4.1と同一の強商の議論で肯定できる。これは、固定された定義可能 instance に必要な原理を定義の複雑さごとに局所化するものであり、全ての複雑さに一様な弱い巨大基数原理を得たものではない。

### 4.4 No.1 との区別

No.1 の strong/almost strong compactness 論法は、あらかじめ与えられた小さいテスト対象と kernel pair への写像の延長を保証するものだった。

ここでは、小さい X を作った後に X∈E(K) を保証する必要がある。E(K) を固定した集合個のテストで表すことは、現在の P3 の仮定からは得られていない。

今回、5.2の supercompact を strongly compact、almost strongly compact、WVP 等へ置き換える証明は得ていない。原理の名前や強さを取り違えない。

---

## 5. 集合個の無限論理の公理によるモデル表示：別の ZFC 肯定範囲

この節は set-theoretic Σ1/Σ2 の議論とは別に、通常の infinitary model theory で直接証明する。

### 定理5.1（ZFC）

K が、ある set signature Sigma と、集合個の L_(chi,chi)(Sigma) 文からなる理論 T に対して、全ての T-models と全ての Sigma-homomorphisms の圏 Mod(T) に同値であるとする。chi は signature の arities も上回る正則無限基数としてよい。

このとき K は strong epimorphisms に関して co-wellpowered。

従って K が P3 の余完備性・generated strong generator の仮定を満たせば、K は locally presentable。

**ここでは ordinary epi 全体に関する co-wellpoweredness を主張しない。** また、任意の K の公理化を仮定なしに与えたわけではない。

### 5.2 一様な small-submodel 構成

固定したモデル A を取る。T の subformulas とその negations、必要な existential forms を含む集合サイズの fragment Phi を取る。各式の自由変数・一回の量化の長さを <chi にそろえる。必要なら chi を拡大する。

    nu >= max(chi, |Sigma|, |Phi|, ||A||, aleph_0),
    mu=2^nu

と置く。mu^(<chi)=mu である。

任意の homomorphism q:A→B（B⊨T）について、q(A) を含む substructure X⊂B を次のように作る。

1. 初期集合に q(A) を含める。
2. 各段階で、現在の集合からの <chi 個の parameters と、Phi の existential formula のうち B で真であるものに対し、一つの witness tuple を B から加える。
3. Sigma の operations で閉じる。
4. これを長さ chi の増大列として反復し、極限では union を取る。

各段階の parameter assignments は mu^(<chi)=mu 個以下。式は |Phi|<=nu 個で、各 witness tuple の長さは <chi<=mu。operations の閉包も同じサイズ内に取れる。従って最終的な X のサイズは <=mu。

chi の正則性により、最終 X の <chi 個の parameters はある段階に全て現れる。従って、その existential statement の witness は次の段階で加わっている。Tarski–Vaught 型の式に関する帰納法から、Phi の各式について X と B の真偽が一致する。

特に X⊨T。relations は B から制限し、operations は閉包を取っているので X→B は injective homomorphism。空 sort を許す場合にも同じ構成でよい。非空 sort を要求する流儀では、その sort の非空性を Phi に加えればよい。

### 5.3 strong epi に対する適用

q:A→B が K 内の strong epi なら、上の構成により

    A→X↪B

と、同じモデル圏内で因子化する。補題2.1の diagonal argument により X↪B は同型。従って ||B||<=mu。

A は固定されているので、mu は q や B に依存しない。このサイズ以下の Sigma-structures と A からの射は同型を除いて集合個であり、強商の集合性が従う。□

### 5.4 仮定の限界

- 必要なのは **理論 T が集合**であること。class-sized orthogonality axioms をそのまま T と呼んではいけない。
- 同型による表示であり、単なる faithful functor や、制約を忘れるだけの非充満な表示では上の因子化を K に戻せない。
- 「K は accessible だからモデル表示がある」と言って P3 に適用すると循環する。本節はモデル表示を独立の追加仮定とした条件付き結果。
- 既存の small-model/Skolem machinery の直接の帰結として扱い、別の open problem の新規解決とは主張しない。
- 一般の Lévy Σ2 クラスは、集合個の infinitary sentences によるモデルクラスとは限らない。本節から4節の巨大基数仮定を無条件に除いてはいない。

---

## 6. reflector の mono 保存を、局所終域の pure monos に弱める

既存の ZFC 十分条件「L は全ての monos を保存する」より、要求する射を少なくできる。

### 条件 (RP_kappa)

ある正則無限 kappa が存在し、全ての B∈K と全ての kappa-pure inclusion

    i:A↪EB

について、誘導される射

    i^#:LA→B

が K の mono である。

ここで purity は **ambient presheaf category P** のもの。A が局所対象であることは要求しない。また、局所対象を終域に持たない arbitrary monos の保存は要求しない。

### 定理6.1（ZFC、条件付き）

P3 の仮定と (RP_kappa) が成り立つなら K は locally presentable。

**証明。** 必要なら kappa を大きくする。より大きい基数について pure な射は元の kappa-pure でもあるので条件は維持される。|Mor D|<kappa としてよい。

全 H∈H の ||EH|| を上回る nu>=kappa,aleph_0 を取り、mu=2^nu とする。すると mu^(<kappa)=mu。

強商 q:H→B を任意に取る。Eq(EH) を含むサイズ <=mu の kappa-pure subpresheaf A↪EB を作れる。具体的には、サイズ <=mu の元集合から始め、<kappa 個の variables/equations/parameters を持ち EB 内で可解な方程式系の解を一つずつ加え、構造写像で閉じることを kappa 段反復する。系の数は mu^(<kappa)=mu 以下で、kappa の正則性により最終 union は kappa-pure。これは No.1 の pure-subobject construction と同じサイズ計算であり、巨大基数は不要。

Eq は A を経由するので、随伴によって

    H→LA --i^#--> B

と因子化する。(RP_kappa) により i^# は mono。q の strong 性から i^# は同型である。

サイズ <=mu の presheaves の skeleton S_mu は集合。従って {LA:A∈S_mu} も同型を除いて集合であり、それらの E-carrier の濃度に共通の集合基数上界 b がある。

上の因子化より任意の B はこの候補の一つと同型なので、全 H について (Q) が成立する。§1を適用する。□

### 6.2 これは何を弱め、何を未解決のまま残すか

全 mono 保存なら (RP_kappa) は自動的に成立する。さらに、K がある kappa の pure subobjects で閉じるなら A 自身が局所となり、i^# は i と同型なので (RP_kappa) が成り立つ。

しかし、P3 が与える「局所対象同士の directed unions で閉じる」ことから、(RP_kappa) はまだ導けていない。

pure mono を split monos の filtered colimit として表せることだけでは不足する。その表示の source/codomain 間の遷移が mono とは限らず、反射後に元の union 保存仮定を適用できない。

従って本節は、一般肯定の不足を「全 ambient mono-colimit 保存」から、より限定した射のクラスの保存問題へ絞る十分条件であり、その条件を元の仮定から証明したものではない。

### 6.3 全 mono 保存より本当に弱いことの対照例

P=Quiv、K=Set を constant quiver E(S)=(S --id,id--> S) として埋め込み、L=pi_0（連結成分集合）とする。

mono A↪E(S) の場合、A の全ての辺は loop である。従って pi_0(A) はその頂点集合と一致し、pi_0(A)→S は単射となる。つまり、この反射は **局所対象を終域に持つ全ての monos** を保存し、特に (RP_kappa) を満たす。

一方、二頂点・辺なしの X から、同じ二頂点に辺 0→1 を加えた Y への包含は Quiv の mono だが、pi_0(X)→pi_0(Y) は 2→1 であり mono でない。

従って (RP_kappa) への限定は、全 mono 保存を単に言い換えたものではない。ただし、この例自体の K は Set なので、No.3 の一般問題を決定するものではない。

---

## 7. 今回、ZFC の一般証明で埋まらなかった箇所

### 7.1 任意の小さい elementary/pure 部分構造が local とは限らない

EB の小さい部分構造 A を作ること自体は ZFC でできる。しかし A∈E(K) とは限らない。そこで A を LA に反射しても、LA→B が mono であるとは限らない。

この違いを無視すると、もともと残っていた strong quotient smallness を、small-subobject construction の中で仮定してしまう。

### 7.2 反射モナドの ambient union 保存

前ノートでは T=EL が全 ambient kappa-directed mono-colimits を保存すれば accessible になり、K が LP と分かった。

その強い保存条件を今回も元の仮定だけから導けていない。局所対象同士の union 閉性は E に関する条件であり、非局所な入力を含む図式に対する T の保存性とは違う。

### 7.3 定義可能性を自動的に低くできていない

「K は full reflective」「generated strong generator が集合個」という圏論的情報から、E(K) が Σ1、Σ2、または set-sized infinitary axiomatizable であるという定理は今回得ていない。

reflector 自体は class functor であって、その全データを集合パラメータに入れてよいわけではない。反射単位の普遍性の確認には任意の局所対象への射が現れるので、これを bounded な検証条件と無条件に読み替えない。

### 7.4 一様原理への結論は未確立

今回、次は証明していない。

    ZFC => P3
    ASC_infinity => P3
    proper class strongly compact => P3
    WVP => P3
    proper class supercompact => unrestricted P3

上の Σ2 版の結論と、最後の unrestricted statement を区別する。

No.1/No.2 の巨大基数下界・独立性には新たな依存を置いていない。N も今回の肯定定理の仮定ではない。

---

## 8. 次の数学で優先する具体的な橋

最優先は、元の union 閉性から、ある kappa の (RP_kappa) またはそれに必要な小さい始域のケースだけを導けるかである。

別の十分な橋は、現在の presheaf 表示の局所対象について、set-sized infinitary axiomatization または Lévy Σ1 定義を構成すること。Σ2 までに留まっても、一つの十分大きい超コンパクト基数による肯定まで進める。

いずれも本稿では未証明。新たに行う際は、通常の LS で作った小部分構造の local 性、またはその反射から元の局所対象への mono 性を明示的に検査する。

---

## 9. 監査項目

- strong epi を ordinary epi に置き換えていない。mono factor の同型性には strong 性を使う。
- intermediate X が K に属することを外部 structural-reflection theorem、または明示的なモデル構成で保証した。
- K の accessibility を前提として使っていない。母圏 P のみが既知の presheaf/LP 圏。
- Σ1/Σ2 は集合論の Lévy hierarchy。構造内部の量化階層と同一視していない。
- Σ2 版に使うのは supercompact。strongly compact / almost strongly compact への置換は未証明。
- 一つの kappa は小さいデータと H 全体を上回る。大きい B ごとに変えていない。
- 定義可能性・公理化の仮定を、元の P3 の仮定から得たとは主張しない。
- set-sized theory の small-submodel 証明では、式の fragment、parameter tuples の個数、witness tuple の長さ、最後の chi 正則性を明記した。
- pure-subobject 構成ではサイズ mu は kappa より大きくてよい。小さい対象が kappa-pure-injective という No.1 の巨大基数補題を、サイズ mu の A に誤適用していない。
- (RP_kappa) の証明は A の反射 LA が同型を除いて集合個という事実を使う。LA の濃度を A の濃度だけで数値的に評価したわけではないが、集合個の反射値から上界を取ることに循環はない。
- 今回の成果を、すべての open problems の現在の解決状況や、新規な公刊結果だとは扱わない。

## 10. 参照・確認範囲

### ローカル

- `positive_quotient_bounds_and_regular_towers_2026-11-17.md` §§2–4：presheaf reduction、強商の一様上界と LP の同値。
- `reflection_first_stone_dynamics_and_ambient_union_boundary_2026-11-17.md` §6：ambient mono-colimit 保存から accessibility。
- `negative_trials_strong_quotients_and_copower_obstruction_2026-11-17.md`：generatedness と strong quotient の無界性が両立しなかった既存候補。

### 一次文献

1. J. Bagaria, C. Casacuberta, A. R. D. Mathias, J. Rosicky, *Definable orthogonality classes in accessible categories are small*, JEMS 17 (2015), 549–589, DOI 10.4171/JEMS/511.
   - Theorem 5.1(a), pp.561–562：Σ1 の small-subobject factorization。
   - Theorem 5.2(a), p.563：Σ2 と一つの supercompact による factorization。
   - Corollary 6.6(a), p.567：Σ_(n+2) と C(n)-extendible の一般化。
   - 本文と pp.562–563 の PDF screenshot を今回確認。モデル・言語の定義は§1、set-theoretic definability は§2。
   - 著者機関リポジトリ：
     https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content

2. I. Di Liberti, J. Rosicky, *Enriched Locally Generated Categories*, TAC 38 (2022), 661–683; arXiv:2009.10980v2.
   - §2冒頭、Theorems 2.18, 2.24：strong quotient smallness を含む locally-generated characterization。
   - Remark 2.27：原著 Problem 3 との関係。
   - 今回 p.3 と p.9 の画像も確認。Remark2.27 の monad 記法・保存性の文章だけから、本稿の未証明の ambient-union bridge を既知として採用していない。
     https://arxiv.org/pdf/2009.10980

3. J. Bagaria, A. Brooke-Taylor, *On colimits and elementary embeddings*, preprint arXiv:1202.5215 (2012; published JSL 2013).
   - Theorems 10, 18, 19：公理化や定義可能性に依存する colimit 保存の比較。
   - Theorem 17：accessible categories の basic-theory 表示。今回この定理を P3 に直接適用して accessibility を先取りすることはしていない。
   - p.11 の画像と定理本文を確認。
     https://arxiv.org/pdf/1202.5215

これらの文献確認は P3 の現在の文献状況の網羅的な調査ではない。本稿の主な実行内容は、既存の structural-reflection 定理から P3 のサイズ上界への適用を完成し、別の ZFC のモデル論的十分条件と pure-mono 十分条件を展開したこと。
