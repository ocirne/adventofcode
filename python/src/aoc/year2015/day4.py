import hashlib

from aoc.util import load_input


def check(s, zeros):
    return hashlib.md5(s.encode()).hexdigest().startswith(zeros * "0")


def search(base, zeros):
    """
    >>> search('abcdef', 5)
    609043
    >>> search('pqrstuv', 5)
    1048970
    """
    i = 0
    while True:
        if check(base + str(i), zeros):
            return i
        i += 1


def part1(lines):
    return search(lines[0], 5)


def part2(lines):
    return search(lines[0], 6)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "4")
    print(part1(data))
    print(part2(data))
