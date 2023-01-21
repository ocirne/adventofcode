from functools import cmp_to_key

from aoc.util import load_input, load_example


def cmp(a, b):
    return (a > b) - (a < b)


def compare(left, right):
    if type(left) == int and type(right) == int:
        return cmp(left, right)
    elif type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            t = compare(left[i], right[i])
            if t == 0:
                continue
            return t
        return cmp(len(left), len(right))
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    else:
        raise Exception


def packets_in_pairs(lines):
    it = iter(map(lambda s: s.strip(), lines))
    while True:
        left = next(it)
        right = next(it)
        yield eval(left), eval(right)
        if next(it, None) is None:
            break


def part1(lines):
    """
    >>> part1(load_example(__file__, "13"))
    13
    """
    return sum(index + 1 for index, (left, right) in enumerate(packets_in_pairs(lines)) if compare(left, right) < 0)


def packets(lines):
    it = iter(map(lambda s: s.strip(), lines))
    while True:
        left = next(it)
        right = next(it)
        yield eval(left)
        yield eval(right)
        if next(it, None) is None:
            break


def part2(lines):
    """
    >>> part2(load_example(__file__, "13"))
    140
    """
    dk1 = eval("[[2]]")
    dk2 = eval("[[6]]")
    u_ps = [dk1, dk2] + list(packets(lines))
    s_ps = sorted(u_ps, key=cmp_to_key(compare))
    return (s_ps.index(dk1) + 1) * (s_ps.index(dk2) + 1)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "13")
    print(part1(data))
    print(part2(data))
