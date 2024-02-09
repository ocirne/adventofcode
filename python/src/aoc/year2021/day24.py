from random import randint

from aoc.util import load_input


def reference(lines, inputs):
    reg = {r: 0 for r in "wxyz"}
    i = 0
    for line in lines:
        token = line.split()
        if token[0] == "inp":
            a = token[1]
            reg[a] = inputs[i]
            i += 1
        else:
            op, a, b = token
            if b in "wxyz":
                b = reg[b]
            else:
                b = int(b)
            if op == "add":
                reg[a] += b
            elif op == "mul":
                reg[a] *= b
            elif op == "div":
                if reg[a] < 0 or b < 0:
                    raise
                reg[a] //= b
            elif op == "mod":
                reg[a] %= b
            elif op == "eql":
                reg[a] = int(reg[a] == b)
            else:
                raise
    return reg["z"]


D = [1, 1, 1, 1, 26, 26, 1, 1, 26, 26, 1, 26, 26, 26]
A = [13, 12, 12, 10, -11, -13, 15, 10, -2, -6, 14, 0, -15, -4]
B = [8, 13, 8, 10, 12, 1, 13, 5, 10, 3, 2, 2, 12, 7]


def deconstructed(inputs):
    z = 0
    for d in range(14):
        x = z % 26
        z //= D[d]
        x += A[d]
        if x != inputs[d]:
            z = 26 * z + inputs[d] + B[d]
    return z


class ModelNumber:
    def __init__(self, lines, start, stop, step):
        self.lines = lines
        self.start = start
        self.stop = stop
        self.step = step

    def _is_valid(self, d, i, z):
        x = z % 26
        z //= D[d]
        x += A[d]
        if x != i:
            z = 26 * z + i + B[d]
        if d == 3:  # < 26**4, 250_000 is good enough
            return z < 250_000, z
        if d == 7:  # < 26**4
            return z < 250_000, z
        if d == 10:  # < 26**3
            return z < 10_000, z
        if d == 11:  # < 26*2
            return z < 400, z
        if d == 12:  # < 26**1
            return z < 15, z
        return True, z

    def dfs(self, d=0, acc=None, z0=0):
        if acc is None:
            acc = []
        if d == 14:
            if z0 == 0:
                assert reference(self.lines, acc) == deconstructed(acc) == 0
                return "".join(str(c) for c in acc)
            return
        for i in range(self.start, self.stop, self.step):
            valid, z1 = self._is_valid(d, i, z0)
            if valid:
                t = self.dfs(d + 1, acc + [i], z1)
                if t is not None:
                    return t


def part1(lines):
    return ModelNumber(lines, 9, 0, -1).dfs()


def part2(lines):
    return ModelNumber(lines, 1, 10, 1).dfs()


if __name__ == "__main__":
    data = load_input(__file__, 2021, "24")
    print(part1(data))
    print(part2(data))
