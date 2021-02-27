from itertools import count
from pathlib import Path


def prepare_data(lines):
    return ((int(i) for i in line.split(': ')) for line in lines)


def part1(lines):
    """
    >>> part1(open(Path(__file__).parent / 'examples/13.txt'))
    24
    """
    return sum(d*r for d, r in prepare_data(lines) if 0 == d % ((r - 1)*2))


def part2(lines):
    """
    >>> part2(open(Path(__file__).parent / 'examples/13.txt'))
    10
    """
    data = list(prepare_data(lines))
    moduli = [(d, (r-1)*2) for d, r in data]
    for i in count():
        if all((d+i) % m != 0 for d, m in moduli):
            return i
