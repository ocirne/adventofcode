import hashlib

from aoc.util import load_input

import sys

sys.setrecursionlimit(2_000)


class Node:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path

    def wins(self):
        return self.x == 3 and self.y == 3


def next_moves(passcode, node):
    md5_hash = hashlib.md5((passcode + node.path).encode()).hexdigest()
    up, down, left, right = (int(x, 16) for x in md5_hash[:4])
    result = []
    if up > 10 and node.y > 0:
        result.append(Node(node.x, node.y - 1, node.path + "U"))
    if down > 10 and node.y < 3:
        result.append(Node(node.x, node.y + 1, node.path + "D"))
    if left > 10 and node.x > 0:
        result.append(Node(node.x - 1, node.y, node.path + "L"))
    if right > 10 and node.x < 3:
        result.append(Node(node.x + 1, node.y, node.path + "R"))
    return result


def bfs(passcode):
    next_level = [Node(0, 0, "")]
    while True:
        current_level = next_level
        next_level = []
        for node in current_level:
            next_level.extend(next_moves(passcode, node))
        for node in next_level:
            if node.wins():
                return node.path
        if not next_level:
            return


def part1(lines):
    """
    >>> part1(['hijkl'])
    >>> part1(['ihgpwlah'])
    'DDRRRD'
    >>> part1(['kglvqrro'])
    'DDUDRLRRUDRD'
    >>> part1(['ulqzkmiv'])
    'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    """
    passcode = lines[0].strip()
    return bfs(passcode)


def dfs(passcode, node):
    if node.wins():
        return len(node.path)
    results = [dfs(passcode, next_node) for next_node in next_moves(passcode, node)]
    if not results:
        return 0
    return max(results)


def part2(lines):
    """
    >>> part2(['ihgpwlah'])
    370
    >>> part2(['kglvqrro'])
    492
    >>> part2(['ulqzkmiv'])
    830
    """
    passcode = lines[0].strip()
    return dfs(passcode, Node(0, 0, ""))


if __name__ == "__main__":
    data = load_input(__file__, 2016, "17")
    print(part1(data))
    print(part2(data))
