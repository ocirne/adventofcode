
from collections import Counter


def part1(data):
    """
    >>> part1('(())')
    0
    >>> part1('()()')
    0
    >>> part1('(((')
    3
    >>> part1('(()(()(')
    3
    >>> part1('))(((((')
    3
    >>> part1('())')
    -1
    >>> part1('))(')
    -1
    >>> part1(')))')
    -3
    >>> part1(')())())')
    -3
    """
    c = Counter(data)
    return c['('] - c[')']


def part2(data):
    """
    >>> part2(')')
    1
    >>> part2('()())')
    5
    """
    floor = 0
    for index, b in enumerate(data):
        if b == '(':
            floor += 1
        elif b == ')':
            floor -= 1
        else:
            raise Exception
        if floor < 0:
            return index + 1


if __name__ == '__main__':
    inputData = open('input', 'r').readline()
    print(part1(inputData))
    print(part2(inputData))
