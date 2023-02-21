from aoc.util import load_input, load_example


def rotate(values, i, x=0):
    f = next(index for index, item in enumerate(values) if item[x] == i)
    return values[f:] + values[:f]


def decrypt_grove(lines, key=1, rounds=1):
    values = list(enumerate(int(n) * key for n in lines))
    m = len(values)
    for _ in range(rounds):
        for i in range(m):
            values = rotate(values, i)
            item = values.pop(0)
            t = item[1] % (m - 1)
            values.insert(t, item)
    values = rotate(values, 0, 1)
    return sum(values[(i + 1) * 1000 % m][1] for i in range(3))


def part1(lines):
    """
    >>> part1(load_example(__file__, "20"))
    3
    """
    return decrypt_grove(lines)


def part2(lines):
    """
    >>> part2(load_example(__file__, "20"))
    1623178306
    """
    return decrypt_grove(lines, key=811589153, rounds=10)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "20")
    print(part1(data))
    print(part2(data))
