from aoc.util import load_input, load_example


def read_garden(lines):
    garden, s = {}, None
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            garden[x, y] = v
            if v == "S":
                s = x, y
    return garden, s


def neighbors(garden, x, y):
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if (nx, ny) in garden and garden[nx, ny] != "#":
            yield nx, ny


def foo(garden, start, max_steps):
    steps = {start}
    for _ in range(max_steps):
        print(len(steps), max_steps)
        new_steps = set()
        for cx, cy in steps:
            for nx, ny in neighbors(garden, cx, cy):
                new_steps.add((nx, ny))
        steps = new_steps
    return len(steps)


def part1(lines, steps=64):
    """
    >>> part1(load_example(__file__, "21"), steps=6)
    16
    """
    garden, start = read_garden(lines)
    return foo(garden, start, steps)


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    """


if __name__ == "__main__":
    print(part1(load_example(__file__, "21"), steps=6))
    data = load_input(__file__, 2023, "21")
    print(part1(data))
    # print(part2(data))
