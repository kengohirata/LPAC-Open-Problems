# No.3：density 還元の疑義に関する依存関係・影響範囲の監査

2026-11-17。

**状態：TARGETED_DEPENDENCY_AUDIT / PROOF_RECONSTRUCTED。**
本稿は、前稿の ordinal-rank 圏と canonical-colimit 計算を入力として、問題のある還元が原著・後続文献・No.1〜3 の研究ノートにどう波及するかを調べたもの。独立査読、著者確認、形式検証、原著全体の再検証は実施していない。候補の公刊済み反例としての確定や、新規性を主張しない。

**結論：『他には影響しない』とは言えない。** 原著 P3 の二つの formulation の同値性、literal formulation に対する VP コメント、2018年論文の導入の同じコメント、および私たちの旧 No.3 ノートの無条件の適用範囲には影響する。一方、実際に presentability・small dense subcategory・明示的な presheaf 表示を仮定または独立に構成している証明には、この誤りを経由しない論証がある。2022年論文の著者公開版 Theorem 2.26 には、別途補足が必要な density の引用箇所を見つけた。これは同定理の反例ではない。

## 1. 三つの前提を分離する

(Lit) C は locally small、cocomplete、集合 G が generated objects からなる strong generator。

(Bnd) C は small dense subcategory を持つ（bounded）。

(Refl) 小圏 D に対する full reflection L:Set^(D^op) ⇄ C:E が与えられ、E はある λ について directed mono-colimits を保存する。

前稿が疑義を与えるのは (Lit)⇒(Bnd)、従って原著 p.296 の (Lit)⇒(Refl)。

今回の扱い：

- (Refl)⇒(Lit) は残る。反射された representables L(y d) の Hom は E の評価関手なので、union 保存から generatedness、full faithfulness から strong generation が従う。
- C が cocomplete で (Bnd) なら full reflective presheaf presentation を構成できる。この段階は generatedness を使わない。
- C が locally presentable なら (Bnd) が得られ、しかも sufficiently filtered colimits を保存する full reflective presentation が得られる。この段階は true presentability を使う。
- (Lit) と (Refl) を今後は同義として使わない。ordinal-rank 候補は literal formulation に対するものであり、reflective formulation の反例ではない。

## 2. 原著で直接影響を受ける部分

### 2.1 Problem 3, pp.295–296

p.296 は generated strong generator の λ-small-colimit closure が dense と述べる。前稿では、finite rank・finite carrier の閉包 A と K=X_(ω+1) について、canonical diagram A↓K の比較射を直接計算し、nonmonic と示した。

p.295 の VP 肯定コメントは、この boundedness を得たうえで Corollary 6.8 を適用する形。したがって、前提を得る還元が破れるなら、その『literal P3 に対する適用』を維持できない。Corollary 6.8 の本来の仮定付き定理や VP 自体を反証したことにはならない。

### 2.2 Theorem 1.11 とその適用を区別する

取得した原著 p.18 の証明は、canonical filtered colimit への generator からの二射を、finite presentability によって一段階へ因子化する。presentable 版の仮定は今回の候補にはない。

従って、Theorem 1.11 自体は今回の反例計算の対象ではない。問題は generated 版への類推である。『原著の基礎的な LP の特徴付けが崩れた』とは結論しない。

Propositions 1.16、1.22、1.26、1.27、Corollary 6.8 の原著の全証明本文は、今回取得できた範囲外を含む。その全ページを行単位で監査したとはしない。以下では、研究に必要な内容を問題の還元を使わずに再証明して、依存を切り離す。

## 3. 独立に維持できる二つの presheaf 表示

### 3.1 Small dense subcategory が既にある場合

D⊂C を small full dense、C を cocomplete とする。

    N(X)=C(-,X)|D,
    F(P)=colim_{(d,x)∈el(P)} d.

colimit の普遍性により

    C(FP,X)≅Nat(P,NX).

従って F⊣N。dense という仮定により N は fully faithful なので、これは full reflection。

ここには、strong generator から density を推論する段階は一切ない。density を与えられた前提として使うことと、それを generatedness から導くことを区別する。

### 3.2 Locally presentable category の場合

C が locally λ-presentable とする。λ-presentable objects の small full skeleton D を取り、N(X)=C(-,X)|D とする。

任意の X の λ-filtered presentation X=colim_i D_i を選ぶ。自然変換 τ:NX→NY は各 canonical injection d_i:D_i→X を射 τ_(D_i)(d_i):D_i→Y に送り、自然性によって cocone を与える。これから一意な f:X→Y を得る。

任意の D∈D と a:D→X は、λ-presentability により一段階 d_i を経由する。その因子化と τ の自然性から f a=τ_D(a)。よって Nf=τ。canonical injections の jointly epimorphicity により一意性も成立する。

従って N は fully faithful。3.1 の coend/element-category colimit による左随伴を持ち、全ての λ-filtered colimits を pointwise に保存する。

この証明は (Lit)⇒(Bnd) を使わない。No.1/No.2 の『任意の LP 圏から presheaf 圏へ移す』部分は、この valid な表示を使っている。

## 4. Quotient-smallness を明示的に持つ generated 版は別である

2022年の Di Liberti–Rosický の Definition 2.3 の λ-convenience には E-cowellpoweredness と M-unions の安定性が含まれる。Theorem 2.24 はこれを仮定し、生成族を λ-small colimits だけでなく E-quotients でも閉じる。

Mono/strong-epi の場合、この追加仮定がなぜ gap を防ぐかを直接説明できる。以下では strong epi–mono factorization、strong-epi cowellpoweredness、λ-directed subobject unions の比較射まで mono であることを明示的に仮定する。

G の <λ 個の余積とその strong quotients を代表する集合 A を取る。任意の X へのこれらの射の images I↪X は再び A に属する。これらの subobjects は λ-directed である。<λ 個の images の上界は、対応する始域の余積から X への image とすればよい。

その union U→X は mono。G の全射が経由するので strong generation から同型。ゆえに X は A-objects の、実際に monic transitions を持つ λ-directed colimit である。

A の対象は generatedness を保つ。この actual mono presentation に対して、3.2 と同様の natural-transformation argument を行えば density が出る。この場合は generatedness を適用してよい図式である。

ordinal-rank 候補では H の強商 X_α が真クラス個あるので、この小さい A を作る前提を満たさない。これは『cowellpoweredness を含む標準定理』を反駁しない理由である。

2018年の Nearly Locally Presentable Categories, Corollary 3.4 も、weak cowellpoweredness により強商閉包を小さく保ち、regular factorization によって canonical diagram を images の cofinal subdiagram に置き換える。小余極限閉包だけから density を主張する proof とは異なる。

## 5. VP に関する影響を切り分ける

### 5.1 今回維持できない適用

    VP + (Lit) ⇒ LP

を、原著の boundedness comment だけで採用しない。候補の直接証明が正しければ literal statement は ZFC で偽であり、この適用には修正が必要。

### 5.2 明示的な full reflective presentation の側は別

P が小さい presheaf category で K⊂P が full reflective なら、K はすべての反射単位、または L-equivalences のクラスへの右直交クラスである。

VP の通常のクラス／定義可能性規約のもとでは、このクラスは既存の accessible category Arr(P) の充満部分圏として扱える。BCMR (2015), Theorems 7.5, 8.4 の経路は、構造反射からこのクラスの small dense subcategory D を取り、arrow colimits に対する orthogonality の保存によって、同じ local objects を集合 D の右直交クラスとして表示するもの。

従って VP のもとで full reflective subcategory of a presheaf category は small-orthogonality class、ゆえに LP となる。この経路は (Lit)⇒(Bnd) を使わない。

BCMR の dense-subcategory argument は ambient accessible category の presentable objects と structural-reflection theorem を使う。任意の抽象的な generated category に同じ定理を適用してはいけない。

### 5.3 重要な違い

候補の U:C→Set は faithful/conservative だが full ではない。候補の対象を単に集合として符号化しただけで、C が既存の構造の圏に full に入ったことにはならない。小さい presheaf 圏の full reflective subcategory でもない。このため、構造のクラスに関する VP の定理が今回の候補を直接排除するわけではない。

## 6. 後続論文の具体的な影響

### 6.1 Positselski–Rosický (2018)

導入 p.254 の『VP の下では weak cowellpoweredness を除去できる』という P3 へのコメントは、今回疑義のある主張の再掲として扱う。その記述を独立の肯定証明と数えない。

一方、Definition 3.1 は weak cowellpoweredness を定義に含む。Corollary 3.4、Theorem 3.6 の該当経路、反射表示を扱う Theorem 4.8 は quotient closure と追加の regular-factorization 仮定を使う。この依存経路に、問題の bare generated⇒dense の推論を見つけてはいない。

『導入のコメントに影響する』と『この論文の全定理が偽』は全く別である。本稿は後者を主張しない。

### 6.2 Di Liberti–Rosický (2022)：守られる部分

Definition 2.5 の M-locally generated は、集合個の生成対象からの actual M-directed-colimit presentation を含む。Remark 2.6 の density はこの presentation から得られる。Theorem 2.18 の convenience と Theorem 2.24 の E-quotient closure を外してはならない。

これらの明示的な仮定を保つ限り、今回の candidate は仮定を満たさず反例にならない。特に2.24に必要な density の経路は§4で別に確認した。

### 6.3 同じ著者公開版の Theorem 2.26：別途補足が必要な箇所

確認できた arXiv:2009.10980v2（2022-03-02）、印刷 p.9 の証明では、free functor が強生成族 G を Alg(T) に与えることの後で、G の λ-small-colimit closure A の density を Remark 2.14 により主張している。

しかし、印刷 p.6 の Remark 2.14 が補足しているのは、λ-generated objects が λ-small colimits で閉じるという Lemma 2.13 の第一の主張の適用範囲である。density の主張ではない。

したがって、少なくともこの引用だけでは density の段階を正当化できない。同じ general generated⇒dense inference なら、今回の問題に触れる。Alg(T) の monadicity、T の M 保存・M-directed-colimit 保存から独立に補える可能性があるため、**Theorem 2.26 自体の反例や偽性は主張しない**。今回その補足証明は完成していない。

出版版は TAC 38 (2022), 661–683、2022-03-31 公刊であることを公式abstractで確認。出版版PDFは取得エラーとなり、今回 p.9 の本文・画像で確認したのは arXiv v2。出版版で同じ箇所が修正されていないと断定しない。

### 6.4 Remark 2.27：二重の条件確認が必要

同じ公開版は、reflective/union-closed formulation と P3 の関連を述べる。literal P3 との同値性はそのまま使わない。

さらに、反射 L:P→K と包含 E:K→P におけるモナドは ambient 上では EL。E が local mono-directed colimits を保存することは、EL が任意の ambient mono-directed colimitsを保存することを自動的には意味しない。L が mono を保存する保証がないため、Theorem 2.26 の T に関する保存仮定を適用前に別途確認する必要がある。記号の順序の問題と、この実質的な保存性の問題を混同しない。

### 6.5 未監査の範囲

2022年論文の全 enriched duality・Banach 空間への応用、その他の引用論文全体の dependency graph は今回全面監査していない。2.26の未補足箇所を、それら全部への反例へ拡大しない。逆に、全て無影響と保証することもしない。

## 7. No.1・No.2 の研究ノートへの影響

ここでいう『依存しない』は今回の gap に限った依存確認であり、全ての新規証明を独立に認証したことではない。

### 7.1 Presheaf reduction

No.1/audits/basic_reductions.md と set_theoretic_upper_bound.md の移送補題は、full reflection が既にある場合の随伴の直接計算。任意の LP 圏への適用には§3.2の valid な表示が使える。P3コメントを使っていない。

### 7.2 明示的な K_fs

No.2/no2_presheaf_presentation_Kfs_2026-11-17.md の P_n,Q は、Hom が全小余極限を保存する small projectives である。単なる generated objects ではない。

その nerve N は全小余極限を保存し、同型を反映する。coend による左随伴 F について NF は representables 上で恒等、両関手は colimits を保存するので全 presheaves 上で NF≅Id。三角恒等式と N の conservativity から counit FN→Id も同型。これが presheaf 圏との同値の直接証明であり、generated⇒dense は使わない。

### 7.3 巨大基数と非 coreflectivity

実際に確認した以下のノートは、既存の具体的 presheaf 圏、または真に LP な母圏から出発している。

- No.2/no2_direct_presheaf_kernel_proof_2026-11-17.md：Isbell 評価、pushout、座標核、順序数の切れ目による否定。
- No.2/p1_p2_measurable_wvp_almost_compact_2026-11-17.md：N_rho の否定例、WVP の presheaf-slice tower、ASC の pure-injectivity と実際の小対象の colimit presentation。
- No.2/p1_restricted_product_reflection_pi2_strong_2026-11-17.md：Π₂ の E_B⊂P/B と Product Reflection、初対象構成。
- No.1/audits/set_theoretic_upper_bound.md：既存の LP 構造圏内の定義可能クラスと BCMR。

従って、これらに対して今回の P3 density gap を理由とする結論の撤回は行わない。各ノートの従前の PROOF_RECONSTRUCTED / 独立監査前という状態も変更しない。

No.1/2 の VP 肯定側も、LP 母圏の colimit-closed full subcategory に対する coreflection の経路を使う。literal P3 を仮定していない。

## 8. No.3 の旧成果への正確な修正

以下の表は依存の修正であり、各ファイルの全行を今回再査読したという意味ではない。

| 対象 | 今後の扱い |
|---|---|
| 元の仮定から full reflective presheaf 表示を得る段階 | 無条件の入力として使用停止 |
| その表示から得た complete / well-powered / strong epi–mono factorization | 表示が明示的にある場合の結果として保持。literal仮定だけから得たとはしない |
| c_B(A) の一段階 coequalizer、標的ごとの反復停止 | full reflection を独立仮定にして保持 |
| RP・CS・pure hull・reduced powers の同値／十分条件 | 記載の反射表示・union保存を前提とする結果へ限定 |
| Σ1/Σ2 の small-local-subobject の条件付き証明 | full embedding と定義可能性を独立に仮定すれば別の経路。候補のfaithful Uには適用しない |
| 集合理論の全モデル・全準同型による表示からの強商上界 | explicit full model presentation を使う独立の十分条件 |
| quasi-small (S∪Q)^⊥ による肯定・一様停止 | explicit presentation を持つ場合の結果。literal仮定からその表示を得たとはしない |
| K_Gamma の具体例、Stone候補の失敗、copower障害 | 各明示的定義のもとでの直接結果。今回の還元への依存はない |
| ordinal-rank候補およびcanonical density反例計算 | 引き続き独立確認前の直接証明として扱う。反射表示を使わない |

### 8.1 個別停止は特に注意

旧 c_B-iteration の停止は、固定した SET EB の部分前層が増大することを数えている。

ordinal-rank 候補では q_infty:H→T の kernel-pair tower は X_α（全集合順序数α）を通り、どの集合段階でも T に達しない、という計算になる。従って、この候補の証明が正しければ、『各strong epiが集合長で停止する』という結論を literal assumptions にまで拡張することは実際に誤りとなる。

これは old reflected-case theorem の矛盾ではなく、適用前提を削れない具体例である。

## 9. 監査から導ける結論と導けない結論

導けること：

1. 問題の還元を必要とする箇所は、他の証明から切り離して記録できる。
2. 通常の LP 理論の density/presheaf presentation は、presentability を本当に使う独立証明で維持できる。
3. quotient-smallness/convenience を前提にする generated 版にも、この gap を回避する正当な証明経路がある。
4. No.1/2 の確認した主要経路に、この還元を必要とする依存は見つからない。
5. P3コメントの再掲と、2022年著者公開版の特定の density ステップは、追加確認対象として残る。

導けないこと：

- 原著・後続論文の全定理が正しいという保証。
- 2022年 Theorem2.26 自体が偽だという結論。
- ordinal-rank候補の独立査読済みという主張。
- No.1/2の全ての数学的正しさの新しい認証。
- reflective formulation が ZFC で否定されたという結論。

原著の問題文に対する候補と、後続論文の special hypotheses の問題を区別することが必要である。

## 10. 今回確認した一次資料と取得範囲

[A] Adámek–Rosický, Open Problems pp.295–297：ユーザーの open-problems.pdf を Files で再読。p295 P1のVPコメントとP3、p296 density/reflectionの文を確認。

[B] 原著出版社配信preview：Definition0.6、Theorem1.11 p18。本文と該当ページ画像を確認。原著の全章は取得していない。
https://api.pageplace.de/preview/DT0400.9780511892615_A24404888/preview-9780511892615_A24404888.pdf

[C] 著者公開 List of Corrections, March 2026：全文の記載とp1画像を確認。p18のsmallness訂正が今回のgenerated/presentableの差を直していないこと、P3への該当訂正が見当たらないことを確認。これは訂正の不存在・新規性の証明ではない。
https://math.fel.cvut.cz/en/people/adamekj/corrections.pdf

[D] Positselski–Rosický, Nearly Locally Presentable Categories, TAC33 (2018), 253–264：導入pp253–254、Definition3.1、Corollary3.4 p258（画像含む）、Theorems3.6,4.8の該当経路。
https://tac.mta.ca/tac/volumes/33/10/33-10.pdf

[E] Di Liberti–Rosický, Enriched Locally Generated Categories, arXiv:2009.10980v2：Definitions2.3,2.5、Remarks2.6,2.14、Theorems2.18,2.24,2.26、Remark2.27。PDF印刷pp3,5,6,9の画像も確認。
https://arxiv.org/pdf/2009.10980
公式出版情報（出版版PDF本文取得は今回失敗）：
https://tac.mta.ca/tac/volumes/38/17/38-17abs.html

[F] Bagaria–Casacuberta–Mathias–Rosický, Definable orthogonality classes in accessible categories are small, JEMS17 (2015), 549–589：Theorems7.5,8.4,8.7,8.8。印刷pp572,578などの画像を確認。ambient accessible structured categoryを使う点を照合。
https://diposit.ub.edu/server/api/core/bitstreams/40988e87-0578-4eb0-9dfd-ef845221b659/content

[G] Börger–Tholen, Total Categories and Solid Functors, CJM42 (1990), 213–229：Example4.3（p223の画像含む）および近傍。strong generationとcolimit-densityを区別する関連先行例として比較。P3解決の独立証明としては使用しない。
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A842E456CD7FFF30360076B3FB3134D4/S0008414X00003540a.pdf/total-categories-and-solid-functors.pdf
