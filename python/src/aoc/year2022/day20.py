from aoc.util import load_input, load_example


def rotate(values, i, x=0):
    f = next(index for index, item in enumerate(values) if item[x] == i)
    return values[f:] + values[:f]


def part1(lines):
    """
    >>> part1(load_example(__file__, "20"))
    3
    """
    values = list(enumerate(map(int, lines)))
    m = len(values)
    print([k for _, k in values])
    for i in range(m):
        values = rotate(values, i)
        print()
        #        print(i, values)
        item = values.pop(0)
        t = (item[1]) % (m - 1)
        values.insert(t, item)
        print("Move value %s from %s to %s" % (item[1], 0, t))
    #        print([k for _, k in values])
    print("result", [k for _, k in values])
    values = rotate(values, 0, 1)
    v1 = values[(+1000) % m][1]
    v2 = values[(+2000) % m][1]
    v3 = values[(+3000) % m][1]
    return v1 + v2 + v3


def part2(lines):
    """
    >>> part2(load_example(__file__, "20"))
    1623178306
    """
    values = list(enumerate(int(n) * 811589153 for n in lines))
    m = len(values)
    print([k for _, k in values])
    for _ in range(10):
        for i in range(m):
            values = rotate(values, i)
            print()
            #        print(i, values)
            item = values.pop(0)
            t = (item[1]) % (m - 1)
            values.insert(t, item)
            print("Move value %s from %s to %s" % (item[1], 0, t))
        #        print([k for _, k in values])
    print("result", [k for _, k in values])
    values = rotate(values, 0, 1)
    v1 = values[(+1000) % m][1]
    v2 = values[(+2000) % m][1]
    v3 = values[(+3000) % m][1]
    return v1 + v2 + v3


if __name__ == "__main__":
    data = load_input(__file__, 2022, "20")
    #    data = load_example(__file__, "20")
    #    print(part1(data))
    print(part2(data))
