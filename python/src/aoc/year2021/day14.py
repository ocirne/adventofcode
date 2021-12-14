from collections import Counter

from aoc.util import load_input, load_example


def read_data(lines):
    template = lines[0].strip()
    rules = {}
    letters = set()
    for line in lines[2:]:
        pair, _, result = line.strip().split()
        rules[pair] = result
        letters.add(result)
    return template, rules, list(letters)


def calc_target_length(template_length, rounds):
    x = template_length
    for i in range(rounds):
        x = x * 2 - 1
    return x


def calc_letter(template, rules, i, depth=10):
    if depth == 0:
        return template[i]
    if i % 2 == 0:
        return calc_letter(template, rules, i // 2, depth - 1)
    else:
        left = calc_letter(template, rules, (i - 1) // 2, depth - 1)
        right = calc_letter(template, rules, (i + 1) // 2, depth - 1)
        return rules[left + right]


def part1(lines):
    """
    >>> part1(load_example(__file__, "14"))
    1588
    """
    template, rules, _ = read_data(lines)
    target_length = calc_target_length(len(template), 10)
    counts = Counter(calc_letter(template, rules, i) for i in range(target_length))
    only_counts = list(count for _, count in counts.most_common())
    return only_counts[0] - only_counts[-1]


def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    2188189693529

    NN
    d.h. NN:0 = N + N

    NCN  (NN -> C)
    d.h. NN:1 enthält 1 C bzw. N + (NN:1) + N

    NBCCN (NC -> B, CN -> C)
    d.h. NN:2 enthält: N + (NC:1) + C + (CN:1) + N = N + (NN:2) + N
    NN:2 = NC:1 + C + CN:1

    NN:3 = N + (NC:2) + C + (CN:2) + N = N + (NN:3) + N
    NN:3 = (NC:2) + C + (CN:2)

    XZ:n = (XY:n-1) + Y + (YZ:n-1), wenn XZ -> Y
    """
    template, base_rules, letters = read_data(lines)
    rules = {}
    for (x, y), result in base_rules.items():
        rules[x, y, 1] = Counter({result: 1})
    for n in range(2, 41):
        for (x, z), y in base_rules.items():
            rules[x, z, n] = rules[x, y, n - 1] + Counter({y: 1}) + rules[y, z, n - 1]
    print(rules["N", "N", 10])
    result = Counter(template)
    for i in range(len(template) - 1):
        x, y = template[i : i + 2]
        result += rules[x, y, 40]
    only_counts = list(count for _, count in result.most_common())
    print(only_counts)
    return only_counts[0] - only_counts[-1]


if __name__ == "__main__":
    data = load_input(__file__, 2021, "14")
    assert part1(load_example(__file__, "14")) == 1588
    print(part1(data))
    assert part2(load_example(__file__, "14")) == 2188189693529
    print(part2(data))
