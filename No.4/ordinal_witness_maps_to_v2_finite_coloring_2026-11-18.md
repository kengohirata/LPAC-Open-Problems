# Problem 4：実際の順序数 witness から V^(2) への射は全て一段階を経由する

2026-11-18。状態：PROOF_RECONSTRUCTED。直接証明の内部点検段階であり、独立査読・形式検証・新規性確認は未実施。No.4 の反例完成を主張しない。

## 1. 結論と設定

Ω=ω、M_1=M_2=End(Ω)、K=(M_1-Set)^(0⇉1)、E(Y)_i=Ω^(Y_i) とする。有限支持条件等による C、D=E(C^op)、mono を要求する局所有限生成クラス M は既存ノートと同じ。

順序数 κ に対し、X_κ=[0,κ] に順序位相を入れ、d_κ(α)=α+1 (α<κ)、d_κ(κ)=κ とする。今回の始域は対角近似ではなく、実際の

    Y_κ=(Cont(X_κ,Ω_discrete) --p=inclusion,q=d_κ^*--> Ω^(X_κ))

である。Z_*=(Ω --id,id--> Ω)、G=E(Z_*) と置く。

旧ノートの T_α、Kappa=colim_(α<ω_1) Ω^(T_α)、および

    R_2=(Ω² --id,id--> Ω²),
    V^(2)=colim_(α<ω_1) E(T_α・R_2)

を使う。V^(2) の両 sort は Kappa^(Ω²)、二本の構造射は id。

本ノートでは次を ZFC で直接証明する。

1. 任意の射 E(Y_κ)→V^(2) は、定数関数の埋め込み r:Z_*→Y_κ に双対な E(r):E(Y_κ)→G を経由する。
2. 従って任意の射 E(Y_κ)→V^(2) は一つの V^(2) stage を経由する。
3. これらの射は Kappa の {0,1}-値元によって完全に分類できる。異なる二射は既に j_0:E(B)→E(Y_κ) 上で異なる。
4. 異なる二射の equalizer は、Y_κ の両 sort で全定数関数を一点に潰した図式の E 像であり、D に属する。

N や No.1 の非 coreflectivity 入力はこれらの証明には不要。N の下では元の Y_κ∈C でもあるため、同じ二射の equalizer も含め、全ての E(Y_κ)⇉V^(2) が D に入る。

## 2. p が injective のときの有限彩色

Y=(Y_0 --p,q--> Y_1)∈K について p が injective とする。A={a∈Y_0:p(a)=q(a)} は M_1-subset。

Y_1 上に、p(a)≠q(a) となる a ごとに p(a) と q(a) を結ぶ無向辺を入れる。各辺を p(a) から q(a) に向けると、p の単射性により各頂点の outdegree は高々1。

このグラフの各 connected component は高々一つの cycle を持つ。実際、二つの cycle を持つ有限連結部分グラフは辺数が頂点数を超える一方、outdegree≤1 の向きづけは辺数≤頂点数を強制する。

従ってグラフは3彩色できる。cycle のない成分では基点からの距離の parity で2彩色する。cycle のある成分では有限 cycle を3彩色し、そこに付く各 tree を親の色と異なる色で順に彩色する。成分ごとの選択には ZFC の選択公理を使える。

よって集合写像 c:Y_1→{0,1,2}⊆Ω で

    c(p(a))=c(q(a)) ⇔ a∈A

を満たすものがある。c は M_1-equivariant である必要はない。E(Y)_1 は全ての Ω 値関数を含むため、この c を元として使える。

## 3. 彩色を使った対角値域への因子化

W=(L --id,id--> L)∈P を考える。L が点ごとの有限演算を持ち、任意の M_2-map Ω^S→L が全ての有限演算を保存すると仮定する。今回の L=Kappa^(Ω²) はこの仮定を満たす。

その理由は、Ω²≅Ω の tuple coding である。二つの射影となる unary maps は Kappa 上でも jointly injective であり、有限個の元は同じ full-power stage で計算できる。従って M_2-map は tuple coding を保存し、tuple coding と unary map の合成で書ける任意の有限演算を保存する。Kappa^(Ω²) についても座標ごとに同じことが成り立つ。

さらに、既存の有限 tuple coding 転送により、任意の対角対象 W∈H_fg もこの仮定を満たす。有限個の元を一つの D-object から受け取ることで有限演算とその恒等式が存在し、tuple coding の一意性により全 M_2-map がこれを保存する。従って以下の因子化補題は、V^(2) に限らず全ての対角 W∈H_fg に適用できる。

θ:E(Y)→W を取る。自然性から

    θ_0(c p)=θ_1(c)=θ_0(c q)。

Ω 上の二変数演算 eq(x,y)=1 (x=y)、eq(x,y)=0 (x≠y) を使うと、§2 の彩色より

    eq(c p,c q)=χ_A,
    θ_0(χ_A)=1_L。

ここで 1_L は定数1の元。f,g:Y_0→Ω が A 上で一致するなら、三変数演算

    sel(b,x,y)=x  (b=1),
    sel(b,x,y)=y  (b≠1)

について sel(χ_A,f,g)=g。従って

    θ_0(g)=sel(1_L,θ_0(f),θ_0(g))=θ_0(f)。

つまり θ_0(f) は f|_A だけで決まる。制限 Ω^(Y_0)↠Ω^A は全射なので、一意な M_2-map φ:Ω^A→L を得る。A は M_1-subset であるため、θ_0 と制限写像の右 M_1-equivariance および制限の全射性から φ も右 M_1-equivariant。

r:ΔA→Y を r_0:A↪Y_0、r_1=p|_A=q|_A で定める。さらに

    θ_1=θ_0 E(p)=φ E(r_1)

なので、二つの sort がともに φ である射 φ^Δ:E(ΔA)→W により

    θ=φ^Δ E(r)

と一意に因子化する。

**注意。** この補題は p の injectivity と W の対角形を使う。p が一般の射の場合や、W の二本の構造射が異なる場合には、この証明を適用していない。

## 4. Y_κ の固定部分は定数関数だけ

Y_κ に対する A は

    A={f∈Cont(X_κ,Ω):f=f∘d_κ}。

この A は定数関数の M_1-set Ω と同型である。実際、f=f∘d_κ なら f(α)=f(α+1) (α<κ)。超限帰納法で f(α)=f(0) を示せる。後続段はこの等式を使い、非零極限段 λ は f の連続性と λ 未満での定数性を使う。可算 cofinality の仮定は不要。

従って §3 により、任意の θ:E(Y_κ)→V^(2) は

    E(Y_κ) --E(r)--> G --φ--> V^(2)

と一意に因子化する。r は両 sort で n↦const_n。

G の両 sort は Ω^Ω で、id_Ω が左 M_2-作用で全体を生成する。二本の構造射は id なので、G は ambient finitely generated。V^(2) は stage monos の directed union だから、φ、従って θ は一つの stage を経由する。

## 5. 射の完全な分類

B(Kappa) を、Kappa の {0,1}-値元全体とする。すなわち B(Kappa)=colim_α 2^(T_α)。

射 φ:G→V^(2) は h=φ(id_Ω)∈Kappa^(Ω²) によって決まる。左・右作用との整合性は

    h(mr,ms)=m·h(r,s)  (m∈End(Ω))

と同値である。

z=h(0,1) とする。0,1 を固定し他の値を0へ送る retraction e に対して ez=z なので z∈B(Kappa)。任意の r,s に対し m(0)=r,m(1)=s となる m を選ぶと

    h(r,s)=m·z。

z が {0,1}-値なので、この右辺は m の0,1以外での値に依存しない。逆に任意の z∈B(Kappa) はこの式で h、従って φ を定める。

よって

    Hom_P(E(Y_κ),V^(2)) ≅ Hom_P(G,V^(2)) ≅ B(Kappa)。

具体的に、z をある stage の b:T_α→{0,1} で表すと、対応する θ_z の両 sort は

    θ_(z,i)(F)(t,r,s)=F(const_r)  if b(t)=0,
    θ_(z,i)(F)(t,r,s)=F(const_s)  if b(t)=1。

これは明示的な K-map T_α・R_2→Y_κ による前合成なので、E の fullness は不要。

また全ての θ_z は V を経由する。旧ノートの唯一の射 η:E(Y_κ)→V は、F を n↦F(const_n) に送る。z∈B(Kappa) に対して

    λ_z:Kappa^Ω→Kappa^(Ω²),
    λ_z(u)(r,s)=「z=0 の部分では u(r)、z=1 の部分では u(s)」

を共通 stage で点ごとに定めると、これは両作用と可換で、θ_z=λ_zη。定義は stage の取り方に依存しない。λ_z は対角座標への制限を左逆として持つ。

## 6. j_0 上での区別と equalizer の明示

B=(Ω⇉1)、X=E(B)、j_0=E(ψ_κ):X→E(Y_κ) とする。j_0 の sort 0 は、id_Ω∈X_0 を0での評価 ev_0 に送る。そして

    θ_z(ev_0)(0,1)=z。

従って θ_z j_0=θ_(z')j_0 なら z=z'、つまり θ_z=θ_(z')。この始域と値域では、j_0 上で一致する異なる二射は存在しない。

次に z≠z' とする。二つを共通 stage の b,b':T_α→2 で表すと、ある t に対して b(t)≠b'(t)。§5 の公式から、任意の sort i と F∈E(Y_κ)_i について

    θ_(z,i)(F)=θ_(z',i)(F)
    ⇔ F(const_r)=F(const_s) for all r,s∈Ω。

必要性は b(t)≠b'(t) となる t で全 (r,s) を検査すればよく、十分性は公式から直ちに従う。

barY_κ を、Y_κ の各 sort で全 const_n を一つの元に同一視した quotient diagram とする。p,q は定数関数を保存するので、この商は K に存在する。すると

    Eq(θ_z,θ_(z'))=E(barY_κ)  (z≠z')。

barY_κ∈C は ZFC で直接分かる。第0 sort は有限支持 M_1-set の quotient なので有限支持。両 sort には、全定数関数を同一視した M_1-fixed point がある。Ω には M_1-fixed point がないため、H_1(barY_(κ,0)) と H_1(barY_(κ,1)) はともに空。従って H_1(p_barY) は空集合間の全単射。

したがって、異なる二射の equalizer は D に属する。N の下で Y_κ∈C を使えば、同じ二射の場合の equalizer E(Y_κ) も D に属する。

## 7. 全ての対角 M-target に対する帰結

**系（因子化は ZFC、equalizer の結論は N）。** 任意の対角 W∈H_fg に対し、全ての E(Y_κ)→W は E(Y_κ)→G を経由する。さらに N の下で W∈M なら、任意の二射 E(Y_κ)⇉W の equalizer は D に属する。

最初の主張は §3–§4。二つの射を a=φ_aE(r), b=φ_bE(r) と書く。G⊔G は fg なので、W∈M より φ_a,φ_b は一つの D-subobject v:E(Z)↪W を同時に経由する。

    φ_a=v g_a,  φ_b=v g_b。

N の下では Y_κ∈C であり、fullness によって g_aE(r),g_bE(r):E(Y_κ)⇉E(Z) は K の二射 Z⇉Y_κ の E 像となる。その C 内の coequalizer の E 像が二射の equalizer。v が mono なので、この equalizer は元の a,b の equalizer と同じであり D に属する。□

## 8. 次の探索に残る範囲

実際の Y_κ と V^(2) の組合せは、具体的な equalizer failure の探索対象から除外できる。rank-2-supported elements の数が大きいことだけでは失敗を生まない。今回それを消したのは、p の injectivity と値域の二本の構造射がともに id であることを結ぶ有限彩色である。

実際の Y_κ を始域に保つなら、次の値域では対角形を外す必要がある。本ノートは、その非対角の場合の反例または一般閉性を証明していない。

参照：

- [V と V^(2) の構成・tuple coding](v_codomain_equalizers_root_compression_2026-11-17.md)
- [有限 tuple coding の一般転送](general_equalizers_finite_orthogonality_and_quotient_reduction_2026-11-17.md)
- [mono 圧縮と既存の安全な場合](mono_local_compression_and_v_equalizers_2026-11-18.md)
