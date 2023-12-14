from aoc.util import load_input, load_example


def read_data(lines):
    w, h = len(lines[0]), len(lines)
    rocks = {}
    for y, line in enumerate(lines):
        for x, rock in enumerate(line):
            if rock != ".":
                rocks[x, y] = rock
    return w, h, rocks


DIRECTION = {
    "NORTH": (0, -1),
    "WEST": (-1, 0),
    "SOUTH": (0, 1),
    "EAST": (1, 0),
}


def roll_rocks_once(w, h, rocks, direction):
    result = {}
    rolls = 0
    dx, dy = DIRECTION[direction]
    for y in range(h):
        for x in range(w):
            if (x, y) not in rocks:
                continue
            if rocks[x, y] == "#":
                result[x, y] = "#"
            if rocks[x, y] == "O":
                if 0 <= x + dx < w and 0 <= y + dy < h and (x + dx, y + dy) not in rocks:
                    result[x + dx, y + dy] = "O"
                    rolls += 1
                else:
                    result[x, y] = "O"
    return result, rolls


def roll_rocks(w, h, rocks, direction="NORTH"):
    rolls = 1
    while rolls > 0:
        rocks, rolls = roll_rocks_once(w, h, rocks, direction)
    return rocks


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
    rocks = roll_rocks(w, h, rocks)
    return total_load(w, h, rocks)


def spin_cycle(w, h, rocks):
    rocks = roll_rocks(w, h, rocks, "NORTH")
    rocks = roll_rocks(w, h, rocks, "WEST")
    rocks = roll_rocks(w, h, rocks, "SOUTH")
    rocks = roll_rocks(w, h, rocks, "EAST")
    return rocks


def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    64
    """
    total_cycles = 1_000_000_000
    w, h, rocks = read_data(lines)
    i = 1
    seen = {}
    modulo, target = None, None
    while True:
        rocks = spin_cycle(w, h, rocks)
        hashed_rocks = hash(frozenset(rocks.items()))
        if hashed_rocks in seen:
            modulo = i - seen[hashed_rocks]
            target = total_cycles % modulo
        if modulo is not None and i % modulo == target:
            return total_load(w, h, rocks)
        seen[hashed_rocks] = i
        i += 1


if __name__ == "__main__":
    data = load_input(__file__, 2023, "14")
    print(part1(data))
    print(part2(data))
