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
    i = 0
    py, px = start_position
    tile = tiles[py][px]
    while True:
        i += 1
        direction, _ = M[direction, tile]
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


def wander2(tiles, start_position, direction="S"):
    i = 0
    py, px = start_position
    tile = tiles[py][px]
    border = set()
    inner_area = set()
    while True:
        i += 1
        direction, ia_pos = M[direction, tile]
        dy, dx = H[direction]
        for ia in ia_pos:
            iy, ix = H[ia]
            inner_area.add((py + iy, px + ix))
        py += dy
        px += dx
        tile = tiles[py][px]
        border.add((py, px))
        if tile == "S":
            return border, inner_area


def neighbors(pos):
    py, px = pos
    return (py - 1, px), (py + 1, px), (py, px - 1), (py, px + 1)


def flooding(border, inner_area):
    open_set = inner_area.difference(border)
    real_inner_area = set()
    while open_set:
        if len(open_set) > 1000:
            return None
        pos = open_set.pop()
        real_inner_area.add(pos)
        for neighbor in neighbors(pos):
            if neighbor in border:
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
    b, ia = wander2(lines, s)
    f = flooding(b, ia)
    if f is not None:
        return len(f)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "10")
    print(part1(data))
    print(part2(data))
