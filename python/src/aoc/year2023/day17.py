from heapq import heappush, heappop

from aoc.util import load_input, load_example


MOVES = {
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
    def __init__(self, lines, min_move, max_move):
        self.min_move, self.max_move = min_move, max_move
        self.w, self.h = len(lines[0]), len(lines)
        self.heat_loss = self.read_city_blocks(lines)

    @staticmethod
    def read_city_blocks(lines):
        return {(x, y): int(c) for y, line in enumerate(lines) for x, c in enumerate(line)}

    def next_directions(self, ld, count_same):
        if count_same < self.min_move:
            yield ld, count_same + 1
        else:
            if count_same < self.max_move:
                yield ld, count_same + 1
            for d in TURNS[ld]:
                yield d, 1

    def neighbors(self, current_node):
        (x, y), last_directions, count_same = current_node
        for nd, next_count_same in self.next_directions(last_directions[-1], count_same):
            dx, dy = MOVES[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.w and 0 <= ny < self.h:
                delta_heat_loss = self.heat_loss[nx, ny]
                next_last_directions = last_directions[-(self.max_move - 1) :] + nd
                yield ((nx, ny), next_last_directions, next_count_same), delta_heat_loss

    def dijkstra(self):
        start2 = ((0, 0), ">", 1)
        start1 = ((0, 0), "v", 1)
        target = (self.w - 1, self.h - 1)
        open_heap = []
        closed_set = set()
        heappush(open_heap, (0, start1))
        heappush(open_heap, (0, start2))
        while open_heap:
            heat_loss, current_node = heappop(open_heap)
            if current_node[0] == target and current_node[2] >= self.min_move:
                return heat_loss
            if current_node in closed_set:
                continue
            closed_set.add(current_node)
            for next_node, delta in self.neighbors(current_node):
                if next_node in closed_set:
                    continue
                heappush(open_heap, (heat_loss + delta, next_node))


def part1(lines):
    """
    >>> part1(load_example(__file__, "17"))
    102
    """
    return HeatCity(lines, 1, 3).dijkstra()


def part2(lines):
    """
    >>> part2(load_example(__file__, "17"))
    94
    >>> part2(load_example(__file__, "17b"))
    71
    """
    return HeatCity(lines, 4, 10).dijkstra()


if __name__ == "__main__":
    data = load_input(__file__, 2023, "17")
    print(part1(data))
    print(part2(data))
