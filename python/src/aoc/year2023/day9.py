from aoc.util import load_input, load_example


def next_value(a, d):
    return a[-1] + rec(d, next_value)


def previous_value(a, d):
    return a[0] - rec(d, previous_value)


def rec(a, f):
    if all(n == 0 for n in a):
        return 0
    d = [s - p for p, s in zip(a[:-1], a[1:])]
    return f(a, d)


def sum_adjacent_values(lines, f):
    """
    >>> sum_adjacent_values(['0 3 6 9 12 15'], next_value)
    18
    >>> sum_adjacent_values(['1 3 6 10 15 21'], next_value)
    28
    >>> sum_adjacent_values(['10 13 16 21 30 45'], next_value)
    68
    >>> sum_adjacent_values(['0 3 6 9 12 15'], previous_value)
    -3
    >>> sum_adjacent_values(['1 3 6 10 15 21'], previous_value)
    0
    >>> sum_adjacent_values(['10 13 16 21 30 45'], previous_value)
    5
    """
    return sum(rec(list(map(int, line.split())), f) for line in lines)


def part1(lines):
    """
    >>> part1(load_example(__file__, "9"))
    114
    """
    return sum_adjacent_values(lines, next_value)


def part2(lines):
    """
    >>> part2(load_example(__file__, "9"))
    2
    """
    return sum_adjacent_values(lines, previous_value)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "9")
    print(part1(data))
    print(part2(data))
