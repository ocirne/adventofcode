from aoc.year2017 import knots


def one_round(data, size=256):
    """
    >>> one_round("3,4,1,5", 5)
    12
    """
    lengths = [int(length) for length in data.split(',')]
    elements = knots.run_rounds(lengths, 1, size)
    return elements[0] * elements[1]


def knot_hash(data):
    """
    >>> knot_hash('')
    'a2582a3a0e66e6e86e3812dcb672a272'
    >>> knot_hash('AoC 2017')
    '33efeb34ea91902bb2f59c9920caa6cd'
    >>> knot_hash('1,2,3')
    '3efbe78a8d82f29979031a4aa0b16a9d'
    >>> knot_hash('1,2,4')
    '63960835bcdc130f0b66d7ff4f6a5a8e'
    """
    return knots.knot_hash(data)


def part1(lines):
    return one_round(lines[0].strip())


def part2(lines):
    return knot_hash(lines[0].strip())
