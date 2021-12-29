from collections import defaultdict

from aoc.util import load_input, load_example


def step(old_cucumbers, width, height):
    next_cucumbers = defaultdict(lambda: ".")
    changes = 0
    for y in range(height):
        for x in range(width):
            value = old_cucumbers[x, y]
            if value == ">":
                if old_cucumbers[(x + 1) % width, y] == ".":
                    next_cucumbers[(x + 1) % width, y] = ">"
                    changes += 1
                else:
                    next_cucumbers[x, y] = ">"
            elif value == "v":
                next_cucumbers[x, y] = value

    next_cucumbers2 = defaultdict(lambda: ".")
    for y in range(height):
        for x in range(width):
            value = next_cucumbers[x, y]
            if value == "v":
                if next_cucumbers[x, (y + 1) % height] == ".":
                    next_cucumbers2[x, (y + 1) % height] = "v"
                    changes += 1
                else:
                    next_cucumbers2[x, y] = "v"
            elif value == ">":
                next_cucumbers2[x, y] = value

    return changes, next_cucumbers2


def part1(lines):
    """
    >>> part1(load_example(__file__, "25b"))
    58
    """
    cucumbers = defaultdict(lambda: ".")
    width = len(lines[0].strip())
    height = len(lines)
    for y, line in enumerate(lines):
        for x, value in enumerate(line.strip()):
            cucumbers[x, y] = value
    steps = 1
    while True:
        changes, cucumbers = step(cucumbers, width, height)
        if changes == 0:
            return steps
        steps += 1


def part2(lines):
    ...


if __name__ == "__main__":
    assert part1(load_example(__file__, "25b")) == 58
    data = load_input(__file__, 2021, "25")
    print(part1(data))
