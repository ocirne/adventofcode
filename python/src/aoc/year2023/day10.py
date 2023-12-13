from aoc.util import load_input, load_example


def position_of_s(lines):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                return y, x


M = {
    ("N", "S"): "N",
    ("S", "S"): "S",
    ("N", "|"): "N",
    ("S", "|"): "S",
    ("W", "-"): "W",
    ("E", "-"): "E",
    ("S", "L"): "E",
    ("W", "L"): "N",
    ("S", "J"): "W",
    ("E", "J"): "N",
    ("N", "7"): "W",
    ("E", "7"): "S",
    ("N", "F"): "E",
    ("W", "F"): "S",
}

H = {
    "N": (-1, 0),
    "S": (+1, 0),
    "W": (0, -1),
    "E": (0, +1),
}


def wander(tiles, start_position, direction="S"):
    i = 0
    py, px = start_position
    tile = tiles[py][px]
    while True:
        i += 1
        direction = M[direction, tile]
        dy, dx = H[direction]
        py += dy
        px += dx
        tile = tiles[py][px]
        if tile == "S":
            return i


def part1(lines):
    """
    >>> part1(load_example(__file__, "10a"))
    4
    >>> part1(load_example(__file__, "10b"))
    8
    """
    s = position_of_s(lines)
    return wander(lines, s) // 2


def part2(lines):
    """
    >>> part2(load_example(__file__, "10a"))
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2023, "10")
    print(part1(data))
    # print(part2(data))
