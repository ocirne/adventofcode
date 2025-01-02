from aoc.util import load_input, load_example

from heapq import heappush, heappop


def read_grid(lines):
    return [tuple(map(int, pair.split(","))) for pair in lines]


def find_neighbors(grid, x, y, s):
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if nx < 0 or s < nx or ny < 0 or s < ny:
            continue
        if (nx, ny) in grid:
            continue
        yield nx, ny


def dijkstra(grid, start, end, s):
    open_heap = []
    closed_set = set()
    heappush(open_heap, (0, start))
    while open_heap:
        steps, position = heappop(open_heap)
        if position == end:
            return steps
        if position in closed_set:
            continue
        closed_set.add(position)
        for neighbor in find_neighbors(grid, *position, s):
            heappush(open_heap, (steps + 1, neighbor))


def find_best_path(grid, corrupted_bytes, s):
    return dijkstra(set(grid[:corrupted_bytes]), start=(0, 0), end=(s, s), s=s)


def part1(lines, size=70, corrupted_bytes=1024):
    """
    >>> part1(load_example(__file__, "18"), size=6, corrupted_bytes=12)
    22
    """
    grid = read_grid(lines[:corrupted_bytes])
    return find_best_path(grid, corrupted_bytes, size)


def binary_search(grid, size):
    left, right = 0, len(grid)
    while left < right:
        middle = (right + left) // 2
        x = find_best_path(grid, middle, size)
        next_x = find_best_path(grid, middle + 1, size)
        if x is not None:
            if next_x is None:
                return middle
            else:
                left = middle - 1
        else:
            right = middle + 1


def part2(lines, size=70):
    """
    >>> part2(load_example(__file__, "18"), size=6)
    '6,1'
    """
    grid = read_grid(lines)
    r = binary_search(grid, size)
    x, y = grid[r]
    return f"{x},{y}"


if __name__ == "__main__":
    data = load_input(__file__, 2024, "18")
    print(part1(data))
    print(part2(data))
