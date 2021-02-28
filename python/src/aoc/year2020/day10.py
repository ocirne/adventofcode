from collections import Counter
from math import prod
from aoc.util import load_example, load_input

MATCH = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}


def part1(lines):
    """
    >>> part1(load_example(__file__, '10a'))
    35
    >>> part1(load_example(__file__, '10b'))
    220
    """
    nums = sorted(map(int, lines))
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    c = Counter(diffs)
    return (c[1] + 1) * (c[3] + 1)


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
    >>> part2(load_example(__file__, '10a'))
    8
    >>> part2(load_example(__file__, '10b'))
    19208
    """
    raw_nums = list(map(int, lines))
    nums = sorted([0, max(raw_nums) + 3] + raw_nums)
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    runs = run_detection(diffs)
    return prod(MATCH[i] for i in runs)


if __name__ == "__main__":
    data = load_input(__file__, 2020, "10")
    print(part1(data))
    print(part2(data))
