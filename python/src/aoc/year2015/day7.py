from aoc.util import load_example, load_input

M = 2 ** 16


def prepare_rules(lines):
    rules = {}
    for line in lines:
        l, r = line.strip().split(" -> ")
        rules[r] = l.split()
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
        if op == "NOT":
            rules[wire] = M - 1 - val
        else:
            raise Exception
    elif len(lh) == 3:
        ref1, op, ref2 = lh
        val1 = deduct(rules, ref1)
        val2 = deduct(rules, ref2)
        if op == "AND":
            rules[wire] = val1 & val2
        elif op == "OR":
            rules[wire] = val1 | val2
        elif op == "LSHIFT":
            rules[wire] = val1 << val2
        elif op == "RSHIFT":
            rules[wire] = val1 >> val2
        else:
            raise Exception
    else:
        raise Exception
    return rules[wire]


def run(lines, wire, new_rule_b=None):
    """
    >>> data = load_example(__file__, '7')
    >>> run(data, 'd')
    72
    >>> run(data, 'e')
    507
    >>> run(data, 'f')
    492
    >>> run(data, 'g')
    114
    >>> run(data, 'h')
    65412
    >>> run(data, 'i')
    65079
    >>> run(data, 'x')
    123
    >>> run(data, 'y')
    456
    """
    rules = prepare_rules(lines)
    if new_rule_b:
        rules["b"] = new_rule_b
    return deduct(rules, wire)


def part1(lines):
    return run(lines, "a")


def part2(lines):
    answer1 = part1(lines)
    return run(lines, "a", answer1)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "7")
    print(part1(data))
    print(part2(data))
