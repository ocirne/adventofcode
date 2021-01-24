from itertools import permutations
from pathlib import Path


def read_data(filename):
    f = open(filename, 'r')
    locations = {}
    distances = {}
    for line in f.readlines():
        start, _, dest, _, distance = line.split()
        locations[start] = True
        locations[dest] = True
        distances[(start, dest)] = int(distance)
        distances[(dest, start)] = int(distance)
    return list(locations.keys()), distances


def calc_distance(distances, route):
    return sum(distances[(route[i-1], route[i])] for i in range(1, len(route)))


def run(filename, fun):
    """
    >>> run(Path(__file__).parent / 'reference', min)
    605
    >>> run(Path(__file__).parent / 'reference', max)
    982
    """
    locations, distances = read_data(filename)
    return fun(calc_distance(distances, route) for route in permutations(locations))


if __name__ == '__main__':
    print(run('input', min))
    print(run('input', max))
