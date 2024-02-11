from aoc.util import load_input, load_example


class Monkey:
    def __init__(self, lines):
        self.items = [int(s) for s in lines[1].split(":")[1].split(",")]
        self.op, self.op_value = lines[2].split()[-2:]
        self.test_divisor = int(lines[3].split()[-1])
        self.test_is_true = int(lines[4].split()[-1])
        self.test_is_false = int(lines[5].split()[-1])
        self.inspected_count = 0


class Monkeys:
    def __init__(self, lines):
        self.monkeys = [Monkey(lines[s : s + 6]) for s in range(0, len(lines), 7)]


def round(monkeys: Monkeys, test_print=lambda m: None):
    """
    >>> monkeys = Monkeys(load_example(__file__, "11"))
    >>> round(monkeys, test_print=lambda m: print(m))
    Monkey 0:
      Monkey inspects an item with a worry level of 79.
        Worry level is multiplied by 19 to 1501.
        Monkey gets bored with item. Worry level is divided by 3 to 500.
        Current worry level is not divisible by 23.
        Item with worry level 500 is thrown to monkey 3.
      Monkey inspects an item with a worry level of 98.
        Worry level is multiplied by 19 to 1862.
        Monkey gets bored with item. Worry level is divided by 3 to 620.
        Current worry level is not divisible by 23.
        Item with worry level 620 is thrown to monkey 3.
    Monkey 1:
      Monkey inspects an item with a worry level of 54.
        Worry level increases by 6 to 60.
        Monkey gets bored with item. Worry level is divided by 3 to 20.
        Current worry level is not divisible by 19.
        Item with worry level 20 is thrown to monkey 0.
      Monkey inspects an item with a worry level of 65.
        Worry level increases by 6 to 71.
        Monkey gets bored with item. Worry level is divided by 3 to 23.
        Current worry level is not divisible by 19.
        Item with worry level 23 is thrown to monkey 0.
      Monkey inspects an item with a worry level of 75.
        Worry level increases by 6 to 81.
        Monkey gets bored with item. Worry level is divided by 3 to 27.
        Current worry level is not divisible by 19.
        Item with worry level 27 is thrown to monkey 0.
      Monkey inspects an item with a worry level of 74.
        Worry level increases by 6 to 80.
        Monkey gets bored with item. Worry level is divided by 3 to 26.
        Current worry level is not divisible by 19.
        Item with worry level 26 is thrown to monkey 0.
    Monkey 2:
      Monkey inspects an item with a worry level of 79.
        Worry level is multiplied by itself to 6241.
        Monkey gets bored with item. Worry level is divided by 3 to 2080.
        Current worry level is divisible by 13.
        Item with worry level 2080 is thrown to monkey 1.
      Monkey inspects an item with a worry level of 60.
        Worry level is multiplied by itself to 3600.
        Monkey gets bored with item. Worry level is divided by 3 to 1200.
        Current worry level is not divisible by 13.
        Item with worry level 1200 is thrown to monkey 3.
      Monkey inspects an item with a worry level of 97.
        Worry level is multiplied by itself to 9409.
        Monkey gets bored with item. Worry level is divided by 3 to 3136.
        Current worry level is not divisible by 13.
        Item with worry level 3136 is thrown to monkey 3.
    Monkey 3:
      Monkey inspects an item with a worry level of 74.
        Worry level increases by 3 to 77.
        Monkey gets bored with item. Worry level is divided by 3 to 25.
        Current worry level is not divisible by 17.
        Item with worry level 25 is thrown to monkey 1.
      Monkey inspects an item with a worry level of 500.
        Worry level increases by 3 to 503.
        Monkey gets bored with item. Worry level is divided by 3 to 167.
        Current worry level is not divisible by 17.
        Item with worry level 167 is thrown to monkey 1.
      Monkey inspects an item with a worry level of 620.
        Worry level increases by 3 to 623.
        Monkey gets bored with item. Worry level is divided by 3 to 207.
        Current worry level is not divisible by 17.
        Item with worry level 207 is thrown to monkey 1.
      Monkey inspects an item with a worry level of 1200.
        Worry level increases by 3 to 1203.
        Monkey gets bored with item. Worry level is divided by 3 to 401.
        Current worry level is not divisible by 17.
        Item with worry level 401 is thrown to monkey 1.
      Monkey inspects an item with a worry level of 3136.
        Worry level increases by 3 to 3139.
        Monkey gets bored with item. Worry level is divided by 3 to 1046.
        Current worry level is not divisible by 17.
        Item with worry level 1046 is thrown to monkey 1.
    """
    for index, monkey in enumerate(monkeys.monkeys):
        test_print("Monkey %d:" % index)
        while monkey.items:
            item = monkey.items.pop(0)
            test_print("  Monkey inspects an item with a worry level of %d." % item)
            if monkey.op == "*":
                if monkey.op_value == "old":
                    item *= item
                    test_print("    Worry level is multiplied by itself to %d." % item)
                else:  # isnumeric()
                    item *= int(monkey.op_value)
                    test_print("    Worry level is multiplied by %s to %d." % (monkey.op_value, item))
            else:  # op == '+' and n.isnumeric()
                item += int(monkey.op_value)
                test_print("    Worry level increases by %s to %d." % (monkey.op_value, item))
            item //= 3
            test_print("    Monkey gets bored with item. Worry level is divided by 3 to %d." % item)
            if item % monkey.test_divisor == 0:
                test_print("    Current worry level is divisible by %d." % monkey.test_divisor)
                next_monkey = monkey.test_is_true
            else:
                test_print("    Current worry level is not divisible by %d." % monkey.test_divisor)
                next_monkey = monkey.test_is_false
            test_print("    Item with worry level %d is thrown to monkey %d." % (item, next_monkey))
            monkeys.monkeys[next_monkey].items.append(item)
            monkey.inspected_count += 1


def bar(monkeys, test_print=lambda m: None):
    """
    >>> monkeys = Monkeys(load_example(__file__, "11"))
    >>> bar(monkeys, test_print=lambda m: print(m))
    After round 1, the monkeys are holding items with these worry levels:
    Monkey 0: 20, 23, 27, 26
    Monkey 1: 2080, 25, 167, 207, 401, 1046
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 2, the monkeys are holding items with these worry levels:
    Monkey 0: 695, 10, 71, 135, 350
    Monkey 1: 43, 49, 58, 55, 362
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 3, the monkeys are holding items with these worry levels:
    Monkey 0: 16, 18, 21, 20, 122
    Monkey 1: 1468, 22, 150, 286, 739
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 4, the monkeys are holding items with these worry levels:
    Monkey 0: 491, 9, 52, 97, 248, 34
    Monkey 1: 39, 45, 43, 258
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 5, the monkeys are holding items with these worry levels:
    Monkey 0: 15, 17, 16, 88, 1037
    Monkey 1: 20, 110, 205, 524, 72
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 6, the monkeys are holding items with these worry levels:
    Monkey 0: 8, 70, 176, 26, 34
    Monkey 1: 481, 32, 36, 186, 2190
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 7, the monkeys are holding items with these worry levels:
    Monkey 0: 162, 12, 14, 64, 732, 17
    Monkey 1: 148, 372, 55, 72
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 8, the monkeys are holding items with these worry levels:
    Monkey 0: 51, 126, 20, 26, 136
    Monkey 1: 343, 26, 30, 1546, 36
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 9, the monkeys are holding items with these worry levels:
    Monkey 0: 116, 10, 12, 517, 14
    Monkey 1: 108, 267, 43, 55, 288
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 10, the monkeys are holding items with these worry levels:
    Monkey 0: 91, 16, 20, 98
    Monkey 1: 481, 245, 22, 26, 1092, 30
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 15, the monkeys are holding items with these worry levels:
    Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
    Monkey 1: 110, 36
    Monkey 2:
    Monkey 3:
    <BLANKLINE>
    After round 20, the monkeys are holding items with these worry levels:
    Monkey 0: 10, 12, 14, 26, 34
    Monkey 1: 245, 93, 53, 199, 115
    Monkey 2:
    Monkey 3:
    """
    for round_index in range(1, 21):
        round(monkeys)
        if round_index < 11 or round_index in (15, 20):
            test_print("After round %d, the monkeys are holding items with these worry levels:" % round_index)
            for monkey_index, monkey in enumerate(monkeys.monkeys):
                if monkey.items:
                    test_print("Monkey %d: %s" % (monkey_index, ", ".join(str(s) for s in monkey.items)))
                else:
                    test_print("Monkey %d:" % monkey_index)
            if round_index < 20:
                test_print("")


def baz(monkeys, test_print=lambda m: None):
    """
    >>> monkeys = Monkeys(load_example(__file__, "11"))
    >>> baz(monkeys, test_print=lambda m: print(m))
    Monkey 0 inspected items 101 times.
    Monkey 1 inspected items 95 times.
    Monkey 2 inspected items 7 times.
    Monkey 3 inspected items 105 times.
    10605
    """
    bar(monkeys)
    for monkey_index, monkey in enumerate(monkeys.monkeys):
        test_print("Monkey %d inspected items %d times." % (monkey_index, monkey.inspected_count))
    c = sorted((m.inspected_count for m in monkeys.monkeys), reverse=True)
    return c[0] * c[1]


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    10605
    """
    monkeys = Monkeys(lines)
    return baz(monkeys)


def part2(lines):
    """
    >>> part2(load_example(__file__, "11"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2022, "11")
    #    data = load_example(__file__, "11")
    print(part1(data))
#    print(part2(data))
