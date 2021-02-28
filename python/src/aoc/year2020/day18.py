from aoc.util import load_input


def calc(a, op, b):
    if op == "+":
        return a + b
    if op == "*":
        return a * b
    raise Exception


def solve_part1(expression, index=0):
    """
    >>> solve_part1('1 + 2 * 3 + 4 * 5 + 6')
    71
    >>> solve_part1('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> solve_part1('2 * 3 + (4 * 5)')
    26
    >>> solve_part1('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    437
    >>> solve_part1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    12240
    >>> solve_part1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    13632
    """
    result, op = 0, "+"
    while index < len(expression):
        t = expression[index]
        index += 1
        if t.isspace():
            continue
        if t.isdigit():
            result = calc(result, op, int(t))
        if t == "+":
            op = "+"
        if t == "*":
            op = "*"
        if t == "(":
            value, index = solve_part1(expression, index)
            result = calc(result, op, value)
        if t == ")":
            return result, index
    return result


PRECEDENCE = {"+": 3, "*": 2}


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
        if token in ["+", "*"]:
            while (
                stack
                and stack[-1] in ["+", "*"]
                and PRECEDENCE[token] <= PRECEDENCE[stack[-1]]
            ):
                result.append(stack.pop())
            stack.append(token)
        if token == "(":
            stack.append(token)
        if token == ")":
            while stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
    while stack:
        if stack[-1] == ")":
            raise
        result.append(stack.pop())
    return result


def evaluate(upn_stack):
    stack = []
    for token in upn_stack:
        if token.isdigit():
            stack.append(int(token))
        elif token in "+*":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(calc(p1, token, p2))
        else:
            raise Exception
    return stack.pop()


def solve_part2(expression):
    """
    >>> solve_part2('1 + 2 * 3 + 4 * 5 + 6')
    231
    >>> solve_part2('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> solve_part2('2 * 3 + (4 * 5)')
    46
    >>> solve_part2('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    1445
    >>> solve_part2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    669060
    >>> solve_part2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    23340
    """
    upn_stack = shunting_yard(expression)
    return evaluate(upn_stack)


def run(lines, solve):
    return sum(solve(line.strip()) for line in lines)


def part1(lines):
    return run(lines, solve_part1)


def part2(lines):
    return run(lines, solve_part2)


if __name__ == "__main__":
    data = load_input(__file__, 2020, "18")
    print(part1(data))
    print(part2(data))
