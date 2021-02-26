from collections import defaultdict
from pathlib import Path


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    4
    """
    data = open(filename).readlines()
    d = defaultdict(lambda: 0)
    for line in data:
        number, _, pos, size = line.split(' ')
        x, y = map(int, pos.split(':')[0].split(','))
        w, h = map(int, size.split('\n')[0].split('x'))
        for i in range(x, x + w):
            for j in range(y, y + h):
                d[(i, j)] += 1
    return sum(1 for i in d.values() if i > 1)


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    3
    """
    data = open(filename).readlines()
    all_numbers = {}
    d = {}
    for line in data:
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


if __name__ == "__main__":
    print(part1("input"))
    print(part2("input"))
