from aoc.util import load_input, load_example
import re

BRICK_PATTERN = r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)"


def read_bricks(lines):
    for index, line in enumerate(lines):
        m = re.match(BRICK_PATTERN, line)
        sx, sy, sz, ex, ey, ez = map(int, m.groups())
        assert 0 <= sx <= ex and 0 <= sy <= ey and 0 < sz <= ez
        yield sx, sy, sz, ex, ey, ez


def falling_down(bricks):
    cube_grid = set()
    for sx, sy, sz, ex, ey, ez in bricks:
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    assert (x, y, z) not in cube_grid
                    cube_grid.add((x, y, z))
    still_falling = False
    new_bricks = []
    for sx, sy, sz, ex, ey, ez in bricks:
        delta = 0
        while sz - delta > 1 and all(
            (x, y, sz - (delta + 1)) not in cube_grid for x in range(sx, ex + 1) for y in range(sy, ey + 1)
        ):
            delta += 1
        if delta > 0:
            still_falling = True
        new_bricks.append((sx, sy, sz - delta, ex, ey, ez - delta))
    return still_falling, new_bricks


def find_necessary_bricks(bricks):
    cube_grid = {}
    for index, (sx, sy, sz, ex, ey, ez) in enumerate(bricks):
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    assert (x, y, z) not in cube_grid
                    cube_grid[x, y, z] = index
    necessary_bricks = set()
    for index, (sx, sy, sz, ex, ey, ez) in enumerate(bricks):
        supporting_bricks = set()
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if (x, y, sz - 1) in cube_grid:
                    supporting_bricks.add(cube_grid[x, y, sz - 1])
        print(index, "is supported by", len(supporting_bricks))
        if len(supporting_bricks) == 1:
            necessary_bricks.update(supporting_bricks)
    return necessary_bricks


def part1(lines):
    """
    >>> part1(load_example(__file__, "22"))
    5
    """
    bricks = list(read_bricks(lines))
    still_falling = True
    while still_falling:
        still_falling, bricks = falling_down(bricks)
    for x in bricks:
        print(x)
    return len(bricks) - len(find_necessary_bricks(bricks))


def part2(lines):
    """
    >>> part2(load_example(__file__, "22"))
    """


if __name__ == "__main__":
    # print(part1(load_example(__file__, "22")))
    print(part1(load_input(__file__, 2023, "22")))

    # data = load_input(__file__, 2023, "23")
    # print(part1(data))
    # print(part2(data))
