from collections import Counter, defaultdict
from itertools import product

from aoc.util import load_input, load_example


def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    739785
    """
    p1, p2 = (int(line.split()[4]) for line in lines)
    score1, score2 = 0, 0
    print(p1, p2)
    dice = 1
    total_roll = 0
    while True:
        print(p1, p2)
        for _ in range(3):
            print("dice", dice)
            p1 += dice
            while p1 > 10:
                p1 -= 10
            dice += 1
            total_roll += 1
            if dice > 100:
                dice = 1
        score1 += p1
        if score1 >= 1000:
            print("player 1 wins with score", score1)
            return total_roll * score2

        for _ in range(3):
            print("dice", dice)
            p2 += dice
            while p2 > 10:
                p2 -= 10
            dice += 1
            total_roll += 1
            if dice > 100:
                dice = 1
        score2 += p2
        if score2 >= 1000:
            print("player 2 wins")
            return total_roll * score1


def sums():
    a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    return Counter(sum(p) for p in product(*a))


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    444356092776315
    """
    p1, p2 = (int(line.split()[4]) for line in lines)
    # Wie oft kann welche Position erreicht werden, und welchen Score hat man dort?
    p11 = defaultdict(lambda: 0)
    p11[p1, 0, p2, 0] = 1
    c = sums()
    print(c)
    total1 = 0
    total2 = 0
    while p11:
        print(len(p11), sum(p11.values()))

        tmp = defaultdict(lambda: 0)
        for (p1, s1, p2, s2), count1 in p11.items():
            for hop, count2 in c.items():
                next_position = p1 + hop
                while next_position > 10:
                    next_position -= 10
                next_score = s1 + next_position
                cases = count1 * count2
                if next_score >= 21:
                    total1 += cases
                else:
                    tmp[next_position, next_score, p2, s2] += cases
        p11 = tmp
        print(len(p11), sum(p11.values()))

        tmp = defaultdict(lambda: 0)
        for (p1, s1, p2, s2), count1 in p11.items():
            for hop, count2 in c.items():
                next_position = p2 + hop
                while next_position > 10:
                    next_position -= 10
                next_score = s2 + next_position
                cases = count1 * count2
                if next_score >= 21:
                    total2 += cases
                else:
                    tmp[p1, s1, next_position, next_score] += cases
        p11 = tmp
    print(total1, total2)
    print(444356092776315, 341960390180808, "ref")
    return max(total1, total2)


if __name__ == "__main__":
    #    assert part1(load_example(__file__, "21")) == 739785
    assert part2(load_example(__file__, "21")) == 444356092776315
    data = load_input(__file__, 2021, "21")
    #    print(part1(data))
    print(part2(data))
