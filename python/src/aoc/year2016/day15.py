from sage.all import CRT_list
import re

from aoc.util import load_input, load_example

PATTERN = r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)\."


def part1(lines):
    """
    >>> part1(load_example(__file__, '15'))
    5
    """
    values = []
    moduli = []
    for line in lines:
        no, modulo, time, value = map(int, re.match(PATTERN, line).groups())
        moduli.append(modulo)
        values.append(-value - no)
    return CRT_list(values, moduli)


def part2(lines):
    """
    >>> part2(load_example(__file__, '15'))
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2016, "15")
    assert part1(load_example(__file__, "15")) == 5
    print(part1(data))
    print(part2(data))
