from aoc.util import load_input, load_example


def neighbors(x, y, z, m=25):
    if x >= 0:
        yield x - 1, y, z
    if x < m:
        yield x + 1, y, z
    if y >= 0:
        yield x, y - 1, z
    if y < m:
        yield x, y + 1, z
    if z >= 0:
        yield x, y, z - 1
    if z < m:
        yield x, y, z + 1


def part1(lines):
    """
    >>> part1(["1,1,1", "2,1,1"])
    10
    >>> part1(load_example(__file__, "18"))
    64
    """
    c = {tuple(map(int, line.strip().split(","))) for line in lines}
    return sum(
        int((x + d, y, z) not in c) + int((x, y + d, z) not in c) + int((x, y, z + d) not in c)
        for x, y, z in c
        for d in (-1, +1)
    )


def part2(lines):
    """
    >>> part2(load_example(__file__, "18"))
    58
    """
    droplets = {tuple(map(int, line.strip().split(","))) for line in lines}
    open_list = [(0, 0, 0)]
    closed_set = set()
    while open_list:
        #        print("open list", len(open_list))
        current_droplet = open_list.pop()
        #        print("current", current_droplet)
        # visit neighbors
        closed_set.add(current_droplet)
        for neighbor in neighbors(*current_droplet):
            if neighbor in closed_set:
                continue
            if neighbor in droplets:
                continue
            open_list.append(neighbor)
    #    print(len(closed_set))
    return sum(int(n not in droplets and n in closed_set) for x, y, z in droplets for n in neighbors(x, y, z))


if __name__ == "__main__":
    data = load_input(__file__, 2022, "18")
    #    data = load_example(__file__, "18")
    #    print(part1(data))
    print(part2(data))
