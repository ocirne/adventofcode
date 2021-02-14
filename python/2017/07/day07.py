from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Node:
    name: str
    weight: int
    total_weight: int = 0
    parent: str = None
    children: list = None


def read_tree(filename):
    parents = {}
    nodes = {}
    f = open(filename, 'r')
    for line in f.readlines():
        name_weight = line.split(')')[0]
        name, weight = name_weight.split(' (')
        node = Node(name, int(weight))
        if '->' in line:
            children = line.strip().split(') -> ')[1].split(', ')
            node.children = children
            for child in children:
                parents[child] = name
        nodes[name] = node
    for child, parent in parents.items():
        nodes[child].parent = parent
    return nodes


def get_root(tree):
    return next(node for node in tree.values() if node.parent is None)


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    'tknk'
    """
    tree = read_tree(filename)
    return get_root(tree).name


def calc_total_weight(nodes, node: Node):
    if node.children is None:
        node.total_weight = node.weight
        return
    for child in node.children:
        result = calc_total_weight(nodes, nodes[child])
        if result is not None:
            return result
    children_total_weights = [nodes[child].total_weight for child in node.children]
    counts = Counter(children_total_weights)
    if len(counts) > 1:
        good_weight = next(name for name, count in counts.items() if count > 1)
        bad_weight = next(name for name, count in counts.items() if count == 1)
        bad_child = next(child for child in node.children if nodes[child].total_weight == bad_weight)
        return nodes[bad_child].weight - (bad_weight - good_weight)
    node.total_weight = node.weight + sum(children_total_weights)


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    60
    """
    tree = read_tree(filename)
    root = get_root(tree)
    return calc_total_weight(tree, root)


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
