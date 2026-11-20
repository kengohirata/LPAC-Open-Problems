# ℵ₁-free E-ring：directed mono union と equalizer で unit の hull が Z に縮む明示例

2026-11-18。状態：PROOF_RECONSTRUCTED。全て ZFC。
これは No.4 の反例ではない。single orthogonality class から mono-local class を作ると、equalizer 閉性が失敗する明示例である。

## 1. 入力となる E-ring

R≠Z を、additive group R⁺ が ℵ₁-free な非零 unital E-ring とする。
すなわち、R⁺ の全ての countable subgroups は free abelian であり、

    End_Z(R⁺)→R,   φ↦φ(1)

が bijective である。従って additive endomorphism で 1 を固定するものは id_R のみである。

このような R は任意に大きい濃度に存在する。Dugas–Mader–Vinsonhaler の large E-ring theorem を、Göbel–Herden–Shelah, *Absolute E-rings*, Advances in Mathematics **226** (2011), 235–253 が紹介しており、同論文 p.237 は従来の大きい E-rings の additive groups が ℵ₁-free であることを明記している。
[一次文献 PDF、pp.235–237](https://shelah.logic.at/files/95652/948.pdf)
元の存在論文は Dugas–Mader–Vinsonhaler, *Large E-rings exist*, J. Algebra **108** (1987), 88–101。

以下の構成は、指定された R に対して明示的に定義される。E-ring の存在定理以外に集合論的仮定は置かない。

## 2. Z·1 は R⁺ の pure subgroup

ℵ₁-free group は torsion-free である。さらに 1 は n>1 で割り切れない。
もし n r=1 なら、ring multiplication を用いて n^k r^k=1 が全ての k で成り立ち、R⁺ の中に Z[1/n] と同型な countable subgroup が得られる。これは free abelian でなく、ℵ₁-freeness に反する。

従って Z·1≤R⁺ は pure である。実際、n x=m·1、n>0 とし、d=gcd(n,m) とする。
Bezout を使うと (n/d)y=1 となる y∈R を得るので n/d=1、すなわち n|m。torsion-freeness より x=(m/n)·1。

## 3. 全射的な partial-homomorphism inverse system

J を、1 を含む R⁺ の finite-rank pure subgroups K 全ての poset とする。

各 K は countable：torsion-free finite-rank group は Q^n に埋め込まれる。
ℵ₁-freeness より K は free abelian であり、rank が有限なので finitely generated free である。

任意の有限部分集合 S⊂R に対し、Z·1+⟨S⟩ の pure closure は finite rank なので J に属する。従って J は directed、R=⋃_(K∈J)K。
また Z·1 自身が J の最小元である。

K≤L が J の二対象なら、K は L の pure subgroup である。L/K は finitely generated torsion-free だから free であり、K↪L は split する。

各 K に対し

    T_K={t:K→R⁺ : t is additive and t(1)=1}

と定義する。包含 K↪R により T_K は非空。
K≤L に対する restriction

    ρ_(LK):T_L→T_K

は全射である。実際 L=K⊕C と分解し、t∈T_K を C 上で 0 とすることで延長できる。
1∈K なので、この延長も 1 を固定する。

ここでは Grp の部分準同型の場合に残った **restriction の全射性を、有限生成 free groups の splitting によって実際に証明できた**。

## 4. Powers の directed mono union

ambient category を Z/Ab とする。対象は指定元を持つ abelian group (A,a) である。

各 K∈J に

    D_K=(R^{T_K}, constant 1)

を対応させる。K≤L に対する transition は restriction の precomposition

    D_K→D_L,
    F↦F∘ρ_(LK)

である。ρ_(LK) が全射なので、これは injective group homomorphism であり、pointing を保存する。

この directed mono diagram の colimit を U とする。U は実際に powers of (R,1) の directed union である。

T_(Z·1) は inclusion 一つだけからなるので、最初の stage D_(Z·1) は (R,1) と同一視できる。
その U への inclusion を

    c:(R,1)↪U

と書く。各 stage で c(r) は constant function with value r である。

## 5. 二つ目の mono と equalizer の正確な計算

x∈R を取り、x∈K∈J とする。evaluation function

    ev_x:T_K→R,   t↦t(x)

の U における像を f(x) と定義する。
restrictions との compatibility により、これは K の選択に依存しない。
有限個の元を一つの K に入れれば、f が additive であることが分かる。
全ての t は 1 を固定するので、f:(R,1)→U は pointed map である。

f は mono である。x≠0 なら、包含 t:K↪R は T_K の元で ev_x(t)=x≠0。従って ev_x≠0 であり、stage maps が mono なので f(x)≠0。

**定理。**

    Eq(c,f)=(Z·1,1)≅(Z,1)。

整数 m に対し、全ての t∈T_K は t(m·1)=m·1 を満たすので Z·1 は equalizer に含まれる。

逆に x∉Z·1 とし、x∈K∈J を選ぶ。Z·1 は K の pure subgroup なので、

    K=Z·1⊕C

と分解できる。この projection に inclusion Z·1↪R を合成した t は T_K に属する。
t(x)∈Z·1 だが x∉Z·1 なので t(x)≠x。
従って ev_x と constant x は D_K で異なり、U でも異なる。よって x は equalizer に属さない。□

**f はどの stage も経由しない。**
もし f:(R,1)→D_K→U と分解したら、最初の射の各 coordinate R→R は 1 を固定する additive endomorphism である。
E-ring property により全て id_R なので、最初の射は constant-function inclusion。その U への合成は c となり、Eq(c,f)=Z·1<R に反する。

従ってこれは、power object から powers の ordinary directed mono union への **具体的な non-stage monomorphism** でもある。

## 6. Single orthogonality class の mono-localization は equalizer で閉じない

η:(Z,1)→(R,1) を inclusion とし、Z/Ab 内の single orthogonality class

    L=η^⊥

を考える。これは full replete で全小極限に閉じる。
(Z,1) は ambient の initial object なので、W∈L とは「pointed map (R,1)→W がちょうど一つある」ことと同値である。

E-ring property から (R,1)∈L。積閉性から全ての D_K も L に属する。

L について次の mono-local class を定義する。

    M_L={Z : ambient finitely generated F→Z は、
               ある L-object D の mono D↪Z を経由する}。

R∈M_L であり、U も L-objects の directed mono union なので U∈M_L。
一方 (Z,1)∉M_L である。initial object (Z,1) 自身は finitely generated なので、もし (Z,1)∈M_L なら L-subobject D↪(Z,1) が存在する。
その image は 1 を含む subgroup of Z なので Z 全体。従って (Z,1)∈L でなければならない。

しかし pointed map r:(R,1)→(Z,1) が存在すれば、inclusion Z→R との合成は R の 1 を固定する endomorphism、従って id_R。その image が Z·1 に含まれることから R=Z·1 となり、仮定に反する。

従って

    R,U∈M_L,
    Eq(c,f)≅(Z,1)∉M_L。

この equalizer failure は ZFC であり、no-measurable assumption や E-ring powers の無限積からの射の分類を必要としない。

## 7. No.4 との関係

(R,1) を含む full class が products、directed mono unions、equalizers に閉じるなら、この構成により (Z,1) を含まざるを得ない。
従って巨大な E-ring の unit による relative rigidity は、これらの閉包操作の下では保持されない。

これは [X/Ab の肯定定理](coslices_of_abelian_groups_limit_countable_union_reflection_2026-11-18.md) と整合する。ここで得たものは No.4 の非反射的な class ではなく、E-ring に基づく mono-local class が equalizer 閉性を失う、具体的な失敗機構である。
