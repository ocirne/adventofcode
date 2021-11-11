from itertools import islice

from aoc.util import load_input


def is_possible_triangle(triangle):
    """
    >>> is_possible_triangle([3, 4, 5])
    True
    >>> is_possible_triangle([5, 10, 25])
    False
    """
    return 2 * max(triangle) < sum(triangle)


def horizontal_triangles(lines):
    for line in lines:
        yield tuple(map(int, line.split()))


def vertical_reading(lines):
    it = horizontal_triangles(lines)
    for t in iter(lambda: tuple(islice(it, 3)), ()):
        for x in range(3):
            yield tuple(t[y][x] for y in range(3))


def part1(lines):
    return sum(is_possible_triangle(t) for t in horizontal_triangles(lines))


def part2(lines):
    return sum(is_possible_triangle(t) for t in vertical_reading(lines))


if __name__ == "__main__":
    data = load_input(__file__, 2016, "3")
    print(part1(data))
    print(part2(data))
