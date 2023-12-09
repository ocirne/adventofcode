from functools import reduce
from math import lcm

from aoc.util import load_input, load_example
import re

NETWORK_PATTERN = r"(\w{3}) = \((\w{3}), (\w{3})\)"


class GhostsMap:
    def __init__(self, lines):
        self.instructions = [0 if d == "L" else 1 for d in lines[0].strip()]
        self.network = {}
        for line in lines[2:]:
            node, right, left = re.match(NETWORK_PATTERN, line).groups()
            self.network[node] = (right, left)

    def measure_path(self, start, end):
        p = start
        i = 0
        while not p.endswith(end):
            p = self.network[p][self.instructions[i % len(self.instructions)]]
            i += 1
        return i


def part1(lines):
    """
    >>> part1(load_example(__file__, "8a"))
    2
    >>> part1(load_example(__file__, "8b"))
    6
    """
    m = GhostsMap(lines)
    return m.measure_path("AAA", "ZZZ")


def list_lcm(a):
    """
    >>> list_lcm([2, 3, 5])
    30
    >>> list_lcm([2, 3, 4])
    12
    """
    return reduce(lcm, a)


def part2(lines):
    """
    >>> part2(load_example(__file__, "8c"))
    6
    """
    m = GhostsMap(lines)
    starts = [p for p in m.network.keys() if p.endswith("A")]
    return list_lcm(m.measure_path(s, "Z") for s in starts)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "8")
    print(part1(data))
    print(part2(data))
