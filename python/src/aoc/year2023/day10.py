from aoc.util import load_input, load_example


def position_of_s(lines):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                return y, x


M = {
    ("N", "S"): ("N", "E"),
    ("S", "S"): ("S", "W"),
    ("N", "|"): ("N", "E"),
    ("S", "|"): ("S", "W"),
    ("W", "-"): ("W", "N"),
    ("E", "-"): ("E", "S"),
    ("S", "L"): ("E", "WS"),
    ("W", "L"): ("N", ""),
    ("S", "J"): ("W", ""),
    ("E", "J"): ("N", "SE"),
    ("N", "7"): ("W", "EN"),
    ("E", "7"): ("S", ""),
    ("N", "F"): ("E", ""),
    ("W", "F"): ("S", "NW"),
}

H = {
    "N": (-1, 0),
    "S": (+1, 0),
    "W": (0, -1),
    "E": (0, +1),
}


def wander(tiles, start_position, direction="S"):
    py, px = start_position
    tile = tiles[py][px]
    loop = set()
    inner_border = set()
    while True:
        direction, inner_border_positions = M[direction, tile]
        dy, dx = H[direction]
        for ibp in inner_border_positions:
            iy, ix = H[ibp]
            inner_border.add((py + iy, px + ix))
        py += dy
        px += dx
        tile = tiles[py][px]
        loop.add((py, px))
        if tile == "S":
            return loop, inner_border


def part1(lines):
    """
    >>> part1(load_example(__file__, "10a"))
    4
    >>> part1(load_example(__file__, "10b"))
    8
    """
    s = position_of_s(lines)
    loop, _ = wander(lines, s)
    return len(loop) // 2


def neighbors(pos):
    py, px = pos
    return (py - 1, px), (py + 1, px), (py, px - 1), (py, px + 1)


def flooding(loop, inner_border):
    open_set = inner_border.difference(loop)
    real_inner_area = set()
    while open_set:
        if len(open_set) > 1000:
            # oops, outer area
            return None
        pos = open_set.pop()
        real_inner_area.add(pos)
        for neighbor in neighbors(pos):
            if neighbor in loop:
                continue
            if neighbor in real_inner_area:
                continue
            open_set.add(neighbor)
    return real_inner_area


def part2(lines):
    """
    >>> part2(load_example(__file__, "10d"))
    8
    >>> part2(load_example(__file__, "10e"))
    10
    """
    s = position_of_s(lines)
    loop, inner_border = wander(lines, s)
    return len(flooding(loop, inner_border))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "10")
    print(part1(data))
    print(part2(data))
