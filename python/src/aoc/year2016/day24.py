from heapq import heappush, heappop
from itertools import combinations, permutations

from aoc.util import load_input, load_example

WALL = "#"


def read_data(lines):
    field = {}
    air_ducts = {}
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            field[x, y] = v
            if v.isnumeric():
                air_ducts[int(v)] = (x, y)
    return field, air_ducts


def find_neighbors(field, current_node):
    cx, cy = current_node
    neighbors = [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]
    return (neighbor for neighbor in neighbors if field[neighbor] != WALL)


def a_star(field, start_node, end_node):
    open_heap = []
    closed_set = set()
    parent = {}
    g = {start_node: 0}

    heappush(open_heap, (0, start_node))
    while open_heap:
        current_node = heappop(open_heap)[1]
        if current_node == end_node:
            length = 0
            while current_node in parent:
                length += 1
                current_node = parent[current_node]
            return length
        closed_set.add(current_node)
        # expand node
        for neighbor in find_neighbors(field, current_node):
            if neighbor in closed_set:
                continue
            tentative_g = g[current_node] + 1
            if neighbor in closed_set and tentative_g >= g[neighbor]:
                continue
            if tentative_g < g.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap]:
                parent[neighbor] = current_node
                g[neighbor] = tentative_g
                heappush(open_heap, (tentative_g, neighbor))


def sort2(x, y):
    return (x, y) if x < y else (y, x)


def count_steps(steps, path):
    return sum(steps[sort2(path[i - 1], path[i])] for i in range(1, len(path)))


def traveling(lines, extra):
    field, air_ducts = read_data(lines)
    steps = {sort2(a, b): a_star(field, air_ducts[a], air_ducts[b]) for a, b in combinations(air_ducts, 2)}
    return min(count_steps(steps, [0] + list(p) + extra) for p in permutations(range(1, max(air_ducts) + 1)))


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    14
    """
    return traveling(lines, [])


def part2(lines):
    return traveling(lines, [0])


if __name__ == "__main__":
    data = load_input(__file__, 2016, "24")
    print(part1(data))
    print(part2(data))
