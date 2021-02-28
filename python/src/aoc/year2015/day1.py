
from collections import Counter

from aoc.util import load_input


def part1(lines):
    """
    >>> part1(['(())'])
    0
    >>> part1(['()()'])
    0
    >>> part1(['((('])
    3
    >>> part1(['(()(()('])
    3
    >>> part1(['))((((('])
    3
    >>> part1(['())'])
    -1
    >>> part1(['))('])
    -1
    >>> part1([')))'])
    -3
    >>> part1([')())())'])
    -3
    """
    data = lines[0]
    c = Counter(data)
    return c['('] - c[')']


def part2(lines):
    """
    >>> part2([')'])
    1
    >>> part2(['()())'])
    5
    """
    floor = 0
    for index, b in enumerate(lines[0]):
        if b == '(':
            floor += 1
        elif b == ')':
            floor -= 1
        else:
            raise Exception
        if floor < 0:
            return index + 1


if __name__ == "__main__":
    data = load_input(__file__, 2015, '1')
    print(part1(data))
    print(part2(data))
