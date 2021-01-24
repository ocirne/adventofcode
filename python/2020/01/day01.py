from pathlib import Path

M = 2020


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    514579
    """
    data = open(filename, 'r').readlines()
    d = {int(s) for s in data}
    for x in d:
        y = M - x
        if y in d:
            return x * y


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    241861950
    """
    data = open(filename, 'r').readlines()
    d = [int(s) for s in data]
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


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
