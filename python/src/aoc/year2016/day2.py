from aoc.util import load_input, load_example

MOVES_1 = {
    "U": lambda x, y: (x, max(0, y - 1)),
    "L": lambda x, y: (max(0, x - 1), y),
    "R": lambda x, y: (min(2, x + 1), y),
    "D": lambda x, y: (x, min(2, y + 1)),
}


def part1(lines):
    """
    >>> part1(load_example(__file__, "2"))
    '1985'
    """
    x, y = 1, 1
    r = ""
    for line in lines:
        for d in line:
            x, y = MOVES_1[d](x, y)
        r += str(y * 3 + x + 1)
    return r


MOVES_2 = {
    "U": lambda x, y: (x, max(abs(2 - x), y - 1)),
    "L": lambda x, y: (max(abs(2 - y), x - 1), y),
    "R": lambda x, y: (min(4 - abs(y - 2), x + 1), y),
    "D": lambda x, y: (x, min(4 - abs(x - 2), y + 1)),
}

FIELD = {
    (2, 0): "1",
    (1, 1): "2",
    (2, 1): "3",
    (3, 1): "4",
    (0, 2): "5",
    (1, 2): "6",
    (2, 2): "7",
    (3, 2): "8",
    (4, 2): "9",
    (1, 3): "A",
    (2, 3): "B",
    (3, 3): "C",
    (2, 4): "D",
}


def part2(lines):
    """
    >>> part2(load_example(__file__, "2"))
    '5DB3'
    """
    x, y = 0, 2
    r = ""
    for line in lines:
        for d in line:
            x, y = MOVES_2[d](x, y)
        r += FIELD[x, y]
    return r


if __name__ == "__main__":
    data = load_input(__file__, 2016, "2")
    print(part1(data))
    print(part2(data))
