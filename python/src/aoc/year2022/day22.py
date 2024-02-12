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


def part2(lines):
    """
    >>> part2(load_example(__file__, "22"))
    """


if __name__ == "__main__":
    print(part1(load_example(__file__, "22")))

    data = load_input(__file__, 2022, "22")
    print(part1(data))
#    print(part2(data))
