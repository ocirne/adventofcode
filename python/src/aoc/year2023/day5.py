from aoc.util import load_input, load_example

# https://github.com/PyCQA/flake8/issues/316
# flake8: noqa


class UseType:
    def __init__(self, line):
        self.destination_range_start, self.source_range_start, self.range_length = map(int, line.split())
        self.destination_range_end = self.destination_range_start + self.range_length
        self.source_range_end = self.source_range_start + self.range_length

    def __str__(self):
        return "%s -> %s" % (self.source_range(), self.destination_range())

    def destination_range(self):
        return self.destination_range_start, self.destination_range_end

    def source_range(self):
        return self.source_range_start, self.source_range_end


def read_almanac(lines):
    it = iter(lines)
    seeds = [int(s) for s in next(it).split(":")[1].split()]
    next(it)
    almanac = []
    try:
        while it:
            # use type name
            next(it)
            use_types = []
            while (line := next(it)) != "":
                use_types.append(UseType(line))
            almanac.append(use_types)
    except StopIteration:
        almanac.append(use_types)
    return seeds, almanac


def map_category(use_types, value):
    for use_type in use_types:
        if use_type.source_range_start <= value < use_type.source_range_start + use_type.range_length:
            return use_type.destination_range_start + value - use_type.source_range_start
    return value


def map_seed(almanac, seed):
    value = seed
    for use_types in almanac:
        value = map_category(use_types, value)
    return value


def part1(lines):
    """
    >>> part1(load_example(__file__, "5"))
    35
    """
    seeds, almanac = read_almanac(lines)
    return min(map_seed(almanac, seed) for seed in seeds)


class UseType2:
    def __init__(self, start, end, delta):
        self.start = start
        self.end = end
        self.delta = delta

    def __str__(self):
        return "%s:%s -> %s:%s" % (self.start, self.end, self.start + self.delta, self.end + self.delta)

    def __lt__(self, other):
        return self.start < other.start


def improved_almanac(lines):
    """
    use type (98, 100) -> (50, 52)
    use type (50, 98) -> (52, 100)
    ->
    -oo .. 50 -> delta 0
    50 .. 98 -> delta +2
    98 .. 100 -> delta -48
    100 .. oo -> delta 0
    """
    it = iter(lines)
    seeds = [int(s) for s in next(it).split(":")[1].split()]
    next(it)
    almanac = []
    try:
        while it:
            # use type name
            next(it)
            use_types = []
            while (line := next(it)) != "":
                destination_range_start, source_range_start, range_length = map(int, line.split())
                source_range_end = source_range_start + range_length
                delta = destination_range_start - source_range_start
                use_types.append(UseType2(source_range_start, source_range_end, delta))
            almanac.append(use_types)
    except StopIteration:
        almanac.append(use_types)
    almanac2 = []
    for u in almanac:
        t = sorted(u)
        use_type2 = []
        use_type2.append(UseType2(-1, t[0].start, 0))
        for i, f in enumerate(t):
            use_type2.append(f)
            if i + 1 < len(t) and t[i].end < t[i + 1].start:
                use_type2.append(UseType2(t[i].end, t[i + 1].start, 0))
        use_type2.append(UseType2(t[-1].end, 10000000000, 0))
        almanac2.append(use_type2)
    return seeds, almanac2


class Foo:
    def __init__(self, almanac):
        self.almanac = almanac

    def foo(self, range_start, range_end, depth=0):
        #        print('--')
        #        print('call depth', depth, 'start', range_start, 'end', range_end)
        if depth >= len(self.almanac):
            return range_start

        best_value = 100000000000000000
        for use_type in self.almanac[depth]:
            #           print('check use type', use_type)
            if range_start >= use_type.end:
                continue
            if range_end < use_type.start:
                break
            #            print('try', depth, use_type, '|', range_start, range_end, 'delta', use_type.delta)
            tmp = self.foo(
                max(range_start + use_type.delta, use_type.start + use_type.delta),
                min(range_end + use_type.delta, use_type.end + use_type.delta),
                depth + 1,
            )
            best_value = min(tmp, best_value)
        return best_value


def part2(lines):
    """
    >>> part2(load_example(__file__, "5"))
    46
    """
    seeds, almanac = improved_almanac(lines)
    result = 10000000000000
    for i in range(0, len(seeds), 2):
        s1, s2 = seeds[i : i + 2]
        foo = Foo(almanac)
        result = min(result, foo.foo(s1, s1 + s2))
    return result


if __name__ == "__main__":
    data = load_input(__file__, 2023, "5")
    print(part1(data))
    print(part2(data))
