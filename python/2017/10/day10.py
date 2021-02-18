from functools import reduce
from operator import xor

SUFFIX = [17, 31, 73, 47, 23]


def run_rounds(lengths, rounds, size):
    elements = list(range(size))
    skip_size = 0
    for r in range(rounds):
        for length in lengths:
            # reverse
            elements = list(reversed(elements[:length])) + elements[length:]
            # rotate
            r = (length + skip_size) % size
            elements = elements[r:] + elements[:r]
            skip_size += 1
    # revert rotations
    s = rounds * len(lengths)
    sum_skip_size = s*(s-1)//2
    x = size - ((rounds * sum(lengths) + sum_skip_size) % size)
    return elements[x:] + elements[:x]


def to_ascii_codes(s):
    """
    >>> to_ascii_codes('1,2,3')
    [49, 44, 50, 44, 51]
    """
    return [ord(c) for c in s]


def sparse_hash(lengths):
    return run_rounds(lengths, 64, 256)


def dense_hash(sparse):
    return [reduce(xor, sparse[i*16:(i+1)*16]) for i in range(16)]


def knot_hash(dense):
    """
    >>> knot_hash([64, 7, 255])
    '4007ff'
    """
    return hex(sum(i * 256**e for e, i in enumerate(reversed(dense))))[2:]


def part1(data, size=256):
    """
    >>> part1("3,4,1,5", 5)
    12
    """
    lengths = [int(length) for length in data.split(',')]
    elements = run_rounds(lengths, 1, size)
    return elements[0] * elements[1]


def part2(data):
    """
    >>> part2('')
    'a2582a3a0e66e6e86e3812dcb672a272'
    >>> part2('AoC 2017')
    '33efeb34ea91902bb2f59c9920caa6cd'
    >>> part2('1,2,3')
    '3efbe78a8d82f29979031a4aa0b16a9d'
    >>> part2('1,2,4')
    '63960835bcdc130f0b66d7ff4f6a5a8e'
    """
    lengths = to_ascii_codes(data) + SUFFIX
    sparse = sparse_hash(lengths)
    dense = dense_hash(sparse)
    return knot_hash(dense)


if __name__ == '__main__':
    input_data = open('input', 'r').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
