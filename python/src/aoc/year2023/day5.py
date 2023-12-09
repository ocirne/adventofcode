import sys

from aoc.util import load_input, load_example

# https://github.com/PyCQA/flake8/issues/316
# flake8: noqa

MAX = sys.maxsize


class UseType:
    def __init__(self, start, end, delta):
        self.start = start
        self.end = end
        self.delta = delta

    def __lt__(self, other):
        return self.start < other.start


class Almanac:
    def __init__(self, lines):
        self.seeds, self.almanac = self.read_almanac(lines)

    @staticmethod
    def read_almanac(lines):
        """
        50 98 2
        52 50 48
        ->
        use type (98, 100) -> (50, 52), delta -48
        use type (50, 98) -> (52, 100), delta +2
        ->
        -oo .. 50 -> delta 0
        50 .. 98 -> delta +2
        []
        98 .. 100 -> delta -48
        100 .. oo -> delta 0
        """
        it = iter(lines)
        seeds = [int(s) for s in next(it).split(":")[1].split()]
        next(it)
        almanac = []
        try:
            while it:
                # ignore type name
                next(it)
                use_types = []
                while (line := next(it)) != "":
                    destination_range_start, source_range_start, range_length = map(int, line.split())
                    source_range_end = source_range_start + range_length
                    delta = destination_range_start - source_range_start
                    use_types.append(UseType(source_range_start, source_range_end, delta))
                almanac.append(use_types)
        except StopIteration:
            almanac.append(use_types)
        almanac_all_ranges = []
        for u in almanac:
            t = sorted(u)
            use_type = []
            use_type.append(UseType(-1, t[0].start, 0))
            for i, f in enumerate(t):
                use_type.append(f)
                if i + 1 < len(t) and t[i].end < t[i + 1].start:
                    use_type.append(UseType(t[i].end, t[i + 1].start, 0))
            use_type.append(UseType(t[-1].end, MAX, 0))
            almanac_all_ranges.append(use_type)
        return seeds, almanac_all_ranges

    def find_location(self, range_start, range_end, depth=0):
        if depth >= len(self.almanac):
            return range_start
        best_value = MAX
        for use_type in self.almanac[depth]:
            if range_start >= use_type.end:
                continue
            if range_end < use_type.start:
                break
            tmp = self.find_location(
                max(range_start + use_type.delta, use_type.start + use_type.delta),
                min(range_end + use_type.delta, use_type.end + use_type.delta),
                depth + 1,
            )
            best_value = min(tmp, best_value)
        return best_value


def pairs(a):
    for i in range(0, len(a), 2):
        yield a[i : i + 2]


def part1(lines):
    """
    >>> part1(load_example(__file__, "5"))
    35
    """
    almanac = Almanac(lines)
    return min(almanac.find_location(seed, seed + 1) for seed in almanac.seeds)


def part2(lines):
    """
    >>> part2(load_example(__file__, "5"))
    46
    """
    almanac = Almanac(lines)
    return min(almanac.find_location(start, start + length) for start, length in pairs(almanac.seeds))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "5")
    print(part1(data))
    print(part2(data))
