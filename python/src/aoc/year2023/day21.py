from collections import defaultdict

from aoc.util import load_input, load_example
from sage.all import PolynomialRing, QQ


def read_garden(lines):
    garden, s = {}, None
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            garden[x, y] = v
            if v == "S":
                s = x, y
    return garden, s


def neighbors(garden, x, y):
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if (nx, ny) in garden and garden[nx, ny] != "#":
            yield nx, ny


def foo(garden, start, max_steps):
    steps = {start}
    for _ in range(max_steps):
        new_steps = set()
        for cx, cy in steps:
            for nx, ny in neighbors(garden, cx, cy):
                new_steps.add((nx, ny))
        steps = new_steps
    return len(steps)


def part1(lines, steps=64):
    """
    >>> part1(load_example(__file__, "21"), steps=6)
    16
    """
    garden, start = read_garden(lines)
    return foo(garden, start, steps)


def read_infinite_garden(lines):
    w, h = len(lines[0]), len(lines)
    garden, s = defaultdict(lambda: None), None
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            garden[x, y] = v
            if v == "S":
                s = x, y
    return w, h, garden, s


def infinite_neighbors(w, h, garden, x, y):
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if garden[nx % w, ny % h] != "#":
            yield nx, ny


def infinite_foo(w, h, garden, start, max_steps):
    steps = {start}
    s = []
    for i in range(max_steps):
        s.append(len(steps))
        new_steps = set()
        for cx, cy in steps:
            for nx, ny in infinite_neighbors(w, h, garden, cx, cy):
                new_steps.add((nx, ny))
        steps = new_steps
    s.append(len(steps))
    return len(steps), s


def part2(lines, steps=26501365):
    width, height, garden, start = read_infinite_garden(lines)
    r, s = infinite_foo(width, height, garden, start, 328)
    assert height == width == 131
    assert steps % width == 65
    assert 65 % 131 == 196 % 131 == 327 % 131 == 65

    R = PolynomialRing(QQ, "x")
    points = [(i, s[i]) for i in (65, 196, 327)]
    p = R.lagrange_polynomial(points)
    return p(steps)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "21")
    print(part1(data))
    print(part2(data))
