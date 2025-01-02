from aoc.util import load_input, load_example

import re


def part1(lines):
    """
    >>> part1(load_example(__file__, "4"))
    18
    """
    w, h = len(lines[0]), len(lines)

    ortho = ["" for _ in range(w)]
    for x in range(w):
        for y in range(h):
            ortho[x] += lines[y][x]

    slash = ["" for _ in range(w + h)]
    for x in range(w):
        for y in range(h):
            slash[x + y] += lines[y][w - x - 1]

    backslash = ["" for _ in range(w + h)]
    for x in range(w):
        for y in range(h):
            backslash[x + y] += lines[y][x]

    total = 0
    for line in lines + ortho + slash + backslash:
        total += len(list(re.finditer("XMAS", line)))
        total += len(list(re.finditer("SAMX", line)))

    return total


def part2(lines):
    """
    >>> part2(load_example(__file__, "4"))
    9
    """
    w, h = len(lines[0]), len(lines)

    return sum(
        1
        for x in range(1, w - 1)
        for y in range(1, h - 1)
        if lines[y][x] == "A"
        and lines[y - 1][x - 1] in "SM"
        and lines[y - 1][x + 1] in "SM"
        and lines[y + 1][x - 1] in "SM"
        and lines[y + 1][x + 1] in "SM"
        and lines[y - 1][x - 1] != lines[y + 1][x + 1]
        and lines[y - 1][x + 1] != lines[y + 1][x - 1]
    )


if __name__ == "__main__":
    data = load_input(__file__, 2024, "4")
    print(part1(data))
    print(part2(data))
