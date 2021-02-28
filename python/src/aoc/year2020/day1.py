from aoc.util import load_example, load_input

M = 2020


def part1(lines):
    """
    >>> part1(load_example(__file__, '1'))
    514579
    """
    d = {int(s) for s in lines}
    for x in d:
        y = M - x
        if y in d:
            return x * y


def part2(lines):
    """
    >>> part2(load_example(__file__, '1'))
    241861950
    """
    d = [int(s) for s in lines]
    p = {}
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            key = d[i] + d[j]
            if key < M:
                p[key] = d[i] * d[j]
    for x in d:
        y = M - x
        if y in p:
            return x * p[y]


if __name__ == "__main__":
    data = load_input(__file__, 2020, '1')
    print(part1(data))
    print(part2(data))
