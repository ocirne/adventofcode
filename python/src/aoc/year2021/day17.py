import re
from collections import defaultdict
from itertools import count, product

from aoc.util import load_input, load_example

PATTERN = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"


def simulate(vx, vy, x1, x2, y1, y2):
    px, py = 0, 0
    max_y = 0
    while True:
        px += vx
        py += vy
        max_y = max(max_y, py)
        vx = max(vx - 1, 0)
        vy -= 1
        if x1 <= px <= x2 and y1 <= py <= y2:
            return max_y
        if x2 < px or py < y1:
            return None
        if vx == 0 and (px < x1 or x2 < px):
            return None


def count_in_target_area(x1, x2, y1, y2):
    target_y = defaultdict(set)
    for start_vy in range(-1100, 1100):
        py = 0
        vy = start_vy
        for step in count(start=1):
            py += vy
            vy -= 1
            if y1 <= py <= y2:
                target_y[step].add(start_vy)
            if py < y1:
                break
    max_steps = max(target_y.keys())
    target_x = defaultdict(set)
    for start_vx in range(x2 + 1):
        px = 0
        vx = start_vx
        for step in count(start=1):
            px += vx
            vx = max(vx - 1, 0)
            if x1 <= px <= x2:
                target_x[step].add(start_vx)
            if x2 < px or max_steps < step:
                break
    max_steps = max(max_steps, max(target_x.keys()))
    all_combinations = []
    for step in range(max_steps + 1):
        all_combinations.extend(product(target_x[step], target_y[step]))
    return len(set(all_combinations))


def part1(lines):
    """
    >>> part1(load_example(__file__, "17"))
    45
    """
    x1, x2, y1, y2 = map(int, re.match(PATTERN, lines[0]).groups())
    #    return two(x1, x2, y1, y2)
    max_y = 0
    for px in range(x2 + 1):
        for py in range(1000):
            y = simulate(px, py, x1, x2, y1, y2)
            if y is not None:
                max_y = max(max_y, y)
    return max_y


def part2(lines):
    """
    >>> part2(load_example(__file__, "17"))
    112
    """
    return count_in_target_area(*map(int, re.match(PATTERN, lines[0]).groups()))


if __name__ == "__main__":
    data = load_input(__file__, 2021, "17")
    #    assert part1(load_example(__file__, "17")) == 45
    #    print(part1(data))
    assert part2(load_example(__file__, "17")) == 112
    print(part2(data))
