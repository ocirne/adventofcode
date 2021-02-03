from pathlib import Path


def read_program(filename):
    f = open(filename, 'r')
    program = []
    for line in f.readlines():
        instruction, ops = line.strip().split(' ', maxsplit=1)
        program.append((instruction, ops.split(', ')))
    return program


def run(program):
    reg = {'a': 0, 'b': 0}
    pp = 0
    while True:
        if pp >= len(program):
            return reg
        ins, ops = program[pp]
        if ins == 'inc':
            r = ops[0]
            reg[r] += 1
        elif ins == 'jmp':
            offset = int(ops[0])
            pp += offset - 1
        elif ins == 'jie':
            r, offset = ops
            if reg[r] % 2 == 0:
                pp += int(offset) - 1
        elif ins == 'jio':
            r, offset = ops
            if reg[r] == 1:
                pp += int(offset) - 1
        elif ins == 'hlf':
            r = ops[0]
            reg[r] //= 2
        elif ins == 'tpl':
            r = ops[0]
            reg[r] *= 3
        pp += 1


def part1(filename, register):
    """
    >>> part1(Path(__file__).parent / 'reference', 'a')
    2
    """
    program = read_program(filename)
    return run(program)[register]


if __name__ == '__main__':
    print(part1('input', 'b'))
