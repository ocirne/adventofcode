import re
from itertools import combinations

from aoc.util import load_input, load_example

GENERATOR_PATTERN = r"(\w+) generator"
MICROCHIP_PATTERN = r"(\w+)-compatible microchip"


class Node:
    def __init__(self, elevator, items, parent=None):
        self.elevator = elevator
        self.items = items
        self.parent = parent

    def elements_on_current_floor(self):
        return [item for item, floor in self.items.items() if floor == self.elevator]

    def is_valid_state(self):
        for (name, mc_type), mc_floor in self.items.items():
            if mc_type == "g":
                continue
            if self.items[name, "g"] == mc_floor:
                continue
            if any(g_type == "g" and g_floor == mc_floor for (_, g_type), g_floor in self.items.items()):
                return False
        return True

    def is_end_state(self):
        return all(floor == 4 for floor in self.items.values())


def valid_moves(node: Node):
    moves = []
    if node.elevator > 1:
        # one item
        for i in node.elements_on_current_floor():
            c = node.items.copy()
            c[i] -= 1
            moves.append(Node(node.elevator - 1, c, node))
        # two items
        for i1, i2 in combinations(node.elements_on_current_floor(), 2):
            c = node.items.copy()
            c[i1] -= 1
            c[i2] -= 1
            moves.append(Node(node.elevator - 1, c, node))
    if node.elevator < 4:
        # one item
        for i in node.elements_on_current_floor():
            c = node.items.copy()
            c[i] += 1
            moves.append(Node(node.elevator + 1, c, node))
        # two items
        for i1, i2 in combinations(node.elements_on_current_floor(), 2):
            c = node.items.copy()
            c[i1] += 1
            c[i2] += 1
            moves.append(Node(node.elevator + 1, c, node))
    return [move for move in moves if node.is_valid_state()]


def read_initial_state(lines):
    items = {}
    for index, line in enumerate(lines):
        line_number = index + 1
        for g in re.findall(GENERATOR_PATTERN, line):
            items[g, "g"] = line_number
        for m in re.findall(MICROCHIP_PATTERN, line):
            items[m, "m"] = line_number
    return Node(1, items)


def bfs(initial_node):
    next_level = [initial_node]
    depth = 0
    while True:
        depth += 1
        current_level = next_level
        print(depth, len(current_level))
        next_level = []
        for node in current_level:
            next_level.extend(valid_moves(node))
        for node in next_level:
            #            print(node.items)
            if node.is_end_state():
                print("win", depth, node.items)
                while node is not None:
                    print(node.elevator, node.items)
                    node = node.parent
                return depth
        if not next_level:
            return


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    11
    """
    return bfs(read_initial_state(lines))


def part2(lines):
    """
    >>> part2(load_example(__file__, "11"))
    30
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2016, "11")
    assert part1(load_example(__file__, "11")) == 11
    print("--")
    print(part1(data))
#    print(part2(data))
