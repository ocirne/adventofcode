from aoc.util import example


def prepare_start_grid(lines):
    cube = set()
    for y, line in enumerate(map(str.strip, lines)):
        for x in range(len(line)):
            if line[x] == '#':
                cube.add((x-5, y-5, 0, 0))
    return cube


def count_cells(cube):
    return len(cube)


def count_env(cube, x, y, z, w, dim):
    dw_range = {3: [0], 4: range(-1, 2)}[dim]
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in dw_range:
                    if dx == dy == dz == dw == 0:
                        continue
                    if (x+dx, y+dy, z+dz, w+dw) in cube:
                        count += 1
    return count


def step(i, cube, dim):
    w_range = {3: [0], 4: range(-7-i, 8+i)}[dim]
    result = set()
    for x in range(-7-i, 8+i):
        for y in range(-7-i, 8+i):
            for z in range(-7-i, 8+i):
                for w in w_range:
                    count = count_env(cube, x, y, z, w, dim)
                    coordinates = (x, y, z, w)
                    if coordinates in cube:
                        if 1 < count < 4:
                            result.add(coordinates)
                    else:
                        if count == 3:
                            result.add(coordinates)
    return result


def run(lines, dim):
    """
    >>> run(example(__file__, '17'), 3)
    112
    >>> run(example(__file__, '17'), 4)
    848
    """
    cube = prepare_start_grid(lines)
    for i in range(6):
        cube = step(i, cube, dim)
    return count_cells(cube)


def part1(lines):
    return run(lines, 3)


def part2(lines):
    return run(lines, 4)
