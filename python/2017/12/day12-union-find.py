from collections import Counter
from itertools import combinations
from pathlib import Path


def find(a, x):
    if a[x] == x:
        return x
    a[x] = find(a, a[x])
    return a[x]


def union(a, x, y):
    i = find(a, x)
    j = find(a, y)
    if i == j:
        return
    if i < j:
        (i, j) = (j, i)
    a[i] = j


def run(filename, count):
    a = [i for i in range(count)]
    f = open(filename, 'r')
    for line in f.readlines():
        root, children = line.strip().split(' <-> ')
        p = [int(root)] + [int(c) for c in children.split(', ')]
        for i, j in combinations(p, 2):
            union(a, i, j)
    # correct canonical elements
    for i in range(count):
        find(a, i)
    return a


def part1(filename, count=2000):
    """
    >>> part1(Path(__file__).parent / 'reference', 7)
    6
    """
    a = run(filename, count)
    return sum(1 for i in a if i == 0)


def part2(filename, count=2000):
    """
    >>> part2(Path(__file__).parent / 'reference', 7)
    2
    """
    a = run(filename, count)
    return len(Counter(a))


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
