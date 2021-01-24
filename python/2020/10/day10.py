from collections import Counter
from math import prod
from pathlib import Path

MATCH = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference_a')
    35
    >>> part1(Path(__file__).parent / 'reference_b')
    220
    """
    f = open(filename, 'r')
    nums = sorted(map(int, f.readlines()))
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    c = Counter(diffs)
    return (c[1]+1) * (c[3]+1)


def run_detection(diffs):
    count = 0
    runs = []
    for v in diffs:
        if v == 1:
            count += 1
        else:
            runs.append(count)
            count = 0
    return runs


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference_a')
    8
    >>> part2(Path(__file__).parent / 'reference_b')
    19208
    """
    f = open(filename, 'r')
    raw_nums = list(map(int, f.readlines()))
    nums = sorted([0, max(raw_nums)+3] + raw_nums)
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    runs = run_detection(diffs)
    return prod(MATCH[i] for i in runs)


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
