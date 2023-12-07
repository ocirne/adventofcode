from collections import Counter

from aoc.util import load_input, load_example


def foo(hand):
    """
    A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
    ->
    e, d, c, b, a, 9, 8, 7, 6, 5, 4, 3, 2
    """
    for v, r in zip("AKQJT", "edcba"):
        hand = hand.replace(v, r)
    c = [w[1] for w in Counter(hand).most_common()][:2]
    if len(c) == 1:
        return "50-%s" % hand
    return "%d%d-%s" % (c[0], c[1], hand)


def part1(lines):
    """
    >>> part1(load_example(__file__, "7"))
    6440
    """
    d = {}
    for line in lines:
        hand, bid = line.split()
        print(foo(hand))
        d[foo(hand)] = int(bid)
    return sum(i * bid for i, (_, bid) in enumerate(sorted(d.items()), start=1))


def part2(lines):
    """
    >>> part2(load_example(__file__, "7"))
    71503
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "7")
    print(part1(data))
#    print(part2(data))
