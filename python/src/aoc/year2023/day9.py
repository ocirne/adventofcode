from aoc.util import load_input, load_example


def foo(a):
    if all(n == 0 for n in a):
        return 0
    d = [s - p for p, s in zip(a[:-1], a[1:])]
    print(d)
    return a[-1] + foo(d)


def analyze_pattern(line):
    """
    >>> analyze_pattern('0 3 6 9 12 15')
    18
    >>> analyze_pattern('1 3 6 10 15 21')
    28
    >>> analyze_pattern('10 13 16 21 30 45')
    68
    """
    a = [int(s) for s in line.split()]
    return foo(a)


def part1(lines):
    """
    >>> part1(load_example(__file__, "9"))
    144
    """
    return sum(analyze_pattern(line) for line in lines)


def part2(lines):
    """
    >>> part2(load_example(__file__, "9"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "9")
    print(part1(data))
    # print(part2(data))
