
def run_rounds(data, rounds, size):
    lengths = [int(length) for length in data.split(',')]
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


def sparse_hash():
    pass

def dense_hash():
    pass

def knot_hash():
    pass


def part1(data, size=256):
    """
    >>> part1("3,4,1,5", 5)
    12
    """
    elements = run_rounds(data, 1, size)
    return elements[0] * elements[1]


def part2(data):
    """
    >>> part2('')
    a2582a3a0e66e6e86e3812dcb672a272
    >>> part2('AoC 2017')
    33efeb34ea91902bb2f59c9920caa6cd
    >>> part2('1,2,3')
    3efbe78a8d82f29979031a4aa0b16a9d
    >>> part2('1,2,4')
    63960835bcdc130f0b66d7ff4f6a5a8e
    """
    pass

if __name__ == '__main__':
    input_data = open('input', 'r').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
