from collections import Counter

from aoc.util import load_input, load_example


def read_data(lines):
    template = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        pair, _, result = line.strip().split()
        rules[pair] = result
    return template, rules


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
    template, rules = read_data(lines)
    target_length = calc_target_length(len(template), 10)
    counts = Counter(calc_letter(template, rules, i) for i in range(target_length))
    only_counts = list(count for _, count in counts.most_common())
    return only_counts[0] - only_counts[-1]


def part2(lines):
    """
    >>> part2(load_example(__file__, "14"))
    2188189693529
    """
    template, rules = read_data(lines)
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2021, "14")
    assert part1(load_example(__file__, "14")) == 1588
    print(part1(data))
    assert part2(load_example(__file__, "14")) == 2188189693529
    print(part2(data))
