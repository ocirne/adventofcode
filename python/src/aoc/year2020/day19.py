import re
from aoc.util import load_example, load_input


def prepare_data(lines, is_part2):
    rules = {}
    messages = []
    f = iter(lines)
    line = next(f)
    while not line.isspace():
        rule_no, rule_desc = line.split(':')
        rules[rule_no] = rule_desc.strip().replace('"', '')
        line = next(f)
    for line in f:
        messages.append(line.strip())
    if is_part2:
        rules['8'] = '42 | 42 8'
        rules['11'] = '42 31 | 42 11 31'
    return rules, messages


def rec_create_regex(rules, no, depth):
    if depth > 4:
        return ''
    regex = ''
    for token in rules[no].split(' '):
        if token == '|':
            regex += token
        elif token.isalpha():
            return token
        else:
            if no == token:
                regex += rec_create_regex(rules, token, depth + 1)
            else:
                regex += rec_create_regex(rules, token, 0)
    return '(' + regex + ')'


def create_regex(rules):
    regex = rec_create_regex(rules, '0', 0)
    return r'^' + regex + '$'


def run(lines, is_part2):
    """
    >>> run(load_example(__file__, '19a'), False)
    2
    >>> run(load_example(__file__, '19b'), True)
    12
    """
    rules, messages = prepare_data(lines, is_part2)
    pattern = create_regex(rules)
    total = 0
    for message in messages:
        if re.match(pattern, message):
            total += 1
    return total


def part1(lines):
    return run(lines, False)


def part2(lines):
    return run(lines, True)


if __name__ == "__main__":
    data = load_input(__file__, 2020, '19')
    print(part1(data))
    print(part2(data))
