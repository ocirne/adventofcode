from aoc.util import load_input, load_example

import sys

sys.setrecursionlimit(142 * 142)


def read_trail(lines):
    trail, start, end = {}, None, None
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            if v in ".<>^v":
                trail[x, y] = v
                if y == 0:
                    start = x, y
                if y == len(lines) - 1:
                    end = x, y
    return trail, start, end


A = {
    "<": ">",
    ">": "<",
    "^": "v",
    "v": "^",
}


def neighbors(trail, current_node):
    (x, y), d, g, visited = current_node
    for next_pos, nd in (((x - 1, y), "<"), ((x + 1, y), ">"), ((x, y - 1), "^"), ((x, y + 1), "v")):
        if nd == A[d]:
            continue
        if next_pos not in trail:
            continue
        if trail[x, y] != "." and trail[x, y] != nd:
            continue
        if str(next_pos) in visited:
            continue
        yield next_pos, nd, g + 1, visited + str(next_pos)


def foo(trail, start, end):
    open_set = {(start, "v", 0, "")}
    closed_set = set()
    while open_set:
        # print(len(open_set))
        current_node = open_set.pop()
        print(current_node[2])
        if current_node[0] == end:
            print(current_node[2], current_node[3])
            yield current_node[2]
        if current_node in closed_set:
            continue
        closed_set.add(current_node)
        for next_node in neighbors(trail, current_node):
            if next_node in closed_set:
                continue
            open_set.add(next_node)


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    94
    """
    trail, start, end = read_trail(lines)
    return max(foo(trail, start, end))


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    """


if __name__ == "__main__":
    # print(part1(load_example(__file__, "23")))
    data = load_input(__file__, 2023, "23")
    print(part1(data))
    # print(part2(data))
