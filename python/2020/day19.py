import re
from pathlib import Path


def read_file(filename):
    rules = {}
    messages = []
    f = open(filename)
    line = f.readline()
    while not line.isspace():
        rule_no, rule_desc = line.split(':')
        rules[rule_no] = rule_desc.strip().replace('"', '')
        line = f.readline()
    line = f.readline()
    while line:
        messages.append(line.strip())
        line = f.readline()
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


def run(filename):
    """
    >>> run(Path(__file__).parent / 'reference_a')
    2
    >>> run(Path(__file__).parent / 'reference_b')
    12
    """
    rules, messages = read_file(filename)
    pattern = create_regex(rules)
    total = 0
    for message in messages:
        if re.match(pattern, message):
            total += 1
    return total


if __name__ == '__main__':
    print(run('input_a'))
    print(run('input_b'))
