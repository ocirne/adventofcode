from collections import Counter
from itertools import combinations
from aoc.util import load_example, load_input
from aoc.disjoint import find, union


def run(lines, count):
    a = [i for i in range(count)]
    for line in lines:
        root, children = line.strip().split(" <-> ")
        p = [int(root)] + [int(c) for c in children.split(", ")]
        for i, j in combinations(p, 2):
            union(a, i, j)
    # correct canonical elements
    for i in range(count):
        find(a, i)
    return a


def part1(lines, count=2000):
    """
    >>> part1(load_example(__file__, '12'), 7)
    6
    """
    a = run(lines, count)
    return sum(1 for i in a if i == 0)


def part2(lines, count=2000):
    """
    >>> part2(load_example(__file__, '12'), 7)
    2
    """
    a = run(lines, count)
    return len(Counter(a))


if __name__ == "__main__":
    data = load_input(__file__, 2017, "12")
    print(part1(data))
    print(part2(data))
