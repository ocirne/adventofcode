from aoc.util import load_example, load_input


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
    >>> run(load_example(__file__, '6'), result_part1)
    5
    >>> run(load_example(__file__, '6'), result_part2)
    4
    """
    banks = tuple(int(line) for line in lines[0].split())
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


if __name__ == "__main__":
    data = load_input(__file__, 2017, '6')
    print(part1(data))
    print(part2(data))
