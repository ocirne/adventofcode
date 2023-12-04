from collections import defaultdict

from aoc.util import load_input, load_example


def matching_numbers(card):
    """
    >>> matching_numbers('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
    4
    >>> matching_numbers('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19')
    2
    >>> matching_numbers('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1')
    2
    >>> matching_numbers('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83')
    1
    >>> matching_numbers('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36')
    0
    >>> matching_numbers('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11')
    0
    """
    numbers = card.split(":")[1]
    win_str, have_str = numbers.split("|")
    win_set = set(win_str.split())
    have_set = set(have_str.split())
    return len(have_set.intersection(win_set))


def scratchcard_worth(card):
    """
    >>> scratchcard_worth('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
    8
    >>> scratchcard_worth('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19')
    2
    >>> scratchcard_worth('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1')
    2
    >>> scratchcard_worth('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83')
    1
    >>> scratchcard_worth('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36')
    0
    >>> scratchcard_worth('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11')
    0
    """
    s = matching_numbers(card)
    return 0 if s == 0 else 2 ** (s - 1)


def part1(lines):
    """
    >>> part1(load_example(__file__, "4"))
    13
    """
    return sum(scratchcard_worth(card) for card in lines)


def part2(lines):
    """
    >>> part2(load_example(__file__, "4"))
    30
    """
    copies = defaultdict(lambda: 1)
    total = 0
    for index, card in enumerate(lines):
        n = matching_numbers(card)
        total += copies[index]
        for i in range(1, n + 1):
            copies[index + i] += copies[index]
    return total


if __name__ == "__main__":
    data = load_input(__file__, 2023, "4")
    print(part1(data))
    print(part2(data))
