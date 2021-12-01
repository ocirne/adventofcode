from aoc.util import load_input, load_example


def part1(lines):
    """
    >>> part1(load_example(__file__, "1"))
    7
    """
    depths = list(map(int, lines))
    return sum(f < s for f, s in zip(depths, depths[1:]))


def part2(lines):
    """
    >>> part2(load_example(__file__, "1"))
    5
    """
    depths = list(map(int, lines))
    windows = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
    return sum(f < s for f, s in zip(windows, windows[1:]))


if __name__ == "__main__":
    data = load_input(__file__, 2021, "1")
    print(part1(data))
    print(part2(data))
