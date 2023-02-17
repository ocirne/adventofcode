from functools import cache
from heapq import heappush, heappop

from aoc.util import load_input, load_example


class Blizzards:
    def __init__(self, lines):
        self.blizzards = {"<": [], ">": [], "^": [], "v": []}
        self.rows = len(lines) - 2
        for y, line in enumerate(lines):
            self.cols = len(line) - 2
            for x, b in enumerate(line):
                if b == "#" or b == ".":
                    continue
                self.blizzards[b].append((x - 1, y - 1))
        self.start = self.lookup_start(lines)
        self.end = self.lookup_end(lines)

    @staticmethod
    def lookup_start(lines):
        return lines[0].find(".") - 1, -1

    @staticmethod
    def lookup_end(lines):
        return lines[-1].find(".") - 1, len(lines) - 2

    @cache
    def free_at_minute(self, minute):
        positions = set()
        for x, y in self.blizzards["<"]:
            positions.add(((x - minute) % self.cols, y))
        for x, y in self.blizzards[">"]:
            positions.add(((x + minute) % self.cols, y))
        for x, y in self.blizzards["^"]:
            positions.add((x, (y - minute) % self.rows))
        for x, y in self.blizzards["v"]:
            positions.add((x, (y + minute) % self.rows))
        free = {(x, y) for x in range(self.cols) for y in range(self.rows)}
        free.add(self.start)
        free.add(self.end)
        result = free.difference(positions)
        return result

    def find_neighbors(self, minute, x, y):
        free_positions = self.free_at_minute(minute + 1)
        neighbors = []
        if (x, y) in free_positions:
            neighbors.append((x, y))
        if (x - 1, y) in free_positions:
            neighbors.append((x - 1, y))
        if (x + 1, y) in free_positions:
            neighbors.append((x + 1, y))
        if (x, y - 1) in free_positions:
            neighbors.append((x, y - 1))
        if (x, y + 1) in free_positions:
            neighbors.append((x, y + 1))
        return neighbors

    def dijkstra(self, start, end, minute_0=0):
        open_heap = []
        closed_set = set()
        heappush(open_heap, (minute_0, start))
        while open_heap:
            minute, position = heappop(open_heap)
            if position == end:
                return minute - minute_0
            if (minute, position) in closed_set:
                continue
            closed_set.add((minute, position))
            for neighbor in self.find_neighbors(minute, *position):
                heappush(open_heap, (minute + 1, neighbor))


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    18
    """
    blizzards = Blizzards(lines)
    return blizzards.dijkstra(blizzards.start, blizzards.end)


def part2(lines):
    """
    >>> part2(load_example(__file__, "24"))
    54
    """
    blizzards = Blizzards(lines)
    m1 = blizzards.dijkstra(blizzards.start, blizzards.end)
    m2 = blizzards.dijkstra(blizzards.end, blizzards.start, m1)
    m3 = blizzards.dijkstra(blizzards.start, blizzards.end, m1 + m2)
    return m1 + m2 + m3


if __name__ == "__main__":
    data = load_input(__file__, 2022, "24")
    print(part1(data))
    print(part2(data))
