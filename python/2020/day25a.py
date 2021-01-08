
from aoc2020 import puzzleInput

M = 20201227
S = 7


def decrypt(key):
    s = S
    e = 1
    while True:
        s = (s * S) % M
        e += 1
        if s == key:
            return e


def run(data):
    key1, key2 = (int(v) for v in data)
    e1 = decrypt(key1)
    e2 = decrypt(key2)
    return pow(S, e1*e2, M)


assert run(puzzleInput('2020/25/reference')) == 14897079

print(run(puzzleInput('2020/25/input')))
