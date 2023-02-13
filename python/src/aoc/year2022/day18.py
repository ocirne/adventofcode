from aoc.util import load_input, load_example


def neighbors(x, y, z, m):
    if x >= 0:
        yield x - 1, y, z
    if x <= m:
        yield x + 1, y, z
    if y >= 0:
        yield x, y - 1, z
    if y <= m:
        yield x, y + 1, z
    if z >= 0:
        yield x, y, z - 1
    if z <= m:
        yield x, y, z + 1


def parse_droplets(lines):
    return {tuple(map(int, line.strip().split(","))) for line in lines}


def count_sides(droplets, it_matters=lambda _: True):
    return sum(int(n not in droplets and it_matters(n)) for x, y, z in droplets for n in neighbors(x, y, z, 100))


def part1(lines):
    """
    >>> part1(["1,1,1", "2,1,1"])
    10
    >>> part1(load_example(__file__, "18"))
    64
    """
    droplets = parse_droplets(lines)
    return count_sides(droplets)


def find_outside(droplets, m):
    open_list = [(0, 0, 0)]
    closed_set = set()
    while open_list:
        current_droplet = open_list.pop()
        closed_set.add(current_droplet)
        for neighbor in neighbors(*current_droplet, m):
            if neighbor in closed_set or neighbor in droplets:
                continue
            open_list.append(neighbor)
    return closed_set


def part2(lines, m=21):
    """
    >>> part2(load_example(__file__, "18"), 6)
    58
    """
    droplets = parse_droplets(lines)
    outside = find_outside(droplets, m)
    return count_sides(droplets, lambda n: n in outside)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "18")
    print(part1(data))
    print(part2(data))
