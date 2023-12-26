from itertools import combinations

from aoc.util import load_input, load_example

LB, UB = 200_000_000_000_000, 400_000_000_000_000


def read_vectors1(lines):
    for line in lines:
        p, v = line.split("@")
        px, py, pz = map(int, p.split(","))
        vx, vy, vz = map(int, v.split(","))
        yield px, py, vx, vy


def cross_point(v1, v2, lb, ub):
    """
    # ax + a * vx == bx + b * wx == cx
    # ay + a * vy == by + b * wy == cy
    """
    ax, ay, vx, vy = v1
    bx, by, wx, wy = v2
    # parallel?
    if vx * wy == vy * wx:
        return False
    n = vx * wy - vy * wx
    a = (wy * (bx - ax) + wx * (ay - by)) / n
    if a < 0:
        return False
    b = (vx * (ay - by) + vy * (bx - ax)) / n
    if b < 0:
        return False
    cx, cy = ax + a * vx, ay + a * vy
    return lb <= cx <= ub and lb <= cy <= ub


def part1(lines, lb=LB, ub=UB):
    """
    >>> part1(load_example(__file__, "24"), lb=7, ub=27)
    2
    """
    vectors = read_vectors1(lines)
    return sum(cross_point(v1, v2, lb, ub) for v1, v2 in combinations(vectors, 2))


def read_vectors2(lines):
    for line in lines:
        p, v = line.split("@")
        px, py, pz = map(int, p.split(","))
        vx, vy, vz = map(int, v.split(","))
        yield px, py, pz, vx, vy, vz


def part2(lines):
    """
    >>> part2(load_example(__file__, "24"))
    47
    """
    vectors = list(read_vectors1(lines))
    for v in vectors:
        print(v)


if __name__ == "__main__":
    print(part2(load_example(__file__, "24")))
    # data = load_input(__file__, 2023, "24")
    # print(part1(data))
    # print(part2(data))
