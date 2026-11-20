# No.8　位相空間の入射性類と直交類

2026年11月19日。Adámek–Rosický の No.8 は位相空間と連続写像の圏 Top について二つの問いを挙げる。以下では便宜上 (a), (b) と呼ぶ。部分圏は充満で同型について閉じ、積・余極限・極限は Top で取る。[原著 *Locally Presentable and Accessible Categories*, Open Problems, p.296](https://doi.org/10.1017/CBO9780511600579.011)

| 問い | 初期調査の結果 |
|---|---|
| (a) 小積と有向余極限で閉じる部分圏は入射性類か | ZFC で否定。連結空間全体が反例になる。 |
| (b) 小極限で閉じる部分圏は直交類か | Hausdorff 空間の剛直な族から、ZFC で否定する証明案を得た。独立検証前。[Top 版の反例構成](top_stiff_circles.md)・[非 T₁ の場合の肯定](positive_attempt.md)・[CompHaus に制限した場合の集合論的な上下界](comphaus_vopenka_bounds.md) |

再点検では、片がコンパクトなら反例構成の輪もコンパクトであることを確認した。これを使うと CompHaus 版の否定には ¬VP だけで足り、CompHaus 版の肯定は VP と同値になる。真クラスからの一括選択を避ける構成も記した。[両証明の再点検と CompHaus 版の同値](proof_check_top_comphaus.md)

さらに (b) の反例候補では、ある基数 κ をその部分圏全体に共通に選び、全対象と外側の証人がともに濃度 κ の余有限空間を部分空間に持たないと仮定できる。[余有限部分空間の濃度による還元と Hausdorff 性との差](cofinite_subspaces.md)

### コンパクト生成 Hausdorff 空間に制限した場合

CGHaus を Hausdorff な \(k\)-空間の圏とする。Noble の系によれば、位相空間 \(Z\) のすべての小直積冪 \(Z^I\) が通常の積位相で \(k\)-空間になることと、\(Z\) がコンパクトであることは同値である。従って \(\mathcal C\subseteq\mathrm{CGHaus}\) が Top の小積で閉じていれば、すべての \(Z\in\mathcal C\) はコンパクト Hausdorff である。逆に CompHaus は Top の小極限で閉じる。ゆえに CGHaus に含まれる Top の極限閉部分圏を調べることは、CompHaus の極限閉部分圏を調べることと一致する。CGHaus の内部の積は通常の積の \(k\) 化であり、No.8(b) の仮定では通常の積そのものを使う。[Noble, *Products of uncountably many k-spaces*, p.609 の Corollary](https://doi.org/10.1090/S0002-9939-1972-0287503-0)

この場合は直交性も CompHaus 内部で判定できる。\(R:\mathrm{Top}\to\mathrm{CompHaus}\) をコンパクト Hausdorff 反射とする。コンパクト Hausdorff 空間 \(Z\) と Top の射 \(u\) について、随伴により \(Z\perp u\iff Z\perp Ru\) である。従って Top での表示があれば各テストに \(R\) を施して内部の表示にできる。逆に CompHaus の内部でテストのクラス \(H\) により表示されるなら、Top では \(H\) に全反射射 \(A\to RA\) を加えればよい。全反射射に直交することは CompHaus に属することと同値なので、外側の証人も CompHaus 内で探せる。これで CGHaus に限定した (b) と CompHaus 内部の (b) の同値を得る。一般の (b) をこの場合に帰着する議論は得ていない。

CompHaus 内部では Vopěnka 原理の下で肯定される（原著演習 6.e(1)）。ZFC でも、非定数の道を持つ対象が一つあれば部分圏は CompHaus 全体になり、零次元空間だけの場合も肯定される。内部の集合個の対象への射で点を分離できれば反射を構成できる。一般の場合の障害は延長の存在である。Cook 連続体を使うと、固定した埋め込みへの延長が失敗し、同じ例で積を取り直せば一意に延長できることを明示できる。[CompHaus での証明と延長が失敗する例](comphaus_positive_attempt.md)

射 \(u:A\to B\) について \(\mathrm{Top}(B,X)\to\mathrm{Top}(A,X)\) が全射なら \(X\) は \(u\) に関して入射的、全単射なら \(u\) に直交する。いずれの問いでも、テストとなる射は真クラス個でもよい。No.7 の母圏に課された局所可呈示性は Top には成り立たない。

## (a) 連結空間と離散二点空間

空空間を含む連結空間の充満部分圏を \(\mathcal C\) とする。連結空間の任意の積は連結で、空積も一点空間である。有向余極限 \(L\) から離散二点空間 \(D_2\) への連続写像を取る。\(L\) の任意の二点はある共通の段階から来る。その段階は連結なので二点の像は等しい。よって \(L\) も連結である。この議論は遷移射に単射性を要求しない。

Adámek–Herrlich–Strecker は、すべての連結空間を含む入射性類は Top 全体になると述べている。(a) には、次のように \(D_2\) が必ず入ることだけを確かめれば十分である。[*The Joy of Cats*, Remark 9.26](https://www.tac.mta.ca/tac/reprints/articles/17/tr17.pdf)

すべての連結空間が入射的になる射 \(u:A\to B\) を一本固定し、連続写像 \(f:A\to D_2\) を任意に取る。\(|B|\) より大きい無限基数 \(\kappa\) を選び、濃度 \(\kappa\) の集合 \(K\) に、空集合と「補集合の濃度が \(\kappa\) 未満の集合」を開集合とする位相を入れる。

1. \(K\) の非空開集合はどの二つも交わるので \(K\) は連結である。一方、濃度 \(\kappa\) 未満の部分空間 \(S\) はすべて離散である。実際、\(T\subseteq S\) に対して \(K\setminus(S\setminus T)\) は開で、\(S\) との交わりは \(T\) である。
2. 二点の埋め込み \(i:D_2\to K\) を選ぶ。\(K\) の入射性により、\(g u=i f\) となる連続写像 \(g:B\to K\) がある。
3. \(S=g[B]\cup i[D_2]\) は濃度 \(\kappa\) 未満で離散である。したがって \(ri=1_{D_2}\) となる連続写像 \(r:S\to D_2\) が取れる。\(g\) の余域を \(S\) に制限して \(r\) と合成すれば、\(f\) の \(B\) への延長を得る。

これで \(D_2\) は \(\mathcal C\) が満たすすべての入射性テストを通る。しかし \(D_2\) は非連結なので \(\mathcal C\) は入射性類ではない。基数 \(\kappa\) はテスト一本ごとに選んでよい。小さい部分空間が離散になる連結空間を使うこの証明は、Remark 9.26 についての公開の議論にもある。[Kevin Carlson ほかによる証明](https://math.stackexchange.com/questions/2924271/injectivity-class-of-connected-spaces-in-top)

## (b) 直交類を判定する条件

\(H_{\mathcal C}\) を「\(\mathcal C\) のすべての対象が直交する射」のクラスとする。\(H_{\mathcal C}^{\perp}\) は \(\mathcal C\) を含む最小の直交類である。従って反例に必要なのは、小極限で閉じる \(\mathcal C\) と \(X\in H_{\mathcal C}^{\perp}\setminus\mathcal C\) である。

Top では一本の射 \(u\) に対する \(\{u\}^{\perp}\) は反射的である。逆に任意の充満反射的部分圏はその反射射のクラスに対する直交類であり、直交類の任意の交わりはテストの合併に対する直交類である。ゆえに (b) は「小極限で閉じる \(\mathcal C\) の外の各 \(X\) を、\(\mathcal C\) を含むどれか一つの反射的部分圏の外に置けるか」とも書ける。Trnková–Adámek–Rosický の Top の例は二つの反射的部分圏の交わりが非反射的になる例で、この交わり自身は直交類である。[Sousa, *Reflective and Orthogonal Hulls*, §2, Example 2.3 直後](https://repositorio.ipv.pt/server/api/core/bitstreams/ebeaeb88-4854-4444-8070-ab761602f21d/content)・[Trnková–Adámek–Rosický, *Topological reflections revisited*](https://doi.org/10.1090/S0002-9939-1990-0987614-9)

### 非 T₀ 空間を含む場合は肯定

小極限で閉じる \(\mathcal C\) が非 T₀ 空間 \(Y\) を含むとする。\(Y\) の位相的に区別できない二点は密着二点空間 \(I_2\) をなす。この二点を固定し、ほかの点をその一方に送る写像 \(Y\to I_2\) は連続なので \(I_2\) は \(Y\) のレトラクトである。極限閉性は冪等射と恒等射の等化子を通じてレトラクト閉性を含むため、\(I_2\in\mathcal C\) である。

任意の \(Z\in\mathcal C\) と任意の部分集合 \(S\subseteq Z\) について、\(S\) は二つの連続写像 \(Z\rightrightarrows I_2\) の等化子にできる。一方を定数 1、他方を \(S\) の特性関数にすればよい。よって \(\mathcal C\) は任意の部分空間と小積で閉じる。

ここから各空間 \(X\) の反射を具体的に作れる。\(X\) から \(\mathcal C\) の対象への連続全射を、余域の同型を除いてすべて取り、その積への対角写像の像を \(R X\) とする。余域の濃度は \(|X|\) 以下なので、これらの全射を集合個で代表できる。部分空間閉性と積閉性から \(R X\in\mathcal C\) である。任意の \(X\to C\) はその像への全射と包含に分解し、その像も \(\mathcal C\) に属する。従って積の対応する射影から \(R X\to C\) が得られ、因子化の一意性は \(X\to R X\) の全射性に従う。これで \(\mathcal C\) は反射的、従って直交類である。

したがって (b) の反例が存在するなら \(\mathcal C\subseteq\mathrm{Top}_0\) である。さらに外側の証人 \(X\) も T₀ になる。実際、\(I_2\to 1\) に直交することは、位相的に区別できない任意の二点が一致すること、すなわち T₀ 性と同値である。この射は \(H_{\mathcal C}\) に入る。

後半の一般論を追うための文献に、Top 内の極限閉性・直交性・入射性・弱い反射性を比較した Herrlich の論文がある。今回はその書誌と要旨を確認した。上の T₀ への還元は直接の証明を記したもので、一般の場合についての既刊の解答の有無は引き続き調査を要する。[Herrlich, *Almost reflective subcategories of Top*](https://doi.org/10.1016/0166-8641(93)90115-T)
