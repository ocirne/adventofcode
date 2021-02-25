
from sage.all import *


def count_part1(house):
    return sum(divisors(house)) * 10


def count_part2(house):
    return sum(d for d in divisors(house) if house // d <= 50) * 11


def run(target, count_presents):
    house = 1
    while True:
        count = count_presents(house)
        if count >= target:
            return house
        house += 1


if __name__ == '__main__':
    puzzleInput = int(open('input').readline())
    print(run(puzzleInput, count_part1))
    print(run(puzzleInput, count_part2))
