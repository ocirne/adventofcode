from functools import lru_cache

from aoc.util import load_input, load_example


class CachedDP:
    def __init__(self, springs, pattern):
        self.springs = springs
        self.pattern = pattern

    @lru_cache
    def dot(self, si, pi):
        return self.rec(si + 1, pi)

    @lru_cache
    def spring(self, si, pi):
        p = self.pattern[pi]
        if si + p > len(self.springs):
            return 0
        for i in range(p):
            if self.springs[si + i] == ".":
                return 0
        if si + p < len(self.springs) and self.springs[si + p] == "#":
            return 0
        return self.rec(si + p + 1, pi + 1)

    @lru_cache
    def rec(self, si: int = 0, pi: int = 0):
        if all(s != "#" for s in self.springs[si:]) and pi >= len(self.pattern):
            return 1
        if si >= len(self.springs) or pi >= len(self.pattern):
            return 0
        total = 0
        c = self.springs[si]
        if c == ".":
            total += self.dot(si, pi)
        elif c == "#":
            total += self.spring(si, pi)
        elif c == "?":
            total += self.dot(si, pi) + self.spring(si, pi)
        return total


def count_arrangements(springs, pattern):
    cached_dp = CachedDP(springs, [int(n) for n in pattern.split(",")])
    return cached_dp.rec()


def part1(lines):
    """
    >>> part1(load_example(__file__, "12"))
    21
    """
    return sum(count_arrangements(*line.split()) for line in lines)


def part2(lines):
    """
    >>> part2(load_example(__file__, "12"))
    525152
    """
    total = 0
    for line in lines:
        springs, pattern = line.split()
        five_springs = "?".join(5 * [springs])
        five_pattern = ",".join(5 * [pattern])
        total += count_arrangements(five_springs, five_pattern)
    return total


if __name__ == "__main__":
    data = load_input(__file__, 2023, "12")
    print(part1(data))
    print(part2(data))
