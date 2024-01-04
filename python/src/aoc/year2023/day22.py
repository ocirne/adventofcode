from collections import defaultdict

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


def find_supporting_bricks_count(bricks):
    cube_grid = {}
    for index, (sx, sy, sz, ex, ey, ez) in enumerate(bricks):
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    assert (x, y, z) not in cube_grid
                    cube_grid[x, y, z] = index
    supporting_bricks_count = defaultdict(set)
    for index, (sx, sy, sz, ex, ey, ez) in enumerate(bricks):
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                below = (x, y, sz - 1)
                if below in cube_grid:
                    supporting_bricks_count[index].add(cube_grid[below])
    return supporting_bricks_count


def find_necessary_bricks(bricks):
    return set(next(iter(x)) for x in find_supporting_bricks_count(bricks).values() if len(x) == 1)


def part1(lines):
    """
    >>> part1(load_example(__file__, "22"))
    5
    """
    bricks = list(read_bricks(lines))
    still_falling = True
    while still_falling:
        still_falling, bricks = falling_down(bricks)
    return len(bricks) - len(find_necessary_bricks(bricks))


def find_falling_bricks(look_down, look_up, bottom):
    open_set = {bottom}
    falling_bricks = set()
    while open_set:
        current_brick = open_set.pop()
        if current_brick in falling_bricks:
            continue
        falling_bricks.add(current_brick)
        for next_brick in look_up[current_brick]:
            if next_brick in falling_bricks:
                continue
            if not all(b in falling_bricks for b in look_down[next_brick]):
                continue
            open_set.add(next_brick)
    return len(falling_bricks) - 1


def part2(lines):
    """
    >>> part2(load_example(__file__, "22"))
    7
    """
    bricks = list(read_bricks(lines))
    still_falling = True
    while still_falling:
        still_falling, bricks = falling_down(bricks)
    normal_dict = find_supporting_bricks_count(bricks)
    inverted_dict = defaultdict(set)
    for top, bottoms in normal_dict.items():
        for bottom in bottoms:
            inverted_dict[bottom].add(top)
    return sum(find_falling_bricks(normal_dict, inverted_dict, bottom) for bottom in find_necessary_bricks(bricks))


if __name__ == "__main__":
    print(part1(load_example(__file__, "22")))
    print(part1(load_input(__file__, 2023, "22")))
    print(part2(load_example(__file__, "22")))
    print(part2(load_input(__file__, 2023, "22")))

    # data = load_input(__file__, 2023, "23")
    # print(part1(data))
    # print(part2(data))
