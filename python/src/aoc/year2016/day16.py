from aoc.util import load_input

FLIP = {"1": "0", "0": "1"}
CHECKSUM = {"00": "1", "11": "1", "01": "0", "10": "0"}


def stretch(a):
    """
    >>> stretch('1')
    '100'
    >>> stretch('0')
    '001'
    >>> stretch('11111')
    '11111000000'
    >>> stretch('111100001010')
    '1111000010100101011110000'
    """
    b = "".join(FLIP[c] for c in a[::-1])
    return a + "0" + b


def checksum(a, verbose=False):
    """
    >>> checksum('110010110100', verbose=True)
    110010110100
    110101
    '100'
    """
    if len(a) % 2 == 1:
        return a
    if verbose:
        print(a)
    return checksum("".join((CHECKSUM[a[i : i + 2]] for i in range(0, len(a), 2))), verbose)


def part1(lines, disk_length=272, verbose=False):
    """
    >>> part1(['10000'], disk_length=20, verbose=True)
    10000
    10000011110
    10000011110010000111110
    10000011110010000111
    0111110101
    '01100'
    """
    state = lines[0].strip()
    while len(state) < disk_length:
        if verbose:
            print(state)
        state = stretch(state)
    if verbose:
        print(state)
    return checksum(state[:disk_length], verbose)


def part2(lines):
    """
    >>> part2(['abc'])
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2016, "16")
    print(part1(data))
    print(part2(data))
