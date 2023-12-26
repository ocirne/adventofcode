from collections import defaultdict, Counter
import random

from aoc.util import load_input, load_example


def read_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        node, neighbors = line.split(": ")
        for neighbor in neighbors.split():
            graph[node].append(neighbor)
            graph[neighbor].append(node)
    return graph


def find_random_paths(graph, candidates):
    start = random.choice(list(graph.keys()))
    open_set = [start]
    visited = set()
    parent = {}
    while open_set:
        current_node = open_set.pop()
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor_node in random.sample(graph[current_node], len(graph[current_node])):
            if neighbor_node in visited:
                continue
            if (current_node, neighbor_node) in candidates:
                continue
            if (neighbor_node, current_node) in candidates:
                continue
            parent[neighbor_node] = current_node
            open_set.append(neighbor_node)
    total = len(graph)
    half = len(visited)
    if half < total:
        return (total - half) * half, None
    return None, [(min(n1, n2), max(n1, n2)) for n1, n2 in parent.items()]


def part1(lines):
    """
    >>> part1(load_example(__file__, "25"))
    54
    """
    graph = read_graph(lines)
    counter = Counter()
    candidates = []
    while True:
        result, path_edges = find_random_paths(graph, candidates)
        if result is not None:
            return result
        counter.update(path_edges)
        candidates = [p for p, _ in counter.most_common()[:3]]


def part2(lines):
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2023, "25")
    print(part1(data))
