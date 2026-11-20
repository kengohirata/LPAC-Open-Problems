"""Verify a finite obstruction to an initial-image construction in Arr(Set).

This verifies the displayed finite diagram only, not non-coreflectivity or
independence. Objects (n0, n1, arrow) mean a function [n0] -> [n1].
"""

from itertools import product
import json


def functions(n, m):
    return tuple(product(range(m), repeat=n))


def hom(source, target):
    n0, n1, a = source
    m0, m1, b = target
    return tuple(
        (f, g)
        for f in functions(n0, m0)
        for g in functions(n1, m1)
        if all(b[f[x]] == g[a[x]] for x in range(n0))
    )


def compose(f, g):
    return tuple(tuple(f[i][x] for x in g[i]) for i in range(2))


def vacuous_square_example():
    a = u = (0, 2, ())
    b = (1, 1, (0,))
    v = j = (0, 1, ())
    f = ((), (0, 0))
    s = q = ((), (0, 0))
    inclusion = ((), (0,))
    id_u = ((), (0, 1))
    id_v = ((), (0,))
    assert f in hom(a, b) and s in hom(u, v)
    assert q in hom(a, j) and inclusion in hom(j, b)
    assert compose(inclusion, q) == f
    squares = [
        (upper, lower)
        for upper in hom(a, u)
        for lower in hom(b, v)
        if compose(s, upper) == compose(lower, f)
    ]
    assert not squares  # The all-squares product-pullback is just B.
    assert compose(s, id_u) == compose(id_v, q)
    lifts = [
        lift
        for lift in hom(j, u)
        if compose(lift, q) == id_u and compose(s, lift) == id_v
    ]
    assert not lifts
    certificate = {
        "ambient": "Arr(Set), finite objects; ordinary unique lifting",
        "A": a, "B": b, "f": f, "U": u, "V": v, "s": s,
        "initial_pullback": b, "image_J": j, "image_quotient": q,
        "image_inclusion": inclusion,
        "f_to_s_square_count": len(squares),
        "failure_upper": id_u, "failure_lower": id_v,
        "lift_count": len(lifts),
        "Hom_B_V_count": len(hom(b, v)),
        "Hom_J_V_count": len(hom(j, v)),
        "claim": "Initial image quotient is not left orthogonal to s.",
        "boundary": "Not a counterexample to P or existence of the OFS.",
    }
    return certificate


def injective_codomain_example():
    a = (2, 2, (0, 1))
    b = (1, 1, (0,))
    u = (3, 2, (0, 0, 1))
    v = (2, 1, (0, 0))
    f = ((0, 0), (0, 0))
    s = ((0, 0, 1), (0, 0))
    assert f in hom(a, b) and s in hom(u, v)
    squares = [
        (upper, lower)
        for upper in hom(a, u)
        for lower in hom(b, v)
        if compose(s, upper) == compose(lower, f)
    ]
    assert len(squares) == 5
    # A -> P has coordinates f and every upper map of a square.
    # Its componentwise image quotient is determined by these signatures.
    quotient = []
    sizes = []
    for degree in range(2):
        signatures = [
            (f[degree][x],) + tuple(upper[degree][x] for upper, _ in squares)
            for x in range(a[degree])
        ]
        distinct = list(dict.fromkeys(signatures))
        quotient.append(tuple(distinct.index(sig) for sig in signatures))
        sizes.append(len(distinct))
    q = tuple(quotient)
    structure = tuple(q[1][a[2][q[0].index(x)]] for x in range(sizes[0]))
    j = (sizes[0], sizes[1], structure)
    assert j == v and q == ((0, 1), (0, 0))
    upper = ((0, 2), (0, 1))
    lower = ((0, 1), (0,))
    assert upper in hom(a, u) and lower in hom(j, v)
    assert compose(s, upper) == compose(lower, q)
    lifts = [
        lift for lift in hom(j, u)
        if compose(lift, q) == upper and compose(s, lift) == lower
    ]
    assert not lifts
    # V=(2 -> 1) is injective: any map to it is just a map of source sets
    # to 2, which extends across any componentwise mono by assigning 0.
    assert v == (2, 1, (0, 0))
    return {
        "ambient": "Arr(Set), finite objects; ordinary unique lifting",
        "A": a, "B": b, "f": f, "U": u, "V": v, "s": s,
        "f_to_s_square_count": len(squares), "all_squares": squares,
        "image_J": j, "image_quotient": q,
        "failure_upper": upper, "failure_lower": lower,
        "lift_count": len(lifts),
        "codomain_injectivity": "V=(2 -> 1) is injective with respect to all monos.",
        "claim": "Even with injective V and nonempty square set, the initial image quotient is not left orthogonal to s.",
        "boundary": "Not a counterexample to P or existence of the OFS.",
    }


def main():
    print(json.dumps({
        "vacuous_squares": vacuous_square_example(),
        "injective_codomain": injective_codomain_example(),
    }, indent=2))


if __name__ == "__main__":
    main()
