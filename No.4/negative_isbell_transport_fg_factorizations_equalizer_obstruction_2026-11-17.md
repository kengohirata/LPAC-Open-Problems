# Problem 4：N の下での反例探索 — Isbell 移送、有限生成テスト、等化子の障害

2026-11-17。

**状態：PROOF_RECONSTRUCTED / NEGATIVE SEARCH INCOMPLETE。P4 の反例はまだ得ていない。以下の直接導出は自己点検段階であり、独立査読・形式検証・新規性確認は未実施。非反射性の主張は、No.1 の採用済みだが独立監査前の非余反射性証明を入力にする。**

**同日後続：H_fg は現在の入力の下で反例候補から除外された。** [filtered-colimit 閉性による棄却](eqc_obstruction_sufficiently_filtered_colimits_2026-11-17.md) を参照。N+(NC) の下で H_fg の一般等化子閉性は偽である。以下の構成・非反射性・特殊な等化子の証明は保持するが、一般等化子閉性を証明して反例を完成させるという末尾の方針は採用しない。

## 0. 到達点

N =「非可算可測基数が存在しない」とする。

1. No.1 の非 coreflective な C⊆K を、N の下で別の**前層圏 P**の全小極限に閉じた非 reflective な D として実現した。単に K^op を母圏とするのではなく、Isbell 埋め込みを各成分に適用する。従って以前の『双対母圏が局所可呈示でない』という障害は、この追加構成で越えられる。
2. 非反射性を目撃する固定 source X は、この P で **二元生成、従って finitely generated**。ただし finitely presentable とは主張しない。
3. D 自身の directed-union 閉性は、split monos の可算鎖で実際に失敗する。
4. X からの射が D を経由する対象のクラス T_X は、全小積・retracts・全 directed unions に閉じ、X で弱始集合を持たない。しかし **等化子閉性の具体的反例**を得たので、T_X は P4 の反例候補として棄却する。
5. T_X を、**全 finitely generated source** からの射を検査する H_fg に置き換えた。H_fg は全小積・retracts・全 directed unions に閉じ、なお X で弱始集合を持たない。
6. H_fg の finitely generated objects は、ちょうど D の finitely generated objects。上の T_X の反例に現れる対象は H_fg から除外される。
7. H_fg は (i) domain が finitely generated な等化子、(ii) codomain が D に属する等化子に閉じる。一般の等化子閉性は未証明であり、ここが現在の残課題。
8. 別の直接計算として、D-objects の split-mono 鎖の union V で、各成分の Hom(V_i,Ω) が空になるものを構成した。よって『union 後も D-object に埋め込める』という近道は N の下で偽。Aronszajn 木・diamond・V=L は不要で、部分単射の逆系だけを使う。

**結論していないもの：N⇒¬P4、V=L⇒¬P4、P4 の独立性、H_fg の全小極限閉性。**

---

## 1. No.1 からの入力と記号

Ω=ω、M_1=End_Set(Ω)、J=(0⇉1) とし、

    K=(M_1-Set)^J = Set^(M_1×J)

と置く。対象は Z=(Z_0 --p_Z,q_Z--> Z_1)。

H_1(A)=Hom_(M_1)(A,Ω)。C⊆K は

    Z_0 が有限支持 M_1-set、かつ
    H_1(p_Z):H_1(Z_1)→H_1(Z_0) が全単射

を満たす対象の full replete subcategory。

有限支持とは、各 z に有限 S⊆Ω が存在し、m|S=n|S なら mz=nz となること。

No.1 では C={}^⊥{τ,σ} と固定二射によって表示している。従って C は K の全小余極限に閉じる。固定標的は

    B=(Ω⇉1)。

**採用する No.1 の入力 (NC)。** ZFC+N の下で C↓B は弱終集合を持たない。

入力元：

    ../No.1/codex_sset_handoff/investigations/
        parallel_actions_counterexample_2026-11-16.md

同ノートの §1.1、§§5–6 を再読した。非反射性の根拠は、Y_κ→B が C 内の任意の Z を経由すると

    |[0,κ]| ≤ |Hom_(M_1)(Z_0,Ω)|

となるという任意因子化に対する下界である。今回その証明を独立査読したとは扱わない。

B∉C は直接確認できる：H_1(1)=∅、H_1(Ω)={id}。

---

## 2. N の下で、双対を再び前層圏に入れる

M_2 は同じ集合 End(Ω) の別コピーとし、M_1 と区別する。

    F:Set^op→M_2-Set,    F(S)=Ω^S

を後合成作用で定める。N の下で Isbell の定理により

    Hom_(M_2)(Ω^S,Ω^T) ≅ Set(T,S)。                   (I)

空集合も含む。特に H_2(F(S))=Hom_(M_2)(Ω^S,Ω)≅S。

これは No.1 §1.1 の可算完備 ultrafilter による証明と同じ入力。一次文献 Isbell, Adequate subcategories, §2.5, pp.549–550 を再確認した。

S_0=M_1×J と置き、

    P=(M_2-Set)^(S_0^op)

とする。これは小圏上の前層圏なので locally finitely presentable。

F の成分ごとの適用により

    E:K^op→P,
    E(Z)_i=Ω^(Z_i)

を得る。元の構造射・M_1作用は前合成により向きを逆転し、M_2作用は後合成である。両作用は可換。

### 補題2.1

N の下で E は fully faithful。さらに、K の全小余極限を P の小極限に送る。

証明：前者は (I) を各成分に適用し、自然性を照合する。後者は Set の colimit に対する Ω^(-) の limit への変換を成分ごとに使う。後者だけなら N は不要。□

D を E(C^op) の replete image とする。

C の余極限閉性と E の性質により、D は P の全小極限に閉じる。特に全小積、等化子、retracts に閉じる。

    X=E(B)

と置くと、fullness から

    (X↓D) ≃ (C↓B)^op。

従って (NC) の下で X↓D は弱始集合を持たない。D は P に反射的でも弱反射的でもない。

**ここまででは P4 の反例ではない。Directed unions の閉性がまだなく、§4では実際の失敗を示す。**

---

## 3. 非反射性の source X は二元生成

P の二つの sorts において

    X_0=Ω^Ω=M_2,      X_1=Ω^1=Ω。

Sort 0 では id_Ω が左 M_2-作用で全体を生成する。Sort 1 では 0∈Ω が全体を生成する。二本の構造射 X_1→X_0 は、いずれも a を定数関数 c_a に送る。

従って X は P の二つの representables の余積の quotient であり、finitely generated。

直接にも、X→colim_i Z_i が directed mono-colimit への射なら、上の二つの元の像が同じ stage に現れる。各 stage は構造写像で閉じ、colimit injection は mono なので、X の全関係式はその stage で成立する。従って射がその stage に因子化する。

**注意：関係式が有限個とは言っていない。Finitely generated を finitely presentable に置き換えてはならない。**

---

## 4. D の union 閉性を壊す明示的な可算鎖

    Z_*=(Ω --id,id--> Ω)

とする。Z_*∈C。

n<ω に対し C_n=2^n・Z_*（K の copower）を取り、2^(n+1)→2^n の restriction による成分全射

    C_(n+1)→C_n

を考える。これらは K で split epi。従って E(C_n)→E(C_(n+1)) は P で split mono。

C は copowers に閉じるので全 stage は D に属する。P で

    U=colim_(n<ω) E(C_n)

を取る。各 sort の台は、2^ω×Ω 上で最初の有限個の bit のみに依存する Ω 値関数の集合として実現できる。

N と Hom(-,Ω) の colimit→limit 性から

    H_2(U_i) ≅ lim_n (2^n×Ω) ≅ 2^ω×Ω。

この同定の下で評価写像

    U_i→Ω^(H_2(U_i))

は cylinder functions の包含である。全 bit が 0 である点集合の特性関数は有限個の bit に依存しないので、この包含は全射でない。

一方 N の下では、どの power F(S) についても評価 F(S)→F(H_2(F(S))) は同型。従って U_i はどの power Ω^S とも M_2-set として同型でない。

よって U∉E(K^op)、特に U∉D。

この失敗は通常の ω-chain の split monos で起こる。単に『保存をまだ証明していない』という意味ではない。

---

## 5. 最初の拡大案 T_X：積と union を保つが、等化子で破綻

次の full replete class を考える：

    T_X={Z∈P : 全 f:X→Z が、ある D∈D を経由する}。

### 補題5.1

T_X は D を含み、全小積・retracts・全 directed unions に閉じる。

積：f:X→∏Z_i の各成分を X→D_i→Z_i と因子化し、D 内の積 ∏D_i を使う。集合個の witnesses の選択は Collection と Choice で行える。

Union：X は finitely generated なので f は一 stage を経由し、その stage での因子化を合成する。

Retract：retract の section へ合成し、D 経由の因子化後に retraction を合成する。□

### 補題5.2

(NC) の下で X↓T_X は弱始集合を持たない。

仮に {r_j:X→Z_j} が弱始集合なら、r_j を X→D_j→Z_j と因子化する。D⊆T_X なので、これら集合個の X→D_j が X↓D の弱始集合になってしまう。□

また X∉T_X。id_X が D を経由すれば X は D-object の retract、従って X∈D となるが、B∉C に矛盾する。

### 5.3 等化子閉性の直接反例

K の三対象

    B=(Ω --!,!--> 1),
    Z_*=(Ω --id,id--> Ω),
    W=(Ω --Δ,Δ--> Ω²)

を考える。Δ(a)=(a,a)。

二射

    v_i:W→Z_*,   (v_i)_0=id, (v_i)_1=π_i,  i=0,1

と

    s:Z_*→B,     s_0=id, s_1=!

がある。K で s は v_0,v_1 の coequalizer。Sort 0 は id,id の coequalizer なので Ω のまま、sort 1 は π_0,π_1:Ω²⇉Ω の coequalizer なので 1。

従って P で

    X=E(B) = Eq(E(v_0),E(v_1): E(Z_*)⇉E(W))。       (E)

E(Z_*)∈D⊆T_X。

さらに E(W)∈T_X。実際、N の下で

    Hom_P(X,E(W)) ≅ Hom_K(W,B)

で、右辺は一元集合。M_1-equivariant な Ω→Ω は id しかないからである。その唯一の射 W→B は s v_i と因子化するので、双対の X→E(W) は E(Z_*) を経由する。

よって (E) は **T_X の二対象間の二射で、等化子 X が T_X に入らない**という明示的な失敗。

これはさらに強い仮定を加えて修復できる種類の穴ではない。この構成・N・(NC) を維持する限り、同じ等化子計算が残る。

**T_X は棄却する。P4 の反例と呼ばない。**

### 5.4 構造計算としての見え方

E(Z_*) の両 sort は M_2。E(W)_0=M_2、E(W)_1=Ω^(Ω²)。二本の E(v_i) は sort 1 で f↦f∘π_i。

    f∘π_0=f∘π_1 ⇔ f は定数関数。

従って等化子の sort 1 は Ω、sort 0 は M_2 となり、正確に X を回収する。

この有限の代数的形は Ω={0,1} および Ω={0,1,2} で総当たり確認した。ただし N による無限 Isbell 埋め込みや非反射性は有限計算の結論ではない。

---

## 6. 改良候補 H_fg：全 finitely generated source を検査する

P の finitely generated objects の skeleton G を取る。これは集合：有限個の representables の余積の quotient は、固定した小さい signature において集合個しかない。

次を定義する：

    H_fg={Z∈P : 全 F∈G、全 f:F→Z が、ある D∈D を経由する}。

具体的な因子化は

    F --u--> D --v--> Z,     f=vu。

v の mono 性は仮定しない。D のサイズにも上界を仮定しない。この二点を定義に勝手に追加しない。

### 定理6.1

H_fg は D を含み、全小積・retracts・全 directed unions に閉じる。

証明は補題5.1と同じ。Union の部分で、今度は任意の検査対象 F の finite generatedness を使う。□

### 定理6.2

(NC) の下で X↓H_fg は弱始集合を持たない。従って H_fg は反射的でも弱反射的でもない。

X 自身が finitely generated なので H_fg⊆T_X。仮の弱始集合の各 X-map を D 経由にして補題5.2と同じ矛盾を得る。□

### 補題6.3

P で finitely generated な Z について、

    Z∈H_fg ⇔ Z∈D。

逆向きは D⊆H_fg。順向きは id_Z の因子化から Z が D-object の retract になることと、D の retract 閉性。□

従って、§5の反例は H_fg の等化子反例にはならない。

実際 W の両 component は可算非空なので、E(W) の各 component は M_2-set として一元生成（各 underlying domain と Ω の全単射を一つ選べばよい）。よって E(W) は P で二元生成。

しかし W∉C：H_1(Ω²) は二つの座標射、H_1(Ω) は一元集合なので H_1(Δ) は単射でない。従って E(W)∉D、補題6.3より E(W)∉H_fg。

**改善点：既に見つけた等化子反例を排除しつつ、非反射性・積・union を保つ。一般の等化子閉性を証明したわけではない。**

---

## 7. H_fg の等化子閉性について、証明できた二範囲

### 定理7.1：codomain が D の場合

Z∈H_fg、D_1∈D、a,b:Z⇉D_1 とする。その等化子 E は H_fg に属する。

証明：F∈G と x:F→E を取り、F→E→Z を F→D_0→Z と因子化する。D_0∈D。

D_0⇉D_1 の誘導二射の等化子 C は D に属する。F→D_0 は C を経由し、C→Z は元の a,b を等化するので C→E がある。これが F→E の D 経由の因子化。□

同じ証明は、codomain が D-object に mono で埋め込める場合にも使える（その mono を a,b に後合成する）。

### 定理7.2：domain が finitely generated の場合

Z,W∈H_fg、Z は P で finitely generated、a,b:Z⇉W とする。その等化子 E は H_fg に属する。

証明：補題6.3より Z∈D。

F∈G と x:F→E を取り、e:E→Z として y=ex と置く。ay=by なので pushout

    Q=Z ⊔_F Z

から W への誘導射 h:Q→W がある。Q は finitely generated：Z⊔Z の quotient であり、有限余積と quotient は finite generatedness を保つ。

W∈H_fg により h は

    Q --k--> D_1 --t--> W,    D_1∈D

と因子化する。Pushout injections j_0,j_1:Z→Q に対して c_i=kj_i:Z→D_1 と置く。c_0y=c_1y。

Z,D_1∈D なので C=Eq(c_0,c_1)∈D。y は C を経由する。また a=tc_0、b=tc_1 なので C→Z は a,b を等化し、C→E がある。これで x が C を経由する。□

### 未解決箇所の正確な形

残るのは、domain が一般の非 finitely generated H_fg-object、codomain も D に埋め込めるとは限らない場合。

F→Eq(a,b) をまず D_0→Z 経由にすることはできるが、その D_0 は大きくてよい。上の証明で必要となる

    D_0 ⊔_F D_0 → W

の domain は一般に finitely generated でないため、H_fg の定義を適用できない。

**ここで D_0 を小さく取れると勝手に仮定してはいけない。** それは No.1 の解集合障害に関わる部分そのものである。

H_fg の一般の等化子閉性が示せれば、全小積と合わせて全小極限閉性が得られ、(NC) の下で N⇒¬P4 に到達する。しかし本稿では、その等化子補題の証明も反例も得ていない。

---

## 8. 別の排除計算：union 後の対象が D に埋め込めるとは限らない

『codomain が D に埋め込めれば定理7.1が使える』という近道を検査した。以下はその一般化を否定する、明示的な directed union。

α<ω_1 に対し

    T_α={t:α→ω : t は単射、かつ ω\im(t) は無限}

と置く。各 T_α は非空。α≤β<ω_1 に対し restriction T_β→T_α は全射：残った無限集合を二つに分け、一方に β\α の新しい値を割り当て、もう一方を使わず残せばよい。

しかし

    lim_(α<ω_1) T_α = ∅。

互換な族があれば、その union は ω_1→ω の単射になってしまう。

C_α=T_α・Z_* と置く。各 C_α∈C。Restriction maps は K の split epis（集合の section を Ω 成分と直積にする）。従って E(C_α) は P の split-mono ω_1-chain。

    V=colim_(α<ω_1) E(C_α)

は定理6.1により H_fg に属する。

各 sort i について、N と (I) によって

    H_2(V_i)
      ≅ lim_α H_2(Ω^(T_α×Ω))
      ≅ lim_α (T_α×Ω)
      = ∅。

一方 V_i は非自明である。各 stage は非自明で、colimit injections は mono。

任意の Y∈K に対して V→E(Y) があれば、Y_i≠∅ である各 sort i で座標評価を合成し V_i→Ω を得てしまう。従って Y_0=Y_1=∅ が必要。

つまり V から D の対象への射が存在するのは、終対象 E(0_K)≅1_P の場合だけ。特に V はいかなる D-object にも mono で埋め込めない。D の集合個の積にも埋め込めない（その積も D に属する）。

この計算は N の Isbell 性以外に、diamond、Aronszajn 木、V=L を使わない。N をさらに強めても、同じ逆系と空の limit の計算はそのまま残る。

**これは P4 の反例ではない。H_fg の codomain 分離を全対象に拡張する近道の反例である。**

---

## 9. さらに大きく閉じればよい、という案の限界

P 内で対象クラスを全小積と**全ての部分対象**で閉じれば、その full subcategory は ZFC で epireflective になる。

直接証明：X→A の像は A の部分対象なのでクラスに残る。前層圏の X の quotient は集合個であり、それらのうちクラスに属するものへの射を選べば解集合が得られる。全小積と部分対象閉性から全小極限閉性もあるので、通常の初対象補題で reflection を得る。単位は epi に取れる。

従って、極限・union 閉性を保証するために無制限の subobject closure を使うと、まさに非反射性を消してしまう。これは N や V=L の有無と無関係な構造的障害。

また、単に『N なら WVP が偽だから P4 も偽』とは推論しない。WVP が扱う全 limit-closed classes と、P4 の union-closed なクラスは区別が必要。

---

## 10. 次に検査すべき一点

現在の具体候補は T_X ではなく H_fg。

必要なのは次の局所因子化補題：

    Z,W∈H_fg, a,b:Z⇉W,
    F は finitely generated, x:F→Z, ax=bx

のとき、ある D∈D と u:F→D、v:D→Z で

    vu=x,    av=bv

を実現できるか。

この補題は H_fg の等化子閉性と同値。定理7.1と7.2は二つの特別な場合を解いている。

否定するなら、非 finitely generated domain と、D に埋め込めない codomain を使うべきである。§8の V は後者の明示的な供給源だが、これを使った等化子反例はまだ構成していない。

肯定するなら、H_fg が与える有限生成 source ごとの因子化を、二射の一致を維持したまま一つの D-witness にまとめる方法が必要。標準の finite-presentation や、小さい D-witness の一様な存在を仮定して埋めない。

---

## 11. 依存関係・確認範囲

- 非反射性：No.1 の (NC) を入力にする。No.2 の強化や No.3 の disputed density 還元は使わない。
- 全ての母圏は、小さい圏上の明示的な前層圏。母圏の local presentability を新たに推論する必要はない。
- E の fully faithfulness：Isbell の N 条件。Limit preservation のみなら ZFC。
- T_X の等化子失敗：W,Z_*,B の直接 coequalizer 計算と (I)。独立の proper-class 論法を使わない。
- H_fg の生成対象に関する性質、二つの等化子範囲：本稿の直接証明。
- §8の逆系：countable ordinals から ω への部分単射の elementary な構成。木の存在定理は使わない。
- 有限検算：Ω のサイズ2,3で、Hom_M(Ω,Ω)が1個、Hom_M(Ω²,Ω)がちょうど2座標射、fπ_0=fπ_1の解が定数関数であることを全数確認。無限証明の代替ではない。
- P4 の現在の公刊状況を網羅的に再調査したとはしない。今回の主作業は反例候補と閉性の数学的検査。

一次資料：

1. J. R. Isbell, Adequate subcategories, Illinois Journal of Mathematics 4 (1960), 541–552, §2.5, pp.549–550。
   https://webhomes.maths.ed.ac.uk/~tl/docs/Isbell_Adequate_subcategories.pdf
   本文とp.549のページ画像を今回再確認。
2. M. Shulman, Set theory for category theory, arXiv:0810.1279, p.20。
   https://arxiv.org/pdf/0810.1279
   M-set への Set^op の表示を本文とページ画像で照合。
3. J. Adámek and J. Rosický, On reflective subcategories of locally presentable categories (2015), Introduction。
   https://arxiv.org/pdf/1504.03886
   全 filtered colimits の reflection theorem と mono-directed unions を区別する背景を本文とp.1画像で再確認。本稿の未証明の等化子補題に同定してはいない。

**最終状態：有力性は未評価だが具体的な改良候補 H_fg を得た。P4 の反例完成・独立性・N による否定は未確立。**
