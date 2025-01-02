from aoc.util import load_input, load_example


def check_part1(t):
    d = [a - b for a, b in zip(t[:-1], t[1:])]
    if not (all(x > 0 for x in d) or all(x < 0 for x in d)):
        return False
    return all(1 <= abs(x) <= 3 for x in d)


def check_part2(t):
    if check_part1(t):
        return True
    return any(check_part1(t[:i] + t[i + 1 :]) for i in range(len(t)))


def count_safe_reports(lines, f):
    return sum(f(list(map(int, line.split()))) for line in lines)


def part1(lines):
    """
    >>> part1(load_example(__file__, "2"))
    2
    """
    return count_safe_reports(lines, check_part1)


def part2(lines):
    """
    >>> part2(load_example(__file__, "2"))
    4
    """
    return count_safe_reports(lines, check_part2)


if __name__ == "__main__":
    data = load_input(__file__, 2024, "2")
    print(part1(data))
    print(part2(data))
