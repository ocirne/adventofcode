from aoc.util import load_input


def solve_captcha(line):
    """
    >>> solve_captcha('1122')
    3
    >>> solve_captcha('1111')
    4
    >>> solve_captcha('1234')
    0
    >>> solve_captcha('91212129')
    9
    """
    return sum(int(c) for i, c in enumerate(line) if line[i - 1] == c)


def part1(lines):
    return solve_captcha(lines[0])


def solve_new_captcha(line):
    """
    >>> solve_new_captcha('1212')
    6
    >>> solve_new_captcha('1221')
    0
    >>> solve_new_captcha('123425')
    4
    >>> solve_new_captcha('123123')
    12
    >>> solve_new_captcha('12131415')
    4
    """
    return sum(int(x) for x, y in zip(line, line[len(line) // 2 :] + line[: len(line) // 2]) if x == y)


def part2(lines):
    return solve_new_captcha(lines[0])


if __name__ == "__main__":
    data = load_input(__file__, 2017, "1")
    print(part1(data))
    print(part2(data))
