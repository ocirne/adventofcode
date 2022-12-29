from aoc.util import load_input, load_example


def calorieSums(lines):
    s = 0
    for line in lines:
        try:
            s += int(line)
        except ValueError:
            yield s
            s = 0
    yield s


def part1(lines):
    """
    >>> part1(load_example(__file__, "1"))
    24000
    """
    return max(calorieSums(lines))


def part2(lines):
    """
    >>> part2(load_example(__file__, "1"))
    45000
    """
    return sum(sorted(calorieSums(lines))[-3:])


if __name__ == "__main__":
    data = load_input(__file__, 2022, "1")
    print(part1(data))
    print(part2(data))
