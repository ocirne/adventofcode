from aoc.util import load_example, load_input


def prepare_ops(lines):
    ops = []
    for line in lines:
        op, arg = line.strip().split()
        ops.append((op, int(arg)))
    return ops


def run_program(ops, part):
    p = 0
    acc = 0
    visited = {}
    while True:
        op, arg = ops[p]
        if op == 'acc':
            acc += arg
            p += 1
        elif op == 'jmp':
            p += arg
        elif op == 'nop':
            p += 1
        else:
            raise Exception
        if part == 'part1':
            if p in visited:
                return acc
        if part == 'part2':
            if p in visited:
                return None
            if p == len(ops):
                return acc
        visited[p] = True


def part1(lines):
    """
    >>> part1(load_example(__file__, '8'))
    5
    """
    ops = prepare_ops(lines)
    return run_program(ops, 'part1')


def modify_op(ops, i):
    op, arg = ops[i]
    if op == 'jmp':
        ops[i] = ('nop', arg)
        return ops
    elif op == 'nop':
        ops[i] = ('jmp', arg)
        return ops
    else:
        return None


def part2(lines):
    """
    >>> part2(load_example(__file__, '8'))
    8
    """
    ops = prepare_ops(lines)
    for i in range(len(ops)):
        mod_ops = modify_op(ops[:], i)
        if mod_ops:
            acc = run_program(mod_ops, 'part2')
            if acc:
                return acc


if __name__ == "__main__":
    data = load_input(__file__, 2020, '8')
    print(part1(data))
    print(part2(data))
