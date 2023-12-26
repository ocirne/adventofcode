from itertools import combinations

from aoc.util import load_input, load_example

LB, UB = 200_000_000_000_000, 400_000_000_000_000


def read_vectors(lines):
    for line in lines:
        p, v = line.split("@")
        px, py, pz = map(int, p.split(","))
        vx, vy, vz = map(int, v.split(","))
        yield px, py, vx, vy


def cross_point(v1, v2):
    """
    # ax + a * vx == bx + b * wx
    # ay + a * vy == by + b * wy
    """
    ax, ay, vx, vy = v1
    bx, by, wx, wy = v2
    # parallel?
    if vx * wy == vy * wx:
        print(v1, v2, "-> parallel")
        return False
    n = vx * wy - vy * wx
    a = (wy * (bx - ax) + wx * (ay - by)) / n
    if a < 0:
        return False
    b = (vx * (ay - by) + vy * (bx - ax)) / n
    if b < 0:
        return False
    cx, cy = ax + a * vx, ay + a * vy
    return LB <= cx <= UB and LB <= cy <= UB


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    2
    """
    vectors = list(read_vectors(lines))
    return sum(cross_point(v1, v2) for v1, v2 in combinations(vectors, 2))


def part2(lines):
    """
    >>> part2(load_example(__file__, "24"))
    """


if __name__ == "__main__":
    # print(part1(load_example(__file__, "24")))
    data = load_input(__file__, 2023, "24")
    print(part1(data))
    # print(part2(data))
