import math

from aoc.util import load_input, load_example


class Monkey:
    def __init__(self, lines):
        self.items = [int(s) for s in lines[1].split(":")[1].split(",")]
        self.operation = self.read_operation(lines[2])
        self.test_divisor = int(lines[3].split()[-1])
        self.when_true = int(lines[4].split()[-1])
        self.when_false = int(lines[5].split()[-1])
        self.inspected_count = 0

    @staticmethod
    def read_operation(line):
        op, op_value = line.split()[-2:]
        if op == "*":
            if op_value == "old":
                return lambda old: old * old
            else:  # isnumeric()
                return lambda old: old * int(op_value)
        else:  # op == '+' and n.isnumeric()
            return lambda old: old + int(op_value)


class MonkeySimulator:
    def __init__(self, lines, divide_by_three):
        self.monkeys = [Monkey(lines[s : s + 6]) for s in range(0, len(lines), 7)]
        self.modulo = math.prod(m.test_divisor for m in self.monkeys)
        self.divide_by_three = divide_by_three

    def _one_round(self):
        for monkey_index, monkey in enumerate(self.monkeys):
            while monkey.items:
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                if self.divide_by_three:
                    item //= 3
                next_monkey = monkey.when_true if item % monkey.test_divisor == 0 else monkey.when_false
                self.monkeys[next_monkey].items.append(item % self.modulo)
                monkey.inspected_count += 1

    def play_rounds(self, n):
        for round_index in range(n):
            self._one_round()
        c = sorted((m.inspected_count for m in self.monkeys), reverse=True)
        return c[0] * c[1]


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    10605
    """
    return MonkeySimulator(lines, divide_by_three=True).play_rounds(20)


def part2(lines):
    """
    >>> part2(load_example(__file__, "11"))
    2713310158
    """
    return MonkeySimulator(lines, divide_by_three=False).play_rounds(10_000)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "11")
    print(part1(data))
    print(part2(data))
