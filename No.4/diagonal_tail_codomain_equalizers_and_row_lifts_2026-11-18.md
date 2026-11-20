# Problem 4：対角 tail quotient を値域とする M-equalizer は安全

2026-11-18。状態：PROOF_RECONSTRUCTED。ZFC の直接証明。内部点検段階で、独立査読・形式検証・新規性確認は未実施。

## 1. 設定と結論

Ω=ω、𝔠=2^ℵ0 とし、λ>𝔠 を正則基数とする。既存の K、P、C、E、D=E(C^op)、および mono を要求するクラス M を使う。

R∈C に対して

    U_R=colim_(β<λ) E([β,λ)・R)

と置く。transition maps は tail restriction による全射であり、一般には mono ではない。各 sort の元は [β,λ)×R_i 上の Ω 値関数の germ で、共通 tail 上の完全な一致で同一視する。

Z_*=(Ω --id,id--> Ω) に対する U=U_(Z_*) を対角 tail object と呼ぶ。これは [既存の row-pattern 議論](mono_candidate_tail_quotients_2026-11-18.md) より ZFC で M に属する。

本ノートの主結果は次のとおり。

1. **任意の Z∈M と a,b:Z⇉U に対し、Eq(a,b)∈M。**
2. 対角 tail objects の任意個の積の部分対象を値域にしても同じ結論。
3. 任意の R∈C について、各 |Y_i|≤𝔠 の Y∈C を始域側に取れば、**Eq(E(Y)⇉U_R)∈D**。R の carrier の上界は不要。

N も No.1 の因子化下界・非 coreflectivity 入力も使わない。

## 2. 高い完全性を持つ reduced power への scalar map

J を集合 T 上の proper ideal とし、J は≤𝔠個の union で閉じるとする。関数の差の集合が J に属するとき同一視する reduced power

    Q_J=Ω^T/J

を考える。

**補題 2.1。** |S|≤𝔠 の集合 S に対し、任意の M_2-map φ:Ω^S→Q_J は、ある集合写像 τ:T→S による前合成を quotient へ送ったものとして表せる。

### 証明

S=∅ の場合は Ω^S=1 が M_2-fixed point を持つ一方、proper な J による Q_J はそれを持たないので、φ は存在しない。

φ に対応する Boolean map

    Φ:P(S)→P(T)/J,  Φ(A)=φ(χ_A)

は可算 joins/meets を保存する。有限演算は tuple coding による。可算 join は disjointification と最初の所属番号を記録する Ω 値関数により保存される。J が可算 union で閉じるため、target の可算 Boolean 演算は representatives 上で計算できる。

S の点を分離する可算族 d_n:S→Ω を取り、φ(d_n) の representatives v_n:T→Ω を選ぶ。各 t の pattern を v(t)=(v_n(t))_(n<ω) とする。

pattern p∈Ω^ω がどの s∈S の (d_n(s))_n とも一致しない場合、A_n={s:d_n(s)=p_n} の交叉は空である。可算 meet 保存により

    {t:v(t)=p}∈J。

このような ghost patterns は高々𝔠個なので、その全 fiber の union も J に属する。それを除いた t について、一意な τ(t)∈S が v(t)=(d_n(τ(t)))_n を満たす。除いた部分では τ を任意の固定 s_0∈S にする。

各 s∈S に対して {s}=intersection_n d_n^(-1){d_n(s)} なので

    Φ({s})=[τ^(-1){s}]_J。

任意の f:S→Ω と φ(f) の representative w:T→Ω を取る。{s}⊆f^(-1){f(s)} と Φ の単調性より

    {t:τ(t)=s, w(t)≠f(s)}∈J。

|S|≤𝔠 なので、これらの union も J に属する。従って [w]_J=[fτ]_J、すなわち φ(f)=[fτ]_J が全 f について成り立つ。□

## 3. 小さい carrier の始域に対する K-map の row lift

|Y_i|≤𝔠 の Y∈K と θ:E(Y)→U_R を取る。各 sort i の reduced power は T=λ×R_i 上の ideal

    J_i={A⊆λ×R_i:ある β<λ について A⊆β×R_i}

によるもの。λ>𝔠 の正則性により J_i は≤𝔠個の union で閉じる。

補題 2.1 により、集合写像

    k_i:λ×R_i→Y_i

を取り、全 f:Y_i→Ω について θ_i(f) を f∘k_i の germ として表せる。

これらは初めから K-map とは限らない。しかし、**一つの tail に制限すれば K-map になる**。

各 Y_i の点を分離する可算族 d_(i,n):Y_i→Ω を取る。任意の m∈M_1 について、θ の equivariance は、各 test d_(i,n) に対する

    d_(i,n)(k_i(t,mr))=d_(i,n)(m k_i(t,r))

がある tail で全 r∈R_i に対して成り立つことを与える。n は可算、m は𝔠個なので、正則性から一つの tail で全て同時に成り立つ。点分離性により、その tail では k_i(t,mr)=m k_i(t,r)。

二本の構造射についても、Y_1 の可算分離族を用いる同じ議論により、共通 tail で自然性を得る。

従って、ある β<λ と K-map

    k:[β,λ)・R→Y

により θ が

    E(Y) --E(k)--> E([β,λ)・R) → U_R

と因子化する。

R_i=∅ の sort は唯一の写像として扱えばよい。R_i≠∅ かつ Y_i=∅ の場合は source の固定点を非自明な reduced power へ送れず、θ は存在しない。

**注意。** R_i が大きいと U_(R,i)→(Ω^λ/eventual)^(R_i) は injective でないことがある。本証明は各 coordinate を別々に扱わず、λ×R_i 全体の bounded-row ideal を使っている。

## 4. Recurrent pairs による equalizer 全体の記述

Y,R∈C とし、二つの K-map k_a,k_b:[β,λ)・R⇉Y が与えられ、それらが U_R への二射 a,b:E(Y)⇉U_R を表すとする。各 sort で k_a,k_b の値が濃度≤𝔠 の部分集合 A_i⊆Y_i に入ると仮定する。

各 (y,z)∈A_i² について

    O_(y,z)={t≥β:ある r∈R_i に対し
                     k_a(t,r)=y, k_b(t,r)=z}

を考える。これが unbounded な pair を recurrent と呼ぶ。

pair は高々𝔠個なので、bounded な O_(y,z) を全て避ける一つの γ<λ を取れる。γ 以降で現れる pair は全て recurrent。

各 f:Y_i→Ω について、germ a_i(f),b_i(f) が等しいことは、f(y)=f(z) が全 recurrent pair について成り立つことと同値である。必要性は、germ が一致する tail より後にも各 recurrent pair が現れるため。十分性は、γ 以降の全ての pair が recurrent であるため。

C の中で coequalizer

    [γ,λ)・R ⇉ Y --q--> Q

を取る。E(q):E(Q)↪E(Y) の各 sort は、γ 以降に現れる全 pair を等化する関数全体である。上の同値により

    Eq(a,b)=E(Q)∈D。

この記述では fg seed ごとに tail を取り直していない。equalizer 全体が一つの C-coequalizer により得られる。

**系 4.1。** |Y_i|≤𝔠 の Y∈C に対し、任意の二射 E(Y)⇉U_R の equalizer は D に属する。R の carrier に制限はない。

## 5. 対角 template では component 数の上界だけでよい

R=Z_* とし、K_λ=Ω^λ/eventual と置く。λ>ω なので

    U_i≅K_λ^Ω

であり、右 M_1-action は Ω 座標への前合成。定数変換が全座標を分離する。

Y∈K について各 I_i=π_0(Y_i) の濃度が≤𝔠 とする。任意の θ:E(Y)→U に対し、旧 V-codomain 証明と同様に scalar map

    φ_i:Ω^(I_i)→K_λ

を取り、各 f:Y_i→Ω と n∈Ω について

    θ_i(f)(n)=φ_i(g_(f,n)),
    g_(f,n)(C)=f(ρ_C(n))

と書ける。

補題 2.1 を適用して τ_i:[β,λ)→I_i を取ると、θ_i は row map

    k_i(t,n)=ρ_(τ_i(t))(n)

による前合成の germ として表せる。k_i は各 row で M_1-equivariant である。

k_i の値は Y_i の roots 全体の中に入り、その集合の濃度は |I_i|·ω≤𝔠。構造射は roots を roots に送る。従って roots を分離する可算族を Y_i 全体へ任意に延長し、§3 と同様に θ の自然性を検査すれば、ある共通 tail で k:[β,λ)・Z_*→Y が K-map になる。

こうして得た row lifts の値は roots に限られるので、§4 の recurrent-pair 議論が適用できる。

**系 5.1。** Y∈C の各 component 数が≤𝔠 なら、任意の E(Y)⇉U の equalizer は D に属する。

## 6. 任意の M-source と積・部分対象

**定理 6.1。** Z∈M、a,b:Z⇉U なら Eq(a,b)∈M。

証明。j:L↪Z を equalizer とし、fg x:F→L を取る。M の定義と [mono を保つ component 圧縮](mono_local_compression_and_v_equalizers_2026-11-18.md) により、jx はある mono v:E(Y)↪Z を経由し、Y∈C、各 |π_0(Y_i)|≤𝔠 とできる。

系 5.1 による av,bv の equalizer E(Q)↪E(Y) は D に属する。元の F→E(Y) はこれを経由する。v が mono なので E(Q)↪L が得られ、x の monic D-factorization となる。□

λ_s>𝔠 が各々正則である対角 tail objects U_s の積に W↪prod_s U_s が埋め込める場合も、Z∈M と二射 Z⇉W の equalizer は M に属する。局所的な component 圧縮を一回行い、各 s について上の coequalizer を取り、それらを C 内の coproduct にまとめて同時に等化すればよい。

また、Z の各 fg map が carrier≤𝔠 の monic D-witness を経由する場合、系 4.1 により任意の R∈C の tail target U_R に対しても Eq(Z⇉U_R)∈M。この主張自体は U_R∈M を仮定しない。

## 7. 結論の範囲

対角 tail quotient は、旧 V^R への写像で検出できない M-object を供給する。しかしそれ自身を equalizer の値域に選ぶ方法は、上の ZFC 定理により反例を生まない。

一般の大きい R に対する U_R と一般の M-source の組合せは、なお未解決である。component 圧縮だけでは R の全 coordinate に対する row-map の値域を濃度𝔠に抑えられないため、§4 の recurrent-pair 議論をそのまま適用できない。
