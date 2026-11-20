# Z-null 内部部分対象の可算順序数への延長

2026年11月16日。母圏は Ab、Hom は通常の群準同型、Ext は Ext¹_Z。N は可測基数の非存在を表す。[前段階](z_null_internal_subobjects_2026-11-15.md)と同じ T={X:Hom(X,Z)=0}、F={K:Hom(T,K)=0 for all T∈T}、固定した可算 torsion-free 群 B=G_b を用いる。

**結果。** N の下で、すべての 0<α<ω₁ に対し、通常の群としては全射でもある T-内部単射 E_α→B を構成でき、|E_α|=beth_{α+1} となる。その核の整数 radical 長は可算であり、族全体の長さには可算順序数の一様上界がない。これはまだ集合個の族なので、非 well-poweredness は未証明である。

V=L の下では任意の非零 torsion-free T-対象から後続段を作れることも、既知の Ext 定理から導ける。非可算共終度の極限で T 所属を保つことが未解決の中心となった。

状態は `PROOF_RECONSTRUCTED`。Ext 供給と逆極限を別担当で調べ、前段階の証明にも再点検を行った。これは内部の証明点検であり、外部査読・形式検証・新規性の確認ではない。有限探索を無限命題の根拠には使っていない。

## 1. 連続な全射逆系の射影

逆系 (E_α,p_{βα}) を、後続射が全射で、各非零極限 δ では E_δ=lim_{α<δ}E_α となるように作る。この意味で連続と呼ぶ。

**補題（ZFC）。** 任意の集合順序数 λ まで作った連続な全射逆系で、極限の各射影 E_λ→E_α は全射である。

**証明。** E_α の元を固定する。後続段で前像を選び、極限段で既に選んだ整合族をその段の元とする超限再帰を行う。集合長の再帰と選択公理で十分である。∎

一般の非可算な全射逆系ではこの結論は偽である。ここでは途中の全極限段の連続性を使った。前段階で保留した全射性は、この構成の範囲では解消した。

## 2. 可算共終度の極限から Ext の類を供給する

**補題（ZFC）。** λ は cf(λ)=ω の極限順序数、E_λ は前節の連続な全射逆系の極限とする。厳密に増大する共終列 β_n<λ を選ぶ。各

$$L_n=\ker(E_{\beta_n+1}\to E_{\beta_n})$$

が階数 ρ_n の自由部分群 F_n を含み、無限基数 ρ_n が非減少で κ=sup_nρ_n とする。このとき

$$\bigoplus_\kappa\mathbb Z^\omega\hookrightarrow E_\lambda,
\qquad r_0\operatorname{Ext}(E_\lambda,\mathbb Z)\ge 2^\kappa.\tag{1}$$

### 2.1 自由群の積を極限へ埋め込む

射影 E_λ→E_{β_n+1} は全射である。F_n の基底の各元を持ち上げ、準同型 s_n:F_n→E_λ を得る。その β_n 以下の座標は零で、β_n+1 座標は元の F_n の包含である。

各 α<λ に対して β_n<α となる n は有限個なので、

$$p_\alpha s((x_n))=\sum_n p_\alpha s_n(x_n)$$

は有限和として定義できる。座標間の整合性から s:∏_nF_n→E_λ は準同型になる。非零の族の最初の非零成分を x_n とすると、β_n+1 座標では後の項はすべて零となり、前の項も零なので、像は x_n≠0。従って s は単射である。

これは集合としての section を群準同型と誤認した議論ではない。自由基底の持上げから得た s_n が準同型であり、各座標での和が有限であることを使った。

### 2.2 Baer–Specker 群の直和を埋め込む

互いに素な I_k を |I_k|=ρ_k となるように取り、I=⊔_kI_k とする。|I|=κ。各 n で、⊔_{k≤n}I_k を F_n の基底へ単射に割り当てる。

i∈I_k に対応する Z^ω の第 j 成分を、F_{k+j} の i に割り当てた基底元の係数として配置する。この操作で

$$D=\bigoplus_{i\in I}\mathbb Z^\omega\hookrightarrow\prod_nF_n$$

を得る。D の元は有限個の i だけに台を持つので、各 F_n における和は有限である。割当てが各段で単射だから、全成分が零となるのは元の全整数列が零の場合だけである。

### 2.3 Ext の下界

Ab では Ext²=0 なので、D≤E_λ による制限は全射である：

$$\operatorname{Ext}(E_\lambda,\mathbb Z)
\twoheadrightarrow\operatorname{Ext}(D,\mathbb Z)
\cong\prod_\kappa\operatorname{Ext}(\mathbb Z^\omega,\mathbb Z).$$

Ext(Z^ω,Z) に無限位数の元があるという文献入力は[前段階 §4.2](z_null_internal_subobjects_2026-11-15.md)と同じ。各成分でその元を選ぶと、右辺は Z^κ を含む。Z^κ の torsion-free rank は 2^κ であり、Q⊗− の完全性から (1) を得る。∎

この補題には N も V=L も不要である。

## 3. すべての可算順序数での構成

**定理（ZFC+N）。** E₀=B として、すべての α<ω₁ にわたる連続な逆系を、

$$0\to\mathbb Z^{\beth_{\alpha+1}}\to E_{\alpha+1}\to E_\alpha\to0\tag{2}$$

となるように構成できる。各 E_α は torsion-free で T に属し、E_α→B は T-内部単射かつ通常の全射であり、

$$|E_\alpha|=\beth_{\alpha+1}\qquad(0<\alpha<\omega_1).\tag{3}$$

**証明。** α=0 の拡大は前段階の p進群の構成である。Ext(B,Z) の beth₁ 個の独立な類から、核 Z^{beth₁} の E₁ を得る。

E_α∈T と Ext(E_α,Z) の beth_{α+1} 個の独立な類があれば、それぞれの Z-拡大の E_α 上の fiber product を取る。N による

$$\operatorname{Hom}(\mathbb Z^J,\mathbb Z)=\mathbb Z^{(J)}$$

と connecting map の単射性から、E_{α+1}∈T となる。核は F に属するので内部単射であり、通常の全射でもある。torsion-free 性は拡大で保たれる。

α>0 が後続順序数なら、直前の核 Z^{beth_α} に Ext を制限する全射と、前段階の下界 r₀Ext(Z^μ,Z)≥2^μ により、必要な beth_{α+1} 個を供給できる。

α=λ が非零可算極限なら、共終な後続段を選び、§2 を適用する。各核 Z^{beth_{β_n+1}} は階数 beth_{β_n+1} の自由群を含むので、ρ_n=beth_{β_n+1}、κ=beth_λ として

$$r_0\operatorname{Ext}(E_\lambda,\mathbb Z)\ge2^{\beth_\lambda}
=\beth_{\lambda+1}$$

を得る。これで極限の後の拡大も作れる。

極限 E_λ の T 所属は、共終な可算列へ制限し、Z の inverse-limit slenderness を使う。全射の可算逆列の極限から Z への射はある段を経由し、その段の双対は零である。[Conner–Herfort–Kent–Pavešić, Theorem 3.6, Corollary 3.11](https://arxiv.org/pdf/2106.06032)。核 K_λ=ker(E_λ→B) は ∏_{α<λ}K_α の部分群なので F に属する。torsion-free 性も積と部分群で保たれる。

サイズについては、各後続射の集合としての section を選ぶと、連続性により集合の全単射

$$E_\alpha\cong_{\rm Set} B\times\prod_{\beta<\alpha}\mathbb Z^{\beth_{\beta+1}}$$

がある。後続 α>0 では和 Σ_{β<α}beth_{β+1}=beth_α、可算極限でも同じ等式が成立する。従って (3) を得る。群の直積分解は主張しない。∎

この定理では初段 B だけ |B|=ℵ₀ であり、(3) を α=0 に適用しない。

## 4. 核の長さは可算順序数全体で無界になる

R(A)=∩_{h:A→Z}ker h とし、下降する超限反復を R^θA と書く。各 K_α=ker(E_α→B) について

$$R^\alpha K_\alpha=0.\tag{4}$$

後続段では R^αK_{α+1} は自然性により (2) の torsionless な核に含まれるので、もう一回 R を適用すると零になる。極限段では各 K_β への射影と自然性から零になる。

一方、[前段階 §6.1](z_null_internal_subobjects_2026-11-15.md)の上界 κ_θ は、各可算 θ についてある可算 η により κ_θ≤beth_η と抑えられる。実際、κ₀=beth₀、後続では二回べき集合を取り、可算極限では可算個の和のべき集合を取るので、可算の beth 添字で足りる。

従って、任意の可算 θ に対し α<ω₁ を α+1>η となるように取れば、(3) とサイズ上界から R^θK_α≠0。つまり、

$$\sup_{\alpha<\omega_1}\min\{\theta:R^\theta K_\alpha=0\}=\omega_1.\tag{5}$$

これは一つの核がすべての可算長を超えたという主張ではない。それぞれの長さは可算で、族全体に可算の一様上界がない。長さ ω₁ という集合順序数の上界は残っている。

## 5. V=L なら後続段は任意の torsion-free T-対象で可能

Hiller–Huber–Shelah の [The Structure of Ext(A,Z) and V=L, Theorem 1 / Corollary 1, p.40](https://shelah.logic.at/files/95951/91.pdf) により、V=L の下で非自由 torsion-free 群 X の Ext の torsion-free rank は、自由な商 X/H を与える最小の H のサイズによって決まる。X* = 0 なら非零自由商はないので H=X しかなく、

$$r_0\operatorname{Ext}(X,\mathbb Z)=2^{|X|}\quad(0\ne X\in\mathcal T, X\text{ torsion-free}).\tag{6}$$

可算の場合も同じ結論である。この帰結は [Shelah–Strüngmann, A characterization of Ext(G,Z) assuming V=L, Lemmas 2.1 and 2.3](https://arxiv.org/pdf/math/0609638) に明記されている。Lemma 2.3 に弱コンパクト基数の非存在は不要である。確認日：2026年11月16日。

V=L は N を含意するので、(6) と拡大補題から

$$0\to\mathbb Z^{2^{|X|}}\to Y\to X\to0,\qquad
Y\in\mathcal T,\qquad |Y|=2^{2^{|X|}}>|X|\tag{7}$$

を作れる。Y は torsion-free、Y→X は内部単射かつ全射。X が既に固定 B の内部部分対象なら合成もそうなる。

従って V=L では、極限後の群が非零 torsion-free T-対象であると分かれば、その先の Ext 供給を個別に証明する必要はない。(7) は §3 の固定したサイズの構成とは別の、より大きくできる後続段である。

## 6. 非可算極限を無条件に扱えない理由

### 6.1 一般の全射逆系では実際に失敗する

Bergman, [Every module is an inverse limit of injectives, Theorem 4 and Corollary 11(b)](https://math.berkeley.edu/~gbergman/papers/lim_inj.pdf), Proc. AMS 141 (2013), 1177–1183 は、全射の非可算逆系が小さい極限を持つ構成を与える。確認日：2026年11月16日。

今回の群を用いたその構成の具体化を記す。非空集合 S_α と全射 S_β→S_α（α≤β<ω₁）からなり、逆極限が空となる系を用いる。この集合系の存在は同論文 (3) の文献入力である。p:P₀→B は前段階の核 Z の全射とし、

$$H_\alpha=\{(x,(y_s))\in P_0\oplus B^{(S_\alpha)}:
\sum_s y_s=p(x)\}.$$

s₀∈S_α を一つ選ぶと H_α≅P₀⊕B^{(S_α\setminus\{s₀\})}。従ってすべて torsion-free で T に属する。有限台の y を集合の全射に沿って足し合わせると、H_β→H_α も全射になる。

整合族 (y_α) の有限台の大きさは非減少であり、ω₁ の非可算共終度から一様に有限である。大きさが安定した後の台の間の写像は全単射になるので、非空なら S_α の逆極限の元を与えてしまう。従って y_α はすべて零。残る x は ker p に属し、

$$\varprojlim_{\alpha<\omega_1}H_\alpha\cong\mathbb Z\notin\mathcal T.\tag{8}$$

ただし、この系は今回の連続な内部単射の系とは異なる。非単射の集合写像から生じる核は B のコピーを含み、T-内部単射ではない。また連続なら §1 によって Z から H_α への射影が全射となるはずなので、途中の全極限段で連続でもあり得ない。(8) は今回の特殊な構成の失敗を証明したものではなく、「全射かつ torsion-free なら十分」という一般化の反例である。

### 6.2 既知の巨大な cellular cover も内部単射ではない

Farjoun–Göbel–Segev–Shelah, [On kernels of cellular covers, Proposition 2.9 and Theorem 2.10](https://shelah.logic.at/files/94961/892.pdf), pp.417–418 の固定標的に対する巨大な核は、K=Z[1/q_K]⊗H として作られる。従って非零の q_K-divisible 群で、Hom(K,Z)=0。K 自身が T に属するため K∉F であり、核の包含が内部単射性を反証する。この文献構成をそのまま非 well-poweredness に使うことはできない。確認日：2026年11月16日。

### 6.3 小さいデータを固定して極限を保護する方法の限界

次の三点は ZFC の直接計算である。

第一に、B⊂Z_p² の通常の部分群 p^nB はすべて B と同型で T に属し、同じ非零の有限 rank を持つが、∩_np^nB=0。従って、像の有限 rank が一定という条件だけでは非零の交わりを保証しない。この列の包含は全射ではなく、今回の塔の反例そのものではない。

第二に、固定した集合個の射 h_i:A_i→B（A_i∈T）が内部単射 E→B を経由するとする。持上げの像の和 J≤E は T に属し、J→B は内部単射で、すべての h_i が J を経由する。一方、|J|≤max(ℵ₀,Σ_i|A_i|)。従って、その固定した cone を保持する条件だけでは巨大な始域が不可欠になるとは言えない。

第三に、元を指定しても T 内の極限に保持されるとは限らない。q:Q→Q/Z は核 Z∈F の T-内部単射である。その通常の自己 pullback は {(x,y):x−y∈Z}≅Q⊕Z だが、T-coreflection は対角 Q である。同じ非零元 1/2+Z の持上げ (1/2,3/2) は通常の pullback に入り、対角には入らない。これは、Z から指定した元を持つ cone が T 内の pullback に残らない具体例である。

## 7. 証明を完結するために残る一つの極限命題

V=L で (7) を用いるなら、次の十分条件が焦点になる。

> 任意の集合順序数 γ に対し、固定 B 上で (7) の後続段を用いた連続な全射逆系を γ まで構成し、その途中のすべての非可算共終度の極限 L=lim E_α でも Hom(L,Z)=0 を同時に満たすように、拡大類を選べる。

この命題がすべての集合長で成り立てば、§1 から極限の B への全射性が保たれ、核は F に属し、(7) でサイズを増やし続けられる。任意の候補基数上界を超える集合長の構成を行えば、固定 B の内部部分対象が集合個でないと結論できる。全体のクラス選択公理を仮定する必要はない。

**この極限命題は未証明である。** §2 の有限和の議論は可算共終度を使い、非可算共終度では有界な一座標に既に無限個の項が現れる。一般の全射逆系には §6.1 の反例があるので、引用定理の単純な拡張では処理できない。

内部極限として t(L) を取れば必ず T に入るが、t(L)→B の全射性や非零性は保証されない。従って、coreflector を取るだけでこの穴を埋めたことにはならない。

なお T は ZFC で coreflective である。仮に上の極限命題から非 well-poweredness を示せても、一般の小さい coorthogonality class の非 coreflectivity、ひいては P の否定へ結び付ける仕事は別に残る。

## 8. 点検範囲

- すべての構成で T と B は固定した。auxiliary な拡大類の集合を変えることと、定義テスト {Z→0} を変えることを区別した。
- 全射性には連続性、零整数双対には可算共終度または未証明の追加条件が必要である。
- 可算順序数の族も集合個であり、(5) は非 well-poweredness そのものではない。
- T 内の epi は通常の全射と同値なので T は co-well-powered だが、それは well-poweredness を意味しない。既存の E₁→B は mono かつ epi で同型ではなく、T を abelian category として扱うこともできない。
- 非 well-poweredness、P の否定、ZFC 独立性はいずれも今回未確立である。
