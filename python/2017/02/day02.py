from itertools import combinations
from pathlib import Path


def read_lines(filename):
    f = open(filename, "r")
    return f.readlines()


def diff_max_min(row):
    return row[-1] - row[0]


def whole_division(row):
    return sum(f for f, r in (divmod(number, modulo) for modulo, number in combinations(row, 2)) if r == 0)


def run(filename, fun):
    """
    >>> run(Path(__file__).parent / 'reference_a', diff_max_min)
    18
    >>> run(Path(__file__).parent / 'reference_b', whole_division)
    9
    """
    lines = read_lines(filename)
    return sum(fun(sorted(int(t) for t in line.split())) for line in lines)


if __name__ == "__main__":
    print(run("input", diff_max_min))
    print(run("input", whole_division))
