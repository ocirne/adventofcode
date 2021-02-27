from collections import Counter
from math import prod
from aoc_util import example

MATCH = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}


def part1(lines):
    """
    >>> part1(example('10a'))
    35
    >>> part1(example('10b'))
    220
    """
    nums = sorted(map(int, lines))
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


def part2(lines):
    """
    >>> part2(example('10a'))
    8
    >>> part2(example('10b'))
    19208
    """
    raw_nums = list(map(int, lines))
    nums = sorted([0, max(raw_nums)+3] + raw_nums)
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    runs = run_detection(diffs)
    return prod(MATCH[i] for i in runs)
