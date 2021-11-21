import copy
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

    def puts(self, bots, outputs, is_part1=False):
        #        print(self.put_lower, self.put_higher, self.output_lower, self.output_higher)
        if self.put_lower and self.output_lower:
            raise Exception("lower put and output")
        if self.put_higher and self.output_higher:
            raise Exception("higher put and output")
        if self.put_lower is None and self.output_lower is None:
            raise Exception("lower put and output")
        if self.put_higher is None and self.output_higher is None:
            raise Exception("higher put and output")
        #       print("index %s self.values %s" % (self.index, self.values))
        mi = min(self.values)
        ma = max(self.values)
        if is_part1 and mi == 17 and ma == 61:
            return True
        if self.put_lower is not None:
            print("put value %s to bot %s" % (mi, self.put_lower))
            bots[self.put_lower].add_value(mi)
        if self.put_higher is not None:
            print("put value %s to bot %s" % (ma, self.put_higher))
            bots[self.put_higher].add_value(ma)
        if self.output_lower is not None:
            print("put value %s to output %s" % (mi, self.output_lower))
            outputs[self.output_lower].append(mi)
        if self.output_higher is not None:
            print("put value %s to output %s" % (ma, self.output_higher))
            outputs[self.output_higher].append(ma)
        self.values.clear()


#        return False


def part1(rules):
    bots = {}
    outputs = defaultdict(list)
    #    print('digraph x {')
    for rule in rules:
        m1 = input_pattern.match(rule)
        if m1:
            value1, bot1 = map(int, m1.groups())
            if bot1 not in bots:
                bots[bot1] = Bot()
            bots[bot1].add_value(value1)
        #            print("i%s -> %s" % (value1, bot1))
        m2 = bot_bot_pattern.match(rule)
        if m2:
            bot2, low_bot2, high_bot2 = map(int, m2.groups())
            if bot2 not in bots:
                bots[bot2] = Bot()
            bots[bot2].put_lower = low_bot2
            bots[bot2].put_higher = high_bot2
        #            print("%s -> %s" % (bot2, low_bot2))
        #            print("%s -> %s [style=dashed]" % (bot2, high_bot2))
        m3 = output_output_pattern.match(rule)
        if m3:
            bot3, low_output3, high_output3 = map(int, m3.groups())
            if bot3 not in bots:
                bots[bot3] = Bot()
            bots[bot3].output_lower = low_output3
            bots[bot3].output_higher = high_output3
        #            print("%s -> { o%s o%s }" % (bot3, low_output3, high_output3))
        m4 = output_bot_pattern.match(rule)
        if m4:
            bot4, low_output4, high_bot4 = map(int, m4.groups())
            if bot4 not in bots:
                bots[bot4] = Bot()
            bots[bot4].output_lower = low_output4
            bots[bot4].put_higher = high_bot4
    #            print("%s -> { o%s %s }" % (bot4, low_output4, high_bot4))
    #    print('}')

    changes = True
    while changes:
        changes = False
        print("run")
        for i, b in bots.items():
            #            if len(b.values) > 0:
            #                print('Bot: %s has %s' % (i, b.values))
            if len(b.values) == 2:
                print("Bot: %s" % i)
                if b.puts(bots, outputs, is_part1=True):
                    print("done")
                    return i
                changes = True
    print("outputs", sorted(outputs.items()))


#    print('sollte 2 herauskommen')


def part2(rules):
    bots = defaultdict(Bot)
    outputs = defaultdict(list)
    for rule in rules:
        m1 = input_pattern.match(rule)
        if m1:
            value1, bot1 = map(int, m1.groups())
            bots[bot1].add_value(value1)
        m2 = bot_bot_pattern.match(rule)
        if m2:
            bot2, low_bot2, high_bot2 = map(int, m2.groups())
            bots[bot2].put_lower = low_bot2
            bots[bot2].put_higher = high_bot2
        m3 = output_output_pattern.match(rule)
        if m3:
            bot3, low_output3, high_output3 = map(int, m3.groups())
            bots[bot3].output_lower = low_output3
            bots[bot3].output_higher = high_output3
        m4 = output_bot_pattern.match(rule)
        if m4:
            bot4, low_output4, high_bot4 = map(int, m4.groups())
            bots[bot4].output_lower = low_output4
            bots[bot4].put_higher = high_bot4

    changes = True
    while changes:
        changes = False
        print("run")
        for i, b in bots.items():
            if len(b.values) > 0:
                print("Bot: %s has %s" % (i, b.values))
            if len(b.values) == 2:
                print("Action for Bot: %s" % i)
                b.puts(bots, outputs)
                changes = True
    print("outputs", sorted(outputs.items()))


if __name__ == "__main__":
    data = load_input(__file__, 2016, "10")
    #    data = load_example(__file__, '10')
    #    print(part1(data))
    print(part2(data))
