import re

from aoc.util import load_input, load_example

SCANNER_REGEX = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")


class Valve:
    def __init__(self, name, flow_rate, neighbors):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors

    def __str__(self):
        return "%s (%s): %s" % (self.name, self.flow_rate, self.neighbors)


LIMIT = 30


class Cave:
    def __init__(self, valves):
        self.valves = valves
        self.expect = {}

    def search2(self):
        for limit in range(LIMIT):
            best_flow = self.search("AA", limit=limit)
            print(limit, best_flow)
            self.expect[limit] = best_flow[0]
        return self.expect[LIMIT - 1]

    def search(self, current="AA", opened=[], duration=0, limit=30, total_flow_rate=0, last_total_flow=0):
        #        print(total_flow_rate, last_total_flow)
        total_flow = last_total_flow + total_flow_rate
        #        print("end, current, %s, opened: %s, total_flow: %s" % (current, opened, total_flow))
        if duration == limit:
            #            print("end, current, %s, opened: %s, total_flow: %s" % (current, opened, total_flow))
            #            print("end")
            return (total_flow, opened)
        if duration in self.expect and total_flow + 50 < self.expect[duration]:
            return (0, [])
        result = (0, [])
        if current not in opened and self.valves[current].flow_rate > 0:
            result = max(
                result,
                self.search(
                    current,
                    opened + [current],
                    duration + 1,
                    limit,
                    total_flow_rate + self.valves[current].flow_rate,
                    total_flow,
                ),
            )
        for n in self.valves[current].neighbors:
            result = max(result, self.search(n, opened, duration + 1, limit, total_flow_rate, total_flow))
        return result


def part1(lines):
    """
    >>> part1(load_example(__file__, "16"))
    1651
    """
    valves = {}
    for line in lines:
        m = SCANNER_REGEX.match(line)
        name, flow_rate, neighbors = m.groups()
        valves[name] = Valve(name, int(flow_rate), neighbors.split(", "))
    cave = Cave(valves)
    return cave.search2()


def part2(lines):
    """
    >>> part2(load_example(__file__, "16"))

    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2022, "16")
    #    data = load_example(__file__, "16")
    print(part1(data))
#    print(part2(data))
