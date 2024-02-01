from functools import reduce
from typing import Tuple

from aoc.util import load_input
from sage.all import inverse_mod


def apply_one_line(shuffle_cmd: str, acc: Tuple[int, int], m: int) -> Tuple[int, int]:
    a, b = acc
    if shuffle_cmd == "deal into new stack":
        return (m - a) % m, (m - b - 1) % m
    else:
        n = int(shuffle_cmd.split(" ")[-1])
        if shuffle_cmd.startswith("cut"):
            return a, (b - n + m) % m
        elif shuffle_cmd.startswith("deal with increment"):
            return (n * a) % m, (n * b) % m
        else:
            raise


def shuffle(lines: list[str], initial: Tuple[int, int], m: int) -> Tuple[int, int]:
    return reduce(lambda acc, line: apply_one_line(line, acc, m), lines, initial)


def part1(lines):
    m = 10007
    i = 2019
    a, b = shuffle(lines, (1, 0), m)
    return (a * i + b) % m


def part2(lines):
    m = 119315717514047
    c = 101741582076661
    x = 2020
    a, b = shuffle(lines, (1, 0), m)
    i = inverse_mod(a, m)
    # (x - b) * i % m for c times
    return (x * pow(i, c, m) - b * ((pow(i, c + 1, m) - i) / (i - 1))) % m


if __name__ == "__main__":
    data = load_input(__file__, 2019, "22")
    print(part1(data))
    print(part2(data))
