from math import prod, sqrt, floor, ceil

from aoc.util import load_input, load_example


def find_best_p(t, d):
    """
    p: press time
    d: distance
    t: time

    p * (t-p) > d
    - p^2 + t * p - d > 0
    a = -1, b = t, c = -d
    p_1 = -b + sqrt(b^2 - 4ac) / 2a

    range: (t - p) - p + 1
    """
    return t - 2 * floor((t - sqrt(t**2 - 4 * d)) / 2) - 1


def part1(lines):
    """
    >>> part1(load_example(__file__, "6"))
    288
    """
    times = [int(t) for t in lines[0].split()[1:]]
    distances = [int(d) for d in lines[1].split()[1:]]
    return prod(find_best_p(t, d) for t, d in zip(times, distances))


def part2(lines):
    """
    >>> part2(load_example(__file__, "6"))
    71503
    """
    t = int(lines[0].replace(" ", "").split(":")[1])
    d = int(lines[1].replace(" ", "").split(":")[1])
    return find_best_p(t, d)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "6")
    print(part1(data))
    print(part2(data))
