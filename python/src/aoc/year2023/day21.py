from collections import defaultdict

from aoc.util import load_input, load_example


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
        print(len(steps), max_steps)
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
        #        print('i', i, 'plots', len(steps))
        s.append(len(steps))
        new_steps = set()
        for cx, cy in steps:
            for nx, ny in infinite_neighbors(w, h, garden, cx, cy):
                new_steps.add((nx, ny))
        steps = new_steps
    #    print('i', max_steps, 'plots', len(steps))
    s.append(len(steps))
    return len(steps), s


def rec(a):
    if all(n == 0 for n in a):
        print("***")
        return 0
    d = [s - p for p, s in zip(a[:-1], a[1:])]
    return a[-1] + rec(d)


def part2(lines, steps=26501365):
    """
    >>> part2(load_example(__file__, "21"), steps=6)
    16
    >>> part2(load_example(__file__, "21"), steps=10)
    50
    >>> part2(load_example(__file__, "21"), steps=50)
    1594
    >>> part2(load_example(__file__, "21"), steps=100)
    6536
    >>> part2(load_example(__file__, "21"), steps=500)
    167004
    >>> part2(load_example(__file__, "21"), steps=1000)
    668697
    >>> part2(load_example(__file__, "21"), steps=5000)
    16733044
    """
    w, h, garden, start = read_infinite_garden(lines)
    r, s = infinite_foo(w, h, garden, start, steps)
    print("r", r)
    print(s)
    print(rec(s[200::2]))


if __name__ == "__main__":
    print(part2(load_example(__file__, "21"), steps=64))
    # data = load_input(__file__, 2023, "21")
    # print(part1(data))
    # print(part2(data))
