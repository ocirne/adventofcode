from aoc.util import load_input, load_example

from math import log10
from functools import lru_cache


@lru_cache(maxsize=None)
def recursive_blink(s, d):
    if d == 0:
        return 1
    if s == 0:
        return recursive_blink(1, d - 1)
    hl, r = divmod(int(log10(s)) + 1, 2)
    if r == 0:
        first, second = divmod(s, 10**hl)
        return recursive_blink(first, d - 1) + recursive_blink(second, d - 1)
    return recursive_blink(2024 * s, d - 1)


def bar(line, blinks):
    return sum(recursive_blink(int(s), blinks) for s in line.split())


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    55312
    """
    return bar(lines[0], 25)


def part2(lines):
    return bar(lines[0], 75)


if __name__ == "__main__":
    data = load_input(__file__, 2024, "11")
    print(part1(data))
    print(part2(data))
