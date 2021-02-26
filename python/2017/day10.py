import knots


def part1(data, size=256):
    """
    >>> part1("3,4,1,5", 5)
    12
    """
    lengths = [int(length) for length in data.split(',')]
    elements = knots.run_rounds(lengths, 1, size)
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
    return knots.knot_hash(data)


if __name__ == '__main__':
    input_data = open('inputs/10/input').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
