import itertools
from math import sqrt


def get_edge_length(target):
    result = int(sqrt(target))
    if result % 2 == 0:
        result -= 1
    if result**2 == target:
        return result
    return result + 2


def manhattan_distance(x, y, middle):
    return abs(x-middle) + abs(y-middle)


def coordinates(edge, target):
    bottom_right = edge**2
    bottom_left = bottom_right - (edge-1)
    top_left = bottom_left - (edge-1)
    top_right = top_left - (edge-1)
    x = y = edge-1
    if bottom_right == target:
        return x, y
    if bottom_left <= target < bottom_right:
        x = target - bottom_left
        return x, y
    else:
        x = 0
    if top_left <= target < bottom_left:
        y = target - top_left
        return x, y
    else:
        y = 0
    if top_right <= target < top_left:
        x = top_left - target
        return x, y
    else:
        x = edge-1
    y = top_right - target
    return x, y


def part1(target):
    """
    >>> part1(1)
    0
    >>> part1(12)
    3
    >>> part1(23)
    2
    >>> part1(1024)
    31
    """
    edge = get_edge_length(target)
    middle = (edge-1) // 2
    x, y = coordinates(edge, target)
    return manhattan_distance(x, y, middle)


def walk_the_grid():
    """
    >>> list(itertools.islice(walk_the_grid(), 9))
    [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (2, 1)]
    """
    x = y = 0
    diameter = 1
    while True:
        while x < diameter:
            x += 1
            yield x, y
        while y > -diameter:
            y -= 1
            yield x, y
        while x > -diameter:
            x -= 1
            yield x, y
        while y < diameter:
            y += 1
            yield x, y
        diameter += 1


def sum_adjacent(grid, x, y):
    result = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) in grid:
                result += grid[i, j]
    return result


def part2(target):
    """
    >>> part2(4)
    5
    >>> part2(58)
    59
    >>> part2(59)
    122
    >>> part2(800)
    806
    """
    grid = {(0, 0): 1}
    for x, y in walk_the_grid():
        value = sum_adjacent(grid, x, y)
        if value > target:
            return value
        grid[x, y] = value


if __name__ == '__main__':
    inputData = int(open('input', 'r').readline())
    print(part1(inputData))
    print(part2(inputData))
