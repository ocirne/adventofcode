from collections import Counter

from aoc.util import load_input, load_example


def hand_type(hand):
    """
    >>> hand_type('42424')
    '32'
    >>> hand_type('12345')
    '11'
    >>> hand_type('55555')
    '50'
    """
    c = [w[1] for w in Counter(hand).most_common()][:2]
    if len(c) == 1:
        return "50"
    return "%d%d" % (c[0], c[1])


def best_hand(hand):
    """
    A, K, Q, J, T, 9, ..., 2
    ->
    e, d, c, b, a, 9, ..., 2

    >>> best_hand('AKQJT')
    '11-edcba'
    >>> best_hand('42424')
    '32-42424'
    """
    for v, r in zip("AKQJT", "edcba"):
        hand = hand.replace(v, r)
    t = hand_type(hand)
    return "%s-%s" % (t, hand)


def find_best_replacement(hand):
    for r in "dcba98765432":
        hand2 = hand.replace("0", r)
        t = hand_type(hand2)
        yield "%s-%s" % (t, hand2), "%s-%s" % (t, hand)


def best_hand_with_joker(hand):
    """
    A, K, Q, T, 9, ..., 2, J
    ->
    d, c, b, a, 9, ..., 2, 0
    """
    for v, r in zip("AKQTJ", "dcba0"):
        hand = hand.replace(v, r)
    return max(find_best_replacement(hand))[1]


def total_winnings(lines, f):
    d = {f(hand): int(bid) for hand, bid in (line.split() for line in lines)}
    return sum(bid * rank for rank, (_, bid) in enumerate(sorted(d.items()), start=1))


def part1(lines):
    """
    >>> part1(load_example(__file__, "7"))
    6440
    """
    return total_winnings(lines, best_hand)


def part2(lines):
    """
    >>> part2(load_example(__file__, "7"))
    5905
    """
    return total_winnings(lines, best_hand_with_joker)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "7")
    print(part1(data))
    print(part2(data))
