from collections import defaultdict

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


class Rule:
    def __init__(self, var1=None, op=None, var2=None):
        self.var1 = var1
        self.op = op
        self.var2 = var2


class Monkey:
    def __init__(self):
        self.value = None
        self.rules = []

    def set_value(self, value):
        self.value = value

    def add_rule(self, rule):
        self.rules.append(rule)


class Monkeys:
    def __init__(self, lines):
        self.monkeys = defaultdict(lambda: Monkey())
        for line in lines:
            token = line.split()
            a = token[0].strip(":")
            if len(token) == 2:
                self.monkeys[a].set_value(int(token[1]))
            else:
                b, op, c = token[1:]
                if a == "root":
                    # root = b == c
                    # t = b - c
                    # -> b = t + c
                    # -> c = b - t
                    t = "####"
                    self.monkeys[t].set_value(0)
                    self.monkeys[t].add_rule(Rule(var1=b, op="-", var2=c))
                    self.monkeys[b].add_rule(Rule(var1=t, op="+", var2=c))
                    self.monkeys[c].add_rule(Rule(var1=b, op="-", var2=t))
                elif op == "+":
                    # a = b + c
                    # -> b = a - c
                    # -> c = a - b
                    self.monkeys[a].add_rule(Rule(var1=b, op="+", var2=c))
                    self.monkeys[b].add_rule(Rule(var1=a, op="-", var2=c))
                    self.monkeys[c].add_rule(Rule(var1=a, op="-", var2=b))
                elif op == "-":
                    # a = b - c
                    # -> b = a + c
                    # -> c = b - a
                    self.monkeys[a].add_rule(Rule(var1=b, op="-", var2=c))
                    self.monkeys[b].add_rule(Rule(var1=a, op="+", var2=c))
                    self.monkeys[c].add_rule(Rule(var1=b, op="-", var2=a))
                elif op == "*":
                    # a = b * c
                    # -> b = a / c
                    # -> c = a / b
                    self.monkeys[a].add_rule(Rule(var1=b, op="*", var2=c))
                    self.monkeys[b].add_rule(Rule(var1=a, op="/", var2=c))
                    self.monkeys[c].add_rule(Rule(var1=a, op="/", var2=b))
                elif op == "/":
                    # a = b / c
                    # -> b = a * c
                    # -> c = b / a
                    self.monkeys[a].add_rule(Rule(var1=b, op="/", var2=c))
                    self.monkeys[b].add_rule(Rule(var1=a, op="*", var2=c))
                    self.monkeys[c].add_rule(Rule(var1=b, op="/", var2=a))
                else:
                    raise
        self.monkeys["humn"].value = None

    def count_open(self):
        return sum(1 for rule in self.monkeys.values() if rule.value is None)

    def deduce(self, name):
        while True:
            count = self.count_open()
            print(count)
            if count == 0:
                break
            for monkey in self.monkeys.values():
                if monkey.value is not None:
                    continue
                for rule in monkey.rules:
                    value1 = self.monkeys[rule.var1].value
                    value2 = self.monkeys[rule.var2].value
                    if value1 is None or value2 is None:
                        continue
                    if rule.op == "+":
                        monkey.value = value1 + value2
                    elif rule.op == "-":
                        monkey.value = value1 - value2
                    elif rule.op == "*":
                        monkey.value = value1 * value2
                    elif rule.op == "/":
                        monkey.value = value1 // value2
                    else:
                        raise
        return self.monkeys[name].value


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    301
    """
    monkeys = Monkeys(lines)
    return monkeys.deduce("humn")


if __name__ == "__main__":
    data = load_input(__file__, 2022, "21")
    print(part1(data))
    print(part2(data))
