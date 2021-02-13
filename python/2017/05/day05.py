from pathlib import Path


def part1(offset):
    return offset + 1


def part2(offset):
    if offset < 3:
        return offset + 1
    return offset - 1


def run(filename, offset_mod):
    """
    >>> run(Path(__file__).parent / 'reference', part1)
    5
    >>> run(Path(__file__).parent / 'reference', part2)
    10
    """
    instructions = [int(line) for line in open(filename, 'r').readlines()]
    count = 1
    p = 0
    while True:
        jump = instructions[p]
        instructions[p] = offset_mod(instructions[p])
        p += jump
        if not 0 <= p < len(instructions):
            return count
        count += 1


if __name__ == '__main__':
    print(run('input', part1))
    print(run('input', part2))
