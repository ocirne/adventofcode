from operator import xor

from aoc.util import load_input, load_example


def next_row(line, length):
    return [line[1]] + [xor(line[i - 1], line[i + 1]) for i in range(1, length)] + [line[length - 1]]


def trap_field(lines, rows):
    """
    >>> trap_field(load_example(__file__, "18a"), 3)
    6
    >>> trap_field(load_example(__file__, "18b"), 10)
    38
    """
    row = [{".": 0, "^": 1}[c] for c in lines[0].strip()]
    length = len(row)
    total = len(row) * rows
    for i in range(rows):
        total -= sum(row)
        row = next_row(row, length - 1)
    return total


def part1(lines):
    return trap_field(lines, 40)


def part2(lines):
    return trap_field(lines, 400_000)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "18")
    print(part1(data))
    print(part2(data))
