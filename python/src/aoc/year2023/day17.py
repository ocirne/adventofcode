from collections import defaultdict
from heapq import heappush, heappop

from aoc.util import load_input, load_example


M = {
    ">": (+1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, +1),
}

TURNS = {
    ">": "^v",
    "<": "^v",
    "^": "<>",
    "v": "<>",
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
            #            if A[d] == last_directions[-1]:
            #                continue
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
        while open_heap:
            best_g, current_node = heappop(open_heap)
            #            print('oh', len(open_heap), self.w, self.h, '->', best_g, current_node)
            if current_node[0] == target:
                return g[current_node]
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


class HeatCityUltra:
    def __init__(self, lines, MIN, MAX):
        self.MIN, self.MAX = MIN, MAX
        self.w, self.h = len(lines[0]), len(lines)
        self.heat_loss = self.read_city_blocks(lines)

    @staticmethod
    def read_city_blocks(lines):
        blocks = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                blocks[x, y] = int(c)
        return blocks

    def neighbors2(self, current_node):
        _, last_directions, count_same = current_node
        ld = last_directions[-1]
        if count_same < self.MIN:
            yield ld, 1, count_same + 1
        else:
            if count_same < self.MAX:
                yield ld, 1, count_same + 1
            for d in TURNS[ld]:
                yield d, 1, 1

    def neighbors(self, current_node):
        (x, y), last_directions, _ = current_node
        for nd, f, count_same in self.neighbors2(current_node):
            dx, dy = M[nd]
            nx, ny = x + f * dx, y + f * dy
            if 0 <= nx < self.w and 0 <= ny < self.h:
                yield (nx, ny), last_directions[-(self.MAX - f) :] + f * nd, count_same

    def score(self, cx, cy, tx, ty):
        return abs(cx - tx) + abs(cy - ty)

    def a_star(self):
        start2 = ((0, 0), ">", 1)
        start1 = ((0, 0), "v", 1)
        target = (self.w - 1, self.h - 1)
        open_heap = []
        closed_set = set()
        heappush(open_heap, (0, start1))
        heappush(open_heap, (0, start2))
        g = defaultdict(lambda: 0)
        while open_heap:
            best_g, current_node = heappop(open_heap)
            # print('oh', len(open_heap), self.w, self.h, '->', best_g, current_node)
            if current_node[0] == target and current_node[2] >= self.MIN:
                print("result:", g[current_node])
                return g[current_node]
            closed_set.add(current_node)
            for next_node in self.neighbors(current_node):
                if next_node in closed_set:
                    continue
                tentative_g = g[current_node] + self.heat_loss[next_node[0]]
                if tentative_g < g[next_node] or next_node not in [i[1] for i in open_heap]:
                    g[next_node] = tentative_g
                    h = self.score(*next_node[0], *target)
                    f = tentative_g + h
                    print(g[current_node], f, tentative_g, h)
                    heappush(open_heap, (f, next_node))


def part2(lines, MIN, MAX):
    """
    >>> part2(load_example(__file__, "17"))
    94
    >>> part2(load_example(__file__, "17b"))
    71
    """
    return HeatCityUltra(lines, MIN, MAX).a_star()


if __name__ == "__main__":
    assert part2(load_example(__file__, "17"), 1, 3) == 102
    assert part2(load_example(__file__, "17"), 4, 10) == 94
    assert part2(load_example(__file__, "17b"), 4, 10) == 71

    # data = load_example(__file__, "17b")
    # data = load_input(__file__, 2023, "17")
    # print(part2(data, 0, 3))
    # print(part2(data, 4, 10))
