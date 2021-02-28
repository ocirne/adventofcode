from collections import defaultdict
from itertools import permutations
from aoc.util import load_example, load_input


def prepare_data(lines, with_me):
    guests = {}
    happiness = defaultdict(lambda: 0)
    for line in lines:
        token = line.strip().strip(".").split()
        guest, direction, value, neighbor = [token[i] for i in [0, 2, 3, 10]]
        guests[guest] = True
        if direction == "gain":
            happiness[(guest, neighbor)] += int(value)
            happiness[(neighbor, guest)] += int(value)
        elif direction == "lose":
            happiness[(guest, neighbor)] -= int(value)
            happiness[(neighbor, guest)] -= int(value)
        else:
            raise
    if with_me:
        for guest in guests.keys():
            happiness[(guest, "me")] = 0
            happiness[("me", guest)] = 0
        guests["me"] = True
    return list(guests.keys()), happiness


def calc_happiness(happiness, arrangement):
    return happiness[(arrangement[0], arrangement[-1])] + sum(
        happiness[(arrangement[i - 1], arrangement[i])]
        for i in range(1, len(arrangement))
    )


def run(lines, with_me):
    """
    >>> run(load_example(__file__, '13'), False)
    330
    """
    guests, happiness = prepare_data(lines, with_me)
    return max(
        calc_happiness(happiness, arrangement) for arrangement in permutations(guests)
    )


def part1(lines):
    return run(lines, with_me=False)


def part2(lines):
    return run(lines, with_me=True)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "13")
    print(part1(data))
    print(part2(data))
