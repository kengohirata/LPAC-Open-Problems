# A_sigma の大域的 coreflectivity：可測基数が存在しない場合

2026年11月16日。状態：`PROOF_RECONSTRUCTED`。主担当が直接証明を書き下して再点検した。独立査読・形式検証・文献上の新規性確認は未実施である。

**結論。** N＝「非可算可測基数が存在しない」を仮定すると、No.1 の平行二射の単独テストが定める部分圏 A_sigma は、母圏全体で coreflective である。特定の標的だけの結果ではない。したがって、同じ仮定の下で No.1 の部分圏 A=A_tau∩A_sigma は二つの full coreflective subcategory の交わりであり、その例は Problem 2(b) の反例にはならない。

N を外した ZFC での判定は本稿では行っていない。N を使う箇所と、その一般化が止まる理由を §9 に明記する。

## 1 設定と証明の構成

Ω=ω、M=End_Set(Ω)、K=M-Set（左作用）、J=(0⇉1)、D=K^J とする。

\[
H(A)=\operatorname{Hom}_M(A,\Omega),\qquad F(X)=\Omega^X.
\]

F(X) の作用は後合成である。対象 Z=(Z_0⇉Z_1) の構造射を p_Z,q_Z と書く。

\[
U=(\Omega^2\overset{\pi_0,\pi_1}{\rightrightarrows}\Omega),
\quad V=(\Omega\rightrightarrows1),
\quad \sigma=(\pi_0,!):U\longrightarrow V.
\]

\[
\mathcal A_\sigma=\{Z:H(p_Z)\text{ is bijective}\}
={}^{\perp}\{\sigma\}.
\]

以後、任意の標的図式には B を用い、元の固定標的 V と区別する。

証明には、既存の [対象で測る同値射の OFS](../No.1/codex_sset_handoff/investigations/object_cogenerated_factorization_2026-11-16.md) を用いる：

\[
\mathcal E=\{e:H(e)\text{ is bijective}\},\qquad
\mathcal R=\mathcal E^{\perp_u}.
\]

(E,R) は K の orthogonal factorization system であり、これは ZFC の結果である。各 B∈K に対し R/B を、K/B のうち構造射が R に属する対象からなる充満部分圏とする。E–R 因子分解により R/B は reflective である。R の極限閉性からその極限は K/B で計算され、余極限は K/B の余極限を反射して得られる。

核心は次である。

> **補助定理。** N の下で、任意の B∈K について (R/B)^op は locally presentable である。

この定理は K^op 全体が locally presentable という主張ではない。標的 B を固定し、構造射を R に制限した圏についての主張である。

## 2 M-set の成分と積の Hom

### 2.1 成分は Ω からの射で数えられる

c_n∈M を値 n の定数写像とする。a∈A に対し

\[
\rho_a:\Omega\longrightarrow A,\qquad \rho_a(n)=c_na
\]

は M-射である。c_n m=c_n により ρ_{ma}=ρ_a である。また ρ_{ρ_a(n)}=ρ_a なので、ρ_a が等しい元は作用の無向連結成分として同じ成分に属する。逆も成立する。従って

\[
\pi(A):=\operatorname{Hom}_M(\Omega,A),\qquad
A=\coprod_{i\in\pi(A)}A_i
\]

は非空連結成分への分解である。各成分にはただ一つの Ω からの射があり、その像は Ω または一点である。空 M-set の成分集合は空。

H(Ω) と H(∅) はいずれも一元集合なので ∅→Ω∈E。従って r:C→B∈R なら、一意持上げ性により π(r) は全単射である。r は成分を一対一に対応させる。

### 2.2 N を使う計算

Isbell の評価表示により、N の下では任意の集合 S について

\[
\tag{1} S\xrightarrow{\cong}H(F(S)),\qquad s\longmapsto\operatorname{ev}_s.
\]

この同定の直接証明は [No.1 の証明ノート §1.1](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md) にある。文献上の定式化は [Shulman, p.20](https://arxiv.org/pdf/0810.1279) でも確認できる。ここでは集合の全単射だけを用いる。

**補題 1。** C が非空連結 M-set なら、任意の集合 X に対し自然な全単射

\[
\tag{2} H(C\times F(X))\cong H(C)\sqcup X
\]

がある。左の H(C) の元は C への射影に沿って引き戻し、X の元は F(X) の座標として読む。

**証明。** 正則左 M-set は M=F(Ω) なので

\[
M\times F(X)=F(\Omega\sqcup X),\qquad
H(M\times F(X))\cong\Omega\sqcup X.
\]

h:C×F(X)→Ω に対し、a∈C ごとに h_a(m,f)=h(ma,f) と置く。(1) より h_a は、ある n∈Ω による m(n)、またはある x∈X による f(x) のいずれかである。

h_{ua}(m,f)=h_a(mu,f) なので、このラベルは M-射 C→Ω⊔ΔX を定める。ΔX は自明作用を持つ X である。逆にそのような M-射から h を復元できる。C が連結なので、像が Ω に入るか、ある一つの x∈X に入るかのどちらかであり、(2) を得る。X=∅ も含む。□

## 3 R に属する射の正規形

**補題 2。** B が非空連結で r:C→B∈R なら、D=im(r)⊆B とある集合 X を用いて、r は B 上で

\[
\tag{3} D\times F(X)\xrightarrow{\operatorname{pr}_D}D\hookrightarrow B
\]

と同型である。D は非空連結である。

**証明。** §2.1 より C は非空連結である。通常の全射 d:C↠D による H(d):H(D)→H(C) は単射なので、H(D) をその像と同一視し、X=H(C)\H(D) とする。

\[
a:C\longrightarrow D\times F(X),\qquad
a(c)=(d(c),(x(c))_{x\in X}).
\]

補題1より H(a):H(D)⊔X→H(C) は全単射であり、a∈E である。a と r の四角に一意持上げ性を用いると

\[
\ell:D\times F(X)\longrightarrow C,
\qquad \ell a=1_C,\quad r\ell=(D\hookrightarrow B)\operatorname{pr}_D
\]

が得られる。D↪B が mono なので dℓ=pr_D。さらに aℓa=a であり、各 Ω 座標について H(a) の単射性を用いると aℓ の F(X) 成分は射影に等しい。従って aℓ=1 であり、a は同型。X=∅ の場合は D 成分だけで同じ結論となる。□

一般の B について、r:C→B∈R の各成分 r_i:C_i→B_i は pullback により R に属する。従って補題2を成分ごとに使える。

以下、H(C)≠∅ を満たす対象を「Ω 値写像を持つ対象」と呼ぶ。もし H(C)=∅ なら、r による H(B)→H(C) から H(B)=∅ でもあり、r∈E∩R、従って r は同型である。したがって R/B で Ω 値写像を持たない対象は、H(B)=∅ の場合の 1_B 一つだけである（同型を除く）。

## 4 正規形の対象と射を集合で記述する

### 4.1 連結した標的

B が非空連結の場合を固定する。非空部分 M-set D⊆B を **許容される D** と呼ぶ条件を

\[
\tag{4} D\times\Omega\longrightarrow B\text{ belongs to }\mathcal R
\]

とする。この条件で選ぶ D は B の部分対象の集合の中にあり、クラス個の選択を使わない。

**補題 3。** R/B の Ω 値写像を持つ対象は、同型を除き、ちょうど

\[
\tag{5} (D,X):=(D\times F(X)\to B),
\quad D\text{ は許容される},\quad H(D)\sqcup X\ne\varnothing
\]

である。

**証明。** 正規形は補題2による。H(D)≠∅ なら、D→D×F(X) に Ω 値写像を全座標で用いた切断がある。従って D×F(X)→B∈R なら D↪B∈R である。逆に D↪B∈R なら、F(X) が E に関して局所的な対象であることから、射影 D×F(X)→D は R に属し、合成も R に属する。この議論を X=1 にも適用すれば (4) との同値が分かる。

H(D)=∅ なら (5) では X≠∅。Ω は F(X) の retract なので、D×F(X)→B∈R から (4) が従う。逆に (4) が成立すれば、B 上で D×Ω→B を X 個積を取る。D↪B が mono、X が非空なのでその積は D×F(X)→B に等しく、R の極限閉性を使える。□

**補題 4。** 正規形の間の Hom は

\[
\tag{6}
\operatorname{Hom}_{\mathcal R/B}((D,X),(E,Y))
\cong
\begin{cases}
\operatorname{Set}(Y,H(D)\sqcup X),&D\subseteq E,\\
\varnothing,&D\nsubseteq E.
\end{cases}
\]

**証明。** B 上の射が存在すれば、その像から D⊆E が必要である。そのとき E 成分は D への射影と包含によって固定され、残る F(Y) 成分は Y 個の Ω 値写像で指定される。補題1を適用する。□

反対圏では (D,X)→(E,Y) に E⊆D と写像 X→H(E)⊔Y が対応する。全体の Ω 値写像の集合 H(D)⊔X 上では、H(D) の部分は制限 H(D)→H(E) で固定される。

### 4.2 複数の成分と空 Hom

B=∐_{i∈I}B_i とする。R/B の Ω 値写像を持つ対象の圏は、各成分 B_i に対する (5) の圏の積である。

この主張には確認が必要である。一般の E 射の成分制限が E に入ると無条件には言えないからである。逆向きを確認するため、各 r_i:C_i→B_i が R で各 H(C_i) が非空とし、r=∐r_i とする。e:X→Y∈E と r との四角を取る。X→C により H(X) は非空、H(e) が全単射なので H(Y) も非空である。Y→B の成分分解に沿って e=∐e_i と書くと、全ての H(X_i),H(Y_i) は非空であり、

\[
H(e)=\prod_i H(e_i)
\]

の全単射性から各 H(e_i) の全単射性が従う。各成分の一意持上げを合わせれば r∈R である。逆向きは R の pullback 閉性による。

H(B)≠∅ なら全ての R/B 対象がこの積に入る。H(B)=∅ なら、これに終対象 1_B だけを加える。1_B から Ω 値写像を持つ対象への射は存在せず、逆向きの射は一意である。反対圏では「他の対象から射が入らない初対象」を一つ加える形になる。

B=∅ の場合、R/B は一対象圏であり、別途直ちに扱える。

## 5 (R/B)^op の local presentability

**補題 5。** N の下で、任意の B∈K について (R/B)^op は accessible、従って locally presentable である。

**証明。** §4 の正規形を使う。I が成分集合のとき、対象は部分対象の組 (D_i)_{i∈I} と変数集合の組 (X_i)_{i∈I} で指定される。D_i の組の候補は集合である。正則基数 λ を、次の全てより大きく取る：|I|、D_i の組の候補数、および全ての |H(D_i)|。これらを一つの集合サイズの上界で抑えられることは B を固定した点に依存する。

まず λ-filtered diagram を取る。反対圏の射に沿って部分対象の組は包含に関して減少する。現れる組は λ 未満個しかないので、その各組を代表する対象を選び、λ-filtered 性によりそれらの共通後続を取れる。その後続の組 D_* は現れる全ての組に含まれる。組が D_* に等しい対象からなる充満部分図式は final であり、それ自身 λ-filtered である。実際、任意の対象から共通後続を取ればこの部分に入り、この部分から出る全ての射もこの部分に留まる。

この部分図式では各 H(D_{*,i}) が固定され、射は集合 H(D_{*,i})⊔X_i の間でその固定部分を恒等的に保つ写像である。集合で filtered colimit を取ると固定部分は依然として単射で入り、各成分の全体は非空である。その補集合を新しい X_i とすれば §4 の正規形になる。(6) から、これは元の圏でも余極限の普遍性を満たす。別の部分対象の組 E への cocone がある条件は E⊆D_* であり、その場合には集合の余極限の普遍性に帰着する。

次に、変数の総数 Σ_i|X_i|<λ の正規形は λ-presentable である。上の安定した部分図式に移った後、そこへの射は λ 未満個の変数の像によって指定されるので、一つの段階を経由する。二つの因子化の一致も同じ λ-filtered 性で一つの段階に移せる。固定部分 H(D_i) の像は包含に伴う制限として既に指定されている。

任意の正規形は、その変数集合の総数 λ 未満の部分集合による λ-filtered colimit である。H(D_i)=∅ の成分では X_i が非空なので一つずつ基準元を選び、各部分集合に含める。|I|<λ によりこの条件はサイズ制限と両立する。これらの小さい正規形の同型類は集合をなす。

H(B)=∅ の場合の追加初対象も λ-presentable である。λ-filtered diagram が他の対象を一つでも含めば、その対象からの後続を用いて追加初対象を除いた final な部分図式に移れる。初対象だけからなる図式は自明に扱える。

以上から accessibility が従う。一方、R/B は §1 により complete なので、その反対圏は cocomplete である。accessible かつ cocomplete なので locally presentable。□

## 6 任意の標的図式の上で使う圏

B=(B_0⇉B_1)∈D を任意に固定する。Q_B を、D/B のうち各成分 r_i:C_i→B_i が R に属する対象からなる充満部分圏とする。

**補題 6（ZFC）。** Q_B は D/B に reflective である。反射単位の各成分は E に属する。

**証明。** b:Z→B の各成分を e_i:Z_i→C_i、r_i:C_i→B_i と因子分解する。e_i∈E と r_j∈R の一意持上げにより p_C,q_C が定まり、e と r は図式の射となる。同じ持上げ性により、Z→T（T→B∈Q_B）は C→T を一意に経由する。□

**補題 7（N）。** Q_B^op は locally presentable である。

**証明。** C_i=(R/B_i)^op は補題5により locally presentable。pullback は R を保存するので

\[
p_B^*,q_B^*:\mathcal R/B_1\longrightarrow\mathcal R/B_0
\]

が定まり、これらは極限を保存する。その反対関手は全ての余極限を保存し、従って accessible である。

P,Q:C_1→C_0 をこの二つの反対関手とする。元の図式の射 C_0→C_1 は、標的の構造射ごとに C_0→p_B^*C_1 と C_0→q_B^*C_1 と書き換えられる。反対圏に移れば

\[
Q_B^{op}\simeq ((P,Q)\downarrow\Delta),
\qquad
(P,Q):C_1\longrightarrow C_0\times C_0,
\quad\Delta:C_0\longrightarrow C_0\times C_0.
\]

accessible functor の comma category は accessible である。また両関手が余極限を保存するので、この comma category は成分ごとに余極限を持つ。従って locally presentable。□

ここで用いた標準的な accessibility の定理には基数の拡大が含まれる。同一の λ で関手が presentable object を保存すると無条件には仮定していない。定理の精確な仮定と uniformization は [mathlib の公式実装・説明](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Presentable/Comma.html) でも確認できる。この参照は補題5や本稿全体の形式検証を意味しない。

## 7 任意の標的への coreflection

**定理（N）。** A_sigma↪D は右随伴を持つ。

**証明。** B∈D を任意に固定する。B 上の射

\[
\tag{7} B\times\sigma:B\times U\longrightarrow B\times V
\]

を考える。U,V の各成分は Ω の積（空積 1 を含む）なので E に関して局所的である。従って B×U→B、B×V→B の各成分は R に属し、(7) は Q_B の射である。

任意の C→B∈Q_B に対し

\[
\operatorname{Hom}_{D/B}(C,B\times U)\cong H(C_1),\qquad
\operatorname{Hom}_{D/B}(C,B\times V)\cong H(C_0)
\]

であり、(7) による Hom 写像は H(p_C) である。従って

\[
\mathcal T_B:=\{C\to B\in Q_B:C\in\mathcal A_\sigma\}
\]

は Q_B の一本の射による coorthogonality class である。補題7により Q_B^op は locally presentable だから、通常の small-orthogonality class の反射定理を反対圏で適用できる。よって T_B↪Q_B は coreflective である。

Q_B の終対象 1_B の coreflection を t:T→B とする。T∈A_sigma であり、t の各成分は R に属する。

Z∈A_sigma からの任意の b:Z→B を取る。補題6により

\[
Z\xrightarrow{e}C\xrightarrow{r}B,
\qquad e_i\in E,\quad r_i\in R
\]

と分解する。H(e_i) が全単射なので、p との可換性から H(p_C) も全単射となり、C→B∈T_B である。従って C→T が B 上で一意に存在し、合成 Z→T は b を因子化する。

一意性も全ての Z について確認できる。Z→T の任意の B 上の射は、e_i∈E と t_i∈R の一意持上げ性により C→T を一意に経由する（自然性も同じ一意性による）。その C→T は T_B での普遍性により唯一である。従って

\[
\operatorname{Hom}_D(Z,T)\xrightarrow{t\circ-}\operatorname{Hom}_D(Z,B)
\]

は全単射である。B が任意だったので大域的 coreflectivity が従う。□

small-orthogonality class の反射定理は、例えば [Casacuberta–Scevenels–Smith, Theorem 2.1](https://www.ub.edu/topologia/casacuberta/articles/css.pdf) に正確な通常圏の形で記されている。ここではホモトピー版や weak lifting は使用していない。

## 8 No.1 と Problem 2(b) への帰結

A_tau は第0成分の有限支持条件だけを課す部分圏であり、ZFC で coreflective である。任意の Z=(Z_0⇉Z_1) に対して

\[
((Z_0)_{fs}\rightrightarrows Z_1)\longrightarrow Z
\]

を取ればよい。構造射を制限し、有限支持元が M-射で有限支持元に送られることを用いると、普遍性が直ちに従う。

従って N の下で

\[
\mathcal A=\mathcal A_\tau\cap\mathcal A_\sigma
\]

は二つの full coreflective subcategory の交わりである。他方、[No.1 の既存の直接証明](../No.1/codex_sset_handoff/investigations/parallel_actions_counterexample_2026-11-16.md) によれば、同じ N の下で A 自身は coreflective でない。この二つの主張は両立する。

したがって、この例は Problem 2(a) 型の非 coreflectivity を示すが、**N の下では Problem 2(b) が要求する表示を実際に持っている**。Problem 2(b) 一般の肯定・否定はここからは導かれない。

## 9 仮定なしへの拡張が止まる箇所

N を直接使用したのは §2.2 の評価表示 (1) である。それにより補題1の「連結 C に対する H(C×F(X))=H(C)⊔X」が得られ、正規形と accessibility が続いた。

この計算は可測基数を許すと実際に失敗する。可測基数 κ 上の非単項の可算完備 ultrafilter U を取ると、各 f:κ→ω について一意な n が f^{-1}({n})∈U を満たす。そこで

\[
h_U(f)=n
\]

と置けば h_U:F(κ)→Ω は M-射であり、座標評価ではない。M-同変性は U に属する f の定値ファイバーが、後合成 m により m(n) のファイバーに含まれることから従う。非単項性により、各点の特性関数を使ってどの座標評価とも異なることが分かる。

C=1 は非空連結で H(1)=∅ なので、補題1を仮定なしに主張すれば、座標評価による写像 κ→H(F(κ)) が全単射だと要求してしまう。h_U はその全射性への反例である。したがって本証明の N を単に削除することはできない。

これは ZFC での coreflectivity を否定する例ではない。補題1以降の正規形・accessibility に代わる論証が必要だという、具体的な方法上の境界である。可測基数が存在する一般の場合の coreflection の不存在は得ていない。

## 10 点検した範囲

**元の標的の再現。** B=V=(Ω⇉1) では (R/Ω)^op は pointed sets、(R/1)^op は Set と同値になる。前者の正規形は Ω×F(X)=F(1⊔X)、後者は F(X) である。pullback Ω→1 の反対関手は自由 pointed set 関手 X↦1⊔X に一致する。従って Q_V^op の対象は、pointed set S_0 と集合 S_1、および二つの写像 S_1⇉S_0 として記述できる。A_sigma の条件は一方が全単射であることなので、その部分圏は pointed set と、基点を保存するとは限らない一つの集合自己写像の圏になる（射は基点を保存して自己写像と可換な写像）。その初対象は (N,0,n↦n+1) であり、反対側では既存の (Ω^N⇉Ω^N)、二射 (1,shift)、V への射 (ev_0,!) を再現する。これは新しい一般証明と前回の明示的 coreflection が一致する点検である。

**Ω 値写像が空の標的。** H(B_0)=∅ なら、H(p_B):H(B_1)→H(B_0) の存在から H(B_1)=∅ でもあり、B は最初から A_sigma に属する。その coreflection は恒等射でよい。§7 の構成も普遍性によりこれと同型になる。

- テストの終域 V 一つだけでなく、任意の標的図式 B を §6–7 で扱った。
- p と q は両方とも保持した。単一の射 p の coreflection に q を任意に付けたわけではない。
- 全ての直交は ordinary Hom の全単射・一意対角持上げである。
- Ω 値写像が空の対象、空 M-set、複数成分、X=∅ を別々に扱った。
- 複数成分に E を制限する段階では、積の全単射から各成分の全単射を得るための非空性を明示した。
- accessibility の基数は標的 B に依存する。A_sigma 自体が accessible という主張はしていない。
- 本稿の結論は ZFC+N の定理としての直接証明であり、仮定なしの ZFC の定理、Problem 2(b) 一般の解決、独立査読済みという主張はしていない。
