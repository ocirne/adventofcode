
def read_ops(filename):
    ops = []
    for line in open(filename, 'r').readlines():
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


def part1(filename):
    """
    >>> part1('reference')
    5
    """
    ops = read_ops(filename)
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


def part2(filename):
    """
    >>> part2('reference')
    8
    """
    ops = read_ops(filename)
    for i in range(len(ops)):
        mod_ops = modify_op(ops[:], i)
        if mod_ops:
            acc = run_program(mod_ops, 'part2')
            if acc:
                return acc


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
