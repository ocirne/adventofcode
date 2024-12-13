from aoc.util import load_input, load_example

from itertools import product
import re

BUTTON_A_PATTERN = r"Button A: X\+(\d+), Y\+(\d+)"
BUTTON_B_PATTERN = r"Button B: X\+(\d+), Y\+(\d+)"
PRIZE_PATTERN = r"Prize: X=(\d+), Y=(\d+)"


def go_bonkers(iax, iay, ibx, iby, ipx, ipy):
    all_a = [(f*3, f*iax, f*iay) for f in range(101)]
    all_b = [(f*1, f*ibx, f*iby) for f in range(101)]
    foo = []
    for (ca, ax, ay), (cb, bx, by) in product(all_a, all_b):
        cp, px, py = ca + cb, ax+bx, ay+by
        if px == ipx and py == ipy:
            foo.append(cp)
    return min(foo) if foo else 0


def part1(lines):
    """
    >>> part1(load_example(__file__, "13"))
    480
    """
    total = 0
    for line in lines:
        a = re.search(BUTTON_A_PATTERN, line)
        if a:
            ax, ay = map(int, a.groups())
        b = re.search(BUTTON_B_PATTERN, line)
        if b:
            bx, by = map(int, b.groups())
        p = re.search(PRIZE_PATTERN, line)
        if p:
            px, py = map(int, p.groups())
#            print('prize', p.groups(), ax, ay, bx, by, px, py)
            total += go_bonkers(ax, ay, bx, by, px, py)
    return total

def go_bonkers2(iax, iay, ibx, iby, ipx, ipy):

    # (px - b * bx) / ax = a

    # ax * py - ax * b * by = ay * px - ay * b * bx
    # b  = (ay * px - ax * py) / (ay * bx - ax * by)
    # c = b * 1 + (px - b * bx) / ax * 3

    # c = (ay * px - ax * py) / (ay * bx - ax * by) * 1 + (px - (ay * px - ax * py) / (ay * bx - ax * by) * bx) / ax * 3

    all_a = [(a*3, a*iax, a*iay) for a in range(101)]
    all_b = [(b*1, b*ibx, b*iby) for b in range(101)]
    foo = []
    for (ca, ax, ay), (cb, bx, by) in product(all_a, all_b):
        cp, px, py = ca + cb, ax+bx, ay+by
        if px == ipx and py == ipy:
            foo.append(cp)
    t1 = (iay * ipx - iax * ipy)
    t2 = (iay * ibx - iax * iby)
    b = t1 / t2
    a = (ipx - b * ibx) / iax
    print(t1, t2, 'a', a, 'b', b)
    if a > 0 and int(a) == a and b > 0 and int(b) == b:
        cost = b + 3 * a
        return int(cost)
    return 0

def part2(lines):
    total = 0
    for line in lines:
        a = re.search(BUTTON_A_PATTERN, line)
        if a:
            ax, ay = map(int, a.groups())
        b = re.search(BUTTON_B_PATTERN, line)
        if b:
            bx, by = map(int, b.groups())
        p = re.search(PRIZE_PATTERN, line)
        if p:
            px, py = map(int, p.groups())
            #            print('prize', p.groups(), ax, ay, bx, by, px, py)
            total += go_bonkers2(ax, ay, bx, by, px+10000000000000, py+10000000000000)
    return total


if __name__ == "__main__":
    #data = load_example(__file__, "13")
    data = load_input(__file__, 2024, "13")
    #print(part1(data))
    print(part2(data))
