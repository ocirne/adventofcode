
import re


def readFile(filename):
    rules = {}
    messages = []
    f = open(filename)
    line = f.readline()
    while not line.isspace():
        ruleNo, ruleDesc = line.split(':')
        rules[ruleNo] = ruleDesc.strip().replace('"', '')
        line = f.readline()
    line = f.readline()
    while line:
        messages.append(line.strip())
        line = f.readline()
    return rules, messages


def recCreateRegex(rules, no):
    regex = ''
    for token in rules[no].split(' '):
        if token == '|':
            regex += token
        elif token.isalpha():
            return token
        else:
            regex += recCreateRegex(rules, token)
    return '(' + regex + ')'


def createRegex(rules):
    regex = recCreateRegex(rules, '0')
    return r'^' + regex + '$'


def run(filename):
    rules, messages = readFile(filename)
    pattern = createRegex(rules)
    total = 0
    for message in messages:
        if re.match(pattern, message):
            total += 1
    return total


assert run('reference_a') == 2

print(run('input_a'))

import re


def readFile(filename):
    rules = {}
    messages = []
    f = open(filename)
    line = f.readline()
    while not line.isspace():
        ruleNo, ruleDesc = line.split(':')
        rules[ruleNo] = ruleDesc.strip().replace('"', '')
        line = f.readline()
    line = f.readline()
    while line:
        messages.append(line.strip())
        line = f.readline()
    return rules, messages


def recCreateRegex(rules, no, depth):
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
                regex += recCreateRegex(rules, token, depth + 1)
            else:
                regex += recCreateRegex(rules, token, 0)
    return '(' + regex + ')'


def createRegex(rules):
    regex = recCreateRegex(rules, '0', 0)
    return r'^' + regex + '$'


def run(filename):
    rules, messages = readFile(filename)
    pattern = createRegex(rules)
    total = 0
    for message in messages:
        if re.match(pattern, message):
            total += 1
    return total


assert run('reference_b') == 12

print(run('input_b'))
