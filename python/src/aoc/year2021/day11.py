from aoc.util import load_input, load_example


def simulate_step(area):
    # brighten up
    for x in range(10):
        for y in range(10):
            area[x, y] += 1
    # flashes
    flashed = {}
    flashes_occur = True
    while flashes_occur:
        flashes_occur = False
        for x in range(10):
            for y in range(10):
                if area[x, y] > 9 and (x, y) not in flashed:
                    flashed[x, y] = True
                    flashes_occur = True
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if (x + dx, y + dy) in area:
                                area[x + dx, y + dy] += 1
    # burnout
    for x in range(10):
        for y in range(10):
            if (x, y) in flashed:
                area[x, y] = 0
    return area, len(flashed)


def simulate(lines, steps):
    area = {}
    for y, line in enumerate(lines):
        for x, octopus in enumerate(line):
            area[x, y] = int(octopus)
    total_flashes = 0
    for i in range(steps):
        area, count_flashes = simulate_step(area)
        if count_flashes == 100:
            return i + 1
        total_flashes += count_flashes
    return total_flashes


def part1(lines):
    """
    >>> part1(load_example(__file__, "11"))
    1656
    """
    return simulate(lines, 100)


def part2(lines):
    """
    >>> part2(load_example(__file__, "11"))
    195
    """
    return simulate(lines, 1000)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "11")
    print(part1(data))
    print(part2(data))
