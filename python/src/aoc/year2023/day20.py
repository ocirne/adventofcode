from aoc.util import load_input, load_example


class Module:
    def __init__(self, destinations):
        self.destinations = destinations.split(", ")
        self.state = None
        self.count = 0


class FlipFlop(Module):
    def __init__(self, destinations):
        super().__init__(destinations)
        self.state = 0

    def pulse(self, _, value):
        self.count += 1
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
        self.count += 1
        assert src in self.most_recent
        self.most_recent[src] = value
        if all(v == 1 for v in self.most_recent.values()):
            self.state = 0
        else:
            self.state = 1
        for d in self.destinations:
            yield d, self.state


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
        self.state = 0

    def pulse(self, src, value):
        self.count += 1
        #   print(src, " -> rx", value)
        self.state = value
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
            #      print(src, "-", value, "->", dest)
            if dest in modules:
                for d, v in modules[dest].pulse(src, value):
                    total_pulses[v] += 1
                    pulses.append((dest, d, v))
    print(total_pulses)
    return total_pulses[0] * total_pulses[1]


def part2(lines):
    #    print('digraph D {')

    #    for line in lines:
    #        src, dest = line.split(" -> ")
    #        if src == "broadcaster":
    #            print(line)
    #        else:
    #            print(line[1:])
    #    print('}')
    #    return

    modules = {"output": Output(), "rx": Output()}
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

    # source, target = 'xr', 'sg'
    # source, target = 'mn', 'dh'
    # source, target = 'pl', 'lm'
    # source, target = 'xc', 'db'
    for i in range(40):
        pulses = [("button", "broadcaster", 0)]
        modules["broadcaster"].pulse(None, 0)
        while pulses:
            src, dest, value = pulses.pop(0)
            #            print(src, "-", value, "->", dest)
            for d, v in modules[dest].pulse(src, value):
                pulses.append((dest, d, v))
        if modules["sg"].state == 1:
            return i, modules["sg"].count
        for t in ("sg", "dh", "lm", "db"):  # , 'rx'):
            # if modules[t].state == 1:
            print("%s: state: %s, %s times" % (t, modules[t].state, modules[t].count), end=" | ")
            modules[t].count = 0
        print()


#        print(" ".join("%s:%s" % (key, module.state) for key, module in modules.items()))
#    return target, total_pulses


if __name__ == "__main__":
    # print(part1(load_example(__file__, "20b")))
    data = load_input(__file__, 2023, "20")
    # print(part1(data))
    print(part2(data))

#  python3 day20.py > 20.dot
#  dot -Tpng 20.dot > output.png
