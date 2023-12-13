from aoc.util import load_input, load_example

# https://github.com/PyCQA/flake8/issues/316
# flake8: noqa


def read_patterns(lines):
    it = iter(lines)
    try:
        while it:
            pattern = []
            while (row := next(it)) != "":
                pattern.append(row)
            yield pattern
    except StopIteration:
        yield pattern


def transform_pattern(pattern):
    result = ["" for _ in range(len(pattern[0]))]
    for row in pattern:
        for x, c in enumerate(row):
            result[x] += c
    return result


def is_reflection_row(pattern, r):
    for i in range(len(pattern)):
        if r - i < 0:
            return i > 0
        if r + i + 1 >= len(pattern):
            return i > 0
        if pattern[r - i] != pattern[r + i + 1]:
            return False
    return True


def count_reflected_rows(pattern):
    for r in range(len(pattern)):
        if is_reflection_row(pattern, r):
            return r + 1
    return 0


def part1(lines):
    """
    >>> part1(load_example(__file__, "13"))
    405
    """
    total = 0
    for pattern in read_patterns(lines):
        total += 100 * count_reflected_rows(pattern)
        total += count_reflected_rows(transform_pattern(pattern))
    return total


def part2(lines):
    """
    >>> part2(load_example(__file__, "13"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "13")
    # data = load_example(__file__, "13")
    print(part1(data))
    # print(part2(data))
