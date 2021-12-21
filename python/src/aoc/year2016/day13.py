from collections import defaultdict
from functools import lru_cache
from heapq import heappush, heappop

from aoc.util import load_input, load_example


@lru_cache
def is_open_space(x, y, fav):
    n = x * x + 3 * x + 2 * x * y + y + y * y + fav
    return bin(n).count("1") % 2 == 0


def score(x, y, tx, ty):
    return abs(x - tx) + abs(y - ty)


def valid_moves(x, y, fav):
    moves = []
    if x > 0:
        moves.append((x - 1, y))
    if y > 0:
        moves.append((x, y - 1))
    moves.append((x + 1, y))
    moves.append((x, y + 1))
    return [move for move in moves if is_open_space(*move, fav)]


def a_star(start, target, fav):
    open_heap = []
    closed_set = set()
    heappush(open_heap, (0, start))
    g = defaultdict(lambda: 0)
    parent = {start: None}
    while open_heap:
        current_node = heappop(open_heap)[1]
        if current_node == target:
            depth = -1
            path_node = current_node
            while path_node is not None:
                path_node = parent[path_node]
                depth += 1
            return depth
        closed_set.add(current_node)
        for neighbor in valid_moves(*current_node, fav):
            if neighbor in closed_set:
                continue
            tentative_g = g[current_node] + 1
            if neighbor in closed_set and tentative_g >= g[neighbor]:
                continue
            if tentative_g < g[neighbor] or neighbor not in [i[1] for i in open_heap]:
                parent[neighbor] = current_node
                g[neighbor] = tentative_g
                h = score(*neighbor, *target)
                f = tentative_g + h
                heappush(open_heap, (f, neighbor))


def part1(lines, tx=31, ty=39):
    """
    >>> part1(load_example(__file__, "13"), tx=7, ty=4)
    11
    """
    fav = int(lines[0])
    return a_star(start=(1, 1), target=(tx, ty), fav=fav)


def part2(lines):
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2016, "13")
    print(part1(data))
    print(part2(data))
