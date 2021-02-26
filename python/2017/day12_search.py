from pathlib import Path


def read_data(filename):
    edges = {}
    f = open(filename)
    for line in f.readlines():
        root, children = line.strip().split(' <-> ')
        edges[int(root)] = [int(c) for c in children.split(', ')]
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


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'references/12.txt')
    6
    """
    edges = read_data(filename)
    return len(search(edges, 0))


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'references/12.txt')
    2
    """
    edges = read_data(filename)
    open_set = set(edges.keys())
    count_groups = 0
    while open_set:
        start = min(open_set)
        group = search(edges, start)
        open_set.difference_update(group)
        count_groups += 1
    return count_groups
