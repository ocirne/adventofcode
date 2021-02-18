
def part1(data, size=256):
    """
    >>> part1("3,4,1,5", 5)
    12
    """
    lengths = [int(length) for length in data.split(',')]
    elements = list(range(size))
    for skip_size, length in enumerate(lengths):
        # reverse
        elements = list(reversed(elements[:length])) + elements[length:]
        # rotate
        r = (length + skip_size) % size
        elements = elements[r:] + elements[:r]
    # revert rotations
    s = len(lengths)
    x = size - ((sum(lengths) + (s*(s-1)//2)) % size)
    elements = elements[x:] + elements[:x]
    return elements[0] * elements[1]


def sparse_hash():

def dense_hash():

def knot_hash():

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


if __name__ == '__main__':
    input_data = open('input', 'r').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
