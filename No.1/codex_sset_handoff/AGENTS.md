# Codex project instructions — sSet coorthogonality explorer

Read `CODEX_HANDOFF.md` before implementation, and keep `CLAIMS_LEDGER.md` up to date.

## Mission
Implement and audit a finite simplicial-set explorer motivated by Adámek–Rosický Open Problem 1: whether every small **coorthogonality** class in a locally presentable category is **coreflective**. Ultimate research objective: possible ZFC independence of this statement. **There is no established counterexample or independence proof in this project.**

## First deliverable
Build an executable, tested Python package for finite **2-truncated** simplicial sets with (a) full simplicial identities, (b) all strict simplicial maps, (c) compositional Hom, (d) unique-lift tests for `f:U→V`, and (e) minimal machine-readable counterexample witnesses. Reproduce the examples in §3 of `CODEX_HANDOFF.md` before searching new examples.

## Mathematical discipline
- `X⊥f` means `Hom(X,U)→Hom(X,V)` is a **bijection**, not a weak equivalence, homotopy class bijection, mere surjection or mere injection.
- Do not claim that any finite search proves ZFC independence, non-coreflectivity, or the existence/nonexistence of an infinite coreflection.
- Distinguish `2-truncated`, `2-skeletal`, `2-coskeletal`, and `cosk₂` extension carefully.
- Audit purported theorems in `prior_notes/`. They are AI-generated drafts, not externally reviewed results. Correct rather than defer to them.
- Each new lemma must include assumptions, exact categorical ambient, proof, counterexample tests, confidence/status, and source if known.
- Persist reproducible seeds, size limits, JSON certificates, and pytest regressions.

## Workflow
1. Write a brief implementation plan in `PROGRESS.md`.
2. Implement smallest correct model (no web UI required).
3. Run tests and show exact results; fix failures.
4. Search only within documented limits; minimize any candidate.
5. Update `PROGRESS.md` and the claims ledger with remaining mathematical gaps.
