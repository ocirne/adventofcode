
from collections import defaultdict


def turn(d, fun, sxy, exy):
    sx, sy = map(int, sxy.split(','))
    ex, ey = map(int, exy.split(','))
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            d[(x, y)] = fun(d[(x, y)])


def run(filename):
    f = open(filename, 'r')
    grid = defaultdict(lambda: False)
    for line in f.readlines():
        token = line.split()
        if line.startswith('toggle'):
            turn(grid, lambda v: not v, token[1], token[3])
        elif line.startswith('turn on'):
            turn(grid, lambda _: True, token[2], token[4])
        elif line.startswith('turn off'):
            turn(grid, lambda _: False, token[2], token[4])
        else:
            raise Exception
    return sum(grid.values())


print(run('input'))

from collections import defaultdict


def turn(d, fun, sxy, exy):
    sx, sy = map(int, sxy.split(','))
    ex, ey = map(int, exy.split(','))
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            d[(x, y)] = fun(d[(x, y)])


def run(filename):
    f = open(filename, 'r')
    grid = defaultdict(lambda: 0)
    for line in f.readlines():
        token = line.split()
        if line.startswith('toggle'):
            turn(grid, lambda x: x + 2, token[1], token[3])
        elif line.startswith('turn on'):
            turn(grid, lambda x: x + 1, token[2], token[4])
        elif line.startswith('turn off'):
            turn(grid, lambda x: max(0, x - 1), token[2], token[4])
        else:
            raise Exception
    return sum(grid.values())


print(run('input'))
