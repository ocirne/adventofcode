from aoc.util import load_input, load_example


def foo(lookup, node):
    value = lookup[node]
    if value[0] == "num":
        return value[1]
    else:
        var1, op, var2 = value[1]
        value1 = foo(lookup, var1)
        value2 = foo(lookup, var2)
        if op == "+":
            return value1 + value2
        elif op == "-":
            return value1 - value2
        elif op == "*":
            return value1 * value2
        elif op == "/":
            return value1 // value2
        else:
            raise


def read_ops(lines):
    lookup = {}
    for line in lines:
        token = line.split()
        key = token[0].strip(":")
        if len(token) == 2:
            lookup[key] = ("num", int(token[1]))
        else:
            lookup[key] = ("op", (token[1], token[2], token[3]))
    return lookup


def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    152
    """
    lookup = read_ops(lines)
    return foo(lookup, "root")


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    301
    """
    lookup = read_ops(lines)
    old_root = lookup["root"][1]
    lookup["root"] = ("op", (old_root[0], "=", old_root[2]))
    del lookup["humn"]
    print(lookup)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "21")
    print(part1(data))
    print(part2(data))
