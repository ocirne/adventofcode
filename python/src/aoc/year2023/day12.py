from aoc.util import load_input, load_example


def dot(springs, pattern, result):
    return rec(springs[1:], pattern, result + ".")


def spring(springs, pattern, result):
    p = pattern[0]
    if p > len(springs):
        return 0
    for i in range(p):
        if springs[i] == ".":
            return 0
    if len(springs) > p and springs[p] == "#":
        return 0
    return rec(springs[p + 1 :], pattern[1:], result + p * "#" + ".")


def rec(springs, pattern, result=""):
    #    print('s %10s p %10s r %-10s' % (springs, pattern, result))
    if all(s != "#" for s in springs) and not pattern:
        #        print("**********", result, "************")
        return 1
    if springs == "" or not pattern:
        return 0
    total = 0
    c = springs[0]
    if c == ".":
        total += dot(springs, pattern, result)
    elif c == "#":
        total += spring(springs, pattern, result)
    elif c == "?":
        total += dot(springs, pattern, result) + spring(springs, pattern, result)
    return total


def count_arrangements(springs, pattern):
    p = [int(n) for n in pattern.split(",")]
    print(springs)
    print(p)
    return rec(springs, p)


def part1(lines):
    """
    >>> part1(load_example(__file__, "12"))
    21
    """
    total = 0
    for i, line in enumerate(lines):
        springs, pattern = line.split()
        tmp = count_arrangements(springs, pattern)
        print(i, tmp)
        total += tmp
    return total


def count_arrangements2(spring, pattern):
    return -1


def part2(lines):
    """
    >>> part2(load_example(__file__, "12"))
    525152
    """
    total = 0
    for i, line in enumerate(lines):
        springs, pattern = line.split()
        tmp = count_arrangements2("?".join(5 * [springs]), ",".join(5 * [pattern]))
        print(i, tmp)
        total += tmp
    return total


if __name__ == "__main__":
    data = load_input(__file__, 2023, "12")
    #    data = load_example(__file__, "12")
    #    print(part1(data))
    print(part2(data))
