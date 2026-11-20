# 可測基数が存在しない場合の道具一覧

確認日：2026年11月15日。仮定を N=「非可算の可測基数が存在しない」とする。measurable は非主 κ-complete ultrafilter を持つ非可算基数 κ の意味であり、real-valued measurable とは区別する。古い文献の「非主可算完備超フィルターを支える基数」という用語も、存在・非存在を全基数について量化すれば同じ N を与える。

目的は、[P の独立性に向けた否定側の方針](no_measurable_strategy_2026-11-15.md)に使える結果を先に広く集めること。以下の14項目は独立した14定理という意味ではなく、共通の超フィルターの事実から派生する道具も含む。P⇒可測基数の存在、N⇒¬P、反鎖型の小さい I_S 表示は未証明。

## 1 一覧と用途

「文献確認」は記載した一次資料で仮定・結論を確認したもの。「直接導出」は以下で証明を再構成したもの。優先度は今回の ordinary-Hom の問題への近さであり、定理の一般的重要性ではない。

| 番号 | N の下で使える結果 | 今回の用途・限界 | 状態・出典 |
|---|---|---|---|
| T1 | 任意の集合上の可算完備超フィルターは主超フィルター。従って非主超フィルターには、どの部分もその超フィルターに属さない可算分割がある | 高：余分な極限操作や積からの射を排除する共通原理。通常の非主超フィルター自体は消えない | 文献確認：[Bergman, §1, Lemma 4 直前](https://math.berkeley.edu/~gbergman/papers/cap_ultra.pdf)。分割への言い換えは直接導出 |
| T2 | 可算無限集合 Ω の一対象充満部分圏が Set で codense | 高：任意の対象を固定した一対象への射から回収する。ただし小さい商による所属判定とは別 | 文献確認：[Isbell, 2.5](https://conceptualmathematics.wordpress.com/wp-content/uploads/2013/05/adequatesubcategories.pdf) |
| T3 | M=End(Ω) とすると、X↦Ω^X が Set^op から M-Set への充満忠実埋め込み。像は reflective | 高：前層圏内で反対向きの集合の射を正確に符号化する。任意余極限や coorthogonality の移送は自動ではない | 埋め込みは [Shulman, p.20](https://arxiv.org/pdf/0810.1279)。随伴と境界は §2 で直接導出 |
| T4 | 任意の I に対し Hom(Z^I,Z)=Z^(I)。各準同型は有限個の座標射の整数線形結合 | 高：大きい積から固定標的 Z への全ての射を計算できる | 文献確認：[Blass–Shelah, Theorem 6 と直後](https://shelah.logic.at/files/182621/854.pdf)から T1 を適用 |
| T5 | 任意の単位的環上の slender module H への射 ∏ A_i→H は有限部分積を経由する | 高：T4 を一般の module の固定標的へ拡張。標的の slenderness を省略しない | 文献確認：[Bergman, §4.1, (25), Łoś–Eda theorem](https://math.berkeley.edu/~gbergman/papers/cap_ultra.pdf)から T1 を適用 |
| T6 | 自由アーベル群 Z^(I) と積 Z^I は、代数的双対 `A*=Hom(A,Z)` に関して `A≅A**` | 中：射の向きを反転する際の正確な対象族。任意の Ab 対象や Pontryagin 双対の主張ではない | T4 から直接導出、§3 |
| T7 | 単位的環準同型 Z^X→Z^Y は、唯一の写像 Y→X の引き戻し。従って Set^op は可換単位的環の圏にも充満忠実に埋め込める | 中：有限項の演算だけを使う符号化。ゼロ環を含める。全 Ab の双対埋め込みではない | T4 から直接導出、§3 |
| T8 | 無限 κ に対し B_κ=Z^κ/Z^{<κ} は非零で Hom(B_κ,Z)=0。さらに正則 κ>\|G\| なら G→B_κ は Z^κ に持ち上がる | 最優先：小さい候補 G を、より大きい B_κ で破る。持上げ自体は ZFC であり N は不要 | 文献確認：[Casacuberta–Scevenels, Theorem 3 と Theorem 5 の証明](https://rac.es/ficheros/doc/00051.pdf)。§4 で再構成 |
| T9 | Ab に積・retract に閉じるが weakly reflective でない充満部分圏がある。B_κ 全体の積・retract 閉包が一例 | 高：固定した Z からの解集合条件が実際に破れる。P とは反射の向きが逆 | 文献確認：[Casacuberta–Gutiérrez–Rosický, Proposition 2.6](https://www.ub.edu/topologia/casacuberta/articles/cgr.pdf)。Corollary 2.7 はスペクトルのホモトピー圏への移送 |
| T10 | T={A∈Ab : Hom(A,Z)=0} は積に閉じ、weakly reflective でなく、生成対象の集合も持たない。しかし一つの mono への coorthogonality class であり ZFC で coreflective | 高：T8 の簡単な応用であり、向きと小ささを検査する対照例。「非 accessible⇒非 coreflective」はここでも失敗 | 直接導出、§5。新規性は主張しない |
| T11 | Grp には、射のどの集合 S に対する S^⊥ とも一致しない reflective class がある。B_κ 全体による reduction の像が一例 | 高：小さい表示の不存在を証明する実例。ただし普遍射の不存在ではない | 文献確認：[Casacuberta–Scevenels, Theorems 1(c), 5](https://rac.es/ficheros/doc/00051.pdf) |
| T12 | F:Set→Set が cofiltered limits を保存するなら、F-coalgebra を一つの操作記号を持つ coequational theory で表示できる。N の下では基準集合 Ω を可算にできる | 中：条件を満たす別の関手の圧縮に使える。反鎖型の endocoreflector は保存条件を満たさない | 文献確認：[Kurz–Rosický, Proposition 2.7, Remark 2.8(2)](https://alexhkurz.github.io/papers/cosig/cosig.pdf) |
| T13 | 全ての距離空間が realcompact。特に任意の離散集合は realcompact | 低：実数値関数による対象の回収。今回の前層圏・ordinary Hom への接続は未確立 | [Comfort–Negrepontis, §2.7](https://matwbn.icm.edu.pl/ksiazki/fm/fm59/fm5911.pdf)の一次資料の索引本文で確認。全文取得は HTTP 403 |
| T14 | 任意の群が弧状連結な compact Hausdorff space の基本群として実現できる | 低：対象の実現結果であり、Hom 集合を保存する埋め込みではない。strict coorthogonality は直接移せない | [Przeździecki, Fund. Math. 192 (2006), 87–92](https://doi.org/10.4064/fm192-1-6)の出版社 Abstract を確認。本文の定理番号は今回未照合 |

T1–T7 は主として「射が余計な超フィルターに由来しなくなる」ことを使う。T8–T11 は、その制約を使って小さい生成・因子化候補を破る。この二系統を別々の目的に使うのがよい。

## 2 前層圏への具体的な埋め込み T3

**仮定・圏。** ZFC+N。Ω は可算無限集合、M=End_Set(Ω)。M-Set は左 M-作用の圏 [M,Set] であり、小さい圏 M^op 上の前層圏である。M 自体が可算とは主張しない。

F:Set^op→M-Set を F(X)=Ω^X、作用を u·h=u∘h と定義する。Isbell 2.5 の codensity は、自然な写像

\[
\operatorname{Set}(Y,X)
\longrightarrow
\operatorname{Hom}_{M\text{-Set}}(\Omega^X,\Omega^Y)
\]

が全単射であることを意味する。

**随伴の確認。** Ω を自然な M-作用を持つ対象とみなし、L(A)=Hom_M(A,Ω) を Set^op の対象とする。積の普遍性から

\[
\operatorname{Hom}_M(A,\Omega^X)
\cong\operatorname{Set}(X,\operatorname{Hom}_M(A,\Omega))
=\operatorname{Set}^{op}(L(A),X).
\]

従って L⊣F。F が充満忠実なので像は reflective である。

**境界点検。** F は ambient coproduct を一般には保存しない。Set^op では 1⊔1=1 だが、M-Set における Ω⊔Ω と Ω の間の標準比較射は fold であり、同型でない。従って「充満忠実埋め込みがある」だけで、colimit-closed class や small coorthogonality class がそのまま移るとは言えない。空集合についても、F(∅) は自明作用を持つ一元集合であり、そこから Ω への equivariant map は存在しない。これは Set(X,∅) の向きと整合する。

状態：埋め込みの出発点は `STANDARD`、上の随伴・境界確認は `PROOF_RECONSTRUCTED`。

## 3 積からの射と双対 T4–T7

T4 は Balcerzyk の定理が与える有限個の可算完備超フィルターを、N の下で全て主超フィルターに置き換えたものである。従って各 h:Z^I→Z には有限 F⊂I と整数 c_i があり、h(x)=Σ_{i∈F}c_i x_i。この表示は零係数を除けば一意。

**T6 の導出。** F_I=Z^(I) と P_I=Z^I に対して F_I*=P_I は ZFC で成立し、N の下で P_I*=F_I。これらの同型は座標射と基底により与えられるので、F_I→F_I** と P_I→P_I** という標準評価射そのものが同型である。

**T7 の導出。** まず単位的環準同型 h:Z^X→Z を考える。加法群の射として上の有限和表示を持つ。各座標冪等元 e_i から c_i²=c_i、異なる i,j に対して e_i e_j=0 から c_i c_j=0、単位元から Σc_i=1 を得る。従って一つだけ c_i=1 であり、h はその座標射である。Z^Y への射について各 y 座標に適用すれば、唯一の Y→X を得る。

**境界点検。** 単位保存を外すと零射も許されるので「唯一の座標射」は成り立たない。X=∅ の場合は Z^∅ をゼロ環とし、ゼロ環から非零環への単位的射はない。Y=∅ の場合は終対象への唯一の射がある。巨大基数の側では、非主可算完備超フィルターに沿う Z-値の極限が、座標射でない単位的環準同型を実際に与える。

状態：T4 は `STANDARD`、T6–T7 の上記導出は `PROOF_RECONSTRUCTED`。全てのアーベル群が二重双対と同型になるとは主張しない。

## 4 reduced product と小さい群からの持上げ T8

κ は無限基数とし、Z^{<κ} は台のサイズが κ 未満の元からなる Z^κ の部分群とする。B_κ=Z^κ/Z^{<κ}、商写像を q_κ と書く。有限 κ をこの定義の対象に含めない。

**零双対。** N の下では Hom(B_κ,Z)=0。実際、h:B_κ→Z を q_κ と合成すると T4 の有限座標和になる。一方、各座標基底元は Z^{<κ} に属するので全係数が零である。対角写像 d_κ:Z→B_κ は単射であり、B_κ は非零。非零整数の定数列の台が κ 全体であることを使う。

**持上げ補題（ZFC）。** κ が無限正則基数、G が |G|<κ の群なら、任意の f:G→B_κ に g:G→Z^κ があり q_κ g=f。

各 a∈G について f(a) の代表 φ(a)∈Z^κ を選ぶ。全ての a,b∈G に対する φ(a)+φ(b)−φ(ab) の台の和集合 E は κ 未満である。ここで正則性と |G|²<κ を使う。E 上の座標を全て零にした g(a) は群準同型になり、q_κ g(a)=f(a) を満たす。∎

この証明は [Casacuberta–Scevenels, Theorem 5 の証明](https://rac.es/ficheros/doc/00051.pdf)にある Wald–Łoś 型の持上げを再構成したもの。

**組合せて得る判定。** G∈Ab、Hom(G,Z)=0、κ>|G| が正則なら

\[
\operatorname{Hom}(G,B_\kappa)=0.
\]

持ち上げた G→Z^κ の各座標が零だからである。この判定自体にも N は不要であり、N が保証するのは全ての B_κ 自身が Z-null になること。特に N の下で κ>|B_λ| が正則なら Hom(B_λ,B_κ)=0。

**用途。** 集合個の Z-null な対象を先に与えられても、その全てのサイズより大きい正則 κ を選べば、どの対象からも非零射を受けない非零 B_κ がある。固定した族を後から大きい対象で破る、明示的な方法である。

**境界点検。** 正則性と |G|<κ は必要な証明条件として保持する。特異 κ で同じ持上げを主張しない。G=Z の場合は対角射が持ち上がるが、Hom(Z,Z)≠0 なので上の零射の帰結は適用されない。κ が可測なら κ-complete ultrafilter に沿う極限が B_κ→Z の非零射を与え、N を外した全称主張は失敗する。

状態：文献の命題は `STANDARD`、この組合せと境界確認は `PROOF_RECONSTRUCTED`。

## 5 一つのテストを持つ対照例 T10

Ab の充満部分圏

\[
\mathcal T=\{A:\operatorname{Hom}(A,\mathbb Z)=0\}
={}^\perp\{0\hookrightarrow\mathbb Z\}
=I_{\{\mathbb Z\to0\}}
\]

を取る。coorthogonality は ordinary Hom の全単射性、I_S は単射性である。Ab では零射が常にあるので、どちらも Hom(A,Z) が零群である条件に一致する。

**(a) ZFC で coreflective。** T は直和と全射商に閉じる。任意の A の中の T-部分群全体の和 t(A) は、集合個の T-対象の直和の全射商なので T に属する。任意の T-対象から A への射の像も T に属し、t(A) を一意に経由する。従って t(A)↪A は coreflection。t(A) を単なる ∩_{f:A→Z}ker f と同一視する議論は不要である。

**(b) N の下で積に閉じる。** T5 を標的 Z に適用する。各 A_i∈T に対し、∏A_i→Z は有限部分積を経由し、その各座標制限が零なので全体も零。retract に閉じることは ZFC で従う。

**(c) N の下で Z は T への弱反射を持たない。** 任意の候補 w:Z→A、A∈T に対し、正則 κ>|A| を選ぶ。§4 から Hom(A,B_κ)=0 だが、B_κ∈T かつ d_κ:Z→B_κ は非零である。従って d_κ は w を経由しない。同じ議論を集合個の候補のサイズ上界に適用すれば、(Z↓T) に弱始対象の集合も存在しない。

**(d) N の下で T に生成対象の集合はない。** 集合 G⊂T の全対象のサイズより大きい正則 κ を取ると、全ての G∈G について Hom(G,B_κ)=0。従って B_κ の恒等射と零射を G からの射で区別できない。特に T は accessible ではない。

これは反射の方向では具体的な解集合条件の失敗だが、余反射は (a) で存在する。**T10 は P の反例ではない。** T の非 well-poweredness も、この議論では示していない。

状態：`PROOF_RECONSTRUCTED`。T4–T5 と Wald–Łoś 型持上げからの帰結を主担当で点検したもので、新規性・独立査読・形式検証は主張しない。空群、有限群、G=Z、および可測 κ の側を境界として点検した。

## 6 次に使う候補と残る接続

第一候補は T4・T5・T8 の組合せ。任意のサイズの対象に関する Hom の計算ができ、「小さい因子化候補を一つの大きい対象で破る」議論まで具体化できる。T9 と T10 はその見本になる。ただし現在得ている失敗は Z から外へ出る射の因子化であり、P が要求する固定 B へ入る射の因子化へ向きを移す必要がある。

第二候補は T2・T3。Set^op の射を前層圏内に忠実に運べる点で、単に Ab^op を取るより具体的。ただし T3 が埋め込むのは Set^op であり Ab^op そのものではない。構造とその射を追加して符号化する場合も、集合個のテストを維持し、ambient な余極限との整合を示さなければならない。T7 は代数的な別の表現先を与える。

**2026年11月16日の追究。** [Set^op の検討](setop_coorthogonality_2026-11-16.md)により、裸の像内のテストは全て ZFC の肯定例となり、任意の非自明なテストに対しても無限 Ω^X は所属できないと判明した。単純な対角図式も有界な因子化先を持つ。一般の構造付き図式への充満埋め込みは可能だが、固定テストと解集合条件失敗を両立させる構成は未完成である。

反鎖型 C=I_S の問題では、前段階の「固定 κ 以下の商で非所属を検出する」という条件を引き続き使う。T2 から可算商で所属が判定できるとは結論しない。T11 は、否定側の仮定が小さい表示を可能にするとは限らず、逆に小さい表示の障害にもなることを示す比較例である。

T12 は保存条件を満たす別候補が出た場合の道具として保留する。[前段階のループ逆列](no_measurable_strategy_2026-11-15.md)により、反鎖型 coreflector と包含との合成には直接適用できない。T13–T14 は対象表現の候補として残すが、現時点では ordinary Hom の正確な移送がないため優先しない。

## 7 仮定と資料の境界

- この一覧の全称的な帰結には V=L を使用していない。V=L、GCH、diamond、内的モデルの不存在などを N と同一視しない。
- T1 は全べき集合上の可算完備超フィルターの話である。任意の σ-代数上の {0,1}-値測度まで全て Dirac と結論しない。例えば非可算集合の可算・余可算 σ-代数には、ZFC で非 Dirac な {0,1}-値可算加法的測度がある。
- real-valued measurable に関する結果は、仮定が異なるため今回の一覧に混ぜていない。
- T9 のホモトピー圏版や T14 の基本群の実現を、strict coorthogonality の反例として使わない。
- T1–T12 の主な根拠は論文本文で確認した。T13 は一次資料の検索索引にある §2.7 の本文、T14 は出版社 Abstract までの確認であり、優先候補として本格的に使う際は本文の確認を追加する。
- 文献結果の採用と今回の直接導出は区別した。理論的調査なので有限探索は実行していない。独立性の証明や一般の P の判定は得ていない。

## 8 主要資料

1. J. R. Isbell, *Adequate subcategories*, Illinois J. Math. 4 (1960), 541–552, 2.5, pp.549–550。[本文](https://conceptualmathematics.wordpress.com/wp-content/uploads/2013/05/adequatesubcategories.pdf)。T2 の元の結果。
2. G. M. Bergman, *Families of ultrafilters, and homomorphisms on infinite direct product algebras*, J. Symbolic Logic 79 (2014), 223–239, §1 および §4.1 (25)。[著者版](https://math.berkeley.edu/~gbergman/papers/cap_ultra.pdf)。T1・T5。著者の measurable の定義では ℵ₀ を含むため、本文の uncountable measurable と本ノートの measurable が対応する。
3. A. Blass and S. Shelah, *Ultrafilters and Partial Products of Infinite Cyclic Groups*, Comm. Algebra 33 (2005), 1997–2007, Theorem 6。[著者版](https://shelah.logic.at/files/182621/854.pdf)、[刊行版の著者保管コピー](https://shelah.logic.at/files/95765/854.pdf)。T4。全文の数式抽出は著者版の方が読みやすい。
4. C. Casacuberta and D. Scevenels, *On the existence of group localizations under large-cardinal axioms*, RACSAM 95 (2001), 163–170, Theorems 1, 3, 5。[本文](https://rac.es/ficheros/doc/00051.pdf)。T8・T11。T10 はこれらの道具から本ノートで導出。
5. C. Casacuberta, J. J. Gutiérrez and J. Rosický, *Are all localizing subcategories of stable homotopy categories coreflective?*, 2013年11月4日付著者版, Proposition 2.6, Corollary 2.7, p.15。[本文](https://www.ub.edu/topologia/casacuberta/articles/cgr.pdf)。T9。
6. A. Kurz and J. Rosický, *Operations and Equations for Coalgebras*, 2004年受稿の著者版, Proposition 2.7, Remark 2.8, pp.7–8。[本文](https://alexhkurz.github.io/papers/cosig/cosig.pdf)。T12。
7. M. A. Shulman, *Set theory for category theory*, arXiv:0810.1279v2 (2008), p.20。[本文](https://arxiv.org/pdf/0810.1279)。T3 の圏論的な定式化。
8. W. W. Comfort and S. Negrepontis, *Extending continuous functions on X×Y to subsets of βX×βY*, Fund. Math. 59 (1966), 1–12, §2.7。[出版社](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/59/1/96102/extending-continuous-functions-on-x-x-y-to-subsets-of-x-x-y)。T13。Gillman–Jerison の結果への言及を確認。
9. A. Przeździecki, *Measurable cardinals and fundamental groups of compact spaces*, Fund. Math. 192 (2006), 87–92。[DOI](https://doi.org/10.4064/fm192-1-6)。T14。著者版と刊行版で定理番号が異なる可能性があり、今回は番号を固定していない。
