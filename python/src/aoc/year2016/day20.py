from aoc.util import load_input, load_example


def to_ranges(lines):
    return [tuple(map(int, line.split("-"))) for line in lines]


def find_next_free(ranges, start_value=0):
    candidate = start_value
    while True:
        next_candidates = [y for x, y in ranges if x <= candidate <= y]
        if not next_candidates:
            return candidate
        candidate = max(next_candidates) + 1


def find_next_blocked(ranges, start_value):
    next_candidates = [x for x, _ in ranges if start_value <= x]
    if not next_candidates:
        return None
    return min(next_candidates)


def part1(lines):
    """
    >>> part1(load_example(__file__, "20"))
    3
    """
    return find_next_free(to_ranges(lines))


def part2(lines, maximum=4294967295):
    """
    >>> part2(load_example(__file__, "20"), 9)
    2
    """
    ranges = to_ranges(lines)
    total = 0
    next_blocked = 0
    while True:
        next_free = find_next_free(ranges, next_blocked)
        next_blocked = find_next_blocked(ranges, next_free)
        if next_blocked is None:
            return total + (maximum - next_free + 1)
        total += next_blocked - next_free


if __name__ == "__main__":
    data = load_input(__file__, 2016, "20")
    print(part1(data))
    print(part2(data))
