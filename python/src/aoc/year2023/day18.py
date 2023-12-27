import re

from aoc.util import load_input, load_example


MOVES = {
    "0": (0, +1),
    "R": (0, +1),
    "1": (+1, 0),
    "D": (+1, 0),
    "2": (0, -1),
    "L": (0, -1),
    "3": (-1, 0),
    "U": (-1, 0),
}


def wander(lines):
    py, px = 0, 0
    edge = set()
    for line in lines:
        direction, count, _ = line.split()
        dy, dx = MOVES[direction]
        for i in range(int(count)):
            py += dy
            px += dx
            edge.add((py, px))
    return edge


def neighbors(pos):
    py, px = pos
    if py < 0 or px < 0:
        print("outer area")
        raise
    return (py - 1, px), (py + 1, px), (py, px - 1), (py, px + 1)


def flooding(edge, start):
    assert start not in edge
    open_set = {start}
    real_inner_area = set()
    while open_set:
        pos = open_set.pop()
        real_inner_area.add(pos)
        for neighbor in neighbors(pos):
            if neighbor in edge:
                continue
            if neighbor in real_inner_area:
                continue
            open_set.add(neighbor)
    assert not edge.intersection(real_inner_area)
    return edge.union(real_inner_area)


def part1(lines):
    """
    good enough

    >>> part1(load_example(__file__, "18"))
    62
    """
    edge = wander(lines)
    #    foo = flooding(edge, (20, 152))

    min_x = min(x for _, x in edge)
    max_x = max(x for _, x in edge)
    min_y = min(y for y, _ in edge)
    max_y = max(y for y, _ in edge)

    print(min_x, max_x, min_y, max_y)

    min_x, max_x = -60, 120
    min_y, max_y = -200, -160
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) == (20, 152):
                print("%", end="")
            elif (y, x) in edge:
                print("#", end="")
            else:
                print(".", end="")
        print()

    print(min_x, max_x, min_y, max_y)

    return len(edge)


def extract_1(lines):
    """
    >>> next(extract_1(["R 6 (#70c710)"]))
    (0, 1, 6)
    >>> next(extract_1(["D 5 (#0dc571)"]))
    (1, 0, 5)
    """
    for line in lines:
        direction, count, _ = line.split()
        dy, dx = MOVES[direction]
        yield dy, dx, int(count)


def extract_2(lines):
    """
    >>> next(extract_2(["R 6 (#70c710)"]))
    (0, 1, 461937)
    >>> next(extract_2(["D 5 (#0dc571)"]))
    (1, 0, 56407)
    """
    pattern = re.compile(r".*\(#([a-f0-9]{5})(\d)\)")
    for line in lines:
        count, direction = pattern.match(line).groups()
        dy, dx = MOVES[direction]
        yield dy, dx, int(count, 16)


def reverse_index(values, left, right):
    if left > right:
        left, right = right, left
    for index, w in enumerate(values):
        if left <= w <= right:
            yield index


def reverse_index2(values, value):
    for index, w in enumerate(values):
        if value == w:
            return index
    #    print(values, value)
    raise


def solution2(iys, ixs, flooded_edge):
    total_area = 0
    for iy, ix in flooded_edge:
        dy = iys[iy + 1] - iys[iy]
        dx = ixs[ix + 1] - ixs[ix]
        total_area += dy * dx
    return total_area


def wander2(lines):
    """
    Kante 0,0 -> 0,5 (vertikal)
    x: Breite: 1
    y: Höhe: 6

    x: [-oo..0][0:1][1..+oo]
    y: [-oo..0][0:6][6..+oo]

    :param lines:
    :return:
    """
    py, px = 0, 0
    ys, xs = set(), set()
    for dy, dx, count in extract_2(lines):
        py += count * dy
        px += count * dx
        ys.add(py)
        ys.add(py + 1)
        xs.add(px)
        xs.add(px + 1)
    ys = sorted(ys)
    xs = sorted(xs)

    py, px = 0, 0
    edge = set()
    for dy, dx, count in extract_2(lines):
        #        print('dy', dy, 'dx', dx, 'count', count, 'px', px, 'py', py)
        if dy == 0:
            iy = reverse_index2(ys, py)
            npx = px + count * dx
            for ix in reverse_index(xs, px, npx):
                edge.add((iy, ix))
            px = npx
            ix = reverse_index2(xs, px)
        if dx == 0:
            ix = reverse_index2(xs, px)
            npy = py + count * dy
            for iy in reverse_index(ys, py, npy):
                edge.add((iy, ix))
            py = npy
            iy = reverse_index2(ys, py)
    return ys, xs, edge


def part2(lines):
    """
    >>> part2(load_example(__file__, "18"))
    952408144115
    """
    ys, xs, edge = wander2(lines)
    #    print('ys', ys)
    #    print('xs', xs)
    #    print('edge', edge)

    edge = flooding(edge, (20, 152))

    min_x = min(x for _, x in edge)
    max_x = max(x for _, x in edge)
    min_y = min(y for y, _ in edge)
    max_y = max(y for y, _ in edge)

    print(min_x, max_x, min_y, max_y)

    min_x, max_x = 0, 180
    min_y, max_y = 0, 40
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) == (20, 152):
                print("%", end="")
            elif (y, x) in edge:
                print("#", end="")
            else:
                print(".", end="")
        print()

    print(min_x, max_x, min_y, max_y)

    return solution2(ys, xs, edge)


if __name__ == "__main__":
    # print(part2(load_example(__file__, "18")))
    data = load_input(__file__, 2023, "18")
    print(part1(data))
    print(part2(data))
