from collections import Counter

RESULTS = []


def read_data(filename):
    f = open(filename)
    return sorted(int(line) for line in f.readlines())


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


def part1(data, total):
    """
    >>> part1([5, 5, 10, 15, 20], 25)
    4
    >>> part2()
    3
    """
    return combine(data, total)


def part2():
    counts = Counter(RESULTS)
    return counts[min(counts.keys())]


if __name__ == '__main__':
    inputData = read_data('input')
    print(part1(inputData, 150))
    print(part2())
