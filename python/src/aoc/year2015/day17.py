from collections import Counter
from aoc.util import load_input

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
    return combine(data[1:], rest, acc) + combine(
        data[1:], rest - data[0], acc + [data[0]]
    )


def part1(lines, total=150):
    """
    >>> part1([5, 5, 10, 15, 20], 25)
    4
    """
    data = prepare_data(lines)
    return combine(data, total)


def part2(lines, total=150):
    """
    >>> part2([5, 5, 10, 15, 20], 25)
    3
    """
    global RESULTS
    RESULTS = []
    part1(lines, total)
    counts = Counter(RESULTS)
    return counts[min(counts.keys())]


if __name__ == "__main__":
    data = load_input(__file__, 2015, "17")
    print(part1(data))
    print(part2(data))
