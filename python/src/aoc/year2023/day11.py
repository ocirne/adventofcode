from itertools import combinations

from aoc.util import load_input, load_example


def expand_universe(lines):
    empty_row = [True for _ in lines]
    empty_column = [True for _ in lines[0]]
    for y, line in enumerate(lines):
        for x, g in enumerate(line):
            if g == "#":
                empty_row[y] = False
                empty_column[x] = False
    expanded = []
    for y, line in enumerate(lines):
        if empty_row[y]:
            expanded.append(line)
            expanded.append(line)
        else:
            expanded_line = ""
            for x, g in enumerate(line):
                if empty_column[x]:
                    expanded_line += "."
                expanded_line += g
            expanded.append(expanded_line)
    return expanded


def positions_of_galaxies(lines):
    for y, line in enumerate(lines):
        for x, g in enumerate(line):
            if g == "#":
                yield y, x


def manhattan_distance(g1, g2):
    (y1, x1), (y2, x2) = g1, g2
    return abs(y2 - y1) + abs(x2 - x1)


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    374
    """
    eu = expand_universe(lines)
    p = positions_of_galaxies(eu)
    total = 0
    for g1, g2 in combinations(p, 2):
        print(g1, g2, manhattan_distance(g1, g2))
        total += manhattan_distance(g1, g2)
    return total


def part2(lines):
    """
    #    >>> part2(load_example(__file__, "11"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "11")
    # data = load_example(__file__, "11")
    print(part1(data))
#    print(part2(data))
