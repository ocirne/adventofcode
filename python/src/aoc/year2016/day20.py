from aoc.util import load_input, load_example


def part1(lines):
    """
    >>> part1(load_example(__file__, "20"))
    3
    """
    ranges = [tuple(map(int, line.split("-"))) for line in lines]
    candidate = 0
    while True:
        next_candidates = [y for x, y in ranges if x <= candidate <= y]
        if not next_candidates:
            return candidate
        candidate = max(next_candidates) + 1


if __name__ == "__main__":
    data = load_input(__file__, 2016, "20")
    print(part1(data))
#    print(part2(data))
