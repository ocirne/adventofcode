from collections import Counter

from aoc.util import load_input, load_example


def read_data(lines):
    template = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        pair, _, result = line.strip().split()
        rules[pair] = result
    return template, rules


def polymerize(template, base_rules, steps):
    """
    XZ:n = (XY:n-1) + Y + (YZ:n-1), XZ -> Y
    """
    rules = {}
    for (x, y), result in base_rules.items():
        rules[x, y, 0] = Counter({result: 1})
    for n in range(1, steps):
        for (x, z), y in base_rules.items():
            rules[x, z, n] = rules[x, y, n - 1] + Counter({y: 1}) + rules[y, z, n - 1]
    total_counts = Counter(template)
    for i in range(len(template) - 1):
        x, y = template[i : i + 2]
        total_counts += rules[x, y, steps - 1]
    only_counts = list(count for _, count in total_counts.most_common())
    return only_counts[0] - only_counts[-1]


def part1(lines):
    """
    >>> part1(load_example(__file__, "14"))
    1588
    """
    template, rules = read_data(lines)
    return polymerize(template, rules, 10)


def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    2188189693529
    """
    template, rules = read_data(lines)
    return polymerize(template, rules, 40)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "14")
    print(part1(data))
    print(part2(data))
