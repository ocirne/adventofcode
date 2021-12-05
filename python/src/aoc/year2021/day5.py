import re
from collections import defaultdict

from aoc.util import load_input, load_example

PATTERN = r"(\d+),(\d+) -> (\d+),(\d+)"


def mark_vents(lines, diagonals=False):
    diagram = defaultdict(lambda: 0)
    for line in lines:
        ux1, uy1, ux2, uy2 = map(int, re.match(PATTERN, line).groups())
        x1, x2 = sorted((ux1, ux2))
        y1, y2 = sorted((uy1, uy2))
        if x1 == x2 and y1 == y2:
            diagram[x1, y1] += 1
        elif x1 == x2:
            for y in range(y1, y2 + 1):
                diagram[x1, y] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                diagram[x, y1] += 1
        elif not diagonals:
            ...
        elif (ux1 < ux2 and uy1 < uy2) or (ux1 > ux2 and uy1 > uy2):
            for i in range(x2 - x1 + 1):
                diagram[x1 + i, y1 + i] += 1
        else:
            for i in range(x2 - x1 + 1):
                diagram[x1 + i, y2 - i] += 1
    return sum(1 for i in diagram.values() if i > 1)


def part1(lines):
    """
    >>> part1(load_example(__file__, "5"))
    5
    """
    return mark_vents(lines)


def part2(lines):
    """
    >>> part2(load_example(__file__, "5"))
    12
    """
    return mark_vents(lines, diagonals=True)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "5")
    print(part1(data))
    print(part2(data))
