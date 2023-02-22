from aoc.util import load_input, load_example


directions = {"R": 1, "U": 1j, "L": -1, "D": -1j}


def part1(lines):
    """
    >>> part1(load_example(__file__, "9a"))
    .
    """
    h = 0j
    t = 0j
    visited = set()
    visited.add(t)
    for line in lines:
        direction, count = line.split()
        for _ in range(int(count)):
            h += directions[direction]
            if abs(h - t) < 2:
                continue
            u = h - ((h - t) / abs(t - h))
            r = complex(round(u.real), round(u.imag))
            print("h", h, "t", t, "h-t", h - t, "u", u, "r", r, "-->", h - r)
            t = r
            visited.add(t)
    return len(visited)


def part2(lines):
    """
    >>> part2(load_example(__file__, "9b"))
    36
    """
    rope = [0j for _ in range(10)]
    visited = set()
    visited.add(rope[9])
    for line in lines:
        direction, count = line.split()
        for _ in range(int(count)):
            rope[0] += directions[direction]
            for i in range(1, 10):
                h = rope[i - 1]
                t = rope[i]
                if abs(h - t) < 2:
                    continue
                u = h - ((h - t) / abs(t - h))
                rope[i] = complex(round(u.real), round(u.imag))
            visited.add(rope[9])
    return len(visited)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "9")
    #    data = load_example(__file__, "9b")
    #    print(part1(data))
    print(part2(data))
