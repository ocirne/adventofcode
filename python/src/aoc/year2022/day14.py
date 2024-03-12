from aoc.util import load_input, load_example


def foo(a, b):
    if a < b:
        return range(a, b+1)
    return range(b, a + 1)

def part1(lines):
    """
    >>> part1(load_example(__file__, "14"))
    24
    """
    cave = {}
    for line in lines:
        pairs = [tuple(map(int, pair.split(','))) for pair in line.split(' -> ')]
        cx, cy = pairs[0]
        for nx, ny in pairs:
            for x in foo(cx, nx):
                for y in foo(cy, ny):
                    cave[x, y] = '#'
            cx, cy = nx, ny
    for y in range(10):
        for x in range(494, 504):
            print(cave.get((x, y), '.'), end='')
        print()

    count = 0
    while True:
        sx, sy = 500, 0
        while True:
            if sy > 1000:
                return count
            if (sx, sy+1) not in cave:
                sy += 1
            elif (sx - 1, sy+1) not in cave:
                sx, sy = sx - 1, sy + 1
            elif (sx + 1, sy+1) not in cave:
                sx, sy = sx + 1, sy + 1
            else:
                cave[sx, sy] = 'o'
                count += 1
                break

        print('---')
        for y in range(10):
            for x in range(494, 504):
                print(cave.get((x, y), '.'), end='')
            print()

def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    93
    """
    cave = {}
    for line in lines:
        pairs = [tuple(map(int, pair.split(','))) for pair in line.split(' -> ')]
        cx, cy = pairs[0]
        for nx, ny in pairs:
            for x in foo(cx, nx):
                for y in foo(cy, ny):
                    cave[x, y] = '#'
            cx, cy = nx, ny
    floor_y = max(y for _, y in cave) + 2
    for y in range(10):
        for x in range(494, 504):
            print(cave.get((x, y), '.'), end='')
        print()

    count = 0
    while True:
        sx, sy = 500, 0
        while True:
            if sy + 1 == floor_y:
                cave[sx, sy] = 'o'
                count += 1
                break
            elif (sx, sy+1) not in cave:
                sy += 1
            elif (sx - 1, sy+1) not in cave:
                sx, sy = sx - 1, sy + 1
            elif (sx + 1, sy+1) not in cave:
                sx, sy = sx + 1, sy + 1
            else:
                cave[sx, sy] = 'o'
                count += 1
                if (sx, sy) == (500, 0):
                    return count
                break

        print('---')
        for y in range(10):
            for x in range(494, 504):
                print(cave.get((x, y), '.'), end='')
            print()


if __name__ == "__main__":
    data = load_input(__file__, 2022, "14")
#    data = load_example(__file__, "14")
#    print(part1(data))
    print(part2(data))
