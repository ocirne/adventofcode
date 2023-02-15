from functools import reduce
from statistics import median

from aoc.util import load_input, load_example

BRACKETS = {"(": ")", "[": "]", "{": "}", "<": ">"}

syntax_checker_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_single_score = {")": 1, "]": 2, "}": 3, ">": 4}


def autocomplete_score(missing):
    return reduce(lambda score, c: 5 * score + autocomplete_single_score[c], missing, 0)


def match_brackets(expression):
    """
    >>> match_brackets('[({(<(())[]>[[{[]{<()<>>')
    ('incomplete', '}}]])})]', 288957)
    >>> match_brackets('[(()[<>])]({[<{<<[]>>(')
    ('incomplete', ')}>]})', 5566)
    >>> match_brackets('{([(<{}[<>[]}>{[]{[(<()>')
    ('invalid', '}', 1197)
    >>> match_brackets('(((({<>}<{<{<>}{[]{[]{}')
    ('incomplete', '}}>}>))))', 1480781)
    >>> match_brackets('[[<[([]))<([[{}[[()]]]')
    ('invalid', ')', 3)
    >>> match_brackets('[{[{({}]{}}([{[{{{}}([]')
    ('invalid', ']', 57)
    >>> match_brackets('{<[[]]>}<{[{[{[]{()[[[]')
    ('incomplete', ']]}}]}]}>', 995444)
    >>> match_brackets('[<(<(<(<{}))><([]([]()')
    ('invalid', ')', 3)
    >>> match_brackets('<{([([[(<>()){}]>(<<{{')
    ('invalid', '>', 25137)
    >>> match_brackets('<{([{{}}[<[[[<>{}]]]>[]]')
    ('incomplete', '])}>', 294)
    """
    stack = []
    for c in expression:
        if c in BRACKETS:
            stack.append(c)
        else:
            for opening, closing in BRACKETS.items():
                if c == closing and stack[-1] != opening:
                    return "invalid", closing, syntax_checker_score[closing]
            stack.pop()
    missing = "".join(BRACKETS[c] for c in reversed(stack))
    return "incomplete", missing, autocomplete_score(missing)


def handle_lines(lines):
    for line in lines:
        yield match_brackets(line)


def part1(lines):
    """
    >>> part1(load_example(__file__, "10"))
    26397
    """
    return sum(score for code, _, score in handle_lines(lines) if code == "invalid")


def part2(lines):
    """
    >>> part2(load_example(__file__, "10"))
    288957
    """
    return median(score for code, _, score in handle_lines(lines) if code == "incomplete")


if __name__ == "__main__":
    data = load_input(__file__, 2021, "10")
    print(part1(data))
    print(part2(data))
