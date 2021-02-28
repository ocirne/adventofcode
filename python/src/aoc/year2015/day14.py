from collections import defaultdict
from itertools import groupby
from operator import itemgetter

from aoc.util import load_input

ROUNDS = 2503


def extract(line):
    """
    >>> extract('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
    ('Comet', 14, 10, 127)
    """
    token = line.split()
    return token[0], int(token[3]), int(token[6]), int(token[13])


def race(line, seconds):
    """
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 0)
    ('Comet', 0)
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 9)
    ('Comet', 126)
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 10)
    ('Comet', 140)
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 137)
    ('Comet', 140)
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 138)
    ('Comet', 154)
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 1000)
    ('Comet', 1120)
    >>> race('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.', 1000)
    ('Dancer', 1056)
    """
    reindeer, speed, flying, resting = extract(line)
    full, rest = divmod(seconds, flying + resting)
    return reindeer, speed * (full * flying + min(flying, rest))


def part1(lines, rounds=ROUNDS):
    """
    >>> part1(['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', \
               'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'], 1000)
    1120
    """
    return max((race(line, rounds) for line in lines), key=itemgetter(1))[1]


def part2(lines, rounds=ROUNDS):
    """
    >>> part2(['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', \
               'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'], 1000)
    689
    """
    points = defaultdict(lambda: 0)
    for i in range(1, rounds + 1):
        groups = groupby((race(line, i) for line in lines), itemgetter(1))
        first_group = max(
            ((key, [item for item in data]) for key, data in groups), key=itemgetter(0)
        )
        for name, _ in first_group[1]:
            points[name] += 1
    return max(points.values())


if __name__ == "__main__":
    data = load_input(__file__, 2015, "14")
    print(part1(data))
    print(part2(data))
