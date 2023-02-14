import re
from collections import namedtuple

from aoc.util import load_input, load_example

SCANNER_REGEX = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")


class Valve:
    def __init__(self, name: str, flow_rate: int, neighbors: dict):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors

    def __str__(self):
        return "%s (%s): %s" % (self.name, self.flow_rate, self.neighbors)


def identify_candidate(valves):
    return next((name for name, valve in valves.items() if valve.flow_rate == 0 and len(valve.neighbors) == 2), None)


def simplify(valves: dict):
    """
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG"
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


Result = namedtuple("Result", "current_flow opened expected_flow")


class Cave:
    def __init__(self, lines, minutes):
        self.valves = self.initialize_valves(lines)
        self.non_empty_valves = set(name for name, valve in self.valves.items() if valve.flow_rate > 0)
        self.expect = {}
        self.minutes = minutes

    @staticmethod
    def initialize_valves(lines):
        valves = {}
        for line in lines:
            m = SCANNER_REGEX.match(line)
            name, flow_rate, neighbors = m.groups()
            valves[name] = Valve(name, int(flow_rate), {n: 1 for n in neighbors.split(", ")})
        return simplify(valves)

    def are_all_open(self, opened):
        return self.non_empty_valves == set(opened)

    def search(self, f):
        result = 0
        for limit in range(self.minutes):
            best_flow = f(self, limit)
            if self.are_all_open(best_flow.opened):
                return best_flow.expected_flow
            self.expect[limit] = best_flow.current_flow
            result = max(result, best_flow.expected_flow)
        return result

    def search_part1(self, current="AA", opened=[], duration=0, limit=30, flow_rate=0, flow=0) -> Result:
        if duration > limit:
            return Result(0, [], 0)
        result = Result(flow, opened, flow + (self.minutes - duration - 1) * flow_rate)
        if duration == limit or self.are_all_open(opened):
            return result
        if duration in self.expect and flow + 100 < self.expect[duration]:
            return result
        # open valve
        if current not in opened and self.valves[current].flow_rate > 0:
            new_flow_rate = flow_rate + self.valves[current].flow_rate
            result = max(
                result,
                self.search_part1(
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
                self.search_part1(
                    n,
                    opened,
                    duration + self.valves[current].neighbors[n],
                    limit,
                    flow_rate,
                    flow + flow_rate * self.valves[current].neighbors[n],
                ),
            )
        return result

    def search_part2(
        self,
        turn="me",
        me="AA",
        me_wait=0,
        elephant="AA",
        elephant_wait=0,
        opened=[],
        duration=0,
        limit=30,
        flow_rate=0,
        flow=0,
    ) -> Result:
        result = Result(flow, opened, flow + (self.minutes - duration - 1) * flow_rate)
        if turn == "me":
            if me_wait > 0:
                return self.search_part2(
                    turn="elephant",
                    me=me,
                    me_wait=me_wait - 1,
                    elephant=elephant,
                    elephant_wait=elephant_wait,
                    opened=opened,
                    duration=duration,
                    limit=limit,
                    flow_rate=flow_rate,
                    flow=flow,
                )
            if me not in opened and self.valves[me].flow_rate > 0:
                # open valve
                new_flow_rate = flow_rate + self.valves[me].flow_rate
                result = max(
                    result,
                    self.search_part2(
                        turn="elephant",
                        me=me,
                        me_wait=0,
                        elephant=elephant,
                        elephant_wait=elephant_wait,
                        opened=opened + [me],
                        duration=duration,
                        limit=limit,
                        flow_rate=new_flow_rate,
                        flow=flow,
                    ),
                )
            # visit neighbors
            for n_me in self.valves[me].neighbors:
                result = max(
                    result,
                    self.search_part2(
                        turn="elephant",
                        me=n_me,
                        me_wait=self.valves[me].neighbors[n_me] - 1,
                        elephant=elephant,
                        elephant_wait=elephant_wait,
                        opened=opened,
                        duration=duration,
                        limit=limit,
                        flow_rate=flow_rate,
                        flow=flow,
                    ),
                )
            return result
        elif turn == "elephant":
            if elephant_wait > 0:
                return self.search_part2(
                    turn="wrap",
                    me=me,
                    me_wait=me_wait,
                    elephant=elephant,
                    elephant_wait=elephant_wait - 1,
                    opened=opened,
                    duration=duration,
                    limit=limit,
                    flow_rate=flow_rate,
                    flow=flow,
                )
            if elephant not in opened and self.valves[elephant].flow_rate > 0:
                # open valve
                new_flow_rate = flow_rate + self.valves[elephant].flow_rate
                result = max(
                    result,
                    self.search_part2(
                        turn="wrap",
                        me=me,
                        me_wait=me_wait,
                        elephant=elephant,
                        elephant_wait=0,
                        opened=opened + [elephant],
                        duration=duration,
                        limit=limit,
                        flow_rate=new_flow_rate,
                        flow=flow,
                    ),
                )
            # visit neighbors
            for n_elephant in self.valves[elephant].neighbors:
                result = max(
                    result,
                    self.search_part2(
                        turn="wrap",
                        me=me,
                        me_wait=me_wait,
                        elephant=n_elephant,
                        elephant_wait=self.valves[elephant].neighbors[n_elephant] - 1,
                        opened=opened,
                        duration=duration,
                        limit=limit,
                        flow_rate=flow_rate,
                        flow=flow,
                    ),
                )
            return result
        else:
            if duration > limit:
                return Result(0, [], 0)
            if duration == limit or self.are_all_open(opened):
                return result
            if duration in self.expect and flow + 50 < self.expect[duration]:
                return result
            return self.search_part2(
                turn="me",
                me=me,
                me_wait=me_wait,
                elephant=elephant,
                elephant_wait=elephant_wait,
                opened=opened,
                duration=duration + 1,
                limit=limit,
                flow_rate=flow_rate,
                flow=flow + flow_rate,
            )


def part1(lines):
    """
    >>> part1(load_example(__file__, "16"))
    1651
    """
    return Cave(lines, 30).search(lambda cave, limit: cave.search_part1(limit=limit))


def part2(lines):
    """
    >>> part2(load_example(__file__, "16"))
    1707
    """
    return Cave(lines, 26).search(lambda cave, limit: cave.search_part2(limit=limit))


if __name__ == "__main__":
    #    data = load_input(__file__, 2022, "16")
    data = load_example(__file__, "16")
    print(part1(data))
    print(part2(data))
