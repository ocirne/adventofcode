from aoc.util import load_input, load_example


POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

BRACKETS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def match_brackets(expression):
    """
    >>> match_brackets('[({(<(())[]>[[{[]{<()<>>')
    >>> match_brackets('{([(<{}[<>[]}>{[]{[(<()>')
    '}'
    >>> match_brackets('[[<[([]))<([[{}[[()]]]')
    ')'
    >>> match_brackets('[{[{({}]{}}([{[{{{}}([]')
    ']'
    >>> match_brackets('[<(<(<(<{}))><([]([]()')
    ')'
    >>> match_brackets('<{([([[(<>()){}]>(<<{{')
    '>'
    """
    stack = []
    for c in expression:
        if c in BRACKETS:
            stack.append(c)
        else:
            for opening, closing in BRACKETS.items():
                if c == closing and stack[-1] != opening:
                    return closing
            stack.pop()


def part1(lines):
    """
    >>> part1(load_example(__file__, "10"))
    26397
    """
    return sum(POINTS[c] for c in (match_brackets(line.strip()) for line in lines) if c is not None)


def part2(lines):
    """
    >>> part2(load_example(__file__, "10"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2021, "10")
    assert part1(load_example(__file__, "10")) == 26397
    print(part1(data))
#    print(part2(data))
