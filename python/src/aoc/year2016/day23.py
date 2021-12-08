from aoc.util import load_input, load_example


class Instruction:
    def __init__(self, line):
        token = line.split()
        if len(token) == 3:
            self.cmd, self.x, self.y = token
            self.count = 2
        elif len(token) == 2:
            self.cmd, self.x = token
            self.y = None
            self.count = 1


def value_of(registers, x):
    try:
        return int(x)
    except ValueError:
        return registers[x]


def part1(lines, init_a=7):
    """
    >>> part1(load_example(__file__, "23"), 0)
    3
    """
    registers = {c: 0 for c in "abcd"}
    registers["a"] = init_a
    instructions = [Instruction(line) for line in lines]
    pp = 0
    while pp < len(instructions):
        ins = instructions[pp]
        if ins.cmd == "cpy":
            # cpy x y copies x (either an integer or the value of a register) into register y.
            if ins.y.isalpha():
                registers[ins.y] = value_of(registers, ins.x)
        elif ins.cmd == "inc":
            # inc x increases the value of register x by one.
            registers[ins.x] += 1
        elif ins.cmd == "dec":
            # dec x decreases the value of register x by one.
            registers[ins.x] -= 1
        elif ins.cmd == "jnz":
            # jnz x y jumps to an instruction y away (positive means forward; negative means backward),
            # but only if x is not zero.
            if value_of(registers, ins.x) != 0:
                pp += value_of(registers, ins.y) - 1
        elif ins.cmd == "tgl":
            tp = pp + value_of(registers, ins.x)
            # If an attempt is made to toggle an instruction outside the program, nothing happens.
            if 0 <= tp < len(instructions):
                tins = instructions[tp]
                if tins.count == 1:
                    # For one-argument instructions, inc becomes dec,
                    # and all other one-argument instructions become inc.
                    if tins.cmd == "inc":
                        tins.cmd = "dec"
                    else:
                        tins.cmd = "inc"
                if tins.count == 2:
                    # For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
                    if tins.cmd == "jnz":
                        tins.cmd = "cpy"
                    else:
                        tins.cmd = "jnz"
        pp += 1
    return registers["a"]


def part2(init_a=12):
    default = {24: True, 22: True, 20: True, 18: True}
    a = init_a
    b = a
    b -= 1
    while True:
        d = a
        a = d * b
        d -= 1
        b -= 1
        c = b
        d = c
        t = d
        d -= t
        c += t
        tp = 16 + c
        if 0 <= tp <= 25:
            if tp in default:
                default[tp] = not default[tp]
            else:
                raise Exception("unknown command %s to toggle" % tp)
        c = -16
        if default[18]:
            assert c == -16
        else:
            c = 1
            break
    c = 96
    while True:
        if default[20]:
            assert False
            if d != 0:
                print("Problem: weiter bei 20 + %s =" % d, 20 + d)
                raise
        else:
            d = 95
        while True:
            a += 1
            if default[22]:
                assert False
                d += 1
            else:
                d -= 1
            if d == 0:
                break
        if default[24]:
            assert False
            c += 1
        else:
            c -= 1
        if c == 0:
            break
    return a


if __name__ == "__main__":
    data = load_input(__file__, 2016, "23")
    print(part1(data))
    print(part2())
