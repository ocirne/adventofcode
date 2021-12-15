from heapq import heappush, heappop

from aoc.util import load_input, load_example


def load_cave(lines):
    cave = {}
    for y, line in enumerate(lines):
        for x, risk_level in enumerate(map(int, line.strip())):
            cave[x, y] = risk_level
    return cave


def find_neighbors(cave, current_node):
    x, y = current_node
    neighbors = []
    if (x - 1, y) in cave:
        neighbors.append((x - 1, y))
    if (x + 1, y) in cave:
        neighbors.append((x + 1, y))
    if (x, y - 1) in cave:
        neighbors.append((x, y - 1))
    if (x, y + 1) in cave:
        neighbors.append((x, y + 1))
    return neighbors


def a_star(score):
    start_node = (0, 0)
    end_node = max(score)
    open_heap = []
    closed_set = set()
    parent = {}
    g = {start_node: 0}

    heappush(open_heap, (0, start_node))
    while open_heap:
        print("open:", len(open_heap), "closed:", len(closed_set))
        current_node = heappop(open_heap)[1]

        if current_node == end_node:
            length = 0
            while current_node in parent:
                print(score[current_node], current_node)
                length += score[current_node]
                current_node = parent[current_node]
            print("return", length)
            return length

        closed_set.add(current_node)
        # expand node
        for neighbor in find_neighbors(score, current_node):
            if neighbor in closed_set:
                continue
            tentative_g = g[current_node] + score[neighbor]
            if neighbor in open_heap and tentative_g >= g[neighbor]:
                continue

            if tentative_g < g.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap]:
                parent[neighbor] = current_node
                g[neighbor] = tentative_g
                heappush(open_heap, (tentative_g, neighbor))


def part1(lines):
    """
    >>> part1(load_example(__file__, "14"))
    40
    """
    cave = load_cave(lines)
    result = a_star(cave)
    return result


if __name__ == "__main__":
    data = load_input(__file__, 2021, "15")
    assert part1(load_example(__file__, "15")) == 40
    print(part1(data))
#    print(part2(data))
