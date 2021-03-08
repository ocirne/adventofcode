from collections import defaultdict, Counter

from aoc.util import load_input, load_example


def prepare_rules(lines):
    it = iter(lines)
    start = next(it)[15]
    steps = int(next(it).split(" ")[5])

    rules = {}
    while True:
        empty = next(it, None)
        if empty is None:
            break
        current_state = next(it)[9]
        for i in range(2):
            next(it)
            next_value = int(next(it)[22])
            movement = -1 if next(it).strip().endswith("left.") else 1
            next_state = next(it)[26]
            rules[(current_state, i)] = (next_value, movement, next_state)
    return start, steps, rules


def part1(lines):
    """
    >>> part1(load_example(__file__, "25"))
    3
    """
    state, steps, rules = prepare_rules(lines)
    band = defaultdict(lambda: 0)
    p = 0
    for _ in range(steps):
        value = band[p]
        next_value, movement, state = rules[(state, value)]
        band[p] = next_value
        p += movement
    return Counter(band.values())[1]


def part2(lines):
    pass


if __name__ == "__main__":
    data = load_input(__file__, 2017, "25")
    print(part1(data))
