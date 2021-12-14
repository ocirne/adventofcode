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
        self.g = 0
        self.h = 0
        self.f = 0

    def elements_on_current_floor(self):
        return [item for item, floor in self.items.items() if floor == self.elevator]

    def is_valid_state(self):
        for (name, mc_type), mc_floor in self.items.items():
            if mc_type != "m":
                continue
            if self.items[name, "g"] == mc_floor:
                continue
            if any(g_type == "g" and g_floor == mc_floor for (_, g_type), g_floor in self.items.items()):
                return False
        return True

    def is_end_state(self):
        return all(floor == 4 for floor in self.items.values())

    def __eq__(self, other):
        return self.items.values() == other.items.values()

    def __hash__(self):
        return hash(self.items.values())


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
    return [move for move in moves if move.is_valid_state()]


def read_initial_state(lines):
    items = {}
    for index, line in enumerate(lines):
        line_number = index + 1
        for g in re.findall(GENERATOR_PATTERN, line):
            items[g, "g"] = line_number
        for m in re.findall(MICROCHIP_PATTERN, line):
            items[m, "m"] = line_number
    return Node(1, items)


def a_star(initial_node):
    open_list = [initial_node]
    closed_set = set()
    while open_list:
        print("open:", len(open_list), "closed:", len(closed_set))
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_set.add(current_node)

        if current_node.is_end_state():
            print("win condition:", current_node.items)
            depth = -1
            while current_node is not None:
                print("path:", current_node.elevator, current_node.items)
                current_node = current_node.parent
                depth += 1
            print("return", depth)
            return depth
        # expand node
        for successor in valid_moves(current_node):
            if successor in closed_set:
                continue
            successor.g = current_node.g + 1
            successor.h = sum(4 - floor for floor in successor.items.values())
            successor.f = successor.g + successor.h
            if successor in open_list:
                index = open_list.index(successor)
                if successor.g > open_list[index].g:
                    continue
            open_list.insert(0, successor)


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    11
    """
    initial_node = read_initial_state(lines)
    return a_star(initial_node)


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
#    print(part1(data))
#    print(part2(data))
