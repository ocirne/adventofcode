

def part1(line):
    """
    >>> part1('1122')
    3
    >>> part1('1111')
    4
    >>> part1('1234')
    0
    >>> part1('91212129')
    9
    """
    return sum(int(c) for i, c in enumerate(line) if line[i-1] == c)


def part2(line):
    """
    >>> part2('1212')
    6
    >>> part2('1221')
    0
    >>> part2('123425')
    4
    >>> part2('123123')
    12
    >>> part2('12131415')
    4
    """
    return sum(int(x) for x, y in zip(line, line[len(line)//2:] + line[:len(line)//2]) if x == y)


if __name__ == '__main__':
    inputData = open('input', 'r').readline().strip()
    print(part1(inputData))
    print(part2(inputData))
