from aoc.util import load_input


def part1(lines):
    """
    >>> part1([+1, +1, +1])
    3
    >>> part1([+1, +1, -2])
    0
    >>> part1([-1, -2, -3])
    -6
    """
    return sum(int(i) for i in lines)


def part2(lines):
    """
    >>> part2([+1, -1])
    0
    >>> part2([+3, +3, +4, -2, -4])
    10
    >>> part2([-6, +3, +8, +5, -6])
    5
    >>> part2([+7, +7, -2, -7, -4])
    14
    """
    running_sum = 0
    memory = {0}
    while True:
        for value in lines:
            running_sum += int(value)
            if running_sum in memory:
                return running_sum
            memory.add(running_sum)


if __name__ == "__main__":
    data = load_input(__file__, 2018, '1')
    print(part1(data))
    print(part2(data))
