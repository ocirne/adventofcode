from sage.all import CRT_list
import re

from aoc.util import load_input, load_example

PATTERN = r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)\."


def drop_disc(lines, extra_disc=None):
    values = []
    moduli = []
    for line in lines:
        no, modulo, _, start = map(int, re.match(PATTERN, line).groups())
        moduli.append(modulo)
        values.append(-start - no)
    if extra_disc is not None:
        moduli.append(extra_disc[0])
        values.append(-extra_disc[1])
    return CRT_list(values, moduli)


def part1(lines):
    """
    >>> part1(load_example(__file__, '15'))
    5
    """
    return drop_disc(lines)


def part2(lines):
    return drop_disc(lines, (11, 7))


if __name__ == "__main__":
    data = load_input(__file__, 2016, "15")
    print(part1(data))
    print(part2(data))
