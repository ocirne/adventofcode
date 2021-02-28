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
    sum_skip_size = s * (s - 1) // 2
    x = size - ((rounds * sum(lengths) + sum_skip_size) % size)
    return elements[x:] + elements[:x]


def to_ascii_codes(s: str):
    """
    >>> to_ascii_codes('1,2,3')
    [49, 44, 50, 44, 51]
    """
    return list(s.encode())


def dense_hash(lengths):
    sparse = run_rounds(lengths, 64, 256)
    return [reduce(xor, sparse[i * 16 : (i + 1) * 16]) for i in range(16)]


def format_knot_hash(value, format_spec):
    """
    >>> format_knot_hash([64, 7, 255], '02x')
    '4007ff'
    >>> format_knot_hash(bytearray.fromhex('A0C20170'), '08b')
    '10100000110000100000000101110000'
    """
    return "".join(format(h, format_spec) for h in value)


def knot_hash(s, format_spec="02x"):
    lengths = to_ascii_codes(s) + SUFFIX
    dense = dense_hash(lengths)
    return format_knot_hash(dense, format_spec)
