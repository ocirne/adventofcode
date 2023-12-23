from aoc.util import load_input, load_example


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
    ".": None,
    "<": ">",
    ">": "<",
    "^": "v",
    "v": "^",
}


def neighbors(trail, current_node):
    g, (x, y), d = current_node
    for next_pos, nd in (((x - 1, y), "<"), ((x + 1, y), ">"), ((x, y - 1), "^"), ((x, y + 1), "v")):
        if nd == A[d]:
            continue
        if next_pos not in trail:
            continue
        if trail[next_pos] == nd or trail[next_pos] == ".":
            yield g + 1, next_pos, nd


def dijkstra(trail, start, end):
    open_set = {(0, start, "v")}
    closed_set = set()
    while open_set:
        print(len(open_set))
        current_node = open_set.pop()
        if current_node[1] == end:
            print(current_node)
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
    16
    """
    trail, start, end = read_trail(lines)
    return dijkstra(trail, start, end)


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    """


if __name__ == "__main__":
    print(part1(load_example(__file__, "23")))
    # data = load_input(__file__, 2023, "21")
    # print(part1(data))
    # print(part2(data))
