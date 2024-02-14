from itertools import cycle, islice

from aoc.util import load_input, load_example


class Part:
    def __init__(self, width, coordinates):
        self.width = width
        self.coordinates = coordinates


parts = [
    # minus
    Part(4, (0, 1, 2, 3)),
    # cross
    Part(3, (1, 1j, 1 + 1j, 2 + 1j, 1 + 2j)),
    # L, kinda
    Part(3, (0, 1, 2, 2 + 1j, 2 + 2j)),
    # pipe
    Part(1, (0, 1j, 2j, 3j)),
    # block
    Part(2, (0, 1j, 1, 1 + 1j)),
]


def can_move(chamber, part, p):
    if p.imag < 0:
        return False
    if p.real < 0:
        return False
    if p.real + part.width > 7:
        return False
    if any((p + c) in chamber for c in part.coordinates):
        return False
    return True


def print_chamber(chamber):
    print("----")
    for y in range(20, -1, -1):
        for x in range(7):
            if complex(x, y) in chamber:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1(lines):
    """
    >>> part1(load_example(__file__, "17"))
    3068
    """
    jet_pattern = cycle(lines[0])
    chamber = set()
    height = 0
    for part in islice(cycle(parts), 2022):
        p = complex(2, height + 3)
        while True:
            # jet
            jet = next(jet_pattern)
            if jet == "<" and can_move(chamber, part, p - 1):
                p -= 1
            elif jet == ">" and can_move(chamber, part, p + 1):
                p += 1
            # falling
            if can_move(chamber, part, p - 1j):
                p -= 1j
            else:
                break
        for c in part.coordinates:
            chamber.add(p + c)
        height = int(max(c.imag for c in chamber)) + 1
        # print_chamber(chamber)
    return height


def part2(lines):
    """
    >>> part2(load_example(__file__, "17"))
    1514285714288
    """


if __name__ == "__main__":
    data = load_input(__file__, 2022, "17")
    print(part1(data))
#    print(part2(data))
