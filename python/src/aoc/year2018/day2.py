from collections import Counter
from itertools import combinations
from aoc.util import load_example, load_input


def part1(lines):
    """
    >>> part1(load_example(__file__, '2a'))
    12
    """
    count_two = 0
    count_three = 0
    for line in lines:
        m = Counter(line).values()
        if 2 in m:
            count_two += 1
        if 3 in m:
            count_three += 1
    return count_two * count_three


def count_diff(line1, line2):
    count = 0
    common_str = ""
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            count += 1
        else:
            common_str += line1[i]
    return count, common_str


def part2(lines):
    """
    >>> part2(load_example(__file__, '2b'))
    'fgij'
    """
    for line1, line2 in combinations(lines, 2):
        count, common = count_diff(line1, line2)
        if count == 1:
            return common


if __name__ == "__main__":
    data = load_input(__file__, 2018, "2")
    print(part1(data))
    print(part2(data))
