# No.8(b)　余有限位相の部分空間による T₁ の場合の還元

2026年11月19日。無限基数 \(\kappa\) の集合に余有限位相を入れた空間を \(F_\kappa\) とする。次のクラスを考える。

\[
\mathcal D_\kappa=\{Z\in\mathrm{Top}_1:\text{すべての連続写像 } F_\kappa\to Z\text{ は定数}\}.
\]

空の余域もこの条件を満たす。\(S\) を Sierpiński 空間とすれば、Top の中で \(\mathcal D_\kappa=\{S\to 1,F_\kappa\to 1\}^{\perp}\) である。

**還元。** Top の小極限で閉じる充満・同型閉部分圏 \(\mathcal C\subsetneq\mathrm{Top}_1\) に対し、ある非可算基数 \(\kappa\) があって \(\mathcal C\subseteq\mathcal D_\kappa\) となる。従って \(\mathcal C\) の全テストを通る外部の対象 \(X\) も同じ \(\mathcal D_\kappa\) に属する。\(\kappa\) は \(\mathcal C\) に依存する。

**写像と部分空間。** T₁ 空間 \(Z\) への非定数連続写像 \(f:F_\kappa\to Z\) は各ファイバーが有限である。各一点の逆像が真の閉集合だからである。したがって像の濃度は \(\kappa\) である。像の部分空間位相は T₁ 性により余有限位相を含み、また像の空でない開集合の逆像は余有限だから、像でもその補集合は有限である。よって像は \(F_\kappa\) と同相である。逆にそのような部分空間があれば包含射が非定数写像になる。従って \(\mathcal D_\kappa\) の条件は \(F_\kappa\) 型の部分空間を含まないことと同値である。

**還元の証明。** 対偶を示す。\(\mathcal C\) の対象の中に、任意に大きな濃度の余有限位相の部分空間が現れるとする。

1. \(\mathcal C\) は任意の部分空間に閉じる。実際、\(Y\in\mathcal C\) と \(A\subseteq Y\) を取り、別の \(C\in\mathcal C\) に含まれる十分大きい余有限部分空間 \(F\) を選ぶ。二つの単射 \(p,q:Y\to F\) を、\(A\) 上でちょうど一致するように取る。\(Y\) は T₁ なので、有限集合の逆像は有限閉集合となり、両単射とも連続である。\(F\hookrightarrow C\) と合成した二射の等化子が、もとの部分空間位相を入れた \(A\) である。
2. 任意の T₁ 空間 \(Z\) が \(\mathcal C\) に入る。まず 1 により、任意に大きい余有限空間自体が \(\mathcal C\) の対象になる。\(|Z|\) に対して十分大きいもの \(F\) を一つ固定する。各閉集合 \(B\subseteq Z\) について、\(B\) を一点 \(b\in F\) に送り、その外を \(F\setminus\{b\}\) に単射で送る写像 \(h_B\) を取る。各ファイバーは閉なので \(h_B\) は連続で、\(h_B^{-1}(\{b\})=B\) である。特に \(B=\varnothing\) の座標は単射である。全 \(h_B\) の対角写像は点を分け、すべての閉集合を閉集合の逆像として復元するので埋め込みである。こうして \(Z\) は \(F\) の冪の部分空間になり、積閉性と 1 を適用できる。

以上から \(\mathcal C=\mathrm{Top}_1\) となる。余有限部分空間の濃度に上界がある場合には、その上界を超える非可算 \(\kappa\) を取れば主張を得る。2 の余有限空間による生成は既知である。ここでは 1 の等化子によって部分空間閉性を導き、No.8(b) に適用した。[Hernández-Arzusa–Hernández, *Reflections in topological algebraic structures*, 余有限空間による生成の記述](https://repositori.uji.es/bitstreams/8c35c862-c351-487a-b17a-79df35eb137d/download)

**Hausdorff 性との差。** 非可算 \(\kappa\) について \(\mathrm{Haus}\subsetneq\mathcal D_\kappa\subsetneq\mathrm{Top}_1\) である。Hausdorff 空間は無限余有限空間を部分空間に持たない。可算無限余有限空間 \(F_{\aleph_0}\) は濃度から \(\mathcal D_\kappa\) に入り、Hausdorff ではない。\(F_\kappa\) 自身は \(\mathcal D_\kappa\) の外にある。

\(T_0\) から \(T_1\) への還元で効いた小さい部分空間の抽出にも限界がある。任意の無限基数 \(\lambda\) に対し、濃度 \(\lambda^+\) の集合に、空集合と「補集合の濃度が \(\lambda\) 以下の集合」を開集合とする位相を入れる。この空間は T₁ で非空開集合のどの二つも交わるが、濃度 \(\lambda\) 以下の部分空間はすべて離散である。従って非 Hausdorff 性を取り出す部分空間の濃度に一律の上限はない。この事実も上の還元も、Hausdorff 空間への一般的な還元の可否を決めるものではない。
