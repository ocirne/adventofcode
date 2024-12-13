from aoc.util import load_input, load_example

import re

BUTTON_A_PATTERN = r"Button A: X\+(\d+), Y\+(\d+)"
BUTTON_B_PATTERN = r"Button B: X\+(\d+), Y\+(\d+)"
PRIZE_PATTERN = r"Prize: X=(\d+), Y=(\d+)"


def calculate_cost(ax, ay, bx, by, px, py):
    b = (ay * px - ax * py) / (ay * bx - ax * by)
    a = (px - b * bx) / ax
    return int(b + 3 * a) if 0 < a == int(a) and 0 < b == int(b) else 0


def press_buttons(lines, offset=0):
    total = 0
    for line in lines:
        a = re.search(BUTTON_A_PATTERN, line)
        if a:
            ax, ay = map(int, a.groups())
        b = re.search(BUTTON_B_PATTERN, line)
        if b:
            bx, by = map(int, b.groups())
        p = re.search(PRIZE_PATTERN, line)
        if p:
            px, py = map(int, p.groups())
            total += calculate_cost(ax, ay, bx, by, px + offset, py + offset)
    return total


def part1(lines):
    """
    >>> part1(load_example(__file__, "13"))
    480
    """
    return press_buttons(lines)


def part2(lines):
    return press_buttons(lines, 10000000000000)


if __name__ == "__main__":
    data = load_input(__file__, 2024, "13")
    print(part1(data))
    print(part2(data))
