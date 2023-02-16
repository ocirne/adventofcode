from collections import defaultdict
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
    def at_minute(self, minute):
        print("recalc at minute", minute)
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
        #        self.print_blizzards(result)
        return result

    def print_blizzards(self, positions):
        for y in range(-2, self.rows + 2):
            for x in range(-2, self.cols + 2):
                if (x, y) in positions:
                    print(".", end="")
                else:
                    print("#", end="")
            print()
        print("start", self.start, "end", self.end)

    def find_neighbors(self, minute, x, y):
        free_positions = self.at_minute(minute + 1)
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

    def a_star(self):
        open_heap = []
        parent = {}
        heappush(open_heap, (0, self.start))
        while open_heap:
            #            print('len', len(open_heap))
            minute, position = heappop(open_heap)
            if position == self.end:
                print("tata", minute)
                #                while (minute, position) in parent:
                #                    minute, position = parent[minute, position]
                #                    print(minute, position)
                return minute
            for neighbor in self.find_neighbors(minute, *position):
                parent[minute + 1, neighbor] = minute, position
                heappush(open_heap, (minute + 1, neighbor))


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    18
    """
    blizzards = Blizzards(lines)
    #    for m in range(2):
    #        print('-- Minute %s --' % m)
    #        foo = blizzards.at_minute(m)
    #        blizzards.print_blizzards(foo)
    #        print('--')
    return blizzards.a_star()


def part2(lines):
    """
    >>> part2(load_example(__file__, "24"))
    ...
    """
    ...


if __name__ == "__main__":
    # data = load_input(__file__, 2022, "24")
    data = load_example(__file__, "24")
    print(part1(data))
#    print(part2(data))
