from collections import defaultdict

from aoc.util import load_input, load_example


class Monkey:
    def __init__(self):
        self.value = None
        self.rules = []

    def set_value(self, value):
        self.value = value

    def add_rule(self, var1, op, var2):
        self.rules.append((var1, op, var2))


class Monkeys:
    def __init__(self, lines, is_part2=False):
        self.monkeys = defaultdict(lambda: Monkey())
        for line in lines:
            token = line.split()
            a = token[0].strip(":")
            if len(token) == 2:
                self.monkeys[a].set_value(int(token[1]))
            else:
                b, op, c = token[1:]
                if is_part2 and a == "root":
                    # root = b == c
                    # t = b - c
                    # -> b = t + c
                    # -> c = b - t
                    t = "####"
                    self.monkeys[t].set_value(0)
                    self.monkeys[t].add_rule(b, "-", c)
                    self.monkeys[b].add_rule(t, "+", c)
                    self.monkeys[c].add_rule(b, "-", t)
                elif op == "+":
                    # a = b + c
                    # -> b = a - c
                    # -> c = a - b
                    self.monkeys[a].add_rule(b, "+", c)
                    self.monkeys[b].add_rule(a, "-", c)
                    self.monkeys[c].add_rule(a, "-", b)
                elif op == "-":
                    # a = b - c
                    # -> b = a + c
                    # -> c = b - a
                    self.monkeys[a].add_rule(b, "-", c)
                    self.monkeys[b].add_rule(a, "+", c)
                    self.monkeys[c].add_rule(b, "-", a)
                elif op == "*":
                    # a = b * c
                    # -> b = a / c
                    # -> c = a / b
                    self.monkeys[a].add_rule(b, "*", c)
                    self.monkeys[b].add_rule(a, "/", c)
                    self.monkeys[c].add_rule(a, "/", b)
                elif op == "/":
                    # a = b / c
                    # -> b = a * c
                    # -> c = b / a
                    self.monkeys[a].add_rule(b, "/", c)
                    self.monkeys[b].add_rule(a, "*", c)
                    self.monkeys[c].add_rule(b, "/", a)
                else:
                    raise
        if is_part2:
            self.monkeys["humn"].value = None

    def count_open(self):
        return sum(1 for rule in self.monkeys.values() if rule.value is None)

    def deduce(self, name):
        while self.count_open() > 0:
            for monkey in self.monkeys.values():
                if monkey.value is not None:
                    continue
                for var1, op, var2 in monkey.rules:
                    value1 = self.monkeys[var1].value
                    value2 = self.monkeys[var2].value
                    if value1 is None or value2 is None:
                        continue
                    if op == "+":
                        monkey.value = value1 + value2
                    elif op == "-":
                        monkey.value = value1 - value2
                    elif op == "*":
                        monkey.value = value1 * value2
                    elif op == "/":
                        monkey.value = value1 // value2
                    else:
                        raise
        return self.monkeys[name].value


def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    152
    """
    monkeys = Monkeys(lines)
    return monkeys.deduce("root")


def part2(lines):
    """
    >>> part2(load_example(__file__, "21"))
    301
    """
    monkeys = Monkeys(lines, is_part2=True)
    return monkeys.deduce("humn")


if __name__ == "__main__":
    data = load_input(__file__, 2022, "21")
    print(part1(data))
    print(part2(data))
