# Ab / Grp の除外結果の再点検

2026-11-15、第2段階。対象は [元ノート](../prior_notes/ab_grp_coorthogonality_progress.md)。ZFC、ordinary Hom、充満・同型閉部分圏で議論する。

状態は **主担当による証明の再構成**。今回の新しい証明は別担当による独立監査・形式検証・外部査読を経ていない。文献上の新規性も未確認。元ノートは変更しない。

## 1. 監査した還元

以下の主要な議論に、結論を壊す誤りは見つからなかった。

| 元ノート | 確認した内容 | 必要な限定 |
|---|---|---|
| §§1–2 | 集合個の射の積による一本化、商と余積に閉じたクラスの trace coreflection | Ab/Grp の零射・自明射を使う。mono と split epi の条件は商閉 |
| §3 | torsionless な Ab の始域を除外 | torsion-free と混同しない。非零 kernel が Z を含むことと U→Z^J を併用 |
| §4 | Hom(-,K)=Ext¹(-,K)=0 のクラス W_K の分類 | Ext²_Z=0 と内部の kernel 閉性が必要 |
| §§5–5.1 | 可除始域、torsion 始域、および列挙された種類のテスト族の除外 | 三種類の群の任意の直和を始域にする主張ではない |
| §§6–7 | Whitehead 案の退化と Ab→Grp の移送 | 移送の逆方向はアーベルな標的 B に対する主張 |
| §§8–9 | Grp の中心拡大への還元と自由群始域の除外 | 中心拡大以外の二つの mono 条件を残す |
| §§10–11 | 特定拡大類の pullback 消滅、cellular cover と coreflection の区別 | 任意の kernel K について Ext¹(-,K) 全体の消滅に置き換えない |

主な証明上の要点を以下に残す。

## 2. W_K の分類とその適用

$W_K=\{A:\operatorname{Hom}(A,K)=0=\operatorname{Ext}^1(A,K)\}$ とする。可除群への埋め込み $K\to I$ と商 $q:I\to I/K$ を使うと $W_K={}^\perp q$。従って小余極限に閉じる。

内部の射 $A\to B$ の像を $J$、cokernel を $D$ とする。$D\in W_K$ であり、$0\to J\to B\to D\to0$ の長完全列と $\operatorname{Ext}^2(-,K)=0$ から $J\in W_K$。次いで $0\to\ker\to A\to J\to0$ から kernel も $W_K$ に入る。同じ長完全列で拡大閉性も従う。$\operatorname{Ext}^2_{\mathbb Z}=0$ は、自由群の部分群が自由であり、アーベル群が長さ1の自由分解を持つため。

この閉性を持つ非空な部分圏 $W\subseteq\mathrm{Ab}$ を考え、$J=\{p:\mathbb Z/p\in W\}$ と置く。

- $\mathbb Q\notin W$ なら全対象が torsion。非 torsion 対象があれば rationalization と retract により Q が入ってしまう。各 p-torsion は乗法 p の kernel と retract により Z/p を検出する。一方、Z/p から拡大・filtered colimit・直和で全 p-primary torsion 群を得る。従って W は J-primary torsion 群全体。
- $\mathbb Q\in W$ なら、$p\notin J$ について乗法 p の kernel と cokernel は零。従って W は $R=\mathbb Z[p^{-1}:p\notin J]$-加群の中に入る。$p\in J$ について Prüfer 群が W に入り、$0\to R\to\mathbb Q\to\bigoplus_{p\in J}\mathbb Z(p^\infty)\to0$ の kernel として R も入る。R の直和と cokernel で全 R-加群が得られる。

前者の coreflector は torsion subgroup、後者は $\operatorname{Hom}_{\mathbb Z}(R,-)$。よって W_K は ZFC で coreflective。

可除始域 $U$ の射では、像 $I$ も可除で $V=I\oplus C$ と分裂し、条件は $W_{\ker f}\cap\{A:\operatorname{Hom}(A,C)=0\}$ となる。後者は商・直和閉なので、上の二場合の内部で trace を取れる。

torsion 始域の場合、$P=\{p:(\ker f)[p]\ne0\}$ に対して A の p-divisibility が強制される。A から U_p への像は U_p の最大可除部分 D_p に入る。P 内の D_p と P 外の U_q に分ければ、前者は可除始域、後者の制限射は mono。可除像を V から分裂させても、素数が互いに異なるので後者から可除像への交差成分は零となる。これで元ノート §5.1 の等式が正当化される。

境界条件：空の prime 集合は零 torsion class または全 Ab を与える。空テスト族は全圏。これらも同じ証明に含まれる。

## 3. Grp の中心拡大への還元

$f:U\to V$、$N=\ker f$、$C=C_U(N)$、$I=f(C)$ とし、$j:C\hookrightarrow U$、$e:C\twoheadrightarrow I$、$m:I\hookrightarrow V$ とする。

$A\perp f$ なら、任意の $u:A\to U$ と $n\in N$ について $c_nu$ と u は f の後で一致する。持ち上げの一意性から u の像は C に入る。mono m の Hom は単射なので、積 $f j=m e$ の全単射性は e と m の各全単射性に分かれる。従って

$$ {}^\perp f={}^\perp\{j,e,m\}. $$

$\ker e=N\cap C=Z(N)$ は C の中心に入る。中心拡大への二つの lift の差は kernel への準同型なので、一意性は $\operatorname{Hom}(A,Z(N))=1$ で表せる。一般の非中心拡大で二つの lift の差を通常の準同型として扱うことはできない。

## 4. 追加の肯定結果：Z(ker f) が有限なら除外できる

まず Ab の $\mathcal N_K=\{A:\operatorname{Hom}(A,K)=0\}$、または Grp でアーベル群 K に対する同じ null class を考える。商と余積に閉じるので包含は trace による右随伴 T を持つ。

**補題。** $\mathcal N_K$ が locally presentable なら、Ab の kernel K を持つ任意のテスト射、および Grp の中心 kernel K を持つテスト射への coorthogonality class は coreflective。

**証明。** クラスは $\mathcal N_K$ 内に入る。随伴により残りの条件は $Tf$ への coorthogonality。任意の $A\in\mathcal N_K$ に対し $\operatorname{Hom}(A,f)$ は単射なので、$Tf$ は $\mathcal N_K$ 内の mono である。locally presentable category 内の mono への coorthogonality は、余極限・strong quotient 閉性と部分対象の trace により coreflective。包含の右随伴を合成すればよい。∎

注意：$Tf$ が **元の圏でも** mono だとは限らない。また $\mathcal N_K$ の局所可呈示性を無条件に仮定してはいけない。

**有限アーベル群 K の場合。** K の位数を割る素数集合を P とする。

$$G\in\mathcal N_K\iff G_{\rm ab}=pG_{\rm ab}\quad(p\in P).$$

各 p について K が Z/p を含むことが必要性を与える。十分性は、p-divisible 群から有限 p-群への写像が零であることによる。

このクラスの局所 $\aleph_1$-可呈示性を直接示せる。$G\in\mathcal N_K$ の可算集合から始め、各 g と $p\in P$ について

$$g=h^p\prod_{j=1}^r[u_j,v_j]$$

と書くための有限個の証人を G 内で加える。これを可算回反復すると、可算な $\mathcal N_K$-部分群を得る。Ab では可換子部分を省く。各 G はそのような可算部分対象の $\aleph_1$-directed union である。可算群は Grp で $\aleph_1$-presentable、小余極限閉性により部分圏でもそうである。従って $\mathcal N_K$ は locally $\aleph_1$-presentable。

§3 と補題を合わせると、**Grp の任意の f について Z(ker f) が有限なら ${}^\perp f$ は coreflective**。j,m の条件も Tj,Tm という mono に移して残す。Ab では有限 kernel が十分である。始域・終域の大きさに制限はない。

この新しい証明は主担当の再構成段階。K=0、K=Z/p、複数素数を持つ有限 K で同じ条件になることを確認した。有限群の全列挙から無限の結論を導いてはいない。

## 5. 文献との照合と候補の扱い

- [Cortés-Izurdiaga–Crivei–Saorín, Corollary 7.2](https://arxiv.org/pdf/2109.05111)（v2, 2022、PDF p.16）では、preabelian category の additive subcategory が coreflective であることと、precovering かつ cokernel 閉であることの同値を確認した。A_f では cokernel 閉性は自動だが、precovering 性は残る。
- [Eklof–Shelah, p.200](https://shelah.logic.at/files/95759/621.pdf) では、非零 Whitehead 群の整数双対が非零であることを確認した。従って Q→Q/Z は Ab で零クラスとなり、独立性の証人にはならない。
- [Farjoun–Göbel–Segev–Shelah, Theorem 2.11](https://arxiv.org/pdf/math/0702294) は固定 M に対する無界なサイズの cellular covers を与える。ただし固定 f の A_f 全体の factor-size 障害とは異なる。f 自体が cellular cover なら、その終域で f が A_f-coreflection になる、という元ノートの指摘も正しい。

今回調べた具体例は [無限候補の計算](../investigations/algebraic_candidates_2026-11-15.md) に記す。特に「可算で非分裂、始域が旧除外三種類に入らない」だけでは、非 coreflectivity の証拠にならない。
