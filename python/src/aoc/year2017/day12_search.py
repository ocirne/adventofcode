from aoc.util import load_input, load_example


def prepare_data(lines):
    edges = {}
    for line in lines:
        root, children = line.split(" <-> ")
        edges[int(root)] = [int(c) for c in children.split(", ")]
    return edges


def search(edges, start):
    open_set = set()
    closed_set = set()
    current = start
    open_set.add(current)
    while open_set:
        current = min(open_set)
        open_set.remove(current)
        closed_set.add(current)
        for e in edges[current]:
            if e not in closed_set:
                open_set.add(e)
    return closed_set


def part1(lines):
    """
    >>> part1(load_example(__file__, '12'))
    6
    """
    edges = prepare_data(lines)
    return len(search(edges, 0))


def part2(lines):
    """
    >>> part2(load_example(__file__, '12'))
    2
    """
    edges = prepare_data(lines)
    open_set = set(edges.keys())
    count_groups = 0
    while open_set:
        start = min(open_set)
        group = search(edges, start)
        open_set.difference_update(group)
        count_groups += 1
    return count_groups


if __name__ == "__main__":
    data = load_input(__file__, 2017, "12")
    print(part1(data))
    print(part2(data))
