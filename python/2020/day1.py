from aoc_util import example

M = 2020


def part1(lines):
    """
    >>> part1(example('1'))
    514579
    """
    d = {int(s) for s in lines}
    for x in d:
        y = M - x
        if y in d:
            return x * y


def part2(lines):
    """
    >>> part2(example('1'))
    241861950
    """
    d = [int(s) for s in lines]
    p = {}
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            key = d[i] + d[j]
            if key < M:
                p[key] = d[i] * d[j]
    for x in d:
        y = M - x
        if y in p:
            return x * p[y]
