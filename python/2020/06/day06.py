from collections import defaultdict
from pathlib import Path


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    11
    """
    f = open(filename, 'r')
    answers = []
    a = {}
    for line in f.readlines():
        if not line.strip():
            answers.append(len(a.keys()))
            a = {}
        else:
            for k in line.strip():
                a[k] = True
    answers.append(len(a.keys()))
    return sum(answers)


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    6
    """
    f = open(filename, 'r')
    answers = []
    a = defaultdict(lambda: 0)
    count_people = 0
    for line in f.readlines():
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


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
