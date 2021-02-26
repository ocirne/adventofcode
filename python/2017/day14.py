from collections import Counter

import knots


def knot_hash(key, i):
    hash_input = '%s-%s' % (key, i)
    return knots.knot_hash(hash_input, '08b')


def count_bits(s):
    return Counter(s)['1']


def part1(key):
    """
    >>> part1('flqrgnkx')
    8108
    """
    return sum(count_bits(knot_hash(key, i)) for i in range(128))


if __name__ == '__main__':
    input_data = open('inputs/14/input').readline().strip()
    print(part1(input_data))
