from typing import Generator

from aoc.util import load_input, load_example

# https://github.com/PyCQA/flake8/issues/316
# flake8: noqa


class MirrorPattern:
    def __init__(self, lines):
        self.w, self.h = len(lines[0]), len(lines)
        self.d = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                self.d[x, y] = c

    @staticmethod
    def is_reflection_line(lines, r):
        for i in range(len(lines)):
            if r - i - 1 < 0 or r + i >= len(lines):
                return i > 0
            if lines[r - i - 1] != lines[r + i]:
                return False
        return True

    def count_reflected_rows(self, forbidden=None):
        rows = ["".join(self.d[x, y] for x in range(self.w)) for y in range(self.h)]
        for i in range(1, self.h + 1):
            if self.is_reflection_line(rows, i) and i != forbidden:
                return i
        return 0

    def count_reflected_columns(self, forbidden=None):
        columns = ["".join(self.d[x, y] for y in range(self.h)) for x in range(self.w)]
        for i in range(1, self.w + 1):
            if self.is_reflection_line(columns, i) and i != forbidden:
                return i
        return 0

    def cleaned_patterns(self):
        for x in range(self.w):
            for y in range(self.h):
                o, self.d[x, y] = self.d[x, y], "." if self.d[x, y] == "#" else "#"
                yield
                self.d[x, y] = o

    def part1(self):
        r = self.count_reflected_rows()
        c = self.count_reflected_columns()
        return 100 * r + c

    def part2(self):
        orig_r = self.count_reflected_rows()
        orig_c = self.count_reflected_columns()
        for _ in self.cleaned_patterns():
            r = self.count_reflected_rows(orig_r)
            c = self.count_reflected_columns(orig_c)
            if r != 0 or c != 0:
                return 100 * r + c


def read_patterns(lines: str) -> Generator[MirrorPattern, None, None]:
    it = iter(lines)
    pattern = None
    try:
        while it:
            pattern = []
            while (row := next(it)) != "":
                pattern.append(row)
            yield MirrorPattern(pattern)
    except StopIteration:
        yield MirrorPattern(pattern)


def part1(lines):
    """
    >>> part1(load_example(__file__, "13"))
    405
    """
    return sum(pattern.part1() for pattern in read_patterns(lines))


def part2(lines):
    """
    >>> part2(load_example(__file__, "13"))
    400
    """
    return sum(pattern.part2() for pattern in read_patterns(lines))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "13")
    print(part1(data))
    print(part2(data))
