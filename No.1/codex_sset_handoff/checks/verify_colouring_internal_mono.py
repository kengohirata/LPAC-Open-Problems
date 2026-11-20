#!/usr/bin/env python3
"""Verify one internal mono for the componentwise non-two-colourable class.

The ordinary category is Quiv (loops and parallel edges allowed). This is a
finite certificate, not a test of non-coreflectivity or of a large cardinal.
Uses the mathematical criterion that the internal kernel pair is obtained by
retaining the non-two-colourable components of the ordinary kernel pair.
"""

import argparse
import itertools
import json
from pathlib import Path


def components(vertices, edges):
    neighbors = {v: set() for v in vertices}
    for _, source, target in edges:
        neighbors[source].add(target)
        neighbors[target].add(source)
    unseen = set(vertices)
    result = []
    while unseen:
        root = min(unseen)
        reached = {root}
        pending = [root]
        while pending:
            vertex = pending.pop()
            for neighbor in neighbors[vertex] - reached:
                reached.add(neighbor)
                pending.append(neighbor)
        unseen -= reached
        result.append(sorted(reached))
    return sorted(result)


def colourings(vertices, edges):
    result = []
    for values in itertools.product(range(2), repeat=len(vertices)):
        colouring = dict(zip(vertices, values))
        if all(colouring[source] != colouring[target]
               for _, source, target in edges):
            result.append(values)
    return result


def verify():
    a_vertices = [0, 1, 2]
    permutations = {"a": [1, 0, 2], "b": [0, 2, 1]}
    a_edges = [(f"{label}{v}", v, permutation[v])
               for label, permutation in permutations.items()
               for v in a_vertices]
    b_vertices = [0]
    b_edges = [("a", 0, 0), ("b", 0, 0)]
    vertex_map = {v: 0 for v in a_vertices}
    edge_map = {name: name[0] for name, _, _ in a_edges}
    b_by_name = {name: (source, target) for name, source, target in b_edges}
    for name, source, target in a_edges:
        assert b_by_name[edge_map[name]] == (vertex_map[source], vertex_map[target])

    assert len(components(a_vertices, a_edges)) == 1
    assert not colourings(a_vertices, a_edges)
    assert not colourings(b_vertices, b_edges)
    assert len(set(vertex_map.values())) < len(vertex_map)
    assert len(set(edge_map.values())) < len(edge_map)

    # The kernel pair is computed from the maps, rather than entered by hand.
    kernel_vertices = [(x, y) for x in a_vertices for y in a_vertices
                       if vertex_map[x] == vertex_map[y]]
    kernel_edges = [((left, right), (ls, rs), (lt, rt))
                    for left, ls, lt in a_edges
                    for right, rs, rt in a_edges
                    if edge_map[left] == edge_map[right]]
    component_results = []
    retained_vertices = set()
    retained_edges = set()
    for vertex_list in components(kernel_vertices, kernel_edges):
        vertex_set = set(vertex_list)
        edge_list = [edge for edge in kernel_edges if edge[1] in vertex_set]
        assert all(edge[2] in vertex_set for edge in edge_list)
        all_colours = colourings(vertex_list, edge_list)
        if not all_colours:
            retained_vertices.update(vertex_set)
            retained_edges.update(name for name, _, _ in edge_list)
        component_results.append({
            "vertices": vertex_list,
            "edges": edge_list,
            "two_colourings": all_colours,
            "retained_by_coreflector": not all_colours,
        })

    diagonal_vertices = {(v, v) for v in a_vertices}
    diagonal_edges = {(name, name) for name, _, _ in a_edges}
    assert retained_vertices == diagonal_vertices
    assert retained_edges == diagonal_edges
    assert sorted(len(c["vertices"]) for c in component_results) == [3, 6]
    assert sorted(len(c["two_colourings"]) for c in component_results) == [0, 2]

    # Local injectivity, used in the size bound, is distinct from injectivity.
    for vertex in a_vertices:
        for endpoint in (1, 2):
            incident = [name for name, source, target in a_edges
                        if (name, source, target)[endpoint] == vertex]
            assert len({edge_map[name] for name in incident}) == len(incident)

    return {
        "ambient_category": "Quiv",
        "D": "loopless directed K2 with one edge in each direction",
        "subcategory": "every connected component has no map to D",
        "A": {"vertices": a_vertices, "edges": a_edges},
        "B": {"vertices": b_vertices, "edges": b_edges},
        "m": {"vertex_map": vertex_map, "edge_map": edge_map},
        "ordinary_kernel_pair": {
            "vertex_count": len(kernel_vertices),
            "edge_count": len(kernel_edges),
            "components": component_results,
        },
        "internal_kernel_pair_is_diagonal": True,
        "internal_mono": True,
        "ambient_mono": False,
        "scope": "One exact finite witness; no independence or non-coreflectivity claim.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = verify()
    if args.output:
        args.output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("PASS: A=(3 vertices, 6 edges), B=(1 vertex, 2 edges)")
    print("Kernel pair: 9 vertices, 18 edges; component sizes 3 and 6")
    print("All two-colouring counts: 0 and 2; retained component is exactly diagonal")
    print("Internal mono: true; ordinary mono: false; local injectivity: true")


if __name__ == "__main__":
    main()
