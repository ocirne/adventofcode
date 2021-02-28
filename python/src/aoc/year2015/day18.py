from aoc.util import load_example, load_input


def corners_on(stay_on, grid, size):
    if stay_on:
        grid[(0, 0)] = True
        grid[(0, size - 1)] = True
        grid[(size - 1, 0)] = True
        grid[(size - 1, size - 1)] = True


def prepare_data(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, light in enumerate(line.strip()):
            if light == "#":
                grid[(x, y)] = True
    return grid


def count_neighbors(grid, x, y):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (x + dx, y + dy) in grid:
                count += 1
    return count


def step(before, size, stay_on):
    after = {}
    for x in range(size):
        for y in range(size):
            cn = count_neighbors(before, x, y)
            if (x, y) in before and 2 <= cn <= 3:
                after[(x, y)] = True
            if cn == 3:
                after[(x, y)] = True
    corners_on(stay_on, after, size)
    return after


def run(lines, size, steps, stay_on):
    """
    >>> run(load_example(__file__, '18'), 6, 4, stay_on=False)
    4
    >>> run(load_example(__file__, '18'), 6, 5, stay_on=True)
    17
    """
    data = prepare_data(lines)
    corners_on(stay_on, data, size)
    for _ in range(steps):
        data = step(data, size, stay_on)
    return len(data)


def part1(lines):
    return run(lines, 100, 100, stay_on=False)


def part2(lines):
    return run(lines, 100, 100, stay_on=True)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "18")
    print(part1(data))
    print(part2(data))
