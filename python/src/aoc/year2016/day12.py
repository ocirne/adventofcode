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
    pass


if __name__ == "__main__":
    data = load_input(__file__, 2016, "12")
    print(part1(data))
    print(part2(data))
