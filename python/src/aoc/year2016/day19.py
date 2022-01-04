from aoc.util import load_input


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
    >>> part1(['5'])
    2
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2016, "19")
    print(part1(data))
    print(part2(data))
