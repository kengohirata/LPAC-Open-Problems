# Problem 4：Y_ω を template にしても順序数 witness からの射は stage に入る

2026-11-18。状態：PROOF_RECONSTRUCTED。内部点検段階。独立査読・形式検証・新規性確認は未実施。

## 1. 設定と結論

κ≥ω とし、これまでと同じ

    C_κ=Cont([0,κ],Ω_discrete),  B_κ=Ω^[0,κ],
    Y_κ=(C_κ --p_κ=inclusion,q_κ=d_κ^*--> B_κ)

を取る。今回の template は

    R=Y_ω=(C_ω --p_ω=inclusion,q_ω=d_ω^*--> B_ω)。

C_ω は eventually constant sequences に極限値を添えた M_1-set であり可算。B_ω は濃度𝔠で、有限支持でない元を含む。R∈C は ZFC で成り立つ。H_1(C_ω)≅[0,ω] と H_1(B_ω)≅[0,ω] の下で H_1(p_ω) は恒等写像であり、後者の座標評価表示には添字集合 [0,ω] が可算であることを使う。

旧ノートの T_α に対し

    V^R=colim_(α<ω_1) E(T_α・R),
    Kappa=colim_(α<ω_1) Ω^(T_α)

と置く。各 stage は D、遷移は mono なので V^R∈M。

**定理（ZFC）。** 任意の θ:E(Y_κ)→V^R は一つの stage E(T_α・R) を経由する。その stage map は明示的な K-map T_α・R→Y_κ の E 像である。

従って N の下では、任意の E(Y_κ)⇉V^R の equalizer は D に属する。N は Y_κ∈C のために使う。No.1 の非 coreflectivity 入力は使わない。

## 2. Sort 0 は既存の可算動力学の範囲に入る

d_ω:[0,ω]→[0,ω] は連続なので、s=d_ω^* は C_ω の endomorphism であり

    q_ω=p_ω s。

V^R の sort 0 は Kappa^(C_ω)。二本の構造射を P,Q と書くと Q=S P、ここで S は s に沿う前合成である。

θ の自然性は

    θ_0 E(p_κ)=P θ_1,
    θ_0 E(q_κ)=Q θ_1=S θ_0 E(p_κ)

を与える。従って二つの sort maps を θ_0 と θ_0E(p_κ) にした射は、p が同型の可算 template

    R_0=(C_ω --id,s--> C_ω)

に対応する V^(R_0) への射となる。

[p が同型の template のノート](ordinal_witness_maps_to_piso_templates_2026-11-18.md) の結果より、θ_0 は一つの stage を経由し、特に

    C_∞={f∈C_κ:∀n<ω, f∘d_κ^n は連続}

への制限だけに依存する。C_∞ は可算で、初めの有限個の自然数以外で一定値を取る関数全体である。

以下では C_∞ を C_κ と B_κ の共通の部分集合とみなす。各 r∈C_ω について、θ_0 の r 座標は χ_(C_∞) を定数1へ送る。

## 3. Sort 1 は一つの scalar coordinate で決まる

b_*:[0,ω]→Ω を b_*(ω)=0、b_*(n)=n+1 (n<ω) という全単射とする。B_ω は左 M_1-set として b_* 上の自由対象である。各 r∈B_ω は一意に

    r=m_r b_*,  m_r=r b_*^(-1)∈M_1

と書ける。

V^R の sort 1 は一般には Kappa^(B_ω) 全体と一致しないが、各 r∈B_ω への座標射

    ev_r:(V^R)_1→Kappa

は存在し、これらは jointly injective。二つの元を共通 stage で表し、その stage の各座標の Kappa への単射性を使えばよい。

scalar map

    φ:Ω^(B_κ)→Kappa,
    φ(F)=θ_1(F)(b_*)

を取る。右 M_1-equivariance より、任意の r=m_r b_* について

    θ_1(F)(r)=φ(F·m_r),
    (F·m_r)(a)=F(m_r a),  a∈B_κ。

従って φ が一つの stage に入れば、θ_1 の全座標を同じ stage で復元できる。B_ω が非可算であることは、この復元の妨げにならない。

## 4. Scalar coordinate が見る集合を濃度𝔠へ圧縮する

I={m_r:r∈C_ω}⊆M_1 は可算。r∈C_ω に対する p の自然性から

    φ(F·m_r)=θ_0(F|_(C_κ))(r)

となる。

φ に対応する countably complete Boolean map を

    Φ:P(B_κ)→B(Kappa),  Φ(A)=φ(χ_A)

とする。可算 meet 保存には元の B_κ のサイズの制限は不要である。

F=χ_(C_∞):B_κ→{0,1} を代入すると、§2 より

    Φ(m_r^(-1)(C_∞))=1  (r∈C_ω)。

従って可算交叉

    U=intersection_(m∈I) m^(-1)(C_∞)⊆B_κ

について Φ(U)=1。

**U の濃度は≤𝔠。** I は Ω の点を分離する。実際、k≥1 に対する selector δ_k:Ω→{0,1} は、δ_k b_* が [0,ω] 上で連続であるため I に属し、これらは Ω を jointly separate する。

a∈U、ω≤x,y≤κ とする。各 m∈I に対し ma∈C_∞ なので

    m(a(x))=m(a(y))。

I の分離性から a(x)=a(y)。従って a は [ω,κ] 上で一定であり、[0,ω] 上の値だけで決まる。よって

    |U|≤|Ω^[0,ω]|=𝔠。

Φ(U)=1 と有限 sel 演算の保存により、φ(F) は F|_U だけで決まる。従って φ は M_2-map Ω^U→Kappa を経由する。|U|≤𝔠 なので scalar stage-factorization lemma が適用でき、ある β と τ:T_β→U によって

    φ(F)=i_β[t↦F(τ(t))]

と表せる。

## 5. 全座標と自然性を同じ stage で復元する

§3 の式から、r=m_r b_* に対して

    θ_1(F)(r)=i_β[t↦F(m_r τ(t))]。

従って θ_1 は集合写像

    k_1:T_β×B_ω→B_κ,
    k_1(t,r)=m_r τ(t)

による前合成として同じ β-stage に入る。r の自由生成表示の一意性により k_1 は明確に定義され、M_1-equivariant である。

§2 で得た θ_0 の stage と共通の γ≥β を取る。両 sort の stage maps は明示的な前合成なので、ある集合写像 k_i:T_γ×R_i→Y_(κ,i) によって与えられる。stage injection が mono であり元の θ が自然なので、stage maps も両作用と構造射について自然。Ω 値関数の点分離性から k=(k_0,k_1) は K-map。

これで θ=i_γE(k) を得る。N の下で Y_κ∈C を使えば、二射を共通 stage に取り、その二つの K-map の C 内の coequalizer を E で移すことにより、equalizer が D に属することも従う。

## 6. c^+ の長い鎖にしてもこの証明は残る

添字を α<𝔠^+ に変更し、T_α を「α から濃度𝔠の集合への単射で、補集合の濃度も𝔠であるもの」としても、restriction は非空集合間の全射になる。

対応する Kappa_𝔠 は、可算個の元を共通 stage に集められる。従って可算 Boolean meet 保存と、|U|≤𝔠 に対する countable-separation による scalar stage-factorization lemma が同じ証明で成立する。§2–§5 の議論もそのまま適用できる。

つまり、この template では「鎖を長くして sort 1 の全座標と colimit を可換にする」操作でも非 stage 射は生じない。

## 7. 結果の限界

Y_ω は確かに有限支持でない sort を持つが、その sort は一つの自由 M_1-generator で生成される。さらに可算な C_ω 部分が、Ω の点を分離する可算個の tests を供給する。この二点が、今回の scalar coordinate の濃度圧縮を可能にしている。

この結果は任意の大きい template R に対する主張ではない。一般の M の equalizer 閉性と、No.4 の反例は未解決である。
