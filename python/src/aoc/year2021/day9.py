from collections import defaultdict, Counter
from math import prod

from aoc.util import load_input, load_example

from aoc.disjoint import union, find


def part1(lines):
    """
    >>> part1(load_example(__file__, "9"))
    15
    """
    area = defaultdict(lambda: 10)
    height = len(lines)
    width = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            area[x, y] = int(c)
    result = 0
    for x in range(width):
        for y in range(height):
            if (
                area[x, y] < area[x + 1, y]
                and area[x, y] < area[x - 1, y]
                and area[x, y] < area[x, y + 1]
                and area[x, y] < area[x, y - 1]
            ):
                result += area[x, y] + 1
    return result


def part2(lines):
    """
    >>> part2(load_example(__file__, "9"))
    1134
    """
    area = defaultdict(lambda: None)
    height = len(lines)
    width = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == "9":
                continue
            area[x, y] = (x, y)
    for x in range(width):
        for y in range(height):
            if area[x, y] is None:
                continue
            if area[x + 1, y] is not None:
                union(area, (x, y), (x + 1, y))
            if area[x, y + 1] is not None:
                union(area, (x, y), (x, y + 1))
    for x in range(width):
        for y in range(height):
            find(area, (x, y))
    counts = Counter(x for x in area.values() if x is not None)
    return prod([size for _, size in counts.most_common()[:3]])


if __name__ == "__main__":
    data = load_input(__file__, 2021, "9")
    print(part1(data))
    print(part2(data))
