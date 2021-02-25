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


if __name__ == '__main__':
    print(part1('input'))
