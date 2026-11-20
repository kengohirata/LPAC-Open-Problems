# 集合個の対象で測る同値射の因子分解

2026年11月16日。Set^op の図式への埋め込みを調べる過程で得た ZFC の肯定結果。主担当の構成を別担当が独立に点検した `INTERNAL_PROOF_CHECKED`。文献上の新規性・形式検証は主張しない。

## 1 定理と範囲

K=Set^{C^op} を前層圏、(W_i)_{i∈I} を集合個の K の対象とする。一意対角持上げの直交を ⊥_u と書き、

\[
\mathcal E=\{e:X\to Y:\operatorname{Hom}_{\mathcal K}(e,W_i)
\text{ is bijective for all }i\},
\qquad\mathcal R=\mathcal E^{\perp_u}
\]

と置く。

**定理（ZFC）。** (E,R) は K の orthogonal factorization system である。すなわち、右側のテストを集合個の終対象への射 W_i→1 とした場合には、OFS が ZFC で存在する。

これは一般の右テスト U_i→V_i の結果ではない。また、対象の coorthogonality class {A:Hom(A,W_i) が一元} の coreflectivity よりも、射の因子分解を直接扱う主張である。

## 2 固定した受け皿

f:A→B を固定し、

\[
T_A=\prod_{i\in I}W_i^{\operatorname{Hom}(A,W_i)},
\qquad
T_B=\prod_{i\in I}W_i^{\operatorname{Hom}(B,W_i)}
\]

とする。指数は集合個の積（cotensor）である。評価射 η_A:A→T_A、η_B:B→T_B、および前合成による τ_f:T_A→T_B は τ_fη_A=η_Bf を満たす。

各 W_i およびそれらの任意の集合添字の積 T について Hom(e,T) は e∈E に対して全単射になる。そのような積の間の**任意の射** T→T' は R に属する。実際、上辺 X→T を Y→T に一意に延長し、下辺との可換性は Hom(e,T') の単射性から従う。

従って

\[
P=B\times_{T_B}T_A,\qquad p:P\to B
\]

は R の射である。a=(f,η_A):A→P に沿って、全ての χ:A→W_i が P に延長する。P→T_A の χ 座標を使えばよい。

J₀=im(a)⊆P とし、a₀:A↠J₀ を取る。Hom(a₀,W_i) は全射性により単射、座標射の制限により全射なので、a₀∈E。

## 3 受け皿の内部での閉包

j:J↪P、a_J:A→J を ja_J=a かつ a_J∈E とする。次の可換四角全てに現れる v の像の和集合を C(J)⊆P とする。

\[
\begin{array}{ccc}
X&\xrightarrow{u}&J\\
e\downarrow&&\downarrow j\\
Y&\xrightarrow{v}&P
\end{array}
\qquad(e\in\mathcal E).
\]

これは集合として定義できる。各 P(c) の元について、集合として符号化された e,u,v の存在を量化すればよく、E 所属も集合パラメータ (C,(W_i)) を持つ一階の条件である。Separation により各成分が集合となり、像の和集合なので部分前層となる。クラス個の coproduct や証人選択は使わない。e=id_J により J⊆C(J)。

**補題。** J→C(J) は E に属する。

**存在。** χ:J→W_i の A への制限 χa_J を取る。この制限の P 上への座標延長 χ̃ は J 上で χ と一致する。a_J∈E による Hom(a_J,W_i) の単射性を使う。従って χ̃ を C(J) に制限すればよい。

**一意性。** φ,ψ:C(J)→W_i が J 上で一致するとする。定義に現れる各 v:Y→P を C(J) に値を持つ射として扱えば、φv と ψv は e:X→Y の後で一致する。e∈E なので φv=ψv。これらの像が C(J) を覆うから φ=ψ。∎

J_{α+1}=C(J_α)、極限段階では union として超限反復する。全ての A→J_α は E に属する。後続は補題と合成閉性、極限は Hom(-,W_i) が colimit を limit に送ることによる。極限での延長は、前の段階の唯一の延長が整合することから直接にも分かる。

κ=max(ℵ₀,Σ_c|P(c)|) と置く。固定した P の部分対象の増大列なので、κ^+ より前に J_{α+1}=J_α となる。そうでなければ各後続で新たな carrier 要素を選べ、κ^+ 個の相異なる元が P に存在することになる。

## 4 停止点での因子分解

J=C(J) なら、任意の e∈E に対する j:J↪P との四角の下辺 v:Y→P は J に像を持つ。従って持上げが存在し、j が通常の mono であるため一意である。つまり j∈R。

よって

\[
A\xrightarrow{a_J}J\xrightarrow{pj}B,
\qquad a_J\in E,\quad pj\in R
\]

という因子分解を得た。最後に各 W_i→1 は R に属し、それらへの一意左持上げ性は E の定義そのものである。従って

\[
{}^{\perp_u}R\subseteq E\subseteq{}^{\perp_u}R
\]

となり、(E,R) は OFS。∎

## 5 射の圏における coreflection

E を Arr(K) の充満部分圏としてみると coreflective である。f:A→B の上記の因子分解を a_J:A→J と pj:J→B とすれば、

\[
(1_A,pj):a_J\longrightarrow f
\]

が coreflection になる。e:X→Y∈E から f への射 (u,v) に対し、a_Ju と v の四角を E⊥_uR で一意に埋めれば、e→a_J への唯一の因子化が得られる。

特に K=M-Set、W=Ω の場合、[Set^op ノート §6](setop_coorthogonality_2026-11-16.md) のテスト

\[
\sigma:(\Omega\xrightarrow{1}\Omega)
\longrightarrow(\Omega\to1)
\]

の coorthogonality class は、Hom(-,Ω) を全単射にする射全体であり、ZFC で coreflective である。従って同節の有限図式は、小さい商への所属継承を否定する対照例であり、P の反例ではない。

## 6 境界点検

- I=∅ なら E は全ての射、R は同型であり、構成は im(f) から固定 B 内で閉包を取る。e 自体を任意に使えるため B に到達する。
- 全 W_i=1 でも同じ結論。空対象 W_i を許しても、定義される座標がある場合だけを使う証明は変わらない。
- P が初対象なら A→P の存在から A も初対象であり、初期像の議論に問題はない。
- E の accessibility、Global Choice、N、巨大基数は使わない。反復は固定した集合サイズの P の内部で行う。
- 一般の右テストでは、全ての A→U_i が B と両立して一つの右射 P→B に延長するとは限らない。§2 の座標の供給が一般化されていないので、一般の P を証明したことにはならない。
