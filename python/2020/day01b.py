
from aoc2020 import puzzleInput

M = 2020


def run(data):
    d = [int(s) for s in data]
    p = {}
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            key = d[i] + d[j]
            if key < M:
                p[key] = d[i] * d[j]
    for x in d:
        y = M - x
        if y in p:
            return x * p[y]


assert run(puzzleInput('01/reference')) == 241861950

print(run(puzzleInput('01/input')))
