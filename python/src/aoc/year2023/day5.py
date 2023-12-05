from aoc.util import load_input, load_example

# https://github.com/PyCQA/flake8/issues/316
# flake8: noqa


class UseType:
    def __init__(self, line):
        self.destination_range_start, self.source_range_start, self.range_length = map(int, line.split())


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


def part2(lines):
    """
    >>> part2(load_example(__file__, "5"))
    281
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2023, "5")
    #    data = load_example(__file__, "5")
    print(part1(data))
#    print(part2(data))
