from aoc.util import load_input, load_example


def deconstruct(line):
    a, b = line.strip().split(",")
    a0, b0 = map(int, a.split("-"))
    a1, b1 = map(int, b.split("-"))
    return a0, b0, a1, b1


def full_overlap(a0, b0, a1, b1):
    return (a0 >= a1 and b0 <= b1) or (a0 <= a1 and b0 >= b1)


def part1(lines):
    """
    >>> part1(load_example(__file__, "4"))
    2
    """
    return sum(full_overlap(*deconstruct(line)) for line in lines)


def partially_overlap(a0, b0, a1, b1):
    return (b0 >= a1 and a0 <= b1) or (b0 <= a1 and a0 >= b1)


def part2(lines):
    """
    >>> part2(load_example(__file__, "4"))
    4
    """
    return sum(partially_overlap(*deconstruct(line)) for line in lines)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "4")
    print(part1(data))
    print(part2(data))
