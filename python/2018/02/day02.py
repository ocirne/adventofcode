from collections import Counter
from itertools import combinations
from pathlib import Path


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference_a')
    12
    """
    data = open(filename).readlines()
    count_two = 0
    count_three = 0
    for line in data:
        m = Counter(line).values()
        if 2 in m:
            count_two += 1
        if 3 in m:
            count_three += 1
    return count_two * count_three


def count_diff(line1, line2):
    count = 0
    common_str = ''
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            count += 1
        else:
            common_str += line1[i]
    return count, common_str


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference_b')
    'fgij'
    """
    data = open(filename).readlines()
    for line1, line2 in combinations(data, 2):
        count, common = count_diff(line1.strip(), line2.strip())
        if count == 1:
            return common


if __name__ == "__main__":
    print(part1("input"))
    print(part2("input"))
