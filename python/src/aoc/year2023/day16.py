from aoc.util import load_input, load_example

import sys

sys.setrecursionlimit(2_00000)


M = {
    ">": (+1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, +1),
}


class CaveWalker:
    def __init__(self, lines):
        self.w, self.h, self.cave = self.read_cave(lines)
        self.visited = {}

    @staticmethod
    def read_cave(lines):
        w, h = len(lines[0]), len(lines)
        cave = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                cave[x, y] = c
        return w, h, cave

    def rec(self, px, py, d):
        dx, dy = M[d]
        px += dx
        py += dy
        if not (0 <= px < self.w and 0 <= py < self.h):
            return
        if (px, py) in self.visited and self.visited[px, py] == d:
            print("loop?")
            return
        self.visited[px, py] = d
        print(px, py, d)
        if self.cave[px, py] == ".":
            self.rec(px, py, d)
        elif self.cave[px, py] == "/":
            if d == ">":
                self.rec(px, py, "^")
            elif d == "<":
                self.rec(px, py, "v")
            elif d == "^":
                self.rec(px, py, ">")
            elif d == "v":
                self.rec(px, py, "<")
        elif self.cave[px, py] == "\\":
            if d == ">":
                self.rec(px, py, "v")
            elif d == "<":
                self.rec(px, py, "^")
            elif d == "^":
                self.rec(px, py, "<")
            elif d == "v":
                self.rec(px, py, ">")
        elif self.cave[px, py] == "|":
            if d in "<>":
                self.rec(px, py, "^")
                self.rec(px, py, "v")
            else:
                self.rec(px, py, d)
        elif self.cave[px, py] == "-":
            if d in "^v":
                self.rec(px, py, "<")
                self.rec(px, py, ">")
            else:
                self.rec(px, py, d)


def part1(lines):
    """
    >>> part1(load_example(__file__, "16"))
    46
    """
    walker = CaveWalker(lines)
    walker.rec(-1, 0, ">")
    return len(walker.visited)


def part2(lines):
    """
    >>> part2(load_example(__file__, "16"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "16")
    #    data = load_example(__file__, "16")
    print(part1(data))
#    print(part2(data))
