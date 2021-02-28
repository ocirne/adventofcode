
from collections import defaultdict

from aoc.util import load_input


def turn(d, fun, sxy, exy):
    sx, sy = map(int, sxy.split(','))
    ex, ey = map(int, exy.split(','))
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            d[(x, y)] = fun(d[(x, y)])


def run(data, toogle, turn_on, turn_off):
    grid = defaultdict(lambda: 0)
    for line in data:
        token = line.split()
        if line.startswith('toggle'):
            turn(grid, toogle, token[1], token[3])
        elif line.startswith('turn on'):
            turn(grid, turn_on, token[2], token[4])
        elif line.startswith('turn off'):
            turn(grid, turn_off, token[2], token[4])
        else:
            raise Exception
    return sum(grid.values())


def part1(lines):
    return run(lines, lambda v: not v, lambda _: True, lambda _: False)


def part2(lines):
    return run(lines, lambda x: x + 2, lambda x: x + 1, lambda x: max(0, x - 1))


if __name__ == "__main__":
    data = load_input(__file__, 2015, '6')
    print(part1(data))
    print(part2(data))
