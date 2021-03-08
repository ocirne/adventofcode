from abc import ABC, abstractmethod
from collections import defaultdict, Counter
from dataclasses import dataclass

from aoc.util import load_input, load_example


@dataclass
class Connector:
    left: int
    right: int
    value: int
    length: int = 1

    def other_port(self, x):
        if x == self.left:
            return self.right
        return self.left

    def __hash__(self):
        return tuple.__hash__((self.left, self.right, self.value, self.length))


class Search(ABC):
    def __init__(self, connectors):
        self.max = 0
        self.result = 0
        self.acc = set()
        self.lookup = defaultdict(list)
        for con in connectors:
            self.lookup[con.left].append(con)
            self.lookup[con.right].append(con)

    def search(self, left_port):
        nothing = True
        for connector in self.lookup[left_port]:
            if connector in self.acc:
                continue
            nothing = False
            right_port = connector.other_port(left_port)
            self.acc.add(connector)
            self.search(right_port)
            self.acc.remove(connector)
        if nothing:
            self.max_criterion()

    @abstractmethod
    def max_criterion(self):
        pass


class Part1(Search):
    def max_criterion(self):
        value = sum(con.value for con in self.acc)
        if value > self.max:
            self.result = value
            self.max = value


class Part2(Search):
    def max_criterion(self):
        value = sum(con.length for con in self.acc)
        if value >= self.max:
            self.result = max(self.result, sum(con.value for con in self.acc))
            self.max = value


def connect_twice(connectors):
    """ values which are exactly twice in the list can be used to merge to connectors """
    result = connectors
    while True:
        values = [con.left for con in result] + [con.right for con in result]
        twice = next((value for value, count in Counter(values).items() if value != 0 and count == 2), None)
        if twice is None:
            return result
        acc = [c for c in result if c.left != twice and c.right != twice]
        c1, c2 = (c for c in result if c.left == twice or c.right == twice)
        o1 = c1.other_port(twice)
        o2 = c2.other_port(twice)
        con = Connector(o1, o2, c1.value + c2.value, c1.length + c2.length)
        acc.append(con)
        result = acc


def run(lines, search_clazz):
    connectors = []
    for line in lines:
        x, y = (int(t) for t in line.split("/"))
        connectors.append(Connector(x, y, x + y))
    connectors = connect_twice(connectors)
    search = search_clazz(connectors)
    search.search(0)
    return search.result


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    31
    """
    return run(lines, Part1)


def part2(lines):
    """
    >>> part2(load_example(__file__, "24"))
    19
    """
    return run(lines, Part2)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "24")
    print(part1(data))
    print(part2(data))
