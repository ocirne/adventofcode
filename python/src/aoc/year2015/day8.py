from collections import Counter

from aoc.util import load_input


def shrink(line):
    """
    >>> shrink('""')
    2
    >>> shrink('"abc"')
    2
    >>> shrink('"aaa\\\\"aaa"')
    3
    >>> shrink('"\\\\x27"')
    5
    """
    result = 0
    index = 0
    while index < len(line):
        character = line[index]
        if character == '"' and (index == 0 or index + 1 == len(line)):
            pass
        else:
            if character == "\\":
                if line[index + 1] == "\\":
                    index += 1
                elif line[index + 1] == '"':
                    index += 1
                elif line[index + 1] == "x" and line[index + 2].isascii() and line[index + 3].isascii():
                    index += 3
                else:
                    raise
            result += 1
        index += 1
    return len(line) - result


def expand(line):
    """
    >>> expand('""')
    4
    >>> expand('"abc"')
    4
    >>> expand('"aaa\\\\"aaa"')
    6
    >>> expand('"\\\\x27"')
    5
    """
    counter = Counter(line)
    return 2 + counter['"'] + counter["\\"]


def loop_sum(data, fun):
    return sum(fun(line) for line in map(str.strip, data))


def part1(lines):
    return loop_sum(lines, shrink)


def part2(lines):
    return loop_sum(lines, expand)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "8")
    print(part1(data))
    print(part2(data))
