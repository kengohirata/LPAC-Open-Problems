# Codex research handoff — sSet small-coorthogonality and ZFC independence

**Prepared:** 2026-11-15  
**Working language:** 日本語（数式・コードは英語可）  
**Deliverable type:** computational research infrastructure + theorem auditing + mathematical evidence  
**Project:** LFP Open Problems / Adámek–Rosický, *Locally Presentable and Accessible Categories*, Open Problem 1

> **最重要:** 研究の最終目標は「小さい coorthogonality class の coreflectivity が ZFC から独立か」を証明すること。**今のところ独立性の証明も、反例もない。** Codex の最初の仕事は、有限 sSet の正確な探索器を作り、過去の議論の補題を再検証することである。有限探索は独立性の証明にはならない。

---

## 0. Codex に最初に依頼すること（実行可能な短期ゴール）

1. この文書と `CLAIMS_LEDGER.md`, `AGENTS.md` を読む。`prior_notes/` は**未査読の研究ノート**として読む。
2. **Phase 0:** 以下の補題について、文献または独立した証明で監査する。反例があれば最小限の具体例とともに訂正する。
   - `sSet` で頂点写像が全単射でないテスト射の coorthogonality は空 simplicial set のみ。
   - 非自明な場合、テスト射の集合を一本の積射にまとめられる。
   - `tr_2 ⊣ cosk_2` による strict Hom の移送（方向を必ず確認）。
   - 「各次数で有限な始域のテスト射なら ZFC で coreflective」「線形なテスト射なら locally ℵ₁-presentable」「固定次数のサイズ障害」の**未査読の証明**。
3. **Phase 1:** `sset_explorer` を Python で実装する。**2-truncated simplicial sets** に対する構造検査、全 simplicial maps の列挙、`X ⟂ f` の全単射判定、明示的 witness 出力、同型による重複排除が MVP。
4. **Phase 2:** quotient / strong-epi–mono factorization / kernel pair / `X∈A_f` だが quotient `Y∉A_f` の探索とテスト。既知の小例を再現する。
5. **Phase 3:** 固定した `(f,B)` に対し bounded な `(A_f ↓ B)` を調べ、候補 coreflection のサイズが探索上限とともにどう変化するか記録する。ただし有限探索で「coreflection が存在しない」と断定しない。
6. 各 phase で `README.md` に動かし方、`PROGRESS.md` に発見（確立／実験／予想の区別）、`tests/` に回帰テストを残す。

**成果物の最低基準:** `pytest` で通る有限 sSet の判定器、最低3種類の nontrivial な既知例、機械可読 JSON の最小 witness、探索制約と現在の数学的結論を記したレポート。

---

## 1. 研究の出発点と問題の正確な向き

Adámek–Rosický, *Locally Presentable and Accessible Categories* (1994), pp. 295–298 の **Open Problem 1** に由来する。

- `K` を locally presentable category とする。
- `S = { f_i: U_i → V_i | i∈I }` を **集合個** の `K` の射とする。
- その **coorthogonality class** を

  `A_S = { X∈K | K(X, f_i): K(X,U_i) → K(X,V_i) がすべて全単射 }`

  と定める。
- `P_K`: 任意の `S` について、充満部分圏 `A_S ↪ K` が **coreflective**。
- `P`: 任意の locally presentable `K` について `P_K` が成立。

`K^op` における small-orthogonality class の **reflectivity** を、`K` の中で書き直したもの。**ordinary Hom-set の全単射**が対象であり、ホモトピー類、mapping space、弱同値、injectivity（全射性のみ）とは異なる。

`A_S` が coreflective とは、包含 `J:A_S→K` に右随伴 `R:K→A_S` があり、任意の `B∈K` に普遍射 `ε_B:R(B)→B` が存在すること。すなわち、任意の `A∈A_S` に対し

`K(A,R(B)) → K(A,B),  g ↦ ε_B∘g`

が全単射である。

**既知の肯定側:** Vopěnka's principle (VP) の下では `P` が真（原著で言及）。VP の相対的無矛盾性を仮定すると `ZFC ⊬ ¬P`。独立性に残るのは `Con(ZFC+¬P)`（例えば `V=L` の下で反例を構成）である。**`(M)` や `V=L` から反例が既に得られているわけではない。**

**絶対に混同しない:** `A_S` が accessible でない ≠ `A_S` が coreflective でない。過去にはリスト彩色を用い、coreflective だが accessibility が大きな基数と関係する例を検討した。これは `¬P` の反例ではない。

### なぜ sSet か

`sSet = Set^{Δ^op}` は locally finitely presentable。`Cat`, `Grp`, `Ab` の複雑な例を nerve 等で移せる可能性があり、さらに genuine な高次 simplex を持つ。

過去に Quiv / graph, 離散力学系 (`N`-actions), `Ab`, `Grp`, `Ban_1`, `Cat` 周辺で候補を探したが、**`P` の反例は未発見**。これらが一般に全て ZFC で成立すると証明したわけではない。過去の「除外定理」も `prior_notes/` を無批判に信用せず監査すること。

---

## 2. sSet の基本構造と探索対象

`sSet = Fun(Δ^op, Set)`。`X` の `n` 次の単体集合を `X_n`、face/degeneracy を

- `d_i: X_n → X_{n-1}` (`0≤i≤n`),
- `s_i: X_n → X_{n+1}` (`0≤i≤n`)

とする。いずれも simplicial identities を満たす。

**検査する性質**（一本のテスト射 `f:U→V` で代表）:

`X ⟂ f  ⇔  post_f: Hom_sSet(X,U) → Hom_sSet(X,V)` が bijection。

有限 2-truncated objects `U,V,X` を使う場合のテストは

`X ⟂₂ f ⇔ Hom_{sSet_{≤2}}(X,U) → Hom_{sSet_{≤2}}(X,V)` が bijection。

これを genuine sSet の問題へ厳密に移すには `cosk₂` を使う：

`Hom_sSet(Z, cosk₂ U) ≅ Hom_{sSet_{≤2}}(tr₂ Z,U)`。

したがって `f=cosk₂(u)` に対する `Z ⟂ f` は `tr₂ Z ⟂₂ u` と同値。ただし **一般の sSet のテスト射を 2 次元に還元したわけではない**。

### 実装するデータ型（MVP）

`TruncatedSSet(max_degree=2)`:

- 有限集合 `X0, X1, X2`（それぞれ ID は安定した整数または文字列）。
- `d0,d1: X1→X0`、`s0:X0→X1`。
- `d0,d1,d2:X2→X1`、`s0,s1:X1→X2`。
- すべての次数 ≤2 で成立すべき simplicial identities を厳密に検査する。
- `SimplicialMap` は `g0:X0→Y0`, `g1:X1→Y1`, `g2:X2→Y2` の組で face と degeneracy のすべてに可換。

**注意:** 2-truncated simplicial set と、「2個以下の nondegenerate simplex しか持たない full simplicial set」、`2-skeletal`、`2-coskeletal` は別物。ここを名称・実装ともに区別する。

### 探索アルゴリズム

1. 小さい objects を列挙する（まず各次数の個数に低い上限、1頂点優先）。identity/degeneracy を含む構造を生成し、simplicial identities で検証。
2. 対象間の全射 `Hom(X,Y)` を、degree 0→1→2 と順に constraint propagation しながら列挙。必要なら SAT/SMT (`z3`) を使う。
3. 有効な `f:U→V` ごとに、`h:X→V` の各々について `Lift_f(h)={g:X→U | f∘g=h}` を正確に数える。
4. `X ⟂₂ f` は全 `h` で `|Lift_f(h)|=1`。全 Hom を materialize せず SAT `0,1,≥2` 判定でもよいが、**証人の実射を保存すること**。
5. 同型による重複排除を行い、候補を simplex 数・同型類・lexicographic encoding で整列する。
6. 対象サイズ・射サイズ・時間・メモリの探索予算と seed をログに記録。

### Witness の形

- **existence failure**: `h:X→V` で `Lift_f(h)=∅`。
- **uniqueness failure**: `h:X→V` と相異なる `g1,g2:X→U` で `f g1=f g2=h`。
- **quotient failure**: `f`, `q:X↠Y`, `X⟂f`, `Y⊥̸f`, および `Y` での失敗 witness。
- **finite bounded coreflection obstruction**: 与えられた **有限探索範囲内で** universal map の候補が存在しない。これは `¬P` ではない。

JSON 出力には objects/maps の完全なデータ、Hom の検査結果、探索境界、最小性の基準を含める。

---

## 3. まず再現する最小の事例（期待値付き）

以下は単に説明例ではなく、**回帰テスト**にする。`tr₂` で計算してよい。

1. **同型テスト:** 任意の `X` と `f=id_U` は `X⟂₂ f`。
2. **頂点が全単射でない:** `f: Δ[0] ⊔ Δ[0] → Δ[0]`（折り畳み）。`X=Δ[0]` は不合格。`X=∅` は合格。
3. **非自明で非分裂な群 nerve の例:** `C4→C2`（剰余写像）による `f:B(C4)→B(C2)` の次数 ≤2 への制限。両端の頂点は一つ、`f` は非 mono、群準同型として section はない。
   - `X=Δ[0]`: 合格。
   - `X=B(C3)` の 2-truncation: 合格（両方への準同型は自明なもののみ）。
   - `X=B(C2)` の 2-truncation: **不合格**（`C2→C2` の非自明な射は `C4→C2` に沿って持ち上がらない）。
   - `X=B(C4)` の 2-truncation: 不合格（持ち上げが非一意）。
4. **可算／有限性の境界:** finite `2-truncated` objects と finite *full* simplicial sets の違いを検出するテストを用意。

有限群 nerve は `B(G)_n=G^n`、face maps は積、degeneracy maps は単位元挿入として組み立てると、独立な oracle になる。

`B(C4)→B(C2)` は本当の `P_sSet` 反例ではない。有限の lifting failure と non-coreflectivity を混同しないこと。

---

## 4. 次の計算段階：商・因子分解・普遍対象

### 4.1 Quotients

各次数の同値関係 `~0,~1,~2` が全ての `d_i,s_i` と整合する場合、成分ごとの商 `q:X↠Y` を構成する。`q` が各次数で全射なら `sSet_{≤2}` で regular epi。

探索すべき witness:

`X⟂₂ f` だが `Y⊥̸₂ f` となる `(f,X,q:Y)`。

これが起きても、**A_f が coreflective ではないとは言えない**。補題の誤りを発見したり、coreflector が mono でない例を分析する用途。

### 4.2 Bounded slice/comma search

`A_f = {X | X⟂₂ f}` の有限列挙範囲を限定し、`A_f ↓ B` の対象 `a:X→B` と射 `t:X→Y` (`b∘t=a`) を列挙する。

「現在の探索領域における終対象の候補」を探し、探索上限を引き上げて振る舞いを観察する。**候補がないことは有限領域内の事実にすぎず、無限対象の coreflection がないという証明にはならない**。

理想的なパターンは、固定 `(f,B)` に対する順序数へ拡張できそうな無限族が見つかること。しかし有限データの外挿は必ず予想として記録。

### 4.3 Fixed-degree size obstruction（未査読の方針）

過去のノートでは、`A⊆sSet` が小余極限閉で `B` に coreflection がなければ、**ある固定次数 `n≥1` で** `A` 内の因子分解先の `n`-simplex 数が任意に大きくなる、という必要条件を導いた。`prior_notes/sset_higher_dimensional_followup.md`, §7 を参照。

この証明は**独立監査が必要**。仮に正しければ、計算探索の「単に必要な最高次数が上がるだけでは不十分」という優先順位付けの根拠になる。

---

## 5. 数学面での候補と、それぞれの位置付け

### A. Genuine な非線形・高次の sSet（優先）

`f:U→V` を頂点上全単射にし、二つ以上の 2-simplex の整合性、高次の貼り合わせ、非分裂性等を与える。`cosk₂` から始め、必要なら 3-truncated / full sSet に拡張。無限の整合性が必要だとしても、有限の例は構成のヒントであって最終的な証明ではない。

### B. 非分裂な quotient functor の nerves

`Cat→sSet` により `N(F):N(C)→N(D)` をテスト。群の中心拡大（`B(C4)→B(C2)` は最小例）などを使い、持ち上げの存在／一意性を比較する。一般の `P_Cat` / `P_Grp` を解いたとは仮定しない。

### C. Simplicial abelian groups / vector spaces（基準例）

過去ノートでは、体 `k` 上の simplicial vector spaces 由来のテスト射に対して coorthogonality を鎖複体へ移し、ZFC の肯定結果を主張している（`prior_notes/sset_higher_dimensional_followup.md`, §§1–6）。有限 GF(2) 実験 `existing_checks/check_linear_formula.py` がある。**計算は証明ではない。** 証明に誤りがないか監査しつつ、探索器の negative control として扱う。

`Ch_≥0(Ab)` / simplicial abelian groups では、体上の線形分解が使えず候補として残っている。

### D. Infinite colouring / graph minors（背景、優先度低）

先行の探索では、list colouring の非コンパクト性を一本のテスト射へ符号化しても、それが **ZFC で coreflective** になり得ることが判明した。accessibility と coreflectivity は異なる。Suslin-tree / infinite-Hadwiger の反例の存在も `P` と両立し得る。直接的な reduction がない限り、有限探索の初期段階では追いかけすぎない。

---

## 6. 数学的な安全装置・証明に求める品質

**以下を守ること。**

- 「`X⟂f` が有限例で成り立つ」と「`A_f` が coreflective」は別問題。
- 「`A_f` が quotient で閉じない」と「非 coreflective」も別問題。
- 「`A_f` が nonaccessible」と「非 coreflective」も別問題。
- 普遍射の存在／不在は、**全ての `A∈A_f` と全ての射 `A→B`** に量化する。有限 cutoff で結論しない。
- `small` はテスト射の集合性。テスト対象 `U,V` が有限という意味ではない。
- strict coorthogonality と homotopy coorthogonality（mapping spaces の弱同値）は混同しない。
- `monomorphism`, `epi`, `quotient`, `split epi` はどの圏（`sSet`, `sSet_≤2`, `Cat` など）での概念か明示する。
- 過去の研究ノートは **assistant-generated・未査読**。例や証明に実際の穴があれば積極的に破ることを優先する。特に実験的な検証済みと数学的に証明済みを区別する。
- 「ZFC 独立」という文言には、二つのモデル／相対的無矛盾性の論証が必要。
- 既知結果を引用するときは定理番号、前提、原文の向きを参照し、出典 URL と検証日を記録する。

**Claim の扱い**：`PROVEN_IN_LITERATURE`, `PROVED_AND_REVIEWED`, `DRAFT_PROOF_UNREVIEWED`, `FINITE_VERIFIED`, `CONJECTURE`, `FALSE_COUNTEREXAMPLE` のいずれかを添える。

---

## 7. ソフトウェア設計・納品物

推奨ディレクトリ（変更可）:

```text
sset_explorer/
  pyproject.toml
  README.md
  AGENTS.md
  src/sset_explorer/
    truncated.py         # finite n-truncated simplicial set, identities
    morphisms.py         # finite maps, compositions, Hom enumerator
    constructors.py      # Δ[n], disjoint unions, finite group nerves
    canonical.py         # isomorphism testing, canonical encoding
    quotients.py         # congruences, quotient maps, kernel pairs
    orthogonality.py     # count lifts, classify failure, certificates
    search.py            # bounded search, deterministic runs
    export.py            # JSON and human-readable report
  tests/
    test_simplicial_identities.py
    test_morphisms.py
    test_known_examples.py
    test_orthogonality.py
    test_quotients.py
  results/
    .gitkeep
  PROGRESS.md
```

**実装原則**：

- Python 3.11+、`pytest` を最小依存とし、必要に応じて `z3-solver` を任意依存にする。
- 小さい範囲では全列挙と SAT/SMT の両方を比較し、独立した oracle で一致検査する。
- 探索は再実行可能（seed、version、bounds、タイムアウト記録）。
- 顕著な例は最小化して JSON に保存し、テストで回帰する。
- `SageMath` は独立の検算用に有用。ただし文献上、Sage の simplicial-set morphisms は一般の infinite domain を扱わないため、それだけに依存しない。
- CLI 例（インターフェース案、未実装）:

```bash
python -m sset_explorer sanity-check
python -m sset_explorer hom --x example_x.json --y example_y.json
python -m sset_explorer test-coorth --x X.json --f f.json --witness
python -m sset_explorer search --max-degree 2 --max-vertices 1 --max-edges 5 --max-triangles 8 --seed 20261115
pytest -q
```

CLI の名前は例であって、既に動くコマンドではない。

**Phase 1 の完成条件**：

1. 全ての生成データが simplicial identities を満たす。
2. 既知の小例の strict Hom を、手計算と一致して数えられる。
3. 全射の持ち上げと一意性の区別を explicit witness で出せる。
4. 主要クラスを同型で重複除去でき、結果が順序依存しない。
5. `README` に数学的仕様と limitations が記載されている。

**Phase 2 の完成条件**：

- quotient と maps の合成・普遍性を小例で検証。
- 最小 `X⟂f`, `Y⊥̸f` の quotient witness を一つ再現、または定めた範囲で見つからなかったことを正確な cutoff とともに報告。
- 発見された例が既知の肯定定理に矛盾したら、**まず実装と補題双方を監査**する。

**Phase 3 の完成条件**：

- bounded `A_f ↓ B` の探索結果、候補と非候補の機械検証可能な certificate、size progression の表。
- 証明できていない一般化は明確に未解決と記述。

---

## 8. 関連資料と推奨の読み順

### 原著・標準資料

1. Adámek & Rosický, *Locally Presentable and Accessible Categories*, Open Problems, pp. 295–298:  
   https://www.cambridge.org/core/books/abs/locally-presentable-and-accessible-categories/open-problems/2C96E4B704E77DA99C42BEDAB6482CCD
2. 原著の Chapter 6, Vopěnka's Principle:  
   https://www.cambridge.org/core/books/abs/locally-presentable-and-accessible-categories/vopenkas-principle/9ECDBC20E42B8D9951CC02D19B095A68
3. `tr_n ⊣ cosk_n` の定義・公式（W. D. Gillam, *Simplicial Methods*）:  
   https://math.mit.edu/~hrm/palestine/gillam-simplicial-methods.pdf
4. SageMath finite simplicial sets/morphisms documentation:  
   https://doc.sagemath.org/html/en/reference/topology/sage/topology/simplicial_set_morphism.html
5. SageMath examples:  
   https://doc-gitlab.sagemath.org/html/en/reference/categories/sage/categories/simplicial_sets.html
6. Homotopical 版の関連文献（**strict 版とは異なる**）:  
   https://arxiv.org/abs/2410.21244

### 同梱の過去ノート（すべて assistant-generated; 未査読）

- `prior_notes/sset_coorthogonality_investigation.md`: sSet の基本的な肯定断片、1-coskeletal、compactness、移送補題。
- `prior_notes/sset_higher_dimensional_followup.md`: 線形テスト、Dold–Kan、固定次数の因子分解サイズ障害。
- `prior_notes/quiv_graph_coorthogonality_refinements.md`: Quiv / Graph の探索史と除外候補。
- `prior_notes/ab_grp_coorthogonality_progress.md`: Ab / Grp の還元・中心拡大の議論。
- `prior_notes/dds_quiv_small_coorthogonality.md`: 離散力学系の検討。
- `prior_notes/coloring_minor_independence_analysis.md`: 無限彩色と minor の独立性周辺の議論。
- `existing_checks/check_linear_formula.py`: 有限 GF(2) の線形同値式検算（証明ではない）。

### 今回の作業で特に注意したい、まだ解けていない問題

- ZFC だけで `P_sSet` を証明できるか？
- `V=L` などの下で、固定した `f:U→V` と `B` について、非 coreflective な `A_f` を構成できるか？
- 高次 simplicial data から、任意の基数まで拡張できる fixed-degree size obstruction を作れるか？
- 2-truncated の段階ですでに本質的な障害があるか、それとも genuinely higher-dimensional な構造が必要か？
- 過去の肯定断片に穴がないか？ 穴があれば、反例構成の入口になる可能性がある。

---

## 9. Codex に渡す初回プロンプト（そのまま貼付可）

> `AGENTS.md`, `CODEX_HANDOFF.md`, `CLAIMS_LEDGER.md` を読み、まず Phase 0 と Phase 1 を実施してください。数学的背景は Adámek–Rosický の Problem 1（strict small-coorthogonality class の coreflectivity）であり、最終的には ZFC 独立性を調べたいですが、今回はその結論を推測しないでください。有限 2-truncated simplicial sets の正確な表現、simplicial maps の全列挙、`X ⟂ f` の判定器、witness 出力、既知例を再現する pytest を実装してください。最初に `Δ[0]`、`B(C4)→B(C2)` のテストを通し、実装後は quotient による破綻例を探索してください。未検証の補題は `CLAIMS_LEDGER.md` に status と根拠を記録し、誤りを発見したら数学的な最小反例を報告してください。実行方法と制限も必ず README に記載してください。

---

**This handoff is a research brief, not a completed proof of independence.**
