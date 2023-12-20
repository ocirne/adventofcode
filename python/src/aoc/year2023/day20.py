from aoc.util import load_input, load_example


class Module:
    def __init__(self, destinations):
        self.destinations = destinations.split(", ")


class FlipFlop(Module):
    def __init__(self, destinations):
        super().__init__(destinations)
        self.state = 0

    def pulse(self, _, value):
        if value == 0:
            self.state ^= 1
            for d in self.destinations:
                yield d, self.state


class Conjunction(Module):
    def __init__(self, destinations):
        super().__init__(destinations)
        self.state = 0
        self.most_recent = {}

    def pulse(self, src, value):
        assert src in self.most_recent
        self.most_recent[src] = value
        if all(v == 1 for v in self.most_recent.values()):
            for d in self.destinations:
                yield d, 0
        else:
            for d in self.destinations:
                yield d, 1


class Broadcaster(Module):
    def __init__(self, destinations):
        super().__init__(destinations)

    def pulse(self, _, value):
        for d in self.destinations:
            yield d, value


class Output(Module):
    def __init__(self):
        super().__init__("")

    def pulse(self, _, value):
        print("Output", value)
        return []


def part1(lines):
    """
    >>> part1(load_example(__file__, "20a"))
    32000000
    >>> part1(load_example(__file__, "20b"))
    11687500
    """
    modules = {"output": Output()}
    for line in lines:
        src, dest = line.split(" -> ")
        if src == "broadcaster":
            modules["broadcaster"] = Broadcaster(dest)
        elif src.startswith("%"):
            modules[src[1:]] = FlipFlop(dest)
        elif src.startswith("&"):
            modules[src[1:]] = Conjunction(dest)
        else:
            raise

    for source, module in modules.items():
        for destination in module.destinations:
            if not destination:
                continue
            if destination not in modules:
                continue
            if not isinstance(modules[destination], Conjunction):
                continue
            modules[destination].most_recent[source] = 0

    total_pulses = {0: 0, 1: 0}
    for _ in range(1000):
        pulses = [("button", "broadcaster", 0)]
        modules["broadcaster"].pulse(None, 0)
        total_pulses[0] += 1
        while pulses:
            src, dest, value = pulses.pop(0)
            print(src, "-", value, "->", dest)
            if dest in modules:
                for d, v in modules[dest].pulse(src, value):
                    total_pulses[v] += 1
                    pulses.append((dest, d, v))
    #    print(total_pulses)
    return total_pulses[0] * total_pulses[1]


def part2(lines):
    """
    >>> part2(load_example(__file__, "20a"))
    """


if __name__ == "__main__":
    # print(part1(load_example(__file__, "20b")))
    data = load_input(__file__, 2023, "20")
    print(part1(data))
    # print(part2(data))
