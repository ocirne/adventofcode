from pathlib import Path


def redistribute(banks):
    value = max(banks)
    index = banks.index(value)
    result = list(banks)
    result[index] = 0
    for i in range(value):
        result[(index + 1 + i) % len(banks)] += 1
    return tuple(result)


# noinspection PyUnusedLocal
def part1(second, first):
    return second


def part2(second, first):
    return second - first


def run(filename, result):
    """
    >>> run(Path(__file__).parent / 'reference', part1)
    5
    >>> run(Path(__file__).parent / 'reference', part2)
    4
    """
    banks = tuple(int(line) for line in open(filename).readline().split())
    known = {}
    count = 1
    while True:
        banks = redistribute(banks)
        if banks in known:
            return result(count, known[banks])
        known[banks] = count
        count += 1


if __name__ == '__main__':
    print(run('input', part1))
    print(run('input', part2))
