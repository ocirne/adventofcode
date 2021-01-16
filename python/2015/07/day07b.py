
import day07a

M = 2**16


def read_rules(filename):
    f = open(filename, 'r')
    rules = {}
    for line in f.readlines():
        l, r = line.strip().split(' -> ')
        rules[r] = l.split()
    rules['b'] = day07a.run(filename, 'a')
    return rules


def deduct(rules, wire):
    if wire.isnumeric():
        return int(wire)
    lh = rules[wire]
    if not isinstance(lh, list):
        if isinstance(lh, int):
            return lh
        elif lh.isnumeric():
            rules[wire] = int(lh)
        else:
            rules[wire] = deduct(rules, lh)
    elif len(lh) == 1:
        return deduct(rules, lh[0])
    elif len(lh) == 2:
        op, ref = lh
        val = deduct(rules, ref)
        if op == 'NOT':
            rules[wire] = M - 1 - val
        else:
            raise Exception
    elif len(lh) == 3:
        ref1, op, ref2 = lh
        val1 = deduct(rules, ref1)
        val2 = deduct(rules, ref2)
        if op == 'AND':
            rules[wire] = val1 & val2
        elif op == 'OR':
            rules[wire] = val1 | val2
        elif op == 'LSHIFT':
            rules[wire] = val1 << val2
        elif op == 'RSHIFT':
            rules[wire] = val1 >> val2
        else:
            raise Exception
    else:
        raise Exception
    return rules[wire]


def run(filename, wire):
    rules = read_rules(filename)
    return deduct(rules, wire)


print(run('input', 'a'))
