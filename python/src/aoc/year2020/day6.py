from collections import defaultdict
from aoc.util import example


def part1(lines):
    """
    >>> part1(example(__file__, '6'))
    11
    """
    answers = []
    a = {}
    for line in lines:
        if not line.strip():
            answers.append(len(a.keys()))
            a = {}
        else:
            for k in line.strip():
                a[k] = True
    answers.append(len(a.keys()))
    return sum(answers)


def part2(lines):
    """
    >>> part2(example(__file__, '6'))
    6
    """
    answers = []
    a = defaultdict(lambda: 0)
    count_people = 0
    for line in lines:
        if not line.strip():
            answers.append(len([1 for v in a.values() if v == count_people]))
            a = defaultdict(lambda: 0)
            count_people = 0
        else:
            for k in line.strip():
                a[k] += 1
            count_people += 1
    answers.append(len([1 for v in a.values() if v == count_people]))
    return sum(answers)
