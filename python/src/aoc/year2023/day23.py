from functools import lru_cache
from aoc.util import load_input, load_example


def read_trail(lines):
    trail, start, end = {}, None, None
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            if v in ".<>^v":
                trail[x, y] = v
                if y == 0:
                    start = x, y
                if y == len(lines) - 1:
                    end = x, y
    return trail, start, end


A = {
    "<": ">",
    ">": "<",
    "^": "v",
    "v": "^",
}


def neighbors(trail, current_node):
    (x, y), d, g, visited = current_node
    for next_pos, nd in (((x - 1, y), "<"), ((x + 1, y), ">"), ((x, y - 1), "^"), ((x, y + 1), "v")):
        if nd == A[d]:
            continue
        if next_pos not in trail:
            continue
        if trail[x, y] != "." and trail[x, y] != nd:
            continue
        if str(next_pos) in visited:
            continue
        yield next_pos, nd, g + 1, visited + str(next_pos)


def foo(trail, start, end):
    open_set = {(start, "v", 0, "")}
    closed_set = set()
    while open_set:
        # print(len(open_set))
        current_node = open_set.pop()
        print(current_node[2])
        if current_node[0] == end:
            print(current_node[2], current_node[3])
            yield current_node[2]
        if current_node in closed_set:
            continue
        closed_set.add(current_node)
        for next_node in neighbors(trail, current_node):
            if next_node in closed_set:
                continue
            open_set.add(next_node)


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    94
    """
    trail, start, end = read_trail(lines)
    return max(foo(trail, start, end))


def neighbors2(trail, current_node):
    (x, y), d, g, visited = current_node
    for next_pos, nd in (((x - 1, y), "<"), ((x + 1, y), ">"), ((x, y - 1), "^"), ((x, y + 1), "v")):
        if nd == A[d]:
            continue
        if next_pos not in trail:
            continue
        # if trail[x, y] != "." and trail[x, y] != nd:
        #    continue
        if str(next_pos) in visited:
            continue
        yield next_pos, nd, g + 1, visited + str(next_pos)


def simple_neighbors(trail, current_pos):
    x, y = current_pos
    return (pos for pos in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if pos in trail)


def find_graph_neighbors(trail, vertices, start):
    open_set = {start}
    visited = set()
    g = {start: 0}
    while open_set:
        current_pos = open_set.pop()
        if current_pos in visited:
            continue
        visited.add(current_pos)
        for next_pos in simple_neighbors(trail, current_pos):
            if next_pos in visited:
                continue
            if next_pos in vertices:
                yield next_pos, g[current_pos] + 1
            else:
                g[next_pos] = g[current_pos] + 1
                open_set.add(next_pos)


def simplify_trail(lines, trail, start, end):
    w, h = len(lines[0]), len(lines)
    vertices = {start, end}
    for y in range(h):
        for x in range(w):
            if (x, y) in trail:
                s = sum(1 for pos in simple_neighbors(trail, (x, y)))
                if s > 2:
                    vertices.add((x, y))
    graph = {v: [] for v in vertices}
    for vertex_start in vertices:
        for vertex_neighbor in find_graph_neighbors(trail, vertices, vertex_start):
            graph[vertex_start].append(vertex_neighbor)
    for v, e in graph.items():
        print(v, e)
    return graph


class Foo:
    def __init__(self, graph, end):
        self.graph = graph
        self.end = end
        self.result = -1

    @lru_cache
    def dfs(self, current, steps=0, visited=""):
        if current == self.end:
            if self.result < steps:
                self.result = steps
                print(steps)
        else:
            for neighbor, edge in self.graph[current]:
                if str(current) in visited:
                    continue
                self.dfs(neighbor, steps + edge, visited + str(current))


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    154
    """
    trail, start, end = read_trail(lines)
    # start_node = (start, "v", 0, "")
    #    return max(foo2(trail, start_node, end))
    graph = simplify_trail(lines, trail, start, end)
    foo3 = Foo(graph, end)
    foo3.dfs(start)
    return foo3.result


if __name__ == "__main__":
    # print(part2(load_example(__file__, "23")))
    print(part2(load_input(__file__, 2023, "23")))

    # data = load_input(__file__, 2023, "23")
    # print(part1(data))
    # print(part2(data))
