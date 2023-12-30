from functools import reduce
from math import lcm

from aoc.util import load_input, load_example


class Module:
    def __init__(self, destinations):
        self.destinations = destinations.split(", ")
        self.state = 0
        self.count = 0

    def reset(self):
        self.state = 0
        self.count = 0


class FlipFlop(Module):
    def __init__(self, destinations):
        super().__init__(destinations)

    def pulse(self, _, value):
        self.count += 1
        if value == 0:
            self.state ^= 1
            for d in self.destinations:
                yield d, self.state


class Conjunction(Module):
    def __init__(self, destinations):
        super().__init__(destinations)
        self.most_recent = {}

    def pulse(self, src, value):
        self.count += 1
        assert src in self.most_recent
        self.most_recent[src] = value
        if all(v == 1 for v in self.most_recent.values()):
            self.state = 0
        else:
            self.state = 1
        for d in self.destinations:
            yield d, self.state

    def reset(self):
        super().reset()
        for src in self.most_recent:
            self.most_recent[src] = 0


class Broadcaster(Module):
    def __init__(self, destinations):
        super().__init__(destinations)

    def pulse(self, _, value):
        self.count += 1
        for d in self.destinations:
            yield d, value


class Output(Module):
    def __init__(self):
        super().__init__("")

    def pulse(self, _, value):
        self.count += 1
        self.state = value
        return []


class Modules:
    def __init__(self, lines):
        self.modules = {"output": Output(), "rx": Output()}
        for line in lines:
            src, dest = line.split(" -> ")
            if src == "broadcaster":
                self.modules["broadcaster"] = Broadcaster(dest)
            elif src.startswith("%"):
                self.modules[src[1:]] = FlipFlop(dest)
            elif src.startswith("&"):
                self.modules[src[1:]] = Conjunction(dest)
            else:
                raise

        for source, module in self.modules.items():
            for destination in module.destinations:
                if not destination:
                    continue
                if destination not in self.modules:
                    continue
                if not isinstance(self.modules[destination], Conjunction):
                    continue
                self.modules[destination].most_recent[source] = 0

    def reset(self):
        for _, module in self.modules.items():
            module.reset()

    def spam_button(self, t=None, count=1_001):
        self.reset()
        total_pulses = {0: 0, 1: 0}
        for i in range(1, count):
            pulses = [("button", "broadcaster", 0)]
            self.modules["broadcaster"].pulse(None, 0)
            total_pulses[0] += 1
            while pulses:
                src, dest, value = pulses.pop(0)
                for d, v in self.modules[dest].pulse(src, value):
                    total_pulses[v] += 1
                    pulses.append((dest, d, v))
                if t is not None and self.modules[t].state == 1:
                    return i
        return total_pulses


def part1(lines):
    """
    >>> part1(load_example(__file__, "20a"))
    32000000
    >>> part1(load_example(__file__, "20b"))
    11687500
    """
    modules = Modules(lines)
    total_pulses = modules.spam_button()
    return total_pulses[0] * total_pulses[1]


def part2(lines):
    modules = Modules(lines)
    return reduce(lcm, (modules.spam_button(t, 2**12) for t in ("sg", "dh", "lm", "db")))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "20")
    print(part1(data))
    print(part2(data))
