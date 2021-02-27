from collections import Counter

from aoc.disjoint import find, union
from aoc.year2017 import knots


def get_grid(key):
    return [binary_knot_hash(key, i) for i in range(128)]


def binary_knot_hash(key, i):
    hash_input = '%s-%s' % (key, i)
    return knots.knot_hash(hash_input, '08b')


def count_bits(s):
    return Counter(s).get('1')


def count_squares(key):
    """
    >>> count_squares('flqrgnkx')
    8108
    """
    grid = get_grid(key)
    return sum(count_bits(row) for row in grid)


def count_regions(key):
    """
    >>> count_regions('flqrgnkx')
    1242
    """
    grid = get_grid(key)
    a = {}
    for y in range(128):
        for x in range(128):
            if grid[y][x] == '1':
                a[(x, y)] = (x, y)
    keys = list(a.keys())
    for i in keys:
        x, y = i
        for j in [(x + 1, y), (x, y + 1)]:
            if j in a:
                union(a, i, j, lambda p, q: q < p)
    for i in a.keys():
        find(a, i)
    return len(Counter(a.values()))


def part1(lines):
    return count_squares(lines[0].strip())


def part2(lines):
    return count_regions(lines[0].strip())
