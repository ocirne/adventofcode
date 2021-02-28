from aoc.util import load_input
from sage.all import *


def count_part1(house):
    return sum(divisors(house)) * 10


def count_part2(house):
    return sum(d for d in divisors(house) if house // d <= 50) * 11


def run(lines, count_presents):
    target = int(lines[0])
    house = 1
    while True:
        count = count_presents(house)
        if count >= target:
            return house
        house += 1


def part1(lines):
    return run(lines, count_part1)


def part2(lines):
    return run(lines, count_part2)


if __name__ == "__main__":
    data = load_input(__file__, 2015, '20')
    print(part1(data))
    print(part2(data))
