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


def deconstructed(inputs):
    z = 0
    for d in range(14):
        x = z % 26
        z //= D[d]
        x += A[d]
        if x != inputs[d]:
            z = 26 * z + inputs[d] + B[d]
    return z


#     0,  1,  2,  3,   4,   5,  6,  7,  8,  9, 10, 11, 12,  13
D = [1, 1, 1, 1, 26, 26, 1, 1, 26, 26, 1, 26, 26, 26]
A = [13, 12, 12, 10, -11, -13, 15, 10, -2, -6, 14, 0, -15, -4]
B = [8, 13, 8, 10, 12, 1, 13, 5, 10, 3, 2, 2, 12, 7]


def is_valid(d, i, z):
    x = z % 26
    z //= D[d]
    x += A[d]
    if x != i:
        z = 26 * z + i + B[d]
    if d == 3:
        return z < 456977, z
    if d == 7:
        return z < 456977, z
    if d == 10:
        return z < 17577, z
    if d == 11:
        return z < 677, z
    if d == 12:
        return z < 27, z
    return True, z


def dfs(d=0, acc=[], z0=0):
    if d == 14:
        print("stop", acc, z0)
        if z0 == 0:
            raise
        return
    for i in range(9, 0, -1):
        valid, z1 = is_valid(d, i, z0)
        if valid:
            dfs(d + 1, acc + [i], z1)


def part1(lines):
    #    for _ in range(100):
    #        inputs = [random.randint(1, 9) for _ in range(14)]
    #        print(inputs)
    #        r = reference(lines, inputs)
    #        d = deconstructed(inputs)
    #        assert r == d, "r %s d %s" % (r, d)
    dfs()


#    print(deconstructed([9 for _ in range(14)]))

#    print(reference(lines, c))
#    print(deconstructed(c))


def dfs2(d=0, acc=[], z0=0):
    if d == 14:
        print("stop", acc, z0)
        if z0 == 0:
            raise
        return
    for i in range(1, 10):
        valid, z1 = is_valid(d, i, z0)
        if valid:
            dfs2(d + 1, acc + [i], z1)


def part2(lines):
    dfs2()


if __name__ == "__main__":
    data = load_input(__file__, 2021, "24")
    print(part1(data))
    print(part2(data))
