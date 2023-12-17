from collections import defaultdict
from heapq import heappush, heappop

from aoc.util import load_input, load_example


M = {
    ">": (+1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, +1),
}

A = {
    ">": "<",
    "<": ">",
    "^": "v",
    "v": "^",
}


class HeatCity:
    def __init__(self, lines):
        self.w, self.h = len(lines[0]), len(lines)
        self.heat_loss = self.read_city_blocks(lines)

    @staticmethod
    def read_city_blocks(lines):
        blocks = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                blocks[x, y] = int(c)
        return blocks

    def neighbors(self, current_node):
        (x, y), last_directions = current_node
        for d in M:
            if A[d] == last_directions[-1]:
                continue
            if all(d == ld for ld in last_directions):
                continue
            dx, dy = M[d]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                continue
            yield (nx, ny), last_directions[-2:] + d

    def score(self, cx, cy, tx, ty):
        return abs(cx - tx) + abs(cy - ty)

    def a_star(self):
        start = ((0, 0), ".")
        target = (self.w - 1, self.h - 1)
        open_heap = []
        closed_set = set()
        heappush(open_heap, (0, start))
        g = defaultdict(lambda: 0)
        #      parent = {start: None}
        while open_heap:
            best_g, current_node = heappop(open_heap)
            #            print('oh', len(open_heap), self.w, self.h, '->', best_g, current_node)
            if current_node[0] == target:
                return g[current_node]
            #               heat_loss = 0
            #               path_node = current_node
            #               while path_node is not start:
            #                   heat_loss += self.heat_loss[path_node[0]]
            #                   path_node = parent[path_node]
            #               return heat_loss
            closed_set.add(current_node)
            for next_node in self.neighbors(current_node):
                if next_node in closed_set:
                    continue
                tentative_g = g[current_node] + self.heat_loss[next_node[0]]
                if next_node in closed_set and tentative_g >= g[next_node]:
                    continue
                if tentative_g < g[next_node] or next_node not in [i[1] for i in open_heap]:
                    #                   parent[next_node] = current_node
                    g[next_node] = tentative_g
                    #                  h = self.score(*next_node[0], *target)
                    #                  print(tentative_g, h)
                    f = tentative_g
                    heappush(open_heap, (f, next_node))


def part1(lines):
    """
    >>> part1(load_example(__file__, "17"))
    102
    """
    return HeatCity(lines).a_star()


def part2(lines):
    """
    >>> part2(load_example(__file__, "17"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "17")
    # data = load_example(__file__, "17")
    print(part1(data))
    # print(part2(data))
