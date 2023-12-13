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


def count_reflected_rows(pattern, forbidden=None):
    for r in range(len(pattern)):
        if is_reflection_row(pattern, r) and r + 1 != forbidden:
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


def replacements(pattern):
    w, h = len(pattern[0]), len(pattern)
    d = {}
    for y, row in enumerate(pattern):
        for x, c in enumerate(row):
            d[x, y] = c
    for x in range(w):
        for y in range(h):
            o = d[x, y]
            d[x, y] = "." if d[x, y] == "#" else "#"
            result = ["".join(d[ix, iy] for ix in range(w)) for iy in range(h)]
            d[x, y] = o
            yield x, y, result


def foo(pattern):
    # print(pattern)
    o_rows = count_reflected_rows(pattern)
    o_cols = count_reflected_rows(transform_pattern(pattern))
    for x, y, smudge_pattern in replacements(pattern):
        #        print(x, y, smudge_pattern)
        s_rows = count_reflected_rows(smudge_pattern, o_rows)
        s_cols = count_reflected_rows(transform_pattern(smudge_pattern), o_cols)
        #            print('x', x, 'y', y, 'r', s_rows, 'c', s_cols)
        if s_rows is not None and s_rows > 0 and s_rows != o_rows:
            return 100 * s_rows
        if s_cols is not None and s_cols > 0 and s_cols != o_cols:
            return s_cols


def part2(lines):
    """
    >>> part2(load_example(__file__, "13"))
    400
    """
    return sum(foo(pattern) for pattern in read_patterns(lines))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "13")
    print(part1(data))
    print(part2(data))
