from pathlib import Path


def corners_on(stay_on, grid, size):
    if stay_on:
        grid[(0, 0)] = True
        grid[(0, size-1)] = True
        grid[(size-1, 0)] = True
        grid[(size-1, size-1)] = True


def read_data(filename):
    grid = {}
    f = open(filename)
    for y, line in enumerate(f.readlines()):
        for x, light in enumerate(line.strip()):
            if light == '#':
                grid[(x, y)] = True
    return grid


def count_neighbors(grid, x, y):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (x+dx, y+dy) in grid:
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


def run(filename, size, steps, stay_on):
    """
    >>> run(Path(__file__).parent / 'reference', 6, 4, stay_on=False)
    4
    >>> run(Path(__file__).parent / 'reference', 6, 5, stay_on=True)
    17
    """
    data = read_data(filename)
    corners_on(stay_on, data, size)
    for _ in range(steps):
        data = step(data, size, stay_on)
    return len(data)


if __name__ == '__main__':
    print(run('input', 100, 100, stay_on=False))
    print(run('input', 100, 100, stay_on=True))
