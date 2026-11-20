# Problem 4：一般化 Specker 群の limit・directed union 閉包は torsion-free 群全体

2026-11-18。状態：PROOF_RECONSTRUCTED（明示的な equalizer による閉包計算）。独立査読・形式検証・新規性確認は未実施。No.4 の反例ではなく、この候補を除外する結果。

内部確認：別 agent が §2 の maximal matching（singular κ を含む）と §4 の閉包計算を監査し、問題を見出さなかった。これは外部査読・形式検証ではない。

## 1. 既知の非反射的候補と、確認できた範囲

無限基数 κ に対して

    B_κ=Z^κ/Z^{<κ},
    Z^{<κ}={x∈Z^κ:|supp(x)|<κ}

と置き、S を全ての B_κ から小積と retract で生成される Ab の full replete subcategory とする。

Casacuberta–Gutiérrez–Rosický, *Are all localizing subcategories of stable homotopy categories coreflective?*, Adv. Math. 252 (2014), Proposition 2.6 は、measurable cardinal が存在しないという仮定の下で S が weakly reflective でないことを示す。この命題が保証するのは積・retract 閉性であり、equalizer 閉性や directed union 閉性ではない。[著者版 PDF、p.15](https://www.ub.edu/topologia/casacuberta/articles/cgr.pdf)

以下の閉包計算は ZFC で成り立つ。

## 2. 置換で全ての非定数剰余類を検出する

**組合せ補題。** |I|=κ が無限で f:I→Z とする。f が「ある定数 n と、κ 未満の例外集合を除いて一致する」という形でなければ、ある置換 π:I→I に対して

    |{i∈I:f(i)≠f(π(i))}|=κ。

**証明。** f(a)≠f(b) となる互いに素な二点集合 {a,b} の、包含について極大な族 M を取る。もし |M|<κ なら、M の点対に使われていない点の集合 U は濃度 κ を持つ。M の極大性から f は U 上で一定。ところが I\U は濃度 κ 未満なので、これは f が例外集合を除いて定数であることを意味し、仮定に反する。よって |M|=κ。M の各点対を交換し、残りを固定する置換 π について、差が現れる点は少なくとも κ 個ある。□

κ は正則でなくてもよい。この証明は singular cardinal と κ=ω の場合にもそのまま適用できる。

## 3. 一つの B_κ と積・equalizer から Z が生成される

座標置換 π∈Sym(κ) は Z^{<κ} を保つので、B_κ の自己同型 a_π:[f]↦[f∘π] を誘導する。二射

    a,d:B_κ⇉∏_(π∈Sym(κ)) B_κ,
    a(x)=(a_π(x))_π,  d(x)=(x)_π

を考える。

**補題（ZFC）。** Eq(a,d) は対角定数剰余類からなる部分群で、Z と同型である。

**証明。** 定数関数の剰余類は全ての置換で固定される。逆に [f] が全ての置換で固定されるなら、全ての π に対して {i:f(i)≠f(π(i))} の濃度は κ 未満である。§2 の補題により、f は κ 未満の例外集合を除いてある定数 n と一致する。従って [f]=[const_n]。異なる整数の定数関数の差は台が κ 全体なので、n↦[const_n] は単射である。□

従って、一つでも B_κ を含む任意の limit-closed full replete subcategory は Z を含む。この議論には B_ω の構造定理も、retract 閉包も、大基数仮定も不要である。

## 4. directed union を加えた閉包の正確な計算

TF を torsion-free abelian groups の full subcategory とする。

**定理（ZFC）。** S を含み、Ab の全ての小極限と directed union で閉じた最小の full replete subcategory は TF である。任意の一つの無限 κ について B_κ 一対象だけから出発しても同じ結論になる。

**証明。** まず B_κ は torsion-free。実際、整数 n≠0 について n[x]=0 なら supp(nx)=supp(x) の濃度が κ 未満であり、[x]=0。TF は積と部分群で閉じるため全ての小極限で閉じる。また torsion-free 群の directed union は torsion-free。従って求める閉包は TF に含まれる。

逆に、§3 によりその閉包は Z を含むので、有限積 Z^n も含む。任意の torsion-free abelian group G はその finitely generated subgroups の directed union であり、各 finitely generated subgroup は有限ランク自由 abelian group Z^n である。従って G は閉包に属する。□

TF は反射的である。反射は

    G ↦ G/t(G)

で、t(G) は G の torsion subgroup。G/t(G) は torsion-free で、torsion-free 群への全ての準同型は t(G) を消すので、この商写像は反射の普遍性を満たす。

以上により、一般化 Specker 群から「積・retract の非弱反射的部分圏を取り、さらに極限と directed union で閉じる」という構成は、No.4 の反例を与えない。閉包の反射性には大基数仮定もその否定も不要。

## 5. 元の S の equalizer 閉性が失敗する場所（N）

N、すなわち measurable cardinal が存在しないと仮定する。このとき、任意の集合 I に対し Z^I→Z の準同型で有限台部分群 Z^(I) を消すものは零である。これは一般化 Specker theorem の帰結であり、上記 Casacuberta–Gutiérrez–Rosický の Proposition 2.6 の証明末尾でも、Fuchs, *Infinite Abelian Groups II*, 94.4 として使われている。

これから Hom(S,Z)=0 が従う。実際、S の対象 A は ∏_j B_(κ_j) の retract である。もし h:A→Z が非零なら、retraction r:∏_j B_(κ_j)→A と全射

    ∏_(i∈I) Z → ∏_j B_(κ_j),  I=disjoint_union_j κ_j

を前合成して、非零の準同型 Z^I→Z を得る。各有限台ベクトルの各 block は Z^{<κ_j} に属するので、この準同型は直和 Z^(I) を消す。矛盾。

従って Z∉S。一方 §3 の a,d の source と target は S に属し、equalizer は Z である。これにより、N の下では S の equalizer 閉性の失敗が具体的に特定される。

注意：この節の N は S 自身の外側に Z があると示すための仮定である。§4 の閉包計算は N を使わない。

## 6. 研究上の境界

同じ論法は、torsion-free 群だけからなり、一つでも B_κ を含む任意のクラスに適用できる。その極限・directed union 閉包は TF になる。特に B_ω を生成系から除き、非可算 κ に限定しても、この障害はなくならない。

これは任意の Ab の limit・directed union 閉部分圏が反射的であるという主張ではなく、上記の具体的生成系に対する閉包計算である。

## 7. 独立した確認：B_ω の既知の分解からも Z が得られる

Goldsmith–Kelly–Wallutis, *On Cotorsion Images of the Baer–Specker Group*, Irish Math. Soc. Bulletin 54 (2004), Proposition 5 は、c=2^ℵ₀ として

    B_ω ≅ Q^(c) ⊕ ∏_(p prime) completion_p(Z_p^(c))

を示す。括弧付き冪は直和である。[原論文 PDF、pp.28–29](https://www.maths.tcd.ie/pub/ims/bull54/R5401.pdf)

この分解から Q と各 Z_p は B_ω の retract となる。Z_p については直和の一座標への inclusion・projection を p-adic completion に延長すればよい。任意の Q-vector space は Q の積の retract なので、Q_p も S に属する。従って

    Q×∏_p Z_p → ∏_p Q_p,  (q,(z_p))↦(q−z_p)_p

の kernel も S の極限閉包に属する。この kernel は ∩_p(Q∩Z_p)=Z によって Z と同型である。これは §3 とは独立した、B_ω に対する確認になる。
