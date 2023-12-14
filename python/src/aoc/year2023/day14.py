from aoc.util import load_input, load_example


def read_data(lines):
    w, h = len(lines[0]), len(lines)
    rocks = {}
    for y, line in enumerate(lines):
        for x, rock in enumerate(line):
            if rock != ".":
                rocks[x, y] = rock
    return w, h, rocks


def roll_rocks_north_once(w, h, rocks):
    result = {}
    rolls = 0
    for y in range(h):
        for x in range(w):
            if (x, y) not in rocks:
                continue
            if rocks[x, y] == "#":
                result[x, y] = "#"
            if rocks[x, y] == "O":
                if y > 0 and (x, y - 1) not in rocks:
                    result[x, y - 1] = "O"
                    rolls += 1
                else:
                    result[x, y] = "O"
    return result, rolls


def total_load(w, h, rocks):
    result = 0
    for y in range(h):
        for x in range(w):
            if rocks.get((x, y), None) == "O":
                result += h - y
    return result


def part1(lines):
    """
    >>> part1(load_example(__file__, "14"))
    136
    """
    w, h, rocks = read_data(lines)
    rolls = 1
    while rolls > 0:
        rocks, rolls = roll_rocks_north_once(w, h, rocks)
        print(rolls)
    return total_load(w, h, rocks)


def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    ...
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2023, "14")
    # data = load_example(__file__, "14")
    print(part1(data))
    # print(part2(data))
