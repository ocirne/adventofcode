from aoc.util import load_input


def decompress(line, recursive=False):
    length = 0
    index = 0
    while index < len(line):
        char = line[index]
        if char == "(":
            end = line.find(")", index)
            marker = line[index + 1 : end]
            count, repeat = map(int, marker.split("x"))
            if recursive:
                length += decompress(line[end + 1 : end + count + 1], recursive) * repeat
            else:
                length += count * repeat
            index = end + 1 + count
        else:
            length += 1
            index += 1
    return length


def part1(lines):
    """
    >>> part1(['ADVENT'])
    6
    >>> part1(['A(1x5)BC'])
    7
    >>> part1(['(3x3)XYZ'])
    9
    >>> part1(['A(2x2)BCD(2x2)EFG'])
    11
    >>> part1(['(6x1)(1x3)A'])
    6
    >>> part1(['X(8x2)(3x3)ABCY'])
    18
    """
    return decompress(lines[0])


def part2(lines):
    """
    #>>> part2(['(3x3)XYZ'])
    #9
    >>> part2(['X(8x2)(3x3)ABCY'])
    20
    >>> part2(['(27x12)(20x12)(13x14)(7x10)(1x12)A'])
    241920
    >>> part2(['(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'])
    445
    """
    return decompress(lines[0], recursive=True)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "9")
    print(part1(data))
    print(part2(data))
