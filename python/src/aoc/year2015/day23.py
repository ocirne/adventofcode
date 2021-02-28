from aoc.util import load_example, load_input


def prepare_program(lines):
    program = []
    for line in lines:
        instruction, ops = line.strip().split(" ", maxsplit=1)
        program.append((instruction, ops.split(", ")))
    return program


def run(lines, init_a=0):
    """
    >>> run(load_example(__file__, '23'))['a']
    2
    """
    program = prepare_program(lines)
    reg = {"a": init_a, "b": 0}
    pp = 0
    while True:
        if pp >= len(program):
            return reg
        ins, ops = program[pp]
        if ins == "inc":
            r = ops[0]
            reg[r] += 1
        elif ins == "jmp":
            offset = int(ops[0])
            pp += offset - 1
        elif ins == "jie":
            r, offset = ops
            if reg[r] % 2 == 0:
                pp += int(offset) - 1
        elif ins == "jio":
            r, offset = ops
            if reg[r] == 1:
                pp += int(offset) - 1
        elif ins == "hlf":
            r = ops[0]
            reg[r] //= 2
        elif ins == "tpl":
            r = ops[0]
            reg[r] *= 3
        pp += 1


def part1(lines):
    return run(lines)["b"]


def part2(lines):
    return run(lines, 1)["b"]


if __name__ == "__main__":
    data = load_input(__file__, 2015, "23")
    print(part1(data))
    print(part2(data))
