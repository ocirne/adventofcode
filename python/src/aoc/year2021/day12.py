from collections import defaultdict

from aoc.util import load_input, load_example


def dfs(nodes, current="start", visited=None, twice_allowed=True):
    if visited is None:
        visited = ["start"]
    if current == "end":
        return 1
    count_paths = 0
    for n in nodes[current]:
        if not n.isupper() and n in visited:
            if twice_allowed and n != "start" and n != "end":
                count_paths += dfs(nodes, n, visited + [n], False)
            continue
        count_paths += dfs(nodes, n, visited + [n], twice_allowed)
    return count_paths


def count_all_paths(lines, twice_allowed):
    nodes = defaultdict(list)
    for line in lines:
        a, b = line.strip().split("-")
        nodes[a].append(b)
        nodes[b].append(a)
    return dfs(nodes, twice_allowed=twice_allowed)


def part1(lines):
    """
    >>> part1(load_example(__file__, "12a"))
    10
    >>> part1(load_example(__file__, "12b"))
    19
    >>> part1(load_example(__file__, "12c"))
    226
    """
    return count_all_paths(lines, twice_allowed=False)


def part2(lines):
    """
    >>> part2(load_example(__file__, "12a"))
    36
    >>> part2(load_example(__file__, "12b"))
    103
    >>> part2(load_example(__file__, "12c"))
    3509
    """
    return count_all_paths(lines, twice_allowed=True)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "12")
    print(part1(data))
    print(part2(data))
