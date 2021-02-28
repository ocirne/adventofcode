import json

from aoc.util import load_input


def traverse(node, ignore_red):
    if isinstance(node, dict):
        if ignore_red and 'red' in node.values():
            return 0
        # keys are never numeric
        return sum(traverse(value, ignore_red) for value in node.values())
    elif isinstance(node, list):
        return sum(traverse(item, ignore_red) for item in node)
    elif isinstance(node, int):
        return node
    else:
        return 0


def part1(lines):
    """
    >>> part1(['[1,2,3]'])
    6
    >>> part1(['{"a":2,"b":4}'])
    6
    >>> part1(['[[[3]]]'])
    3
    >>> part1(['{"a":{"b":4},"c":-1}'])
    3
    >>> part1(['{"a":[-1,1]}'])
    0
    >>> part1(['[-1,{"a":1}]'])
    0
    >>> part1(['[]'])
    0
    >>> part1(['{}'])
    0
    """
    root = json.loads(lines[0])
    return traverse(root, ignore_red=False)


def part2(lines):
    """
    >>> part2(['[1,2,3]'])
    6
    >>> part2(['[1,{"c":"red","b":2},3]'])
    4
    >>> part2(['{"d":"red","e":[1,2,3,4],"f":5}'])
    0
    >>> part2(['[1,"red",5]'])
    6
    """
    root = json.loads(lines[0])
    return traverse(root, ignore_red=True)


if __name__ == "__main__":
    data = load_input(__file__, 2015, '12')
    print(part1(data))
    print(part2(data))
