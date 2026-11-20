# 第21段階：必要条件の強化に向けた reduced power と accessibility の境界

2026-11-17。状態：PROOF_RECONSTRUCTED。新規導出は独立査読・形式検証前。

完全な証明は [No.2 の主ノート](../../../No.2/p1_lower_bound_reduced_powers_accessibility_boundary_2026-11-17.md)。

**今回、P1 の巨大基数下界をさらに強めたとは記録しない。** P1⇒可測基数が真クラスという既存下界を維持し、P1⇒ASC∞ や strong 基数の真クラスは未証明のままとする。

## 1. 超フィルターの追加条件を商で符号化

|Omega|=rho、M=End(Omega)、H=Hom_M(-,Omega)、delta=rho^+ とする。proper filter F on I について、

    L_F=Omega^I/~F,
    f~F g ⇔ {i:f(i)=g(i)}∈F

と定義すると、No.1 の full-power 計算から

    H(L_F)≅{Fを延長するdelta-complete ultrafilters on I}

を得る。χ_Aと定数1の同一視がA∈Fを強制する。

co-small filter on lambdaを使えば、H(L_F)はdelta-complete uniform ultrafiltersを正確に表す。有限cone filter on P_kappa(lambda)ならfine ultrafiltersを正確に表す。全<kappa-cone filterはkappa-completeだが、delta<kappaでは単なるfine性より強い条件を符号化するので区別する。

Usuba, A note on delta-strongly compact cardinals, Theorem 1.2により、ある固定kappa以上の全正則lambdaでuniformなdelta-complete ultrafilterが存在することは、kappaのL_(delta,omega)-compactnessと同値。

## 2. ZFC-coreflectiveだがaccessibilityにcompactnessが必要な明示例

    N_rho={empty}∪{X:H(X)=empty}={}^perp{empty→Omega}

は一本のmonoテストのクラスで、coreflectorはBがnullならB、非空でOmegaへ写ればempty。内部monoは母圏のmonoであり、well-poweredでもある。

しかし次は同値である。

1. N_rhoがaccessible。
2. 任意の非空null actが、ある一様な濃度mu以下の非空null subactを含む。
3. あるkappaがL_(rho^+,omega)-compact。

必要方向の核心：proper kappa-complete filter Fについて、L_Fのサイズ<kappaのsubact YはOmegaへの同変写像を持つ。ただし|M|<kappaとする。各yの代表f_yを取り、全作用等式f_(my)(i)=m(f_y(i))を同時に満たすiをFの完備性から選べるためである。

一方、N_rhoがaccessibleなら、generatorのサイズをmuで抑え、非空null actの中にサイズ≤muのnull像を得る。kappa>max(mu,|M|,rho)としてL_Fに適用すると、H(L_F)=emptyの場合は矛盾する。従ってFはrho^+-complete ultrafilterへ延長される。

逆方向はcone filterのultrafilter延長からHom(-,Omega)の局所・大域compactnessを得る。各非空null actは<kappaのnull subactを含み、それらによるkappa-directed unionで生成される。

全rhoに量化すると

    全N_rhoがaccessible ⇔ ASC∞。

既存のASC∞による肯定定理と合わせれば、presheaf圏の全small coorthogonality classのaccessibilityもASC∞と同値。ただしこれをP1のcoreflectivityと同一視しない。

## 3. 一つの反例構成案を排除

Lをreduced power、Aを有限支持actとして

    Z=(A --(alpha,id), (beta,t)--> L×A)

とする。Z→B_rhoの任意の射は、Lやfilterに依存しない固定対象

    P_rho=(finite-image Omega-valued sequences --id,shift--> 同じact)

を経由する。第0成分はa↦(b_0(t^n a))_(n<omega)、第1成分はLを忘れた同じ列。有限支持により列の像は有限。P_rhoはp=idなので合格。

従ってnullなreduced powerを単に積因子として加えても、No.1型の因子化サイズ障害は生じない。

## 4. 残る必要条件強化のための具体的な還元

rhoに依存する固定の圏・テスト集合・標的を構成し、そのcoreflector Rから一つのkappaを読み取り、全正則lambda≥kappaについて

    Omega^lambda/~co-small → Omega

を抽出する補題が得られれば、P1⇒ASC∞へ進む。今回はこの補題を得ていない。

個別のN_rhoのcoreflectivityはZFCで常に存在するので、その存在だけからaccessibilityやultrafilter extensionを推論するのは誤り。一方、この観察はグローバルなP1⇒ASC∞の非含意を証明しない。P1を別の図式圏へ適用して追加の整合性を強制する可能性は残る。

参照：No.2主ノート§§1–9；Usuba arXiv:2001.02124, Theorems 1.2/1.7；Brooke-Taylor–Rosický arXiv:1506.01986v2, Definition 2.3/Proposition 2.4。新しいP1下界が成立したという記載に変更しない。
