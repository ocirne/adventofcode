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


def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    152
    """
    lookup = {}
    for line in lines:
        token = line.split()
        key = token[0].strip(":")
        print(token)
        if len(token) == 2:
            lookup[key] = ("num", int(token[1]))
        else:
            lookup[key] = ("op", (token[1], token[2], token[3]))
    print(lookup)
    return foo(lookup, "root")


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    .
    """


if __name__ == "__main__":
    data = load_input(__file__, 2022, "21")
    print(part1(data))
    print(part2(data))
