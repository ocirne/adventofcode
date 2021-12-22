import re

from aoc.util import load_input, load_example

PATTERN = r".+x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"


def read_data(lines, max50=False):
    rules = []
    xs = set()
    ys = set()
    zs = set()
    for line in lines:
        action = line.split()[0] == "on"
        x1, x2, y1, y2, z1, z2 = map(int, re.match(PATTERN, line).groups())
        if max50 and (x1 < -50 or x2 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50):
            continue
        xs.add(x1)
        xs.add(x2 + 1)
        ys.add(y1)
        ys.add(y2 + 1)
        zs.add(z1)
        zs.add(z2 + 1)
        rules.append((action, x1, x2 + 1, y1, y2 + 1, z1, z2 + 1))
    return rules, sorted(xs), sorted(ys), sorted(zs)


def count_cuboids(lines, max50):
    rules, xs, ys, zs = read_data(lines, max50)
    cuboid = [[[False for _ in range(len(xs))] for _ in range(len(ys))] for _ in range(len(zs))]
    for action, xo1, xo2, yo1, yo2, zo1, zo2 in rules:
        for xi in range(xs.index(xo1), xs.index(xo2)):
            for yi in range(ys.index(yo1), ys.index(yo2)):
                for zi in range(zs.index(zo1), zs.index(zo2)):
                    cuboid[zi][yi][xi] = action
    total = 0
    for x in range(len(xs)):
        for y in range(len(ys)):
            for z in range(len(zs)):
                if cuboid[z][y][x]:
                    total += (xs[x + 1] - xs[x]) * (ys[y + 1] - ys[y]) * (zs[z + 1] - zs[z])
    return total


def part1(lines):
    """
    >>> part1(load_example(__file__, "22a"))
    39
    >>> part1(load_example(__file__, "22b"))
    590784
    >>> part1(load_example(__file__, "22c"))
    474140
    """
    return count_cuboids(lines, max50=True)


def part2(lines):
    """
    >>> part2(load_example(__file__, "22a"))
    39
    >>> part2(load_example(__file__, "22c"))
    2758514936282235
    """
    return count_cuboids(lines, max50=False)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "22")
    print(part1(data))
    print(part2(data))
