# 修復列のサイズ上界と Weak Vopěnka principle

2026年11月16日。新しい直接証明の状態は PROOF_RECONSTRUCTED。既存の修復列の定理を前提とする。今回の含意は主担当が直接点検したもので、独立した担当による査読・形式検証・新規性確認はしていない。

**結論。** 固定したテスト集合と標的に対する正規化修復列が停止しなければ、ある presheaf 圏の slice に Ord の反対圏が充満埋め込みされる。従って Weak Vopěnka principle（WVP）の下ではすべての修復列が停止し、P が成立する。逆向きの P⇒WVP、¬WVP⇒¬P は証明していない。

ユーザーの「集合論的問題が見えたら一旦止まる」という指示に従い、この接続を記録したところで停止する。WVP の否定から特殊な修復列を構成する研究や、定義可能性の階層による仮定の弱化には進んでいない。

## 1 設定と使用する既存結果

C を小圏、K=Set^(C^op)、Σ={s_i:U_i→V_i} を射の集合とする。

$$
\mathcal A=\{X:\operatorname{Hom}_{\mathcal K}(X,s_i)
\text{ is bijective for every }i\}.
$$

Q は A の対象の通常の全射商からなる充満部分圏であり、同じ記号でその trace coreflector を表す。T は前段階で構成した、一意性を含む修復関手、F=QT|_Q とする。固定した B に対して

$$
B_0=QB,\qquad B_{\alpha+1}=F B_\alpha,\qquad
B_\delta=Q\left(\lim_{\alpha<\delta}B_\alpha\right)
$$

と置き、β≥α の遷移射を p_{βα}:B_β→B_α、構造射を b_α=p_{α0}:B_α→B_0 と書く。

[前段階の証明](positive_tower_2026-11-16.md)、§§3–5 より、次を使用する。

1. 全 B_α は Q の対象である。
2. 各 p_{βα} は A-equivalence、すなわち全 A∈A に対し Hom(A,p_{βα}) が全単射である。
3. 各 p_{βα} は K の通常の全射であり、Q の内部では mono である。特に b_α は Q-mono。
4. e_X:FX→X が section を持てば X∈A であり、e_X は同型になる。実際、e_X=t_X q_{TX} の section は t_X の section を与え、修復関手の補題1を適用できる。
5. B の A-coreflection の存在、修復列の停止、全 B_α の carrier サイズの集合基数による共通上界は同値。

ここで Q 内部の mono と K の mono を混同しない。b_α が K の mono であるとは仮定しない。

## 2 後の段階への一つの射が停止を強制する

**補題。** α<β とし、K/B_0 における射

$$
u:(B_\alpha,b_\alpha)\longrightarrow(B_\beta,b_\beta),
\qquad b_\beta u=b_\alpha
$$

が存在すれば、B_α∈A であり、e_{B_α}:B_{α+1}→B_α は同型になる。

**証明。** b_β=b_αp_{βα} なので

$$
b_\alpha p_{\beta\alpha}u=b_\alpha.
$$

B_α と B_β は Q に属し、b_α は Q 内で mono である。従って

$$
p_{\beta\alpha}u=1_{B_\alpha}.
$$

β≥α+1 だから、v=p_{β,α+1}u:B_α→B_{α+1} が定義され、

$$
e_{B_\alpha}v
=p_{\alpha+1,\alpha}p_{\beta,\alpha+1}u
=p_{\beta\alpha}u
=1_{B_\alpha}.
$$

よって e_{B_α} は section を持つ。§1の4から B_α∈A、従って e_{B_α} は同型である。□

この証明は、単なる同型類の反復や、同じ大きさの対象が二度出現することを仮定していない。必要なのは、固定した B_0 への射と可換な「前から後への射」である。

## 3 非停止なら Ord の反対圏が充満埋め込みされる

**定理。** 上の列がどの集合順序数でも停止しないと仮定する。このとき

$$
\operatorname{Hom}_{\mathcal K/B_0}
\big((B_\beta,b_\beta),(B_\alpha,b_\alpha)\big)
=
\begin{cases}
\{p_{\beta\alpha}\},&\beta\geq\alpha,\\
\varnothing,&\beta<\alpha.
\end{cases}
$$

従って α↦(B_α,b_α) は充満忠実な関手

$$
\mathrm{Ord}^{op}\longrightarrow\mathcal K/B_0
$$

を与える。

**証明。** β≥α なら標準の遷移射がある。同じ slice 内の二射 u,v:B_β→B_α は b_αu=b_αv を満たす。両対象が Q に属し b_α が Q-mono なので u=v。従って射はちょうど一つである。

β<α の場合、B_β→B_α という slice 射があれば§2の補題によって β 段階で停止してしまう。非停止の仮定に反するので射は存在しない。

遷移射の合成則は逆列の定義から従い、上の Hom の計算が充満忠実性を与える。□

K/B_0 は局所可呈示である。さらに presheaf の slice 表示により

$$
\mathcal K/B_0\simeq
\mathbf{Set}^{(\int_C B_0)^{op}},
$$

であり、要素の圏 ∫_C B_0 は小さい。従って埋め込み先は再び presheaf 圏として取れる。

固定した集合パラメータ C,Σ,B から各段階を定義している点にも注意する。T は明示的な集合添字の積と pullback、Q は全 Q-部分対象の和集合であり、各集合長の段階は ZFC の超限再帰で作れる。非停止を仮定したときの族は、集合パラメータから定義された class sequence として扱える。真のクラス長の極限対象を形成しているわけではない。

## 4 WVP による条件付きサイズ上界

WVP の標準的な圏論的定式化は、Ord^op がどの局所可呈示圏にも充満埋め込みされない、というものである。この定式化は Casacuberta–Gutiérrez, §1.1(b) にも明記されている。WVP 自体は通常の ZFC 定理ではなく、追加の集合論的原理である。[一次資料](https://www.ub.edu/topologia/casacuberta/articles/Semiweak.pdf)

**系。** WVP を仮定すれば、任意の小圏 C、テスト集合 Σ、標的 B について上の正規化修復列は停止する。従って全 B_α のサイズに集合基数の共通上界がある。

**証明。** 非停止なら§3が WVP に反する。停止と上界の同値は既存の定理7である。直接には、停止段階 γ 以後は B_γ と同型になり、α≤γ では B_γ→B_α が全射なので、κ=max(ℵ₀,|B_γ|) が全段階の上界になる。□

これは上界の存在を追加原理から導く証明であり、ZFC 単独の上界や、C,Σ,B の濃度からの明示的な基数公式を得たわけではない。

各 presheaf 圏における coreflection の存在と、既存の充満反射部分圏への移送から

$$
\boxed{\mathrm{WVP}\Longrightarrow P}
$$

を得る。対偶は ¬P⇒¬WVP である。通常の Hom の命題 P へのこの含意は、既存の修復列の性質と§§2–3からここで導いたものであり、引用文献のホモトピー局所化定理を適用したものではない。

## 5 ここで残る問題と停止範囲

今回、サイズ上界の問題は「この特殊な修復列から Ord^op の充満埋め込みが生じることを排除できるか」という形になった。WVP はそれを排除する十分条件を与える。

ただし、WVP の否定が与える一般の Ord^op の充満埋め込みを、固定した小さいテスト集合による今回の正規化修復列として実現できるとは示していない。従って

$$
P\Longrightarrow\mathrm{WVP},
\qquad
\neg\mathrm{WVP}\Longrightarrow\neg P
$$

はいずれも未証明である。WVP が P に必要、P が WVP と同値、P が ZFC から独立、という結論は得られていない。

ZFC 肯定には、一般の WVP に頼らず、この修復列の特殊性から§3のパターンを排除する証明が必要になる。独立性へ向かうには、集合論側の反例と固定テストによる修復列を結ぶ追加の実現定理が必要になる。どちらも今回ここから先は追わず、ユーザー指定の停止点とする。

## 境界点検

- 空テスト族・同型だけのテストでは初めから停止するので、非停止定理の仮定を満たさない。
- α=0 では b_0 が恒等射で、§2の補題はそのまま成立する。
- 後続・極限の β を区別する必要はなく、β≥α+1 の遷移射を使う。
- Q 内の mono 性を使う二射の始域と終域はすべて Q に属している。
- 充満埋め込みは slice K/B_0 内で主張する。B_0 と可換でない任意の K-射の不存在は主張しない。
- 集合サイズのどの長さまでも列を作れることと、真のクラス長の極限を集合として取れることは別であり、後者は用いていない。

## 参考資料

- Casacuberta–Gutiérrez, *Homotopy reflectivity is equivalent to the weak Vopěnka principle*, Introduction および §1.1(b)。WVP の局所可呈示圏による定式化のみを使用。https://www.ub.edu/topologia/casacuberta/articles/Semiweak.pdf
- Bagaria–Wilson, *The Weak Vopěnka Principle for definable classes of structures*, §2。Ord^op の graph への充満埋め込みによる定義と、集合パラメータによる定義可能 class の背景を確認。https://doi.org/10.1017/jsl.2022.42

文献確認日：2026年11月16日。
