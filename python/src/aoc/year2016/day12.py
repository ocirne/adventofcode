from aoc.util import load_input, load_example


def dereference(registers, x):
    if x.isnumeric():
        return int(x)
    return registers[x]


def part1(lines):
    """
    >>> part1(load_example(__file__, "12"))
    42
    """
    registers = {c: 0 for c in "abcd"}
    pp = 0
    while pp < len(lines):
        token = lines[pp].split()
        if token[0] == "cpy":
            # cpy x y copies x (either an integer or the value of a register) into register y.
            _, px, y = token
            x = dereference(registers, px)
            registers[y] = x
        if token[0] == "inc":
            # inc x increases the value of register x by one.
            x = token[1]
            registers[x] += 1
        if token[0] == "dec":
            # dec x decreases the value of register x by one.
            x = token[1]
            registers[x] -= 1
        if token[0] == "jnz":
            # jnz x y jumps to an instruction y away (positive means forward; negative means backward),
            # but only if x is not zero.
            _, px, y = token
            x = dereference(registers, px)
            if x != 0:
                pp += int(y) - 1
        pp += 1
    return registers["a"]


def part2(lines):
    """
    >>> part2(load_example(__file__, "12"))
    """
    a = b = c = d = 0
    # cpy 1 a
    a = 1
    # cpy 1 b
    b = 1
    # cpy 26 d
    d = 26
    # jnz c 2
    if c != 0:
        # cpy 7 c
        c = 7
        while c != 0:
            # inc d
            d += 1
            # dec c
            c -= 1
            # jnz c -2
    while d != 0:
        # cpy a c
        c = a
        while b != 0:
            # inc a
            a += 1
            # dec b
            b -= 1
            # jnz b -2
        # cpy c b
        b = c
        # dec d
        d -= 1
        # jnz d -6
    # cpy 16 c
    c = 16
    while c != 0:
        # cpy 12 d
        d = 12
        while d != 0:
            # inc a
            a += 1
            # dec d
            d -= 1
            # jnz d -2
        # dec c
        c -= 1
        # jnz c -5
    return a


if __name__ == "__main__":
    data = load_input(__file__, 2016, "12")
    print(part1(data))
    print(part2(data))
