"""Finite checks of the equalizer obstruction in the No.4 negative note.

Only finite transformation-monoid identities are checked. This does NOT
verify Isbell's infinite theorem, the No.1 input, or nonreflectivity.
"""
from itertools import product
import json
from pathlib import Path


def equivariant_operations(n: int, arity: int):
    if n < 1 or arity < 1:
        raise ValueError("n and arity must be positive")
    omega = tuple(range(n))
    tuples = tuple(product(omega, repeat=arity))
    index = {x: i for i, x in enumerate(tuples)}
    monoid = tuple(product(omega, repeat=n))
    transforms = [
        tuple(index[tuple(m[x] for x in t)] for t in tuples)
        for m in monoid
    ]
    answers = []
    for values in product(omega, repeat=len(tuples)):
        if all(
            all(values[mt[i]] == m[values[i]] for i in range(len(tuples)))
            for m, mt in zip(monoid, transforms)
        ):
            answers.append(values)
    return tuples, monoid, answers


def check(n: int) -> dict:
    omega = tuple(range(n))
    _, monoid, unary = equivariant_operations(n, 1)
    pairs, _, binary = equivariant_operations(n, 2)
    projections = [tuple(t[i] for t in pairs) for i in (0, 1)]
    assert unary == [omega]
    assert set(binary) == set(projections)
    equalizer = [f for f in monoid if all(f[a] == f[b] for a, b in pairs)]
    constants = [tuple([a] * n) for a in omega]
    assert set(equalizer) == set(constants)
    for i in (0, 1):
        assert all(projections[i][pairs.index((a, a))] == a for a in omega)
    return {
        "omega_size": n,
        "transformation_monoid_size": len(monoid),
        "equivariant_unary_operations": len(unary),
        "equivariant_binary_operations": len(binary),
        "binary_operations_are_exactly_projections": True,
        "dual_equalizer_is_exactly_constant_functions": True,
        "dual_equalizer_size": len(equalizer),
        "diagonal_and_projection_factorizations_verified": True,
    }


if __name__ == "__main__":
    report = {
        "scope": "Finite algebraic sanity checks only; no infinite theorem verified.",
        "checks": [check(2), check(3)],
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    Path(__file__).with_name("results.json").write_text(text, encoding="utf-8")
    print(text, end="")
