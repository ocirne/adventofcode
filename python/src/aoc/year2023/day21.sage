from collections import defaultdict

from aoc.util import load_input, load_example
from sage.all import PolynomialRing, QQ


class Garden:
    def __init__(self, lines):
        self.width, self.height = len(lines[0]), len(lines)
        self.plots, self.start = defaultdict(lambda: None), None
        for y, line in enumerate(lines):
            for x, v in enumerate(line):
                self.plots[x, y] = v
                if v == "S":
                    self.start = x, y

    def _neighbors(self, x, y):
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if self.plots[nx % self.width, ny % self.height] != "#":
                yield nx, ny

    def step_around(self, max_steps):
        steps = {self.start}
        reachable = [0]
        for _ in range(max_steps):
            new_steps = set()
            for cx, cy in steps:
                for nx, ny in self._neighbors(cx, cy):
                    new_steps.add((nx, ny))
            steps = new_steps
            reachable.append(len(steps))
        return reachable


def part1(lines, steps=64):
    """
    >>> part1(load_example(__file__, "21"), steps=6)
    16
    """
    garden = Garden(lines)
    reachable = garden.step_around(steps)
    return reachable[-1]


def part2(lines, steps=26501365):
    garden = Garden(lines)
    reachable = garden.step_around(328)
    assert garden.height == garden.width == 131
    assert steps % garden.width == 65
    assert 65 % 131 == 196 % 131 == 327 % 131 == 65

    R = PolynomialRing(QQ, "x")
    points = [(i, reachable[i]) for i in (65, 196, 327)]
    p = R.lagrange_polynomial(points)
    return p(steps)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "21")
    print(part1(data))
    print(part2(data))
