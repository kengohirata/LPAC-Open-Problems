# No.4 の EQ_C を妨げる filtered colimit 閉性

2026-11-17。

**結論：採用済みの No.1 の入力 (NC) と N の下で、(EQ_C) は偽である。H_fg は一般の等化子に閉じず、No.4 の反例候補として棄却する。**

これは No.4 自体の肯定・否定ではない。新しい部分は、H_fg が十分大きい基数の **任意の filtered colimit** に閉じることを直接証明し、公刊済みの反射定理と組み合わせた点にある。等化子反例の存在を証明するが、具体的な終域 W と二射の式はまだ与えていない。状態は PROOF_RECONSTRUCTED / CONDITIONAL_REFUTATION_OF_EQ_C。No.1 の (NC) の独立監査・形式検証の状態は変更しない。

## 1 設定と採用する入力

Ω=ω、M_1=M_2=End_Set(Ω)、J=(0⇉1) とする。

    K=(M_1-Set)^J,
    P=(M_2-Set)^((M_1×J)^op),
    E:K^op→P,       E(Y)_i=Ω^{Y_i}.

C は K の full replete subcategory で、

    Y_0 の全元が有限支持を持ち、
    H_1(p_Y):Hom_(M_1)(Y_1,Ω)→Hom_(M_1)(Y_0,Ω) が全単射

となる対象からなる。C は K の全小余極限に閉じる。D は E(C^op) の replete image とする。

    B=(Ω⇉1),       X=E(B),
    H_fg={W∈P : 全 finitely generated F と全 f:F→W が
                         F→D→W, D∈D と因子化する}.

この「全 f」はすべての射を指し、surjection に限定しない。D→W の mono 性、中間 D のサイズ上界、因子化の一意性を要求しない。

N は「非可算可測基数が存在しない」。N の下で E は fully faithful である。

**(NC)** C↓B は弱終集合を持たない。

(NC) は [No.1 の証明稿](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md) からの入力であり、ここで再証明したとはしない。N による full faithfulness と合わせると

    X↓D ≃ (C↓B)^op

なので、X↓D は弱始集合を持たない。

以下のサイズ・filtered-colimit 補題は ZFC で成り立ち、N や (NC) を使わない。最後の棄却にのみ、この非反射性の入力を用いる。

## 2 有限生成対象には共通の presentability rank がある

𝔠=2^{aleph_0}、μ=𝔠^+ と置く。μ は非可算正則基数である。

P は小圏 A 上の前層圏 Set^(A^op) と書ける。具体的には

    A=(M_2×(M_1×J)^op)^op

でよい。A の対象は二つ、射の集合の濃度は 𝔠 である。各 representable y(a) の全 sort を合わせた台集合の濃度も高々 𝔠。

### 補題 2.1

P の finitely generated object F は有限個の representables の余積の quotient であり、全台集合の濃度は高々 𝔠 である。

**証明。** F の有限個の元が生成する部分前層は directed system をなし、その union は F である。F の finite generatedness をこの mono-colimit に適用すると、id_F はその一段階を経由する。その段階の包含は split epi でもある mono なので同型となり、有限個の元が F を生成する。これらの元に対応する representables の有限余積から F への射は成分全射である。各 representable の濃度上界から |F|≤𝔠。□

### 補題 2.2

P のすべての finitely generated object は μ-presentable である。

**証明。** F の category of elements el(F) は、対象・射とも高々 𝔠 個しか持たない。標準的な表示

    F ≅ colim_(a,x)∈el(F) y(a)

は <μ 個の射からなる図式である。各 representable の Hom は成分評価であり、すべての小余極限を保存する。したがって Hom_P(F,-) は <μ 個の成分評価からなる limit である。集合の圏では μ-filtered colimits と μ-small limits が可換するので、Hom_P(F,-) は μ-filtered colimits を保存する。□

**finite generatedness を finite presentability と同一視していない。** 関係式は有限個とは限らず、最大 𝔠 個ある。その関係式全体を処理できる μ=𝔠^+ に上げている。

### 補題 2.3

P は locally μ-presentable である。

**直接確認。** 全台集合のサイズが <μ の前層は、同じ category-of-elements 論法により μ-presentable。任意の前層は、サイズ <μ の部分前層全体の μ-directed union である。<μ 個の元から生成される部分前層は、射の個数が 𝔠<μ なので再びサイズ <μ となる。サイズ <μ の前層の同型類は集合個である。P は余完備なので結論を得る。□

この証明では、No.3 で問題となった「抽象的な generated strong generator から density を得る」という還元を使用しない。母圏は最初から明示的な前層圏である。

## 3 H_fg は任意の μ-filtered colimit に閉じる

### 定理 3.1

H_fg は P 内の全 μ-filtered colimits に閉じる。図式の射に mono 性を要求しない。

**証明。** 小さい μ-filtered category I と図式 (W_i)_(i∈I) を取り、全 W_i∈H_fg とする。P で W=colim_i W_i と置く。

F は finitely generated、f:F→W は任意とする。補題 2.2 により F は μ-presentable なので、ある i で

    f = c_i f_i,       f_i:F→W_i

と因子化する。W_i∈H_fg より、ある D_i∈D と

    F→D_i→W_i

があり、その合成は f_i。W_i→W を合成すれば f も D_i を経由する。すべての F,f に成立するので W∈H_fg。□

これは従来の directed-union 閉性より、別の方向で強い性質である。全 ω-filtered colimits に閉じるとは主張しない。一つの十分大きい正則基数 μ について、mono とは限らない遷移を持つ colimits に閉じることが重要である。

## 4 積閉性と非反射性

### 補題 4.1

H_fg は全小積に閉じる。

**証明。** C の余積を E で移せるので D は全小積に閉じる。F→∏_i W_i の各成分を F→D_i→W_i と因子化し、D の積を取れば F→∏_i D_i→∏_i W_i が得られる。集合個の因子化証人の選択には ZFC の Collection と Choice で足りる。空積は E(0_K)=1_P∈D で処理する。□

### 補題 4.2

N と (NC) の下で X↓H_fg は弱始集合を持たない。従って H_fg は P に反射的でない。

**証明。** X の sort 0 は Ω^Ω、sort 1 は Ω である。それぞれ id_Ω と 0 で左 M_2-set として生成されるので、X は P で二元生成。

仮に {r_j:X→W_j}_j が X↓H_fg の弱始集合とする。X が fg なので、それぞれを

    X --u_j--> D_j --v_j--> W_j,       D_j∈D

と因子化できる。

任意の f:X→D, D∈D に対し、D⊆H_fg なので、ある j と h:W_j→D によって f=h r_j=h v_j u_j。従って {u_j:X→D_j}_j は X↓D の弱始集合になる。§1 の入力に矛盾する。□

## 5 反射定理による一般等化子閉性の否定

用いる公刊済みの定理は次の形である。

**反射定理。** 局所可呈示圏の full replete subcategory が、全小極限と、ある十分大きい正則基数 μ の全 μ-filtered colimits に閉じるなら、reflective である。

今回の μ>ω については、さらに具体的な Hébert–Rosický の定理を適用できる。locally μ-presentable category の full subcategory が全小極限と μ-filtered colimits に閉じれば、μ-presentable objects 間の射の集合への右直交クラスであり、従って reflective である。正確な出典と原著正誤表との関係は §9 に記す。

### 定理 5.1

N と (NC) の下で H_fg は一般の等化子に閉じない。

**証明。** 等化子に閉じると仮定する。補題 4.1 の全小積閉性と合わせると H_fg は全小極限に閉じる。P は locally μ-presentable（補題 2.3）、H_fg は μ-filtered colimits に閉じる（定理 3.1）。上の公刊済み定理により H_fg は reflective である。これは補題 4.2 と矛盾する。□

したがって、次の三つは同時には成立しない。

    No.1 から採用した X↓D の弱始集合の不存在
    H_fg の現在の定義
    H_fg の一般等化子閉性

最初の二つを維持する今回の研究では、最後を棄却する。これは No.1 の (NC) を独立に確証したという意味ではない。

### 系 5.2

N と (NC) の下で、前稿の条件 (EQ_C) は偽である。

前稿で証明した

    (EQ_C) ⇔ H_fg の一般等化子閉性

に定理 5.1 を適用する。次節では、成分数の制限を含む正確な否定形を確認する。

## 6 EQ_C に反するデータの存在

N と (NC) の下で、以下のデータが存在する。

    Y∈C,       |π_0(Y_i)|≤𝔠  (i=0,1),
    W∈H_fg,
    a,b:E(Y)⇉W,
    F は finitely generated,
    t:F→E(Y),       at=bt,

しかも、どの Y'∈C、q:Y→Y'、h:Y'→Q(F) に対しても

    t^♯=h q    かつ    aE(q)=bE(q)

を同時には満たせない。

**証明。** 定理 5.1 より、Z,W∈H_fg と二射 a_0,b_0:Z⇉W で、その等化子 e:M→Z が H_fg に属さないものを取れる。定義により、ある fg F と f:F→M が、いかなる D∈D も経由しない。

Z∈H_fg なので ef は F→E(Y_0)→Z と因子化する。前稿の相対成分圧縮を適用して

    ef = v t,       t:F→E(Y),       v:E(Y)→Z,
    Y∈C,           |π_0(Y_i)|≤𝔠

とできる。a=a_0v、b=b_0v と置けば at=bt。

上記の q,h が存在すれば、currying により h は t':F→E(Y') に対応し E(q)t'=t。vE(q) は a_0,b_0 を等化するので、ある k:E(Y')→M があり ek=vE(q)。すると

    ekt'=vE(q)t'=vt=ef

であり、e の mono 性から kt'=f。これは f の D-因子化にほかならず、矛盾する。□

この導出は **存在証明** である。W、a、b を具体的な集合・作用・関数で明示した反例とは区別する。

前稿の部分的な閉性定理と合わせると、この証人の E(Y) は fg ではなく、W は D-object に mono で埋め込めない。W が旧終域 V に mono で埋め込める場合も除外される。どの V^(2) が証人になるかは、この存在証明からは分からない。

## 7 固定したテスト集合による修正も同じ障害を持つ

### 一般補題

P を locally presentable、D⊆P を全小積に閉じた full replete class、T を P の対象の集合とする。

    H_T={W : 全 F∈T と全 F→W が、ある D∈D を経由する}

と定義する。

T の全対象が同時に μ-presentable となり、P も locally μ-presentable となる十分大きい正則 μ を選べる。定理 3.1 と同じ一段階への因子化によって、H_T は μ-filtered colimits に閉じる。また補題 4.1 と同じ証明で全小積に閉じる。

もし T のある X に対して X↓D が弱始集合を持たなければ、補題 4.2 と同じ証明で X↓H_T も弱始集合を持たない。従って H_T は一般の等化子に閉じない。

P の finitely generated objects は同型を除き集合個なので、H_fg はこの補題の一例である。固定した正則 λ に対する全 λ-generated presheaves にテストを増やす修正も、その対象が同型を除き集合個である限り、同じ障害を受ける。

したがって「finite を countable にする」「固定した一つのより大きい rank に増やす」だけでは、非反射性を保持しながら全小極限閉性を得る修正にならない。これは任意の異なる構成を排除するものではなく、ここに明記した H_T 型の定義に対する障害である。

## 8 No.4 の到達点と次に必要な変更

従来の候補 H_fg に関する次の結果は、この否定と両立する。

- 全小積、retracts、全 directed unions に閉じること。
- fg な始域、D に埋め込める終域、特定の終域 V についての等化子閉性。
- 有限生成直交性の転送、有限 tuple coding、順序数の一致集合の後続・可算共終数閉性。
- No.1 の入力からの非反射性。

修正すべきなのは、「一般等化子閉性を証明すればこの候補で反例が完成するので、その証明を目指す」という研究方針である。現在の入力の下では、その一般閉性は成立しない。

No.4 の負の解を目指すなら、全小極限と directed unions には閉じるが、**どの十分大きい正則 μ に対しても全 μ-filtered colimits には閉じない**候補が必要となる。H_T 型の集合個の始域による局所因子化定義は、この必要条件を満たせない。

D から全小極限・directed unions で閉じたクラスを作る別経路は、このノートでは否定していない。ただし、拡大後の X-map が D を経由することによって非反射性を移す従来の方法を、そのまま維持できるとは限らない。別の解集合障害の証明が必要になる可能性がある。

No.4 の一般肯定、N⇒¬P4、V=L⇒¬P4、P4 の独立性のいずれも結論しない。

## 9 使用した一次資料と確認範囲

1. M. Hébert and J. Rosický, *Uncountable Orthogonality is a Closure Property*, Bulletin of the London Mathematical Society 33 (2001), 685–688. DOI: [10.1112/S0024609301008451](https://doi.org/10.1112/S0024609301008451)。[出版社の定理要約](https://academic.oup.com/blms/article-abstract/33/6/685/305277) を確認。λ>ω の locally λ-presentable category における、全小極限・λ-directed colimits 閉性と λ-orthogonality class の同値を用いる。
2. M. Hébert, J. Adámek and J. Rosický, *More on orthogonality in locally presentable categories*, Cahiers de topologie et géométrie différentielle catégoriques 42(1) (2001), 51–80。[公開全文](https://www.numdam.org/article/CTGDC_2001__42_1_51_0.pdf) の pp.52–53 に、上記の正確な定理が再掲されている。今回その本文を確認した。
3. J. Adámek and J. Rosický, *On reflective subcategories of locally presentable categories* (2015)。[著者公開版](https://arxiv.org/pdf/1504.03886) p.1、Introduction に、full subcategory に対する「全小極限とある λ-filtered colimits に閉じれば reflective」という Reflection Theorem の明記を確認した。iso-full だが full でない部分圏についての同論文の open problem と混同しない。
4. [原著の March 2026 正誤表](https://math.fel.cvut.cz/en/people/adamekj/corrections.pdf) pp.1–2。Theorem 1.39 の原著の証明には誤りがあるが、非可算 λ の主張は正しく、Hébert–Rosický (2001) に正しい証明があると記載されている。今回は λ=ω の誤った同値や原著の誤った証明に依存せず、非可算 μ=𝔠^+ を使う。

Hébert–Rosický の原論文の証明全文を新たに独立監査したとはしない。使用した定理の本文での再掲・出版社の要約・著者正誤表を照合した。今回の直接部分は §§2–4 とその帰結であり、それを上記文献に既存の H_fg の結果として帰属させない。

ローカル入力：

- [H_fg の定義、積・union 閉性、非反射性](negative_isbell_transport_fg_factorizations_equalizer_obstruction_2026-11-17.md)
- [相対成分圧縮と V を終域とする等化子](v_codomain_equalizers_root_compression_2026-11-17.md)
- [(EQ_C) の定義と一般等化子閉性との同値](general_equalizers_finite_orthogonality_and_quotient_reduction_2026-11-17.md)

## 10 再点検した境界

- filtered-colimit 閉性に中間 D のサイズ上界を使っていない。小さいのはテスト始域 F の presentability rank だけである。
- μ-filtered colimit の射に mono 性を課していない。ここを directed union の証明と取り違えると今回の障害が見えなくなる。
- F が finitely presentable であるとはしていない。μ=𝔠^+ への変更を明示した。
- 反射定理を適用する full subcategory は H_fg、母圏は P。K^op を局所可呈示と仮定していない。
- H_fg 自身の accessibility や small strong generator を仮定していない。それらを入力とする随伴関手定理で結論を先取りしていない。
- No.3 の disputed density 還元、VP、supercompact、strongly compact は今回の補題の入力ではない。
- (NC) の採用を外した無条件の ZFC 否定とはしていない。正確な含意は N+(NC)⇒¬(EQ_C) である。
- 有限の計算実験で真クラス・filtered-colimit の結論を検証したとはしない。今回の検証は直接証明と公刊定理の適用条件の点検である。
