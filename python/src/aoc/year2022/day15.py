import re

from aoc.util import load_input, load_example

SENSOR_PATTERN = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")


def read_segments(lines, y):
    for line in lines:
        m = SENSOR_PATTERN.match(line)
        if m is None:
            continue
        sx, sy, bx, by = map(int, m.groups())
        md = abs(sx - bx) + abs(sy - by)
        t = md - abs(sy - y)
        if t < 0:
            continue
        a, b = sx - t, sx + t
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
    segments = sorted(read_segments(lines, y))
    segments = merge(merge(segments))
    total_length = sum(t - f for f, t in segments)
    # -1 for counting beacons by hand
    return total_length - 1


class BeaconFinder:
    def __init__(self, lines):
        self.areas = list(self.read_areas(lines))

    @staticmethod
    def read_areas(lines):
        for line in lines:
            m = SENSOR_PATTERN.match(line)
            if m is None:
                continue
            sx, sy, bx, by = map(int, m.groups())
            md = abs(sx - bx) + abs(sy - by)
            yield sx, sy, md

    def exists_cover(self, x0, y0, x1, y1):
        """Eine Überdeckung existiert genau dann, wenn alle vier Ecken innerhalb einer area liegen"""
        for sx, sy, md in self.areas:
            md00 = abs(sx - x0) + abs(sy - y0)
            md01 = abs(sx - x0) + abs(sy - y1)
            md10 = abs(sx - x1) + abs(sy - y0)
            md11 = abs(sx - x1) + abs(sy - y1)
            if md00 <= md and md01 <= md and md10 <= md and md11 <= md:
                return True
        return False

    # Binäre Suche auf dem gesamten Raum
    def search_beacon(self, x0, y0, x1, y1):
        if self.exists_cover(x0, y0, x1, y1):
            return None
        if x0 == x1 and y0 == y1:
            return x0, y0
        if x0 > x1 or y0 > y1:
            return None
        if x1 - x0 > y1 - y0:
            xp = (x1 - x0) // 2
            t = self.search_beacon(x0, y0, x0 + xp, y1)
            if t is not None:
                return t
            if xp > 0:
                t = self.search_beacon(x0 + xp, y0, x1, y1)
                if t is not None:
                    return t
        else:
            yp = (y1 - y0) // 2
            t = self.search_beacon(x0, y0, x1, y0 + yp)
            if t is not None:
                return t
            if yp > 0:
                t = self.search_beacon(x0, y0 + yp, x1, y1)
                if t is not None:
                    return t


def part2(lines, m=4_000_000):
    """
    >>> part2(load_example(__file__, "15"), m=20)
    56000011
    """
    bf = BeaconFinder(lines)
    x, y = bf.search_beacon(0, 0, m, m)
    return x * 4000000 + y


if __name__ == "__main__":
    data = load_input(__file__, 2022, "15")
    print(part1(data))
    print(part2(data))
