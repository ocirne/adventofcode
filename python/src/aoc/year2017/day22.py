from collections import defaultdict

from aoc.util import load_example, load_input


def prepare_map(lines):
    result = defaultdict(lambda: ".")
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                result[x, y] = "#"
    return result, (len(lines) - 1) // 2


MOVEMENTS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

CLEAN = "."
WEAKENED = "W"
INFECTED = "#"
FLAGGED = "F"


def part1(lines, n=10000):
    """
    >>> part1(load_example(__file__, "22"), 7)
    5
    >>> part1(load_example(__file__, "22"), 70)
    41
    >>> part1(load_example(__file__, "22"))
    5587
    """
    grid, mxy = prepare_map(lines)
    cx = cy = mxy
    direction = 0
    infection_counter = 0
    for _ in range(n):
        if grid[cx, cy] == "#":
            direction = (direction + 1) % 4
            grid[cx, cy] = "."
        else:
            direction = (direction + 3) % 4
            grid[cx, cy] = "#"
            infection_counter += 1
        dx, dy = MOVEMENTS[direction]
        cx += dx
        cy += dy
    return infection_counter


def part2(lines, n=10000000):
    """
    >>> part2(load_example(__file__, "22"), 100)
    26
    >>> part2(load_example(__file__, "22"))
    2511944
    """
    grid, mxy = prepare_map(lines)
    cx = cy = mxy
    direction = 0
    infection_counter = 0
    for _ in range(n):
        current = grid[cx, cy]
        if current == CLEAN:
            grid[cx, cy] = WEAKENED
            direction = (direction + 3) % 4
        elif current == WEAKENED:
            grid[cx, cy] = INFECTED
            infection_counter += 1
        elif current == INFECTED:
            grid[cx, cy] = FLAGGED
            direction = (direction + 1) % 4
        elif current == FLAGGED:
            grid[cx, cy] = CLEAN
            direction = (direction + 2) % 4
        else:
            raise
        dx, dy = MOVEMENTS[direction]
        cx += dx
        cy += dy
    return infection_counter


if __name__ == "__main__":
    data = load_input(__file__, 2017, "22")
    print(part1(data))
    print(part2(data))
