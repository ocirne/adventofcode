from collections import Counter

RESULTS = []


def prepare_data(lines):
    return sorted(int(line) for line in lines)


def combine(data, rest, acc=None):
    if acc is None:
        acc = []
    if rest < 0:
        return 0
    if rest == 0:
        RESULTS.append(len(acc))
        return 1
    if not data:
        return 0
    return combine(data[1:], rest, acc) + combine(data[1:], rest - data[0], acc + [data[0]])


def part1(lines, total=150):
    """
    >>> part1([5, 5, 10, 15, 20], 25)
    4
    >>> part2([])
    3
    """
    data = prepare_data(lines)
    return combine(data, total)


def part2(lines):
    part1(lines)
    counts = Counter(RESULTS)
    return counts[min(counts.keys())]
