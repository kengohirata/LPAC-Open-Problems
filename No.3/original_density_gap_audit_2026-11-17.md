# No.3：原著の density 還元の監査

2026-11-17。

**状態：DIRECT_DENSITY_COUNTERCALCULATION / PROOF_RECONSTRUCTED。独立査読・形式検証・著者確認・新規性確認は未実施。**

## 0. 結論の範囲

前稿 `ordinal_rank_candidate_and_boundedness_conflict_2026-11-17.md` の候補圏を再点検した。今回の監査では、余完備性、strong generation、finite generatedness の証明の破綻は見つかっていない。

さらに、生成対象の有限余極限閉包に関する canonical colimit を明示し、その比較射が **非 mono** であることを直接計算した。これにより、原著 p.296 の「generated strong generator の small-colimit closure が dense」という主張に対する、具体的な反例計算を得た。

類推元である Theorem 1.11 の証明本文（p.18）では、canonical filtered diagram への二射の因子化に **presentability** を使っている。generatedness では図式の遷移が mono である必要があるが、その仮定はなく、候補ではこの因子化が実際に失敗する。

**Theorem 1.11 自体の誤りを主張していない。** 問題はその presentable 版の証明を、p.296 で generated 版へ移す段階。

以下の計算が正しければ、literal Problem 3 は ZFC で否定され、p.295 の VP による肯定コメントにも修正が必要となる。ただし、これは公刊済みの訂正や外部合意のある結論ではなく、本稿の直接証明に基づく診断である。full reflective presheaf formulation の反例を得たとはしない。

## 1. 原著の取得・照合範囲

ユーザー提供の Open Problems pp.295–296 に加え、出版社配信プレビュー pp.1–18 を取得した。

- 原著 pp.1–2 は locally small な class categories と small diagrams による余完備性を扱う。候補の順序数 tag は集合で、このサイズ規約から直ちに排除されない。
- Definition 0.6, pp.2–3 は strong generator を generator と proper-subobject detection で定義する。dense であることを定義に含めていない。
- Theorem 1.11 の証明 p.18 は、finite presentability を用いて二射を canonical filtered diagram の一段階へ因子化する。
- p.296 は generated strong generator の λ-small-colimit closure の密度を、Theorem 1.11 と Proposition 1.16 に類似するとして述べる。

**Proposition 1.16、1.22、Corollary 6.8 の完全な証明本文を今回行ごとに監査したわけではない。** 特定した箇所は、取得した Theorem 1.11 の証明、p.296 の明示的主張、および以下の候補内の直接計算。

生成性の意味は、Positselski–Rosický (2018), pp.253–254 の通常の directed colimits of monomorphisms の定義とも照合した。同論文は VP 肯定のコメントを繰り返すが、その箇所では原著 Problem 3 を参照しており、別の証明は示していない。

## 2. Theorem 1.11 のどの段階を移せないか

A を強生成族の finite-colimit closure、K を任意の対象とし、

    D:A↓K→C,
    K*=colim D,
    m:K*→K

を取る。A の finite-colimit closure により A↓K は filtered。

原著は m が mono であることを示すため、生成対象 G からの二射 p,q:G→K* で mp=mq を考える。そして G の **finite presentability** により、両者を同じ canonical injection f*:A→K* に因子化する。続いて A 内の coequalizer を使って p=q とする。

G が finitely generated なだけなら、この因子化には D が mono の図式であることが必要だが、canonical diagram の射は一般の morphisms である。filtered diagram を directed poset に置き換えても、mono 性は得られない。

以下は因子化不能の可能性の指摘だけでなく、実際の m の nonmonicity の計算である。

## 3. 候補の三仮定の再監査

C の対象は (α,X,b,c), α∈Ord, b≠c、および (∞,X,b)。射は rank を下げず、b を保存し、同じ ordinal rank では c を保存、rank 上昇時には c を b に送る集合写像。∞からordinalへの射はない。

    G=(0,{b,c,x},b,c),
    H=(0,{b,c},b,c),
    X_α=(α,{0,1},0,1).

### Strong generator

x の値により C(G,Y)≅UY。U は faithful で、rank上昇射は二点を潰すので bijective でなく、同rankのbijective射は逆も射になる。従ってconservative。

さらにmonoはunderlying injectiveと同値。proper monoが省く元をGのxで選べるため、原著のproper-subobject testを直接満たす。

### Finite generatedness

Monoはrankを変えない。Directed mono diagramのrankは一定。そのcolimitは同rankでの通常のmarked-set unionであり、より高いrankの標的へのcoconeも、指定点を基点に潰す写像として一意に延長される。低rankへのcoconeはない。従ってUはこれらのcolimitsを保存し、Gはfinitely generated。

### Cocompleteness

初対象はH。集合個のordinal-rank objectsの非空coproductは、rankの上限δに置き、基点を貼り合わせ、δ未満の項のcを基点に潰す。最大rankがあればそのcを共通のcとし、最大rankがなければfresh cを加える。標的がδならc_targetへ、より高ければ基点へ、その新しい点の像が一意に決まる。

∞型を含むcoproductは∞型pointed quotient。

Parallel arrowsのcodomain rank β<∞で通常のset coequalizerを取る。b,cが異なるままならrank βを維持する。同一視された場合はrank β+1でfresh cを加える。Equalizing mapの標的は必ずrank βより高いため、新しいcの像はrank規則で一意に強制される。∞型ではordinary pointed quotient。

この確認は高rankの標的も含めた普遍性であり、same-rank部分圏でだけ確認したものではない。Small coproductsとcoequalizersからcocompletenessを得る。

## 4. finite-colimit closure A の具体化

A を、有限ordinal rank n<ωと有限underlying carrierを持つ対象の小さいfull skeletonとする。これは{G}の有限余極限閉包（同型を除く）に等しい。

- 有限coproductはfinite rank、finite carrierを保つ。
- Coequalizerはrankを高々一つ上げ、finite carrierを保つ。
- 空余積でH=X_0を得る。
- G⇉X_n の二射でxをb,cに送ると、そのcoequalizerはX_(n+1)。n=0も含む。
- X_nと有限個のGのcoproductにより、rank nで任意の有限個の自由元を持つ対象を得る。

従って原著のλ=ωの場合の閉包を、ここでは完全に記述できる。

## 5. canonical diagram の cofinal chain

    K=X_(ω+1)=(ω+1,{0,1},0,1)

とする。各n<ωについて

    Z_n=(n,{b,c,z},b,c),
    h_n:Z_n→K,
    h_n(b)=h_n(c)=0, h_n(z)=1

と置く。遷移Z_n→Z_m (n<m)は b↦b,c↦b,z↦z。これはA↓Kの鎖。

この鎖はA↓Kにcofinal/finalである。

(存在) f:A→KのAのrankをr<ωとする。n>rを選び、f(a)=0ならb、f(a)=1ならzへ送れば、fをZ_n経由で因子化できる。

(連結性) fからZ_n、Z_mへの二因子化は、十分大きいℓ>n,mへ送れば一致する。値1の元の像はzしかなく、値0の元の像にあったb/cの差はrank上昇で潰れるからである。

従ってcanonical colimitは、このnonmonic transitionの鎖で計算できる。

## 6. 比較射の nonmonicity

上の鎖のC-colimitは

    Z=(ω,{b,d,z},b,d), b≠d,

で、各injectionは b↦b,c↦b,z↦z。新しい指定点dはどの段階の像にもない。

### 普遍性

鎖からYへのcoconeがあればrank(Y)≥ω。zの像は互換性で一つに決まる。bの像はb_Y、dの像はrank(Y)=ωならc_Y、それより高ければb_Y。これが唯一のC-morphism Z→Yを与える。低rankの標的へのcoconeはない。∞型でも同じ規則で成立。

よって

    colim_(A↓K) A ≅ Z.

Canonical comparison m:Z→Kは

    m(b)=0, m(d)=0, m(z)=1.

従ってmはmonoではない。

G→Zの二射u,vを、自由元xをそれぞれb,dへ送るものとして取ると、

    u≠v,  mu=mv.

vはどのcanonical injection A→Zも経由しない。全てのinjectionのimageが{b,z}に含まれるためである。

**これがTheorem1.11で必要だった一段階への因子化の明示的な失敗である。** A↓Kはfilteredであり、cofinalなdirected chainまであるが、遷移はcをbへ潰すためmonoではない。Gのgeneratednessは適用できない。

従って、finite-colimit closure Aがdenseという結論そのものがこの候補では失敗する。単なる説明不足だけの指摘ではない。

## 7. 基数の拡大によって密度を回復できるわけでもない

任意の小さいfull subcategory D⊂Cに対し、そこに現れるordinal ranksを全て超えるα<βを選ぶ。∞型の対象が含まれてもよい。

Ordinal型DからX_α,X_βへのHomは、二つのmarksを0へ送り、残りの元を任意に送る同じ集合の写像として自然に一致する。∞型Dからは両方空。従って

    C(-,X_α)|D ≅ C(-,X_β)|D,

だがX_α≄X_β。restricted nerveはfully faithfulではなく、Dはdenseでない。

Cにはsmall dense subcategoryが存在しない。従って、λを大きくしてsmall-colimit closureを取り直すだけでは、smallnessを保つ限り修復できない。

## 8. 影響範囲と以前の議論の修正

1. **Theorem1.11は否定していない。** その仮定はpresentableであり、候補Gは満たさない。
2. **p.296のgenerated→dense還元が直接の問題。** 現在の候補の計算に基づけば、その結論はliteral hypothesesから成立しない。
3. **p.295のVP肯定コメントも、そのまま採用できない。** 問題はVPやCorollary6.8自体でなく、それを適用する前のboundedness。候補が正しければ、literal formulationはZFCで否定され、VPを追加しても構成は消えない。
4. **Reflective formulationとは区別する。** Cはsmall dense subcategoryを持たず、小さいpresheaf圏のfull reflective subcategoryにはなれない。その別formulationへの反例を得たとはしていない。
5. **私たちの過去ノートも条件を付け直す必要がある。** 原著還元を無条件の入力にした箇所を切り離し、full reflective presentationを独立の仮定とする。その設定内の反射像・個別停止・RP等の直接補題を、この候補が否定するわけではない。

外部査読未実施であり、公刊済みの訂正や独立性の決着としては扱わない。

## 9. Co-wellpoweredness の役割

Di Liberti–Rosický (2022), Theorem2.24では、生成族をλ-small colimitsだけでなくE-quotientsでも閉じる。factorization systemのλ-convenienceにはE-cowellpowerednessが含まれる。

候補ではHのstrong quotients X_αが全ordinal ranksを走る。Strong quotient closureを加えると、まさにsmallnessが失われる。この比較は、generatednessを使う標準証明に必要な追加の小ささを明示するもの。co-wellpowerednessを外した元の問題を同論文が解いたとはしない。

## 10. 訂正情報・先行例・参照

著者公開March2026正誤表では、p.18の訂正はfinite-colimit closureのessential smallnessの説明を修正している。上のpresentabilityによる因子化を変更するものではなく、p.295–296の今回のdensity assertionの訂正は見つからなかった。absenceを新規性の証拠とはしない。

Börger–Tholen(1990), Example4.3は関連するordinal-indexed strong-generator/non-cowellpowered例だが、同論文がfinite generatednessやProblem3の解決を主張したとはしていない。

一次資料：

- 原著pp.295–296：提供済みopen-problems.pdfをFilesで確認。
- 原著Definition0.6とTheorem1.11：出版社配信preview、pp.1–3,17–18を本文・画像で確認。
  https://api.pageplace.de/preview/DT0400.9780511892615_A24404888/preview-9780511892615_A24404888.pdf
- Positselski–Rosický(2018), Nearly Locally Presentable Categories, pp.253–254、本文・画像確認。
  https://tac.mta.ca/tac/volumes/33/10/33-10.pdf
- Di Liberti–Rosický(2022), Enriched Locally Generated Categories, Definition2.3、Theorem2.24（印刷p.9）、本文・画像確認。
  https://arxiv.org/pdf/2009.10980
- List of Corrections, March2026。
  https://math.fel.cvut.cz/en/people/adamekj/corrections.pdf
- Börger–Tholen(1990), Total Categories and Solid Functors, Example4.3, pp.223–225。
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A842E456CD7FFF30360076B3FB3134D4/S0008414X00003540a.pdf/total-categories-and-solid-functors.pdf

## 11. 独立監査用の最小依存列

(1) Cの射規則。
(2) Hom(G,-)=U、monoのrank保存。
(3) 同rankのdirected mono-colimitsと、一般のcoproduct/coequalizerの普遍性。
(4) A=有限carrier・有限rankのfinite-colimit closure。
(5) Z_n→X_(ω+1)の鎖のcofinality。
(6) colim Z_n=(ω,{b,d,z})と、canonical comparisonがb,dを同一視すること。

この六点が通れば、p.296のliteral density assertionに対する反例計算が成立する。Theorem1.11のpresentable版への反例ではない。
