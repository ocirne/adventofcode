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
def result_part1(second, first):
    return second


def result_part2(second, first):
    return second - first


def run(lines, result):
    """
    >>> run(open(Path(__file__).parent / 'examples/6.txt'), result_part1)
    5
    >>> run(open(Path(__file__).parent / 'examples/6.txt'), result_part2)
    4
    """
    banks = tuple(int(line) for line in next(lines).split())
    known = {}
    count = 1
    while True:
        banks = redistribute(banks)
        if banks in known:
            return result(count, known[banks])
        known[banks] = count
        count += 1


def part1(lines):
    return run(lines, result_part1)


def part2(lines):
    return run(lines, result_part2)
