from aoc.util import load_input, load_example


directions = {"R": 1, "U": 1j, "L": -1, "D": -1j}


def simulate_rope(lines, knots):
    rope = [0j for _ in range(knots)]
    visited = {rope[knots - 1]}
    for line in lines:
        direction, count = line.split()
        for _ in range(int(count)):
            rope[0] += directions[direction]
            for i in range(1, knots):
                h = rope[i - 1]
                t = rope[i]
                if abs(h - t) < 2:
                    continue
                u = h - ((h - t) / abs(h - t))
                rope[i] = complex(round(u.real), round(u.imag))
            visited.add(rope[knots - 1])
    return len(visited)


def part1(lines):
    """
    >>> part1(load_example(__file__, "9a"))
    13
    """
    return simulate_rope(lines, 2)


def part2(lines):
    """
    >>> part2(load_example(__file__, "9b"))
    36
    """
    return simulate_rope(lines, 10)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "9")
    print(part1(data))
    print(part2(data))
