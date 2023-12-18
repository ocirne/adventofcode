from aoc.util import load_input, load_example


MOVES = {
    "U": (-1, 0),
    "D": (+1, 0),
    "L": (0, -1),
    "R": (0, +1),
}


def wander(lines):
    py, px = 0, 0
    edge = set()
    for line in lines:
        direction, count, _ = line.split()
        dy, dx = MOVES[direction]
        for i in range(int(count)):
            py += dy
            px += dx
            edge.add((py, px))
    return edge


def neighbors(pos):
    py, px = pos
    return (py - 1, px), (py + 1, px), (py, px - 1), (py, px + 1)


def flooding(edge, start):
    assert start not in edge
    open_set = {start}
    real_inner_area = set()
    while open_set:
        if len(open_set) > 1000:
            # oops, outer area
            return None
        pos = open_set.pop()
        real_inner_area.add(pos)
        for neighbor in neighbors(pos):
            if neighbor in edge:
                continue
            if neighbor in real_inner_area:
                continue
            open_set.add(neighbor)
    assert not edge.intersection(real_inner_area)
    return edge.union(real_inner_area)


def part1(lines):
    """
    good enough

    >>> part1(load_example(__file__, "18"))
    62
    """
    edge = wander(lines)
    foo = flooding(edge, (1, 1))
    min_x = min(x for _, x in foo)
    max_x = max(x for _, x in foo)
    min_y = min(y for y, _ in foo)
    max_y = max(y for y, _ in foo)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) in edge:
                print("#", end="")
            else:
                print(".", end="")
        print()
    return len(foo)


def part2(lines):
    """
    >>> part2(load_example(__file__, "18"))
    """


if __name__ == "__main__":
    # print(part1(load_example(__file__, "18")))
    data = load_input(__file__, 2023, "18")
    print(part1(data))
    # print(part2(data))
