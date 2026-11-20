# Problem 4：小さい自己射による閉包の制御と ZFC の特別場合

2026-11-18。

**状態：PROOF_RECONSTRUCTED。特別な母圏での肯定証明を直接記した。一般 P4 は未解決。strict local presentability との関係は既存文献と照合したが、新規性・独立査読・形式検証は未確認。**

## 1. 小さい image を持つ自己射から、小さい A-subobject を作る

P=Set^(D^op)、A⊆P を full replete かつ全小極限閉とする。正則 λ>|Mor D| を固定する。

次の条件を仮定する。

    (SE_λ) ある集合基数 ν があり、B∈A、S⊆UB、|S|<λ なら、
           S を点ごとに固定する endomorphism e:B→B で
           |im_P(e)|≤ν となるものが存在する。

**補題 1.1。** (SE_λ) から small-hull bound (SH) が従う。

証明。C=Eq(e,id_B) と置く。C∈A で S⊆UC。各 x∈C は x=e(x) なので C⊆im_P(e)。従って

    |cl_B(S)|≤|C|≤|im_P(e)|≤ν.

□

ここでは im_P(e) 自体の A-membership を仮定しない。e が idempotent なら C はその image であり、小さい retract を作る方法が特別場合として含まれる。

A が λ-directed unions にも閉じるなら、[small-hull の同値定理](positive_small_reflections_and_strong_quotients_2026-11-18.md) により A は反射的かつ局所可呈示。

さらに、各集合基数 κ に対して「|S|≤κ の seed を固定し、image の大きさが b(κ) 以下」という版があるなら、union 閉性を仮定しなくても全 X↓A の解集合を得られ、A は反射的。

## 2. Strict local presentability との関係

局所 λ-presentable な圏 K が strictly locally λ-presentable であるとは、λ-presentable な Q を始域とする任意の b:Q→B について

    Q --b--> B --f--> B' --b'--> B,
    b' f b = b

を満たす λ-presentable B' があることをいう。b'f が idempotent であることは要求しない。

P がこの性質を持てば、|S|<λ の seed が生成する部分前層 Q↪B に適用して、小さい B' を経由する e=b'f を得る。P の λ-presentables は同型を除いて集合個なので、それらの carrier の大きさには一様な集合上界がある。従って (SE_λ) が成り立つ。

**系 2.1。** Strictly locally λ-presentable な presheaf category の full replete subcategory が全小極限と λ-directed unions に閉じるなら、それは反射的かつ局所可呈示。

ここで strict local presentability は追加の母圏の仮定。一般の locally presentable category がこの性質を持つとは言えない（§5）。

この条件の定義および groupoid の例は Adámek–Milius–Sousa–Wißmann, *On finitary functors and finitely presentable algebras*, §6, Definition 6.5, Examples 6.6 と対応する。本ノートでは既存概念を P4 の hull に適用している。

## 3. 小さい groupoid 上の前層：全小極限閉性だけで反射

D が小さい groupoid とし、

    τ=max(ℵ0,|Mor D|)

と置く。以下では任意の B∈P と任意サイズの seed S を扱う。

### 3.1 Orbit の大きさと種類

全ての射が可逆なので、B は disjoint な orbits に分解する。各 orbit は一つの元から生成され、ある representable y(d) の quotient となる。従って各 orbit の carrier は τ 以下であり、その同型類は 2^τ 個以下。

### 3.2 Seed を含む小さい retract

B の orbits のうち、次を選ぶ。

- S と交わる全ての orbit。
- B に現れる各 orbit 同型類について一つの代表 orbit。

それらの coproduct を C⊆B とする。各選ばれなかった orbit を、選んだ同型 orbit へ同型で写し、C 上では恒等射を取れば、presheaf retraction r:B→C を得る。

S⊆UC であり、

    |C|≤max(|S|,2^τ).

従って B が A に属すなら、C は retraction から生じる idempotent と恒等射の equalizer なので A に属する。

### 3.3 反射の構成と上界

任意の f:X→B∈A は、|C|≤max(|X|,2^τ) の A-object C を経由する。これが X↓A に解集合を与え、全小極限閉性から反射が存在する。

反射の unit の像は RX 全体を A-hull として生成するため、同じ小さい retract の構成から

    |RX|≤max(|X|,2^τ)

も従う。

**定理 3.1。** 小さい groupoid D について、Set^(D^op) の全小極限閉な full replete subcategory は ZFC で反射的。directed-union 閉性は、この反射性の証明には不要。

さらに λ-directed unions に閉じる場合、small-hull bound があるので A は局所可呈示。

Set、many-sorted sets、任意の固定群 G の G-sets はこの場合に含まれる。G の有限性はこの基数上界を使う証明には不要。

## 4. 一つの射の圏 Set^→：fiber ごとの retract

P=Set^→ とし、B は関数 t:E→V とする。seed を S_E⊆E、S_V⊆V と書く。

まず V' に S_V と t(S_E) を入れる。V が非空なら必要に応じて一つの default vertex を加え、E が非空なら非空 fiber を持つ一つの vertex v* も加える。

次に E' に S_E を入れ、各 v∈V' の fiber t^(-1)(v) が非空なら、その fiber から一元 e_v を選んで加える。C=(E'→V') とする。

retraction を次で定める。

- 選んだ V' と E' の上では恒等射。
- 選ばれなかった非空 fiber の vertex は v* に送り、その fiber の全ての元は e_(v*) に送る。
- 選ばれなかった empty fiber の vertex は default vertex に送る。
- 選んだ vertex の fiber の、E' に入っていない元は e_v に送る。

これらは t と可換し、B→C は retraction。E または V が空の場合は該当する選択を省けばよい。

κ=max(ℵ0,|S_E|+|S_V|) とすると |C|≤κ。従って任意の full replete limit-closed A⊆Set^→ に解集合が存在する。

**定理 4.1。** Set^→ の全小極限閉な full replete subcategory は ZFC で反射的。さらに directed unions に閉じる場合は局所可呈示。

有限 seed に対しては C も有限になる。これは有限生成された hull が実際に有限である具体的な場合である。

## 5. この自己射の方法は一般 P4 の必要条件ではない

Graphs の presheaf category 全体を A=P とする。これはもちろん P4 の全仮定を満たし、反射は恒等関手。

無限基数 κ に対し、頂点 κ、辺を全ての異なる ordered pairs とする、loop のない完全有向グラフ K_κ を取る。任意の endomorphism e:K_κ→K_κ の頂点写像は injective。異なる頂点を同じ頂点に送ると、それらの間の辺の像が loop になってしまうためである。

従って e の image の大きさは κ 以上。seed を空にしても、κ に依存しない小さい image の endomorphism は存在しない。

よって (SE_λ) を P4 の仮定から導くことはできない。A=P では小さい subgraph は豊富に存在するが、それが大きいグラフの endomorphism の固定点として得られるとは限らない。

この例は、small-hull bound 自体を否定しない。否定するのは、それを一つの小さい自己射から得る方法の普遍性である。

## 6. 得られた範囲

本ノートでの ZFC の肯定証明は、次の順序で成立する。

    小さい image を持つ自己射（または retract）
      ⇒ equalizer として小さい A-subobject
      ⇒ small-hull bound
      ⇒ union 閉性を使った全 source の反射・局所可呈示性。

全サイズの seed に対して直接上界がある groupoid と Set^→ では、反射性に union 閉性を使う必要もない。

一般の P4 に対しては §5 がこの方法の限界。次に必要なのは、自己射による実現を仮定せずに小さい A-subobject を作る方法、または [普遍近似](positive_universal_approximants_and_stabilization_2026-11-18.md) 自体の上界である。

## 7. 参照

J. Adámek, S. Milius, L. Sousa, T. Wißmann, *On finitary functors and finitely presentable algebras*, preprint, §6, Definition 6.5 and Examples 6.6。

https://www.mat.uc.pt/preprints/ps/p1907.pdf

同文献の groupoid の十分な rank は λ>2^α。本ノートの orbit による直接証明はこの基数条件と整合する。上の反射性への適用を新規な定理だと主張しない。
