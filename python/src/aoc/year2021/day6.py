from collections import Counter, defaultdict

from aoc.util import load_input, load_example


def simulate(lines, days):
    """
    >>> simulate(load_example(__file__, "6"), 18)
    26
    """
    state = Counter(map(int, lines[0].split(",")))
    for i in range(days):
        next_state = defaultdict(lambda: 0)
        for k, v in state.items():
            if k == 0:
                next_state[6] += v
                next_state[8] += v
            else:
                next_state[k - 1] += v
        state = next_state
    return sum(state.values())


def part1(lines):
    """
    >>> part1(load_example(__file__, "6"))
    5934
    """
    return simulate(lines, 80)


def part2(lines):
    """
    >>> part2(load_example(__file__, "6"))
    26984457539
    """
    return simulate(lines, 256)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "6")
    print(part1(data))
    print(part2(data))
