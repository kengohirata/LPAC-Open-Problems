# 小さい商閉性失敗例と、その coreflection

2026-11-15。母圏は \(\mathcal T=\mathbf{Set}^{\Delta_{\le2}^{op}}\)。Hom は strict な自然変換全体である。以下は手計算による証明と、全関数タプルの有限列挙の双方で確認した例。最小性・文献上の新規性は主張しない。

## 1. 対象と射

\(U=\operatorname{tr}_2 B(C_2)\) とし、\(V=\operatorname{tr}_2(\Delta[2]/\partial\Delta[2])\) とする。両方とも頂点は一つ。

| 対象 | 1単体 | 2単体 | 次数ごとのサイズ |
|---|---|---|---|
| \(U\) | \(e,a\) | \(z,s_0a,s_1a,t\) | \((1,2,4)\) |
| \(V\) | \(e\) | \(z,u\) | \((1,1,2)\) |

\(e\) は退化辺、\(z\) は頂点からの完全退化2単体である。1単体の faces はすべて唯一の頂点、頂点の degeneracy は \(e\)。2単体の faces を \((d_0,d_1,d_2)\) の順に書くと
\[
z\mapsto(e,e,e),\quad s_0a\mapsto(a,a,e),\quad
s_1a\mapsto(e,a,a),\quad t\mapsto(a,e,a)
\]
であり、\(V\) では \(z,u\) ともに \((e,e,e)\) に写る。

射 \(f:U\to V\) は辺 \(a\) を \(e\) に、\(t\) を \(u\) に写し、退化2単体を \(z\) に写す。上記の順序で完全な数値データは

```text
U: d0=[0,1,0,1], d1=[0,1,1,0], d2=[0,0,1,1]
   s0=[0,1], s1=[0,2]
V: d0=d1=d2=[0,0], s0=s1=[0]
f: degree 0=[0], degree 1=[0,0], degree 2=[0,0,0,1]
```

となる。\(f\) は次数ごとに全射なので \(\mathcal T\) の regular epimorphism であり、mono ではない。

## 2. Hom の手計算

\(U\to U\) は \(a\) の像によって場合分けできる。\(a\mapsto e\) なら、\(t\) は境界 \((e,e,e)\) の唯一の2単体 \(z\) に写る。\(a\mapsto a\) なら \(t\mapsto t\) が強制される。従って定数射と恒等射の二つである。

\(U\to V\) では辺の像は強制され、\(t\) の像を \(z,u\) から自由に選べる。従って定数射と \(f\) の二つである。

\(V\to U\) では辺は \(e\) に写り、\(u\) は境界 \((e,e,e)\) の2単体に写るため \(z\) しか選べない。従って定数射のみである。\(V\to V\) では \(u\) の像を自由に選べるため、定数射と恒等射が得られる。

| \(X\) | \(|\mathcal T(X,U)|\) | \(|\mathcal T(X,V)|\) | \(\mathcal T(X,f)\) の fibre のサイズ |
|---|---:|---:|---|
| \(U\) | 2 | 2 | 定数射に1、\(f\) に1 |
| \(V\) | 1 | 2 | 定数射に1、\(1_V\) に0 |

よって \(U\in\mathcal A_f={}^\perp f\) だが \(V\notin\mathcal A_f\)。商閉性が失敗する。失敗を示す射は \(1_V\) で、持ち上げが存在しない。

さらに、**\(f:U\to V\) 自身が \(V\) の \(\mathcal A_f\)-coreflection である。** \(U\in\mathcal A_f\) であり、任意の \(Z\in\mathcal A_f\) に対して \(\mathcal T(Z,f)\) が全単射であることは定義そのものだからである。商閉性の失敗から coreflection の不存在を結論してはいけない。

## 3. 再現可能な全列挙

Handoff ディレクトリで次を実行する。

```sh
python3 checks/verify_quotient_witness.py --output results/quotient_witness.json
```

[検算プログラム](../checks/verify_quotient_witness.py)は標準ライブラリのみを使い、次数0–2内の全 simplicial identities、射の自然性、次数ごとの全射性、全 Hom、持ち上げの全 fibre、得られた射の合成閉性を検査する。例に特化した Hom 分類で候補を間引かず、全次数の関数の組を列挙して自然性で選別する。

2026-11-15 の実行結果：

| 検査 | 結果 |
|---|---|
| identities の点ごとの等式検査 | \(U\): 27、\(V\): 15、すべて成立 |
| 候補関数タプル | \(U\to U\): 1024、\(U\to V\): 16、\(V\to U\): 32、\(V\to V\): 4 |
| 自然変換数 | 順に 2、2、1、2 |
| 合成閉性 | 24組すべて成立 |
| fibre のサイズ | \(U\): `[1,1]`、\(V\): `[1,0]` |

[JSON 証明書](../results/quotient_witness.json)には構造表、全射リスト、全 fibre が保存されている。乱数や探索上限は使っていない。これは指定した一例についての全列挙であり、すべての同サイズの対象を探索した結果ではない。

## 4. Full sSet への移送と限界

左随伴 skeleton と右随伴 coskeleton を区別して
\[
F=\operatorname{cosk}_2(f),\qquad
q=\operatorname{sk}_2(f):\operatorname{sk}_2U\twoheadrightarrow\operatorname{sk}_2V
\]
と置く。\(\operatorname{sk}_2\) は左随伴として coequalizer を保存するので \(q\) は regular epi。\(\operatorname{tr}_2\operatorname{sk}_2\cong1\) と \(\operatorname{tr}_2\dashv\operatorname{cosk}_2\) から
\[
\operatorname{sk}_2U\perp F,\qquad \operatorname{sk}_2V\not\perp F
\]
が従う。従って full sSet でも商閉性の失敗になる。

ここで \(F\) 自体を商射と扱ってはいけない。\(\operatorname{cosk}_2\) は一般に epi を保存しない。この例でも \((\operatorname{cosk}_2U)_3\) は8元、\((\operatorname{cosk}_2V)_3\) は16元で、\(F_3\) は全射になれない。前者は nerve \(BC_2\) の3単体、後者は四つの2次元面それぞれへの \(z,u\) の選択で数えられる。

一方、\(\operatorname{cosk}_2U\) は degreewise finite である。[有限始域に関する肯定結果](compactness_and_finite_tests.md)より、\({}^\perp F\) は full sSet で coreflective。従ってこの例は非 coreflectivity や独立性の反例ではない。
