from heapq import heappush, heappop

from aoc.util import load_input, load_example


def load_cave(lines):
    cave = {}
    for y, line in enumerate(lines):
        for x, risk_level in enumerate(map(int, line)):
            cave[x, y] = risk_level
    return cave


def find_neighbors(current_node, end_node):
    ex, ey = end_node
    cx, cy = current_node
    neighbors = []
    if cx > 0:
        neighbors.append((cx - 1, cy))
    if cx < ex:
        neighbors.append((cx + 1, cy))
    if cy > 0:
        neighbors.append((cx, cy - 1))
    if cy < ex:
        neighbors.append((cx, cy + 1))
    return neighbors


def a_star(score, end_node):
    start_node = (0, 0)
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
                length += score(*current_node)
                current_node = parent[current_node]
            return length
        closed_set.add(current_node)
        # expand node
        for neighbor in find_neighbors(current_node, end_node):
            if neighbor in closed_set:
                continue
            tentative_g = g[current_node] + score(*neighbor)
            if neighbor in closed_set and tentative_g >= g[neighbor]:
                continue
            if tentative_g < g.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap]:
                parent[neighbor] = current_node
                g[neighbor] = tentative_g
                heappush(open_heap, (tentative_g, neighbor))


def expand_score(cave, ex, ey):
    return lambda x, y: ((cave[x % ex, y % ey] + x // ex + y // ey) - 1) % 9 + 1


def part1(lines):
    """
    >>> part1(load_example(__file__, "15"))
    40
    """
    cave = load_cave(lines)
    ex, ey = max(cave)
    end_node = ex, ey
    result = a_star(expand_score(cave, ex + 1, ey + 1), end_node)
    return result


def part2(lines):
    """
    >>> part2(load_example(__file__, "15"))
    315
    """
    cave = load_cave(lines)
    ex, ey = max(cave)
    end_node = 5 * (ex + 1) - 1, 5 * (ey + 1) - 1
    result = a_star(expand_score(cave, ex + 1, ey + 1), end_node)
    return result


if __name__ == "__main__":
    data = load_input(__file__, 2021, "15")
    print(part1(data))
    print(part2(data))
