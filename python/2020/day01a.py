
from aoc2020 import puzzleInput

M = 2020


def run(data):
    d = {int(s) for s in data}
    for x in d:
        y = M - x
        if y in d:
            return x * y


assert run(puzzleInput('01/reference')) == 514579

print(run(puzzleInput('01/input')))
