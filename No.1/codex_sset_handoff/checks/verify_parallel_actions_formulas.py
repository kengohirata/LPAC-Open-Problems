"""Finite sanity checks for the parallel-action counterexample proof.

These check action/composition directions and finite Hom equations only.
They do not verify Isbell's theorem, compactness, or non-coreflectivity.
"""

import argparse
import itertools
import json
from pathlib import Path


def compose(f, g):
    return tuple(f[g[x]] for x in range(len(g)))


def act(m, x):
    return tuple(m[v] for v in x)


def minimal_coordinate_supports(values, monoid, omega_size):
    supports = []
    for size in range(omega_size + 1):
        for subset in itertools.combinations(range(omega_size), size):
            if any(set(previous).issubset(subset) for previous in supports):
                continue
            by_restriction = {}
            valid = True
            for m, value in zip(monoid, values):
                restriction = tuple(m[s] for s in subset)
                if restriction in by_restriction:
                    if by_restriction[restriction] != value:
                        valid = False
                        break
                else:
                    by_restriction[restriction] = value
            if valid:
                supports.append(subset)
    return supports


def hom_from_power(n, omega, monoid):
    """For n <= |Omega| the injective tuple generates the full power."""
    generator = tuple(range(n))
    states = tuple(itertools.product(omega, repeat=n))
    homs = []
    for value in omega:
        candidate = {}
        valid = True
        for m in monoid:
            x = act(m, generator)
            y = m[value]
            if x in candidate and candidate[x] != y:
                valid = False
                break
            candidate[x] = y
        if not valid:
            continue
        assert set(candidate) == set(states)
        assert all(candidate[act(m, x)] == m[candidate[x]]
                   for m in monoid for x in states)
        homs.append(candidate)
    expected = [{x: x[i] for x in states} for i in range(n)]
    assert homs == expected
    return states, homs


def run_checks():
    omega = tuple(range(3))
    monoid = tuple(itertools.product(omega, repeat=3))
    indices = {m: i for i, m in enumerate(monoid)}
    composition_indices = {
        (i, j): indices[compose(m, n)]
        for i, m in enumerate(monoid)
        for j, n in enumerate(monoid)
    }

    # For each a in Omega^2, check Phi_a(nx)(m)=Phi_a(x)(mn).
    states = tuple(itertools.product(omega, repeat=2))
    equivariance_checks = 0
    support_certificates = []
    for a in states:
        phi = {x: tuple(int(act(m, x) == a) for m in monoid) for x in states}
        for x in states:
            for j, n in enumerate(monoid):
                lhs = phi[act(n, x)]
                rhs = tuple(phi[x][composition_indices[i, j]]
                            for i in range(len(monoid)))
                assert lhs == rhs
                equivariance_checks += 1
        supports = minimal_coordinate_supports(phi[a], monoid, len(omega))
        expected_support = tuple(sorted(set(a)))
        assert supports == [expected_support]
        support_certificates.append({"a": a, "minimal_support": expected_support})

    hom_counts = []
    sigma_counts = []
    for n in range(4):
        power, homs = hom_from_power(n, omega, monoid)
        hom_counts.append({"power": n, "Hom_to_Omega": len(homs)})
        if not n:
            continue
        successor = tuple(min(i + 1, n - 1) for i in range(n))
        q = {x: tuple(x[successor[i]] for i in range(n)) for x in power}
        # Y=(F(n), id, successor^*). A map to the source of sigma
        # has components ((v p, v q), v); sigma selects v p.
        post_sigma = []
        for v in homs:
            u = {x: (v[x], v[q[x]]) for x in power}
            assert all(u[act(m, x)] == act(m, u[x])
                       for m in monoid for x in power)
            post_sigma.append({x: u[x][0] for x in power})
        assert post_sigma == homs
        sigma_counts.append({"X_size": n, "Hom_to_source": len(homs),
                             "Hom_to_target": len(post_sigma), "bijective": True})

    # Enumerate finite k:T->T and h:T->X with h k=d h and 0 in im(h).
    # The finite successor chain must be entirely in im(h).
    dynamical_counts = []
    for n in range(1, 5):
        successor = tuple(min(i + 1, n - 1) for i in range(n))
        for m in range(1, 5):
            count = 0
            for k in itertools.product(range(m), repeat=m):
                for h in itertools.product(range(n), repeat=m):
                    if 0 not in h:
                        continue
                    if not all(h[k[t]] == successor[h[t]] for t in range(m)):
                        continue
                    assert set(h) == set(range(n))
                    assert m >= n
                    count += h.count(0)
            if m < n:
                assert count == 0
            if m == n:
                assert count > 0
            dynamical_counts.append({"X_size": n, "T_size": m,
                                     "pointed_semiconjugacies": count})

    return {
        "omega_size": len(omega),
        "monoid_size": len(monoid),
        "cofree_equivariance_checks": equivariance_checks,
        "point_detector_supports": support_certificates,
        "finite_power_Hom_counts": hom_counts,
        "sigma_Hom_counts": sigma_counts,
        "finite_dynamical_factorizations": dynamical_counts,
        "boundary": "Finite algebraic checks only; the infinite conditional theorem is proved separately in the research note.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_checks()
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(serialized)
        print(json.dumps({"status": "PASS", "output": str(args.output),
                          "cofree_checks": result["cofree_equivariance_checks"],
                          "dynamical_cases": len(result["finite_dynamical_factorizations"])}))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
