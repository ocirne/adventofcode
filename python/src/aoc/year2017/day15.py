from itertools import islice

from aoc.util import load_input


def read_starts_values(lines):
    return (int(lines[i].split()[4]) for i in range(2))


def gen(factor, start):
    value = start
    while True:
        value = value * factor % 2147483647
        yield value & 0xFFFF


def judge1(start_a, start_b):
    """
    >>> judge1(65, 8921)
    588
    """
    ag = gen(16807, start_a)
    bg = gen(48271, start_b)
    return sum(a == b for a, b in islice(zip(ag, bg), 40_000_000))


def judge2(start_a, start_b):
    """
    >>> judge2(65, 8921)
    309
    """
    ag = filter(lambda x: x & 3 == 0, gen(16807, start_a))
    bg = filter(lambda x: x & 7 == 0, gen(48271, start_b))
    return sum(a == b for a, b in islice(zip(ag, bg), 5_000_000))


def part1(lines):
    start_a, start_b = read_starts_values(lines)
    return judge1(start_a, start_b)


def part2(lines):
    start_a, start_b = read_starts_values(lines)
    return judge2(start_a, start_b)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "15")
    print(part1(data))
    print(part2(data))
