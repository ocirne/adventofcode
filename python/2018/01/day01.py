
def part1(data):
    """
    >>> part1([+1, +1, +1])
    3
    >>> part1([+1, +1, -2])
    0
    >>> part1([-1, -2, -3])
    -6
    """
    return sum(data)


def part2(data):
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
        for value in data:
            running_sum += value
            if running_sum in memory:
                return running_sum
            memory.add(running_sum)


if __name__ == "__main__":
    input_data = [int(line) for line in open('input', 'r').readlines()]
    print(part1(input_data))
    print(part2(input_data))
