from aoc.util import load_example, load_input


def criterion_part1(offset):
    return offset + 1


def criterion_part2(offset):
    if offset < 3:
        return offset + 1
    return offset - 1


def run(lines, offset_mod):
    """
    >>> run(load_example(__file__, '5'), criterion_part1)
    5
    >>> run(load_example(__file__, '5'), criterion_part2)
    10
    """
    instructions = [int(line) for line in lines]
    count = 1
    p = 0
    while True:
        jump = instructions[p]
        instructions[p] = offset_mod(instructions[p])
        p += jump
        if not 0 <= p < len(instructions):
            return count
        count += 1


def part1(lines):
    return run(lines, criterion_part1)


def part2(lines):
    return run(lines, criterion_part2)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "5")
    print(part1(data))
    print(part2(data))
