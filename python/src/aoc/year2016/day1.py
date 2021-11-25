from aoc.util import load_input

MOVES = {
    "N": {"R": "E", "L": "W", "move": lambda x, y, v: (x, y + v)},
    "E": {"R": "S", "L": "N", "move": lambda x, y, v: (x + v, y)},
    "S": {"R": "W", "L": "E", "move": lambda x, y, v: (x, y - v)},
    "W": {"R": "N", "L": "S", "move": lambda x, y, v: (x - v, y)},
}


def part1(lines):
    """
    >>> part1(["R2, L3"])
    5
    >>> part1(["R2, R2, R2"])
    2
    >>> part1(["R5, L5, R5, R3"])
    12
    """
    direction, x, y = "N", 0, 0
    for turn, width in ((p[0], int(p[1:])) for p in lines[0].split(", ")):
        direction = MOVES[direction][turn]
        x, y = MOVES[direction]["move"](x, y, width)
    return abs(x + y)


def part2(lines):
    """
    >>> part2(["R8, R4, R4, R8"])
    4
    """
    direction, x, y = "N", 0, 0
    visited = {}
    for turn, width in ((p[0], int(p[1:])) for p in lines[0].split(", ")):
        direction = MOVES[direction][turn]
        for i in range(width):
            x, y = MOVES[direction]["move"](x, y, 1)
            if (x, y) in visited:
                return abs(x + y)
            else:
                visited[x, y] = True


if __name__ == "__main__":
    data = load_input(__file__, 2016, "1")
    print(part1(data))
    print(part2(data))
