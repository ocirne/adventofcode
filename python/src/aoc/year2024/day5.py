from aoc.util import load_input, load_example

from functools import cmp_to_key


def is_valid(rules, line):
    for r1, r2 in rules:
        p1 = line.find(r1)
        p2 = line.find(r2)
        if p1 != -1 and p2 != -1 and p1 > p2:
            return False
    return True


def create_rules_comparator(rules):
    def rules_cmp(a, b):
        if (a, b) in rules:
            return -1
        if (b, a) in rules:
            return 1
        return 0
    return rules_cmp


def part1(lines):
    """
    >>> part1(load_example(__file__, "5"))
    143
    """
    rules = []
    iter_lines = iter(lines)
    while True:
        line = next(iter_lines).strip()
        if line == '':
            break
        rules.append(tuple(line.split('|')))

    total = 0
    for line in iter_lines:
        if is_valid(rules, line):
            token = line.split(',')
            total += int(token[(len(token) - 1) // 2])
    return total


def part2(lines):
    """
    >>> part2(load_example(__file__, "5"))
    123
    """
    rules = []
    iter_lines = iter(lines)
    while True:
        line = next(iter_lines).strip()
        if line == '':
            break
        rules.append(tuple(line.split('|')))
    rules_cmp = create_rules_comparator(rules)
    total = 0
    for line in iter_lines:
        if not is_valid(rules, line):
            token = line.strip().split(',')
            correct = sorted(token, key=cmp_to_key(rules_cmp))
            total += int(correct[(len(correct) - 1) // 2])
    return total


if __name__ == "__main__":
    data = load_input(__file__, 2024, "5")
    print(part1(data))
    print(part2(data))
