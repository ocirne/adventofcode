from collections import Counter, defaultdict
from itertools import product

from aoc.util import load_input, load_example


def mod1(x, m):
    """
    >>> mod1(1, 10)
    1
    >>> mod1(10, 10)
    10
    >>> mod1(11, 10)
    1
    >>> mod1(15, 10)
    5
    """
    return (x - 1) % m + 1


def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    739785
    """
    p1, p2 = (int(line.split()[4]) for line in lines)
    score1, score2 = 0, 0
    dice = 1
    total_roll = 0
    while True:
        for _ in range(3):
            p1 = mod1(p1 + dice, 10)
            dice = mod1(dice + 1, 100)
            total_roll += 1
        score1 += p1
        if score1 >= 1000:
            return total_roll * score2

        for _ in range(3):
            p2 = mod1(p2 + dice, 10)
            dice = mod1(dice + 1, 100)
            total_roll += 1
        score2 += p2
        if score2 >= 1000:
            return total_roll * score1


def counts_per_round():
    return Counter(sum(p) for p in product([1, 2, 3], repeat=3))


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    444356092776315
    """
    p1, p2 = (int(line.split()[4]) for line in lines)
    state = defaultdict(lambda: 0)
    state[p1, 0, p2, 0] = 1
    counts = counts_per_round()
    total1 = 0
    total2 = 0
    while state:
        tmp = defaultdict(lambda: 0)
        for (p1, s1, p2, s2), count1 in state.items():
            for hop, count2 in counts.items():
                next_position = mod1(p1 + hop, 10)
                next_score = s1 + next_position
                cases = count1 * count2
                if next_score >= 21:
                    total1 += cases
                else:
                    tmp[next_position, next_score, p2, s2] += cases
        state = tmp

        tmp = defaultdict(lambda: 0)
        for (p1, s1, p2, s2), count1 in state.items():
            for hop, count2 in counts.items():
                next_position = mod1(p2 + hop, 10)
                next_score = s2 + next_position
                cases = count1 * count2
                if next_score >= 21:
                    total2 += cases
                else:
                    tmp[p1, s1, next_position, next_score] += cases
        state = tmp
    return max(total1, total2)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "21")
    print(part1(data))
    print(part2(data))
