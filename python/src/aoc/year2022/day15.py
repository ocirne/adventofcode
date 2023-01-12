import re

from aoc.util import load_input, load_example

SENSOR_PATTERN = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")


def foo(lines, y):
    for line in lines:
        m = SENSOR_PATTERN.match(line)
        if m is None:
            continue
        sx, sy, bx, by = map(int, m.groups())
        #        if sy == y:
        #            print("sensor at %s, %s!" % (sx, sy))
        #        if by == y:
        #            print("beacon at %s, %s!" % (bx, by))
        md = abs(sx - bx) + abs(sy - by)
        t = md - abs(sy - y)
        if t < 0:
            continue
        a, b = sx - t, sx + t

        #        print("s", sx, sy, "b", bx, by, "md", md, "x", a, b + 1)
        yield a, b + 1


def merge(segments):
    if len(segments) <= 1:
        return segments
    rec = merge(segments[1:])
    if segments[0][1] < rec[0][0]:
        return [segments[0]] + rec
    else:
        # merge
        return [(segments[0][0], max(segments[0][1], rec[0][1]))] + rec[1:]


def part1(lines, y=2_000_000):
    """
    >>> part1(load_example(__file__, "15"), y=10)
    26
    """
    segments = sorted(foo(lines, y))
    segments = merge(merge(segments))
    total_length = sum(t - f for f, t in segments)
    # -1 for counting beacons by hand
    return total_length - 1


def part2(lines, m=4_000_000):
    """
    >>> part2(load_example(__file__, "15"), m=20)
    56000011
    """
    for y in range(m + 1):
        segments = sorted(foo(lines, y))
        segments = merge(merge(merge(segments)))
        if len(segments) > 1:
            x = segments[0][1]
            return x * 4000000 + y


if __name__ == "__main__":
    data = load_input(__file__, 2022, "15")
    print(part1(data))
    print(part2(data))
