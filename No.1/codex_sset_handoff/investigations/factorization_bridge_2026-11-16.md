# 固定テストへの接続：射の圏と一意持上げによる因子分解

2026年11月16日。ordinary Hom による Adámek–Rosický Problem 1 の命題を P とする。既存の証明済み結果は前提として採用し、再監査は行わない。本稿の新しい直接証明は `PROOF_RECONSTRUCTED`。新規性や形式検証は主張しない。

$$T=\{A\in\mathrm{Ab}:\operatorname{Hom}(A,Z)=0\},\quad
F=\{K:\operatorname{Hom}(A,K)=0\ (A\in T)\},\quad S_0=Z^{(\omega)}.$$

前段階で得た条件を D と書く：固定した S₀ の通常の単射 i:S₀↪K で K∈F、coker i∈T を満たすもののサイズが、任意の集合基数を超える。

**今回の結論。** D⇒¬P という条件付き還元は得られていない。一方、P を集合個の射で余生成する orthogonal factorization system の存在と同値に書き換え、D の証人をそのまま射の圏へ移す案には強い排除条件を得た。特に、以前の T-内部単射をテストにする直接案では、非自明な D の証人は一意持上げ条件を満たせない。

## 1. 対象の coorthogonality と射の一意持上げを区別する

この節では K は局所可呈示圏、Σ は K の射の集合とする。e:A→B と f:U→V について、e ⊥_u f は、任意の可換正方形

$$f a=b e\qquad(a:A\to U,\ b:B\to V)$$

に対し、g:B→U で ge=a、fg=b を満たすものがちょうど一つ存在することを表す。これは通常の射同士の orthogonality で、弱い持上げ性ではない。

$$L_\Sigma=\{e:e\perp_u f\ (f\in\Sigma)\},\qquad
R_\Sigma=\{r:e\perp_u r\ (e\in L_\Sigma)\}.$$

射の圏 K^→ で

$$\rho_f:(1_U:U\to U)\longrightarrow(f:U\to V),\qquad
\rho_f=(1_U,f)$$

と置く。Hom_{K^→}(e,1_U) は K(B,U) と同一視でき、Hom_{K^→}(e,f) は上の可換正方形の集合である。従って

$$L_\Sigma={}^\perp_{K^\to}\{\rho_f:f\in\Sigma\}.\tag{1}$$

右辺は射の圏における、集合個のテストへの ordinary-Hom coorthogonality class である。

## 2. P と集合個の右テストによる因子分解の同値

**定理。** 次の二つの全称命題は同値である。

1. P：任意の局所可呈示 K と射の集合 Σ について {}^⊥Σ は coreflective。
2. 任意の局所可呈示 K と射の集合 Σ について、(L_Σ,R_Σ) は orthogonal factorization system をなす。

ここで 2 は、すべての射 b が b=rℓ、ℓ∈L_Σ、r∈R_Σ と因子分解できる、という存在を含む。右側のテスト集合から L を定める点に注意する。

### 2.1 P から因子分解へ

K^→ も局所可呈示なので、P と (1) より L=L_Σ は K^→ で coreflective。b:X→Y の coreflection を (a,d):(ℓ:A→M)→b とする。

任意の Z について 1_Z∈L であり、

$$\operatorname{Hom}_{K^\to}(1_Z,\ell)=K(Z,A),\qquad
\operatorname{Hom}_{K^\to}(1_Z,b)=K(Z,X).$$

coreflection の普遍性より K(Z,a) が常に全単射なので a は同型。従って coreflection を

$$X\xrightarrow{\ell}M\xrightarrow rY,\qquad b=r\ell$$

という形で取れる。

r∈R を示す。e:A'→B'∈L と、u:A'→M、v:B'→Y、ru=ve を取る。pushout P=M⊔_{A'}B' を作り、j:M→P、k:B'→P、w:P→Y とする。L は pushout と合成で閉じるので jℓ:X→P∈L。coreflection により一意な h:P→M があり、

$$hj\ell=\ell,\qquad rh=w.$$

hj は ℓ から b への射の恒等因子化と同じ因子化を与えるため、coreflection の一意性から hj=1_M。従って hk が所望の lift である。別の lift g があれば、(1_M,g) の pushout から得る P→M も同じ普遍条件を満たすので h と一致する。lift は一意。

R=L^{⊥_u} は定義通りであり、Σ⊆R だから {}^{⊥_u}R⊆{}^{⊥_u}Σ=L。逆包含は自動なので両クラスは互いの orthogonal である。

### 2.2 因子分解から P へ

初対象からの射 0→B を

$$0\longrightarrow C\xrightarrow rB$$

と因子分解する。0→C∈L は C∈{}^⊥Σ と同値。任意の A∈{}^⊥Σ に対し、0→A∈L と r∈R の一意持上げが、任意の A→B の C を通る一意因子化を与える。従って r は coreflection。∎

この定理は P を証明したものではなく、未解決の存在条件を等価に移したものである。固定 K の P_K だけから K の因子分解を導いたのでもない。前向きには P_{K^→} を使用した。

## 3. 最も自然な右テスト q:Q→Q/Z は ZFC で処理できる

既存の結果 W_Z={C:Hom(C,Z)=Ext(C,Z)=0}={0} を前提として使う。

**定理（ZFC）。** q:Q↠Q/Z に対して

$$L_{\{q\}}=\{e:e\text{ は通常の全射で }\ker e\in T\},\tag{2}$$

$$R_{\{q\}}=\{r:\ker r\in F\}.\tag{3}$$

### 3.1 左クラスの計算

e:A→B が q に一意左持上げ性を持つとする。N=ker e、I=im e、C=coker e と置く。

任意の h:N→Z を Q に入れ、Q の injectivity で a:A→Q に延長する。qa は N 上で零なので I→Q/Z を誘導し、Q/Z の injectivity で b:B→Q/Z に延長できる。e⊥_u q から a=ge となるため h=0。従って N∈T。

N∈T である通常の全射 A↠I は q に一意左持上げ性を持つ。従って e の持上げ性から、包含 I↪B にも同じ持上げ性が従う（I 上の正方形を A に引き戻し、A↠I の全射性を使う）。

任意の c:C→Q/Z を B に引き戻し、I→Q を零にした正方形を考える。得られる lift B→Q は I 上で零なので C→Q を与える。ゆえに Hom(C,Q)→Hom(C,Q/Z) は全射。一意性は Hom(C,Z)=0 を与え、Ext(C,Q)=0 と完全列から Ext(C,Z)=0。既存の W_Z={0} より C=0。これで (2) の必要性を得る。

逆に e が全射で N∈T なら、正方形の上辺 a は N を ker q=Z に写すので N 上で零。従って a は B に一意に降り、所望の lift となる。

### 3.2 右クラスと因子分解

ker r∈F なら、(2) の e の核から ker r への写像は零なので、任意の正方形に一意 lift がある。逆に、各 A∈T の射 A→0 は (2) に属するため、それらに右直交する r は Hom(A,ker r)=0 を満たす。これで (3) を得る。

任意の b:X→Y の因子分解は明示できる：

$$X\twoheadrightarrow X/t(\ker b)\longrightarrow Y.\tag{4}$$

左射の核は T に属し、右射の核は (ker b)/t(ker b)∈F。従って (2)–(3) は ZFC で orthogonal factorization system をなす。射の圏での L_{\{q\}}-coreflection も (4) で与えられる。これは T の well-poweredness を仮定しない。

**含意。** T 内部単射は (3) に属するが、その巨大化はこの因子分解の不存在を意味しない。D が真であっても、この固定テストによる反例は得られない。

## 4. D の証人が実際に与えるもの

Ab^→ の充満部分圏

$$I=\{e:A\to B:\operatorname{coker}e\in T\}$$

を取る。Hom_{Ab^→}(e,(0→Z))=Hom(coker e,Z) なので、I は一つの mono test への coorthogonality class であり、ZFC で monocoreflective。

I に右 Hom-null な射の対象は、ちょうど (0→F')、F'∈F である。実際、すべての 1_A が I に入ることから始域が零でなければならず、残る条件は Hom(T,F')=0 となる。

従って、I の射 (a,b):e→e' が内部単射であることは、a が通常の単射で ker b∈F となることと同値である。これは Ab^→ における torsion pair の核判定を、そのまま用いたものである。

D の各証人 i:S₀↪K は I の対象であり、

$$(1_{S_0},0):i\longrightarrow b_0=(S_0\to0)\tag{5}$$

は I-内部単射である。つまり D は、固定 b₀ の I 内部部分対象を本当に非有界にする。

しかし (5) の i を L_Σ の対象にするには、さらに i⊥_u f をすべての固定テスト f∈Σ について要求しなければならない。次節は、その段階で多くの候補が排除されることを示す。

逆向きの対照も明示できる。f=(0→Z) を選ぶと L_{\{f\}}=I であり、D の証人はすべて条件を満たす。しかし b₀ 自身が I に属するので、その coreflection は恒等射である。(5) の因子化では K 全体が零へ写り、サイズ下界は何も残らない。従って「無界な D の証人が固定小テストのクラスに入る」という条件だけでは不足する。

## 5. テストの核が強制する双対条件

### 5.1 一意持上げは核への Hom の同型を強制する

**補題（ZFC）。** i:S₀↪K と f:U→V について i⊥_u f なら、H=ker f に対して

$$i^*_H:\operatorname{Hom}(K,H)\xrightarrow{\sim}\operatorname{Hom}(S_0,H).\tag{6}$$

**証明。** 上辺を S₀→H↪U、下辺を K→V の零射にした正方形を使う。lift は H に値を取り、存在・一意性がちょうど (6) である。∎

H の任意の retract H' についても Hom(i,H') は同型となる。C=K/i(S₀) とすれば、特に Hom(C,H)=0 である。

### 5.2 Z が核の retract なら非自明な D の証人は入らない

**補題（ZFC）。** K∈F とし、Hom(i,Z) が同型なら i:S₀↪K は同型である。

**証明。** S₀ は整数双対に関して reflexive である。実際 S₀*=Z^ω、可算 Specker 定理より (Z^ω)*=Z^(ω) で、自然な評価射 S₀→S₀** が同型になる。

Hom(i,Z) の同型と評価射の自然性から、K→K**→S₀**≅S₀ という i の retraction r が得られる。K≅S₀⊕J と分裂し、Hom(i,Z) の同型から Hom(J,Z)=0。J∈F でもあるので J∈T∩F={0}。∎

**帰結。** ker f が Z を retract として持つなら、D の証人 i∈L_{\{f\}} は恒等拡大だけである。特に ker f∈F が非零ならこの結論が適用できる。非零 F-群 H では Hom(H,Z)≠0 であり、その非零像 dZ への全射が分裂するので Z が retract になるからである。

これは以前の T-内部単射をテストにする案をすべて処理する。核が零なら f は通常の mono であり、ρ_f も Ab^→ の mono。その集合への coorthogonality は既存の ZFC の肯定結果に入る。核が非零 F なら、非自明な D の証人は条件を満たさない。

対照として、通常の包含 S₀=Z^(ω)↪Z^ω は非自明な F-dense extension である。Z^ω∈F、かつ可算 Specker 定理より整数双対の制限は Z^(ω)↪Z^ω となり単射なので、余核は T に属する。しかしこの制限は全射ではないため、上の一意持上げ条件は満たさない。非自明な dense extension 自体を否定した結果ではない。

### 5.3 核に torsion があれば D の証人のサイズは連続体以下

**補題（ZFC）。** K∈F、S₀↪K、C=K/S₀ とする。C が p-divisible なら |K|≤2^ℵ₀。

**証明。** K=S₀+pK なので帰納的に K=S₀+p^nK。従って K/p^nK は可算である。一方 P=∩_n p^nK は p-divisible：K の torsion-free 性による p 乗根の一意性を使うと、x∈P の K 内の p 乗根も P に属する。従って Hom(P,Z)=0 であり、P≤K∈F から P=0。

ゆえに K は ∏_{n≥1}K/p^nK に単射で入り、右辺のサイズは高々 2^ℵ₀。∎

ker f が非零 torsion を持てば、ある Z/p がその部分群になる。(6) の単射性から Hom(C,ker f)=0、従って Hom(C,Z/p)=0。これは C/pC=0 を意味するので補題が適用できる。

同様に ker f が Q を部分群として含めば、Hom(C,Q)=0 より C は torsion。K の rank は S₀ の rank 以下となり、torsion-free な K 自身が可算となる。

### 5.4 既存の剛体群 G_b を核に替える案も処理できる

**補題（ZFC）。** 非零 torsion-free 群 H について、End(H)=Z·1_H、かつ H^ω→H のすべての準同型が有限個の座標を経由するとする。K∈F と Hom(i,H) の同型から、i:S₀↪K は同型である。

**証明。** Hom(S₀,H)=H^ω。仮定から Hom(H^ω,H)=Z^(ω) となり、評価射

$$S_0\longrightarrow\operatorname{Hom}(\operatorname{Hom}(S_0,H),H)$$

は同型。§5.2 と同じく、Hom(i,H) の同型から K→S₀ の retraction を得る。分裂核 J は Hom(J,H)=0 を満たす。Z↪H なので Hom(J,Z)=0、さらに J∈F だから J=0。∎

既存の p進群 G_b には End(G_b)=Z と slender 性が証明済みである。[End の計算](algebraic_candidates_2026-11-15.md)、[slender 性](finite_coordinate_trial_2026-11-15.md)。従って ker f=G_b、または G_b を retract として含む核でも、非自明な D の証人は L_{\{f\}} に入らない。単に核を Z から G_b に取り替えるだけでは接続できない。

## 6. F 所属をそのまま付加する方法は余極限閉性に反する

### 6.1 射の圏

F の対象間の射 i:S→K で coker i∈T となるもの全体を考える。非自明な D の証人 i:S₀↪K と 1_{S₀} はこのクラスに入る。二射

$$(1_{S_0},i),(0,0):1_{S_0}\rightrightarrows i$$

の Ab^→ での coequalizer は (0→C)、C=coker i≠0。C∈T なので C∉F である。このクラスは coequalizer 閉でなく、どんな射のクラスへの coorthogonality class にもならない。

### 6.2 S₀ を固定した coslice

S₀↓Ab で、F-dense extensions だけを集めても同じ問題が起こる。i の自身との coproduct は S₀→K⊔_{S₀}K であり、

$$K\amalg_{S_0}K\cong K\oplus(K/i(S_0)).$$

同型は [(x,y)]↦(x+y,[y]) で与えられる。右辺は非零 T-群 C を部分群として含むので F に属さない。これは i が pure であっても変わらない。

これらは文字通りの F-始域／終域条件の排除であり、別の図式の核などに F を符号化するすべての方法を排除したものではない。

## 7. 固定した小さいデータでテストへの射が決まる場合の上界

**補題（ZFC）。** Σ={f_j:U_j→V_j} は Ab の射の集合、A={}^⊥Σ とする。S と B を固定する。X∈A、a:S→X、h:X→B が与えられ、すべての j について Hom(X,U_j)→Hom(S,U_j) が単射であるとする。このとき h は、サイズに X に依存しない上界を持つ Q∈A を経由する。

**証明。** 各 j と s∈Hom(S,U_j) に対し、s の X への延長があればその唯一の延長を、なければ零射を座標に取る。h と合わせて

$$X\longrightarrow B\times\prod_j U_j^{\operatorname{Hom}(S,U_j)}$$

を作り、その通常の像を Q、全射を q:X↠Q とする。任意の v:Q→V_j を q と合成すると、X∈A より唯一の lift u:X→U_j がある。u は上で記録した座標の一つなので Q に降りる。一意性は q の全射性から従う。従って Q∈A。固定した積の部分群なのでサイズは一様に有界。∎

特に a の余核が T に属し、すべての U_j∈F なら仮定を満たす。この種の観測だけでは巨大な dense extension のサイズを因子化先に保持できない。

さらに Ab 自体では、すべてのテスト始域 U_j∈F の場合、A は常に ZFC で coreflective である。全 f_j が mono なら既存の mono-test 定理を使う。非 mono が一つあれば、その核は非零 torsion-free 群なので Z を含み、A の対象 X は Hom(X,Z)=0 を満たす。従って全 j について Hom(X,U_j)=0 となり、

$$A=T\cap\bigcap_j\{X:\operatorname{Hom}(X,V_j)=0\}.$$

これは直和・通常の商に閉じる null class であり、部分群の和による coreflector を持つ。

## 8. 残った条件と今回の停止点

今回の直接案は、D の証人 i:S₀↪K を射の圏の対象として固定 b₀=(S₀→0) に写し、L_Σ の coreflection からサイズ上界を引き出すものだった。

これをサイズ非有界な族で実行するには、少なくとも次が必要になる。

- Σ の全射が通常の mono ではないこと。全て mono なら ρ_f も mono で、ZFC で coreflective。
- 各非零 ker f が torsion-free かつ Z-null であること。非零整数双対があれば Z が retract となり、torsion があれば連続体の上界が生じる。
- Q を含む核、および G_b のように §5.4 を満たす retract を持つ核も避けること。
- そのような固定 H=ker f に対し、無界な D の証人で Hom(K,H)→Hom(S₀,H) が同型になることを、別途示すこと。D 自体が与えるのは整数双対の単射性であり、この H に対する全単射性ではない。
- 最後に、その証人から仮想的な coreflection への因子化が巨大な部分を消さないことを示すこと。所属の条件を満たすだけではサイズ下界はまだ出ない。

**この二つの最後の条件は未証明である。** 核を非零 F-群や既存の G_b に取る方法は明確に排除され、自然な q:Q→Q/Z の持上げクラスにも ZFC の因子分解がある。したがって、以前の内部単射の塔をそのまま射の圏へ運ぶ方法はここで止まる。

P と因子分解の同値は今後も使えるが、D⇒¬P の一般還元が存在するとも存在しないとも証明していない。異なる核や、群を図式の内部に配置して因子化を制御する別の符号化は未解決である。非 well-poweredness、P の否定、ZFC 独立性を今回証明したとは主張しない。
