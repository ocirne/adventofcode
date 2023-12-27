import re
from typing import Tuple, Set, List, Generator

from aoc.util import load_input, load_example


class Digger:
    def __init__(self, edge):
        self.edge = edge

    @staticmethod
    def _neighbors(position):
        x, y = position
        if x < -200 or y < -200:
            print("outer area")
            raise
        return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    def dig_inner_area(self, start):
        assert start not in self.edge
        open_set = {start}
        real_inner_area = set()
        while open_set:
            current = open_set.pop()
            real_inner_area.add(current)
            for neighbor in self._neighbors(current):
                if neighbor in self.edge:
                    continue
                if neighbor in real_inner_area:
                    continue
                open_set.add(neighbor)
        assert not self.edge.intersection(real_inner_area)
        return self.edge.union(real_inner_area)


class Indizes:
    def __init__(self, lines, extract_dig_plan):
        x, y = 0, 0
        xs, ys = set(), set()
        for dx, dy, count in extract_dig_plan(lines):
            x += count * dx
            y += count * dy
            xs.add(x)
            xs.add(x + 1)
            ys.add(y)
            ys.add(y + 1)
        self.x, self.y = sorted(xs), sorted(ys)

    @staticmethod
    def _reverse(values: List[int], value: int) -> int:
        for index, w in enumerate(values):
            if value == w:
                return index
        raise

    @staticmethod
    def _reverse_range(values: List[int], left: int, right: int) -> Generator[int, None, None]:
        if left > right:
            left, right = right, left
        for index, w in enumerate(values):
            if left <= w <= right:
                yield index

    def reverse_x(self, x: int) -> int:
        return self._reverse(self.x, x)

    def reverse_x_range(self, left: int, right: int) -> Generator[int, None, None]:
        return self._reverse_range(self.x, left, right)

    def reverse_y(self, y: int) -> int:
        return self._reverse(self.y, y)

    def reverse_y_range(self, left: int, right: int) -> Generator[int, None, None]:
        return self._reverse_range(self.y, left, right)


def trace_edge(indizes: Indizes, lines: List[str], extract_dig_plan) -> Set[Tuple[int, int]]:
    x, y = 0, 0
    edge = set()
    for dx, dy, count in extract_dig_plan(lines):
        if dx != 0:
            iy = indizes.reverse_y(y)
            next_x = x + count * dx
            edge.update((ix, iy) for ix in indizes.reverse_x_range(x, next_x))
            x = next_x
        if dy != 0:
            ix = indizes.reverse_x(x)
            next_y = y + count * dy
            edge.update((ix, iy) for iy in indizes.reverse_y_range(y, next_y))
            y = next_y
    return edge


def sum_total_area(indizes: Indizes, area: Set[Tuple[int, int]]) -> int:
    total_area = 0
    for ix, iy in area:
        w = indizes.x[ix + 1] - indizes.x[ix]
        h = indizes.y[iy + 1] - indizes.y[iy]
        total_area += w * h
    return total_area


MOVES = {
    "0": (+1, 0),
    "R": (+1, 0),
    "1": (0, +1),
    "D": (0, +1),
    "2": (-1, 0),
    "L": (-1, 0),
    "3": (0, -1),
    "U": (0, -1),
}


def extract_dig_plan_1(lines: List[str]) -> Generator[Tuple[int, int, int], None, None]:
    """
    >>> next(extract_dig_plan_1(["R 6 (#70c710)"]))
    (1, 0, 6)
    >>> next(extract_dig_plan_1(["D 5 (#0dc571)"]))
    (0, 1, 5)
    """
    for line in lines:
        direction, count, _ = line.split()
        dx, dy = MOVES[direction]
        yield dx, dy, int(count)


def extract_dig_plan_2(lines: List[str]) -> Generator[Tuple[int, int, int], None, None]:
    """
    >>> next(extract_dig_plan_2(["R 6 (#70c710)"]))
    (1, 0, 461937)
    >>> next(extract_dig_plan_2(["D 5 (#0dc571)"]))
    (0, 1, 56407)
    """
    pattern = re.compile(r".*\(#([a-f0-9]{5})(\d)\)")
    for line in lines:
        count, direction = pattern.match(line).groups()
        dx, dy = MOVES[direction]
        yield dx, dy, int(count, 16)


def find_inner_area(lines: List[str], extract_dig_plan, start) -> int:
    indizes = Indizes(lines, extract_dig_plan)
    edge = trace_edge(indizes, lines, extract_dig_plan)
    area = Digger(edge).dig_inner_area(start)
    return sum_total_area(indizes, area)


def part1(lines: List[str], start: Tuple[int, int] = (152, 20)):
    """
    >>> part1(load_example(__file__, "18"), start=(1, 1))
    62
    """
    return find_inner_area(lines, extract_dig_plan_1, start)


def part2(lines: List[str], start: Tuple[int, int] = (152, 20)):
    """
    >>> part2(load_example(__file__, "18"), start=(1, 1))
    952408144115
    """
    return find_inner_area(lines, extract_dig_plan_2, start)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "18")
    print(part1(data))
    print(part2(data))
