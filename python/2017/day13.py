from itertools import count
from aoc_util import example


def prepare_data(lines):
    return ((int(i) for i in line.split(': ')) for line in lines)


def part1(lines):
    """
    >>> part1(example('13'))
    24
    """
    return sum(d*r for d, r in prepare_data(lines) if 0 == d % ((r - 1)*2))


def part2(lines):
    """
    >>> part2(example('13'))
    10
    """
    data = list(prepare_data(lines))
    moduli = [(d, (r-1)*2) for d, r in data]
    for i in count():
        if all((d+i) % m != 0 for d, m in moduli):
            return i
