from collections import Counter

import knots


def get_grid(key):
    return [binary_knot_hash(key, i) for i in range(128)]


def binary_knot_hash(key, i):
    hash_input = '%s-%s' % (key, i)
    return knots.knot_hash(hash_input, '08b')


def count_bits(s):
    return Counter(s).get('1')


def part1(key):
    """
    >>> part1('flqrgnkx')
    8108
    """
    grid = get_grid(key)
    return sum(count_bits(row) for row in grid)


def find(a, x):
    if a[x] == x:
        return x
    a[x] = find(a, a[x])
    return a[x]


def union(a, x, y):
    i = find(a, x)
    j = find(a, y)
    if i == j:
        return
    if j < i:
        (i, j) = (j, i)
    a[i] = j


def part2(key):
    """
    >>> part2('flqrgnkx')
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
                union(a, i, j)
    for i in a.keys():
        find(a, i)
    return len(Counter(a.values()))


if __name__ == '__main__':
    input_data = open('inputs/14/input').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
