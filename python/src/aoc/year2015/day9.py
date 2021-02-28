from itertools import permutations
from aoc.util import load_example, load_input


def prepare_data(lines):
    locations = {}
    distances = {}
    for line in lines:
        start, _, dest, _, distance = line.split()
        locations[start] = True
        locations[dest] = True
        distances[(start, dest)] = int(distance)
        distances[(dest, start)] = int(distance)
    return list(locations.keys()), distances


def calc_distance(distances, route):
    return sum(distances[(route[i - 1], route[i])] for i in range(1, len(route)))


def run(lines, fun):
    """
    >>> run(load_example(__file__, '9'), min)
    605
    >>> run(load_example(__file__, '9'), max)
    982
    """
    locations, distances = prepare_data(lines)
    return fun(calc_distance(distances, route) for route in permutations(locations))


def part1(lines):
    return run(lines, min)


def part2(lines):
    return run(lines, max)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "9")
    print(part1(data))
    print(part2(data))
