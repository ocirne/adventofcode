from pathlib import Path


def read_program(filename):
    f = open(filename)
    program = []
    for line in f.readlines():
        instruction, ops = line.strip().split(' ', maxsplit=1)
        program.append((instruction, ops.split(', ')))
    return program


def run(filename, init_a=0):
    """
    >>> run(Path(__file__).parent / 'reference')['a']
    2
    """
    program = read_program(filename)
    reg = {'a': init_a, 'b': 0}
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


if __name__ == '__main__':
    print(run('input')['b'])
    print(run('input', 1)['b'])
