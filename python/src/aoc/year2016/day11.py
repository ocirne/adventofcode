import re
from heapq import heappush, heappop
from itertools import combinations

from aoc.util import load_input, load_example

GENERATOR_PATTERN = r"(\w+) generator"
MICROCHIP_PATTERN = r"(\w+)-compatible microchip"


class Node:
    def __init__(self, elevator, items, parent=None):
        self.elevator = elevator
        self.items = items
        self.key = str(self.elevator) + str(sorted(self.items.items()))
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def elements_on_current_floor(self):
        return [item for item, floor in self.items.items() if floor == self.elevator]

    def min_floor(self):
        return min(floor for _, floor in self.items.items())

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

    def score(self):
        return sum(4 - floor for floor in self.items.values())

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __gt__(self, other):
        return self.score() >= other.score()


def valid_moves(parent: Node):
    moves = []
    if parent.elevator > parent.min_floor():
        # one item
        for i in parent.elements_on_current_floor():
            c = parent.items.copy()
            c[i] -= 1
            moves.append(Node(parent.elevator - 1, c, parent))
        # two items
    #        for i1, i2 in combinations(parent.elements_on_current_floor(), 2):
    #            c = parent.items.copy()
    #            c[i1] -= 1
    #            c[i2] -= 1
    #            moves.append(Node(parent.elevator - 1, c, parent))
    if parent.elevator < 4:
        # one item
        for i in parent.elements_on_current_floor():
            c = parent.items.copy()
            c[i] += 1
            moves.append(Node(parent.elevator + 1, c, parent))
        # two items
        for i1, i2 in combinations(parent.elements_on_current_floor(), 2):
            c = parent.items.copy()
            c[i1] += 1
            c[i2] += 1
            moves.append(Node(parent.elevator + 1, c, parent))
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
    open_heap = []
    closed_set = set()

    heappush(open_heap, (0, initial_node))
    while open_heap:
        print("open:", len(open_heap), "closed:", len(closed_set))
        current_node = heappop(open_heap)[1]
        if current_node.is_end_state():
            print("win condition:", current_node.items)
            depth = -1
            path_node = current_node
            while path_node is not None:
                print("path:", path_node.elevator, path_node.items)
                path_node = path_node.parent
                depth += 1
            print("return", depth)
            return depth
        closed_set.add(current_node)
        # expand node
        for successor in valid_moves(current_node):
            if successor in closed_set:
                continue
            tentative_g = current_node.g + 1
            if successor in closed_set and tentative_g >= successor.g:
                continue
            if tentative_g < successor.g or successor not in [i[1] for i in open_heap]:
                successor.parent = current_node
                successor.g = tentative_g
                h = successor.score()
                f = tentative_g + h
                #                print('g', successor.g, 'h', h, 'f', f)
                heappush(open_heap, (f, successor))


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
    print(part1(data))
#    print(part2(data))
