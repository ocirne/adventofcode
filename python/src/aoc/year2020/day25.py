from aoc.util import example

M = 20201227
S = 7


def decrypt(key):
    s = S
    e = 1
    while True:
        s = (s * S) % M
        e += 1
        if s == key:
            return e


def part1(lines):
    """
    >>> part1(example(__file__, '25'))
    14897079
    """
    key1, key2 = (int(v) for v in lines)
    e1 = decrypt(key1)
    e2 = decrypt(key2)
    return pow(S, e1*e2, M)
