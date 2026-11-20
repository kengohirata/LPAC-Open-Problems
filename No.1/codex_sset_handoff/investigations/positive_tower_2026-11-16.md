# ZFC での逆向き修復列と停止条件

2026年11月16日。通常の Hom による small coorthogonality を扱う。既存の結果は前提として採用する。§§1–7 の直接証明は `INTERNAL_PROOF_CHECKED`。一般の P の証明も非停止例も得ていない。

小圏 C に対する K=Set^{C^op} と、射の集合 S={s_i:U_i→V_i} を固定する。A={X:Hom(X,s_i) が全単射 for all i} と置く。A は K の小余極限に閉じる。

本稿は、一意性を最初から組み込んだ修復関手 T と、その正規化 F を構成する。F の逆向き超限列が停止することは、個々の標的の A-coreflection の存在と同値である。したがって停止条件は元問題を解決するために実際に十分であり、正規化した構成については必要でもある。ZFC だけで全標的の停止を導くサイズ評価は未解決である。

## 1 一段階の修復関手

B∈K に対して H_i=Hom(B,U_i)、K_i=Hom(B,V_i)、j_i=(s_i)_*:H_i→K_i とする。集合で添字付けた冪は K の積である。次の pullback で T B と t_B:T B→B を定める。

$$
T B=B\times_{\prod_i(V_i^{K_i}\times U_i^{H_i})}\prod_i U_i^{K_i}.
$$

B からの射はすべての h:B→V_i および g:B→U_i による evaluation、右側の射は (s_i^{K_i},j_i^*) である。すなわち T B は、射 t_B と π_{i,h}:T B→U_i を持ち、

$$s_i\pi_{i,h}=h t_B,\qquad \pi_{i,s_i g}=g t_B$$

を満たす普遍対象である。第二式が既存の持上げとの整合性を強制する。

射 b:B→D に沿って h:D→V_i を hb:B→V_i に引き戻すことで T b が定義される。従って T は関手、t:T⇒Id は自然変換である。

**補題 1.** 次は同値である。

1. B∈A。
2. t_B は同型。
3. t_B は section を持つ。

**証明。** section σ:B→T B があれば、h↦π_{i,h}σ は j_i の右逆であり、第二の整合式によって左逆でもある。従って j_i は全単射。逆に j_i が全単射なら、各 h の唯一の持上げを評価射に使うことで σ を得る。各座標 π_{i,h} は第二式で t_B から決まるので σt_B=1 でもある。□

**補題 2.** X∈A なら Hom(X,t_B) は全単射である。

**証明。** a:X→B に対し、各 ha:X→V_i は唯一の持上げを持つ。その持上げを π_{i,h} の座標にする。h=s_i g の場合は ga が持上げなので第二式も満たす。座標ごとの一意性から全体も一意。□

以下、この性質を持つ射を A-equivalence と呼ぶ。これは弱同値や homotopy の用語ではなく、Hom(X,-) の全単射性だけを意味する。

**補題 3.** T は co-well-pointed、すなわち T(t_B)=t_{T B} を満たす。

**証明。** 両辺は T²B→T B。B 成分は自然性から等しい。座標 (i,h) で比較すると、T(t_B) の座標は T²B の π_{i,h t_B} である。一方 h t_B=s_iπ_{i,h} なので、T(T B) に課した第二式から

$$\pi_{i,h t_B}=\pi_{i,h}\,t_{T B}.$$

これがもう一方の座標である。□

この構成は Kelly の well-pointed endofunctor による orthogonality の構成を双対にしたものに対応する。ただし本節の式と証明は直接記した。[Kelly 1980, §§5, 9–10](https://doi.org/10.1017/S0004972700006353)。

## 2 通常の逆列から分かることと分からないこと

B_0=B、B_{α+1}=T B_α、極限段階 B_δ=lim_{α<δ}B_α とする。各集合順序数までの構成は ZFC で可能である。補題 2 と representable Hom の極限保存から、すべての B_α→B は A-equivalence である。

どこかで t_{B_α} が同型なら B_α∈A なので B_α→B は coreflection になる。しかし、coreflection が存在すればこの生の列が必ず停止する、とはここでは証明していない。任意の co-well-pointed functor についての一般論では、対応する順方向の主張に Kelly Remark 5.4 の反例がある。同反例の圏は presheaf 圏ではなく、本稿の T の反例としては使わない。

次節では coreflection の存在と停止の同値が成り立つように列を正規化する。

## 3 商閉包の trace による正規化

Q を、A の対象から通常の全射を受ける対象の充満部分圏とする。

$$Q=\{Y:\exists A_0\in A,\ A_0\twoheadrightarrow Y\}.$$

presheaf 圏では通常の全射、regular epi、成分ごとの全射が一致する。

**補題 4.** Q は商と小余極限に閉じ、K の monocoreflective な充満部分圏である。

**証明。** 商閉性は全射の合成から従う。Q の小図式 (Y_j) に対し各 A_j↠Y_j を選ぶと、⊔_j A_j→colim_j Y_j は全射である。⊔_j A_j∈A なので余極限も Q に入る。空図式では初対象が A に入ることを使う。集合個の証人 A_j の選択は、S で定義されたクラスに対する ZFC の Collection と Choice で行える。

B のすべての Q-部分対象の和集合を QB⊆B とする。部分対象は集合個であり、この和集合は余積の像だから Q に属する。Y∈Q から B への射の像は Y の商なので Q に入り、従って QB を経由する。包含が mono なので因子化は一意。これで q_B:QB↪B が coreflection となる。Q はこの具体的な trace 関手の記号としても用いる。□

**補題 5.** u:X→Y が A-equivalence で Y∈Q なら u は K の全射である。X∈Q はこの結論に不要。

**証明。** 全射 a:A_0↠Y、A_0∈A を選ぶ。A-equivalence により a=uv となる v:A_0→X がある。uv が成分ごとに全射なので u も全射。□

Q 上の関手と自然変換を

$$F=QT|_Q,\qquad e_B=t_Bq_{T B}:F B\longrightarrow B$$

で定める。補題 2 と Q の coreflection の普遍性から e_B は A-equivalence。従って補題 5 により全射である。また e_B が section を持てば t_B も持つので、補題 1 より

$$e_B\text{ is iso}\quad\Longleftrightarrow\quad B\in A.$$

**補題 6.** F も co-well-pointed である。

**証明。** F²B→F B の二射 e_{F B} と F(e_B) を、mono q_{T B}:F B→T B で後合成して比較する。自然性から

$$q_{T B}e_{F B}=t_{T B}\,T(q_{T B})\,q_{T F B},$$

$$q_{T B}F(e_B)=T(t_B)\,T(q_{T B})\,q_{T F B}.$$

補題 3 によって右辺は等しい。□

Q の極限は Q(lim_K -) で計算できる。これは右随伴 Q による具体的な構成である。

## 4 停止と coreflection の同値

任意の B∈K に対し、以下の逆向き列を作る。

$$B_0=QB,\quad B_{α+1}=F B_α,\quad B_δ=Q(\lim_{α<δ}B_α).$$

すべての遷移射 B_β→B_α は A-equivalence である。後続段階は上記の e、極限段階は

$$\operatorname{Hom}(A_0,Q\lim B_α)\cong\lim\operatorname{Hom}(A_0,B_α)$$

と帰納法による。各 Hom 集合は Hom(A_0,B) に同一視され、遷移はその恒等写像になる。特に、補題 5 によりすべての遷移射は K の全射である。一般の全射の逆極限が全射を保つと仮定しているのではない。

**定理 7.** 次は同値である。

1. B に A-coreflection が存在する。
2. 上の列のある後続遷移 B_{α+1}→B_α が同型になる。
3. 列の全対象の underlying total carrier の濃度に、集合基数による共通上界がある。

**証明。** 2⇒1 は補題 1 の F 版と B_α→B の A-equivalence から従う。

1⇒2：r:R→B を coreflection とする。R∈A なので、各段階の A-equivalence によって一意な r_α:R→B_α がある。任意の A_0∈A について Hom(A_0,r_α) は全単射であるから、r_α も coreflection、従って A-equivalence である。B_α∈Q なので r_α は全射である。

したがって全 B_α は固定した R の商である。β>α なら ker(r_β)⊆ker(r_α)。R の congruence は集合個しかないので、この降下列はどこかの隣接段階で等しくなる。presheaf の全射の kernel congruence が等しければ、その間の遷移は同型である。□

1⇒3 は各 r_α の全射性から従う。3⇒2 を直接見るには、κ を共通上界である無限基数とし、λ=(2^κ)^+ 段階を取る。全射 B_λ→B_α（α<λ）の kernel congruence は高々 2^κ 個しかない。隣接段階で一度も同型にならなければ、これらは厳密に降下する λ 個の異なる congruence を与え、矛盾する。□

この定理の 1⇒2 は、未構成の R が存在すると仮定した条件付き証明である。R を ZFC で先に作ったわけではなく、全列の上界を導く無条件の証明にもなっていない。

## 5 一意性は保持され 存在性が残る

I={X:Hom(X,s_i) が単射 for all i} とする。I は通常の商に閉じる。実際、全射 X↠Y で前合成すれば、Y から U_i への二射の一致を X 上で検査できる。A⊆I なので Q⊆I。

したがって正規化した列では、極限段階を含むすべての B_α に一意性が成立する。全射遷移により、Hom(B_α,U_i) と Hom(B_α,V_i) は後の段階の Hom に単射で移る。

さらに各 h:B_α→V_i は、T B_α の座標 π_{i,h} を Q(T B_α) に制限することで B_{α+1} 上で持ち上がる。つまり、各段階の存在性の欠如は次段階で修復される。

極限段階 δ で、すべての h:B_δ→V_i がある前段階を経由するなら B_δ∈A となる。ただし、この段階因子化条件は十分条件であり、必要条件だとは主張しない。新しい h が現れても、それらが別の理由で既に持ち上がる可能性がある。

ここに残る問題は、固定した S と B から全列のサイズ上界を得ること、または新しい h の持上げを一斉に保証することである。S が集合であることだけからは、両者ともまだ導けていない。

**補題 8.** Q の対象間の A-equivalence は Q 内部の mono である。

**証明。** u:X→Y が A-equivalence、v,w:Z→X が Q 内の射で uv=uw とする。A_0∈A からの全射 a:A_0↠Z を選ぶ。Hom(A_0,u) の単射性から va=wa であり、a が K の epi なので v=w。□

従って正規化列の各 B_α→B_0 は Q 内部の部分対象である。**Q が well-powered なら列は停止する。** ただし、これらの射は K では全射であり、一般には K の mono ではない。母圏 K の well-poweredness だけで Q の部分対象を数えることはできない。

## 6 境界条件と証明の範囲

- S が空または同型だけなら T=Id、Q=K で列は直ちに停止する。
- すべての s_i が mono なら t_B も mono であり、生の修復列は固定 B の部分対象の降下列になる。well-poweredness から停止し、既存の mono テストの肯定結果を回復する。
- 通常の逆極限に新しい射が現れる事実だけでは、本稿の特殊な列の非停止は証明できない。
- 本稿は presheaf 圏における新しい条件付き構成と停止判定を与える。一般の P、ZFC 独立性、ある具体的な列の非停止は未証明である。

参照した一次資料：G. M. Kelly, *A unified treatment of transfinite constructions for free algebras, free monoids, colimits, associated sheaves, and so on*, Bull. Austral. Math. Soc. 22 (1980), 1–83, §§5–10, とくに Proposition 5.3, Remark 5.4, Proposition 7.3。2026年11月16日に本文を確認。上の presheaf 内の正規化と証明は、本稿で直接展開したものとして区別する。

## 7 実際の修復列で新しい射が現れても停止する例

本節の母圏は **Ab** である。上記の積・pullback・商閉包・trace による構成を Ab 内で直接行う。presheaf の反射表示が Q や全射を保存すると仮定して移送した例ではない。本節の状態は `INTERNAL_PROOF_CHECKED`。

素数 p を固定し、E=Q/Z と s=p_E:E→E を唯一のテストとする。E は injective cogenerator であり、Hom(X,p_E)=Hom(p_X,E) なので

$$A=\{X:p_X\text{ is iso}\}=\mathbf Z[1/p]\text{-Mod}$$

である。R_0=Z[1/p] と書く。A の商閉包 Q は p-divisible groups の圏である。一方の包含は明らかである。逆に p-divisible group の任意の元は、p 乗根を順次選ぶことである射 R_0→B の像に入る。これらの射の余積は B への全射になる。

**命題 9.** B が p-divisible なら、F B=Q(T B) は自然に B と同型であり、この同型で e_B:F B→B は p_B に対応する。

**証明。** H=Hom(B,E) とする。射

$$j_B:B\longrightarrow T B,\qquad c\longmapsto (pc,(h(c))_{h\in H})$$

を定める。T の条件は p h(c)=h(pc) と (pg)(c)=g(pc) なので満たされる。E が cogenerator であるため j_B は mono である。その像は p-divisible なので Q(T B) に含まれる。

逆に r:R_0→B の T B への唯一の持上げを計算すると、座標 h での値は

$$x\longmapsto h(r(x/p))$$

となる。従って持上げ全体は x↦j_B(r(x/p)) であり、その像は j_B(B) に含まれる。T B の任意の p-divisible 部分群は R_0 からの射の像で生成されるので Q(T B)⊆j_B(B) となる。最後に t_Bj_B=p_B。□

B=C_{p^∞}=Z[1/p]/Z と取る。正規化した修復列は有限段階で

$$\cdots\xrightarrow p C_{p^\infty}\xrightarrow p C_{p^\infty}\xrightarrow p C_{p^\infty}$$

となる。ω 段階の K 内の逆極限を L とする。L 上の p 倍写像の逆は座標を一つずらす写像であるから、p_L は同型である。従って L∈A⊆Q であり、Q による切り取りは不要で、修復列は ω 段階で停止する。

それでも L→E には、どの有限段階の射も経由しないものがある。実際、p 以外の素数による乗法も L 上で同型だから L は Q-vector space である。

$$z=(0,1/p+Z,1/p^2+Z,\ldots)\in L$$

を取り、Q-linear functional χ:L→Q で χ(z)=1 を満たすものを選ぶ。χ と Q↠Q/Z の合成を h とする。ℓ≠p を素数とし、π_n:L→C_{p^∞} を第 n 座標とすると

$$p^n z/\ell\in\ker\pi_n,\qquad h(p^n z/\ell)=p^n/\ell+Z\ne0.$$

従って h はどの π_n も経由しない。しかし L∈A なので h の s に沿う持上げは存在し、一意である。

この例は、**実際の正規化した修復列に新しい射が現れることと、列が停止しないことは別である**と示す。§5 の段階因子化条件は停止の十分条件にとどまる。従って一般の停止問題を「逆極限で新しい射が現れる」という現象だけで否定することはできない。

また有限段階の p:C_{p^∞}→C_{p^∞} は、K=Ab では全射、Q 内部では mono だが同型ではない。実際、kernel Z/p への p-divisible group からの射は零しかない。この例は、正規化した遷移射の二つの性質だけから直ちに同型だと結論することも排除する。
