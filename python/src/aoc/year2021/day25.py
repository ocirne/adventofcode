from collections import defaultdict

from aoc.util import load_input, load_example


def move_herd(old_cucumbers, width, height, moving_herd, other_herd, fun):
    next_cucumbers = defaultdict(lambda: ".")
    changes = False
    for y in range(height):
        for x in range(width):
            value = old_cucumbers[x, y]
            if value == moving_herd:
                if old_cucumbers[fun(x, y)] == ".":
                    next_cucumbers[fun(x, y)] = moving_herd
                    changes = True
                else:
                    next_cucumbers[x, y] = moving_herd
            elif value == other_herd:
                next_cucumbers[x, y] = value
    return changes, next_cucumbers


def step(c0, width, height):
    changes_east, c1 = move_herd(c0, width, height, ">", "v", lambda x, y: ((x + 1) % width, y))
    changes_south, c2 = move_herd(c1, width, height, "v", ">", lambda x, y: (x, (y + 1) % height))
    return changes_east or changes_south, c2


def read_cucumbers(lines):
    cucumbers = defaultdict(lambda: ".")
    width = len(lines[0])
    height = len(lines)
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            cucumbers[x, y] = value
    return cucumbers, width, height


def part1(lines):
    """
    >>> part1(load_example(__file__, "25b"))
    58
    """
    cucumbers, width, height = read_cucumbers(lines)
    steps = 1
    while True:
        changes, cucumbers = step(cucumbers, width, height)
        if changes == 0:
            return steps
        steps += 1


def part2(lines): ...


if __name__ == "__main__":
    assert part1(load_example(__file__, "25b")) == 58
    data = load_input(__file__, 2021, "25")
    print(part1(data))
