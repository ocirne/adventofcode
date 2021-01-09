
from aoc2020 import puzzleInput


def run(data):
    total_valid = 0
    for line in data:
        range, letterw, password = line.split()
        first, second = map(int, range.split('-'))
        letter = letterw.split(':')[0]
        count = 0
        if password[first - 1] == letter:
            count += 1
        if password[second - 1] == letter:
            count += 1
        if count == 1:
            total_valid += 1
    return total_valid


assert run(puzzleInput('02/reference')) == 1

print(run(puzzleInput('02/input')))
