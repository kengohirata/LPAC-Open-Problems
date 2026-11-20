#!/usr/bin/env python3
"""Exhaustive strict-Hom certificate for one finite 2-truncated witness.

Standard library only. This checks finite data, not global coreflectivity.
Run from the handoff directory:
  python3 checks/verify_quotient_witness.py --output results/quotient_witness.json
"""

import argparse
import itertools
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def validate(x):
    """Check all generator relations whose source/target degrees lie in 0..2."""
    sizes, d, s = x["sizes"], x["faces"], x["degeneracies"]
    require(len(sizes) == 3 and len(d) == 3 and len(s) == 2, "degree count")
    require(d[0] == [], "no degree-zero faces")
    count = 0
    for n in (1, 2):
        require(len(d[n]) == n + 1, "face count")
        for table in d[n]:
            require(len(table) == sizes[n], "face domain")
            require(all(0 <= y < sizes[n - 1] for y in table), "face codomain")
    for n in (0, 1):
        require(len(s[n]) == n + 1, "degeneracy count")
        for table in s[n]:
            require(len(table) == sizes[n], "degeneracy domain")
            require(all(0 <= y < sizes[n + 1] for y in table), "degeneracy codomain")
    # d_i d_j = d_{j-1} d_i for i < j (source degree 2).
    for i in range(3):
        for j in range(i + 1, 3):
            for a in range(sizes[2]):
                require(d[1][i][d[2][j][a]] == d[1][j - 1][d[2][i][a]], "dd")
                count += 1
    # s_0 s_0 = s_1 s_0 (source degree 0).
    for a in range(sizes[0]):
        require(s[1][0][s[0][0][a]] == s[1][1][s[0][0][a]], "ss")
        count += 1
    # d_i s_j, source degree 0 or 1.
    for n in (0, 1):
        for j in range(n + 1):
            for i in range(n + 2):
                for a in range(sizes[n]):
                    lhs = d[n + 1][i][s[n][j][a]]
                    if i < j:
                        rhs = s[n - 1][j - 1][d[n][i][a]]
                    elif i in (j, j + 1):
                        rhs = a
                    else:
                        rhs = s[n - 1][j][d[n][i - 1][a]]
                    require(lhs == rhs, "ds")
                    count += 1
    return count


def is_map(x, y, g):
    if len(g) != 3:
        return False
    for n in range(3):
        if len(g[n]) != x["sizes"][n] or any(a < 0 or a >= y["sizes"][n] for a in g[n]):
            return False
    for n in (1, 2):
        for i in range(n + 1):
            for a in range(x["sizes"][n]):
                if g[n - 1][x["faces"][n][i][a]] != y["faces"][n][i][g[n][a]]:
                    return False
    for n in (0, 1):
        for i in range(n + 1):
            for a in range(x["sizes"][n]):
                if g[n + 1][x["degeneracies"][n][i][a]] != y["degeneracies"][n][i][g[n][a]]:
                    return False
    return True


def all_maps(x, y):
    """Enumerate every tuple of degree functions, without witness-specific pruning."""
    degree_functions = [
        tuple(itertools.product(range(y["sizes"][n]), repeat=x["sizes"][n]))
        for n in range(3)
    ]
    maps = [g for g in itertools.product(*degree_functions) if is_map(x, y, g)]
    candidates = 1
    for functions in degree_functions:
        candidates *= len(functions)
    return maps, candidates


def compose(f, g):
    return tuple(tuple(f[n][a] for a in g[n]) for n in range(3))


def identity(x):
    return tuple(tuple(range(n)) for n in x["sizes"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    u = {
        "name": "U = tr_2 B(C_2)",
        "sizes": [1, 2, 4],
        "labels": [["v"], ["e", "a"], ["z", "s0a", "s1a", "t"]],
        "faces": [[], [[0, 0], [0, 0]], [[0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1]]],
        "degeneracies": [[[0]], [[0, 1], [0, 2]]],
    }
    v = {
        "name": "V = tr_2 (Delta[2]/boundary Delta[2])",
        "sizes": [1, 1, 2],
        "labels": [["v"], ["e"], ["z", "u"]],
        "faces": [[], [[0], [0]], [[0, 0], [0, 0], [0, 0]]],
        "degeneracies": [[[0]], [[0], [0]]],
    }
    f = ((0,), (0, 0), (0, 0, 0, 1))
    objects = {"U": u, "V": v}
    identity_checks = {name: validate(x) for name, x in objects.items()}
    require(is_map(u, v, f), "f is a morphism")
    require(all(set(f[n]) == set(range(v["sizes"][n])) for n in range(3)), "f degreewise surjective")
    hom, candidates = {}, {}
    for xn, x in objects.items():
        for yn, y in objects.items():
            key = xn + "->" + yn
            hom[key], candidates[key] = all_maps(x, y)
    require([len(hom[k]) for k in ("U->U", "U->V", "V->U", "V->V")] == [2, 2, 1, 2], "Hom counts")
    fibres = {}
    for name in objects:
        fibres[name] = [
            {"target_map": h, "lifts": [g for g in hom[name + "->U"] if compose(f, g) == h]}
            for h in hom[name + "->V"]
        ]
    require(all(len(row["lifts"]) == 1 for row in fibres["U"]), "U coorthogonal to f")
    id_v_row = next(row for row in fibres["V"] if row["target_map"] == identity(v))
    require(id_v_row["lifts"] == [], "id_V has no lift")
    # Check closure under composition for all eight typed triples, and identities.
    composition_checks = 0
    for an, a in objects.items():
        require(identity(a) in hom[an + "->" + an], "identity in Hom")
        for bn in objects:
            for cn in objects:
                for g in hom[an + "->" + bn]:
                    for h in hom[bn + "->" + cn]:
                        require(compose(h, g) in hom[an + "->" + cn], "composition closure")
                        composition_checks += 1
    certificate = {
        "scope": "One finite 2-truncated example; exhaustive strict maps. No minimality or non-coreflectivity claim.",
        "objects": objects,
        "test_and_quotient_map": f,
        "simplicial_identity_checks": identity_checks,
        "candidate_function_tuples": candidates,
        "hom_counts": {key: len(value) for key, value in hom.items()},
        "hom_maps": hom,
        "lift_fibres": fibres,
        "composition_checks": composition_checks,
        "conclusions": {"degreewise_surjective": True, "U_coorthogonal": True, "V_coorthogonal": False, "id_V_has_no_lift": True},
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"hom_counts": certificate["hom_counts"], "candidate_function_tuples": candidates,
                      "simplicial_identity_checks": identity_checks, "composition_checks": composition_checks,
                      "lift_counts": {key: [len(row["lifts"]) for row in rows] for key, rows in fibres.items()}}, indent=2))


if __name__ == "__main__":
    main()
