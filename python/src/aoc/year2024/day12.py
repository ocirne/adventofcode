from aoc.util import load_input, load_example


def read_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, value in enumerate(line.strip()):
            grid[x, y] = value
    return grid


def part1(lines):
    """
    >>> part1(load_example(__file__, "5"))
    1930
    """
    grid = read_grid(lines)
    total = 0
    closed_set = set()
    for start in grid:
        if start in closed_set:
            continue
        plant = grid[start]
        open_heap = [start]
        area = 1
        sx, sy = start
        fences = 4 - sum(
            (m in grid and grid[m] == plant) for m in ((sx - 1, sy), (sx + 1, sy), (sx, sy - 1), (sx, sy + 1))
        )
        while open_heap:
            position = open_heap.pop()
            if position in closed_set:
                continue
            closed_set.add(position)
            px, py = position
            for n in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                if n not in grid:
                    continue
                if n in closed_set:
                    continue
                if grid[n] == plant and n not in open_heap:
                    area += 1
                    nx, ny = n
                    fences += 4 - sum(
                        (m in grid and grid[m] == plant)
                        for m in ((nx - 1, ny), (nx + 1, ny), (nx, ny - 1), (nx, ny + 1))
                    )
                    open_heap.append(n)
        total += area * fences

    return total


def merge_fences(fences):
    new_fences = []
    while fences:
        d, (px, py), (nx, ny) = fences.pop()
        if d == "W" or d == "E":
            i = 1
            while True:
                c = (d, (px, py + i), (nx, ny + i))
                if c in fences:
                    fences.remove(c)
                else:
                    break
                i += 1
            i = -1
            while True:
                c = (d, (px, py + i), (nx, ny + i))
                if c in fences:
                    fences.remove(c)
                else:
                    break
                i -= 1
        if d == "N" or d == "S":
            i = 1
            while True:
                c = (d, (px + i, py), (nx + i, ny))
                if c in fences:
                    fences.remove(c)
                else:
                    break
                i += 1
            i = -1
            while True:
                c = (d, (px + i, py), (nx + i, ny))
                if c in fences:
                    fences.remove(c)
                else:
                    break
                i -= 1
        new_fences.append((d, (px, py), (nx, ny)))
    return new_fences


def part2(lines):
    """
    >>> part2(load_example(__file__, "5"))
    1206
    """
    grid = read_grid(lines)

    total = 0
    closed_set = set()
    for start in grid:
        if start in closed_set:
            continue
        plant = grid[start]
        open_heap = [start]
        area = 1
        sx, sy = start
        fences = [
            (d, start, m)
            for d, m in (("W", (sx - 1, sy)), ("E", (sx + 1, sy)), ("N", (sx, sy - 1)), ("S", (sx, sy + 1)))
            if m not in grid or grid[m] != plant
        ]
        while open_heap:
            position = open_heap.pop()
            if position in closed_set:
                continue
            closed_set.add(position)
            px, py = position
            for n in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                if n not in grid:
                    continue
                if n in closed_set:
                    continue
                if grid[n] == plant and n not in open_heap:
                    area += 1
                    nx, ny = n
                    fences += [
                        (d, n, m)
                        for d, m in (("W", (nx - 1, ny)), ("E", (nx + 1, ny)), ("N", (nx, ny - 1)), ("S", (nx, ny + 1)))
                        if m not in grid or grid[m] != plant
                    ]
                    open_heap.append(n)
        total += area * len(merge_fences(fences))

    return total


if __name__ == "__main__":
    data = load_input(__file__, 2024, "12")
    print(part1(data))
    print(part2(data))
