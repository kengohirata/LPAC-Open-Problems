# CompHaus 版 No.8(b) の集合論的な上界と下界

2026年11月19日。\(K=\mathrm{CompHaus}\) とし、\(P\) を「\(K\) の小極限閉な充満・同型閉部分圏はすべて直交類である」とする。テスト射には真クラスを許す。以下は既知の定理を組み合わせた証明案であり、\(P\) についての結論は独立検証前である。クラスと VP・WVP には同じクラス解釈を使う。以下のランクモデルは、全クラスを許す場合には \((V_\kappa,\mathcal P(V_\kappa))\) と読む。

**再点検による更新。** 後続の輪の構成を使うと、以下の否定方向から WVP を除ける。CompHaus 版の \(P\) は VP と同値になる。以下は当初のスライスによる証明を記録する。[コンパクト性と真クラスの選択を含む証明](proof_check_top_comphaus.md)

## 1. 二つの反射性定理を使う場所

\(L=K^{\mathrm{op}}\) は可算アリティの代数の圏と同値なので局所可呈示である。VP の下で Adámek–Rosický 6.28 を使うのは、\(L\) の**余極限閉**部分圏 \(\mathcal C^{\mathrm{op}}\) を**余反射的**とする段階である。双対の反射射から直交類表示を得るのは ZFC の議論である。[原著第6章](https://doi.org/10.1017/CBO9780511600579.009)・[Marra–Reggio](https://arxiv.org/abs/1508.07750)

一方 WVP の下では、局所可呈示圏の**極限閉**充満部分圏が**反射的**になる。この定理を別の圏に適用すると、\(K\) の任意の直交類が反射的であることを示せる。以下がその導出である。[Casacuberta–Gutiérrez, Introduction, 通常の圏についての同値条件](https://www.ub.edu/topologia/casacuberta/articles/Semiweak.pdf)

\(\mathcal D\subset L\) がある射のクラス \(S\) で定まる余直交類、すなわち \(D\in\mathcal D\) と「すべての \(s\in S\) で \(L(D,s)\) が全単射」が同値とする。\(X\in L\) を固定する。スライス \(L/X\) の対象 \(p:Y\to X\) で、すべての \(D\in\mathcal D\) について \(L(D,p)\) が全単射になるものからなる充満部分圏を \(E_X\) とする。\(E_X\) はスライスで小極限閉である。実際、各 \(a:D\to X\) について、\(a\) の \(p\) を経由する持ち上げがちょうど一つという条件であり、スライスの表現可能関手 \((L/X)(a,-)\) は極限を保つ。空極限も含む。

スライスは局所可呈示なので、WVP により \(E_X\) は反射的である。スライスの始対象を反射し、\(E_X\) の始対象 \(e:B\to X\) を取る。\(s:U\to V\) を \(S\) の射、\(g:B\to V\) を任意とする。引き戻し \(t:B\times_VU\to B\) はすべての \(D\in\mathcal D\) から見ると全単射を誘導する。よって \(et\in E_X\)。始対象性から \(e\to et\) が一意にあり、\(t\) との合成は \(e\) の自己射なので恒等である。これは \(g\) の \(s\) に沿う持ち上げを与え、他の持ち上げも \(e\to et\) を与えるので一致する。従って \(B\in\mathcal D\)。\(e\in E_X\) より \(e\) は \(X\) の余反射射である。双対に戻せば求める反射となる。この議論は任意の局所可呈示圏 \(L\) に通用する。

## 2. VP の失敗から得る極限閉部分圏

Rosický–Trnková の Remarks 2–3 により、\(\neg\mathrm{VP}\) の下で、互いに異なる空間間には定数射しかなく、各自己射は恒等射か定数射であるコンパクト Hausdorff 空間の真クラス \(\mathcal M\) がある（stiff proper class）。一点以下の空間と離散二点空間は除いてよい。残る各 \(M\) は連結である。実際、非自明な開閉分割を持ち三点以上あれば、各片から一点ずつ選んで非定数かつ非恒等の自己射が作れる。離散二点でも入れ替えが可能である。[Rosický–Trnková, *Representability of concrete categories by non-constant morphisms*, Remarks 2–3](https://dml.cz/bitstream/handle/10338.dmlcz/107347/ArchMath_025-1989-1_16.pdf)

\(\mathcal C\) を空空間と \(\mathcal M\) の元の任意の集合添字積からなる同型閉な充満部分圏とする。\(h:\prod_i M_i\to N\)（\(N\in\mathcal M\)）は定数または \(M_i=N\) の座標射に限られる。\(M_i\ne N\) の変数の切片は定数である。\(M_i=N\) では異なる \(a,b\in N\) における切片の値の対は \(\Delta_N\cup\{(a,b)\}\) に入り、他の変数の積の連結性から、この座標の切片は一斉に定数か一斉に恒等である。全座標の切片が定数なら有限座標だけを変えた点の稠密性から \(h\) は定数である。

従って積の間の等化子は、同じ型の座標同士の等式と、座標や定数の値を指定する等式で切り出される。矛盾すれば空で、両立すれば自由な座標の同値類の積に同相である。積閉性と合わせて \(\mathcal C\) は小極限閉である。一方、離散二点空間 \(D\) は弱反射さえ持たない。任意の候補 \(r:D\to\prod_i M_i\) に対し、その集合個の因子に登場しない \(N\in\mathcal M\) を選ぶ。非定数射 \(D\to N\) は \(r\) を経由できない。従って \(\mathcal C\) は反射的でない。

§1 と合わせて

\[
\mathrm{VP}\Rightarrow P,\qquad
\mathrm{WVP}\land\neg\mathrm{VP}\Rightarrow\neg P.
\]

特に **WVP 上では \(P\) と VP が同値**になる。また、WVP の仮定なしでも「CompHaus の極限閉充満部分圏がすべて反射的」は VP と同値である。\(D\) は弱反射の不存在の証人であり、\(D\) 自身が \(\mathcal C\) の直交閉包に入るかはこの証明には不要である。WVP の下では \(D\) の直交閉包への反射先がその閉包と \(\mathcal C\) の差に入る。

## 3. 候補の基数仮定を同時に満たすモデル

外の宇宙に extendible 基数が存在すると仮定し、最小のものを \(\kappa\) とする。

- \(\kappa\) は supercompact、従って Woodin である。Woodin 性のランク版と Wilson の「Ord is Woodin」と WVP の同値から \(V_\kappa\) で WVP が成り立つ。さらに Bagaria–Wilson の boldface の階層定理により、そこには任意に大きな \(\Pi_2\)-strong 基数が存在する。[Wilson, Theorem 1.6](https://arxiv.org/abs/1907.00284)・[Bagaria–Wilson, Theorem 5.13](https://doi.org/10.1017/jsl.2022.42)
- \(\kappa\) は \(\Sigma_3\)-correct である。任意の \(\alpha<\kappa\) について外の宇宙で「\(\alpha\) より大きい supercompact 基数がある」は \(\kappa\) 自身を証人に真であり、これは \(\Sigma_3\) なので \(V_\kappa\) に反映する。従って内部には任意に大きな supercompact、特に strongly compact および almost strongly compact 基数がある。[Bagaria ほか, Proposition 6.2, Lemma 6.3](https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content)・[Tsaprounis, supercompact 性の定義複雑性](https://myria.math.aegean.gr/~ktsap/cnext.pdf)
- \(\gamma<\kappa\) が extendible かどうかも内外で一致する。実際 \(C^{(1)}\)-extendible と extendible は同値で、前者は \(\Pi_3\) である。\(\kappa\) の最小性から内部には extendible 基数がなく、従って VP は失敗する。[Bagaria ほか, Proposition 6.2, Corollary 6.9](https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content)・[Bagaria–Goldberg, 定義複雑性](https://math.berkeley.edu/~goldberg/Papers/ReflectingMeasures.pdf)

この同一モデルで §2 により \(P\) が失敗する。従ってこれらの仮定の単独使用・同時使用から一般の \(P\) を導くことはできない、という相対的な非含意を得る。また CompHaus と Top の間の反射により、このモデルの \(\mathcal C\) は Top の No.8(b) に対しても反例となる。[母圏を移す証明](README.md)

同じ議論は固定した複雑さを超える。外で VP と一つのパラメータなしの一階文 \(\varphi\) が真だとする。\(m\ge1\) を \(\Sigma_{m+2}\)-correctness が \(\varphi\) の真偽を保存するほど大きく取り、最小の \(C^{(m)}\)-extendible 基数を \(\lambda\) とする。\(V_\lambda\) で \(\varphi\) が真である一方、各 \(\gamma<\lambda\) で「\(\gamma\) は \(C^{(m)}\)-extendible」は \(\Pi_{m+2}\) なので内外で一致する。従って内部で VP は偽である。\(\lambda\) は extendible、従って Woodin なので WVP は真であり、\(P\) は偽となる。この観察は有限個の一階仮定を連言にした場合にも適用できる。無限の公理スキーマやクラスパラメータを含む仮定は別途検討が必要である。[Bagaria ほか, Lemma 6.3, Corollary 6.9](https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content)・[Bagaria–Goldberg](https://math.berkeley.edu/~goldberg/Papers/ReflectingMeasures.pdf)

## 4. 正の結果を与える定義可能性の条件

双対代数の固定した構造表示で \(\mathcal C^{\mathrm{op}}\) を集合パラメータ付き \(\Sigma_n\) で定義できるとする。Bagaria–Casacuberta–Mathias–Rosický の定理 7.5 により、下表の仮定で内部の集合個の対象からの図式の余極限として各対象を、母圏内でも表せる。双対に戻すと \(\mathcal C\) 内の集合個の余域への写像が各対象の点を分離する。従って前稿 §3 の反射の構成が適用できる。[定理 7.5](https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content)・[反射の構成](comphaus_positive_attempt.md)

| 双対表示での対象クラスの定義 | 十分な仮定 |
|---|---|
| \(\Sigma_1\) | ZFC |
| \(\Sigma_2\) | 任意に大きな supercompact 基数 |
| \(\Sigma_{n+2}\), \(n\ge1\) を固定 | 任意に大きな \(C^{(n)}\)-extendible 基数 |

さらに、各外部対象 \(X\notin\mathcal C\) ごとに、\(\mathcal C\) を含み \(X\) を含まない上表の極限閉部分圏が一つあれば、\(\mathcal C\) はそれらの交わりとして直交類になる。この局所的な十分条件は \(\mathcal C\) 自身の定義の複雑さを制限しない。\(P\) 単独から VP が従う方向は後続の再点検で扱った。
