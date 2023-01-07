import re

from aoc.util import load_input, load_example

MOVE_PATTERN = re.compile(r"^move (\d+) from (\d+) to (\d+)$")


def move_crates_single(stacks, crates, source, target):
    for _ in range(crates):
        tmp = stacks[source - 1].pop(0)
        stacks[target - 1].insert(0, tmp)


def move_crates_multiple(stacks, crates, source, target):
    tmp_stack = []
    for _ in range(crates):
        tmp = stacks[source - 1].pop(0)
        tmp_stack.insert(0, tmp)
    for _ in range(crates):
        tmp = tmp_stack.pop(0)
        stacks[target - 1].insert(0, tmp)


def move_crates(lines, count, move_crates_fun):
    stacks = [[] for _ in range(count)]
    for line in lines:
        if not line.strip().startswith("["):
            break
        for i in range(count):
            if 1 + 4 * i < len(line):
                c = line[1 + 4 * i]
                if c.isalpha():
                    stacks[i].append(c)
    for line in lines:
        m = MOVE_PATTERN.match(line)
        if m:
            crates, source, target = map(int, m.groups())
            move_crates_fun(stacks, crates, source, target)
    return "".join(stacks[i][0] for i in range(count))


def part1(lines, count=9):
    """
    >>> part1(load_example(__file__, "5"), count=3)
    'CMZ'
    """
    return move_crates(lines, count, move_crates_single)


def part2(lines, count=9):
    """
    >>> part2(load_example(__file__, "5"), count=3)
    'MCD'
    """
    return move_crates(lines, count, move_crates_multiple)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "5")
    print(part1(data))
    print(part2(data))
