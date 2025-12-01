from aoc.util import load_input, load_example


def part1_internal(p, signum, delta):
    return p == 0


def part2_internal(p, signum, delta):
    return (-(signum * p) % 100 + delta) // 100


def solve(lines, f):
    p, total = 50, 0
    for line in lines:
        signum = -1 if line[0] == "L" else 1
        delta = int(line[1:])
        p = (p + signum * delta) % 100
        total += f(p, signum, delta)
    return total


def part1(lines):
    """
    >>> part1(load_example(__file__, "1"))
    3
    """
    return solve(lines, part1_internal)


def part2(lines):
    """
    >>> part2(load_example(__file__, "1"))
    6
    """
    return solve(lines, part2_internal)


if __name__ == "__main__":
    data = load_input(__file__, 2025, "1")
    print(part1(data))
    print(part2(data))
