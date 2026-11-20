# No.14　\(V=L\) では \(L_\beta\) の圏の列の安定性に還元される

2026年11月20日。\(V=L\) を仮定する。\(P\) は No.14 の肯定、すなわち「すべての大きいアクセス可能圏に忠実なアクセス可能関手を持つ一つの大きいアクセス可能圏が存在する」を表す。圏 \(\mathcal A,\mathcal B\) について、忠実なアクセス可能関手 \(\mathcal A\to\mathcal B\) が存在することを \(\mathcal A\preceq\mathcal B\) と書く。以下はこのノートでの導出で、独立検証は未実施である。

**結論。** 各無限基数 \(\mu\) に対し、\(L_\beta\) 型の対象と初等埋め込みからなる大きいアクセス可能圏 \(\mathcal C_\mu\) を定義でき、コードが \(H_{\mu^+}\) に入る任意の大きいアクセス可能圏 \(\mathcal K\) に対して \(\mathcal C_\mu\preceq\mathcal K\) となる。従って \(V=L\) では

\[
P\iff\exists\mu\ \forall\mu'>\mu\ \ \mathcal C_\mu\preceq\mathcal C_{\mu'}
\]

が成り立つ。任意の始域 \(\mathcal T\) に関する量化は消え、問いは \(L_\beta\) の間の初等埋め込みの臨界点を関手的かつ忠実に持ち上げられるかになる。さらに右辺の各 \(\mathcal C_\mu\preceq\mathcal C_{\mu'}\) は、小さい圏からの忠実関手の存在と同値である（§5）。

## 1. 圏 \(\mathcal C_\mu^c\) と \(\mathcal C_\mu\)

\(\mu\) を無限基数、\(c\in H_{\mu^+}\) を basic theory のコードとする。記号の項数、連言・選言の大きさ、量化する変数の個数はすべて \(\mu\) 以下である。\(\mathcal C_\mu^c\) を次で定める。

- **対象**は推移的集合 \(M\) で、次を満たすもの。
  1. \(M\models\mathrm{ZFC}^-\)（冪集合公理を除き Collection を含む）かつ \(V=L\)。従って \(M=L_\beta\)。
  2. \(M\) は長さ \(\mu\) の列で閉じる。
  3. \(M\) で最大の基数 \(\vartheta_M\) が存在し、\(M\models\operatorname{cf}(\vartheta_M)=\mu^+\)。
  4. \((A_c)\)：\(M\) の中に、ソートが \(\vartheta_M\) の分割になっている \(c\) のモデルが存在する。
- **射**は初等埋め込みで、各 \(\xi\le\mu\) を固定するもの。

大きい \(c\in H_{\mu^+}\) 全体を \(S_\mu\) とし、すべての \(c\in S_\mu\) について \((A_c)\) を満たす対象のなす充満部分圏を \(\mathcal C_\mu\) とする。

**基本事項。** 条件 2 から \(H_{\mu^+}\subseteq M\) で、射は \(H_{\mu^+}\) を点ごとに固定する。\(x\in H_{\mu^+}\) を \(\mu\)-列 \(s\) の値域として書くと、\(\in\)-帰納法で \(s\in M\)、\(j(s)=j\circ s=s\) となるからである。特に \(\mu^+\) は \(M\) で正しく計算され、\(\mu^+\) 未満の順序数と \(c\) は固定される。\(L_{\mu^+,\mu^+}\) の式の \(M\) の元であるモデルにおける充足は、代入がすべて \(\mu\)-列で \(M\) に属するので、\(M\) と外部で一致する。

**条件 3 の選び方。** 最大基数の共終数を \(\mu^+\) にしたのは次の二つを同時に満たすためである。
- 共終数が \(\mu\) 以下だと、\(\vartheta^\mu>\vartheta\) となり、濃度がちょうど \(\vartheta\) の \(c\)-モデルが存在しない理論がある（\(c\) が \(\mu\)-列での閉性を要求する場合）。
- \(\vartheta\) を後続基数にすると、臨界点が \(\vartheta\) 自身の射があり、§2 の決定性が崩れる。

なお、最初に考えた「\(\vartheta+1\) から定義可能な元だけからなる対象」に絞る方法は使えない。そのような \(L_\beta\) では \(\Sigma_n\)-hull の高さ \(\beta_n<\beta\) が \(\beta\) に共終で、\(\operatorname{cf}(\beta)=\omega\) となり、\(\omega\)-列ですら閉じないからである。

## 2. 射は \(\vartheta\) への制限で決まる

**補題 A。** \(j,j'\colon M\to N\) が \(\mathcal C_\mu^c\) の射で \(j|\vartheta_M=j'|\vartheta_M\) なら \(j=j'\)。

1. \(j\) は \(\vartheta_M\) で連続である。\(M\) 内の共終写像 \(s\colon\mu^+\to\vartheta_M\) を取ると、\(j(\mu^+)=\mu^+\) で \(\mu^+\) 未満は固定されるので \(j(s)=j\circ s\)。これは \(j(\vartheta_M)=\vartheta_N\) に共終である。
2. \(\vartheta_M\) は \(M\) で極限基数だから、\(M\) 内の凝縮により \(\vartheta_M\) の有界部分集合は \(L_{\vartheta_M}\) に属する。\(L_{\vartheta_M}\) の元は \(<_L\) で \(\eta\) 番目（\(\eta<\vartheta_M\)）の元であり、その像は \(j(\eta)\) 番目の元である。従って \(j|L_{\vartheta_M}\) は \(j|\vartheta_M\) で決まる。
3. \(x\in M\) に対し、\((\operatorname{trcl}\{x\},\in)\) をコードする \(<_L\)-最小の \(A\subseteq\vartheta_M\) を取る。1 により \(j(A)=\bigcup_{\xi<\vartheta_M}j(A\cap\xi)\) で、2 により右辺は \(j|\vartheta_M\) で決まる。\(j(x)\) は \(j(A)\) の復号である。

## 3. アクセス可能性と大きさ

**補題 B。** \(c\) が大きいとき \(\mathcal C_\mu^c\) は大きいアクセス可能圏で、\(\mu^+\)-有向余極限を持つ。\(\mathcal C_\mu\) も同様である。

- **\(\mu^+\)-有向余極限。** 初等埋め込みの直極限は、降下列が一段階に集まるので整礎で、崩壊して推移的になる。\(\mu\)-列の元も一段階に集まり、その段階の列 \(s\) について \(j_i(s)=j_i\circ s\) だから条件 2 が保たれる。条件 1・3・4 は \(\mu,c\) を助変数とする一階の条件で、初等直極限で保たれる。
- **表示。** \(\theta^\mu=\theta\ge\mu^+\) とする。対象 \(M\) の \(\theta\) 個以下の元を含み、\(\mu+1\) を含み、Skolem 関数と \(\mu\)-列で閉じた初等部分構造 \(Z\) を濃度 \(\le\theta\) で取れる。\(Z\supseteq H_{\mu^+}\) であり、その崩壊は再び対象で、逆崩壊は射である。これらは \(\theta^+\)-有向な表示を与え、濃度 \(\le\theta\) の対象は \(\theta^+\)-可呈示である。\(V=L\) では \(\theta=\mu^+\) が使える。
- **大きさ。** \(\vartheta\) を共終数 \(\mu^+\) の特異基数とし、\(M=H_{\vartheta^+}=L_{\vartheta^+}\) を取る。条件 1–3 は成り立つ。GCH と \(\operatorname{cf}(\vartheta)>\mu\) から \(\vartheta^\mu=\vartheta\) なので、\(c\) の濃度 \(\ge\vartheta\) のモデルから、\(\vartheta\) 個の元を証人で閉じた部分構造を取ると濃度がちょうど \(\vartheta\) の \(c\)-モデルを得る。台を \(\vartheta\) に移せば \((A_c)\) が成り立つ。\(S_\mu\) は集合なので、十分大きい \(\vartheta\) では全 \(c\in S_\mu\) について同時に成り立つ。そのような \(\vartheta\) は非有界にあり、対応する \(H_{\vartheta^+}\) は互いに同型でない。

この補題には「強到達不能基数がない」は使わない。

## 4. 最小モデル関手と還元

**命題 C。** \(c\in H_{\mu^+}\) が大きいとき、忠実で \(\mu^+\)-有向余極限を保存する関手 \(\Phi_c\colon\mathcal C_\mu^c\to\operatorname{Mod}(c)\) がある。

\(\Phi_c(M)\) を、\(M\) の中で \(<_L\)-最小の、ソートが \(\vartheta_M\) の分割である \(c\)-モデルとし、\(\Phi_c(j)=j|\vartheta_M\) とする。

- \(j\) は \(c\) を固定するので \(j(\Phi_c(M))=\Phi_c(N)\)。ソート名は固定され、長さ \(\mu\) 以下の組 \(t\) について \(j(t)=j\circ t\) だから、\(j|\vartheta_M\) は関係を保つ準同型である。
- 忠実性は補題 A。
- \(\mu^+\)-有向余極限 \(M_\infty\) では \(\vartheta_\infty=\bigcup_i j_i[\vartheta_i]\) で、長さ \(\mu\) 以下の組は一段階から来る。関係の成立は初等性により段階と一致するので、\(\Phi_c(M_\infty)\) は \(\operatorname{Mod}(c)\) でのソートごとの余極限である。

**定理 D（\(V=L\)）。** \(P\iff\exists\mu\,\forall\mu'>\mu\ \ \mathcal C_\mu\preceq\mathcal C_{\mu'}\)。

- 任意の大きいアクセス可能圏は、ある \(\mu\) と大きい \(c\in H_{\mu^+}\) について \(\operatorname{Mod}(c)\) と同値である（原著定理 5.35、コードは改名してよい）。充満な包含 \(\mathcal C_\mu\subseteq\mathcal C_\mu^c\) と \(\Phi_c\) の合成により \(\mathcal C_\mu\preceq\operatorname{Mod}(c)\)。
- （\(\Leftarrow\)）\(\mathcal T=\mathcal C_\mu\) とする。大きい \(\mathcal K\simeq\operatorname{Mod}(c)\) に対し \(c\in H_{\mu'^+}\) となる \(\mu'>\mu\) を取れば \(\mathcal C_\mu\preceq\mathcal C_{\mu'}\preceq\mathcal K\)。
- （\(\Rightarrow\)）\(P\) の始域を \(\mathcal T\simeq\operatorname{Mod}(c_0)\)、\(c_0\in H_{\mu^+}\) と表示すると、任意の \(\mu'\) で \(\mathcal C_\mu\preceq\mathcal T\preceq\mathcal C_{\mu'}\)。

## 5. 小さい圏からの忠実関手への言い換え

\(\theta^\mu=\theta\ge\mu'\) とし、濃度 \(\le\theta\) の対象のなす \(\mathcal C_\mu\) の小さい充満部分圏を \(\mathcal C_\mu^{\le\theta}\) とする。このとき

\[
\mathcal C_\mu\preceq\mathcal C_{\mu'}\iff\text{ある }\theta\text{ で忠実関手 }\mathcal C_\mu^{\le\theta}\to\mathcal C_{\mu'}\text{ が存在する。}
\]

右から左は [extendible のノート §2](common_sources_and_extendibility.md) の延長による。\(\mathcal C_{\mu'}\) の射はすべて単射で、\(\theta^+\)-有向余極限は合併として計算できるので、\(\operatorname{Ind}_{\theta^+}\) による延長は忠実になる。左から右は、関手のランクより大きい \(\theta\) で制限すればよい。従って問題は、与えられた小さい圏を \(\mu'\)-列で閉じた \(L_\beta\) と初等埋め込みで忠実に実現できるかである。

## 6. 射の形と、使える障害

**射の形。** \(j\colon M\to N\) が全順序数を固定すれば \(M\prec N\) の包含で、\(\vartheta_M=\vartheta_N\) である。そうでないとき、補題 A から臨界点 \(\gamma\) は \(\vartheta_M\) 未満の \(M\)-正則基数である。\(\mathcal P(\gamma)\subseteq M\) なら \(\{A:\gamma\in j(A)\}\) が可算完備な非主超フィルターになり、\(L\) に可測基数がないことに反する。従って \(\mathcal P(\gamma)\nsubseteq M\) で、\(\gamma\ge(\mu^{++})^M\)。特に \(\vartheta_M\) が実際の基数である対象から出る射は包含だけである。対象に「強到達不能基数がない」を課せば、\(\gamma=(\delta^+)^M<(\delta^+)^N\) の形に限られる。

**識別不能列による障害。** 有限順序数 \(n\) と順序埋め込み、および一つの対象 \(X\) と、\(\omega_1\) の各増加 \(n\)-組に対応する射 \(n\to X\) からなる圏を \(\Delta_{\omega_1}\) とする（\(X\) の自己射は恒等射のみ）。**\(V=L\) では、\(\Delta_{\omega_1}\) から \(L_\beta\) と初等埋め込みの圏への忠実関手は存在しない。** 実際、関手 \(G\) があれば、\(x\in G(1)\) を取り \(e_i=G(i)(x)\in G(X)\) と置くと、増加組 \(\bar\imath\) について \(e_{\bar\imath}\) の型は \(G(n)\) における固定した組の型に等しく、\(\bar\imath\) によらない。忠実性から、ある \(x\) で \(e_i\) は互いに異なる。\(<_L\) の順位に移せば、極限順序数 \(\beta^*\) の \(L_{\beta^*}\) に非可算な識別不能順序数の集合が得られ、\(0^\#\) が存在する（Jech, *Set Theory*, 系 18.18）。

この障害は \(\mathcal C_\mu\) と \(\mathcal C_{\mu'}\) の両方に同じく働くので、単独では二つを区別しない。区別に使える非対称性は、\(\mathcal C_{\mu'}\) の対象が長さ \(\mu^+\) の列を元として持つのに対し、\(\mathcal C_\mu\) の対象は持たないことである。\(\mathcal C_\mu\) の \(\mu^+\) 本の射の族の像は、終域では一つの元になる。

## 7. 未解決

- \(\mathcal C_\mu\preceq\mathcal C_{\mu'}\) の成否。最小の場合は \(\mu=\omega\)、\(\mu'=\omega_1\)。
- 肯定側の候補は、\(L_\beta\) を \(L_{\kappa+\beta}\) 型の対象へずらす構成。生成元の型の保存が条件になる。
- 否定側の候補は、\(\mu^+\) 本の射の族から終域の中に列を作り、§6 の識別不能列かそれに類する矛盾を導くこと。
