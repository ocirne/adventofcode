from itertools import count
from pathlib import Path


def read_data(filename):
    f = open(filename)
    return ((int(i) for i in line.split(': ')) for line in f)


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    24
    """
    return sum(d*r for d, r in read_data(filename) if 0 == d % ((r - 1)*2))


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    10
    """
    data = list(read_data(filename))
    moduli = [(d, (r-1)*2) for d, r in data]
    for i in count():
        if all((d+i) % m != 0 for d, m in moduli):
            return i


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
