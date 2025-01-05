from aoc.util import load_input, load_example


def inclusive_range(a, b):
    if a < b:
        return range(a, b + 1)
    return range(b, a + 1)


def read_cave(lines):
    cave = set()
    for line in lines:
        pairs = [tuple(map(int, pair.split(","))) for pair in line.split(" -> ")]
        cx, cy = pairs[0]
        for nx, ny in pairs:
            for x in inclusive_range(cx, nx):
                for y in inclusive_range(cy, ny):
                    cave.add((x, y))
            cx, cy = nx, ny
    return cave, max(y for _, y in cave) + 2


def drop_sand(cave, floor_y, with_floor):
    sx, sy = 500, 0
    while True:
        if sy + 1 == floor_y:
            if with_floor:
                return sx, sy
            else:
                return None
        elif (sx, sy + 1) not in cave:
            sy += 1
        elif (sx - 1, sy + 1) not in cave:
            sx, sy = sx - 1, sy + 1
        elif (sx + 1, sy + 1) not in cave:
            sx, sy = sx + 1, sy + 1
        else:
            return sx, sy


def simulate_falling_sand(lines, with_floor, init_count, end_condition):
    cave, floor_y = read_cave(lines)
    count = init_count
    while True:
        p = drop_sand(cave, floor_y, with_floor)
        if end_condition(p):
            return count
        cave.add(p)
        count += 1


def part1(lines):
    """
    >>> part1(load_example(__file__, "14"))
    24
    """
    return simulate_falling_sand(lines, with_floor=False, init_count=0, end_condition=lambda p: p is None)


def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    93
    """
    return simulate_falling_sand(lines, with_floor=True, init_count=1, end_condition=lambda p: p == (500, 0))


if __name__ == "__main__":
    data = load_input(__file__, 2022, "14")
    print(part1(data))
    print(part2(data))
