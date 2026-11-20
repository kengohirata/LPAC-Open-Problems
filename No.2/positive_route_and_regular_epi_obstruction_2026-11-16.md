# Problem 2(b)：肯定方向の第一段階と regular epi への還元の障害

2026年11月16日。状態：`PROOF_RECONSTRUCTED`。以下は今回の直接証明・構成であり、独立査読・形式検証・文献上の新規性確認はしていない。No.1 の主定理は本プロジェクトの確立済み入力として使用し、再証明・再監査を目的としない。

## 0. 研究目標と今回の到達点

目標は Adámek–Rosický の Open Problem 2(b)：任意の locally presentable category K の任意の ordinary coorthogonality class A が、K の二つの full coreflective subcategories の交わりとして表せるか、である。テストのクラスは集合に限定しない。

今回、一般肯定証明は完成していない。しかし、以下を直接示した。

1. 任意のテストを strong epi–mono 分解すると、coorthogonality class を二つの coorthogonality classes の交わりに分解でき、mono 側は常に monocoreflective。
2. 残った strong epi 側も常に coreflective、とする補題は使えない。No.1 の母圏を「第0成分が有限支持」の図式に制限すると、なお locally presentable であり、N の下で一本の regular epi の coorthogonality class が非 coreflective になる。
3. この新しい母圏では、No.1 のサイズ下界は H(p) の全単射性ではなく、全射性だけで成立する。したがって A を含む coreflective subcategory は、必ず存在条件に不合格の対象を含む。
4. 一方、有限像の列による小さい対象 P と P→B を ZFC で明示でき、すべての A-対象からの Hom は全単射になる。ただし P 自身は A に入らない。失敗は非主的 ultrafilter に対応する持ち上げの不存在である。
5. P に座標を一つ加えて一意性も失敗させる単純な修正では、B 上の非自明な自己同型が現れる。その修正した射も coreflection にはできない。

2、3、5 は特定の肯定構成の障害であって、Problem 2(b) の否定ではない。

## 1. 一般の肯定構成：テストの strong epi–mono 分解

K を locally presentable とし、Σ を射のクラスとする。f:U→V の strong epi–mono 分解を

    U --e_f--> I_f --m_f--> V

とする。任意の X に対し Hom(X,m_f) は単射である。

**命題 1（ZFC）。**

\[
X\perp f\quad\Longleftrightarrow\quad X\perp e_f\ \text{かつ}\ X\perp m_f.
\]

**証明。** Hom(X,f)=Hom(X,m_f)Hom(X,e_f)。左辺の合成が全単射なら、Hom(X,m_f) は全射でもあるため全単射。その逆写像との合成により Hom(X,e_f) も全単射になる。逆は自明。□

したがって

\[
{}^\perp\Sigma={}^\perp\{e_f\}\cap{}^\perp\{m_f\}.
\]

Σ が proper class の場合、クラス全体について代表分解を選ぶ代わりに、各 f のすべての strong epi–mono 分解に現れる e と m を使ってよい。クラス選択を新たに仮定する必要はない。

**命題 2（ZFC）。** 任意の mono のクラス M に対し、C={}^⊥M は monocoreflective である。

**証明。** C は小余極限に閉じる。また q:X→Q が strong epi、X∈C なら Q∈C である。実際、mono m:U→V と b:Q→V に対し、bq は X∈C により U に持ち上がる。その持ち上げと q,m の可換四角を strong epi–mono の対角性で埋めれば、b が U に一意に持ち上がる。

固定した B について、K は well-powered なので、C に属する B の部分対象は同型を除いて集合個である。その余積の B への strong image R(B)↪B を取る。小余極限閉性と strong quotient 閉性から R(B)∈C。任意の X∈C から B への射の strong image も、この集合に現れる。したがって X→B は R(B) を経由し、R(B)→B が mono なので因子化は一意。□

この証明は、No.1 の `investigations/list_colouring_independence_2026-11-15.md` §2.1 の trace 論法を、任意の mono のクラスに用いたもの。

よって、肯定方向としては「mono 側は完成、strong epi 側の coreflectivity が残る」というところまで一般に進める。ただし次節は、strong epi 側が常に coreflective という追加補題そのものを否定する。

## 2. 有限支持を母圏に組み込むと、一本の regular epi が残る

No.1 と同じく

\[
\Omega=\omega,\quad M=\operatorname{End}(\Omega),\quad
\mathcal D=(M\text{-}\mathbf{Set})^{(0\rightrightarrows1)},
\quad H(A)=\operatorname{Hom}_M(A,\Omega)
\]

とする。今回の母圏を

\[
\mathcal K_{fs}=\{Z=(Z_0\rightrightarrows Z_1)\in\mathcal D:
Z_0\text{ の全元が有限支持を持つ}\}
\]

という充満部分圏に変更する。第1成分には有限支持を要求しない。

### 2.1 K_fs は locally presentable

**補題 3（ZFC）。** K_fs は locally presentable。包含 K_fs→D はすべての小余極限を作る。

**証明。** 有限支持の元は M-射で有限支持の元に送られる。また、部分対象では有限支持性が継承される。D の余極限は成分ごとの余積の商として計算されるので、第0成分の有限支持性は小余極限で保存される。従って K_fs は余完備で、余極限は D で計算される。

無限基数 μ≥|M| を固定し、λ=μ^+ とする。D は二つの sort と、集合個（高々 μ 個）の unary operations（M の各作用、p、q）および等式で記述される。

総台集合のサイズが μ 以下の D-対象は λ-presentable である。直接には、λ-filtered colimit への写像を指定する高々 μ 個の元の像と、高々 μ 個の自然性・作用保存等式を、一つの段階に集められる。二つの因子化が等しいことも、高々 μ 個の元ごとの一致を一つの段階に集めて判定できる。K_fs の λ-filtered colimit は D で計算されるため、こうした対象が K_fs に属すれば K_fs でも λ-presentable である。

任意の Z∈K_fs は、総台集合のサイズが μ 以下の部分図式の λ-filtered union である。高々 μ 個の元から生成した部分図式には、作用と p,q を適用しても高々 μ 個しか元がない。また高々 μ 個の小部分図式は、その和集合から生成した同サイズの部分図式に含まれる。各部分図式は Z_0 の部分 M-set を第0成分に持つため K_fs に残る。

このサイズの対象の同型類は集合をなす。従って K_fs は λ-accessible かつ cocomplete、すなわち locally presentable。□

有限支持性を finitary variety の公理で表したと主張しているわけではない。ここで使ったのは、余極限閉性、部分対象閉性、および十分大きい λ における生成元・関係式のサイズ評価である。

### 2.2 σ は K_fs の regular epi

\[
U=(\Omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\Omega),\qquad
B=(\Omega\rightrightarrows1),\qquad
\sigma=(\pi_0,!):U\longrightarrow B.
\]

Ω と Ω² は有限支持 M-set なので U,B∈K_fs。

σ は D において成分ごとの全射。その kernel pair は、第0成分が Ω³、第1成分が Ω² であり、K_fs に属する。K_fs の coequalizer は D で計算されるので、σ は K_fs でもその kernel pair の coequalizer、従って regular epi である。

No.1 の Hom 計算を、そのまま充満部分圏 K_fs 内で使うと

\[
\mathcal A={}^\perp_{\mathcal K_{fs}}\{\sigma\}
=\{Z\in\mathcal K_{fs}:H(p_Z)\text{ が全単射}\}.
\]

これは、D 内では二つのテスト τ,σ を用いていた No.1 の A と同一の対象・射を持つ。

**定理 4（ZFC+N、No.1 からの帰結）。** K_fs は locally presentable、σ はその一本の regular epi だが、{}^⊥_{K_fs}{σ} は coreflective でない。N は非可算可測基数が存在しないという仮定。

**証明。** No.1 の固定標的 B は K_fs に属する。A、B およびすべての因子化の Hom は D でも K_fs でも同じ。No.1 で得た A↓B の弱終集合の不存在が、そのまま K_fs 内でも成立する。□

従って、§1 の strong epi 側を単に coreflective と主張する構成は失敗する。しかもテストが proper class だから失敗するのではなく、一本の regular epi で既に失敗する。

## 3. 「存在条件だけ」でも同じサイズ障害が残る

\[
\mathcal J=\{Z\in\mathcal K_{fs}:H(p_Z)\text{ が全射}\}
\]

と置く。これは coorthogonality class と主張しない。一意性を課さない存在条件だけのクラスである。

No.1 の試験対象を再利用する。無限基数 κ に対し、X_κ=[0,κ]、d_κ は後続操作（κ は固定）、C(X)=Cont(X,Ω_disc)、F(X)=Ω^X とし、

\[
Y_\kappa=(C(X_\kappa)\overset{i,d_\kappa^*}{\rightrightarrows}F(X_\kappa)),
\qquad \psi_\kappa:Y_\kappa\longrightarrow B
\]

を、基点0での評価で定める。N の下で Y_κ∈A は No.1 の入力である。

**補題 5（ZFC+N）。** 因子化

\[
Y_\kappa\xrightarrow{a}Z\xrightarrow{b}B,
\qquad Z\in\mathcal J,\quad ba=\psi_\kappa
\]

があれば、H(Z_0) から X_κ への連続全射がある。従って κ≤|H(Z_0)|。

**証明。** T=H(Z_0)、S=H(Z_1)、u=H(p_Z)、v=H(q_Z) とする。No.1 の双対表示の下で a は

\[
h:T\to X_\kappa,\qquad \ell:S\to X_\kappa,
\qquad hu=\ell,\quad hv=d_\kappa\ell
\]

を与える。h は連続である。

u の単射性は不要である。任意の t∈T に対し、全射性から u(s)=t となる s を一つ取ると

\[
d_\kappa(h(t))=d_\kappa(\ell(s))=h(v(s))\in h(T).
\]

よって h(T) は d_κ-不変。Z_0 が有限支持なので T はコンパクト、従って h(T) は閉。B 上の条件から0を含む。後続段階を不変性、極限段階を閉性で進める超限帰納法により h(T)=X_κ。□

**系 6（ZFC+N）。** C を K_fs の full coreflective subcategory で A⊆C を満たすものとする。B の C-coreflection ε:T→B では、H(p_T) は全射でない。

**証明。** すべての ψ_κ は ε を経由する。H(p_T) が全射なら、補題5によってすべての κ に対し κ≤|H(T_0)| となり矛盾する。□

従って A⊆C⊆J を満たす coreflective C は存在しない。

特に A=C_0∩C_1 という表示が K_fs 内に存在するなら、両方の C_i が存在条件を満たさない対象を含まなければならない。これはその表示の不存在を示さない。

## 4. 肯定構成を実行：すべての合格対象からの Hom を受ける有限像列

ここからこの節の構成自体には N を仮定しない。

M=Ω^ω と同定し、

\[
M_{fin}=\{f:\omega\to\Omega:\operatorname{im}(f)\text{ が有限}\}
\]

とする。これは正則左 M-set M の有限支持部分である。有限像は支持になり、逆に支持の外に像の元があれば、その値だけを動かす自己写像で支持性が破れる。

j:M_fin→M を包含、t:M→M を shift、t(f)(n)=f(n+1) として

\[
P=(M_{fin}\overset{j,tj}{\rightrightarrows}M),
\qquad \varepsilon=(\operatorname{ev}_0,!):P\longrightarrow B
\]

を取る。P∈K_fs。

**命題 7（ZFC）。** 任意の Z∈A に対し

\[
\mathcal K_{fs}(Z,P)\xrightarrow{\varepsilon\circ-}
\mathcal K_{fs}(Z,B)
\]

は全単射。

**証明。** b:Z→B を取って h_0=b_0 とし、H(p_Z) の全単射性を使って一意に

\[
\ell_n p_Z=h_n,\qquad h_{n+1}=\ell_n q_Z
\]

を定める。a_0(z)(n)=h_n(z)、a_1(w)(n)=ℓ_n(w) と置く。

z∈Z_0 の有限支持 S_z を取る。各 h_n は M-射なので h_n(z)∈S_z。従って a_0(z) は有限像であり、a_0 は M_fin に値を持つ。a_1 は M に値を持つ。それぞれ座標ごとに同変であり、再帰式から

\[
ja_0=a_1p_Z,\qquad tja_0=a_1q_Z,\qquad
\operatorname{ev}_0a_0=b_0.
\]

よって唯一の図式の射 a:Z→P を得る。一意性は同じ座標再帰と H(p_Z) の単射性による。右辺 Hom が空なら、左辺の射から ε との合成で右辺の射が得られるため左辺も空。□

これは A-対象から見た普遍性を完全に満たす。しかし coreflection には追加で P∈A が必要であり、それが成立しない。

### 4.1 どの所属条件が失敗するか

正則左作用から

\[
H(M)\cong\omega,\qquad n\leftrightarrow\operatorname{ev}_n.
\]

一方、H(M_fin) は ω 上のすべての ultrafilter と対応する。ultrafilter U は、各有限像写像 f について U に属する唯一の fibre の値を返す写像 h_U を与える。これは M-同変である。

逆に h:M_fin→Ω から特性関数の値で ultrafilter を回収する。補集合との整合性は0と1を交換する自己写像、有限交叉との整合性は有限個の値を Ω に符号化して座標射・論理積を後合成することで得る。一般の有限像 f の値は、その選ばれた fibre によって決まる。

この同定の下で

\[
H(j):\omega\hookrightarrow\operatorname{Ult}(\omega)
\]

は主 ultrafilter の包含である。ZFC では非主的 ultrafilter が存在するため、これは単射だが全射でない。例えば非主的 U による h_U は、各 n に対して χ_{\{n\}} の値が0であり、eval_n と異なる。

従って P∉A。ただし P は一意性だけのクラス

\[
\mathcal I=\{Z\in\mathcal K_{fs}:H(p_Z)\text{ が単射}\}
\]

には属する。

この節の ultrafilter は有限分割だけを選ぶ通常の ultrafilter であり、可算完備性を要求しない。したがって N の下でも非主的 ultrafilter は存在し、No.1 の Isbell 表示との矛盾はない。

### 4.2 前の No.2 の構成との関係

既存ノート `sigma_coreflectivity_2026-11-16.md` §2 の

\[
C=(M\overset{1,t}{\rightrightarrows}M)\longrightarrow B
\]

は D における A_sigma-coreflection である。この C の第0成分を有限支持部分に制限したものが P である。

したがって、「D で coreflect してから有限支持部分へ戻す」操作は、A-対象からの Hom を保存するが、H(p) の全射性を失う。単なる普遍性の計算だけから coreflection と結論できないことを、明示的に確認できる。

## 5. 単純な重複座標による修正も、そのままでは失敗する

§3 の系6と、一意性クラス I を第一因子に固定する方針を合わせると、さらに制約が得られる。

仮に A=I∩C で C が coreflective なら、B の C-coreflection T→B について H(p_T) は全射でない。T∈I なら T∈I∩C=A となり矛盾するため、H(p_T) は単射でもない。

従って、この方針で第二因子の coreflection を作るなら、H(p_T) が「非単射かつ非全射」でなければならない。P は単射なので、そのままでは使えない。

そこで、P の第1成分に一つの座標を追加した

\[
Q_0=M_{fin},\qquad Q_1=M\times\Omega,
\]
\[
p_Q(f)=(f,f(0)),\qquad q_Q(f)=(t(f),f(1)),
\qquad \eta=(\operatorname{ev}_0,!):Q\longrightarrow B
\]

を考える。

Q は再び A-対象からの Hom を B と同じにする。命題7の a_1 に追加座標 ℓ_0 を付ければ存在し、H(p_Z) の全単射性により追加座標も一意に定まる。

H(p_Q) は単射でない。Q_1→Ω の二つの射「M 座標の0番目を読む」と「追加座標を読む」が p_Q 上で一致するためである。

H(p_Q) は全射でもない。直接には、任意の M-射 h:M×Ω→Ω は、ある列座標または追加座標の評価である。これには可算完備 ultrafilter の非主性が必要ない。M×Ω=Ω^{ω⊔{*}} の可算添字集合では、同変射は No.1 §1.1 と同じ有限符号化の議論で可算完備 ultrafilter を与え、可算集合上のそのような ultrafilter は主的だからである。従って H(p_Q) の像は依然として主 ultrafilter だけである。

しかし η は coreflection の counit にはならない。Q の第0成分で恒等、第1成分で

\[
\gamma_1((x_0,x_1,x_2,\ldots),a)
=((a,x_1,x_2,\ldots),x_0)
\]

とする。これは同変であり、p_Q と q_Q の像では交換する二座標が等しいので、γ=(1,γ_1):Q→Q は図式の自己同型となる。さらに ηγ=η だが γ≠1_Q。

Q が所属する full subcategory の coreflection として η を用いれば、Q からの射 η に対して恒等射と γ の二つの因子化が生じる。従って普遍性の一意性に反する。

これは、非単射性を人工的に足すだけでは不十分であり、coreflector 候補の B 上の自己射も制御する必要があることを示す。一般に別の Q や別の C が作れないという証明ではない。

## 6. 二つの coreflector を両立させる方針の限界

一般に C_0,C_1 が coreflective で coreflector R_0,R_1 を持つとする。R_0 が C_1 を C_1 に送るなら、R_0R_1(B) は C_0∩C_1 に属し、そこからの Hom 計算により交わりも coreflective となる。

従って、No.1 のような非 coreflective A を二つの coreflective subcategories の交わりとして実現する際、二つの coreflector が互いの像を保つことを要求してはならない。それは Problem 2(b) の要求より強すぎる。

K_fs⊂D と A_sigma⊂D に対しては、まさに C を有限支持部分へ戻すと P が A_sigma から出る。既存の二因子表示は D 内の表示であり、その各因子を K_fs に制限しても coreflectivity が継承されるわけではない。

## 7. 今回の正確な未解決点

一般的な否定は得ていない。任意の coorthogonality class A に対して二つの full coreflective subcategories を構成することも、K_fs 内の具体的な A に対してその二つを構成することも、ここでは完成していない。

肯定方向の次の十分目標として、一意性クラス

    I_Σ={X:Hom(X,f) が単射、すべての f∈Σ}

を第一因子に固定し、

    A⊆C、C coreflective、I_Σ∩C=A

を満たす C を構成することが考えられる。これは一般の Problem 2(b) より強い方針であり、失敗しても Problem 2(b) 自体の否定にはならない。

今回の具体例では、こうした C の B-coreflection は H(p) の非単射性と非全射性を両方持ち、しかも B 上の自己射は恒等射に限られなければならない。有限像列 P は前者を満たさず、重複座標 Q は後者を満たさない。この三条件を同時に満たし、さらに任意の標的へ拡張できる構成が残る。

## 8. 参照元と文献確認の範囲

No.1 の主入力：

- `../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md` §§3–6：テストの Hom 計算、コンパクト性、試験族、因子化サイズ下界。
- 同 §1.1：同変射と ultrafilter の対応で用いる有限符号化。
- `../No.1/codex_sset_handoff/investigations/list_colouring_independence_2026-11-15.md` §2：一意性クラスと mono テストの trace 構成。
- `sigma_coreflectivity_2026-11-16.md` §2：B における A_sigma の明示的 coreflection。
- `sigma_coreflectivity_under_no_measurables_2026-11-16.md`：D 全体での A_sigma の coreflectivity。今回、これを K_fs に自動的に移すことはしていない。

原著 Open Problems p.295 の Problem 2(b) とコメントは Library の `open-problems.pdf` で確認した。Trnková–Adámek–Rosický, “Topological reflections revisited”, Proc. AMS 108 (1990), 605–612 は原著の参照先として確認したが、今回その本文は取得できていない。そのため、同論文の正確な十分条件を双対化済みとは主張しない。上記の数学は、No.1 の採用済み結果と明示した直接証明による。
