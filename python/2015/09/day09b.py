
from itertools import permutations


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


def run(filename):
    locations, distances = read_data(filename)
    return max(calc_distance(distances, route) for route in permutations(locations))


assert run('reference') == 982

print(run('input'))
