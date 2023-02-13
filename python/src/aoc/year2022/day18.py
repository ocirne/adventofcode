from aoc.util import load_input, load_example


def part1(lines):
    """
    >>> part1(["1,1,1", "2,1,1"])
    10
    >>> part1(load_example(__file__, "18"))
    64
    """
    c = {tuple(map(int, line.strip().split(","))) for line in lines}
    return sum(
        int((x + d, y, z) not in c) + int((x, y + d, z) not in c) + int((x, y, z + d) not in c)
        for x, y, z in c
        for d in (-1, +1)
    )


def part2(lines):
    """
    >>> part2(load_example(__file__, "18"))
    58
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2022, "18")
    #    data = load_example(__file__, "18")
    print(part1(data))
#    print(part2(data))
