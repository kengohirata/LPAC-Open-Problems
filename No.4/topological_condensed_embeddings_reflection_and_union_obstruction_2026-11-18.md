# Problem 4：位相空間の condensed embedding と directed union の障害

2026-11-18。状態：PROOF_RECONSTRUCTED（標準的埋め込みの除外と明示的 union 反例）。No.4 の反例は構成していない。以下は標準的な小 probe・condensed・逐次収束の経路を調べた結果であり、任意の別種の full embedding を否定するものではない。

内部確認：別 agent が §3 の directed union 反例と §7 の閉包・反射の構成を監査し、問題を見出さなかった。外部査読・形式検証は未実施。

## 1. 固定した小 site と、全ての空間を混同しない

κ を非可算 strong limit cardinal とし、Prof_<κ を濃度 κ 未満の profinite spaces の小 skeleton とする。有限 jointly surjective families による topology の sheaf category を Cond_κ と書く。

    N_κ(X)(S)=Top(S,X),  S∈Prof_<κ

は位相空間から Cond_κ への functor である。Clausen–Scholze の講義ノート Proposition 1.7 は、N_κ が κ-compactly generated spaces 上で fully faithful であり、topological realization L_κ を左随伴に持つことを示す。κ-compactly generated とは、κ 未満の compact Hausdorff probes からの写像が位相を決めるという条件である。[原講義ノート、pp.8–9](https://www.math.uni-bonn.de/people/scholze/Condensed.pdf)

ここで Cond_κ は小 site 上の Grothendieck topos、従って locally presentable である。一方「全ての compactly generated spaces が、この一つの Cond_κ に fully faithfully 入る」とは言えない。§4 で具体的に否定する。

## 2. fully faithful な範囲は既に reflective

L_κ(F) は集合 F(*) に、全ての S∈Prof_<κ と a∈F(S) に由来する写像 S→F(*) についての final topology を入れた空間である。従って L_κ(F) は κ-compactly generated で、随伴の counit は

    L_κ N_κ(X) ≅ k_κ X → X

となる。よって κ-compactly generated spaces の N_κ-image は Cond_κ の reflective full subcategory であり、その embedding は全ての小極限を保つ。

Hausdorff 条件や weak Hausdorff 条件を加えても、ここから非反射的な候補は得られない。

* Hausdorff reflection X→h_H X は quotient map として取れる。全ての Hausdorff 空間への写像の kernel relation の共通部分で割り、quotient topology を入れる構成である。対角写像による Hausdorff product の部分空間位相より quotient topology の方が細かいので、商は Hausdorff になる。
* CG spaces から CGWH spaces への weak Hausdorff reflection も quotient map として取れる。これは Strickland, *The category of CGWH spaces*, Proposition 2.22 の明示的な構成である。[原ノート PDF、p.7](https://ncatlab.org/nlab/files/StricklandCGHWSpaces.pdf)
* κ-compactly generated spaces は quotient で閉じる。実際、それらは κ-small compact Hausdorff spaces の coproduct の quotient であり、quotient の合成も quotient である。

従って h_H L_κ と h_WH L_κ は、それぞれ κ-compactly generated Hausdorff spaces、κ-compactly generated weak Hausdorff spaces の image への反射を与える。これらの embedding は fully faithful かつ全極限保存である。

ただし、これらの image は ambient directed union で閉じない。次節で、それを countable compact Hausdorff spaces だけを用いて示す。

## 3. 明示的な directed union の失敗

I=[0,1] とし、J を I の全ての可算 compact subsets K の集合とする。包含で順序付けると、K∪K' も可算 compact なので J は directed。各 K は compact Hausdorff、従って κ-compactly generated Hausdorff である。

Cond_κ における mono diagram の union を

    F=colim_(K∈J) N_κ(K) ⊂ N_κ(I)

とする。

### 3.1 ambient union の具体的な内容

Prof_<κ の sheaf condition は、有限 coproduct を product に送る条件と、各 surjection に対する一つの equalizer condition で書ける。filtered colimits は Set の有限極限と可換なので、この colimit は objectwise に計算できる。従って

    F(S)={f:S→I continuous : f(S) is countable}。

ここで逆向きも成り立つ。可算像 f(S) は compact Hausdorff 空間 I 内の compact subset なので、それ自身が J の対象となる。

### 3.2 位相的 realization は元の区間に戻る

Top における colim_(K∈J) K は通常の位相を持つ I である。

実際、A⊂I が全ての K∈J に対して A∩K closed in K を満たすとする。A 内の収束列 x_n→x を取れば、K={x}∪{x_n:n∈ω} は J に属する。A∩K が closed なので x∈A。従って A は sequentially closed であり、I は metric space なので A は closed。逆向きは明らかである。

L_κ は左随伴なので colimit を保ち、

    L_κ(F) ≅ I。

### 3.3 F はいかなる位相空間の nerve でもない

Cantor space C=2^ω から I への連続全射 q を取る。κ は非可算 strong limit なので |C|=c<κ、すなわち C は site の probe である。q の像は非可算なので

    q∈N_κ(I)(C),  q∉F(C)。

よって unit F→N_κL_κ(F)=N_κ(I) は同型でない。もし F≅N_κ(X) なら、N_κ(k_κX)≅N_κ(X) と L_κN_κ(X)=k_κX からこの unit は同型になるはずであり、矛盾。

**結論（ZFC）。** Cond_κ 内で、countable compact Hausdorff spaces の nerves の directed union が、位相空間の nerve の範囲から既に脱落する。従って κ-CG、κ-CGHaus、κ-CGWH の各 image は directed union で閉じない。

これは「位相空間の側で union が存在しない」という障害ではない。位相空間の union は I として存在し、ambient sheaf union と一致しないという障害である。

## 4. 小 probe では全ての CGHaus を fully faithfully 見られない

より一般に、小さい集合 A の位相空間を probes として使うとする。それらの underlying sets の濃度を全て上回る正則基数 λ を取る。

    X=[0,λ]（順序位相）,  X^+=[0,λ) ⊔ {λ}

と置く。X は compact Hausdorff、X^+ は locally compact Hausdorff で、共に CGHaus である。同じ underlying set 上の恒等写像

    u:X^+→X

は連続な全単射だが同相でない。

しかし任意の A∈A と連続写像 f:A→X について、f(A)\{λ} は λ 未満に有界である。従ってある β<λ に対して

    f^(-1){λ}=f^(-1)((β,λ])

は open。よって f は X^+ にも連続に lift する。つまり全ての probes A に対して Top(A,u) は全単射となる。

従って restricted nerve は u を同型に送るが、u 自身は同型でない。fully faithful functor は同型を反映するので、どの固定した小 probe family も CGHaus 全体、従って CGWH 全体の fully faithful nerve を与えない。これは小 dense subcategory が存在しないことも示す。

特に Prof_<κ を固定した Cond_κ の場合にもこの障害がある。大きな空間を扱うたびに κ を拡大する操作は、一つの locally presentable ambient category に全対象が入ることとは別である。

## 5. 全ての cardinal stage を合わせた Cond は LP ambient にならない

Clausen–Scholze の Proposition 2.9 と Definition 2.11 は、Cond を Cond_κ の fully faithful な colimit-preserving transition functors に沿った大きな union として定義する。extremally disconnected spaces への制限では、transition は left Kan extension である。[原講義ノート、pp.14–15](https://www.math.uni-bonn.de/people/scholze/Condensed.pdf)

この記述から Cond が locally presentable でないことを直接確認できる。

**補題。** どの固定 stage Cond_κ も Cond 全体ではない。

**証明。** 濃度 κ 以上の extremally disconnected compact Hausdorff space E を取る。例えば十分大きい離散集合の Stone–Čech compactification でよい。もし representable condensed set N(E) が Cond_κ の image にあれば、E における left Kan extension の表示から、id_E:E→E は

    E→S→E,  |S|<κ

と分解される。すると E→S は単射で、|E|<κ という矛盾を得る。□

もし Cond が locally presentable なら、ある小集合 G の objects が小 colimits によって全対象を生成する。G の各対象が属する stage の bound を取り、一つの Cond_κ に全てを入れられる。しかしその image は全ての小 colimits で閉じるので、Cond 全体がその stage に含まれてしまい、補題に反する。

したがって、大きい Cond に移って標準的な all-size embedding を得ても、No.4 の locally presentable ambient という条件を失う。この結論は Campbell の seminar abstract にも明示されている「small generator がない」という記述と整合する。[本人の講演要旨](https://centre-of-australian-category-theory.github.io/seminar/talks/1632)

全 CGWH→Cond の full faithfulness 自体は、Clausen–Scholze, *Lectures on Analytic Geometry*, Proposition 1.2(4) に明記されている。小極限も保つ。CGWH の極限は通常の Top-limit を k-ify したもので、compact probes からの Hom は k-ification で変わらず、各 Hom(S,−) は極限を保つからである。ただし、これによって ambient の LP 性が得られるわけではない。[原講義ノート、p.8](https://www.math.uni-bonn.de/people/scholze/Analytic.pdf)

## 6. 小 nerve による別形式の埋め込みへの一般的注意

**一般補題。** C が locally small かつ cocomplete で、A→C が小図式であるとする。restricted nerve

    N:C→Set^(A^op),  N(X)(a)=C(Aa,X)

が fully faithful なら、その image は reflective である。

**証明。** presheaf P の category of elements は小さいので、

    L(P)=colim_((a,x)∈el(P)) Aa

が存在し、L⊣N。full faithfulness より counit は同型。□

N がある full sheaf subcategory に値を取る場合にも、この L を sheaf objects に制限すれば同じ随伴が得られる。従って、cocomplete な空間の圏を小 probe の fully faithful nerve として提示する標準的方法は、通常は反射を同時に構成している。

逐次収束に限定した既知の例でも同じ点に注意が必要である。Menni–Simpson, *Topological and limit-space subcategories of countably-based equilogical spaces*, §3.3 は、sequential spaces Seq→Lim の embedding に、sequentially open subsets で位相を入れる左随伴があることを明記する。[原論文、p.748](https://www.pure.ed.ac.uk/ws/portalfiles/portal/12309421/S0960129502003699a.pdf)

本ノートでは、任意の filters を使う convergence-space category の locally presentable 性を仮定していない。また、そのような圏への embedding が全ての directed union を保つという未確認の主張も使っていない。

## 7. union 閉包を取る修復も reflective なクラスに到達する

固定した Cond_κ の中で、quasicompact object とはある profinite probe S から epimorphism N_κ(S)↠F を持つ object とする。quasiseparated object とは、任意の二射 N_κ(S)→F、N_κ(T)→F の pullback が quasicompact となる object とする。その full subcategory を QS_κ と書く。

### 7.1 quasicompact subobject の具体形

S が κ-small profinite で、R↪N_κ(S) が quasicompact なら、R は S の closed subspace の nerve である。

実際、κ-small profinite U と epimorphism N_κ(U)↠R を取り、合成 N_κ(U)→N_κ(S) を連続写像 f:U→S に対応させる。像 H=f(U) は S の closed profinite subspace。U→H は surjection なので site の cover であり、N_κ(U)→N_κ(S) の sheaf image は N_κ(H) である。これは R と一致する。

### 7.2 quasicompact quasiseparated objects は compact Hausdorff spaces

F が quasicompact quasiseparated とし、N_κ(S)↠F を取る。kernel pair R は quasiseparated 性から quasicompact で、R↪N_κ(S×S)。§7.1 により R は S×S の closed equivalence relation の nerve となる。商 X=S/R は compact Hausdorff、|X|<κ であり、F≅N_κ(X)。逆方向も、compact Hausdorff spaces の対角が closed であることから直ちに分かる。

最後の同定は sheaf image の同定でも確認できる。任意の profinite T→X に対し、S×_X T は S×T の closed profinite subspace で、T へ全射する。従って N_κ(S)→N_κ(X) は epi で、kernel pair は R。topos 内の epi は自身の kernel pair の coequalizer なので、F と N_κ(X) は同じ商である。

### 7.3 products・subobjects・directed union 閉性

QS_κ は次の操作で閉じる。

* **Subobjects:** A↪F と S,T→A に対し、S×_A T=S×_F T。
* **Arbitrary products:** S,T→∏_i F_i の pullback は、N_κ(S×T) 内で S×_(F_i)T の共通部分。各々は §7.1 により closed profinite subspace であり、任意の共通部分も closed profinite subspace。従って quasicompact。
* **Directed unions:** profinite probes は Cond_κ の objectwise filtered colimit を検出するので、S,T→colim_i F_i は一つの共通 stage に入る。その stage→colimit が mono なので、二射の pullback はそこで計算したものと一致する。

Subobjects と products で閉じることから、全ての小極限でも閉じる。

### 7.4 各 quasiseparated object は compact Hausdorff subobjects の union

F∈QS_κ とし、全ての probe maps N_κ(S)→F の images を取る。各 image は quasicompact かつ quasiseparated なので、§7.2 により κ-small compact Hausdorff space の nerve。有限個の images の union は、有限 coproduct の probes からの map の image なので、再び同じ形である。

具体的には image I に対して N_κ(S)↠I が epi なので quasicompact、I↪F なので quasiseparated であり、N_κ(S)↠I の kernel pair は S×_F S と一致する。この relation が closed であることが、位相的な compact quotient と sheaf image を同定する根拠である。

これらの images は directed family をなし、その union は F。実際、F(S) の各 element に対応する map N_κ(S)→F は自身の image を経由するため、union は各 probe で F 全体を覆う。

κ-CGWH spaces の nerves は quasiseparated である。二つの compact probes の fiber product は、weak Hausdorff 条件により S×T の closed subset となるためである。特に κ-CGHaus spaces の nerves も含まれる。

**閉包定理（ZFC）。** Cond_κ 内で、κ-CGHaus または κ-CGWH の image に小極限と directed union を加えた最小の full replete subcategory は、ちょうど QS_κ である。κ-small compact Hausdorff spaces の nerves だけから出発しても同じ。

### 7.5 QS_κ への反射は quotient images の集合から構成できる

任意の F∈Cond_κ に対し、codomain が QS_κ に属する全ての epi quotients F↠Q を同型を除いて選ぶ。Grothendieck topos の epi quotients は kernel equivalence relations で分類されるため、これは集合である。

それらの積 P を取り、対角射 F→P の image を η:F↠R↪P とする。§7.3 により P,R∈QS_κ。

任意の f:F→Q、Q∈QS_κ は image I↪Q を経由し、I∈QS_κ。従って epi F↠I は選んだ quotient の一つであり、積の射影 P→I を R に制限することで f は η を経由する。η は epi なので分解は一意。これが QS_κ への反射である。

**結論。** 標準的な topological image の union 閉性の失敗を、limit・directed union 閉包を取ることで修復すると、反射的な QS_κ が得られる。この修復も No.4 の反例を与えない。

## 8. 三条件の確認と残る範囲

| 標準候補 | Full embedding | 小極限保存 | Ambient directed union 閉性 | No.4 への障害 |
|---|---|---|---|---|
| κ-CG → Cond_κ | 成立 | 成立 | §3 で失敗 | 既に reflective でもある |
| κ-CGHaus / κ-CGWH → Cond_κ | 成立 | 成立 | §3 で失敗 | quotient reflection を合成できる |
| 全 CGHaus / CGWH → 一つの Cond_κ | §4 で失敗 | full embedding として採用不可 | 採用不可 | cardinal bound を越えられない |
| 全 CGHaus / CGWH → 全 cardinal stages の Cond | 成立 | 成立 | §3 と同じ障害が残る | ambient が LP でない |
| QS_κ → Cond_κ | full inclusion | 成立 | 成立 | §7.5 により reflective |

これらは標準経路の具体的な除外である。CGHaus または CGWH に対する、restricted nerve と異なる任意の full embedding into an LP category が不可能だとは結論していない。そのような embedding を提案するなら、全極限と ambient directed union の保存を新たに証明する必要がある。
