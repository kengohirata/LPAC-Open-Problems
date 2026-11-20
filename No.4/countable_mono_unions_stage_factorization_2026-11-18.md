# Problem 4：可算 mono union を値域とする equalizer は安全

2026-11-18。状態：PROOF_RECONSTRUCTED。内部点検段階。独立査読・形式検証・新規性確認は未実施。

## 1. 結論

K、P、E、C、D=E(C^op)、および mono を要求するクラス M は既存の No.4 ノートと同じ。

本ノートでは N（非可算 measurable cardinal が存在しない）を仮定し、次を示す。

1. D-objects の任意の可算 mono chain の union U に対し、任意の Y∈K からの射 E(Y)→U は一段階を経由する。各 mono の分裂は不要。
2. 従って Z∈M と二射 Z⇉U の equalizer は M に属する。Z∈D なら、その equalizer 自体が D に属する。
3. U の任意の集合個の積の部分対象を値域としても、Z∈M の equalizer は M に属する。

同じ結論は、可算な cofinal chain を持つ directed union にも適用できる。一般の directed union や、No.4 の反例については結論しない。

なお、**分裂する**可算 mono chain の union が D に埋め込めることは、N を使わず最後の §7 で直接示す。分裂しない一般の可算 chain の D への埋め込みは、本ノートでは主張しない。上の equalizer 結果にその埋め込みは不要。

## 2. 二点列の binary coloring

**補題。** 集合 S の二点の列 (y_n,z_n)_(n<ω) で y_n≠z_n とする。このとき F:S→{0,1} で F(y_n)≠F(z_n) となる n が無限個あるものが存在する。

証明。ある点 s が無限個の pair に現れるなら、F(s)=0、その他を1とすればよい。そうでなければ、各点は有限個の pair にしか現れない。既に選んだ有限個の pair の頂点と交わる pair は有限個なので、再帰的に互いに頂点を共有しない pair を無限個選べる。それぞれの両端を0と1に塗る。□

## 3. 可算の全射逆系と全関数冪

集合の逆系

    S_0 ← S_1 ← S_2 ← …

の bonding maps が全て全射とする。S=lim_n S_n、π_n:S→S_n と置く。S_n が非空なら、可算選択により各 π_n は全射である。ある S_n が空の場合は、全射性と写像の存在により全段階が空である。

M_2-set の mono union

    U=colim_n Ω^(S_n)

を取り、各 stage の射は bonding map に沿う前合成とする。各 π_n に沿う前合成は自然な射

    j:U↪Ω^S

を定め、各 π_n が全射なので j は injective。

**補題（N）。** 任意の集合 A と M_2-map φ:Ω^A→U は、ある n と集合写像 τ_n:S_n→A によって

    φ(f)=i_n(f∘τ_n)

と表される。

### 証明

全 S_n が空なら U=1 であり、主張は直ちに従う。以下、S_n は全て非空。

各 s∈S において評価すると

    Ω^A --φ--> U --j--> Ω^S --ev_s--> Ω

という M_2-map を得る。N の下での Isbell の座標評価表示により、一意な τ(s)∈A による評価である。従って τ:S→A が定まり、全 f:A→Ω について

    jφ(f)=f∘τ。

A が空なら Ω^A=1 の M_2-fixed point を U に送ることはできないので、この場合 φ 自体が存在しない。

τ がどの π_n も経由しないと仮定する。π_n は全射なので、その場合各 n について

    π_n(s_n)=π_n(s'_n),
    τ(s_n)≠τ(s'_n)

となる s_n,s'_n∈S が存在する。§2 の補題を τ(s_n),τ(s'_n) に適用し、無限個の n で値が異なる F:A→{0,1} を取る。

一方 φ(F) は U の元なので、ある stage N_0 に属する。従って Fτ は π_(N_0) を経由する。n≥N_0 なら π_n(s_n)=π_n(s'_n) から π_(N_0)(s_n)=π_(N_0)(s'_n) となり、

    Fτ(s_n)=Fτ(s'_n)

でなければならない。これは無限個の n で異なるように選んだことに反する。

よって τ=τ_nπ_n となる n と τ_n:S_n→A が存在する。j の injectivity より φ(f)=i_n(fτ_n) が全 f について成り立つ。□

**依存関係。** N は全関数冪 Ω^A→Ω の座標評価表示に使った。inverse-limit projections の全射性、pair coloring、stage の一様化は ZFC の議論である。

## 4. D の任意の可算 mono chain への適用

    D_0 ↪ D_1 ↪ D_2 ↪ …,  D_n∈D,
    U=colim_n D_n

を取る。各 D_n を E(Y_n), Y_n∈C と同一視する。N の下で E は fully faithful なので、各 transition はある K-map

    q_n:Y_(n+1)→Y_n

の E 像である。E(q_n) が mono であるため q_n は各 sort で全射である。

任意の θ:E(Y)→U、Y∈K を取る。各 sort i について、§3 を集合逆系 (Y_(n,i)) と M_2-map θ_i に適用する。一つの stage n_i を経由し、その stage map は集合写像 Y_(n_i,i)→Y_i による前合成と分かる。

二つの sort の stage を共通の n に上げる。U の stage inclusion が mono であるため、θ の右 M_1-action との可換性と二本の構造射に関する自然性は stage map に反映される。Ω 値関数の点分離性により、二つの集合写像は K-map k:Y_n→Y をなし、

    θ=i_n E(k)

となる。

**ここでは Y の成分数・carrier・有限支持性にサイズ制限を置いていない。** 有限性は union の cofinal chain が可算である点にある。

## 5. M の equalizer 閉性

**定理（N）。** Z∈M、a,b:Z⇉U とする。すると Eq(a,b)∈M。

証明。j:L↪Z を equalizer とし、fg x:F→L を取る。M の定義により jx=v t となる Y∈C と mono v:E(Y)↪Z を取る。

§4 により av,bv:E(Y)⇉U は共通 stage E(Y_n) を経由する。対応する二射 k_a,k_b:Y_n⇉Y の C 内の coequalizer r:Y→Q を取る。E(r):E(Q)↪E(Y) は二射の equalizer。

stage injection が mono であるため、t は E(Q) を経由する。vE(r):E(Q)↪Z は a,b を equalize し、L への mono を与える。これが x の D-subobject による因子化なので L∈M。□

始域 Z が最初から E(Y)∈D なら、局所化をせず同じ coequalizer を取れるため Eq(a,b)∈D。

## 6. 任意個の積と部分対象への拡張

U_s (s∈I) がそれぞれ D-objects の可算 mono chain の union で、W↪prod_s U_s が mono とする。すると、N の下で Z∈M と任意の a,b:Z⇉W に対し Eq(a,b)∈M。

証明。fg map を局所的な mono E(Y)↪Z に入れた後、各座標 s の二射はある E(Y_(n_s,s)) stage を経由する。全ての n_s を共通にする必要はない。C の中で

    coproduct_s Y_(n_s,s) ⇉ Y → Q

を coequalizer とすれば、E(Q) は全座標を同時に等化する D-subobject となる。□

特に、これらの union の積、およびそれに埋め込める M-object の全 retracts は M に属する。

## 7. Split-mono chain なら D への埋め込みも直接得られる

ここだけは一般の category-theoretic な議論であり、N を使わない。

可算 chain A_0 --i_0↪ A_1 --i_1↪ … に対し、r_n:A_(n+1)→A_n、r_ni_n=id があるとする。union U の各 stage から A_n への射を、stage m≤n では inclusion の合成、m≥n では retraction の合成で定める。これらは chain の transition と可換なので

    π_n:U→A_n

を定める。π_n は A_n stage 上で恒等射。

従って P における射

    (π_n)_n:U→prod_n A_n

は mono。二つの元を共通 stage A_n に取り、π_n で比較すればよい。

A_n∈D の場合、D の積は E(C 内の coproduct) として ZFC で存在する。よって split-mono な可算 D-chain の union は D に埋め込める。

## 8. 次に残る範囲

実際の Isbell 候補に対して、普通の可算 mono chain を値域とする反例探索は除外できる。可算鎖が split でないことだけでは、equalizer failure は生じない。

一般の可算 mono chain の union が D に埋め込めるかどうかは、この証明とは別の問いとして残る。No.4 の equalizer 反例をこの種の union で探すなら、少なくとも可算 cofinal chain のない directed system が必要になる。
