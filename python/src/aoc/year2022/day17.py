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
    for y in range(70, -1, -1):
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

    T = 1000000000000

    print(len(lines[0]))
    jet_pattern = cycle(lines[0])
    jet_index = 0
    chamber = set()
    height = 0
    last_part_index = -1
    last_height = 0
    for part_index, part in enumerate(islice(cycle(parts), 30)):
        p = complex(2, height + 3)
        while True:
            # jet
            jet = next(jet_pattern)
            #            if (part_index % 5) == 0 and (jet_index % len(lines[0]) == 0):
            jet_index = jet_index + 1
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
        if part_index % 1735 == 140:
            #            if (T % (part_index - last_part_index) == 0):
            print(
                "det kenn ick",
                part_index,
                jet_index,
                part_index % 5,
                jet_index % len(lines[0]),
                "-->",
                (part_index - last_part_index),
                height,
                "(%d)" % (height - last_height),
            )
            last_part_index = part_index
            last_height = height
    #        if (part_index % 5, jet_index % len(lines[0])) in seen:
    #            print('kenn ick', part_index, jet_index, part_index % 5, jet_index % len(lines[0]), '-->',
    #            (part_index - last_part_index), height, '(%d)' % (height - last_height))
    #            print(part_index - seen[(part_index % 5, jet_index % len(lines[0]))])
    #        seen[(part_index % 5, jet_index % len(lines[0]))] = part_index

    # det kenn ick 965 5512 0 32 --> 5 1468 (11)
    # det kenn ick 970 5539 0 19 --> 5 1475 (7)
    # det kenn ick 975 5571 0 11 --> 5 1482 (7)
    # det kenn ick 980 5598 0 38 --> 5 1492 (10)
    # det kenn ick 985 5625 0 25 --> 5 1498 (6)
    # det kenn ick 990 5654 0 14 --> 5 1504 (6)
    # det kenn ick 995 5686 0 6 --> 5 1510 (6)

    print(T % 700)  # 400
    assert (T - 400) % 35 == 0
    anzahl = (T - 400) // 35
    print(anzahl * 53 + 608)
    print(1514285714288)

    print("--")
    m = 1735  # 35
    print(T % m)
    i = 2711
    print("i", i)
    base = 2842  # 209 # 26
    # r = T % m
    r = 1875
    print("r", r)
    assert (T - r) % m == 0
    anzahl = (T - r) // m
    print("anzahl", anzahl)
    print(anzahl * i + base)
    print(1514285714288)

    #    print_chamber(chamber)
    return height, jet_index


if __name__ == "__main__":
    print(part2(load_example(__file__, "17")))

    data = load_input(__file__, 2022, "17")

#    print(part1(data))
#    print(part2(data))
