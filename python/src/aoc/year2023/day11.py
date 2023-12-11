from itertools import combinations

from aoc.util import load_input, load_example


class Universe:
    def __init__(self, lines):
        self.empty_rows, self.empty_columns = self.identify_empty_rows_columns(lines)
        self.galaxies = self.positions_of_galaxies(lines)

    @staticmethod
    def positions_of_galaxies(lines):
        for y, line in enumerate(lines):
            for x, g in enumerate(line):
                if g == "#":
                    yield y, x

    @staticmethod
    def identify_empty_rows_columns(lines):
        empty_row = [True for _ in lines]
        empty_column = [True for _ in lines[0]]
        for y, line in enumerate(lines):
            for x, g in enumerate(line):
                if g == "#":
                    empty_row[y] = False
                    empty_column[x] = False
        return empty_row, empty_column

    def manhattan_distance(self, g1, g2, factor):
        (y1, x1), (y2, x2) = g1, g2
        if y1 > y2:
            y1, y2 = y2, y1
        if x1 > x2:
            x1, x2 = x2, x1
        y = sum(1 for r in self.empty_rows[y1:y2] if r)
        x = sum(1 for c in self.empty_columns[x1:x2] if c)
        return abs(y2 - y1) + abs(x2 - x1) + (x + y) * (factor - 1)


def measure_universe(lines, factor):
    """
    >>> measure_universe(load_example(__file__, "11"), 2)
    374
    >>> measure_universe(load_example(__file__, "11"), 10)
    1030
    >>> measure_universe(load_example(__file__, "11"), 100)
    8410
    """
    universe = Universe(lines)
    return sum(universe.manhattan_distance(g1, g2, factor) for g1, g2 in combinations(universe.galaxies, 2))


def part1(lines):
    return measure_universe(lines, 2)


def part2(lines):
    return measure_universe(lines, 1_000_000)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "11")
    print(part1(data))
    print(part2(data))
