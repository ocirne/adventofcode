from aoc.util import load_input
from sortedcontainers import SortedList


def part1(lines):
    """
    >>> part1(['5'])
    3
    """
    count_elves = int(lines[0])
    elves = list(range(1, count_elves)) + [0]
    current = 0
    for i in range(count_elves - 1):
        next_wp = elves[current]
        next_next_wp = elves[next_wp]
        elves[current] = next_next_wp
        elves[next_wp] = -1
        current = next_next_wp
    return elves.index(max(elves)) + 1


def part2(lines):
    """
    >>> part2(['5'])
    2
    """
    count_elves = int(lines[0])
    elves = SortedList(range(count_elves))
    current_index = 0
    while len(elves) > 1:
        opposite_index = (current_index + len(elves) // 2) % len(elves)
        elves.pop(opposite_index)
        if opposite_index > current_index:
            current_index += 1
        if current_index >= len(elves):
            current_index = 0
    return elves[0] + 1


if __name__ == "__main__":
    data = load_input(__file__, 2016, "19")
    print(part1(data))
    print(part2(data))
