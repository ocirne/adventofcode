from aoc.util import load_input


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
    line = lines[0].strip()
    length = 0
    index = 0
    while index < len(line):
        char = line[index]
        if char == "(":
            end = line.find(")", index)
            marker = line[index + 1 : end]
            count, repeat = map(int, marker.split("x"))
            length += count * repeat
            index = end + 1 + count
        else:
            length += 1
            index += 1
    return length


if __name__ == "__main__":
    data = load_input(__file__, 2016, "9")
    print(part1(data))
#    print(part2(data))
