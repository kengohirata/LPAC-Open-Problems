# sSet の高次元 coorthogonality：線形テストの除外と固定次数の障害

日付：2026-11-15

## 0. 状況と用語

通常の simplicial sets の圏を sSet とする。射の集合 S に対し

\[
\mathcal A_S=\{X\mid \operatorname{sSet}(X,f)\text{ が全単射 for all }f\in S\}
\]

と置く。すべて ordinary Hom の条件であり、ホモトピー類や derived mapping spaces の条件ではない。

一般の P_sSet の ZFC 証明も、その独立性を示す反例も、今回得られていない。本ノートの成果は、次の二つの直接証明である。これらの文献上の新規性は確認していない。

1. 体 k 上の simplicial vector spaces の線形写像を、構造を忘れてテスト射に使う場合、直交類は locally aleph_1-presentable で coreflective。次数・次元・基数の上限は不要。
2. 任意の小余極限閉充満部分圏 A⊆sSet について、B の coreflection がないなら、単に必要な次元が高くなるだけでなく、一つの固定次数で因子分解先のサイズに一様上界がなくなる。

## 1. 前提：標準的な線形化

C_*(X;k) を X の正規化鎖複体とする。C_n(X;k) は非退化 n-simplex を基底とする自由 k-vector space である。

simplicial k-vector space U の正規化複体を N(U) と書く。自由 simplicial vector space と忘却の随伴、および Dold–Kan 対応から

\[
\operatorname{sSet}(X,\operatorname{und}U)
\cong
\operatorname{sVect}_k(k[X],U)
\cong
\operatorname{Ch}_{\ge0}(k)(C_*(X;k),N(U)).
\]

これは Hom 集合そのものの自然な全単射である。

参考：Stacks Project, Theorem 14.24.3 (019G); Kerodon, Construction 2.5.5.9 (00QH), Construction 2.5.6.3 (00QT)。

## 2. 体上の複体の分解

非負次数複体 C に対して

- Z_n(C)=ker(d_n),
- B_n(C)=im(d_{n+1}),
- H_n(C)=Z_n(C)/B_n(C)

と置く。d_0:C_0→0 とする。

体上では各短完全列が分裂するので、補空間を選んで

\[
C_n\cong B_n(C)\oplus H_n(C)\oplus B_{n-1}(C)
\]

と書ける。最後の成分から次の次数の最初の成分への differential は恒等写像で、他の成分では零である。

S^n(W) は次数 n のみに W を置く複体、D^n(W) (n≥1) は次数 n,n−1 に W を置き、その間の differential を恒等写像とする複体とする。

すると、非標準的だが実際の複体同型として

\[
C\cong
\bigoplus_{n\ge0}S^n(H_n(C))
\oplus
\bigoplus_{n\ge1}D^n(B_{n-1}(C))
\]

が成り立つ。これは単なる準同型や鎖ホモトピー同値ではない。

任意の複体 E に対して

\[
\operatorname{Ch}(S^n(k),E)\cong Z_n(E),
\qquad
\operatorname{Ch}(D^n(k),E)\cong E_n.
\]

第二の式で disk の次数は n,n−1、Hom は top degree n の元で決まることに注意。

## 3. 線形テストの直交条件を完全に記述する

simplicial k-linear maps の集合 {f_i:U_i→V_i} を取り、その underlying simplicial maps に対する直交類 A を考える。phi_i=N(f_i) と置く。

次数の集合を

\[
J=\{n\ge0\mid Z_n(\phi_i)\text{ が同型でない }i\text{ が存在}\},
\]

\[
K=\{n\ge1\mid (\phi_i)_n\text{ が同型でない }i\text{ が存在}\}
\]

で定める。

### 命題 3.1

\[
X\in\mathcal A
\iff
\begin{cases}
H_n(X;k)=0 & (n\in J),\\
d_n:C_n(X;k)\to C_{n-1}(X;k)\text{ が零} & (n\in K).
\end{cases}
\]

### 証明

第1節の随伴で問題を Hom_Ch(C_*(X;k),phi_i) の全単射性へ移す。第2節の分解に対して Hom を取ると、sphere summands からは Z_n(phi_i)、disk summands からは (phi_i)_n が現れる。

非零 vector space W を始域とする Hom_k(W,g) が全単射であることは、g が同型であることと同値である。W の基底を選べば、Hom_k(W,g) は g のコピーの積であり、各因子に零元があるためである。

したがって、H_n(C) が非零なら Z_n(phi_i) は同型でなければならず、B_{n-1}(C) が非零なら (phi_i)_n は同型でなければならない。逆向きも同じ積の計算で従う。B_{n-1}(C)=0 は d_n=0 と同値である。∎

注意：H_n(phi_i) ではなく Z_n(phi_i) を使っている。strict な Hom の全単射性なので、テスト射の準同型性だけでは足りない。

## 4. 可算な A-部分対象を構成する

### 補題 4.1

X∈A と可算個の simplices Z⊆X に対して、Z⊆Y⊆X、Y∈A、かつ Y の全 simplices の集合が高々可算となる Y が存在する。

### 証明

k_0 を k の素体（Q または F_p）とする。k_0 は可算であり

\[
C_*(X;k)\cong C_*(X;k_0)\otimes_{k_0}k.
\]

体の拡大は忠実かつ完全なので、命題3.1の条件は k を k_0 に置き換えても変わらない。

Z の face と degeneracy に関する閉包を Y^(0) とする。Δ の射は可算個なので、これは可算である。

Y^(r) が可算であるとする。すべての n∈J と、C_n(Y^(r);k_0) のすべての cycle z を考える。これらは全部合わせても可算個である。H_n(X;k_0)=0 より、X 内で

\[
d_{n+1}b_z=z
\]

となる有限鎖 b_z がある。それらの台の simplices を加え、face と degeneracy で閉じて Y^(r+1) とする。

Y=∪_{r<ω}Y^(r) と置く。可算性は保たれる。Y の任意の cycle は有限支持なので、ある段階 Y^(r) に現れ、次の段階で boundary になる。よって n∈J に対して H_n(Y;k_0)=0。

n∈K の d_n=0 は部分 simplicial set に引き継がれる。正規化鎖複体 C_*(Y;k_0)→C_*(X;k_0) は次数ごとに単射だからである。従って Y∈A。∎

### 定理 4.2

A は locally aleph_1-presentable であり、sSet の coreflective full subcategory である。

### 証明

任意の coorthogonality class は小余極限に閉じる。これは

\[
\operatorname{sSet}(\operatorname{colim}_a X_a,f)
\cong \lim_a\operatorname{sSet}(X_a,f)
\]

と、全単射の極限は全単射であることから従う。

補題4.1より、X∈A の可算な A-部分対象のなす半順序は aleph_1-directed で、合併は X である。可算な simplicial sets は sSet で aleph_1-presentable である：射を指定する可算個の値と可算個の方程式が aleph_1-filtered colimit の一段階で実現できるためである。

A の余極限は sSet で計算されるので、これらの対象は A 内でも aleph_1-presentable である。その同型類は集合個。従って A は locally aleph_1-presentable。

coreflector の直接構成は次節に与える。∎

## 5. Coreflector の直接構成とサイズ上界

B∈sSet を固定する。可算な A-対象の skeleton を一つ取り、そこから B への射の圏を J_B とする。これは小さい圏である。

J_B は可算図式の cocone を持つ。実際、可算な A-対象の可算図式の余極限は、なお可算で A に属し、B への射を持つ。従って J_B は aleph_1-filtered。

\[
R(B)=\operatorname{colim}_{(C\to B)\in J_B} C
\]

と置き、r_B:R(B)→B を標準射とする。A の余極限閉性より R(B)∈A。

任意の a:X→B (X∈A) を、補題4.1による可算 A-部分対象からの directed colimit として書く。各部分対象 C→X→B は J_B の対象なので、標準射 C→R(B) が整合的に得られ、一つの u:X→R(B) に貼り合わさる。r_B u=a。

一意性を示す。可算 C∈A と h:C→R(B) について、C の aleph_1-presentability と J_B の aleph_1-filteredness により、h はある D→B∈J_B を経由する。従って、J_B 内の射と colimit の関係式を使うと、h はその合成 r_B h:C→B から定まる標準射と一致する。一般の X でも可算部分対象への制限で一意性が従う。

よって r_B は coreflection。

全 simplices の濃度を |B| と書く。可算な simplicial sets の同型類は高々 2^{aleph_0} 個で、可算 C から B への射は高々 (|B|+2)^{aleph_0} 個。従って

\[
|R(B)|\le (|B|+2)^{\aleph_0}
\]

と取れる。この粗い上界はテスト射の大きさには依存しない。

## 6. 真に無限次元の非分裂射の計算

k=Q とする。m≥1 ごとに

\[
q_m:D^{2m+1}(\mathbb Q)\longrightarrow S^{2m+1}(\mathbb Q)
\]

を、次数2m+1では恒等、次数2mでは零とする。

\[
E=\bigoplus_{m\ge1}D^{2m+1}(\mathbb Q),\qquad
F=\bigoplus_{m\ge1}S^{2m+1}(\mathbb Q),\qquad
g=\bigoplus_{m\ge1}q_m.
\]

Dold–Kan の逆関手 Γ を使い、f=und Γ(g):und Γ(E)→und Γ(F) と置く。

E は acyclic、F は各奇数次数3,5,7,…に Q の homology を持つ。一般化 Eilenberg–MacLane simplicial sets について π_n(Γ(C))≅H_n(C) なので、f は underlying simplicial sets としても split epi ではない。両端は一頂点を持つ。Γ(F) は任意に高い次数に非零 homotopy group を持つので、有限 n に対して n-coskeletal ではない。

本例では

\[
J=\{2,3,4,5,\ldots\},\qquad
K=\{2,4,6,\ldots\}.
\]

従って

\[
X\perp f
\iff
\begin{cases}
H_n(X;\mathbb Q)=0 &(n\ge2),\\
d_{2m}=0 &(m\ge1).
\end{cases}
\]

このクラスは、すべての1-skeletal simplicial sets を含む。また、Δ[2m+1]/Λ_i[2m+1] のように非退化2m-cellと2m+1-cellが一組存在する simplicial sets も含む。従って離散 simplicial sets だけへの退化ではない。

しかし第4–5節により、このクラスは locally aleph_1-presentable かつ coreflective。無限個の非零 homotopy groups を持つ終域と非分裂性だけでは反例にならない。

注意：本例で π を使ったのは非分裂性と非有限coskeletal性の確認だけである。coorthogonality と coreflection の証明は引き続き strict Hom について行っている。

## 7. 一般の sSet：非存在は一つの固定次数で検出される

この節は線形構造を仮定しない。

A⊆sSet を充満・同型閉・小余極限閉部分圏とし、B∈sSet を固定する。

### 定理 7.1

次は同値である。

(a) B の A-coreflection が存在する。

(b) 各 n≥0 について、ある基数 κ_n が存在し、任意の a:X→B (X∈A) が

\[
X\longrightarrow Y\longrightarrow B,
\qquad Y\in A,\quad |Y_n|\le\kappa_n
\]

と因子分解する。

異なる n について、同じ Y が使えるとは仮定していない。

### 証明

(a)⇒(b) は coreflection の対象を Y に取ればよい。

(b)⇒(a)：κ=max(aleph_0,sup_n κ_n) とする。a_0:X_0→B から始めて、n段目で(b)を次数nに適用し

\[
X_0\longrightarrow X_1\longrightarrow X_2\longrightarrow\cdots
\]

という B 上の列を作り、X_i∈A、|(X_{n+1})_n|≤κ を満たすようにする。

Y=colim_n X_n∈A とする。m≤n なら degeneracy map により (X_{n+1})_m は (X_{n+1})_n に単射で入る。従って、各固定mに対し、列の十分後ろでは m-simplex の数がκ以下である。

sSet の余極限は次数ごとに計算されるので、|Y_m|≤κ。さらに次数は可算個なので、全 simplices の数もκ以下。よって、任意のa_0はサイズκ以下のA-対象を経由する。

サイズκ以下の simplicial sets の同型類と、それらからBへの射は集合個である。従って A↓B に weakly terminal set がある。

A↓B は余完備である。weakly terminal set の余積 W を取り、W のすべての自己射と恒等射を coequalize して q:W→Q とする。Q は終対象である。実際、u,v:X→Q の coequalizer c:Q→T を取り、weak terminality から h:T→W を選ぶと、hcq∈End(W) より qhcq=q。q が epi なので qhc=id_Q。c は split mono かつ coequalizer なので同型、従ってu=v。射の存在はWのweak terminalityから従う。∎

### 系 7.2

B の A-coreflection が存在しないなら、ある固定した自然数 n が存在して

\[
\forall\kappa\ \exists(a:X\to B),\ X\in A,
\]

かつ任意の A-対象を通る因子分解 X→Y→B に対して |Y_n|>κ が成り立つ。

つまり、単に必要な次数が高くなるだけでは solution-set condition は破れない。一つの固定次数で、必要な simplex の個数に基数上界がなくなる必要がある。

これは「有限 truncated category での反例が存在する」という主張ではない。Y∈A という制約は、依然として全次数の条件である。

### 系 7.3：頂点では障害は起きない

A={}^⊥{f} で f_0 が全単射なら、A は Δ[0] とすべての離散 simplicial sets を含む。

a:X→B について、a_0で同じ頂点に写る頂点対を、Δ[0] のコピーを使う coequalizer で同一視する。この coequalizer Y は A に属し、a はYを経由し、|Y_0|≤|B_0|。

従って非存在を証言する次数nはn≥1に取らなければならない。

より一般に f_n が全単射なら Δ[n]∈A なので、a_nで同一視されるn-simplexをΔ[n]のコピーでcoequalizeでき、|Y_n|≤|B_n|となる。

## 8. 二つの補足的な除外・注意

### 8.1 頂点列で単体が決まる始域

U の各n-simplexがその順序付き頂点列によって一意に決まると仮定する。

f:U→V の頂点写像が全単射ならfはdegreewise単射：f(x)=f(y)なら、f_0の単射性によりx,yの頂点列が同じになり、x=y。

この場合、{}^⊥f はmonoへのcoorthogonality classなのでcoreflective。頂点写像が全単射でなければ、非空XはΔ[0]をretractとして持つため、{}^⊥f={∅}。

従って、頂点列でsimplexが決まるような ordered abstract simplicial complexes を始域にして、単に次元を増やす方針も反例を生まない。

### 8.2 有限段階の一意性は無限段階に自動で貼り合わさる

X のn-skeletonをsk_nXとする。h:X→Vに対して

\[
L_n(h)=\{g_n:sk_nX\to U\mid fg_n=h|_{sk_nX}\}
\]

と置くと、全体の持ち上げ集合はlim_n L_n(h)。各L_n(h)がsingletonなら、制限は自動的に整合するのでlimもsingleton。

従って「各有限段階では一意に解けるのに、無限段階でだけ解けない」という構成は成立しない。非空性だけなら無限枝の存在は別問題だが、それだけではcoreflectionの非存在を意味しない。

## 9. 検算と未解決部分

命題3.1のHom計算について、GF(2)上の4次数の複体と鎖写像を生成し、chain-map方程式から直接計算する全単射性と、cycle/disk判定を比較する有限検算を300件行った。一致した。コードはsset_followup_checks/check_linear_formula.py。

有限検算は無限次元の定理の証明の代用ではない。定理の根拠は上の分解と可算部分対象構成である。

今回得られていないもの：

- 一般のP_sSetのZFC証明。
- P_sSetの反例、または追加公理の下での反例。
- arbitrary simplicial abelian groupsの準同型をテストにした場合の一般定理。
- 高次元の反例を有限truncated categoryへ移す定理。

探索上の修正：単に高次元化するのではなく、体上の線形分解では扱えない関係を使い、固定したBと一つの固定次数nで、A内の因子分解に必要なn-simplex数を任意の基数以上に強制することを狙う。

## 参考資料

[R1] The Stacks Project, Theorem 14.24.3 (019G), Dold–Kan.
https://stacks.math.columbia.edu/tag/019G

[R2] Kerodon, Construction 2.5.5.9 (00QH), The Normalized Chain Complex of a Simplicial Set.
https://kerodon.net/tag/00QH

[R3] Kerodon, Construction 2.5.6.3 (00QT), The Eilenberg–MacLane Functor.
https://kerodon.net/tag/00QT

[R4] Kerodon, Exercise 3.2.2.22 (00W2), Homotopy of Eilenberg–MacLane Spaces.
https://kerodon.net/tag/00W2

[R5] The Stacks Project, Lemma 14.19.10 (018B), Coskeleton functors.
https://stacks.math.columbia.edu/tag/018B
