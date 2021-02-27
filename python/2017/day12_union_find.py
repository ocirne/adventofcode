from collections import Counter
from itertools import combinations
from aoc_util import example
import disjoint


def run(lines, count):
    a = [i for i in range(count)]
    for line in lines:
        root, children = line.strip().split(' <-> ')
        p = [int(root)] + [int(c) for c in children.split(', ')]
        for i, j in combinations(p, 2):
            disjoint.union(a, i, j)
    # correct canonical elements
    for i in range(count):
        disjoint.find(a, i)
    return a


def part1(lines, count=2000):
    """
    >>> part1(example('12'), 7)
    6
    """
    a = run(lines, count)
    return sum(1 for i in a if i == 0)


def part2(lines, count=2000):
    """
    >>> part2(example('12'), 7)
    2
    """
    a = run(lines, count)
    return len(Counter(a))
