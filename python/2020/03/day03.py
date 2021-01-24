from pathlib import Path


def read_data(filename):
    f = open(filename, 'r')
    return list(map(str.strip, f.readlines()))


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


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    7
    """
    lines = read_data(filename)
    return count_trees(lines, 3, 1)


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    336
    """
    lines = read_data(filename)
    a = count_trees(lines, 1, 1)
    b = count_trees(lines, 3, 1)
    c = count_trees(lines, 5, 1)
    d = count_trees(lines, 7, 1)
    e = count_trees(lines, 1, 2)
    return a*b*c*d*e


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
