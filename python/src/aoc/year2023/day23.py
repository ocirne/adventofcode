from functools import lru_cache
from aoc.util import load_input, load_example


class GridTrail:

    ANTI = {
        "<": ">",
        ">": "<",
        "^": "v",
        "v": "^",
    }

    def __init__(self, lines):
        self.trail, self.start, self.end = {}, None, None
        for y, line in enumerate(lines):
            for x, v in enumerate(line):
                if v in ".<>^v":
                    self.trail[x, y] = v
                    if y == 0:
                        self.start = x, y
                    if y == len(lines) - 1:
                        self.end = x, y

    def _neighbors(self, current_node):
        (x, y), d, g, visited = current_node
        for next_pos, nd in (((x - 1, y), "<"), ((x + 1, y), ">"), ((x, y - 1), "^"), ((x, y + 1), "v")):
            if nd == self.ANTI[d]:
                continue
            if next_pos not in self.trail:
                continue
            if self.trail[x, y] != "." and self.trail[x, y] != nd:
                continue
            if str(next_pos) in visited:
                continue
            yield next_pos, nd, g + 1, visited + str(next_pos)

    def dijkstra_directed(self):
        open_set = {(self.start, "v", 0, "")}
        closed_set = set()
        while open_set:
            current_node = open_set.pop()
            if current_node[0] == self.end:
                yield current_node[2]
            if current_node in closed_set:
                continue
            closed_set.add(current_node)
            for next_node in self._neighbors(current_node):
                if next_node in closed_set:
                    continue
                open_set.add(next_node)


class GraphTrail:
    def __init__(self, lines, grid: GridTrail):
        self.grid = grid
        self.trail = self._grid_to_graph(lines)
        self.result = -1
        self.end = grid.end

    def _grid_neighbors(self, x, y):
        return (pos for pos in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if pos in self.grid.trail)

    def _find_graph_neighbors(self, vertices, start):
        open_set = {start}
        visited = set()
        g = {start: 0}
        while open_set:
            current_pos = open_set.pop()
            if current_pos in visited:
                continue
            visited.add(current_pos)
            for next_pos in self._grid_neighbors(*current_pos):
                if next_pos in visited:
                    continue
                if next_pos in vertices:
                    yield next_pos, g[current_pos] + 1
                else:
                    g[next_pos] = g[current_pos] + 1
                    open_set.add(next_pos)

    def _grid_to_graph(self, lines):
        w, h = len(lines[0]), len(lines)
        vertices = {self.grid.start, self.grid.end}
        for y in range(h):
            for x in range(w):
                if (x, y) in self.grid.trail:
                    s = sum(1 for _ in self._grid_neighbors(x, y))
                    if s > 2:
                        vertices.add((x, y))
        graph = {v: [] for v in vertices}
        for vertex_start in vertices:
            for vertex_neighbor in self._find_graph_neighbors(vertices, vertex_start):
                graph[vertex_start].append(vertex_neighbor)
        return graph

    @lru_cache
    def dfs(self, current, steps=0, visited=""):
        if current == self.end:
            if self.result < steps:
                self.result = steps
        else:
            for neighbor, edge in self.trail[current]:
                if str(current) in visited:
                    continue
                self.dfs(neighbor, steps + edge, visited + str(current))


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    94
    """
    trail = GridTrail(lines)
    return max(trail.dijkstra_directed())


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    154
    """
    grid = GridTrail(lines)
    graph = GraphTrail(lines, grid)
    graph.dfs(grid.start)
    return graph.result


if __name__ == "__main__":
    data = load_input(__file__, 2023, "23")
    print(part1(data))
    print(part2(data))
