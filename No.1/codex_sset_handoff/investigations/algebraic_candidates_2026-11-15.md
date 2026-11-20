# 固定した無限テストと標的の調査

2026-11-15、第2段階。母圏は Ab、集合論は ZFC、Hom は通常の準同型全体。

**結論。** 局所化・p進商の二例はクラス全体を分類できた。さらに、可算 rank 3 の二つの cellular cover からテスト f と別の標的 B を固定したところ、rank 4 の可算群による B の coreflection を構成できた。この固定対にはサイズ障害がない。ただし同じ f に対する全標的の coreflectivity は示していない。

状態：`PROOF_RECONSTRUCTED`。主担当が証明を書き下し、仮定と境界事例を再点検した。独立した別担当の査読・形式検証・文献上の新規性確認は未実施。無限対象の主張を有限近似で認定していない。

## 1. 素数ごとの可逆性から得られる除外補題

**補題。** $f:U\to V$ はアーベル群の準同型、U は reduced（非零の可除部分群を持たない）とする。すべての素数 $\ell$ について、乗法 $\ell$ が U または V の少なくとも一方で全単射なら

$$
{}^\perp f=\{A:\operatorname{Hom}(A,U)=0=\operatorname{Hom}(A,V)\}.
$$

従ってこのクラスは商・直和に閉じ、trace によって coreflective である。

**証明。** $A\perp f$ なら、$\operatorname{Hom}(A,U)\cong\operatorname{Hom}(A,V)$ はアーベル群としての同型である。乗法 $\ell$ の可逆性はこの同型を通して移るので、$H=\operatorname{Hom}(A,U)$ では全素数の乗法が可逆。従って H は可除群である。任意の $a\in A$ に対する評価 $H\to U$ の像は可除部分群なので零。すべての評価が零だから H=0、従って $\operatorname{Hom}(A,V)=0$。逆は自明。∎

reduced という仮定を外してはいけない。例えば恒等射 Q→Q は全対象を許すので、両方の Hom が零という結論にはならない。

### 1.1 局所化から Prüfer 群への商

素数 p を固定し、

$$ f_p:\mathbb Z[1/p]\longrightarrow\mathbb Z[1/p]/\mathbb Z=C_{p^\infty} $$

とする。これは非分裂全射。始域は非可除・非 torsion・非 torsionless なので、元ノートの始域に関する三種類の除外だけでは処理されない。

しかし p は始域で可逆、$q\ne p$ は終域で可逆であり、始域は reduced。補題が適用できる。Prüfer 群は可除・injective なので、A に無限位数の元または非零 p-torsion があれば、そこからの非零写像を A 全体へ延長できる。従って

$$ {}^\perp f_p=\{\text{p-primary 成分を持たない torsion 群}\}. $$

coreflector は $B\mapsto\bigoplus_{q\ne p}t_q(B)$。したがって任意の B で因子分解先を $|B|$ 以下に取れる。

手計算による境界確認：$\mathbb Z/q$（$q\ne p$）は属し、$\mathbb Z/p$ は持ち上げの存在に失敗する。Z は kernel Z によって一意性に失敗する。

### 1.2 p進整数の非閉部分群による商

次に

$$ g_p:\mathbb Z_p\longrightarrow\mathbb Z_p/\mathbb Z $$

を考える。母圏は位相群ではなく Ab。商に Hausdorff な商位相を仮定していない。

$q\ne p$ は始域で可逆。終域で p は可逆である。全射性は、任意の $x\in\mathbb Z_p$ に整数を加えて p で割れるようにできることから従う。単射性は、$px\in\mathbb Z$ かつ $x\in\mathbb Z_p$ なら $x\in\mathbb Z$ となることによる。始域は $\bigcap_n p^n\mathbb Z_p=0$ なので reduced。

終域は全素数について可除で、p-torsion は零、各 $q\ne p$ について非零 q-torsion を持つ。最後の主張は $1/q+\mathbb Z$ を見ればよい。injectivity と補題から

$$ {}^\perp g_p=\{\text{p-primary torsion 群}\}. $$

coreflector は $t_p(B)\hookrightarrow B$。こちらも一様なサイズ上界 $|B|$ を持つ。

境界確認：$\mathbb Z/p^n$ は属し、$\mathbb Z/q$（$q\ne p$）は属さない。両例を同じ torsion class と取り違えない。

## 2. 非自明な固定対 f,B の選定

上の二例では条件が null class に退化したため、今度は非零の持ち上げを実際に持つ対象を含むテストを選ぶ。

構成の出発点は [Göbel–Rodríguez–Strüngmann, *Cellular covers of cotorsion-free modules*, Theorem 3.2, Example 3.3](https://www.impan.pl/shop/en/publication/transaction/download/product/88206)（2012, pp.216–218）。同論文の rank 3 の例を座標で記述し、同じ終域に向かう独立な二つの cover を比較する。以下の二つの cover の比較と pullback の証明は今回書き下したもの。

Example 3.3 の説明には線形独立という表現があるが、ここでは Theorem 3.2 の構成に合わせて、より強い **代数的独立性** を明示して使う。線形独立性だけで以下の係数比較が成立するとは主張しない。

素数を $p=2$ に固定する。以下の議論自体は任意の p で同様に成り立つ。$\mathbb Z_p$ 内の $w,a,b$ を Q 上代数的に独立に選び、一度固定する。その存在は、Q と有限個の元から生成する体の代数的閉包が可算である一方、$\mathbb Z_p$ は非可算であることから従う。

$R=\mathbb Z[1/p]$ と置き、群

$$
M=(R+Rw)\cap\mathbb Z_p,
$$
$$
G_a=\bigl(R(1,0)+R(0,1)+R(wa,w)\bigr)\cap\mathbb Z_p^2,
$$
$$
G_b=\bigl(R(1,0)+R(0,1)+R(wb,w)\bigr)\cap\mathbb Z_p^2
$$

を定める。いずれも集合・群として明示された **可算** 群である。rank は順に 2,3,3。

第2座標射影を $\pi_a:G_a\to M$、$\pi_b:G_b\to M$ とする。今回固定する対は

$$\boxed{f=\pi_a:G_a\to M,\qquad B=G_b.}$$

B は f の終域 M と異なる。単に cellular cover 自身を同じ終域の coreflection として使う状況を避け、実際に別の標的を調べる。

## 3. 構造と全 Hom の計算

### 3.1 Exact sequence と completion

$y=(r+sw)/p^n\in M$、$r,s\in\mathbb Z$ を取る。$c+swa\equiv0\pmod{p^n}$ となる整数 c を選べば、

$$\left((c+swa)/p^n,\ (r+sw)/p^n\right)\in G_a$$

は y の lift になる。従って $\pi_a$ は全射。第2座標が零なら w の超越性から w の係数も定数項も零なので、kernel は $\mathbb Z(1,0)$。b についても同様である。

$$0\longrightarrow\mathbb Z\longrightarrow G_i\xrightarrow{\pi_i}M\longrightarrow0
\qquad(i=a,b).$$

ここで交叉による定義から

$$G_i\cap p^n\mathbb Z_p^2=p^nG_i,\qquad M\cap p^n\mathbb Z_p=p^nM$$

が成り立つ。さらに G_i は $\mathbb Z^2$、M は Z を含むので、それぞれの p進 completion は $\mathbb Z_p^2,\mathbb Z_p$ である。

このため、**任意の代数的準同型** $h:G_i\to M$ は p進連続であり、completion 間の連続準同型へ延長する。理由は $h(p^nG_i)\subseteq p^nM$ であり、連続な準同型だけを選別しているわけではない。延長は $\mathbb Z_p$-線形である。

### 3.2 Hom(G_i,M) と End(G_i)

h の延長を $h(x,y)=\alpha x+\beta y$ と書く。標準基底が G_i に入るので $\alpha,\beta\in M$。$\alpha=A_0+A_1w$、$\beta=B_0+B_1w$（係数は R）と書ける。

$$h(wi,w)=\alpha wi+\beta w\in M$$

と w,i の代数的独立性から、$\alpha=0$、$B_1=0$ を得る。$\beta\in R\cap\mathbb Z_p=\mathbb Z$ なので

$$\operatorname{Hom}(G_i,M)=\mathbb Z\pi_i.$$

$M\cap\mathbb Q=\mathbb Z$ であり、非零 $n\pi_i$ は $wi,w$ の第2座標を $nw\notin\mathbb Z$ に送る。従って

$$\operatorname{Hom}(G_i,\mathbb Z)=0.$$

任意の $\varphi\in\operatorname{End}(G_i)$ について $\pi_i\varphi=n\pi_i$。差 $\varphi-n1$ は kernel Z に値を取るため零となり、

$$\operatorname{End}(G_i)=\mathbb Z1_{G_i}.$$

よって各 $\pi_i$ は cellular cover であり、特に $G_a\in\mathcal A={}^\perp f$。非零 kernel と $\operatorname{Hom}(G_i,\mathbb Z)=0$ により、これらの exact sequences は非分裂である。

この始域は旧ノートの三種類の除外には入らない。非零の torsion-free 群なので torsion ではない。p進分離性から $\bigcap_n p^nG_i=0$ であり、非零可除群でもない。もし torsionless なら Z の積へ埋め込めるが、$\operatorname{Hom}(G_i,\mathbb Z)=0$ と矛盾する。また kernel は無限巡回群 Z なので、今回追加した有限 kernel の除外にも入らない。

### 3.3 二つの cover の間に射はない

$u:G_b\to G_a$ を取る。composition $\pi_a u=n\pi_b$ なので、completion 上では

$$u(x,y)=(c x+d y,n y).$$

$u(1,0)\in\ker\pi_a=\mathbb Z(1,0)$ から $c\in\mathbb Z$。$u(0,1)=(d,n)\in G_a$ の第2座標が整数であることから $d\in\mathbb Z$ も従う。

$u(wb,w)\in G_a$ の条件は

$$cwb+dw=r+nwa\qquad(r\in R)$$

となる。w,a,b の代数的独立性により $c=d=n=r=0$。従って

$$\operatorname{Hom}(G_b,G_a)=0=\operatorname{Hom}(G_a,G_b).$$

一方 $\operatorname{Hom}(G_b,M)=\mathbb Z\pi_b\ne0$ なので、**B=G_b は A に属さない**。$1_B$ が coreflection になる退化例ではない。

## 4. Pullback による B の coreflection

$$P=G_a\times_M G_b$$

とし、射影を $p_a:P\to G_a$、$p_b:P\to G_b$、共通の射を $\rho:P\to M$ とする。座標では

$$
P=\bigl(Re_1+Re_2+Re_3+R(wa,wb,w)\bigr)\cap\mathbb Z_p^3.
$$

実際、二つの第2座標が等しい条件から、R に属する定数係数と w の係数がそれぞれ一致する。従ってこの表示が得られる。P は可算、rank 4。p進 completion は $\mathbb Z_p^3$。

任意の $h:P\to M$ は completion に延長し、$h(x_1,x_2,y)=\alpha x_1+\beta x_2+\gamma y$、$\alpha,\beta,\gamma\in M$ と書ける。

$$\alpha wa+\beta wb+\gamma w\in M$$

に代数的独立性を適用すると $\alpha=\beta=0$、$\gamma\in\mathbb Z$。従って

$$\operatorname{Hom}(P,M)=\mathbb Z\rho,\qquad \operatorname{Hom}(P,\mathbb Z)=0.$$

任意の $n\rho:P\to M$ は $np_a$ によって f に沿って持ち上がる。二つの lift の差は kernel Z への射なので零。従って

$$P\in\mathcal A.$$

任意の $X\in\mathcal A$ と $v:X\to G_b$ を取る。$\pi_bv:X\to M$ は f に沿って一意に $u:X\to G_a$ に持ち上がる。よって組 $(u,v)$ は P への一意な射を与える。

$$\boxed{p_b:P\longrightarrow G_b\text{ は }\mathcal A\text{-coreflection。}}$$

これは X のサイズに制限のない普遍性の証明である。固定した f,B に対し、**すべての $X\to B$ が可算な P を一意に経由する**ので、無界な factor-size 障害は起きない。

## 5. この例から分かる、もう一つの区別

$G_a\in\mathcal A$ だからといって、A 全体が G_a から小余極限だけで生成されるとは限らない。この例では実際に異なる。

クラス $\{X:\operatorname{Hom}(X,G_b)=0\}$ は小余極限に閉じ、§3.3 より G_a を含む。従って G_a の小余極限閉包に属する対象から G_b への射は零である。

ところが $P\in\mathcal A$ から G_b への射 $p_b$ は全射で非零。従って

$$\operatorname{ColimClosure}(G_a)\subsetneq{}^\perp\pi_a.$$

この差はすでに可算群で現れる。したがって、テストの始域 G_a による cellular approximation を作れたことだけでは、A 全体の coreflector を得たとは言えない。

## 6. 仮定の検査と到達範囲

- w,a,b は固定した。対象のサイズに合わせて f や B を変更していない。
- 代数的独立性は Hom の係数比較に使った。単なる線形独立で代用していない。
- S-purity は p の冪に関するもの。全整数に関する純部分群と無断で同一視していない。
- 「全代数的 Hom が連続」は p進 filtration の保存から直接示した。任意の群間の自動連続性を仮定していない。
- $a=b$ と置くと $P\cong G_a\oplus\mathbb Z$ となり、Hom(P,Z)=0 は失敗する。この場合 P は A に属さず、標的 G_a の coreflection は $1_{G_a}$ である。従って独立性を落とした同じ pullback 公式を無条件で使ってはいけない。
- $G_b\notin\mathcal A$ と、P による非零 coreflection の存在を別々に示した。
- 今回は有限テストを追加していない。p進数の有限桁近似は代数的独立性や全 Hom を保証しないため、ここでは証明によって扱った。

## 7. 残る課題

今回具体的に調べた対 $(\pi_a,G_b)$ は肯定的に処理できた。**反例側の有望な固定対を確保したとは、まだ言えない。** また、${}^\perp\pi_a$ が Ab 全体で coreflective かは未決定である。

この f を引き続き調べるなら、具体的な次の補題が焦点になる。

> 任意の固定 B に対し、$X\in{}^\perp\pi_a$ から B への射を、サイズが B と f だけで抑えられる ${}^\perp\pi_a$-対象に因子分解できるか。

今回の pullback 計算は、特定の B→M と Hom(P,M) の剛性を利用した。任意の B にはそのような射や剛性がないので、そのまま一般化できない。逆に反例を目指すなら、この範囲を外れる B を選び、単に対象を大きくするだけでなく、全ての有界サイズの中間対象を排除する必要がある。

今回得た分類・pullback・閉包の厳密包含はいずれも ZFC 内の結果であり、一般問題の ZFC 独立性は示していない。

第8段階の続報：可測基数が存在しないと仮定すると、slender な端点を持つテストの coorthogonality class は積に閉じる。これにより、上の固定 f について任意の集合 J に対する p_b^J:P^J→G_b^J も coreflection になる。[有限座標性の適用 §5](finite_coordinate_trial_2026-11-15.md)。この追加結果も全標的の coreflectivity は示していない。
