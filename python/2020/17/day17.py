from collections import defaultdict
from pathlib import Path


def read_start_grid(filename):
    f = open(filename)
    cube = defaultdict(lambda: '.')
    for y, line in enumerate(map(str.strip, f.readlines())):
        for x in range(len(line)):
            cube[(x-5, y-5, 0, 0)] = line[x]
    return cube


def count_cells(cube):
    return sum(1 for value in cube.values() if value == '#')


def count_env(cube, x, y, z, w, dim):
    dw_range = {3: [0], 4: range(-1, 2)}[dim]
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in dw_range:
                    if dx == dy == dz == dw == 0:
                        continue
                    if cube[(x+dx, y+dy, z+dz, w+dw)] == '#':
                        count += 1
    return count


def step(i, cube, dim):
    w_range = {3: [0], 4: range(-7-i, 8+i)}[dim]
    result = defaultdict(lambda: '.')
    for x in range(-7-i, 8+i):
        for y in range(-7-i, 8+i):
            for z in range(-7-i, 8+i):
                for w in w_range:
                    count = count_env(cube, x, y, z, w, dim)
                    coordinates = (x, y, z, w)
                    if cube[coordinates] == '#' and 1 < count < 4:
                        result[coordinates] = '#'
                    elif cube[coordinates] == '.' and count == 3:
                        result[coordinates] = '#'
    return result


def run(filename, dim):
    """
    >>> run(Path(__file__).parent / 'reference', 3)
    112
    >>> run(Path(__file__).parent / 'reference', 4)
    848
    """
    cube = read_start_grid(filename)
    for i in range(6):
        cube = step(i, cube, dim)
    return count_cells(cube)


if __name__ == '__main__':
    print(run('input', 3))
    print(run('input', 4))
