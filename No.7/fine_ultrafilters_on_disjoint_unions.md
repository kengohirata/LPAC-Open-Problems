# No.7 と非交和上の完備超フィルター

一般の No.7 を \(P_7\) とする。前稿の上下界に使った二つの構成を組み合わせると、集合パラメータ付き定義可能クラスの同じ規約の下で、\(P_7\) を次の集合論的条件に帰着できる。以下は今回の直接証明で、独立検証前である。

## 条件

任意の無限基数 \(\rho\)、任意の出発基数 \(\tau>\rho\)、および各正則基数 \(\kappa\ge\tau\) に基数 \(\lambda_\kappa\ge\kappa\) を割り当てる任意のクラス関数を取る。正則基数の非空な**集合** \(J\subseteq[\tau,\mathrm{Ord})\) と、
\[
  I_J=\coprod_{\kappa\in J}P_\kappa(\lambda_\kappa),
  \qquad P_\kappa(\lambda)=\{s\subseteq\lambda:|s|<\kappa\}
\]
上の \(\rho^+\)-完備超フィルター \(U\) が存在し、次を満たすかを問う。
\[
  \forall (a_\kappa)_{\kappa\in J}\in\prod_{\kappa\in J}P_\kappa(\lambda_\kappa),\qquad
  \{(\kappa,s)\in I_J:a_\kappa\subseteq s\}\in U. \tag{1}
\]
各成分で**別々に指定した**小集合を同時に使えることが条件である。\(J\) が一点のとき、通常の fine 性よりも大きい、サイズ \(<\kappa\) の集合を含むすべての上方錐を要求する。超フィルターの完備性として仮定したのは \(\rho^+\) までである。

## No.7 から (1)

\(|\Omega|=\rho\)、\(M=\mathrm{End}(\Omega)\) とし、局所可呈示圏 \(M\)-Set を取る。\(I_\kappa=P_\kappa(\lambda_\kappa)\)、\(F_\kappa\) をその上方錐が生成するフィルターとし、\(Q_\kappa=\Omega^{I_\kappa}/F_\kappa\) とする。正則性により \(F_\kappa\) は固有な \(\kappa\)-完備フィルターである。\(\mathcal C\) は全 \(Q_\kappa\) の小積のレトラクト全体とする。

任意の \(u:A\to B\) にすべての \(Q_\kappa\) が入射的なら、\(\Omega\) も入射的である。実際、\(|M|,|A|,|B|,\aleph_0\) を超える \(\kappa\) を選ぶ。任意の \(A\to\Omega\) を定数列で \(Q_\kappa\) に送って \(B\) に沿って延長し、像の代表列を選ぶ。作用の保存と元の射への一致を要求する各等式は \(F_\kappa\)-大な集合で成立し、それらの個数は \(\kappa\) 未満である。共通部分の一点で評価すればよい。従って \(P_7\) が成り立てば \(\Omega\in\mathcal C\) であり、ある小積から \(\Omega\) への \(M\)-射がある。空積からそのような射はない。

各商射の積を前合成すると、添字集合の非交和を \(I\) として \(M\)-射 \(\Omega^I\to\Omega\) を得る。このような射は \(I\) 上の \(\rho^+\)-完備超フィルターによる評価と一致する。積内の各成分で錐を一つずつ選ぶと、その非交和の特性関数は商の積では定数 1 と一致する。従ってその非交和は超フィルターに属する。因子の重複があれば、各コピーを元の成分に送る写像で超フィルターを押し出せば (1) を得る。[評価と超フィルターの対応、補題1](../No.1/codex_sset_handoff/investigations/measurable_thresholds_and_strong_compactness_2026-11-17.md)

## (1) から No.7

積とレトラクトで閉じる \(\mathcal C\subseteq\mathcal K\) と \(X\in\mathrm{Inj}(H(\mathcal C))\) を固定し、前稿と同じ充満忠実な右随伴 \(N:\mathcal K\to\widehat D\) を取る。\(\rho\ge |NX|,|\mathrm{Mor}\,D|,\aleph_0\)、\(\tau=\rho^+\) とする。各正則 \(\kappa\ge\tau\) について、前稿の「積に入れる射の選び方」の三段階は ZFC だけで \(p_\kappa:X\to C_\kappa\)、\(C_\kappa\in\mathcal C\) を与える。\(Np_\kappa\) の像を含むサイズ \(<\kappa\) のすべての部分前層上で \(Np_\kappa\) に左逆がある。[前稿の局所構成](compactness_upper_bound_and_failure_of_wvp.md)

\(\lambda_\kappa\) は、この性質を持つ \(p_\kappa\) で \(|NC_\kappa|\le\lambda_\kappa\) となるものが存在する最小の基数 \(\ge\kappa\) とする。これはクラス選択を要しない。一度 (1) を適用して \(J,U\) を得たら、\(J\) の範囲だけで証人 \(p_\kappa\) と、各ソートの元を区別する \(NC_\kappa\) の全要素の \(\lambda_\kappa\) への単射を選ぶ。集合添字の証人は Collection と選択で足りる。

\(s\in P_\kappa(\lambda_\kappa)\) ごとに、符号が \(s\) に属する要素と \(Np_\kappa\) の像が生成する部分前層を \(B_{\kappa,s}\) とする。サイズは \(<\kappa\) である。上記の左逆 \(r_{\kappa,s}:B_{\kappa,s}\to NX\) を選ぶ。\(P=\prod_{\kappa\in J}C_\kappa\) の各ソートの元 \(y=(y_\kappa)_\kappa\) に対し、(1) を各 \(y_\kappa\) の符号の一元集合に適用すると、\(y_\kappa\in B_{\kappa,s}\) となる \((\kappa,s)\) の集合は \(U\)-大である。その上で \(r_{\kappa,s}(y_\kappa)\) の取りうる値は \(\rho\) 個以下なので、\(U\)-ほとんど至る所で一意な一定値を持つ。それを \(r(y)\) とする。各 \(r_{\kappa,s}\) の自然性と左逆の等式から、\(r:NP\to NX\) は自然変換で、\(N\langle p_\kappa\rangle\) の左逆となる。\(N\) が充満忠実なので \(X\) は \(P\) のレトラクトであり \(X\in\mathcal C\)。□

## 否定例のために次に検証する命題

**追記。** 下記の最小値を使う族は、出発基数が最初の可測基数 \(\mu\) 未満なら、ちょうど \(\mu\) 個の成分で条件 (1) を満たす。成分の濃度を変更すると、同じ範囲の全添字集合にわたり持ち上げを排除できる。[最初の可測基数での構成と排除](first_measurable_index_size.md)

仮に almost strongly compact 基数の真クラス存在が失敗すれば、ある \(\rho\) について、どの \(\kappa\ge\rho^+\) も \(L_{\rho^+,\omega}\)-compact ではない。そのような各正則 \(\kappa\) について、一本の成分では (1) を満たさない最小の \(\lambda_\kappa\) がある。実際、任意の固有な \(\kappa\)-完備フィルター \(F\) に対し、\(\lambda\ge |F|,\kappa\) として \(F\) の元を \(\lambda\) で符号化し、各 \(s\in P_\kappa(\lambda)\) について \(s\) が指定するフィルター要素の共通部分から一点を選べる。錐をすべて含む超フィルターがあれば、この選択写像で押し出して \(F\) を延長できる。逆向きは錐フィルター自体に延長性を適用すればよい。[Brooke-Taylor–Rosický, Definition 2.3・Proposition 2.4](https://arxiv.org/pdf/1506.01986)

この具体的な \(\kappa\mapsto\lambda_\kappa\) が反例かを調べるには、可測基数が非有界なモデルで、**すべての集合 \(J\)** について (1) が失敗することを示せば十分である。もし \(U\) が存在すれば、添字への射影 \(\pi:I_J\to J\) による \(\pi_*U\) は非主的な \(\rho^+\)-完備超フィルターでなければならない。主的なら、その一つの成分への制限が \(\lambda_\kappa\) の選び方に反する。従って \(|J|\) が \(\rho\) より上の最初の可測基数未満の場合は排除済みである。上の追記により、出発点がその可測基数未満なら、最小の選び方では実際にその可測基数の濃度で成功する。(1) は他の出発点とクラス関数にも量化している。
