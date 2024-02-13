from aoc.util import load_input, load_example
import re

RDLU = {
    0: (+1, 0),  # right
    1: (0, +1),  # down
    2: (-1, 0),  # left
    3: (0, -1),  # up
}


def part1(lines):
    """
    >>> part1(load_example(__file__, "22"))
    6032
    """
    m = {}
    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line):
            if not c.isspace():
                m[x, y] = c
    path = lines[-1]
    print(path.find("R"))
    print(path.find("L"))
    print(path.find("[RL]"))
    print(re.split("([RL])", path))
    x, y, f = min(x for x, y in m.keys() if y == 0), 0, 0
    print(x, y)
    for t in re.split("([RL])", path):
        print(x, y)
        if t.isnumeric():
            dx, dy = RDLU[f]
            for _ in range(int(t)):
                cx, cy = x + dx, y + dy
                if (cx, cy) not in m:
                    if f == 0:
                        cx = min(tx for tx, ty in m.keys() if ty == cy)
                    if f == 1:
                        cy = min(ty for tx, ty in m.keys() if tx == cx)
                    if f == 2:
                        cx = max(tx for tx, ty in m.keys() if ty == cy)
                    if f == 3:
                        cy = max(ty for tx, ty in m.keys() if tx == cx)
                if m[cx, cy] == "#":
                    break
                x, y = cx, cy
        elif t == "R":
            f = (f + 1) % 4
        elif t == "L":
            f = (f + 3) % 4
        else:
            raise

    return 1000 * (y + 1) + 4 * (x + 1) + f


"""
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

          (2,0)
(0,1)(1,1)(2,1)
          (2,2)(3,2)

RDLU = {
    0: (+1, 0),  # right
    1: (0, +1),  # down
    2: (-1, 0),  # left
    3: (0, -1),  # up
}

10R5L5R10L4R5L5

Faltlinien (6 Quadrate * 4)

1: (verlassen!)
4, y, 0 -> 6: 4, 4-y, 2
1, y, 2 -> 3: y, 1, 1
x, 1, 3 ->

2:
x, 4, 1 ->
1, y, 2 ->
x, 1, 3 ->

3:
x, 4, 1 -> 5: 1, x, 1
x, 1, 3 -> 1: 1, y, 0

4:
4, y, 0 -> 6: y, 1, 1
1, y, 2 -> 3: 4, y, 2

5:
x, 4, 1 -> 1: x, 1, 1
1, y, 2 -> 3: 4-y, 4, 2

6:
4, y, 0 ->
x, 4, 1 ->
x, 1, 3 -> 4: 4, 4-x, 2

"""


def read_data(lines):
    m = {}
    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line):
            if not c.isspace():
                m[x, y] = c
    path = lines[-1]
    return m, path


def read_data2(lines, size):
    m = {}
    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line):
            if not c.isspace():
                q = x // size, y // size
                if q not in m:
                    m[q] = {}
                m[q][x % size, y % size] = c
    path = lines[-1]
    print(m)
    return m, path


def neighbor_2d(m, cx, cy, f, dx, dy):
    nx, ny = cx + dx, cy + dy
    if (nx, ny) not in m:
        if f == 0:
            nx = min(x for x, y in m.keys() if y == ny)
        elif f == 1:
            ny = min(y for x, y in m.keys() if x == nx)
        elif f == 2:
            nx = max(x for x, y in m.keys() if y == ny)
        elif f == 3:
            ny = max(y for x, y in m.keys() if x == nx)
    if m[nx, ny] == "#":
        return cx, cy, f
    return nx, ny, f


MASTER_BLASTER_TEST = {
    # q, f: nq, nf, (s, x, y) -> nx, ny
    ((2, 0), 0): ((3, 2), 2, lambda s, x, y: (s, y)),  # 4, y
    ((2, 0), 1): ((2, 1), 1, lambda s, x, y: (x, s - y)),
    ((2, 0), 2): ((1, 1), 1, lambda s, x, y: (y, 0)),
    ((2, 0), 3): ((7, 7), 7, lambda s, x, y: (x, y)),  # x, 1
    ((0, 1), 0): ((1, 1), 0, lambda s, x, y: (0, y)),
    ((0, 1), 1): ((7, 7), 7, lambda s, x, y: (x, y)),  # x, 4
    ((0, 1), 2): ((7, 7), 7, lambda s, x, y: (x, y)),  # 1, y
    ((0, 1), 3): ((2, 0), 1, lambda s, x, y: (s - x, 0)),
    ((1, 1), 0): ((7, 7), 7, lambda s, x, y: (x, y)),  # 4, y
    ((1, 1), 1): ((2, 2), 0, lambda s, x, y: (0, x)),
    ((1, 1), 2): ((0, 1), 2, lambda s, x, y: (s, y)),
    ((1, 1), 3): ((2, 0), 0, lambda s, x, y: (0, x)),
    ((2, 1), 0): ((3, 2), 1, lambda s, x, y: (s - y, 0)),
    ((2, 1), 1): ((2, 2), 1, lambda s, x, y: (x, 0)),
    ((2, 1), 2): ((7, 7), 7, lambda s, x, y: (x, y)),  # 1, y
    ((2, 1), 3): ((2, 0), 3, lambda s, x, y: (x, s)),
    ((2, 2), 0): ((3, 2), 0, lambda s, x, y: (0, y)),
    ((2, 2), 1): ((0, 1), 3, lambda s, x, y: (s - x, s)),
    ((2, 2), 2): ((7, 7), 7, lambda s, x, y: (x, y)),  # 1, y
    ((2, 2), 3): ((2, 1), 3, lambda s, x, y: (x, s)),
    ((3, 2), 0): ((7, 7), 7, lambda s, x, y: (x, y)),  # 4, y
    ((3, 2), 1): ((2, 0), 2, lambda s, x, y: (s, s - y)),
    ((3, 2), 2): ((2, 2), 2, lambda s, x, y: (s, y)),
    ((3, 2), 3): ((7, 7), 7, lambda s, x, y: (x, y)),  # x, 1
}


def neighbor_3d(m, s, cq, cf, cx, cy, dx, dy):
    nq, nf, nx, ny = cq, cf, cx + dx, cy + dy
    if (nx, ny) not in m[cq]:
        print("missing q", nq, "f", nf, "x", nx, "y", ny)
        nq, nf, f = MASTER_BLASTER_TEST[cq, cf]
        nx, ny = f(s - 1, cx, cy)
        print("--> nq ", nq, "nxy", nx, ny, "nf", nf)
    if m[nq][nx, ny] == "#":
        return cq, cf, cx, cy
    return nq, nf, nx, ny


def part2(lines, size=50):
    """
    >>> part2(load_example(__file__, "22"))
    5031
    """
    m, path = read_data2(lines, size)
    print([len(v) for v in m.values()])
    print(path)
    q = 2, 0
    f, x, y = 0, 0, 0
    for t in re.split("([RL])", path):
        if t.isnumeric():
            for _ in range(int(t)):
                dx, dy = RDLU[f]
                q, f, x, y = neighbor_3d(m, size, q, f, x, y, dx, dy)
                print("***", q, "xy", x, y, "f", f)
        elif t == "R":
            f = (f + 1) % 4
        elif t == "L":
            f = (f + 3) % 4
        else:
            raise

    qx, qy = q
    return 1000 * (qy * size + y + 1) + 4 * (qx * size + x + 1) + f


if __name__ == "__main__":
    print(5031)
    print(part2(load_example(__file__, "22"), 4))

#    data = load_input(__file__, 2022, "22")
#    print(part1(data))
#    print(part2(data))
