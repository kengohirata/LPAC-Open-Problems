# Open Problem 3 — Removing co-wellpoweredness from locally generated categories

> **Current status — 2026-11-20 (summary added by Claude Opus 5.5; not human-verified).** The ordinal-rank candidate is a ZFC counterexample to Problem 3 as literally stated. So the answer is **no**: a cocomplete category with a strong generator formed by generated objects need not be locally presentable.
>
> - **The category:** ordinal-ranked bi-pointed sets ([details](ordinal_rank_candidate_and_boundedness_conflict_2026-11-17.md)).
> - **The four required properties hold**, each checked against the book's definitions:
>   1. cocompleteness;
>   2. the single object G is a strong generator;
>   3. G is ℵ₀-generated in the sense of Def. 1.67;
>   4. the initial object has a proper class of strong quotients, so the category is not locally presentable (Thm 1.58).
> - **Re-derivation:** an AI cross-check on 2026-11-20 re-derived all four properties and found no misreading of the definitions. It also recomputed the non-monic comparison at X_(ω+1). Finite cases were checked by exhaustive computation.
> - **The conflict with the book:** the "unresolved source conflict" below is the counterexample's disagreement with the book's density step on p.296. The cross-check located the error in that step. Theorem 1.11 and Prop. 1.22 use presentability, and the book replaces it by generatedness, but the transition maps of the canonical diagram are not monic.
> - **Consequences, if correct:**
>   - The book's remark on p.295 that the answer is positive under VP fails for the literal statement. So does its repetition in the 2018 introduction.
>   - The reformulation on p.296 in terms of full reflective subcategories is **not** equivalent to the literal statement. It is not refuted by this example and is true under VP.
> - **Still open:** novelty against the literature, including the relation to Börger–Tholen Ex. 4.3 and the Di Liberti–Rosický density step, has not been checked.
>
> Statements below that the candidate is unresolved, or that no ZFC negative answer is concluded, are superseded by this summary.

## Current dependency warning — 2026-11-17

**Do not identify the literal generated-strong-generator formulation with the full-reflective-presheaf formulation without an additional proof.** The ordinal-rank candidate and the explicit canonical-colimit calculation challenge the book's generated⇒dense step. These are reconstructed proofs, not independently refereed results.

See `density_gap_dependency_impact_audit_2026-11-17.md` for the impact audit. Older No.3 results using `L ⊣ E` retain a **full reflective presheaf presentation and the specified union preservation as independent hypotheses**. The ordinary locally-presentable-category presentation used in No.1/No.2 has a separate valid proof using actual presentability. No.1/No.2's previous independent-review status is unchanged.

The book's literal VP-positive comment and its repetition in the 2018 introduction require re-examination if the candidate is correct. A further density step in the available arXiv v2 of Di Liberti–Rosický (2022), Theorem 2.26, also needs a separate justification; this is not a counterexample to that theorem. Published-version differences and all downstream applications have not been exhaustively audited.

The chronological entries below are preserved as research history, not simultaneous unconditional claims.

## Source
J. Adámek and J. Rosický, *Locally Presentable and Accessible Categories* (1994),
“Open Problems,” pp. 295–296, Problem 3.
DOI: https://doi.org/10.1017/CBO9780511600579.011

## Exact problem
> Can the definition of a locally generated category be stated without
> co-wellpoweredness? More precisely, is every cocomplete category with
> a strong generator formed by generated objects locally presentable?

### ZFC formulation
Is the following true in ZFC?

If a locally small category K is cocomplete and has a **set** G of
**generated** objects forming a **strong generator**, then K is locally
presentable (equivalently, locally μ-presentable for some regular μ)?

For a regular cardinal λ, an object A is λ-generated when K(A,-)
preserves λ-directed colimits of monomorphisms. This is weaker than
λ-presentability, where the hom-functor must preserve all λ-directed
colimits. Since G is a set, generatedness can be arranged uniformly at
some sufficiently large regular λ.

A strong generator G means that the restricted Yoneda/nerve
K -> Set^{G^op} is faithful and conservative; equivalently, any proper
subobject of X fails to contain the image of at least one morphism
G -> X, G in G.

The missing standard hypothesis is (weak/strong) co-wellpoweredness:
that each object has only a set of strong quotients up to equivalence.
Under that hypothesis, the locally generated category is known to be
locally presentable. A locally presentable category is co-wellpowered.

## Formulation claimed equivalent in the book (p. 296) — equivalence under audit

**The converse reduction from the literal assumptions is not currently accepted as an input. The reflective formulation remains a separate, more restrictive question.**

Is every **full reflective** subcategory of a locally finitely
presentable category K, closed under λ-directed unions in K for some
regular λ, itself locally presentable?

The book explains that, starting from a cocomplete category with a set
A0 of λ-generated strong generators, closure under λ-small colimits
produces a small dense subcategory A of λ-generated objects. The
canonical functor
    E : K -> Set^{A^op}
is fully faithful and right adjoint, and preserves λ-directed colimits
of monomorphisms. (The source's K denotes the starting category.)

## Conditional results and status
- The book reports an affirmative answer under Vopěnka's principle (p. 295,
  via Corollary 6.8 and a boundedness argument analogous to Proposition 1.22).
  **The application to the literal formulation depends on the disputed boundedness step and is not an unconditional input in the current investigation.** The VP-positive result for an explicitly given full reflective presheaf subcategory has a separate route.
- L. Positselski and J. Rosický, “Nearly Locally Presentable
  Categories,” *Theory and Applications of Categories* 33 (2018),
  pp. 253–264, introduction, explicitly says it remained open whether
  set theory is needed to remove weak co-wellpoweredness, citing
  Adámek–Rosický Open Problem 3:
  https://www.tac.mta.ca/tac/volumes/33/10/33-10.pdf
- The example CPO is *nearly* locally finitely presentable but not
  locally presentable; the weaker notion of nearly presentable must
  **not** be confused with λ-generated. Thus this fact by itself does
  not solve Problem 3.
- Status after 2018 is not yet comprehensively audited; no claim of
  present-day openness or of a ZFC answer is made here.

## Research directions
(A) Positive: derive a solution set/weak co-wellpoweredness, or show
that the reflective image E(K) in the presheaf category is accessible
from closure under λ-directed unions. Locate precisely where the
standard proof uses quotient smallness.
(B) Negative: construct a full reflective subcategory of a locally
finitely presentable category, closed under λ-directed unions, which
is not locally presentable, or produce a cocomplete category with a
generated strong generator but a proper class of strong quotients.
(C) Set-theoretic: determine whether the statement is equivalent to,
weaker than, or independent via a fragment of Vopěnka's principle.

## Caution
The book's Problem 3 is distinct from Problems 1–2. Results in
neighboring problems may suggest constructions, but do not establish
anything about Problem 3 without checking all hypotheses.


## 2026-11-17: 肯定方向の第1段階

詳細：`positive_quotient_bounds_and_regular_towers_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。一般の ZFC 証明・反例・独立性は未確立。独立査読・形式検証・新規性確認は未実施。**

- presheaf への既知の反射表示を入力として、完備性・well-poweredness・strong epi–mono factorization を確保した。
- G の <λ 個の余積からなる集合 H を取り、全ての対象を H からの K-内部の像の λ-directed union として表示した。λ-generated objects は、ちょうど H の strong quotients である。
- K が locally presentable であることは、H ごとの strong quotient codomain の大きさに標的非依存の集合基数上界があることと同値。この局所的上界から全対象の weak co-wellpoweredness を導く証明を書いた。
- ZFC の肯定範囲を二つ確認：(i) H からの strong epi が全て regular epi、(ii) presheaf reflector が mono を保存する。
- 単純な kernel-pair count が strong quotients に使えないことを、Cat の [1]→BC_n (n≥2) で直接示した。これは Problem 3 の反例ではない。
- kernel pair の coequalizer を反復する canonical tower を検討。始域 H ごとの一様な集合順序数の停止上界と、上記の quotient smallness は同値。mono の列でないため generatedness をそのまま極限段階に使えないことが残る。
- VP が上界を与える機構を整理したが、その必要性は証明していない。サイズ問題への到達と、ZFC 独立性の確立を区別する。
- 文献確認を2022年の Di Liberti–Rosický と2026年の Kawase–Nasuまで追加。2026年の分解上界は presentability を使用しており、今回そのまま使うと循環する。網羅的な現在の解決状況の調査を完了したとは主張しない。


## 2026-11-17: N の下での否定方向 — 強商の無界性と generatedness の障害

詳細：`negative_trials_strong_quotients_and_copower_obstruction_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。No.3 の反例・独立性は未確立。独立査読・形式検証・新規性確認なし。**

- No.2 の採用済み入力「N の下で A_sigma が大域的 coreflective」を用い、K_0=(A_sigma)^op を調べた。K_0 は余完備で、二対象からなる strong generator を持つ。
- 新しく、順序数試験対象 Y_kappa から固定 T_*=(Omega^omega --id,shift*--> Omega^omega) への制限射 a_kappa が A_sigma 内で **strong mono** であることを証明。核となる補題は、評価射 Y_kappa->B を経由させる A_sigma 内の epi quotient は同型になる、という quotient rigidity。pushout で一意右持上げ性に移す。
- 従って K_0 には固定 T_*^op からの strong epi quotients が真クラス個あり、非 locally presentable。ただし **K_0 は No.3 の反例ではない**。
- ZFC の一般補題：前層圏の充満部分圏 C が ambient copowers で閉じ、非初対象を含むなら、C^op の generated objects 全体でも strong generator を作れない。D・2^S（S は <lambda サイズの座標部分集合）の逆系を使い、任意の正則無限 lambda について、split-mono colimit での因子化失敗を明示した。K_0 の生成対象の選び直しでも回避できない。
- 直接転用も排除：局所可呈示圏の全小余極限で閉じた充満部分圏は、小さい strong generator を持てば既に LP。従って No.1/2 の非 coreflective な A は、N の下で小さい strong generator 自体を持たない。
- Isbell の Set^op の反射像について、同じ cube から、すべての正則 lambda で ambient lambda-directed union 閉性の失敗を確認。
- 前層圏の epireflective subcategory は weakly co-wellpowered となることを確認。¬VP による文献の nearly-presentable な反例を generated 版の反例と取り違えない。
- 今回の新しい前進は、固定始域の **強商** の無界性まで実現し、それと generated strong generator の両立が失敗する理由を特定したこと。N⇒¬P3、V=L⇒¬P3、P3⇒巨大基数のいずれも結論しない。


## 2026-11-17: 反射・union 保存を先に確保する構成の検査

詳細：`reflection_first_stone_dynamics_and_ambient_union_boundary_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。独立査読・形式検証・新規性確認は未実施。No.3 の反例・独立性・一般肯定は未確立。**

- 前回の「全余極限閉部分圏の small strong generator」と「ambient copowers を保った双対化」の排除補題を再点検し、記載された仮定の範囲で維持した。
- 有限支持 M-set の presheaf 圏 S において、Stone 双対像 C(X)=Cont(X,ω) への反射 A↦C(H(A)) を Hom 計算で明示した。その包含は全 filtered colimits を保存する。
- 両成分有限支持の図式圏 S^(0⇉1) で、両成分が Stone 双対かつ p が同型となる部分圏 R_cont の reflector を、Boolean algebra の可算余積・shift・合同関係から構成。包含は λ=ω で union を保存するが、R_cont は Boolean algebra with endomorphism の finitary variety と同値なので LFP。反射単位が epi でなく、reflector が mono を保存しない具体例も与えた。
- 連続な自己写像では一点の orbit の閉包が不変になり、Stone 空間としてその濃度は 2^(2^aleph_0) 以下。旧順序数機構による無界性が失われる理由を明示した。
- 第0成分を Stone 双対、第1成分を任意の冪にした R_mix は N の下で反射を持つ。しかし全 λ で座標 cube により ambient union 閉性が失敗。さらに「Stone 頂点と集合としての辺」の圏の双対で、generated objects は平行辺の fold を検出できないと示した。これは別の生成族への取り替えも排除する。
- R_mix で一方の双対構造射を全単射にして不連続 dynamics を残した R_disc は、可算積を持たない。一点固定系の可算余積があれば、有限点を固定し ω 以上で後続操作を行う任意に大きい [0,κ] に連続全射してしまう、という ZFC の直接証明。従っていかなる完備圏の full reflective subcategory にもなれない。
- 一般補題：前層圏上の自己関手 T が、ある κ で **任意の ambient な** κ-directed mono-colimit を保存すれば、ある μ で accessible。小部分前層による元の支持に加え、等式の検出も使う直接証明を記録した。T の mono 保存は仮定していないが、単なる boundedness より強い仮定である。
- 帰結：P3 の反例では、局所対象同士の mono-colimit は E がある λ で保存する一方、T=EL は非局所な入力も含む mono-colimit をどの κ でもすべて保存できない。この二つを混同しない。前者から後者を導く橋は未証明。
- 今回の新証明は No.2 の A_sigma の大域的 coreflectivity に依存しない。N は混合候補の Isbell 全忠実表示に使用し、位相的障害・一般関手補題は ZFC で示した。


## 2026-11-17: 肯定側 — 定義可能性と小さい局所部分対象による十分条件

詳細：`positive_definability_and_local_submodels_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。既存の文献定理を用いた条件付き肯定結果と直接証明。独立査読・形式検証・新規性確認は未実施。一般の P3 の ZFC 肯定・反例・独立性は未確立。**

- 核心を small-local-subobject factorization にした。強商 H→B が小さい局所対象 X と mono X→B を経由すれば、この mono は strong 性により同型。従って X のサイズ上界が B の上界になる。
- presheaf 表示における局所対象のクラスが集合パラメータ付き **Lévy Σ1** なら、BCMR (2015) Theorem 5.1(a) による小型化から **ZFC で肯定**。K の accessibility を仮定せずに (Q) を得る。
- 同じクラスが **Σ2** なら、固定データを上回る **一つの supercompact（超コンパクト）基数**で肯定。BCMR Theorem 5.2(a) を使用。strongly compact（強コンパクト）とは区別する。高い定義の複雑さは Corollary 6.6(a) の C(n)-extendible 版で同様に扱える。
- **元の P3 の仮定から Σ1/Σ2 定義可能性を導いたわけではない。** よって一般の P3 について VP を強コンパクトや超コンパクトの真クラスへ弱めた、という結論ではない。
- 別の ZFC 肯定範囲：K が集合個の L_(chi,chi) 公理の全モデル・全準同型の圏として表せれば、small-submodel/Skolem 構成で strong quotient smallness を得る。式の fragment、mu^(<chi)=mu、chi 段の閉包を明示。公理の真クラスを集合と扱わず、ordinary epi 全体の co-wellpoweredness とは区別した。
- reflector の全 mono 保存という既存条件を限定した：ある kappa に対して、**局所対象を終域に持つ ambient kappa-pure monos**を L が mono に送れば ZFC で肯定。小さい pure subpresheaf A を作り、strong 性で B≅LA とする。A の候補は集合個なので反射像も集合個である。
- 一般の場合に残るのは、小部分構造の local 性、またはその反射 LA→B の mono 性。元の local-union 閉性からこの保証を導く橋は今回未証明。
- N、No.1/2 の非 coreflectivity、独立性は今回の肯定定理の入力にしていない。


## 2026-11-17: RP の監査・同値性と fixed-domain split-colimit への還元

詳細：`rp_equivalence_split_colimits_and_compactness_gap_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。独立査読・形式検証・新規性確認なし。一般の P3 の肯定・反例・独立性は未確立。**

- 前回の探索計画を修正：LP な reflective subcategory では、十分大きいある κ で pure-subobject 閉性、従って RP_κ が必ず成立する。右随伴 E の accessibility、集合個の反射単位による orthogonality 表示、purity の lifting から直接証明。従って P3 の前提下では LP⇔∃κ RP_κ。全 κ で RP が失敗する LP の反例を探す必要はない。
- 強商ごとに小さい A⊂EB を選ぶ条件 W を定式化。purity 自体は条件から外せるが、一様なサイズ上界を要求した W は Q、従って LP と同値。見かけ上の条件の弱化を、一般肯定の新証明と取り違えない。
- 固定 κ の失敗は実際に起こる。κ-ary operation の代数を二 sort の hypergraph presheaves に充満反射表示し、二元の定数零 operation の中で <κ-support の records だけを残した A を構成。A→EB は κ-pure だが、反射後は t(1,1,...) と0が同一視され nonmonic。圏は LP で、κ^+ では pure 閉性と RP が戻る。κ に応じて圏が変わる対照例。
- κ>|Mor D| なら、pure inclusion A⊂EB を A∪C（C は <κ サイズの部分前層）の directed union に表示でき、各 A→A∪C は split mono。反射後も始域 LA からの射は split だが、段階間の射は mono と判定できない。
- K 内の条件 CS_κ：fixed-domain split monos の κ-directed colimit が mono のまま、を切り出した。P3 の前提下で LP⇔∃κ CS_κ⇔∃κ RP_κ。元の union 保存は段階間の射が mono の場合なので、そのまま CS に適用できない。
- almost strong compactness 型の filter extension で、始域 X を固定し κ がその E-carrier に対して十分大きければ、fixed-domain split-extension colimit が実際に split mono になることを直接証明。ultraproduct の K 所属性は不要。得たのは ∀X∃κ_X であり、P3 に必要な一様条件 ∃κ∀X への移行は未証明。
- 非 LP と仮定した場合、同じ固定 H の強商から、任意の κ について κ-pure unit A→ELA と nonmonic strong epi LA→B が必ず生じることを示した。反例そのものの構成ではなく、必要な反例形の精密化。
- 今回も ZFC⇒P3、WVP⇒P3、ASC_infinity⇒P3 のいずれも結論していない。


## 2026-11-17: 生成対象からの二射の分離と、反射で新たに生じる等式

詳細：`generator_separation_reduced_powers_and_new_equalities_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。主担当による直接証明・再点検。独立査読・形式検証・新規性確認なし。一般の P3 の肯定・反例・独立性は未確立。**

- pure inclusion の fixed-domain split-extension 表示と FC(kappa,theta) による始域固定の整合化を再点検し、記載された仮定の範囲で維持した。purity が与えるのは交わり上の一致であり、それが貼り合わせに十分。
- 小さい局所対象 D への任意の h:X→D を split-extension colimit へ延長するコンパクト性の補題を得た。しかし、生成対象からの二射を一様に小さい局所対象で分離できるという追加仮定は、Grp の finitely presentable strong generator Z でも偽。任意に大きい finitary alternating simple groups が具体的な障害となる。
- retractions を元の X に戻さず、tail filter による categorical reduced power Q_F(X) に送れば、ZFC で colim Y_i→Q_F(X)、合成 s が diagonal に等しい cocone を作れる。これは古典的な pure/reduced-power の機構であり、Hébert (2004) Theorem 2.4(a) の証明との対応を確認した。
- 特殊な pure inclusion A⊂EB ではこの構成を反射前に行い、EB→Red_F(A)、反射後には B→L Red_F(A) と gamma r=L(delta_A) を得た。L(delta_A) の monicity は r の monicityへの十分条件であり、同値とはしない。
- generatedness を実際に使える箇所を得た。product restriction の kernel relations R_S の directed mono-union R_F は、元の union 保存により局所対象。Gからの二射が ambient reduced power で等しいなら、Gのgeneratednessにより一つのR_Sで既に等しい。
- 残るのは R_F を K 内で coequalize した際の新しい等式。必要なのは relation 全体のeffectivityでなく、constant families 上で kernel pair が拡大しないこと。
- この拡大が fixed rank で実在する明示例を構成。任意の正則無限 kappa に対し、二sortのunary presheaves内で (∀xi<kappa, p_xi(v)=a(v))⇒a(v)=b(v) を課すfull epireflective K_kappa を取る。全directed unionsを保存し、二対象からなるfinitely generated strong generatorを持ち、locally kappa^+-presentable。
- K_kappa はambient subobjectsに閉じるのでRPは全rankで成立する。しかしkappa-complete tail filterのreduced powerの反射が二つのconstant elementsを潰し、CS_kappaは失敗する。したがって ∃rank RP と ∃rank CS の同値を、同じrankでの同値に読み替えてはならない。圏とsignatureはkappaに応じて変わり、No.3の反例ではない。
- 一般肯定に向けて未解決なのは、固定Hの強商から得られる特殊なr:LA→Bについて、反射が追加する等式の発生を一様に小さいデータへ局所化できるか。今回も ZFC⇒P3、ASC_infinity⇒P3、WVP⇒P3 を結論していない。


## 2026-11-17: 固定始域の強商 — 反射像による等式局所化と個別停止

詳細：`fixed_source_image_iteration_and_relative_equation_witnesses_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。主担当の直接証明・再点検のみ。独立査読・形式検証・新規性確認なし。P3一般の肯定・否定・独立性は未確立。**

- 特殊な r_A:LA→B に集中し、c_B(A)=Im_P(E r_A) を構成。A⊂c_B(A)、|c_B(A)|≤|ELA|。包含を反射した LA→L c_B(A) が kerpair(r_A) の coequalizer であり、その段階の全等式を正確に一段階で検出すると示した。一般の reduced-power diagonal の monicity は要求しない。
- κ>|Mor D| と i:A⊂EB のκ-purityの下で、新しく加わる元 c_B(A)\A がκ未満なら A→c_B(A) がsplit。反射後はregular epiでもあるため同型となり、r_Aはmono。固定Hの強商を因子化しているなら同型。従ってnonmonic failureには一段階で少なくともκ個の新元が必要。A自身がκ未満という仮定は不要。
- c_Bの超限反復は、各固定EBの中でのambient subpresheavesの増大なので、μ_B=max(aleph_0,|EB|) に対しμ_B^+より前に停止。fixed pointは局所対象で、停止値はAを含む最小のK-subobject。強商H→Bの像を含んで開始すれば停止値はEB全体。
- A_0=Im_P(Eq)から開始した反射列は、初期射H→LA_0を含めてcanonical regular-epi decompositionとなる。**初期ノートで未証明とした「各strong epiごとの集合長での停止」は、このpresheaf反射表示の設定では今回証明できた。** 残るのは、Hからの全強商に共通する停止順序数である。
- 一段階のサイズ上界Φ(μ)を、小さいpresheavesの集合の反射値から定義。反復長がHごとに一様なら、基数の超限再帰で(Q)が従う。一方、個別停止のμ_B^+はBに依存するので、これを(Q)と混同しない。
- 元のunion保存から最終閉包cl_Bはλ-directed unionsを保存。ただし一段階c_Bの保存は未証明。最終閉包の連続性と一段階のサイズ上界だけでは一様反復長が出ないことを、順序論的対照作用素で確認。この対照例は反射圏の反例ではない。
- Catの[1]→BC_nを、simplicial nerveの反射で再計算。初期像の反射はBℕ、次の像でN(BC_n)全体に到達し、二段階のregular decompositionを再現。
- 今回の新証明にN・巨大基数・No.1/2の反例を用いない。ZFC⇒P3、ASC_infinity⇒P3、WVP⇒P3はいずれも未証明。


## 2026-11-17: 一様停止の条件付き証明と、任意の集合順序数まで続く実例

詳細：`uniform_stopping_quasi_small_tests_and_transfinite_constants_2026-11-17.md`。

**状態：PROOF_RECONSTRUCTED。独立査読・形式検証・新規性確認は未実施。一般のP3は未解決。**

- 直前の反射像c_Bによる各標的ごとの停止を再点検し、維持した。一様化に必要な追加条件を別に扱った。
- 新しい条件付き肯定：presheaf表示でK=(S∪Q)^⊥、Sが射の集合、Qがambient epiの任意クラスなら、元のP3の仮定の下でKはZFCでLP。A=S^⊥はLPで、L_0(Q)はAのregular epis。従ってKはA-subobjectsで閉じ、K-strong episをA-strong episへ移せる。強商の集合性と標準locally-generated theoremを適用する。
- この追加条件では停止上界も実際に得る。Aがlocally μ-presentableなら、Aのregular decompositionをKへの反射で移し、canonical towerとの比較から、Kの全strong episはμ以下で停止する。Qが真クラスであってもよい。既存のquasi-small orthogonalityと分解理論の組合せとして扱い、新規性は主張しない。
- 反射像の反復をgeneratednessの基数だけで抑える案に、実際の圏の対照例を得た。任意の非零集合順序数Γについて、bと部分定数c_α（α<Γ）を持ち、[全β<αでc_β=bかつ定義済み]⇒c_αが定義済み、という条件を課すK_Γを構成。
- K_Γは小さい右直交クラスなのでreflectiveかつLP。包含は全directed mono-unionsを保存し、反射されたrepresentablesはfinitely generatedなstrong generatorの集合となる。固定段階内の超限帰納法でunion保存を証明した。
- H_Γは初対象でfinitely presentable。H_Γ→終対象T_Γはstrong epiで、canonical regular towerは正確にΓ段必要。後続では次の部分定数の自由な値を追加し、極限では前の値が全てbに潰れた後に次の定数を追加する。
- T_Γの部分前層A_S上でc_T(A_S)=A_(S∪{min(Γ\S)})を計算。以前の純粋に順序論的な対照作用素を、実際の反射・自然性・local union保存を持つ圏で実現した。最終閉包は定数で連続だが、一段階c_Tは極限のunionを保存しない。
- **Γとともに圏・signature・生成族は変わる。固定した一圏で全順序数の長さが必要とは示しておらず、P3の反例ではない。** 生成性の基数λ=ωや始域だけの小ささから短い共通上界を出す近道を排除した結果。
- 一般の単位クラスをepi–mono分解して、局所対象をepiクラスQとmonoクラスMへの右直交で表示できることを確認。Qをclassのまま残しM側を集合個のテストで代替できれば今回の定理が使えるが、そのsmallnessは元のgeneratednessから未証明。
- 今回もZFC⇒P3、WVP⇒P3、ASC_infinity⇒P3、N⇒¬P3は結論していない。


## 2026-11-17: 反例探索 — ordinal-rank 候補と、原著の boundedness 還元との未解消の衝突

詳細：`ordinal_rank_candidate_and_boundedness_conflict_2026-11-17.md`。

**状態：CANDIDATE_WITH_UNRESOLVED_SOURCE_CONFLICT。No.3 の解決・ZFC 否定・独立性の確定とは扱わない。** *（2026-11-20 追記：AI による検証で候補は字義どおりの No.3 の ZFC 反例と判定され、衝突の原因は原著 p.296 の稠密性のステップにあるとされた。冒頭の「Current status — 2026-11-20」を参照。）*

- 任意長の K_Gamma を別々に作る方法から、一つの圏の対象に ordinal rank を持たせる方法を試した。対象は二点を区別した集合と順序数、または infinity-rank の一点付き集合。rank が上がる射は二つの区別された点を同一視する。
- 一つの rank-0 三元対象 G の Hom が忘却関手 U と自然同型になる。U が faithful/conservative、mono が underlying injection と一致する、従って mono 図式は rank 一定になる、という計算を得た。
- 全小余積・余等化・積・等化子の明示式、directed mono-colimit の計算、G の有限生成性を証明候補として記載。固定 H から二元対象 X_alpha への strong quotients の真クラス、および長さ alpha の regular tower も直接検査した。
- 有限 rank・有限 carrier の補助検算では、余積/余等化の普遍性、表現可能性、mono 検査、strong epi の lifting を確認した。ただし無限・真クラスの主張の証明とは区別する。
- **重大な未解消事項：** この候補の計算を採用すると、generated strong generator を持つにもかかわらず小さい dense subcategory が存在しない。これは原著 pp.295–296 の boundedness 還元・VP 下の肯定記述と衝突する。2018 年の Positselski–Rosicky の同じ記述、および著者の2026年3月版正誤表も照合したが、衝突は解消できていない。
- 候補は full reflective presheaf presentation を持たない、という直接議論も記載。従って以前の「その表示を前提にした」個別停止の定理を反証するものとして扱わない。問題は元の仮定から表示を導く部分、または今回の候補の普遍性・生成性の証明にある。
- N や V=L は使っていない。もし候補が intended definitions の下で正しければ literal formulation の ZFC 反例になるが、その結論を確定していない。既存の VP 肯定記述を根拠なく撤回したり、別の問題へ定義を黙って変更したりしない。
- 次の優先課題は、新しい候補を積み増すことではなく、この一つの候補の §§3–5（strong generation、generatedness、cocompleteness）と原著の還元を独立に監査し、衝突箇所を特定すること。


## 2026-11-17: 原著の density 還元の具体的な監査

詳細：`original_density_gap_audit_2026-11-17.md`。

**状態：DIRECT_DENSITY_COUNTERCALCULATION / PROOF_RECONSTRUCTED。独立査読・形式検証・著者確認・新規性確認は未実施。**

- 原著の出版社配信previewでDefinition0.6（pp.2–3）、Theorem1.11の証明（p.18）を取得し、本文・画像を照合。原著のstrong generatorの定義にdensityは含まれない。生成性の通常の意味はPositselski–Rosický(2018)導入とも照合した。
- Theorem1.11自体の誤りではなく、p.296でpresentable版の証明をgenerated版へ移す箇所を特定。canonical diagramはfilteredだがmonoの図式とは限らず、Gからcolimitへの二射を一段階へ因子化するためのpresentabilityをgeneratednessで置き換えられない。
- 候補圏では有限余極限閉包Aを「有限carrier・有限ordinal rankの対象」の小さいfull skeletonとして同定。K=X_(ω+1)について、canonical diagram A↓Kにcofinalな鎖Z_n=(n,{b,c,z})を構成し、colim Z_n=(ω,{b,d,z})を直接計算した。比較射はb,dをともに0、zを1へ送り、**非mono**となる。dを選ぶGからの射はどの段階も経由しない。
- 従って、今回の候補の直接証明に基づけば、p.296のdensity主張には具体的な反例がある。単なる説明不足の指摘だけではない。候補の余完備性・finite generatedness・strong generationは今回の監査では維持されたが、外部独立検証済みとはしない。
- 任意のsmall full subcategoryはordinal ranksが有界で、その先のX_α,X_βのrestricted nervesは同型になるため、候補にsmall dense subcategoryはない。基数の拡大だけではこの問題は修復されない。
- **今後の前提に関する警告：** 元のliteral Problem3からfull reflective presheaf presentationへの移行を、原著コメントだけで無条件に採用しない。過去のその設定内の直接補題は、表示の存在を独立仮定とすれば引き続き別途評価できる。候補はreflective formulationへの反例ではない。
- p.295のVP肯定のコメントも、boundednessを導く箇所に依存しており、候補が正しければ修正が必要。ただしVPやCorollary6.8自体の反駁を主張しない。Proposition1.16・1.22・Corollary6.8の完全な証明本文を今回行ごと監査したわけではない。
- March2026正誤表のp.18訂正は有限余極限閉包のsmallnessに関するもので、今回の因子化問題を解消しない。p.295–296への該当訂正は見つからなかったが、それを新規性の証拠とはしない。
