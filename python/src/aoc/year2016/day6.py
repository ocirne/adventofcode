from collections import Counter

from aoc.util import load_input, load_example


def column_counts(lines, pos):
    result = ""
    for i in range(len(lines[0])):
        result += Counter(line[i] for line in lines).most_common()[pos][0]
    return result


def part1(lines):
    """
    >>> part1(load_example(__file__, "6"))
    'easter'
    """
    return column_counts(lines, 0)


def part2(lines):
    """
    >>> part2(load_example(__file__, "6"))
    'advent'
    """
    return column_counts(lines, -1)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "6")
    print(part1(data))
    print(part2(data))
