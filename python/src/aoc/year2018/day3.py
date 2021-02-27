from collections import defaultdict
from aoc.util import example


def part1(lines):
    """
    >>> part1(example(__file__, '3'))
    4
    """
    d = defaultdict(lambda: 0)
    for line in lines:
        number, _, pos, size = line.split(' ')
        x, y = map(int, pos.split(':')[0].split(','))
        w, h = map(int, size.split('\n')[0].split('x'))
        for i in range(x, x + w):
            for j in range(y, y + h):
                d[(i, j)] += 1
    return sum(1 for i in d.values() if i > 1)


def part2(lines):
    """
    >>> part2(example(__file__, '3'))
    3
    """
    all_numbers = {}
    d = {}
    for line in lines:
        number, _, pos, size = line.split(' ')
        n = int(number.split('#')[1])
        x, y = map(int, pos.split(':')[0].split(','))
        w, h = map(int, size.split('\n')[0].split('x'))
        all_numbers[n] = True

        for i in range(x, x + w):
            for j in range(y, y + h):
                key = (i, j)
                if key in d:
                    all_numbers[n] = False
                    all_numbers[d[key]] = False
                else:
                    d[key] = n

    for n, condition in all_numbers.items():
        if condition:
            return n
