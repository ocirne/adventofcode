from collections import Counter
from itertools import combinations
from pathlib import Path
import disjoint


def run(filename, count):
    a = [i for i in range(count)]
    f = open(filename)
    for line in f.readlines():
        root, children = line.strip().split(' <-> ')
        p = [int(root)] + [int(c) for c in children.split(', ')]
        for i, j in combinations(p, 2):
            disjoint.union(a, i, j)
    # correct canonical elements
    for i in range(count):
        disjoint.find(a, i)
    return a


def part1(filename, count=2000):
    """
    >>> part1(Path(__file__).parent / 'examples/12.txt', 7)
    6
    """
    a = run(filename, count)
    return sum(1 for i in a if i == 0)


def part2(filename, count=2000):
    """
    >>> part2(Path(__file__).parent / 'examples/12.txt', 7)
    2
    """
    a = run(filename, count)
    return len(Counter(a))


if __name__ == '__main__':
    print(part1('inputs/12/input'))
    print(part2('inputs/12/input'))
