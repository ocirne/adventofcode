import re

from aoc.util import load_input, load_example

SCANNER_REGEX = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")
LIMIT = 30
LIMIT2 = 26


class Valve:
    def __init__(self, name: str, flow_rate: int, neighbors: list):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors: dict = {n: 1 for n in neighbors}

    def __str__(self):
        return "%s (%s): %s" % (self.name, self.flow_rate, self.neighbors)


def identify_candidate(valves):
    for name, valve in valves.items():
        if valve.flow_rate == 0 and len(valve.neighbors) == 2:
            return name


def simplify(valves: dict):
    """
    Valve FF has flow rate=0; tunnels lead to valves EE, GG
    EE->(1)->FF->(1)->GG
    is the same as
    EE->(2)->GG
    """
    while True:
        middle = identify_candidate(valves)
        if middle is None:
            return valves
        n1, n2 = valves[middle].neighbors.keys()
        weight = valves[middle].neighbors[n1] + valves[middle].neighbors[n2]
        valves[n1].neighbors[n2] = weight
        valves[n2].neighbors[n1] = weight
        del valves[n1].neighbors[middle]
        del valves[n2].neighbors[middle]
        del valves[middle]


class Cave:
    def __init__(self, valves):
        self.valves = valves
        self.interesting_valves = set(name for name, valve in valves.items() if valve.flow_rate > 0)
        self.expect = {}

    def search2(self):
        result = 0
        for limit in range(LIMIT):
            best_flow = self.search("AA", limit=limit)
            if self.all_are_open(best_flow[1]):
                return best_flow[2]
            print(limit, best_flow, "**")
            self.expect[limit] = best_flow[0]
            result = max(result, best_flow[2])
        for key, value in self.expect.items():
            print(key, value)
        print("result", result)
        return result

    def search(self, current="AA", opened=[], duration=0, limit=30, flow_rate=0, flow=0):
        #        print(total_flow_rate, last_total_flow)
        #        total_flow = last_total_flow + total_flow_rate
        #        print("end, current, %s, opened: %s, total_flow: %s" % (current, opened, total_flow))
        if duration > limit:
            return 0, [], 0
        if duration == limit or self.all_are_open(opened):
            #            print("end, current, %s, opened: %s, total_flow: %s" % (current, opened, total_flow))
            #            print("end")
            return flow, opened, flow + (LIMIT - duration - 1) * flow_rate
        if duration in self.expect and flow + 100 < self.expect[duration]:
            return flow, opened, flow + (LIMIT - duration - 1) * flow_rate
        result = flow, opened, flow + (LIMIT - duration - 1) * flow_rate
        # open valve
        if current not in opened and self.valves[current].flow_rate > 0:
            new_flow_rate = flow_rate + self.valves[current].flow_rate
            result = max(
                result,
                self.search(
                    current,
                    opened + [current],
                    duration + 1,
                    limit,
                    new_flow_rate,
                    flow + new_flow_rate,
                ),
            )
        # visit neighbors
        for n in self.valves[current].neighbors:
            result = max(
                result,
                self.search(
                    n,
                    opened,
                    duration + self.valves[current].neighbors[n],
                    limit,
                    flow_rate,
                    flow + flow_rate * self.valves[current].neighbors[n],
                ),
            )
        return result

    def search3(self):
        for limit in range(LIMIT2):
            best_flow = self.search4("AA", limit=limit)
            print(limit, best_flow)
            if self.all_are_open(best_flow[1]):
                return best_flow[2]
            self.expect[limit] = best_flow[0]
        return self.expect[LIMIT2 - 1]

    def all_are_open(self, opened):
        return self.interesting_valves == set(opened)

    def search4(self, turn="me", me="AA", elephant="AA", opened=[], duration=0, limit=30, flow_rate=0, flow=0):
        if turn == "me":
            result = (0, [])
            if me not in opened and self.valves[me].flow_rate > 0:
                result = max(
                    result,
                    self.search4(
                        "elephant",
                        me,
                        elephant,
                        opened + [me],
                        duration,
                        limit,
                        flow_rate + self.valves[me].flow_rate,
                        flow,
                    ),
                )
            for n_me in self.valves[me].neighbors:
                result = max(result, self.search4("elephant", n_me, elephant, opened, duration, limit, flow_rate, flow))
            return result
        elif turn == "elephant":
            result = (0, [])
            if elephant not in opened and self.valves[elephant].flow_rate > 0:
                result = max(
                    result,
                    self.search4(
                        "wrap",
                        me,
                        elephant,
                        opened + [elephant],
                        duration,
                        limit,
                        flow_rate + self.valves[elephant].flow_rate,
                        flow,
                    ),
                )
            for n_elephant in self.valves[elephant].neighbors:
                result = max(result, self.search4("wrap", me, n_elephant, opened, duration, limit, flow_rate, flow))
            return result
        else:
            if duration == limit or self.all_are_open(opened):
                return flow, opened, flow + (LIMIT2 - duration) * flow_rate
            if duration in self.expect and flow + 30 < self.expect[duration]:
                return 0, []
            return self.search4(
                "me",
                me,
                elephant,
                opened,
                duration + 1,
                limit,
                flow_rate,
                flow + flow_rate,
            )


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
    cave = Cave(simplify(valves))
    #    for valve in cave.valves.values():
    #        print(valve)
    return cave.search2()


def part2(lines):
    """
    >>> part2(load_example(__file__, "16"))
    1707
    """
    valves = {}
    for line in lines:
        m = SCANNER_REGEX.match(line)
        name, flow_rate, neighbors = m.groups()
        valves[name] = Valve(name, int(flow_rate), neighbors.split(", "))
    cave = Cave(simplify(valves))
    return cave.search3()


if __name__ == "__main__":
    #    data = load_input(__file__, 2022, "16")
    data = load_example(__file__, "16")
    print(part1(data))
#    print(part2(data))
