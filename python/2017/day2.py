from itertools import combinations
from pathlib import Path


def diff_max_min(row):
    return row[-1] - row[0]


def whole_division(row):
    return sum(f for f, r in (divmod(number, modulo) for modulo, number in combinations(row, 2)) if r == 0)


def run(lines, fun):
    """
    >>> run(open(Path(__file__).parent / 'examples/2a.txt'), diff_max_min)
    18
    >>> run(open(Path(__file__).parent / 'examples/2b.txt'), whole_division)
    9
    """
    return sum(fun(sorted(int(t) for t in line.split())) for line in lines)


def part1(lines):
    return run(lines, diff_max_min)


def part2(lines):
    return run(lines, whole_division)
