# No.2　双対圏の直交類は二つの反射的部分圏の交わりか

この README は 2026-11-20 に Claude (Opus 5.5) が書いた。内容は、このフォルダの研究ノートと、それに対する AI による検証の要約である。人間による検証はまだ行っていない。

## 問題

Adámek–Rosický, *Locally Presentable and Accessible Categories*, Open Problems, p.295, Problem 2：局所可呈示圏の双対圏における各直交類（テストの射は真クラスでもよい）は、(a) 反射的か、(b) 二つの full reflective subcategory の交わりか。[原問題 p.295](https://doi.org/10.1017/CBO9780511600579.011)

ノートは双対を取って、局所可呈示圏 \(\mathcal K\) の余直交類（coorthogonality class）が、二つの full coreflective subcategory の交わりになるかを問う形で扱う。主に (b) を扱う。

## 部分圏は replete（同型で閉じる）と読む

**この問題は、部分圏が同型で閉じている（replete）と読む必要がある。** 原著は replete を明示していないが、そう読まないと (b) は自明に肯定される。

理由は次のとおりである。余直交類 \(\mathcal A\) は同型で閉じている。\(\mathcal A\) と交わらない各同型類から、相異なる二つの対象 \(r_1,r_2\) を選ぶ。同型類は真クラスなので、これは常にできる。\(r_1\) を全部 \(\mathcal A\) に加えた充満部分圏を \(\mathcal C_1\)、\(r_2\) を全部加えたものを \(\mathcal C_2\) とする。

- \(\mathcal C_1\cap\mathcal C_2=\mathcal A\) である。
- 各 \(\mathcal C_i\) は \(\mathcal K\) の全ての同型類と交わるので、\(\mathcal K\) と圏同値になる。各対象の同型射を余反射に使えるので、coreflective である。

以下の主張は、どれも「full かつ replete な coreflective subcategory」についてのものである。主定理の記述（[直接証明](no2_direct_presheaf_kernel_proof_2026-11-17.md) の 46 行目付近）には replete が書かれている。一方、結論文（9 行目付近）と原著との対応（457 行目付近）では省略されているので、この読み方で読むこと。

## ノートの主張（未検証）

- **否定側。** 非可算可測基数が存在しなければ、(b) の反例がある。
  - 母圏 \(K_{\mathrm{fs}}\) は、\(M=\mathrm{End}(\omega)\) 作用を持つ集合の平行二射で、第 0 成分が有限台のものからなる。これは前層圏として表示できる。
  - 一つの正則エピ \(\sigma\) について \(\mathcal A={}^{\perp}\{\sigma\}\) と置く。\(\mathcal A\) を含む full replete coreflective subcategory は、どれも \(\mathcal A\) に属さない対象 \(B\) を含む。
  - 従って \(\mathcal A\) は、そのような部分圏の、いかなる族の交わりにもならない。
  - さらに、基数 \(\rho\) を使う版により、「(b) が肯定的なら、可測基数が真クラス個存在する」ことも主張されている。
- **肯定側。** WVP の下では、任意の余直交類（テストは真クラスでもよい）が coreflective になる。従って (a) も (b) も肯定される。
- **ノートが主張しないこと。** P2 ⇒ WVP、VP との同値性、正確な無矛盾性の強さはいずれも主張していない。

## 主なファイル

- [no2_direct_presheaf_kernel_proof_2026-11-17.md](no2_direct_presheaf_kernel_proof_2026-11-17.md)：無可測基数の下での反例の直接証明。
- [no2_presheaf_presentation_Kfs_2026-11-17.md](no2_presheaf_presentation_Kfs_2026-11-17.md)：\(K_{\mathrm{fs}}\) の前層表示。末尾の追記は、それより前の群の増大に関するノートを置き換えている。
- [p1_p2_measurable_wvp_almost_compact_2026-11-17.md](p1_p2_measurable_wvp_almost_compact_2026-11-17.md)：WVP による肯定と、可測基数の真クラスへの強化。No.1 と No.2 の両方を扱う。
- [sigma_coreflectivity_under_no_measurables_2026-11-16.md](sigma_coreflectivity_under_no_measurables_2026-11-16.md)：より前の試行。「反例にならない」という記述は別の母圏 \(D\) でのものなので、上の結論と矛盾しない。
- `p1_*.md`：主に No.1 についてのノート。

## AI による検証の結果（2026-11-20）

否定側（\(K_{\mathrm{fs}}\) の前層表示、\(\sigma\) が正則エピであること、補題 A・B、可測基数の真クラスへの強化）と、WVP による肯定側を、別の AI セッションが導き直した。誤りと重大な穴は見つからなかった。指摘は次の二点である。

- 上記の replete の読み方を明記すること。
- \(\rho\) 版の書き下しが p1_p2 ノート §1.3 では概略にとどまっていること。

人間による検証と新規性の確認は未実施である。
