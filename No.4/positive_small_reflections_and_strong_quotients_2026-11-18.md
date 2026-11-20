# Problem 4：小さい source の反射と strong quotient のサイズ

2026-11-18。前段：[定義可能性と hull の基数上界](positive_definability_hulls_and_cardinal_bounds_2026-11-17.md)。

**状態：PROOF_RECONSTRUCTED。以下は直接証明を整理した研究ノートであり、独立査読・形式検証・新規性確認は未実施。一般の P4 の証明ではない。**

## 1. 設定と今回の到達点

小圏 D に対して P=Set^(D^op) とし、A⊆P は full replete、全小極限および λ-directed unions に閉じるとする。λ は正則無限基数で |Mor D|<λ としてよい。union rank は大きくしても閉性を失わない。

一般の局所可呈示母圏からこの設定への移送は前段ノート §1 のものを使う。対象の大きさ |B| は全 sort の台集合の非交和の濃度。

今回証明するのは次の三点。

1. 小さい seed が生成する A-hull は、A の内部で λ-generated である。しかし固定 seed から生成される対象の圏では、ambient mono は全て同型になる。従ってその圏だけを調べても union 閉性からサイズ上界は出ない。
2. 小さい source Q の反射 RQ が存在し、それら RQ の A-strong quotients が各々集合個なら、A 全体が反射的かつ局所可呈示になる。
3. 前段の small-hull 条件 (SH) は、この設定では **A 自身の局所可呈示性と同値**。反射性との同値ではない。

追加の応用として、Σ2 定義可能性と「A の射の ambient image が A に属する」、または A の regularity を仮定すれば、固定データより上の一つの strong cardinal で全 source の反射を得る。これらの追加条件は P4 の仮定から導いていない。

## 2. Hull と相対的な生成性

B∈A と sorted subset S⊆UB に対して

    cl_B(S) = ⋂ { C ↪ B : C∈A, S⊆UC }

と置く。P の well-poweredness により交わりは集合個で、全小極限閉性により cl_B(S)∈A。

### 2.1 Monos の一致

A の射 m が A-mono であることと P-mono であることは同値。実際、mono は diagonal A→A×_B A が同型であることで特徴づけられ、full inclusion は pullback を保存し、同型を反映する。

以後、A 内の strong epi は、A の全 mono に対する左直交性の意味で使う。ambient epi/strong epi とは区別する。

### 2.2 Seed による一意性と mono に対する持上げ

h:X→H∈A が H=cl_H(im h) を満たすとする。X 自身は A に属さなくてよい。

- u,v:H⇉B∈A が uh=vh を満たせば、Eq(u,v)↪H は seed を含む A-subobject。従って Eq(u,v)=H、u=v。
- m:C↪B が A-mono、u:X→C、v:H→B、mu=vh なら、pullback H×_B C↪H は seed を含む。従って同型であり、一意な d:H→C が dh=u、md=v を満たす。

特に、h は A を値域にする射に関して epic であり、A の monos に対する相対的な strong-epi 性を持つ。

A の任意の f:B→C は

    B → cl_C(im f) ↪ C

と因子化する。最初の射は上の pullback 議論により A-strong epi。従って A には (strong epi, mono) 因子化がある。この時点で A の余完備性や反射性は使っていない。

### 2.3 Hull の自然性

g:B→B' が A の射なら

    g(cl_B(S)) ⊆ cl_B'(gS).

右辺を g に沿って引き戻した A-subobject が S を含むことから従う。ここで左辺は ambient image であり、左辺自体が A-object であるとは主張しない。

### 2.4 Union continuity

λ-directed-union 閉性から

    cl_B(S) = ⋃ {cl_B(T) : T⊆S, |T|<λ}.             (H)

右辺は λ-directed union で A に属し、S を含む。逆包含は最小性による。

### 2.5 小さい hull と内部 λ-generated objects

|S|<λ なら H=cl_B(S) は A の内部で λ-generated である。

証明。H→⋃_i A_i が A の λ-directed mono-colimit への射とする。包含がこの colimit を P で計算するので、S の像は一つの A_i に入る。引戻し H×_(⋃A_i) A_i↪H は S を含む A-subobject だから H 全体。従って H→⋃A_i は A_i を経由する。一意性も mono 性から従う。

逆に B∈A は (H) によりその <λ-seed hulls の λ-directed union。B が内部 λ-generated なら id_B が一つの hull inclusion を経由し、その inclusion は同型。従って

    内部 λ-generated A-objects
      = <λ 個の元から A-hull として生成される A-objects

が同型を除いて成り立つ。

これは対象ごとの生成性であり、これら全ての同型類が集合個だとはまだ言えない。

## 3. 固定 source の生成対象の圏

X∈P を固定する。G_X を X↓A の full subcategory

    Ob G_X = {h:X→H : H=cl_H(im h)}

とする。

§2.2 により、G_X は thin：二対象の間の射は高々一つ。さらに、その全ての射は **A 内で strong epi** である。実際、u:H→H' が X 上の射なら im(u) を含む A-subobject は im(h') を含み、H' 全体でなければならない。

従って G_X の射で **P-mono / A-mono であるものは全て同型**。thin category 自身では全ての射が mono なので、ここは必ず ambient mono と区別する。

G_X は全ての小さい meet を持つ。h_i:X→H_i の meet は

    X → cl_(∏H_i)(im ⟨h_i⟩).

また、包含 G_X→X↓A は右随伴を持ち、f:X→B をその hull に送る。生成対象から B への射は、§2.2 の pullback 議論でこの hull を一意に経由するからである。G_X は完備だが、その inclusion が一般に極限を保存するとは主張しない。

X の反射の存在は、G_X に初対象があることと同値。しかし G_X 全体が essentially small であることとは同値にしていない。

この構造は union 閉性の使いどころを限定する。固定 X の生成対象の間の ambient-mono diagram は同型だけからなり、その union から新しい大きさの制約は出ない。異なる seed を比較すること、または strong quotient のサイズを抑えることが別途必要である。

## 4. 小さい source の反射から全体へ

Q を |Q|<λ の ambient presheaf とする。同型を除けばこのような Q は集合個。

次の二条件を仮定する。

    (LR) 全ての |Q|<λ の Q が A-reflection η_Q:Q→RQ を持つ。
    (SQ) 各々の RQ の A-strong quotients は、商としての同型を除き集合個。

**定理 4.1。** (LR)+(SQ) から (SH)、従って A の反射性と局所可呈示性が従う。

### 証明

まず η_Q の seed は RQ 全体を生成する。H=cl_RQ(im η_Q) とすると、η_Q の普遍性により RQ→H があり、H↪RQ との合成は id_RQ。従って H↪RQ は同型。

B∈A、|S|<λ を取り、Q⊆B を S が生成する部分前層とする。|Mor D|<λ と正則性から |Q|<λ。H=cl_B(S)=cl_B(UQ) と置く。

Q→H は反射を通じて e:RQ→H に延長される。e の像を含む A-subobject は seed S を含むので H 全体。§2.2 により e は A-strong epi。

従って、全ての小さい hull は、集合個の RQ の strong quotient のいずれかである。(SQ) により、その全体の同型類も集合個。台集合濃度の上限 ν を取れば

    ∀B∈A ∀S⊆UB (|S|<λ ⇒ |cl_B(S)|≤ν).             (SH)

を得る。

任意の X→B の hull の大きさは (H) により

    max(ν, (max(λ,|X|))^{<λ})

以下。これが X↓A の解集合を与え、完備性から反射が得られる。

固定 C∈A の strong quotient e:C→B では、B=cl_B(im e)。同じ上界により全ての strong quotients が集合個。従って A は strong epis に関して co-wellpowered。

反射により A は余完備。representables の反射 R(yd) は小さい strong generator であり、包含が λ-directed unions を保存するため内部 λ-generated。余完備性・λ-generated strong generator・strong quotient smallness を仮定する標準の locally-generated theorem により A は局所可呈示。□

最後の標準入力では co-wellpoweredness を省いていない。No.3 の disputed density reduction は使わない。

### 4.2 反射が既にある場合の解釈

X が反射 η_X:X→RX を持つ場合、G_X は RX の A-strong quotients の圏と同値になる。

生成対象 h:X→H には一意な e:RX→H が対応し、上の議論で strong epi。逆に strong epi e:RX→H に対し cl_H(im(eη_X))↪H を引き戻すと、η_X の生成性から e はこの subobject を経由し、strong 性から subobject は全体。従って eη_X は生成対象。

このため「小さい source の反射がある」から「その source の全 hull が一様に小さい」へ進むには、strong quotient のサイズという追加の問題が正確に残る。

### 4.3 反射を仮定する source は自由前層だけでもよい

定理 4.1 の仮定は、実際には次の集合の source に制限できる。

    F = ∐_{j∈J} y(d_j),    |J|<λ.

これら F の反射 RF が存在し、各 RF の strong quotients が集合個なら十分。任意の |S|<λ の seed は、各元に対応する representable を足した F からの射 F→B の像に含まれる。F→cl_B(S) を RF から延長すれば、同じ生成性の議論で strong epi を得る。

従って、関係を持つ全ての小さい Q の反射を先に用意する必要はない。ただし、reflect(yd) が個々に存在するだけでは、これら <λ-coproducts の反射の存在まではまだ言えない。

## 5. Small-hull bound は局所可呈示性と同値

**定理 5.1。** §1 の仮定の下では、次は同値。

    (i) (SH) が成り立つ。
    (ii) A は局所可呈示。
    (iii) (LR) と (SQ) が成り立つ。

(i)⇒(ii) と (iii)⇒(i) は §4 の証明。ここで (i)⇒(ii) は (LR) を先に仮定せず、解集合から全反射を作る。

(ii)⇒(i) を直接示す。A の小さい strong generator G を取る。各 <λ-indexed family (G_j) の A 内の coproduct C=∐_j G_j を作る。そのような C は集合個で、A は co-wellpowered なので、それらの strong quotients の代表も集合 H をなす。

B∈A に対し、これら C→B の A-image、すなわち (strong epi, mono) 因子化の mono 部分を全て集める。これは Sub_A(B) の集合であり、λ-directed である。<λ 個の image を、対応する <λ 個の coproduct の全 summand を合わせた一つの coproduct の image が上から抑えるためである。

その union U↪B は A に属す。全ての G∈G から B への射が U を経由するので、strong generator 性から U↪B は同型。

従って |S|<λ の任意の S⊆UB は、上記の一つの image H↪B に含まれる。この H は集合 H の代表の一つと同型。よって

    |cl_B(S)| ≤ |H| ≤ sup {|H_0| : H_0∈H}

という一様な上界を得る。ここでは包含 A→P が一般の filtered colimits を保存するとは先取りしていない。

(ii)⇒(iii) は、いま得た (SH) からの反射性と、局所可呈示圏の co-wellpoweredness による。□

**結論の強さ。** 一般の P4 を解くために (SH) を証明しようとすると、反射性に加えて局所可呈示性まで証明しようとしている。反射的で union-closed な full subcategory の strong quotient smallness を無条件に仮定してはならない。

## 6. 商の smallness を保証する二つの追加条件

次の追加仮定を考える。

    (IC) 全ての A の射 f:B→C に対し、P で計算した image im_P(f) が A に属する。

**補題 6.1。** (IC) の下で、A の全 strong epis は P の regular epis。従って A は strong-quotient co-wellpowered。

証明。e:B→C の P-image 分解は B→I↪C で、I∈A。e の A-strong 性から I↪C が同型。従って e は componentwise surjective。固定 B のそのような quotients は P において集合個であり、fullness により A の quotient 同型でも同じ。□

従って (IC) の下では、(LR) だけで定理 4.1 が適用できる。

### 6.2 Regularity による別の十分条件

次の条件も (SQ) を保証する。

    (ER) A の全 strong epi は、その A-kernel pair の coequalizer である。

固定 C の kernel pairs は C×C の A-subobjects なので集合個。同じ kernel pair の coequalizers は商として同型。従って (ER) から strong quotient smallness が従う。

特に **A が regular category なら (ER) が成立する**。regular epi–mono 分解において、strong epi の mono 部分は同型になるためである。ここでは A の regular epis が P の regular epis でもあるとは要求しない。

この条件は (IC) と区別する。例えば sheaf category の full inclusion into presheaves について、内部での有効商と pointwise quotient は一般に異なる。

なお (IC) の下では、ambient image 分解が A 内の regular epi–mono 分解を与え、regular epis の pullback 安定性も P から移る。従って十分条件の関係は

    (IC) ⇒ A regular ⇒ (ER) ⇒ strong quotient smallness

であり、独立な仮定の列だとはしていない。

### 6.3 Σ2 と一つの strong cardinal

A の対象クラスが、固定した presheaf 表示で Σ2(p) とする。D,p,λ のコードが V_κ に入る strong cardinal κ があるとする。

Bagaria–Wilson, Proposition 3.3 は Σ2(V_κ)-Product Reflection を与える。各 |Q|<λ の Q は同型コピーを V_κ に取り直せる。Q↓A を Q の元の名前を加えた構造のクラスとして符号化すると、これは固定パラメータが V_κ に属する Σ2 クラス。

前段ノート §2 の積・等化子の議論により、Q↓A に初対象が得られる。クラスが集合の場合はその全対象を取ればよく、proper class の場合に PRP を使う。従って **同じ一つの κ から (LR) が得られる**。

**系 6.3。** Σ2(p)、全小極限閉性、λ-directed-union 閉性、および (IC) または (ER) の下で、固定データより上の一つの strong cardinal は A の反射性と局所可呈示性を導く。特に A が regular であれば適用できる。

同じ結論はこれらの代わりに (SQ) を直接仮定しても成り立つ。

この結果は前段の「Σ2＋一つの supercompact」の結果に **追加の圏論的条件を付けた**場合のもの。一般 P4 の巨大基数上界を下げたとは主張しない。strong は strongly compact とは異なる。

### 6.4 (IC) がある場合の明示的な基数上界

Proposition 3.3 の証明は、comma category の V_κ 内の符号全体を PRP の witness にできることを示している。強基数 κ は inaccessible なので、この集合の大きさは κ 以下、各 factor の carrier は κ 未満。その積と、その後の等化子として作る小さい source の反射は

    |RQ|≤κ^κ=2^κ

と抑えられる。多ソート積への制限でもこの上界は増えない。空の母圏 signature の自明な場合は別途直ちに成立する。

(IC) があれば RQ からの strong quotient は componentwise surjective なので、小さい hull 全体に ν=2^κ という (SH) の上界が使える。従って任意の X の反射 RX について

    |RX|≤max(2^κ, (max(λ,|X|))^{<λ})

を得る。反射の unit の像が RX を生成することを使った。

(ER) だけの場合は kernel pairs の個数から集合サイズの上界は得られるが、coequalizer の ambient carrier が増えないとは言えない。上の 2^κ の明示的評価を (ER) だけに適用しない。

### 6.5 Σ1 の場合は ZFC で局所可呈示性まで進む

A が Σ1(p) であれば、λ-directed-union 閉性と全小極限閉性から **ZFC で局所可呈示性**が従う。前段で記した反射性より強い結論である。

直接には、B∈A と |S|<λ を固定し、A-membership の Σ1 witness と B,p,D を含む十分大きい V_θ を取る。Downward Löwenheim–Skolem により

    M ≺ V_θ,
    B とその witness ∈M,
    TC({p,D})∪S⊆M,
    |M|≤ν=max(ℵ0,λ,|TC({p,D})|)

となる M を取れる。V_θ は使用する Δ0 の検証と構造の符号化に十分な高さに選ぶ。

M の transitive collapse による B のコピーを B_0 とする。p,D は固定され、Σ1 の upward absoluteness から B_0∈A。inverse collapse の B_0 上の制限は B への presheaf embedding で、その像は S を含み、大きさ ν 以下。従って |cl_B(S)|≤ν。

これが (SH) を与え、定理 5.1 で A は局所可呈示。これは BCMR Theorem 5.1(a) の小さい subobject を使う議論の直接版であり、新しい外部定理としては扱わない。

## 7. 残る問題

一般の P4 の仮定から、次のいずれも導いていない。

- 小さい source 全ての反射 (LR)。
- それらの反射の strong quotient smallness (SQ)。
- Ambient image 閉性 (IC)。
- 全ての strong epis の有効性 (ER)、または A の regularity。
- Small-hull bound (SH)、従って局所可呈示性。

反射性だけを狙う、(SH) より弱い正確な目標は、別ノートの [普遍近似の停止条件](positive_universal_approximants_and_stabilization_2026-11-18.md) で扱う。

## 8. 外部入力

1. Bagaria–Wilson, *The Weak Vopěnka Principle for Definable Classes of Structures*, JSL 88 (2023), 145–168, Proposition 3.3, p.151。
   https://diposit.ub.edu/server/api/core/bitstreams/5ac83f7a-9752-4a28-bf65-31c2d878692a/content
   今回は「κ strong ⇒ Σ2(V_κ)-PRP」の固定パラメータ版を使用。一般の全 source を一つの κ で直接反射したとはしていない。
2. Positselski–Rosický, *Nearly Locally Presentable Categories*, TAC 33(10) (2018), 253–264, Introduction p.253。
   https://www.tac.mta.ca/tac/volumes/33/10/33-10.pdf
   使用したのは strong quotient smallness を含む locally-generated characterization のみ。
3. Bagaria–Casacuberta–Mathias–Rosický, *Definable orthogonality classes in accessible categories are small*, JEMS 17 (2015), 549–589, Theorem 5.1(a)。
   https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content
   §6.5 の Σ1 small-subobject argument に対応する。

以上の外部入力から本ノートの結論への適用は、ここに記した直接証明の自己点検段階である。
