# 可測基数の必要条件の強化と、強コンパクト基数による肯定

2026-11-17。状態：`PROOF_RECONSTRUCTED`。本セッションで直接証明を展開・点検したもの。独立査読、外部査読、形式検証、新規性調査は未実施。有限計算を無限の結論の根拠にしていない。既存の `parallel_actions_counterexample_2026-11-16.md` と `positive_purity_2026-11-16.md` を出発点とするが、本稿で使う拡張部分は以下に記す。

## 0. 結論と、一般問題・固定例の区別

P は「任意の局所可呈示圏 K と射の集合 S について、ordinary Hom による coorthogonality class {}^perp S が coreflective」という主張。

今回の主な結論は

\[
\boxed{\text{強コンパクト基数が真クラス存在}\ \Longrightarrow\ P\ \Longrightarrow\ \text{可測基数が真クラス存在}.}
\]

特に、既存の否定側の仮定 N（可測基数が存在しない）を、M（可測基数の全体が集合である）へ弱められる。可測基数がちょうど一つ存在するモデル L[U] でも P は偽になる。したがって「可測基数が一つ存在する」という公理だけから一般の P を証明することはできない（通常の相対的無矛盾性の意味）。

一方、元の Omega=omega の固定された反例クラスについて、可測基数一つがその coreflectivity を保証するかは、今回未判定。一般の P の否定では、Omega のサイズを変更してよい。この区別を維持する。

## 1. 任意の無限サイズへの Isbell 型計算の拡張

無限基数 rho と |Omega|=rho の集合 Omega を固定する。M_Omega=End(Omega) は合成を積とするモノイドで、左作用を使う。

\[
F(X)=\Omega^X,\qquad H(A)=\operatorname{Hom}_{M_\Omega}(A,\Omega).
\]

F(X) への作用は後合成。H(A) は離散 Omega の積 Omega^A の部分空間位相を持つ。

**補題1。** 任意の集合 X に対し、H(F(X)) は X 上の rho^+-complete ultrafilters の集合と自然に全単射になる。ここで rho^+-complete は「rho 個以下の交叉で閉じる」という意味である。

**証明。** X が非空とし、phi:Omega^X→Omega を M_Omega-射とする。任意の f について phi(f)∈im(f) である。im(f) を点ごとに固定するすべての自己写像が phi(f) も固定することを使う。

Omega の異なる二点を 0,1 と呼び、

\[
\mathscr U_\phi=\{A\subseteq X:\phi(\chi_A)=1\}
\]

と定める。補集合は 0,1 を交換する自己写像で、有限交叉は二つの特性関数の値の組を Omega に符号化し、座標射と論理積を自己写像で表すことで検証できる。したがってこれは ultrafilter。

任意の f:X→Omega について t=phi(f) とすると、t の特性関数 m_t:Omega→Omega を使って
phi(chi_{f^{-1}(t)})=phi(m_t f)=m_t(phi(f))=1。
従って rho 個以下のセルからなるどの分割にも、U_phi に属するセルがある。

この分割性は rho^+-completeness と同値。実際、rho 個以下の U_phi-集合の交叉が U_phi に属さないなら、最初の脱落位置と共通部分により rho 個以下の U_phi-small なセルに分割でき、矛盾する。ここで rho は無限なので rho+1 個という基数も rho 個以下である。

逆に、rho^+-complete ultrafilter U があれば、phi_U(f) を f^{-1}(t)∈U となる唯一の t と定義する。分割のセル数は rho 以下なので存在し、一意性は ultrafilter 性による。後合成との可換性は、選んだ fibre の包含関係から従う。両構成は互いに逆。X が空なら、両側とも空である（F(empty)=1 から Omega への equivariant map は存在しない）。∎

**補題2。** 非主的な rho^+-complete ultrafilter がある集合上に存在すれば、rho より大きい可測基数が存在する。

**証明。** U-small なセルだけによる分割の最小基数を nu とする。非主性から singleton 分割が存在し、rho^+-completeness から nu>rho。最小性により U は nu-complete である。そうでなければ nu 未満の U-集合の交叉の失敗から、最初の脱落位置による nu 未満の small セルの分割を作れる。最小分割 X→nu に沿って U を押し出すと、nu 上の非主的 nu-complete ultrafilter を得る。∎

逆に可測基数 nu>rho の測度は rho^+-complete である。従って

\[
\boxed{\forall X,\ X\xrightarrow{\mathrm{ev}}H(F(X))\text{ が全単射}\ \Longleftrightarrow\ \text{rho より大きい可測基数が存在しない}.}
\]

rho=aleph_0 は既存の Isbell 型の計算に一致する。一般 rho では「すべての可測基数が存在しない」ことを要求していない。

## 2. 有限支持とコンパクト双対は Omega が非可算でも維持される

a∈A の有限支持とは、有限 S⊂Omega に対して m|S=n|S なら ma=na となること。

有限 S を点ごとに固定するすべての n が a を固定する、という条件と同値である。逆方向では、m,n が S 上一致するとき、w|S=m|S で各 fibre が濃度 rho の全射 w:Omega→Omega を選ぶ。これは有限個の値を指定しても rho×rho=rho により可能。S 上恒等な u,v で wu=m, wv=n とできるので ma=wa=na。

K=2^{M_Omega} に (n chi)(m)=chi(mn) という cofree 作用を入れ、有限支持元の部分対象を K_fs、包含を j:K_fs→K とする。

**補題3。** A⊥j と A が有限支持であることは同値。

順方向の非自明な部分には、各 a∈A の singleton の特性関数 c_a:A→2 に対応する equivariant map Phi_a(x)(m)=c_a(mx) を使う。Phi_a(a) の有限支持 S を取ると、S を固定する n に対して c_a(na)=1、すなわち na=a。前段落から a が有限支持である。逆方向は equivariant map が有限支持を保つことと j の mono 性による。

**補題4。** 有限支持 A に対し H(A) は compact Hausdorff。各 a に有限支持 S_a を選ぶと、h(a)∈S_a が強制される。H(A) は有限離散空間の積 prod_a S_a の中で equivariance の閉条件により定義される。空支持や H(A)=empty も許す。

**補題5。** Stone 空間 X に対し C(X)=Cont(X,Omega_disc) は有限支持で、評価写像 X→H(C(X)) は同相。

連続関数の像は有限なので、その像が支持になる。phi:C(X)→Omega が equivariant なら、有限個の関数の値をまとめて Omega に符号化することで、それらの値 phi(f) を同時に実現する点がある。閉集合 f^{-1}(phi(f)) の有限交叉性、X のコンパクト性、clopen による点分離から、phi は唯一の点での評価となる。評価は連続な全単射で、compact-to-Hausdorff により同相。∎

これらは全て ZFC の証明で、Omega の可算性は使わない。

## 3. 二本の固定テスト

J=(0⇉1)、D_rho=(M_Omega-Set)^J とする。これは小さい圏上の前層圏（実際には locally finitely presentable）である。対象を Z=(Z_0 ⇉ Z_1)、二射を p_Z,q_Z と書く。

R_0(W)=(W⇉1) とし、

\[
\tau_\rho=R_0(j),\qquad
\sigma_\rho:(\Omega^2\mathrel{\substack{\xrightarrow{\pi_0}\\\xrightarrow[\pi_1]{}}}\Omega)\longrightarrow(\Omega\rightrightarrows1)
\]

とする。sigma の成分は (pi_0,!)。固定標的は B_rho=(Omega⇉1)、A_rho={}^perp{tau_rho,sigma_rho}。

随伴と直接の Hom 計算から

\[
Z\in A_\rho\ \Longleftrightarrow\ Z_0\text{ が有限支持、かつ }H(p_Z):H(Z_1)\to H(Z_0)\text{ が全単射}.
\]

q_Z には別の条件を課していない。全てのデータは rho を選んだ時点で固定され、後で使う基数 theta に依存しない。

## 4. M の下での反例と、真クラス個の可測基数という下界

rho より大きい可測基数が存在しないと仮定する。Stone 空間 X と任意の集合写像 d:X→X に対して

\[
Y_{X,d}=(C(X)\mathrel{\substack{\xrightarrow{i}\\\xrightarrow[d^*]{}}}\Omega^X),\qquad d^*(f)=f\circ d
\]

を作る。d の連続性は仮定しない。補題1–5から H(i) は集合としての恒等写像 X→X に対応するので、Y_{X,d}∈A_rho。

X_theta=[0,theta] に順序位相を入れ、d(alpha)=alpha+1（alpha<theta）、d(theta)=theta、基点0を取る。これは Stone 空間で、0を含む閉 d-不変部分集合は全体だけである。後続段では d、極限段では閉性を使った超限帰納法による。

評価と終対象への射により psi_theta:Y_theta→B_rho を得る。任意の A_rho 内の因子化 Y_theta→Z→B_rho を考える。

T=H(Z_0)、S=H(Z_1)、u=H(p_Z):S→T、v=H(q_Z):S→T とし、k=v u^{-1} と置く。最初の射の双対は h:T→X_theta、ell:S→X_theta を与え、二つの自然性条件は hu=ell、hv=d ell。従って hk=dh。

T は有限支持条件により compact、h は連続なので h(T) は閉。さらに d-不変であり、Z→B_rho の第0成分が0の逆像を与えるため0を含む。従って h は全射である。ゆえに

\[
\tag{*}
|X_\theta|\leq |H(Z_0)|\leq\rho^{|Z_0|}.
\]

k や u^{-1} の連続性は使っていない。

A_rho↓B_rho の任意の集合個の候補を取り、それらの |H(Z_0)| を全て上回る theta を選ぶと、(*) により psi_theta はどの候補も経由できない。従って weakly terminal set がなく、coreflection がない。

**定理6。** rho より大きい可測基数がなければ、固定された A_rho は B_rho で coreflection を持たない。

可測基数全体が集合なら、その全てを抑える無限基数 rho を一度だけ選べる。この rho で定理6を適用する。従って

\[
\boxed{M\Longrightarrow\neg P,\qquad P\Longrightarrow\forall\rho\ \exists\nu>\rho\ (\nu\text{ は可測}).}
\]

これは「候補のサイズごとにテストを変える」議論ではない。rho を一度選んで圏・テスト・標的を固定し、theta だけを無界に変える。

可測基数の存在から、可測基数がちょうど一つの標準内モデル L[U] が得られる（Kunen の定理）。そのモデルで rho をその唯一の可測基数以上に取れば本反例が成立する。従って

Con(ZFC+『可測基数が存在』) ⇒ Con(ZFC+『可測基数が存在』+not P)。

この結論は、元の Omega=omega の A_omega がそのモデルでも非 coreflective だという主張ではない。

## 5. 可測基数があると、元の順序数族はどこで止まるか

nu を rho より大きい最初の可測基数とする。無限基数 theta について、上の同じ定義の候補は正確に

\[
\boxed{Y_\theta\in A_\rho\ \Longleftrightarrow\ \theta<\nu}
\]

を満たす。

theta<nu なら、[0,theta] 上の非主的 rho^+-complete ultrafilter は、補題2の証明から rho<mu≤theta の可測基数を生むので存在しない。従って従来通り H(i) が全単射。

theta≥nu の場合、nu 上の非主的 nu-complete ultrafilter U を [0,theta] に押し出す。その fibre evaluation phi_U は Omega^{[0,theta]}→Omega の equivariant map となる。もう一つ、点 nu での評価 ev_nu がある。これらは集合 {nu} の特性関数上で異なる。一方、f:[0,theta]→Omega_disc が連続なら、nu の下のある tail で f は f(nu) に等しい。U は全てのそのような tail を含むので、phi_U(f)=f(nu)。従って H(i) は単射でなく、Y_theta は不合格。∎

**重要な区別。** この族が nu で不合格になることは、A_rho の coreflection が存在することを証明しない。所属条件が壊れたので既存の反例証明をそのまま延長できなくなった、という結果である。

さらに B_rho に A_rho-coreflection R→B_rho が存在するなら |R_0|≥nu。実際、全 theta<nu の Y_theta が R を経由するので |H(R_0)|≥nu。nu は強到達不能なので、rho,|R_0|<nu なら rho^{|R_0|}<nu となり矛盾する。これは必要サイズの下界であり、存在証明ではない。

## 6. 肯定側：小さい標的は、強コンパクト性により pure-injective になる

K=Set^{C^op} とし、kappa を強コンパクト基数、|Mor C|<kappa とする。対象のサイズは全ソートの台集合の非交和の濃度。

**補題7。** |D|<kappa の対象 D は kappa-pure-injective。

**証明。** kappa-pure inclusion Y⊂X と h:Y→D を取る。延長のため、各 x∈X(c) の像を D(c) に値を取る変数とし、全ての構造写像を保存する方程式、および y∈Y の像を h(y) にする方程式を課す。この制約集合を E とする。

E の kappa 個未満の部分集合の制約は満たせる。対応する X 内で成立する方程式系を Y の元をパラメータとする系に書き、purity によって Y 内で解き、h を適用する。空ソートについても、X(c) が非空なら無パラメータの存在条件により Y(c) は非空、従って D(c) も非空である。

P_kappa(E) の上の cone filter（各 e∈E を含む部分集合が大きい）は kappa-complete。強コンパクト性によって kappa-complete ultrafilter U に延長できる。各 s∈P_kappa(E) について s を満たす割当を選び、未使用の変数は任意に補う。

各変数の値域は kappa 未満なので、その値は U 上ほとんど至るところ一つの値に定まる。これを全変数について採用する。各方程式は有限個の変数を使い、その方程式を含む s の集合は U に属するため、極限割当でも成立する。h を延長する自然変換 X→D を得る。∎

ここで必要なのは任意の制約集合 E に対する fine ultrafilter である。単にある可測基数上に一つ測度が存在するという仮定が、この手順を供給するわけではない。

## 7. 小さいテスト集合への適用

S={f_i:U_i→V_i} を固定し、kappa が強コンパクトで

\[
|\operatorname{Mor}C|+\sum_i(|U_i|+|V_i|)+\aleph_0<\kappa
\]

とする。W_i=U_i×_{V_i}U_i も kappa 未満なので、補題7により V_i,W_i は同じ kappa で pure-injective。

X∈A={}^perp S と kappa-pure Y⊂X を取る。Y→V_i を X→V_i に延長して X の持上げを制限すれば存在性を得る。一意性については二つの候補 Y→U_i を合わせた Y→W_i を X→W_i に延長し、二射影の一致を X の直交性から得る。従って Y∈A。

サイズの議論も明記する。mu=2^kappa とすれば mu^{<kappa}=mu。X 内のサイズ≤mu の元集合を、サイズ≤mu の kappa-pure subpresheaf に拡大できる。長さ kappa の増大列で、各段の kappa 未満の方程式系のうち X で解けるものの解を一つずつ加える。系の数は mu 以下、構造演算の数も mu 以下。kappa の正則性により最終合併は pure となる。

従って各 X∈A はサイズ≤mu の A-部分対象の mu^+-directed union となる。これらの小さい対象は K でも A でも mu^+-presentable で、同型類は集合個。A は全ての小余極限に閉じ、包含がそれらを保存する。ゆえに A は locally presentable、包含は右随伴を持つ。

**定理8。** 固定された前層圏と固定されたテスト集合のデータを十分上回る強コンパクト基数が一つあれば、その coorthogonality class は locally presentable かつ coreflective。

この証明で「存在性だけ」と「一意性」を混同していない。一意性には W_i への同時延長が必要である。

## 8. 一般の P への移送と、固定反例への適用

任意の局所可呈示圏 D は、ある前層圏 K の充満反射部分圏として表せる。L:K⇄D:J、L⊣J とし、D のテスト S について A={}^perp_D S、C={}^perp_K(JS) と置くと C=L^{-1}(A)。

C が K で coreflective なら A は D で coreflective。実際、JB の C-coreflection c:C_0→JB と単位 eta:C_0→JLC_0 を考える。c=Jd eta と書け、JLC_0∈C なので、普遍性から t:JLC_0→C_0 を得て t eta=id。反射の普遍性から eta t=id も従う。したがって C_0 は J の像に属し、d は D での coreflection になる。

強コンパクト基数が真クラスあれば、各前層表示と各 JS のサイズを上回る一つを選べる。定理8から

\[
\boxed{\text{強コンパクト基数が真クラス存在}\Longrightarrow P.}
\]

この移送段階では、一般の D の A が accessible であることまで主張する必要はなく、coreflectivity だけを結論している。

固定例 A_rho の全データのサイズは高々 2^{2^rho}。実際 |M_Omega|=rho^rho=2^rho、|2^{M_Omega}|=2^{2^rho}。kappa>rho が強コンパクトなら強到達不能なので 2^{2^rho}<kappa。従って定理8が適用できる。

まとめると、固定された例には

\[
\exists\kappa>\rho\ (\kappa\text{ 強コンパクト})
\Longrightarrow A_\rho\text{ は coreflective}
\Longrightarrow\exists\nu>\rho\ (\nu\text{ 可測})
\]

という上下界がある。特に元の A_omega は、強コンパクト基数が一つ存在すれば肯定的に処理できる。

## 9. 未解決部分と主張しないこと

- 可測基数一つから一般の P は導けない。この点は今回の M⇒not P と L[U] によって決着する。
- 可測基数が真クラス存在すれば P か：今回未証明。
- 元の固定 A_omega は可測基数一つで coreflective か：今回未証明。
- P と強コンパクト基数の真クラスの同値性、正確な無矛盾性強度、新規性は主張しない。
- 通常の可測性で fine ultrafilter を得ること、元の候補族の失敗から肯定解を結論すること、Omega を変えた反例を元の固定圏の反例と呼ぶことは行わない。
- 肯定側の機構は、コンパクト性による小さい対象の pure-injectivity という既知の方法の前層版を、既存の kernel-pair 判定に接続したもの。文献の弱持上げ定理をそのまま一意持上げ定理として引用していない。

## 10. 参照した一次資料・著者資料

1. J. R. Isbell, *Adequate subcategories*, Illinois J. Math. 4 (1960), 541–552, §2.5。可算版の背景。一般 rho 版は本稿§1で直接証明。
   https://conceptualmathematics.wordpress.com/wp-content/uploads/2013/05/adequatesubcategories.pdf
2. M. Shulman, *Set theory for category theory*, p.20。Set^op の小 dense subcategory と可測基数の非有界性の関係、Adámek–Rosický A.5 の説明。
   https://arxiv.org/pdf/0810.1279
3. J. Jureczko, *The new operations on complete ideals*, Open Mathematics 17 (2019), 415–422, Fact 11。Kunen の L[U] の唯一の可測基数定理を明記。
   https://doi.org/10.1515/math-2019-0032
4. A. Karagila, *Large Cardinals*, 講義ノート、§3.5 p.21、§6.1 pp.30–31。L[U] と、強コンパクト性の filter extension / fine ultrafilter 定式化。Web取得版の更新表示は2026-04-13。
   https://karagila.org/files/LC-2025.pdf
5. S. Cox and J. Rosicky, *Fibrantly generated weak factorization systems*, Rend. Sem. Mat. Univ. Padova 152 (2024), 133–144, §3。pure-injectivity と projectivity class の accessibility の背景。今回の強コンパクト十分条件そのものを同論文の定理として引用していない。
   https://ems.press/content/serial-article-files/48316
6. M. Cortes-Izurdiaga and J. Saroch, *The cotorsion pair generated by the Gorenstein projective modules and lambda-pure-injective modules*, arXiv:2104.08602v2, §5, Proposition 5.3、Remark 5.4、Proposition 5.6。強コンパクト性と小さい加群の pure-injectivity の既知の類例。
   https://arxiv.org/pdf/2104.08602
