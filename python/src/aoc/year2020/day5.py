
def to_int(line):
    """
    >>> to_int('FBFBBFFRLR')
    357
    >>> to_int('BFFFBBFRRR')
    567
    >>> to_int('FFFBBBFRRR')
    119
    >>> to_int('BBFFBBFRLL')
    820
    """
    bin_repr = line \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('R', '1') \
        .replace('L', '0')
    return int(bin_repr, 2)


def part1(lines):
    return max(to_int(line) for line in lines)


def part2(lines):
    seats = sorted(to_int(line) for line in lines)
    for i in range(1, len(seats)):
        if seats[i-1] != seats[i] - 1:
            return seats[i]-1
