
def calc(a, op, b):
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    raise Exception


def part1(expression, index=0):
    """
    >>> part1('1 + 2 * 3 + 4 * 5 + 6')
    71
    >>> part1('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> part1('2 * 3 + (4 * 5)')
    26
    >>> part1('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    437
    >>> part1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    12240
    >>> part1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    13632
    """
    result, op = 0, '+'
    while index < len(expression):
        t = expression[index]
        index += 1
        if t.isspace():
            continue
        if t.isdigit():
            result = calc(result, op, int(t))
        if t == '+':
            op = '+'
        if t == '*':
            op = '*'
        if t == '(':
            value, index = part1(expression, index)
            result = calc(result, op, value)
        if t == ')':
            return result, index
    return result


PRECEDENCE = {'+': 3, '*': 2}


def shunting_yard(expression):
    """ https://de.wikipedia.org/wiki/Shunting-yard-Algorithmus """
    stack = []
    result = []
    index = 0
    while index < len(expression):
        token = expression[index]
        index += 1
        if token.isspace():
            continue
        if token.isdigit():
            result.append(token)
        if token in ['+', '*']:
            while stack and stack[-1] in ['+', '*'] and PRECEDENCE[token] <= PRECEDENCE[stack[-1]]:
                result.append(stack.pop())
            stack.append(token)
        if token == '(':
            stack.append(token)
        if token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
    while stack:
        if stack[-1] == ')':
            raise
        result.append(stack.pop())
    return result


def evaluate(upn_stack):
    stack = []
    for token in upn_stack:
        if token.isdigit():
            stack.append(int(token))
        elif token in '+*':
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(calc(p1, token, p2))
        else:
            raise Exception
    return stack.pop()


def part2(expression):
    """
    >>> part2('1 + 2 * 3 + 4 * 5 + 6')
    231
    >>> part2('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> part2('2 * 3 + (4 * 5)')
    46
    >>> part2('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    1445
    >>> part2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    669060
    >>> part2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    23340
    """
    upn_stack = shunting_yard(expression)
    return evaluate(upn_stack)


def run(filename, solve):
    f = open(filename, 'r')
    return sum(solve(line.strip()) for line in f.readlines())


if __name__ == '__main__':
    print(run('input', part1))
    print(run('input', part2))
