from aoc.util import load_input, load_example

from collections import Counter


def read_lists(lines):
    left = []
    right = []
    for line in lines:
        l, r = [int(x) for x in line.split()]
        left.append(l)
        right.append(r)
    return left, right


def part1(lines):
    """
    >>> part1(load_example(__file__, "1"))
    11
    """
    left, right = read_lists(lines)
    return sum(abs(l-r) for l, r in zip(sorted(left), sorted(right)))


def part2(lines):
    """
    >>> part2(load_example(__file__, "1"))
    31
    """
    left, right = read_lists(lines)
    c = Counter(right)
    return sum(x * c[x] for x in left)


if __name__ == "__main__":
    data = load_input(__file__, 2024, "1")
    print(part1(data))
    print(part2(data))
