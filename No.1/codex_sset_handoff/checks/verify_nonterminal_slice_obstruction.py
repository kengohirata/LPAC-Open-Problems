"""Verify the finite Hom counts of the slice-assembly counterexample.

The general OFS and coreflection assertions are proved in the research note.
This script verifies only the displayed finite presheaves and their maps.
"""

import json
from verify_nonterminal_image_obstruction import compose, hom


def main():
    zero = (0, 0, ())
    u = c = (0, 1, ())
    v = (1, 2, (0,))
    b = (1, 1, (0,))
    s = ((), (0,))
    r = ((), (0,))
    beta = ((0,), (0,))
    assert hom(b, v) == (beta,)
    assert s in hom(u, v) and r in hom(c, b)
    assert compose(beta, r) == s
    assert len(hom(c, u)) == 1
    assert len(hom(c, v)) == 2
    old_colouring = compose(beta, r)
    old_lifts = [h for h in hom(c, u) if compose(s, h) == old_colouring]
    new_colouring = ((), (1,))
    new_lifts = [h for h in hom(c, u) if compose(s, h) == new_colouring]
    assert len(old_lifts) == 1 and not new_lifts
    assert len(hom(zero, u)) == len(hom(zero, v)) == 1
    print(json.dumps({
        "ambient": "Arr(Set), ordinary unique lifting",
        "U": u, "V": v, "B": b, "C": c, "s": s, "r": r,
        "Hom_B_V_count": len(hom(b, v)),
        "Hom_C_U_count": len(hom(c, u)),
        "Hom_C_V_count": len(hom(c, v)),
        "old_colouring": old_colouring, "old_lift_count": len(old_lifts),
        "new_colouring": new_colouring, "new_lift_count": len(new_lifts),
        "boundary": "Finite assembly obstruction; not a counterexample to P."
    }, indent=2))


if __name__ == "__main__":
    main()
