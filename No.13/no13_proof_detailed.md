# No.13：完備かつ公理化可能な圏は局所可呈示である（証明の詳細版）

2026-11-20。この文書は [証明草稿](no13_reduced_products_proof_draft.md) の §2–§6 を、Claude (Fable 5.2) が一段ずつ導き直して書き直したものである。草稿で略述されていた箇所（§2 の公理の一覧、§3.1 の往復論法、§4 の補題、基数の選び方）を省略せずに書いた。

**状態。** AI が生成した証明であり、人間による検証はまだ行っていない。文献で既に解決されているかどうかも未確認である。

**AI による点検の記録（2026-11-20）。** 書いた AI 自身による全文の再読と、別の AI セッションによる独立の査読を行った。どちらも誤りや重大な穴を見つけなかった。査読で指摘された軽微な点（真クラスからの選択の扱い、補題 2.5 の証明の省略、§8 の不正確な記述など）は反映してある。これは正しさの保証ではない。

## 0. 主張と証明の構成

記法と規約は原著 Adámek–Rosický, *Locally Presentable and Accessible Categories* の 5.24–5.26 に従う（§1 にまとめる）。

**定理 A。** $`T`$ を無限論理 $`L_\infty`$ の理論（文の集合）とし、 $`\mathcal C=\mathrm{Mod}\,T`$ を $`T`$ のモデルとすべての準同型の圏とする。 $`\mathcal C`$ がすべての小極限を持つなら、 $`\mathcal C`$ は局所可呈示である。証明は ZFC で行う。

圏同値は完備性も局所可呈示性も保つので、定理 A は Open Problem 13「完備かつ公理化可能な圏は局所可呈示か」への肯定的な答えになる。

定理 A は次の定理に帰着する。 $`G`$ を小圏とし、前層を、 $`G`$ の対象をソート、 $`G`$ の射を単項演算とする署名 $`\Sigma_G`$ の構造とみなす（§1.5）。

**定理 B。** $`G`$ を小圏、 $`\mathcal D`$ を前層圏 $`\mathrm{Set}^{G^{op}}`$ の充満かつ同型で閉じた部分圏とし、次を仮定する。

- (B1) $`\mathcal D`$ は $`\mathrm{Set}^{G^{op}}`$ の小極限で閉じる。
- (B2) ある正則基数 $`\chi`$ と、 $`L_\chi(\Sigma_G)`$ の文の集合 $`S`$ があって、 $`\Sigma_G`$-構造 $`P`$ が $`\mathcal D`$ に属することと $`P\models S`$ とが同値である。

このとき、ある正則基数 $`\kappa`$ について、 $`\mathcal D`$ は $`\mathrm{Set}^{G^{op}}`$ の $`\kappa`$-有向余極限で閉じる。したがって $`\mathcal D`$ は局所 $`\kappa`$-可呈示であり、特に局所可呈示である。

定理 B は、原著の定理 5.20・系 5.21（有限論理 $`L_\omega`$ で公理化可能で、 $`\mathrm{Str}\,\Sigma`$ の有限極限で閉じる構造のクラスは局所有限可呈示）に対応する主張を、前層の署名の場合に無限論理で述べたものである。有限論理の証明は超積を使う。無限論理ではコンパクト性が使えないので、ここでは §3 の補題がその代わりをする。

**証明の流れ。**

1. §2：定理 A を定理 B に帰着する。小さいモデルの充満部分圏 $`G`$ に関する制限米田関手で $`\mathcal C`$ を前層圏に埋め込み、その本質像を $`\Sigma_G`$ の文の集合で公理化する。
2. §3（鍵となる補題）：$`A\in\mathcal D`$ のとき、 $`A`$ に項数 $`<\chi`$ のすべての写像を演算として加えた代数 $`A^+`$ について、冪 $`(A^+)^J`$ の任意の部分代数は $`\mathcal D`$ に属する。
3. §4：$`A\in\mathcal D`$ の、十分に完備なフィルターによる被約冪は $`\mathcal D`$ に属する。
4. §5：フィルターの完備度を対象によらず一様に選び、被約積でも閉じることを示す。
5. §6：$`\kappa`$-有向余極限を、被約積の間の二つの射の等化子として表す。
6. §7：反射定理（原著 2.48 の系）で結論する。

超フィルター、Łoś の定理、巨大基数はどこにも使わない。

## 1. 規約

### 1.1 署名・論理・構造

- $`\lambda`$ は正則基数とする。 $`\lambda`$-項の署名 $`\Sigma`$ は、ソートの集合と、項数（ソートの列）の長さが $`<\lambda`$ の演算記号・関係記号の集合からなる。
- $`\Sigma`$-構造は各ソートに集合（空でもよい）を与え、記号を解釈する。準同型は、演算と可換で関係を保つソートごとの写像である（関係を反映することは要求しない）。 $`\mathrm{Str}\,\Sigma`$ は構造と準同型の圏である。
- $`L_\lambda(\Sigma)`$ の式は、原子式から、否定、 $`<\lambda`$ 個の式の連言と選言、 $`<\lambda`$ 個の変数の存在量化で作る。全称量化と含意は、 $`\neg\exists\neg`$ と $`\neg,\vee`$ による略記とする（原著では基本記号だが、こう書き直しても式の意味は変わらない）。以下で「部分式」というときは、書き直した後の式の部分式を指す。 $`\lambda`$ が正則なので、各式の自由変数は $`<\lambda`$ 個である。 $`L_\infty`$ は、すべての $`\lambda`$ にわたる $`L_\lambda`$ の合併である。
- 理論 $`T`$ は文の**集合**である。 $`\mathrm{Mod}\,T`$ は $`T`$ のモデルのなす $`\mathrm{Str}\,\Sigma`$ の充満部分圏である。
- $`\lambda<\lambda'`$ なら $`L_\lambda\subseteq L_{\lambda'}`$ なので、 $`\lambda`$ は必要に応じて大きく取り直してよい。

### 1.2 関係署名への取り替え

演算記号 $`\sigma`$ をそのグラフを表す関係記号 $`R_\sigma`$ に置き換え、「 $`R_\sigma`$ は全域的な関数のグラフである」という文を公理に加える。項を含む原子式は、項の値を表す変数を存在量化して書き直す。こうして得られる関係署名の理論 $`T'`$ について、 $`\mathrm{Mod}\,T`$ と $`\mathrm{Mod}\,T'`$ は圏として同型である（準同型が関数のグラフを保つことと、関数と可換であることは同値）。

以下 §2 では、 $`\Sigma`$ は**関係記号だけ**からなるとする。このとき、構造 $`X`$ の任意のソートごとの部分集合 $`Y`$ は、関係を $`Y`$ に制限した**誘導部分構造**になる（項数 0 の関係記号は、 $`X`$ での真偽をそのまま引き継ぐ）。包含 $`Y\hookrightarrow X`$ は準同型であり、関係を反映する。

### 1.3 フィルター

集合 $`I\neq\emptyset`$ 上のフィルター $`F`$ は、 $`\emptyset\notin F`$ のとき**固有**という。基数 $`\theta`$ について、 $`<\theta`$ 個の元の共通部分がまた $`F`$ に属するとき $`\theta`$**-完備**という。

### 1.4 被約積

$`(A_i)_{i\in I}`$ を演算記号だけの署名の構造の族、 $`F`$ を $`I`$ 上の固有フィルターとする。**被約積** $`\prod^F A_i`$ を次で定める。

- ソート $`s`$ の元は、**部分切断**の同値類である。部分切断とは、定義域 $`\mathrm{dom}f\in F`$ を持ち、各 $`i\in\mathrm{dom}f`$ で $`f(i)\in(A_i)_s`$ となる関数 $`f`$ をいう。
- $`f\sim f'`$ とは、ある $`X\in F`$ が $`X\subseteq\mathrm{dom}f\cap\mathrm{dom}f'`$ かつ $`f|_X=f'|_X`$ を満たすことである。これは同値関係である。
- 項数 $`<\theta`$ の演算は、 $`F`$ が $`\theta`$-完備なら、代表の共通定義域の上で座標ごとに定める。代表の取り替えは $`<\theta`$ 個の $`F`$ の元の共通部分の上で値を変えないので、これは代表の選び方によらない。単項演算には完備性は要らない。

**注意 1.4。** すべての $`A_i`$ が同じ $`A`$ のとき、 $`\prod^F A`$ は通常の被約冪 $`A^I/F`$（全域関数 $`I\to A_s`$ を、一致する座標の集合が $`F`$ に属するとき同一視したもの）と自然に同型である。実際、全域関数の類を部分切断の類に送る写像は単射である。全射でもある。部分切断 $`f`$ があれば $`A_s\neq\emptyset`$ なので、 $`f`$ を $`\mathrm{dom}f`$ の外に任意に延ばせるからである。

部分切断を使うのは、 $`(A_i)_s`$ が一部の $`i`$ で空になる場合を扱うためである。

### 1.5 前層の署名

小圏 $`G`$ に対し、署名 $`\Sigma_G`$ を次で定める。ソートは $`G`$ の対象である。 $`G`$ の各射 $`p\colon g\to h`$ に、ソート $`h`$ からソート $`g`$ への単項演算記号 $`p^*`$ を置く。関係記号は置かない。

- 前層 $`P\colon G^{op}\to\mathrm{Set}`$ は、 $`p^*`$ を $`P(p)`$ と解釈して $`\Sigma_G`$-構造になる。
- 前層の間の $`\Sigma_G`$-準同型は、ちょうど自然変換である。
- 極限、冪、被約積はソートごとに計算される。
- $`\Sigma_G`$ の項は、一つの変数に単項演算記号を有限回施したものである。したがって原子式は $`m(x)=m'(y)`$ の形をしている（ $`m,m'`$ は単項演算記号の有限列）。

## 2. 定理 A を定理 B に帰着する

この節では $`\Sigma`$ を $`\lambda`$-項の関係署名、 $`T`$ を $`L_\lambda(\Sigma)`$ の理論、 $`\mathcal C=\mathrm{Mod}\,T`$ とする。 $`\Phi_T`$ を、 $`T`$ の文の部分式全体の集合とする。

無限基数 $`\nu`$ を $`\nu\ge\lambda`$、 $`\nu\ge|\Phi_T|`$、 $`\nu\ge|\Sigma|`$（ソートと関係記号の総数）となるように取り、 $`\mu=2^\nu`$ と置く。このとき $`\mu^{<\lambda}=\mu`$ である。構造の濃度とは、全ソートの台の非交和の濃度をいう。

### 2.1 下方 Löwenheim–Skolem

**補題 2.1。** $`X`$ を $`\Sigma`$-構造、 $`Z`$ を $`X`$ の濃度 $`\le\mu`$ の部分集合とする。このとき、 $`Z`$ を含む濃度 $`\le\mu`$ の誘導部分構造 $`Y\subseteq X`$ で、次を満たすものがある：すべての $`\varphi\in\Phi_T`$ と $`Y`$ の元の組 $`\bar y`$ について

```math
Y\models\varphi[\bar y]\iff X\models\varphi[\bar y].
```

特に $`X\models T`$ なら $`Y\models T`$ である。

*証明。* 原著 5.41 と同じ構成である。 $`Y_0=Z`$ とする。 $`Y_\alpha`$ から $`Y_{\alpha+1}`$ を作るには、 $`\exists\bar w\,\psi\in\Phi_T`$ の形の各式と、 $`Y_\alpha`$ の元による自由変数への各代入 $`\bar y`$ で $`X\models\exists\bar w\,\psi[\bar y]`$ となるものについて、証人の組を一つ選んで加える。極限では合併を取る。 $`Y=Y_\lambda`$ と置く。

各段階で加える元は $`|\Phi_T|\cdot\mu^{<\lambda}\cdot\lambda\le\mu`$ 個なので、 $`|Y|\le\mu`$ である。 $`\lambda`$ が正則なので、 $`Y`$ の元の長さ $`<\lambda`$ の組はある $`Y_\alpha`$（ $`\alpha<\lambda`$ ）に含まれる。同値は式の構成に関する帰納法で示す。原子式では $`Y`$ が誘導部分構造であることから従う。否定・連言・選言は明らか。存在量化では、 $`X`$ での証人が次の段階で $`Y`$ に加えられていることを使う。∎

### 2.2 小さいモデルは稠密である

各ソートの台が $`\mu`$ の部分集合である $`T`$-モデルの全体は集合であり、濃度 $`\le\mu`$ の任意の $`T`$-モデルはその一つと同型である。この集合から同型類ごとに代表を一つずつ選び、それらを対象とする $`\mathcal C`$ の充満部分圏を $`G`$ とする。 $`G`$ は小圏であり、濃度 $`\le\mu`$ の任意の $`T`$-モデルは $`G`$ のちょうど一つの対象と同型である。制限米田関手を

```math
N\colon\mathcal C\to\mathrm{Set}^{G^{op}},\qquad N(X)(g)=\mathcal C(g,X)
```

と置く。 $`g\in G`$ の元 $`a`$ とは、あるソートの台の元のことである。

**補題 2.2（まとめ上げ）。** $`X\in\mathcal C`$ とする。 $`\mu`$ 個以下の射の族 $`(x_k\colon g_k\to X)_{k\in K}`$（ $`g_k\in G`$ ）と、濃度 $`\le\mu`$ の部分集合 $`Z\subseteq X`$ が与えられたとする。このとき、 $`h\in G`$、射 $`z\colon h\to X`$、 $`G`$ の射 $`p_k\colon g_k\to h`$ があって、次が成り立つ。

- (i) すべての $`k`$ で $`z\,p_k=x_k`$。
- (ii) $`Z\subseteq\mathrm{im}\,z`$。
- (iii) $`z`$ は単射で、関係を反映する：$`X\models R(z(\bar c))`$ なら $`h\models R(\bar c)`$。

*証明。* $`Z'=Z\cup\bigcup_k\mathrm{im}\,x_k`$ の濃度は $`\le\mu`$ である。補題 2.1 により、 $`Z'`$ を含む濃度 $`\le\mu`$ の誘導部分構造 $`Y\subseteq X`$ で $`Y\models T`$ となるものがある。 $`G`$ の取り方から、同型 $`\iota\colon h\to Y`$（ $`h\in G`$ ）がある。 $`z`$ を $`\iota`$ と包含の合成とする。これは準同型で、(ii)(iii) を満たす。

$`x_k`$ の像は $`Y`$ に入るので、 $`p_k=\iota^{-1}x_k`$ と置ける。 $`Y`$ は誘導部分構造なので、 $`x_k`$ を $`Y`$ への写像とみなしたものも準同型である。したがって $`p_k`$ は準同型で、 $`G`$ は充満なので $`G`$ の射である。(i) は定義から従う。∎

特に、 $`X\in\mathcal C`$ のすべての元 $`c`$ は、ある $`g\in G`$、 $`x\colon g\to X`$、 $`a\in g`$ により $`c=x(a)`$ と書ける（ $`K=\emptyset`$、 $`Z=\{c\}`$ とする）。

**命題 2.3。**

1. $`N`$ は充満忠実である。
2. $`N`$ は $`\mathcal C`$ に存在する極限を保つ。
3. $`\mathcal C`$ が完備なら、 $`N`$ の本質像 $`\mathcal D`$（ある $`N(X)`$ と同型な前層のなす充満部分圏）は、 $`\mathrm{Set}^{G^{op}}`$ の小極限で閉じる。

*証明。* (1) 忠実性。 $`f,f'\colon X\to X'`$ が $`Nf=Nf'`$ を満たすとする。各元 $`c=x(a)`$ について $`f(c)=(fx)(a)=(f'x)(a)=f'(c)`$ である。

充満性。 $`\eta\colon NX\to NX'`$ を自然変換とする。 $`X`$ の元 $`c=x(a)`$（ $`x\colon g\to X`$ ）に対し $`f(c)=\eta_g(x)(a)`$ と置く。

- *代表によらないこと。* $`x(a)=x'(a')`$（ $`x'\colon g'\to X`$ ）とする。補題 2.2 を $`x,x'`$ に適用して $`z,p,p'`$ を取る。 $`z`$ は単射なので $`p(a)=p'(a')`$ である。自然性から $`\eta_g(x)=\eta_g(zp)=\eta_h(z)\,p`$、同様に $`\eta_{g'}(x')=\eta_h(z)\,p'`$ となる。ゆえに $`\eta_g(x)(a)=\eta_h(z)(p(a))=\eta_h(z)(p'(a'))=\eta_{g'}(x')(a')`$。
- *準同型であること。* $`X\models R((c_k)_{k<\beta})`$（ $`\beta<\lambda`$ ）とし、 $`c_k=x_k(a_k)`$ と書く。補題 2.2 で $`z,(p_k)`$ を取ると、(iii) から $`h\models R((p_k(a_k))_k)`$ である。 $`\eta_h(z)\colon h\to X'`$ は準同型なので $`X'\models R((\eta_h(z)(p_k(a_k)))_k)`$。上と同じ計算で $`\eta_h(z)(p_k(a_k))=f(c_k)`$ である。
- *$`Nf=\eta`$ であること。* $`x\colon g\to X`$ と $`a\in g`$ について $`(fx)(a)=f(x(a))=\eta_g(x)(a)`$。

(2) 表現可能関手 $`\mathcal C(g,-)`$ は極限を保ち、前層圏の極限は各点で計算される。

(3) $`\Delta\colon\mathcal J\to\mathcal D`$ を小図式とする。各 $`j`$ について $`X_j\in\mathcal C`$ と同型 $`\Delta(j)\cong N(X_j)`$ を選ぶ。そのような対の全体は真クラスでありうるが、集合論的ランクが最小の対に限れば集合になるので、これは集合の族からの選択である。 $`N`$ が充満忠実なので、 $`\Delta`$ の射は一意に $`\mathcal C`$ の射に持ち上がり、図式 $`\Delta'\colon\mathcal J\to\mathcal C`$ と自然同型 $`\Delta\cong N\Delta'`$ を得る。 $`\mathcal C`$ は完備なので (2) により $`\lim\Delta\cong\lim N\Delta'\cong N(\lim\Delta')\in\mathcal D`$。∎

### 2.3 $`\Sigma`$ の式を $`\Sigma_G`$ の式に翻訳する

$`\Sigma`$ のソート $`s`$ に対し、**タグ**の集合を

```math
\mathrm{Tag}_s=\{(g,a)\mid g\in G,\ a\in g_s\}
```

と置く。タグ $`t=(g,a)`$ とソート $`g`$ の変数 $`x`$ の対は、 $`P=NX`$ では $`X`$ の元 $`x(a)`$ を表すことを意図している。

**基本の式。** 以下、 $`z`$ はソート $`h`$ の変数である。

- 同じソートのタグ $`t=(g,a)`$、 $`t'=(g',a')`$ に対し

  ```math
  \mathrm{Eq}_{t,t'}(x,x')\ :=\ \bigvee_{(h,p,p')}\exists z\,\bigl(p^*z=x\ \wedge\ p'^*z=x'\bigr).
  ```

  選言は、 $`h\in G`$、 $`p\in G(g,h)`$、 $`p'\in G(g',h)`$ で $`p(a)=p'(a')`$ を満たす三つ組全体にわたる。

- 項数 $`(s_k)_{k<\beta}`$ の関係記号 $`R`$ と、タグの列 $`\bar t=(t_k)_{k<\beta}`$（ $`t_k=(g_k,a_k)\in\mathrm{Tag}_{s_k}`$ ）に対し

  ```math
  \mathrm{Rel}^R_{\bar t}(\bar x)\ :=\ \bigvee_{(h,(p_k)_k)}\exists z\,\bigwedge_{k<\beta}p_k^*z=x_k.
  ```

  選言は、 $`h\in G`$ と $`p_k\in G(g_k,h)`$ で $`h\models R((p_k(a_k))_k)`$ を満たす組全体にわたる。

**翻訳。** $`\Sigma`$ の式 $`\varphi(\bar v)`$（自由変数 $`v_k`$ のソートは $`s_k`$ ）と、タグの列 $`\bar t`$（ $`t_k=(g_k,a_k)\in\mathrm{Tag}_{s_k}`$ ）に対し、 $`\Sigma_G`$ の式 $`\varphi^{\bar t}(\bar x)`$（ $`x_k`$ のソートは $`g_k`$ ）を、 $`\varphi`$ の構成に関する再帰で定める。

- $`(v_k=v_l)^{\bar t}:=\mathrm{Eq}_{t_k,t_l}(x_k,x_l)`$。
- $`R(v_{k_0},v_{k_1},\dots)^{\bar t}:=\mathrm{Rel}^R_{(t_{k_0},t_{k_1},\dots)}(x_{k_0},x_{k_1},\dots)`$。
- $`(\neg\varphi)^{\bar t}:=\neg\varphi^{\bar t}`$、 $`(\bigwedge_i\varphi_i)^{\bar t}:=\bigwedge_i\varphi_i^{\bar t}`$、 $`(\bigvee_i\varphi_i)^{\bar t}:=\bigvee_i\varphi_i^{\bar t}`$。
- $`\bar w`$ のソートを $`(s'_m)_m`$ として

  ```math
  (\exists\bar w\,\psi(\bar v,\bar w))^{\bar t}\ :=\ \bigvee_{\bar u\in\prod_m\mathrm{Tag}_{s'_m}}\exists\bar y\,\psi^{\bar t\bar u}(\bar x,\bar y).
  ```

  ある $`\mathrm{Tag}_{s'_m}`$ が空なら、これは空の選言、すなわち偽である。

**補題 2.4（ $`NX`$ での意味）。** $`X\in\mathcal C`$ とする。 $`\Sigma`$ のすべての式 $`\varphi(\bar v)`$、タグの列 $`\bar t`$、 $`x_k\in NX(g_k)=\mathcal C(g_k,X)`$ について

```math
NX\models\varphi^{\bar t}[\bar x]\iff X\models\varphi[(x_k(a_k))_k].
```

*証明。* $`\varphi`$ の構成に関する帰納法による。 $`NX`$ では $`p^*z=z\,p`$ であることに注意する。

- *等式。* $`NX\models\mathrm{Eq}_{t,t'}[x,x']`$ なら、 $`zp=x`$、 $`zp'=x'`$、 $`p(a)=p'(a')`$ となる $`h,p,p',z`$ があり、 $`x(a)=z(p(a))=z(p'(a'))=x'(a')`$。逆に $`x(a)=x'(a')`$ なら、補題 2.2 を $`x,x'`$ に適用する。 $`z`$ が単射なので $`p(a)=p'(a')`$ であり、この $`(h,p,p')`$ と $`z`$ が選言の一項を満たす。
- *関係。* $`NX\models\mathrm{Rel}^R_{\bar t}[\bar x]`$ なら、 $`h\models R((p_k(a_k))_k)`$ と準同型 $`z`$ から $`X\models R((x_k(a_k))_k)`$。逆は補題 2.2 と (iii) による。
- *否定・連言・選言。* 帰納法の仮定から直ちに従う。
- *存在量化。* 左辺が成り立つなら、あるタグの列 $`\bar u`$ と $`y_m\in\mathcal C(g'_m,X)`$ で $`NX\models\psi^{\bar t\bar u}[\bar x,\bar y]`$ となり、帰納法の仮定から $`(y_m(b_m))_m`$ が $`X`$ での証人になる。逆に $`X`$ に証人 $`(c_m)_m`$ があれば、補題 2.2 の後の注意により各 $`c_m`$ を $`y_m(b_m)`$ と書け、帰納法の仮定から左辺が成り立つ。∎

### 2.4 本質像の公理系 $`S`$

$`\Sigma_G`$-構造 $`P`$ に対する次の文を考える。

- **(S0) 前層の等式。** 各 $`g\in G`$ について $`\forall x\,(\mathrm{id}_g^*x=x)`$。合成可能な各対 $`p\colon g\to h`$、 $`q\colon h\to k`$ について $`\forall z\,(p^*q^*z=(qp)^*z)`$。
- **(S1) 推移性。** 同じソートの各タグ $`t,t',t''`$ について

  ```math
  \forall x\,x'\,x''\ \bigl(\mathrm{Eq}_{t,t'}(x,x')\wedge\mathrm{Eq}_{t',t''}(x',x'')\rightarrow\mathrm{Eq}_{t,t''}(x,x'')\bigr).
  ```

- **(S2) 関係が代表によらないこと。** 各関係記号 $`R`$ と、その項数に合うタグの列 $`\bar t,\bar t'`$ について

  ```math
  \forall\bar x\,\bar x'\ \Bigl(\bigwedge_k\mathrm{Eq}_{t_k,t'_k}(x_k,x'_k)\wedge\mathrm{Rel}^R_{\bar t}(\bar x)\rightarrow\mathrm{Rel}^R_{\bar t'}(\bar x')\Bigr).
  ```

- **(S3) $`T`$ の翻訳。** 各 $`\sigma\in T`$ について、文 $`\sigma^{\emptyset}`$（空のタグ列による翻訳）。
- **(S4) 単射性。** 各 $`g\in G`$ について

  ```math
  \forall x\,x'\ \Bigl(\bigwedge_{a\in g}\mathrm{Eq}_{(g,a),(g,a)}(x,x')\rightarrow x=x'\Bigr).
  ```

- **(S5) 全射性。** 各 $`g\in G`$ と、 $`g`$ の各元 $`a`$ にそのソートのタグ $`t_a=(g_a,b_a)`$ を割り当てる各関数 $`a\mapsto t_a`$ について

  ```math
  \forall(y_a)_{a\in g}\ \Bigl(\bigwedge_{(R,\bar a)}\mathrm{Rel}^R_{(t_{a_k})_k}\bigl((y_{a_k})_k\bigr)\rightarrow\exists x\bigwedge_{a\in g}\mathrm{Eq}_{(g,a),t_a}(x,y_a)\Bigr).
  ```

  ここで $`y_a`$ はソート $`g_a`$ の変数、 $`x`$ はソート $`g`$ の変数である。連言は、関係記号 $`R`$ と $`g\models R(\bar a)`$ を満たす $`g`$ の元の組 $`\bar a=(a_k)_k`$ の対全体にわたる。

$`S`$ を (S0)–(S5) の文全体の集合とする。 $`G`$、 $`\Sigma`$、 $`T`$、タグは集合なので、 $`S`$ は集合である。現れる連言・選言の項数は集合の濃度で抑えられ、一度に量化する変数は $`\mu`$ 個以下である。これらすべてと $`\lambda`$ より大きい正則基数 $`\chi`$ を一つ選ぶと、 $`S\subseteq L_\chi(\Sigma_G)`$ である。

**$`P`$ から構造 $`X_P`$ を作る。** $`P`$ が (S0)–(S2) を満たすとする。

- $`\mathrm{Eq}`$ は、三つ組 $`(g,a,x)`$（ $`(g,a)\in\mathrm{Tag}_s`$、 $`x\in P(g)`$ ）全体の上の同値関係である。反射性は $`h=g`$、 $`p=p'=\mathrm{id}_g`$、 $`z=x`$ と (S0) から、対称性は定義の対称性から、推移性は (S1) から従う。
- $`X_P`$ のソート $`s`$ の台を、この同値類 $`[g,a,x]`$ 全体とする。
- 関係 $`R`$ は、代表について $`\mathrm{Rel}^R`$ が成り立つときに成り立つと定める。(S2) により代表の選び方によらない。

**補題 2.5。** $`P`$ が (S0)–(S2) を満たすとする。 $`\Sigma`$ のすべての式 $`\varphi(\bar v)`$、タグの列 $`\bar t`$、 $`x_k\in P(g_k)`$ について

```math
X_P\models\varphi[([t_k,x_k])_k]\iff P\models\varphi^{\bar t}[\bar x].
```

*証明。* $`\varphi`$ の構成に関する帰納法による。

- *等式。* $`[t_k,x_k]=[t_l,x_l]`$ は、同値類の定義により $`P\models\mathrm{Eq}_{t_k,t_l}[x_k,x_l]`$ と同値である。
- *関係。* $`X_P\models R(([t_k,x_k])_k)`$ は、 $`X_P`$ の関係の定義により $`P\models\mathrm{Rel}^R_{\bar t}[\bar x]`$ と同値である（(S2) により代表によらない）。
- *否定・連言・選言。* 帰納法の仮定から直ちに従う。
- *存在量化。* $`X_P`$ に証人 $`(c_m)_m`$ があるとする。各 $`c_m`$ の代表 $`(g'_m,b_m,y_m)`$ を選び $`u_m=(g'_m,b_m)`$ と置くと、帰納法の仮定から $`P\models\psi^{\bar t\bar u}[\bar x,\bar y]`$ であり、翻訳の定義から $`P\models(\exists\bar w\,\psi)^{\bar t}[\bar x]`$ となる。逆に、あるタグの列 $`\bar u`$ と $`\bar y`$ で $`P\models\psi^{\bar t\bar u}[\bar x,\bar y]`$ なら、帰納法の仮定から $`([u_m,y_m])_m`$ が $`X_P`$ での証人になる。∎

**標準的な写像。** $`P`$ が (S0)–(S2) を満たすとき、 $`g\in G`$ と $`x\in P(g)`$ に対し

```math
\varepsilon_g(x)\colon g\to X_P,\qquad a\mapsto[g,a,x]
```

と置く。

- $`\varepsilon_g(x)`$ は準同型である。 $`g\models R(\bar a)`$ のとき、 $`h=g`$、 $`p_k=\mathrm{id}_g`$、 $`z=x`$ が (S0) により $`\mathrm{Rel}^R_{((g,a_k))_k}(x,x,\dots)`$ の選言の一項を満たす。
- $`\varepsilon`$ は自然である。 $`p\colon g\to g'`$ と $`x'\in P(g')`$ について、 $`h=g'`$、 $`p`$、 $`p'=\mathrm{id}_{g'}`$、 $`z=x'`$ が $`\mathrm{Eq}_{(g,a),(g',p(a))}(p^*x',x')`$ を満たすので、 $`\varepsilon_g(p^*x')=\varepsilon_{g'}(x')\,p`$ である。

したがって $`X_P\models T`$ のとき、 $`\varepsilon\colon P\to N(X_P)`$ は自然変換である。

**命題 2.6。** $`\Sigma_G`$-構造 $`P`$ について、 $`P\models S`$ であることと、 $`P`$ がある $`X\in\mathcal C`$ について $`NX`$ と同型な前層であることは同値である。すなわち $`\mathrm{Mod}\,S=\mathcal D`$。

*証明。* (⇒) $`P\models S`$ とする。(S0) から $`P`$ は前層である。(S3) と補題 2.5 から $`X_P\models T`$、すなわち $`X_P\in\mathcal C`$ である。

- $`\varepsilon_g`$ は単射である。 $`\varepsilon_g(x)=\varepsilon_g(x')`$ は、すべての $`a\in g`$ で $`\mathrm{Eq}_{(g,a),(g,a)}(x,x')`$ が成り立つことを意味し、(S4) から $`x=x'`$。
- $`\varepsilon_g`$ は全射である。準同型 $`\phi\colon g\to X_P`$ を取り、各 $`a`$ について $`\phi(a)`$ の代表 $`(g_a,b_a,y_a)`$ を選ぶ。 $`\phi`$ が準同型なので、補題 2.5 の原子式の場合から (S5) の前件が成り立つ。(S5) の与える $`x`$ は $`\varepsilon_g(x)=\phi`$ を満たす。

ゆえに $`\varepsilon\colon P\to N(X_P)`$ は自然同型である。

(⇐) $`S`$ の真偽は同型で不変なので、 $`P=NX`$ としてよい。(S0) は明らか。写像 $`\vartheta\colon(g,a,x)\mapsto x(a)`$ を考える。補題 2.4 の原子式の場合から、 $`\mathrm{Eq}`$ は $`\vartheta`$ の値の一致と同値で、 $`\mathrm{Rel}^R`$ は $`\vartheta`$ の値の組で $`R`$ が成り立つことと同値である。したがって (S1)(S2) が成り立ち、 $`\vartheta`$ は単射で関係を保ち反映する写像 $`X_P\to X`$ を誘導する。補題 2.2 の後の注意から、これは全射でもある。ゆえに $`X_P\cong X`$ である。(S3) は補題 2.4 から従う。この同型のもとで $`\varepsilon_g(x)`$ は $`x`$ 自身に対応するので、 $`\varepsilon_g`$ は全単射であり、(S4)(S5) が成り立つ。∎

### 2.5 帰着のまとめ

$`\mathcal C`$ が完備だとする。命題 2.3 と命題 2.6 により、 $`\mathcal D`$ は $`\mathrm{Set}^{G^{op}}`$ の充満かつ同型で閉じた部分圏で、(B1) と (B2) を満たし、 $`\mathcal C\simeq\mathcal D`$ である。定理 B から $`\mathcal D`$ は局所可呈示なので、 $`\mathcal C`$ も局所可呈示である。これで定理 A は定理 B に帰着した。

以下 §3–§7 では、 $`G`$、 $`\mathcal D`$、 $`\chi`$、 $`S`$ を定理 B のとおりとする。(B1) から、 $`\mathcal D`$ は積・冪・等化子、および射の族の同時等化子で閉じる。

## 3. 鍵となる補題：冪の部分代数

$`A\in\mathcal D`$ を固定する。署名 $`\Sigma_A^+`$ を次で定める。ソートは $`G`$ の対象である。長さ $`<\chi`$ のソートの列 $`\bar s=(s_k)_{k<\ell}`$、ソート $`s'`$、および**すべての**写像

```math
f\colon A^{\bar s}:=\prod_{k<\ell}A_{s_k}\longrightarrow A_{s'}
```

に対して、項数 $`\bar s\to s'`$ の演算記号を一つ置く。 $`A^+`$ を、各記号をその写像自身で解釈した $`A`$ の展開とする。

- $`\ell=0`$ の場合として、 $`A`$ の各元が定数になる。
- $`\ell=1`$ の場合として、 $`A`$ の演算 $`p^*`$ が含まれる。したがって $`\Sigma_A^+`$-代数 $`H`$ は $`\Sigma_G`$-構造への縮約を持つ。これを $`H|_G`$ と書く。

**補題 3.1。** $`J`$ を空でない集合、 $`H`$ を冪 $`(A^+)^J`$ の部分代数とする（各 $`H_s\subseteq(A_s)^J`$ で、 $`\Sigma_A^+`$ のすべての演算の座標ごとの適用で閉じる）。このとき $`H|_G\in\mathcal D`$ である。

*証明。* 証明は三段階からなる。

**段階 0：基数と記号。** 無限基数 $`\tau`$ を、 $`\tau\ge\chi`$ かつすべてのソート $`s`$ で $`\tau\ge|A_s|`$ となるように取り、

```math
\rho=2^\tau,\qquad\delta=\rho^+
```

と置く。 $`\delta`$ は正則で、 $`\chi\le\tau<\rho<\delta`$ である。長さ $`<\chi`$ のソートの列 $`\bar s`$ について $`|A^{\bar s}|\le\tau^{<\chi}\le\rho`$ である。

$`|U|>\delta`$ となる集合 $`U`$ を取り、 $`E=J\times U`$、 $`P=A^E`$ と置く。(B1) により $`P\in\mathcal D`$ である。

- $`h\in(A_s)^J`$ の**引き戻し**を $`h^\pi\in(A_s)^E`$、 $`h^\pi(j,u)=h(j)`$ とする。
- $`f,f'\in(A_s)^E`$ に対し $`d(f,f')=\{e\in E\mid f(e)\neq f'(e)\}`$ と置く。
- 各ソート $`s`$ について

  ```math
  W_s=\{\,f\in(A_s)^E\mid\exists h\in H_s\ \ |d(f,h^\pi)|\le\delta\,\}
  ```

  と置く。

$`W`$ は $`P`$ の $`\Sigma_G`$-部分構造である。実際 $`p\colon g\to g'`$ と $`f\in W_{g'}`$ について、 $`d(p^*f,(p^*h)^\pi)\subseteq d(f,h^\pi)`$ であり、 $`H`$ は演算 $`p^*`$ で閉じるので $`p^*h\in H_g`$ である。

**段階 1：$`W`$ は $`P`$ の $`L_\chi`$-初等部分構造である。** すなわち、 $`L_\chi(\Sigma_G)`$ のすべての式 $`\varphi`$ と $`W`$ の元の組 $`\bar q`$ について $`W\models\varphi[\bar q]\iff P\models\varphi[\bar q]`$ を示す。

長さ $`<\chi`$ のソートの列を**形**と呼ぶ。形 $`\bar s`$ の $`P`$ の元の組 $`\bar p=(p_k)_k`$ は、写像 $`\bar p\colon E\to A^{\bar s}`$ と同一視できる。 $`v\in A^{\bar s}`$ に対し

```math
E^{\bar p}_v=\{e\in E\mid\bar p(e)=v\}
```

を $`v`$ の**セル**と呼ぶ。基数 $`c`$ に対し $`\lfloor c\rfloor=\min(c,\delta)`$ と書く。同じ形の、 $`P`$ の組 $`\bar p`$ と $`W`$ の組 $`\bar q`$ について

```math
\bar p\approx\bar q\quad:\iff\quad\forall v\in A^{\bar s}\ \ \lfloor|E^{\bar p}_v|\rfloor=\lfloor|E^{\bar q}_v|\rfloor
```

と定める。

*主張 1（原子式）。* $`\bar p\approx\bar q`$ なら、 $`\bar p`$ が $`P`$ で満たす原子式と、 $`\bar q`$ が $`W`$ で満たす原子式は一致する。

原子式 $`m(x_k)=m'(x_l)`$ を取る。 $`m,m'`$ は $`A`$ では写像 $`m^A,m'^A`$ として解釈される。 $`P`$ の演算は座標ごとなので、 $`P\models(m(x_k)=m'(x_l))[\bar p]`$ は、すべての $`e`$ で $`m^A(p_k(e))=m'^A(p_l(e))`$ となること、すなわち $`E^{\bar p}_v\neq\emptyset`$ となるすべての $`v`$ で $`m^A(v_k)=m'^A(v_l)`$ となることと同値である。 $`W`$ は部分構造なので $`\bar q`$ についても同じである。 $`\bar p\approx\bar q`$ から、空でないセルを持つ $`v`$ は両者で一致する。

*主張 2（ $`P`$ から $`W`$ へ）。* $`\bar p\approx\bar q`$ とし、 $`\bar w`$ を $`P`$ の形 $`\bar s'`$ の組とする。このとき $`W`$ の形 $`\bar s'`$ の組 $`\bar w'`$ で $`\bar p\bar w\approx\bar q\bar w'`$ となるものがある。

$`v\in A^{\bar s}`$、 $`z\in A^{\bar s'}`$ に対し $`n_{v,z}=|E^{\bar p\bar w}_{(v,z)}|`$ と置く。 $`E^{\bar p}_v`$ はセル $`E^{\bar p\bar w}_{(v,z)}`$（ $`z\in A^{\bar s'}`$ ）の非交和である。 $`\bar w`$ が存在し $`E\neq\emptyset`$ なので $`A^{\bar s'}\neq\emptyset`$ である。

$`|E^{\bar p}_v|<\delta`$ のとき $`v`$ を**小さい**、そうでないとき**大きい**という。 $`\bar p\approx\bar q`$ から、 $`v`$ が小さいなら $`|E^{\bar q}_v|=|E^{\bar p}_v|`$、大きいなら $`|E^{\bar q}_v|\ge\delta`$ である。

写像 $`z_0\colon A^{\bar s}\to A^{\bar s'}`$ を次のように選ぶ。 $`v`$ が大きいとき、 $`E^{\bar p}_v`$ は $`\le\rho`$ 個のセルの和で、 $`\delta`$ は正則かつ $`\delta>\rho`$ なので、 $`n_{v,z}\ge\delta`$ となる $`z`$ がある。その一つを $`z_0(v)`$ とする。 $`v`$ が小さいときは $`z_0(v)`$ を任意に選ぶ。

$`\bar w'\colon E\to A^{\bar s'}`$ を、 $`\bar q`$ のセルごとに定める。

- $`v`$ が小さいとき。全単射 $`\beta_v\colon E^{\bar q}_v\to E^{\bar p}_v`$ を選び、 $`e\in E^{\bar q}_v`$ で $`\bar w'(e)=\bar w(\beta_v(e))`$ とする。このとき $`|E^{\bar q\bar w'}_{(v,z)}|=n_{v,z}`$ である。
- $`v`$ が大きいとき。 $`E^{\bar q}_v`$ の中に、 $`z\neq z_0(v)`$ で添字付けた互いに素な部分集合 $`C_{v,z}`$ を、 $`|C_{v,z}|=\lfloor n_{v,z}\rfloor`$ かつ残り $`E^{\bar q}_v\setminus\bigcup_zC_{v,z}`$ の濃度が $`\ge\delta`$ となるように選ぶ。これは可能である： $`E^{\bar q}_v`$ から濃度 $`\delta`$ の互いに素な部分集合 $`Q_0,Q_1`$ を取ると、 $`\rho\cdot\delta=\delta`$ なので $`C_{v,z}`$ をすべて $`Q_1`$ の中に取れ、残りは $`Q_0`$ を含む。 $`e\in C_{v,z}`$ では $`\bar w'(e)=z`$、残りでは $`\bar w'(e)=z_0(v)`$ とする。このとき、 $`z\neq z_0(v)`$ では $`|E^{\bar q\bar w'}_{(v,z)}|=\lfloor n_{v,z}\rfloor`$ であり、 $`z=z_0(v)`$ では両側とも濃度 $`\ge\delta`$ である。

どちらの場合も $`\lfloor|E^{\bar q\bar w'}_{(v,z)}|\rfloor=\lfloor n_{v,z}\rfloor`$ となる。 $`\bar w'`$ を $`P`$ の組とみなせば、これは $`\bar p\bar w\approx\bar q\bar w'`$ の条件である。

残るのは、 $`\bar w'`$ の各成分 $`w'_m`$ が $`W`$ に属することである。 $`q_k\in W`$ なので、 $`h_k\in H`$ で $`|d(q_k,h_k^\pi)|\le\delta`$ となるものがある。 $`z_0`$ の第 $`m`$ 成分 $`\zeta_m\colon A^{\bar s}\to A_{s'_m}`$ は $`\Sigma_A^+`$ の演算記号の一つである。 $`H`$ は部分代数なので

```math
\hat h_m:=\zeta_m\bigl((h_k)_k\bigr)\in H_{s'_m},\qquad\hat h_m(j)=\zeta_m\bigl((h_k(j))_k\bigr).
```

$`e=(j,u)`$ が次の二つの集合のどちらにも属さないとする。

- $`D_1=\bigcup_kd(q_k,h_k^\pi)`$
- $`D_2=\bigcup_{v\in V_0}E^{\bar q}_v\ \cup\ \bigcup_{v\in V_1}\bigcup_{z\neq z_0(v)}C_{v,z}`$ （ $`V_0`$ は小さい $`v`$ の全体、 $`V_1`$ は大きい $`v`$ の全体）

このとき $`\bar q(e)=(h_k(j))_k`$ であり、 $`\bar w'(e)=z_0(\bar q(e))`$ なので、 $`w'_m(e)=\hat h_m(j)=\hat h_m^\pi(e)`$ である。

濃度を数える。 $`D_1`$ は $`<\chi\le\delta`$ 個の濃度 $`\le\delta`$ の集合の和なので $`|D_1|\le\delta`$。小さいセルは濃度 $`\le\rho`$ で高々 $`\rho`$ 個、 $`C_{v,z}`$ は濃度 $`\le\delta`$ で高々 $`\rho\cdot\rho`$ 個なので $`|D_2|\le\delta`$。ゆえに $`|d(w'_m,\hat h_m^\pi)|\le\delta`$、すなわち $`w'_m\in W`$ である。

*主張 3（ $`W`$ から $`P`$ へ）。* $`\bar p\approx\bar q`$ とし、 $`\bar w'`$ を $`W`$ の形 $`\bar s'`$ の組とする。このとき $`P`$ の形 $`\bar s'`$ の組 $`\bar w`$ で $`\bar p\bar w\approx\bar q\bar w'`$ となるものがある。

$`m_{v,z}=|E^{\bar q\bar w'}_{(v,z)}|`$ と置く。 $`v`$ が小さいときは全単射で $`\bar w'`$ を移す。 $`v`$ が大きいときは $`|E^{\bar q}_v|\ge\delta`$ なので、 $`m_{v,z_1}\ge\delta`$ となる $`z_1`$ がある。 $`E^{\bar p}_v`$ の中に、 $`z\neq z_1`$ について濃度 $`\lfloor m_{v,z}\rfloor`$ の互いに素な部分集合を、残りの濃度が $`\ge\delta`$ となるように選び、主張 2 と同じように $`\bar w`$ を定める。 $`P`$ は全冪なので、こうして定めた $`\bar w`$ は $`P`$ の組である。

*主張 4。* $`\bar p\approx\bar q`$ なら、自由変数が $`\bar p`$ の形に含まれるすべての $`\varphi\in L_\chi(\Sigma_G)`$ について $`P\models\varphi[\bar p]\iff W\models\varphi[\bar q]`$。

$`\varphi`$ の構成に関する帰納法による。原子式は主張 1、否定・連言・選言は帰納法の仮定から従う。 $`\varphi=\exists\bar y\,\psi`$ のとき、 $`P`$ での証人 $`\bar w`$ から主張 2 で $`\bar w'`$ を取り、 $`\bar p\bar w\approx\bar q\bar w'`$ に帰納法の仮定を適用する。逆は主張 3 による。量化する変数は $`<\chi`$ 個なので、延長した組の長さも $`<\chi`$ である。

*段階 1 の結論。* $`W`$ の組 $`\bar q`$ を $`P`$ の組とみなすと、自明に $`\bar q\approx\bar q`$ である。主張 4 から $`W`$ は $`P`$ の $`L_\chi`$-初等部分構造である。特に $`P\models S`$ なので $`W\models S`$、すなわち (B2) により $`W\in\mathcal D`$ である。

**段階 2：置換の固定点として $`H`$ を取り出す。** $`\sigma\in\mathrm{Sym}(U)`$ に対し $`\hat\sigma\colon P\to P`$、 $`\hat\sigma(f)(j,u)=f(j,\sigma(u))`$ と置く。 $`\hat\sigma`$ は $`P`$ の自己同型である。 $`\hat\sigma(h^\pi)=h^\pi`$ であり、 $`d(\hat\sigma f,h^\pi)`$ は $`d(f,h^\pi)`$ の $`E`$ の全単射による像なので、 $`\hat\sigma`$ は $`W`$ の自己同型に制限される。

$`W\in\mathcal D`$ なので、冪 $`W^{\mathrm{Sym}(U)}`$ は $`\mathcal D`$ に属する。二つの射

```math
\Delta,\Theta\colon W\rightrightarrows W^{\mathrm{Sym}(U)},\qquad\Delta(f)=(f)_\sigma,\quad\Theta(f)=(\hat\sigma f)_\sigma
```

の等化子 $`K`$ も $`\mathcal D`$ に属する。 $`K_s`$ は、すべての $`\sigma`$ で $`\hat\sigma f=f`$ となる $`f\in W_s`$ 全体である。

- $`f\in K_s`$ とする。 $`\mathrm{Sym}(U)`$ は $`U`$ に推移的に作用するので、 $`f`$ は各 $`\{j\}\times U`$ の上で定数である。すなわち、ある $`k\colon J\to A_s`$ について $`f=k^\pi`$。 $`f\in W_s`$ なので、ある $`h\in H_s`$ で $`|d(k^\pi,h^\pi)|\le\delta`$。ところが $`d(k^\pi,h^\pi)=\{j\mid k(j)\neq h(j)\}\times U`$ は、空でなければ濃度 $`\ge|U|>\delta`$ である。ゆえに $`k=h`$。
- 逆に、 $`h\in H_s`$ なら $`h^\pi\in K_s`$ である。

したがって $`K=\{h^\pi\mid h\in H\}`$ である。 $`U\neq\emptyset`$ なので $`h\mapsto h^\pi`$ は単射であり、演算 $`p^*`$ と可換である。ゆえに $`H|_G\cong K`$ となり、 $`\mathcal D`$ は同型で閉じるので $`H|_G\in\mathcal D`$ である。∎

## 4. 被約冪

**補題 4.1。** $`A\in\mathcal D`$ とする。ある基数 $`\kappa_A`$ があって、空でない集合 $`I`$ 上の任意の固有な $`\kappa_A`$-完備フィルター $`F`$ について、被約冪 $`A^I/F`$ は $`\mathcal D`$ に属する。

*証明。* $`\Phi_S`$ を $`S`$ の文の部分式全体の集合とする。基数 $`\mu_A`$ を

```math
\mu_A^{<\chi}=\mu_A,\qquad\mu_A\ge|\Sigma_A^+|,\qquad\mu_A\ge|\Phi_S|
```

となるように取る（例えば、右の二つと $`\chi`$ を抑える無限基数 $`\nu'`$ について $`\mu_A=2^{\nu'}`$ ）。 $`|\Sigma_A^+|`$ は演算記号の総数で、ソートの数以上である。 $`\kappa_A=\mu_A^+`$ と置く。

$`F`$ を固有な $`\kappa_A`$-完備フィルターとする。 $`\chi\le\mu_A`$ なので $`F`$ は $`\chi`$-完備であり、 $`\Sigma_A^+`$ のすべての演算が被約冪 $`B^+:=(A^+)^I/F`$ の上で定まる（§1.4）。その $`\Sigma_G`$-縮約は $`B:=A^I/F`$ である。

**小さい初等部分代数。** 補題 2.1 と同じ構成で、 $`B^+`$ の部分集合 $`H`$ を次を満たすように取る。

- (a) $`|H|\le\mu_A`$。
- (b) $`H`$ は $`\Sigma_A^+`$ のすべての演算で閉じる。
- (c) すべての $`\varphi\in\Phi_S`$ と $`H`$ の元の組 $`\bar b`$ について $`H|_G\models\varphi[\bar b]\iff B\models\varphi[\bar b]`$。

構成は次のとおり。 $`H_0=\emptyset`$。 $`H_{\alpha+1}`$ は、 $`H_\alpha`$ に、 $`H_\alpha`$ の元の組への各演算の値と、各 $`\exists\bar y\,\psi\in\Phi_S`$ と $`H_\alpha`$ の元の各組 $`\bar b`$ で $`B\models\exists\bar y\,\psi[\bar b]`$ となるものの証人を一組ずつ加えたものとする。極限では合併を取り、 $`H=H_\chi`$ と置く。各段階で加える元は $`\mu_A\cdot\mu_A^{<\chi}\cdot\chi=\mu_A`$ 個以下である。 $`\chi`$ が正則なので、 $`H`$ の元の長さ $`<\chi`$ の組はある段階に含まれる。(c) は補題 2.1 と同じ帰納法で示す。原子式の場合は、(b) により $`H|_G`$ が $`B`$ の $`\Sigma_G`$-部分構造であることから従う。

**冪への埋め込み。** 各 $`b\in H_s`$ について、代表の全域関数 $`r_b\colon I\to A_s`$ を選ぶ。 $`\Sigma_A^+`$ の各演算記号 $`o`$ と、その項数に合う $`H`$ の元の各組 $`\bar b=(b_k)_k`$ について

```math
I_{o,\bar b}=\{\,i\in I\mid o\bigl((r_{b_k}(i))_k\bigr)=r_{o(\bar b)}(i)\,\}
```

と置く。 $`B^+`$ の演算の定義から $`I_{o,\bar b}\in F`$ である。対 $`(o,\bar b)`$ は $`\mu_A\cdot\mu_A^{<\chi}=\mu_A`$ 個以下なので、 $`F`$ の $`\mu_A^+`$-完備性から

```math
J:=\bigcap_{(o,\bar b)}I_{o,\bar b}\in F
```

であり、 $`F`$ が固有なので $`J\neq\emptyset`$ である。

$`\iota\colon H\to(A^+)^J`$ を $`\iota(b)=r_b|_J`$ で定める。

- $`J`$ の定義から、 $`\iota`$ は $`\Sigma_A^+`$ のすべての演算と可換である。ゆえに $`\iota(H)`$ は $`(A^+)^J`$ の部分代数である。
- $`\iota`$ は単射である。 $`r_b|_J=r_{b'}|_J`$ なら、 $`r_b`$ と $`r_{b'}`$ は $`J\in F`$ の上で一致し、 $`b=b'`$ となる。

したがって $`H|_G\cong\iota(H)|_G`$ であり、補題 3.1 から $`H|_G\in\mathcal D`$、すなわち $`H|_G\models S`$ である。(c) により $`B\models S`$、すなわち $`A^I/F\in\mathcal D`$。∎

## 5. 被約積と完備度の一様化

この節は [§4 の補題の文書](section4_reduced_products_and_ranked_types.md) の内容を含む。

### 5.1 ランク付き往復型

$`L_\chi(\Sigma_G)`$ の式の**量化ランク** $`\mathrm{qr}`$ を次で定める。原子式は $`0`$。 $`\mathrm{qr}(\neg\varphi)=\mathrm{qr}\,\varphi`$。連言・選言は成分の上限。 $`\mathrm{qr}(\exists\bar y\,\varphi)=\mathrm{qr}\,\varphi+1`$。

$`\Sigma_G`$-構造 $`A`$ と、形 $`\bar s`$ の組 $`\bar a`$ に対し、 $`\mathrm{tp}_\beta(A,\bar a)`$ を順序数 $`\beta`$ に関する再帰で定める。

- $`\mathrm{tp}_0(A,\bar a)`$ は、形 $`\bar s`$ の変数に関する原子式のうち、 $`A`$ で $`\bar a`$ が満たすもの全体の集合。
- $`\mathrm{tp}_{\beta+1}(A,\bar a)`$ は対 $`(\mathrm{tp}_\beta(A,\bar a),\,\Xi)`$。ここで $`\Xi`$ は、各形 $`\bar s'`$ に集合 $`\{\mathrm{tp}_\beta(A,\bar a\bar c)\mid\bar c\in A^{\bar s'}\}`$ を対応させる関数。
- 極限順序数 $`\beta`$ では $`\mathrm{tp}_\beta(A,\bar a)=(\mathrm{tp}_\gamma(A,\bar a))_{\gamma<\beta}`$。

定義から次が従う。

- (T1) $`\gamma\le\beta`$ のとき、 $`\mathrm{tp}_\beta`$ が等しければ $`\mathrm{tp}_\gamma`$ も等しい。
- (T2) $`\mathrm{tp}_{\gamma+1}(A,\bar a)=\mathrm{tp}_{\gamma+1}(B,\bar b)`$ とする。任意の形 $`\bar s'`$ と $`\bar c\in A^{\bar s'}`$ に対し、 $`\mathrm{tp}_\gamma(A,\bar a\bar c)=\mathrm{tp}_\gamma(B,\bar b\bar d)`$ となる $`\bar d\in B^{\bar s'}`$ がある。 $`A`$ と $`B`$ を入れ替えても同じである。

**補題 5.1。** 形 $`\bar s`$ と $`\beta`$ を固定すると、すべての $`(A,\bar a)`$ にわたる $`\mathrm{tp}_\beta(A,\bar a)`$ の値は一つの集合 $`\mathbb T_\beta(\bar s)`$ に収まる。

*証明。* $`\beta`$ に関する帰納法を、すべての形について同時に行う。 $`\mathbb T_0(\bar s)`$ は原子式の集合の冪集合に取れる。 $`\mathbb T_{\beta+1}(\bar s)`$ は $`\mathbb T_\beta(\bar s)\times\prod_{\bar s'}\mathcal P(\mathbb T_\beta(\bar s\bar s'))`$ に取れる。形の全体は集合である。極限では直積を取る。∎

### 5.2 Feferman–Vaught 型の補題

**補題 5.2。** $`F`$ を $`I`$ 上の固有な $`\chi`$-完備フィルターとし、 $`(A_i)_{i\in I}`$、 $`(B_i)_{i\in I}`$ を $`\Sigma_G`$-構造の族とする。 $`\bar a=([f_k])_{k<\ell}`$ と $`\bar b=([g_k])_{k<\ell}`$ を、それぞれ $`\prod^FA_i`$ と $`\prod^FB_i`$ の同じ形の組とする（ $`\ell<\chi`$ ）。ある $`X\in F`$ と順序数 $`\beta`$ について

- $`X\subseteq\bigcap_k(\mathrm{dom}f_k\cap\mathrm{dom}g_k)`$
- すべての $`i\in X`$ で $`\mathrm{tp}_\beta(A_i,(f_k(i))_k)=\mathrm{tp}_\beta(B_i,(g_k(i))_k)`$

が成り立つとする。このとき、 $`\mathrm{qr}\,\varphi\le\beta`$ となるすべての $`\varphi\in L_\chi(\Sigma_G)`$ について

```math
\textstyle\prod^FA_i\models\varphi[\bar a]\iff\prod^FB_i\models\varphi[\bar b].
```

*証明。* $`\varphi`$ の構成に関する帰納法による。帰納法の主張は、すべての $`\beta\ge\mathrm{qr}\,\varphi`$、すべての族と組について同時に述べる。

- *原子式* $`m(x_k)=m'(x_l)`$。演算は座標ごとなので、 $`\prod^FA_i`$ で成り立つことは

  ```math
  Z_A=\{\,i\in\mathrm{dom}f_k\cap\mathrm{dom}f_l\mid A_i\models m(f_k(i))=m'(f_l(i))\,\}\in F
  ```

  と同値である。 $`Z_B`$ も同様に定める。(T1) により $`X`$ 上で $`\mathrm{tp}_0`$ が一致するので $`Z_A\cap X=Z_B\cap X`$。 $`X\in F`$ だから $`Z_A\in F\iff Z_B\in F`$。
- *否定・連言・選言。* 部分式の量化ランクは $`\le\beta`$ なので、同じ $`\bar a,\bar b,X,\beta`$ で帰納法の仮定を使い、被約積の水準でブール結合を取る。
- *存在量化* $`\varphi=\exists\bar y\,\psi`$。 $`\gamma=\mathrm{qr}\,\psi`$ と置くと $`\gamma+1\le\beta`$ で、(T1) により $`X`$ 上で $`\mathrm{tp}_{\gamma+1}`$ が一致する。 $`\prod^FA_i\models\psi[\bar a,\bar c]`$ となる $`\bar c=([h_m])_m`$ を取り、 $`Y=X\cap\bigcap_m\mathrm{dom}h_m`$ と置く。 $`\chi`$-完備性から $`Y\in F`$。各 $`i\in Y`$ で、(T2) により

  ```math
  \mathrm{tp}_\gamma\bigl(A_i,\bar a(i)\bar c(i)\bigr)=\mathrm{tp}_\gamma\bigl(B_i,\bar b(i)\bar d(i)\bigr)
  ```

  となる $`\bar d(i)`$ を選ぶ（選択公理）。 $`Y`$ 上の部分切断 $`e_m(i)=\bar d(i)_m`$ から $`\bar d=([e_m])_m`$ を作る。 $`\bar a\bar c`$ と $`\bar b\bar d`$ は、 $`Y`$ とランク $`\gamma`$ について補題の仮定を満たすので、帰納法の仮定から $`\prod^FB_i\models\psi[\bar b,\bar d]`$。逆向きも同様である。∎

補題 5.2 は二つの被約積を比べる主張であり、式の真偽が座標ごとに決まるとは言っていない。否定を被約積の水準で取るのはそのためである。

### 5.3 セルへの分解

$`F`$ を $`I`$ 上の固有フィルターとする。補集合が $`F`$ に属する集合を**零集合**という。 $`I'\subseteq I`$ が零集合でないとき、

```math
F|_{I'}=\{\,Y\subseteq I'\mid Y\cup(I\setminus I')\in F\,\}
```

を $`I'`$ 上の**跡**という。

**補題 5.3。** $`F`$ を固有な $`\kappa`$-完備フィルターとし、 $`I=\bigsqcup_{t\in\mathbb T}I_t`$ を $`|\mathbb T|<\kappa`$ 個の部分への分割とする。 $`\mathbb T^*`$ を、 $`I_t`$ が零集合でない $`t`$ の全体とする。

1. $`t\in\mathbb T^*`$ のとき、 $`F_t:=F|_{I_t}`$ は $`I_t`$ 上の固有な $`\kappa`$-完備フィルターである。
2. 制限による写像

   ```math
   \textstyle r\colon\prod^F_{i\in I}A_i\longrightarrow\prod_{t\in\mathbb T^*}\ \prod^{F_t}_{i\in I_t}A_i,\qquad[f]\mapsto\bigl([f|_{\mathrm{dom}f\cap I_t}]\bigr)_t
   ```

   は $`\Sigma_G`$-構造の同型である。

*証明。* (1) $`\emptyset\in F_t`$ は $`I_t`$ が零集合であることと同値なので、 $`F_t`$ は固有である。 $`\bigcap_j(Y_j\cup(I\setminus I_t))=(\bigcap_jY_j)\cup(I\setminus I_t)`$ から $`\kappa`$-完備性が従う。

(2) まず、各 $`t\in\mathbb T^*`$ に $`Y_t\in F_t`$ が与えられたとき $`\bigcup_tY_t\in F`$ であることを示す。その補集合は

```math
\textstyle\bigcup_{t\in\mathbb T^*}(I_t\setminus Y_t)\ \cup\ \bigcup_{t\notin\mathbb T^*}I_t
```

に含まれる。これは $`<\kappa`$ 個の零集合の和であり、零集合の全体は $`\kappa`$-完備なイデアルなので、零集合である。

- *定義できること。* $`\mathrm{dom}f\in F`$ なら $`\mathrm{dom}f\cap I_t\in F_t`$ である。 $`f\sim f'`$ なら制限どうしも同値である。
- *単射。* $`r[f]=r[f']`$ なら、各 $`t\in\mathbb T^*`$ で $`f,f'`$ がある $`Y_t\in F_t`$ の上で一致する。上の事実から $`\bigcup_tY_t\in F`$ の上で一致する。
- *全射。* 各 $`t\in\mathbb T^*`$ に $`Y_t\in F_t`$ 上の部分切断 $`f_t`$ が与えられたとき、貼り合わせ $`f=\bigcup_tf_t`$ の定義域は $`F`$ に属し、 $`r[f]=([f_t])_t`$。
- *準同型。* 単項演算は両辺で座標ごとに作用する。全単射で演算と可換なので同型である。∎

### 5.4 一様な完備度

**系 5.4。** ある正則基数 $`\kappa`$ があって、 $`\mathcal D`$ の対象の任意の族 $`(A_i)_{i\in I}`$（ $`I\neq\emptyset`$ ）と、 $`I`$ 上の任意の固有な $`\kappa`$-完備フィルター $`F`$ について $`\prod^FA_i\in\mathcal D`$ となる。

*証明。* $`\alpha=\sup\{\mathrm{qr}\,\sigma\mid\sigma\in S\}`$ と置く。補題 5.1 により、空の組の型の集合 $`\mathbb T:=\mathbb T_\alpha(\emptyset)`$ がある。 $`\mathcal D`$ の対象で実現される各 $`t\in\mathbb T`$ について、 $`\mathrm{tp}_\alpha(A(t),\emptyset)=t`$ となる $`A(t)\in\mathcal D`$ を一つ選ぶ。 $`t`$ を実現する $`\mathcal D`$ の対象のうち集合論的ランクが最小のもの全体は集合なので、これは集合の族からの選択である。正則基数 $`\kappa`$ を

```math
\kappa>\chi,\qquad\kappa>|\mathbb T|,\qquad\forall t\ \ \kappa\ge\kappa_{A(t)}
```

となるように取る（ $`\kappa_{A(t)}`$ は補題 4.1 の基数）。 $`\kappa`$ は族にも $`F`$ にもよらない。

族 $`(A_i)`$ と $`F`$ が与えられたとする。 $`I_t=\{i\mid\mathrm{tp}_\alpha(A_i,\emptyset)=t\}`$ と置くと、 $`I`$ は $`<\kappa`$ 個の部分に分割される。補題 5.3 により

```math
\textstyle\prod^FA_i\ \cong\ \prod_{t\in\mathbb T^*}\ \prod^{F_t}_{i\in I_t}A_i.
```

$`t\in\mathbb T^*`$ を固定する。 $`F_t`$ は固有で $`\kappa`$-完備、特に $`\chi`$-完備である。補題 5.2 を、 $`I_t`$ 上の二つの族 $`(A_i)_{i\in I_t}`$ と定数族 $`(A(t))_{i\in I_t}`$、空の組、 $`X=I_t`$、 $`\beta=\alpha`$ に適用すると、すべての $`\sigma\in S`$ について

```math
\textstyle\prod^{F_t}_{i\in I_t}A_i\models\sigma\iff\prod^{F_t}_{i\in I_t}A(t)\models\sigma.
```

右辺の構造は、注意 1.4 により被約冪 $`A(t)^{I_t}/F_t`$ と同型である。 $`I_t\neq\emptyset`$ で、 $`F_t`$ は $`\kappa_{A(t)}`$-完備なので、補題 4.1 からこれは $`\mathcal D`$ に属し、 $`S`$ を満たす。ゆえに $`\prod^{F_t}_{i\in I_t}A_i\models S`$、すなわち $`\mathcal D`$ に属する。 $`\mathcal D`$ は積で閉じるので、 $`\prod^FA_i\in\mathcal D`$。∎

## 6. 有向余極限を等化子として表す

**命題 6.1。** $`\kappa`$ を系 5.4 の基数とする。 $`I`$ を $`\kappa`$-有向な半順序集合、 $`(D_i,d_{ij}\colon D_i\to D_j)_{i\le j}`$ を $`\mathcal D`$ の図式、 $`(b_i\colon D_i\to B)`$ をその $`\mathrm{Set}^{G^{op}}`$ での余極限とする。このとき $`B\in\mathcal D`$ である。

*証明。* 前層圏の有向余極限はソートごとに計算される。 $`B`$ の各元は $`b_i(x)`$ の形をしており、 $`b_i(x)=b_{i'}(x')`$ は、ある $`k\ge i,i'`$ で $`d_{ik}(x)=d_{i'k}(x')`$ となることと同値である。

**フィルター。** $`{\uparrow}i=\{j\in I\mid j\ge i\}`$ と書き、

```math
F=\{\,X\subseteq I\mid\exists i\in I\ \ {\uparrow}i\subseteq X\,\}
```

と置く。 $`{\uparrow}i\neq\emptyset`$ なので $`F`$ は固有である。 $`I`$ が $`\kappa`$-有向なので、 $`<\kappa`$ 個の $`{\uparrow}i_\alpha`$ の共通部分は、 $`i_\alpha`$ たちの上界 $`k`$ の $`{\uparrow}k`$ を含む。ゆえに $`F`$ は $`\kappa`$-完備なフィルターである。

系 5.4 により

```math
\textstyle R:=\prod^F_{i\in I}D_i\in\mathcal D,\qquad Q:=\prod^F_{i\in I}R\in\mathcal D
```

である（ $`Q`$ は $`R`$ の定数族の被約積）。

**射 $`e\colon B\to R`$。**

```math
e(b_i(x))=[\,j\mapsto d_{ij}(x)\ \ (j\in{\uparrow}i)\,]
```

と置く。

- *代表によらないこと。* $`b_i(x)=b_{i'}(x')`$ なら、ある $`k`$ について $`{\uparrow}k`$ の上で $`d_{ij}(x)=d_{i'j}(x')`$。
- *単射。* $`e(b_i(x))=e(b_{i'}(x'))`$ なら、二つの切断は $`F`$ のある元の上で一致する。その元は空でないので、ある $`j\ge i,i'`$ で $`d_{ij}(x)=d_{i'j}(x')`$、すなわち $`b_i(x)=b_{i'}(x')`$。
- *準同型。* $`d_{ij}`$ と $`b_i`$ が準同型で、 $`R`$ の演算は座標ごとだからである。

**射 $`p,q\colon R\rightrightarrows Q`$。**

```math
p(r)=[\,i\mapsto r\ \ (i\in I)\,],\qquad q([f])=[\,i\mapsto e(b_i(f(i)))\ \ (i\in\mathrm{dom}f)\,].
```

$`q`$ は代表によらない： $`f\sim f'`$ が $`X\in F`$ の上で一致するなら、対応する切断も $`X`$ の上で一致する。 $`p,q`$ が準同型であることは、 $`e`$ と $`b_i`$ が準同型であることから従う。

**$`e(B)`$ は $`p,q`$ の等化子である。**

- $`r=e(b_j(x))`$ とする。 $`r`$ の代表として $`f(i)=d_{ji}(x)`$（ $`i\in{\uparrow}j`$ ）が取れる。 $`i\in{\uparrow}j`$ について $`e(b_i(f(i)))=e(b_i(d_{ji}(x)))=e(b_j(x))=r`$。ゆえに $`q(r)`$ と $`p(r)`$ は $`{\uparrow}j\in F`$ の上で一致する代表を持ち、 $`p(r)=q(r)`$。
- 逆に $`r=[f]`$ が $`p(r)=q(r)`$ を満たすとする。ある $`X\in F`$、 $`X\subseteq\mathrm{dom}f`$ について、すべての $`i\in X`$ で $`r=e(b_i(f(i)))`$ となる。 $`X\neq\emptyset`$ なので $`r\in e(B)`$。

前層圏の等化子はソートごとの等化子なので、 $`p,q`$ の等化子は部分前層 $`e(B)`$ である。 $`R,Q\in\mathcal D`$ と (B1) から $`e(B)\in\mathcal D`$。 $`e`$ は単射な準同型で、署名は演算だけなので、 $`B\cong e(B)`$ である。 $`\mathcal D`$ は同型で閉じるので $`B\in\mathcal D`$。∎

## 7. 証明の完結

**定理 B の証明。** 命題 6.1 により、 $`\mathcal D`$ は $`\mathrm{Set}^{G^{op}}`$ の中で $`\kappa`$-有向余極限で閉じる。(B1) により小極限でも閉じる。前層圏 $`\mathrm{Set}^{G^{op}}`$ は局所有限可呈示であり（原著の例 1.12）、したがって局所 $`\kappa`$-可呈示である（定理 1.20 の後の注意）。原著の定理 2.48 の系

> Every full subcategory of a locally λ-presentable category closed under limits and λ-directed colimits is locally λ-presentable.

により、 $`\mathcal D`$ は局所 $`\kappa`$-可呈示である。∎

**定理 A の証明。** §2.5 と定理 B による。∎

## 8. 補足

### 8.1 基数を選ぶ順序

どの基数が何に依存するかを、選ぶ順にまとめる。

1. $`T`$ と $`\Sigma`$ から $`\lambda`$、 $`\nu`$、 $`\mu=2^\nu`$（§2）。
2. $`\mu`$ から $`G`$、タグ、公理系 $`S`$、 $`\chi`$（§2.4）。
3. 各 $`A\in\mathcal D`$ について、補題 3.1 の $`\tau,\rho,\delta`$ と集合 $`U`$。これらは補題 3.1 の証明の中だけで使う。
4. 各 $`A\in\mathcal D`$ について $`\mu_A`$ と $`\kappa_A=\mu_A^+`$（補題 4.1）。
5. $`S`$ の量化ランクの上限 $`\alpha`$、型の集合 $`\mathbb T`$、代表 $`A(t)`$、そして一様な $`\kappa`$（系 5.4）。
6. $`\kappa`$ を固定した後で、任意の $`\kappa`$-有向図式を取る（命題 6.1）。

### 8.2 仮定を使う箇所

- **公理化可能性**は三か所で使う。小さいモデルの稠密性（補題 2.1・2.2）、 $`W\models S`$ から $`W\in\mathcal D`$ を得るところ（補題 3.1 の段階 1）、初等部分代数から被約冪に $`S`$ を移すところ（補題 4.1）。
- **完備性**は (B1) として使う。冪 $`A^E`$ と $`W^{\mathrm{Sym}(U)}`$、同時等化子 $`K`$（補題 3.1）、セルにわたる積（系 5.4）、等化子 $`e(B)`$（命題 6.1）である。
- **前層の署名が単項演算だけであること**は、記述を簡単にするために使う。原子式が $`m(x)=m'(y)`$ の形になり（§1.5）、被約積の演算の定義にフィルターの完備性が要らない（§1.4）。

### 8.3 点検に使った例

証明の中間の主張が強すぎないかを、次の例で確かめた。いずれも矛盾しなかった。

- **$`\mathrm{Set}^{op}`$ 型の類。** $`\Omega`$ を無限集合（例えば $`\omega`$ ）とする。可測基数がないとき、 $`M=\mathrm{End}(\Omega)`$ の作用する集合のうち $`\Omega^X`$ と同型なもの全体は、 $`M`$-集合の圏の小極限で閉じ、 $`\mathrm{Set}^{op}`$ と同値である。$`J`$ が十分大きいとき、「濃度 $`<\chi`$ の集合の外で定数」である関数 $`J\to\Omega`$ 全体 $`H`$ は $`\Omega^Y`$ の形にならない。したがって補題 3.1 により、この類はどの $`L_\chi`$ でも公理化できない。これは局所可呈示でないことと整合する。
- **$`A_t\cong A_s^{\omega_1}`$ で定まる類**（射影 $`\pi_\alpha\colon t\to s`$ を持つ前層）。 $`\chi=\omega_1`$ で $`J`$ が非可算のとき、可算集合の外で定数である関数全体が補題 3.1 の $`H`$ になり、類に属さない。この類を公理化するには $`\omega_1`$ 個の変数の量化が要るので、これも整合する。
- **極限理論のモデル。** $`\forall\bar x(\varphi\to\exists!\bar y\,\psi)`$ の形の公理では、一意な証人を与える写像が $`\Sigma_A^+`$ の演算なので、 $`H`$ は確かに類に属する。

### 8.4 この証明が示さないこと

- 等化子だけを持つ公理化可能な圏については何も示さない。補題 3.1 は任意の冪と同時等化子を、系 5.4 は積を使う。
- 局所可呈示性のランクの具体的な上界は与えない。 $`\kappa`$ は $`\kappa_{A(t)}`$ の上限として選ばれる。
- 新規性は主張しない。文献調査は終わっていない。

### 8.5 草稿からの主な変更点

- 定理 B を独立した主張として切り出した。
- §2 の公理を (S0)–(S5) として列挙し、翻訳の補題 2.4・2.5 を証明した。
- 補題 3.1 で $`\chi\le\delta`$ を明示し、例外の個数を $`D_1,D_2`$ に分けて数えた。
- 補題 4.1 で $`\mu_A\ge|\Sigma_A^+|`$ を明示した。
- 真クラスからの選択になる三か所（ $`G`$ の対象、命題 2.3 (3) の $`X_j`$、系 5.4 の $`A(t)`$ ）を、集合からの選択に直した。
- 草稿 §1（No.11 の図式の計算）、§4.1（商ブール代数による別証）、§6 後半（可呈示対象の直接構成と No.11 への帰結）は含めていない。

### 8.6 検証するときに見る順番

1. **補題 3.1。** 証明の新しい部分はここにある。特に主張 2 で、 $`\bar w'`$ の成分が $`W`$ に属することの確認。
2. **命題 2.6。** 公理系 $`S`$ が本質像を正確に切り出すこと。
3. **補題 4.1。** 初等部分代数を冪に埋め込むところ。
4. 残り（§5・§6）は標準的な議論である。
