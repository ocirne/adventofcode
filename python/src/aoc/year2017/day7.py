from collections import Counter
from dataclasses import dataclass
from aoc.util import load_example, load_input


@dataclass
class Node:
    name: str
    weight: int
    total_weight: int = 0
    parent: str = None
    children: list = None


def prepare_tree(lines):
    parents = {}
    nodes = {}
    for line in lines:
        name_weight = line.split(")")[0]
        name, weight = name_weight.split(" (")
        node = Node(name, int(weight))
        if "->" in line:
            children = line.strip().split(") -> ")[1].split(", ")
            node.children = children
            for child in children:
                parents[child] = name
        nodes[name] = node
    for child, parent in parents.items():
        nodes[child].parent = parent
    return nodes


def get_root(tree):
    return next(node for node in tree.values() if node.parent is None)


def part1(lines):
    """
    >>> part1(load_example(__file__, '7'))
    'tknk'
    """
    tree = prepare_tree(lines)
    return get_root(tree).name


def calc_correction_weight(nodes, node: Node):
    if node.children is None:
        node.total_weight = node.weight
        return
    for child in node.children:
        result = calc_correction_weight(nodes, nodes[child])
        if result is not None:
            return result
    children_total_weights = [nodes[child].total_weight for child in node.children]
    counts = Counter(children_total_weights).most_common()
    if len(counts) > 1:
        (good_weight, _), (bad_weight, _) = counts
        bad_child = next(child for child in node.children if nodes[child].total_weight == bad_weight)
        return nodes[bad_child].weight - (bad_weight - good_weight)
    node.total_weight = node.weight + sum(children_total_weights)


def part2(lines):
    """
    >>> part2(load_example(__file__, '7'))
    60
    """
    tree = prepare_tree(lines)
    root = get_root(tree)
    return calc_correction_weight(tree, root)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "7")
    print(part1(data))
    print(part2(data))
