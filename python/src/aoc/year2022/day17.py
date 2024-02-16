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


def rocks_falling(jet_pattern):
    iter_jet = cycle(enumerate(jet_pattern))
    chamber = set()
    height = 0
    for part_index, part in cycle(enumerate(parts)):
        p = complex(2, height + 3)
        while True:
            # jet
            jet_index, jet = next(iter_jet)
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
        yield height, part_index, jet_index


def part1(lines):
    """
    >>> part1(load_example(__file__, "17"))
    3068
    """
    return next(islice(rocks_falling(lines[0]), 2021, None))[0]


def find_cycle(jet_pattern):
    seen = {}

    # TODO for some reason the first hits are not valid
    skip = 20

    for rocks, (height, part_index, jet_index) in enumerate(rocks_falling(jet_pattern)):
        key = part_index, jet_index
        if key in seen:
            skip -= 1
            if skip == 0:
                last_rocks, last_height = seen[key]
                cycle_rocks = rocks - last_rocks
                cycle_height = height - last_height
                return cycle_rocks, cycle_height
        seen[key] = rocks, height


def find_base_height(jet_pattern, total_rocks, cycle_rocks):
    base_rocks = total_rocks % cycle_rocks + cycle_rocks
    for rocks, (height, part_index, jet_index) in enumerate(rocks_falling(jet_pattern)):
        if rocks == base_rocks:
            return base_rocks, height


def part2(lines):
    """
    >>> part2(load_example(__file__, "17"))
    1514285714288
    """
    jet_pattern = lines[0]
    total_rocks = 1000000000000
    cycle_rocks, cycle_height = find_cycle(jet_pattern)
    base_rocks, base_height = find_base_height(jet_pattern, total_rocks, cycle_rocks)
    return (total_rocks - base_rocks) // cycle_rocks * cycle_height + base_height - 1


if __name__ == "__main__":
    data = load_input(__file__, 2022, "17")
    print(part1(data))
    print(part2(data))
