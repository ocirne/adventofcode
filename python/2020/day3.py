from aoc_util import example


def prepare_data(lines):
    return list(map(str.strip, lines))


def count_trees(lines, right, down):
    max_x = len(lines[0])
    count = 0
    x = 0
    y = 0
    while y < len(lines):
        g = lines[y][x % max_x]
        if g == '#':
            count += 1
        x += right
        y += down
    return count


def part1(lines):
    """
    >>> part1(example('3'))
    7
    """
    data = prepare_data(lines)
    return count_trees(data, 3, 1)


def part2(lines):
    """
    >>> part2(example('3'))
    336
    """
    data = prepare_data(lines)
    a = count_trees(data, 1, 1)
    b = count_trees(data, 3, 1)
    c = count_trees(data, 5, 1)
    d = count_trees(data, 7, 1)
    e = count_trees(data, 1, 2)
    return a*b*c*d*e
