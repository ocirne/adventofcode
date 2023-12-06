from math import prod

from aoc.util import load_input, load_example


def find_best_p(t, d):
    """
    p: press time
    d: distance
    t: time

    p * (t-p) > d
    """
    for p in range(d):
        if p * (t - p) > d:
            #            print(t, d, p, t-p)
            return (t - p) - p + 1


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
    t = int("".join(lines[0].split()[1:]))
    d = int("".join(lines[1].split()[1:]))
    return find_best_p(t, d)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "6")
    print(part1(data))
    print(part2(data))
