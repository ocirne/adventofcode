import re
from collections import defaultdict

from aoc.util import load_input, load_example

PATTERN = r"(\d+),(\d+) -> (\d+),(\d+)"


def part1(lines):
    """
    >>> part1(load_example(__file__, "5"))
    5
    """
    diagram = defaultdict(lambda: 0)
    for line in lines:
        x1, y1, x2, y2 = map(int, re.match(PATTERN, line).groups())
        if x1 == x2 and y1 == y2:
            diagram[x1, y1] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                diagram[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                diagram[x, y1] += 1
        else:
            ...
    print(sum(1 for i in diagram.values() if i > 1))


if __name__ == "__main__":
    data = load_input(__file__, 2021, "5")
    print(part1(data))
