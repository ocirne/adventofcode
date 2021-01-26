
def extract(line):
    """
    >>> extract('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
    [14, 10, 127]
    """
    token = line.split()
    return [int(token[i]) for i in [3, 6, 13]]


def race(line, seconds):
    """
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 0)
    0
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 9)
    126
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 10)
    140
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 137)
    140
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 138)
    154
    >>> race('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 1000)
    1120
    >>> race('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.', 1000)
    1056
    """
    speed, flying, resting = extract(line)
    full, rest = divmod(seconds, flying + resting)
    return speed * (full * flying + min(flying, rest))


def part1(data):
    return max(race(line, 2503) for line in data)


if __name__ == '__main__':
    inputData = open('input', 'r').readlines()
    print(part1(inputData))
#    print(part2(inputData))
