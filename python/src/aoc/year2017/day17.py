from aoc.util import load_input
from collections import deque


def part1(lines):
    """
    >>> part1(['3'])
    638
    """
    steps = int(lines[0])
    path = deque()
    path.append(0)
    current = 0
    for i in range(1, 2018):
        current = (current + 1 + steps) % len(path)
        path.insert(current + 1, i)
    pos2017 = path.index(2017)
    return path[pos2017 + 1]


if __name__ == "__main__":
    data = load_input(__file__, 2017, "17")
    print(part1(data))
