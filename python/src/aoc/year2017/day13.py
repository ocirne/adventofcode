from itertools import count
from aoc.util import load_example, load_input


def prepare_data(lines):
    return ((int(i) for i in line.split(": ")) for line in lines)


def part1(lines):
    """
    >>> part1(load_example(__file__, '13'))
    24
    """
    return sum(d * r for d, r in prepare_data(lines) if 0 == d % ((r - 1) * 2))


def part2(lines):
    """
    >>> part2(load_example(__file__, '13'))
    10
    """
    data = list(prepare_data(lines))
    moduli = [(d, (r - 1) * 2) for d, r in data]
    for i in count():
        if all((d + i) % m != 0 for d, m in moduli):
            return i


if __name__ == "__main__":
    data = load_input(__file__, 2017, "13")
    print(part1(data))
    print(part2(data))
