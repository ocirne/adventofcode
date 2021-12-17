import re
from collections import defaultdict
from itertools import count, product

from aoc.util import load_input, load_example

PATTERN = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"


def count_in_target_area(line):
    x1, x2, y1, y2 = map(int, re.match(PATTERN, line).groups())
    target_y = defaultdict(set)
    total_max_y = 0
    for start_vy in range(-1100, 1100):
        py = 0
        max_y = 0
        vy = start_vy
        for step in count(start=1):
            py += vy
            max_y = max(max_y, py)
            vy -= 1
            if y1 <= py <= y2:
                target_y[step].add(start_vy)
                total_max_y = max(total_max_y, max_y)
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
    return total_max_y, len(set(all_combinations))


def part1(lines):
    """
    >>> part1(load_example(__file__, "17"))
    45
    """
    return count_in_target_area(lines[0])[0]


def part2(lines):
    """
    >>> part2(load_example(__file__, "17"))
    112
    """
    return count_in_target_area(lines[0])[1]


if __name__ == "__main__":
    data = load_input(__file__, 2021, "17")
    print(part1(data))
    print(part2(data))
