from collections import defaultdict

from aoc.util import load_input, load_example
import re

input_pattern = re.compile(r"value (\d+) goes to bot (\d+)")
bot_bot_pattern = re.compile(r"bot (\d+) gives low to bot (\d+) and high to bot (\d+)")
output_bot_pattern = re.compile(r"bot (\d+) gives low to output (\d+) and high to bot (\d+)")
output_output_pattern = re.compile(r"bot (\d+) gives low to output (\d+) and high to output (\d+)")


class Bot:
    def __init__(self):
        self.values = []
        self.put_lower = None
        self.put_higher = None
        self.output_lower = None
        self.output_higher = None

    def add_value(self, value):
        self.values.append(value)

    def gives(self, bots, outputs, is_part1, mi_target, ma_target):
        mi = min(self.values)
        ma = max(self.values)
        if is_part1 and mi == mi_target and ma == ma_target:
            return True
        if self.put_lower is not None:
            bots[self.put_lower].add_value(mi)
        if self.put_higher is not None:
            bots[self.put_higher].add_value(ma)
        if self.output_lower is not None:
            outputs[self.output_lower].append(mi)
        if self.output_higher is not None:
            outputs[self.output_higher].append(ma)
        self.values.clear()


def load_bots(lines):
    bots = defaultdict(Bot)
    for rule in lines:
        m = input_pattern.match(rule)
        if m:
            value1, bot1 = map(int, m.groups())
            bots[bot1].add_value(value1)
        m = bot_bot_pattern.match(rule)
        if m:
            bot2, low_bot2, high_bot2 = map(int, m.groups())
            bots[bot2].put_lower = low_bot2
            bots[bot2].put_higher = high_bot2
        m = output_output_pattern.match(rule)
        if m:
            bot3, low_output3, high_output3 = map(int, m.groups())
            bots[bot3].output_lower = low_output3
            bots[bot3].output_higher = high_output3
        m = output_bot_pattern.match(rule)
        if m:
            bot4, low_output4, high_bot4 = map(int, m.groups())
            bots[bot4].output_lower = low_output4
            bots[bot4].put_higher = high_bot4
    return bots


def simulate(bots, outputs, is_part1=False, mi_target=None, ma_target=None):
    changes = True
    while changes:
        changes = False
        for i, b in bots.items():
            if len(b.values) == 2:
                if b.gives(bots, outputs, is_part1, mi_target, ma_target):
                    return i
                changes = True
    return outputs[0][0] * outputs[1][0] * outputs[2][0]


def part1(lines, mi_target=17, ma_target=61):
    """
    >>> part1(load_example(__file__, "10"), 2, 5)
    2
    """
    bots = load_bots(lines)
    outputs = defaultdict(list)
    return simulate(bots, outputs, is_part1=True, mi_target=mi_target, ma_target=ma_target)


def part2(lines):
    """
    >>> part2(load_example(__file__, "10"))
    30
    """
    bots = load_bots(lines)
    outputs = defaultdict(list)
    simulate(bots, outputs)
    return outputs[0][0] * outputs[1][0] * outputs[2][0]


if __name__ == "__main__":
    data = load_input(__file__, 2016, "10")
    print(part1(data))
    print(part2(data))
