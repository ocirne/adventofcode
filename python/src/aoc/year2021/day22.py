import re
from collections import defaultdict

from aoc.util import load_input, load_example

PATTERN = r".+x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"


def part1(lines):
    """
    >>> part1(load_example(__file__, "22a"))
    39
    >>> part1(load_example(__file__, "22b"))
    590784
    """
    cuboid = defaultdict(lambda: False)
    for line in lines:
        action = line.split()[0] == "on"
        xo1, xo2, yo1, yo2, zo1, zo2 = map(int, re.match(PATTERN, line).groups())
        x1 = max(xo1, -50)
        x2 = min(xo2, 50)
        y1 = max(yo1, -50)
        y2 = min(yo2, 50)
        z1 = max(zo1, -50)
        z2 = min(zo2, 50)
        print(xo1, xo2, yo1, yo2, zo1, zo2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    cuboid[x, y, z] = action
    return sum(int(v) for v in cuboid.values())


def is_on(xc1, xc2, yc1, yc2, zc1, zc2, rules):
    #    print('is_on', xc1, xc2, yc1, yc2, zc1, zc2)
    for action, xo1, xo2, yo1, yo2, zo1, zo2 in reversed(rules):
        if xo1 <= xc1 and xc2 <= xo2 and yo1 <= yc1 and yc2 <= yo2 and zo1 <= zc1 and zc2 <= zo2:
            return action
    return False


def part2(lines):
    """
    >>> part2(load_example(__file__, "22c"))
    2758514936282235
    """
    rules = []
    xs = set()
    ys = set()
    zs = set()
    for line in lines:
        action = line.split()[0] == "on"
        xo1, xo2, yo1, yo2, zo1, zo2 = map(int, re.match(PATTERN, line).groups())
        print(action, xo1, xo2, yo1, yo2, zo1, zo2)
        xs.add(xo1)
        xs.add(xo2 + 1)
        ys.add(yo1)
        ys.add(yo2 + 1)
        zs.add(zo1)
        zs.add(zo2 + 1)
        rules.append((action, xo1, xo2 + 1, yo1, yo2 + 1, zo1, zo2 + 1))
    xss = sorted(xs)
    yss = sorted(ys)
    zss = sorted(zs)
    print("xss", len(xss), xss)
    print("yss", len(yss), yss)
    print("zss", len(zss), zss)
    cuboid = [[[False for _ in range(len(xss))] for _ in range(len(yss))] for _ in range(len(zss))]
    for i, rule in enumerate(rules):
        print(i, "rule", rule)
        action, xo1, xo2, yo1, yo2, zo1, zo2 = rule
        for xi in range(xss.index(xo1), xss.index(xo2)):
            for yi in range(yss.index(yo1), yss.index(yo2)):
                for zi in range(zss.index(zo1), zss.index(zo2)):
                    cuboid[zi][yi][xi] = action
    total = 0
    for xi in range(len(xss)):
        print(xi)
        for yi in range(len(yss)):
            for zi in range(len(zss)):
                if cuboid[zi][yi][xi]:
                    total += (xss[xi + 1] - xss[xi]) * (yss[yi + 1] - yss[yi]) * (zss[zi + 1] - zss[zi])
    print(total)
    return total
    total = 0
    #    for xi in range(1, len(xss)):
    #        print(xi)
    #        for yi in range(1, len(yss)):
    #            for zi in range(1, len(zss)):
    #                on = is_on(*xss[xi-1:xi+1], *yss[yi-1:yi+1], *zss[zi-1:zi+1], rules)
    #                if on:
    #                    total += (xss[xi] - xss[xi-1]) * (yss[yi] - yss[yi-1]) * (zss[zi] - zss[zi-1])
    print(total)
    return total


if __name__ == "__main__":
    #    assert part1(load_example(__file__, "22a")) == 39
    assert part2(load_example(__file__, "22a")) == 39
    #    assert part1(load_example(__file__, "22b")) == 590784
    #    assert part2(load_example(__file__, "22b")) == 590784
    #    assert part2(load_example(__file__, "22c")) == 474140
    #    assert part2(load_example(__file__, "22c")) == 2758514936282235
    data = load_input(__file__, 2021, "22")
    #    assert part2(data) == 596598
    #    print(part1(data))
    print(part2(data))
